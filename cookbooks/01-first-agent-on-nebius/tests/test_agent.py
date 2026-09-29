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
    ]
    body = b"".join(_sse_chunk(c) for c in chunks) + b"data: [DONE]\n\n"
    return body


@pytest.mark.asyncio
@respx.mock
async def test_agent_run_streams_tokens() -> None:
    upstream = respx.post("https://api.tokenfactory.nebius.com/v1/chat/completions").mock(
        return_value=httpx.Response(
            200,
            content=_build_completion_stream(),
            headers={"content-type": "text/event-stream"},
        )
    )

    with TestClient(app) as client:
        with client.stream(
            "POST",
            "/agent/run",
            json={"prompt": "say hi", "temperature": 0.9, "max_tokens": 77},
        ) as resp:
            assert resp.status_code == 200
            body = b"".join(resp.iter_bytes()).decode("utf-8")

    assert "event: status" in body
    assert "event: token" in body
    assert "event: done" in body
    sent = json.loads(upstream.calls.last.request.content)
    assert sent["temperature"] == 0.9
    assert sent["max_tokens"] == 77


@pytest.mark.asyncio
@respx.mock
async def test_development_error_identifies_authentication_failure(monkeypatch) -> None:
    monkeypatch.setenv("ENV", "development")
    monkeypatch.setenv("NEBIUS_DEBUG_ERRORS", "true")
    respx.post("https://api.tokenfactory.nebius.com/v1/chat/completions").mock(
        return_value=httpx.Response(
            401,
            json={"error": {"message": "secret upstream response", "type": "auth_error"}},
        )
    )

    with TestClient(app) as client:
        response = client.post("/agent/run", json={"prompt": "say hi"})

    assert '"code": "upstream_authentication_error"' in response.text
    assert "Token Factory rejected the configured API key" in response.text
    assert "AuthenticationError" in response.text
    assert "secret upstream response" not in response.text
    assert '"requestId": "unknown"' not in response.text


@pytest.mark.asyncio
@respx.mock
async def test_production_error_hides_upstream_details(monkeypatch) -> None:
    monkeypatch.setenv("ENV", "production")
    monkeypatch.setenv("NEBIUS_DEBUG_ERRORS", "true")
    upstream = respx.post("https://api.tokenfactory.nebius.com/v1/chat/completions").mock(
        return_value=httpx.Response(
            404,
            json={"error": {"message": "secret upstream response", "type": "not_found"}},
        )
    )

    with TestClient(app) as client:
        response = client.post("/agent/run", json={"prompt": "say hi"})

    assert '"code": "upstream_model_not_found"' in response.text
    assert '"detail": "internal error"' in response.text
    assert "NotFoundError" not in response.text
    assert "secret upstream response" not in response.text
    assert upstream.call_count == 1


@pytest.mark.asyncio
@respx.mock
async def test_transient_rate_limit_is_retried_before_streaming() -> None:
    attempts = 0

    def respond(request: httpx.Request) -> httpx.Response:
        nonlocal attempts
        attempts += 1
        if attempts < 3:
            return httpx.Response(
                429,
                request=request,
                json={"error": {"message": "try later", "type": "rate_limit"}},
            )
        return httpx.Response(
            200,
            request=request,
            content=_build_completion_stream(),
            headers={"content-type": "text/event-stream"},
        )

    respx.post("https://api.tokenfactory.nebius.com/v1/chat/completions").mock(side_effect=respond)

    with TestClient(app) as client:
        response = client.post("/agent/run", json={"prompt": "say hi"})

    assert response.status_code == 200
    assert "event: token" in response.text
    assert attempts == 3
