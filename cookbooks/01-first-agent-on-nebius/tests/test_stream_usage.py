"""Exercise SDK streaming with missing/null usage and provider retry headers."""

import asyncio
import json

import httpx
import pytest
import respx

from app.config import Settings
from app.core.nebius_client import NebiusClient
from app.observability.metrics import nebius_streams_without_usage_total, nebius_tokens_total


@pytest.mark.parametrize(
    "usage",
    [
        None,
        {"prompt_tokens": None, "completion_tokens": None, "total_tokens": None},
        {"prompt_tokens": 7, "completion_tokens": 2, "total_tokens": 9},
    ],
)
@respx.mock
def test_stream_tolerates_missing_usage_and_reports_incomplete_metrics(usage) -> None:
    chunks = [{"choices": [{"delta": {"content": "answer"}, "index": 0}]}]
    if usage is not None:
        chunks.append({"choices": [], "usage": usage})
    body = "".join("data: " + json.dumps(chunk) + "\n\n" for chunk in chunks) + "data: [DONE]\n\n"
    respx.post("https://example.com/v1/chat/completions").respond(200, text=body)
    model = "usage-regression"
    missing = nebius_streams_without_usage_total.labels(model=model)
    output = nebius_tokens_total.labels(model=model, type="output")
    before_missing, before_output = missing._value.get(), output._value.get()

    async def run() -> list:
        client = NebiusClient(
            Settings(
                _env_file=None, nebius_api_key="test", nebius_base_url="https://example.com/v1/"
            )
        )
        try:
            return [chunk async for chunk in client.stream_chat(model=model, messages=[])]
        finally:
            await client.aclose()

    chunks = asyncio.run(run())
    assert "".join(chunk if isinstance(chunk, str) else chunk.text for chunk in chunks) == "answer"
    complete = usage is not None and usage["completion_tokens"] is not None
    assert output._value.get() - before_output == (2 if complete else 0)
    assert missing._value.get() - before_missing == (0 if complete else 1)


@respx.mock
def test_retry_after_is_respected_before_opening_stream(monkeypatch) -> None:
    sleeps: list[float] = []

    async def sleep(seconds: float) -> None:
        sleeps.append(seconds)
        await asyncio.sleep(0)

    monkeypatch.setattr("openai._base_client.anyio.sleep", sleep)
    route = respx.post("https://example.com/v1/chat/completions").mock(
        side_effect=[
            httpx.Response(
                429, headers={"retry-after": "12"}, json={"error": {"message": "retry later"}}
            ),
            httpx.Response(
                200,
                text='data: {"choices":[{"delta":{"content":"ok"},"index":0}]}\n\ndata: [DONE]\n\n',
            ),
        ]
    )

    async def run() -> None:
        client = NebiusClient(
            Settings(
                _env_file=None, nebius_api_key="test", nebius_base_url="https://example.com/v1/"
            )
        )
        try:
            chunks = [
                chunk async for chunk in client.stream_chat(model="retry-regression", messages=[])
            ]
            assert chunks
        finally:
            await client.aclose()

    asyncio.run(run())
    assert sleeps == [12.0]
    assert route.call_count == 2
