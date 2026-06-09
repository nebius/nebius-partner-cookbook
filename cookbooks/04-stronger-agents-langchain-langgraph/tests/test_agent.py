"""Agent route tests. All upstream calls are mocked with respx — no network."""

from __future__ import annotations

import json

import httpx
import pytest
import respx
from fastapi.testclient import TestClient

from app.main import app


def _sse_chunk(data: dict[str, object]) -> bytes:
    return b"data: " + json.dumps(data).encode("utf-8") + b"\n\n"


def _build_completion_stream() -> bytes:
    chunks = [
        {"choices": [{"delta": {"content": "Hello"}, "index": 0}]},
        {"choices": [{"delta": {"content": " world"}, "index": 0}]},
        {"choices": [{"delta": {}, "index": 0, "finish_reason": "stop"}]},
        {
            "choices": [],
            "usage": {"prompt_tokens": 123, "completion_tokens": 45, "total_tokens": 168},
        },
    ]
    body = b"".join(_sse_chunk(c) for c in chunks) + b"data: [DONE]\n\n"
    return body


def _mock_nebius_stream() -> respx.Route:
    return respx.post("https://api.studio.nebius.ai/v1/chat/completions").mock(
        return_value=httpx.Response(
            200,
            content=_build_completion_stream(),
            headers={"content-type": "text/event-stream"},
        )
    )


@pytest.mark.asyncio
@respx.mock
async def test_agent_run_streams_tokens() -> None:
    nebius_route = _mock_nebius_stream()

    with TestClient(app) as client:
        with client.stream("POST", "/agent/run", json={"prompt": "say hi"}) as resp:
            assert resp.status_code == 200
            body = b"".join(resp.iter_bytes()).decode("utf-8")

    assert "event: status" in body
    assert '"phase": "routed"' in body
    assert '"route": "direct"' in body
    assert '"contextNeed": "direct_answer"' in body
    assert "event: token" in body
    assert "event: done" in body
    assert "Time:" in body
    assert "Tokens: 123 in, 45 out" in body
    assert "Cost: $" in body
    assert "Routing: direct / direct_answer" in body
    assert '"inputTokens": 123' in body
    assert '"outputTokens": 45' in body

    sent_body = json.loads(nebius_route.calls.last.request.content)
    assert sent_body["max_tokens"] == 384
    assert sent_body["temperature"] == 0.4
    assert sent_body["stream_options"] == {"include_usage": True}


@pytest.mark.asyncio
@respx.mock
async def test_agent_run_routes_latest_book_question_to_fresh_context() -> None:
    nebius_route = _mock_nebius_stream()

    with TestClient(app) as client:
        with client.stream(
            "POST",
            "/agent/run",
            json={
                "prompt": "What is the latest book written by Michel Houellebecq?",
                "temperature": 0.1,
                "max_tokens": 2048,
            },
        ) as resp:
            assert resp.status_code == 200
            body = b"".join(resp.iter_bytes()).decode("utf-8")

    assert '"route": "deliberate"' in body
    assert '"contextNeed": "fresh_publication_context"' in body
    assert "question depends on latest/current publication context" in body

    sent_body = json.loads(nebius_route.calls.last.request.content)
    assert sent_body["max_tokens"] == 700
    assert sent_body["temperature"] == 0.1
    assert sent_body["messages"][0]["role"] == "system"
    assert "Answer the user's book question directly first" in sent_body["messages"][0]["content"]
    assert "Do not claim live tools were called" in sent_body["messages"][0]["content"]
    assert "Routing summary: fresh_publication_context" in sent_body["messages"][0]["content"]


@pytest.mark.asyncio
@respx.mock
async def test_agent_run_respects_smaller_client_token_budget() -> None:
    nebius_route = _mock_nebius_stream()

    with TestClient(app) as client:
        with client.stream(
            "POST",
            "/agent/run",
            json={"prompt": "say hi", "max_tokens": 120},
        ) as resp:
            assert resp.status_code == 200
            body = b"".join(resp.iter_bytes()).decode("utf-8")

        metrics = client.get("/metrics")

    assert '"route": "direct"' in body

    sent_body = json.loads(nebius_route.calls.last.request.content)
    assert sent_body["max_tokens"] == 120
    assert "agent_route_total" in metrics.text
    assert "agent_first_token_seconds" in metrics.text


@pytest.mark.asyncio
@respx.mock
async def test_agent_run_uses_history_for_follow_up_topic() -> None:
    nebius_route = _mock_nebius_stream()

    with TestClient(app) as client:
        with client.stream(
            "POST",
            "/agent/run",
            json={
                "prompt": "Give me more books on that topic (at least 10).",
                "history": [
                    {
                        "role": "user",
                        "content": "I'd like to improve my fitness, which books do you recommend?",
                    },
                    {
                        "role": "assistant",
                        "content": "Here are several fitness books...",
                    },
                ],
            },
        ) as resp:
            assert resp.status_code == 200
            body = b"".join(resp.iter_bytes()).decode("utf-8")

    assert '"contextNeed": "curated_recommendation"' in body
    sent_body = json.loads(nebius_route.calls.last.request.content)
    user_message = sent_body["messages"][1]["content"]
    assert "Recent conversation context:" in user_message
    assert "improve my fitness" in user_message
    assert "Resolve references like 'that topic'" in user_message


@pytest.mark.asyncio
@respx.mock
async def test_agent_run_uses_nebius_price_lookup_for_cost() -> None:
    _mock_nebius_stream()
    respx.get("https://api.studio.nebius.ai/v1/models").mock(
        return_value=httpx.Response(
            200,
            json={
                "data": [
                    {
                        "id": "meta-llama/Llama-3.3-70B-Instruct",
                        "pricing": {
                            "input_per_million": 1.0,
                            "output_per_million": 2.0,
                        },
                    }
                ]
            },
        )
    )

    with TestClient(app) as client:
        with client.stream("POST", "/agent/run", json={"prompt": "say hi"}) as resp:
            assert resp.status_code == 200
            body = b"".join(resp.iter_bytes()).decode("utf-8")

    assert "Cost: $0.000213" in body
    assert '"costUsd": 0.000213' in body
