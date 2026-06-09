"""Agent route tests. All upstream calls are mocked with respx — no network."""

from __future__ import annotations

import json

import httpx
import pytest
import respx
from fastapi.testclient import TestClient

from app.main import app


def _sse_chunk(data: dict[str, object]) -> bytes:
    return (b"data: " + json.dumps(data).encode("utf-8") + b"\n\n")


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
    respx.post("https://api.studio.nebius.ai/v1/chat/completions").mock(
        return_value=httpx.Response(
            200,
            content=_build_completion_stream(),
            headers={"content-type": "text/event-stream"},
        )
    )

    with TestClient(app) as client:
        with client.stream("POST", "/agent/run", json={"prompt": "say hi"}) as resp:
            assert resp.status_code == 200
            body = b"".join(resp.iter_bytes()).decode("utf-8")

    assert "event: status" in body
    assert "event: token" in body
    assert "event: done" in body
