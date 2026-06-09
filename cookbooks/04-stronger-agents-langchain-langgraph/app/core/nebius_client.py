"""Thin wrapper around the OpenAI SDK pointed at Nebius AgentKit."""

from __future__ import annotations

from collections.abc import AsyncIterator
from dataclasses import dataclass

import httpx
import structlog
from openai import AsyncOpenAI
from openai.types.chat import ChatCompletionMessageParam
from tenacity import (
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
)

from app.config import Settings, get_settings
from app.observability.metrics import nebius_request_duration, nebius_tokens_total

logger = structlog.get_logger()


@dataclass(frozen=True)
class ChatStreamChunk:
    text: str = ""
    input_tokens: int | None = None
    output_tokens: int | None = None


class NebiusClient:
    """Async client for chat completions on Nebius AgentKit."""

    def __init__(self, settings: Settings) -> None:
        self._settings = settings
        self._client = AsyncOpenAI(
            api_key=settings.nebius_api_key,
            base_url=str(settings.nebius_base_url),
            timeout=httpx.Timeout(connect=5.0, read=60.0, write=10.0, pool=5.0),
            max_retries=0,  # we own retries via tenacity
        )

    @retry(
        retry=retry_if_exception_type((httpx.HTTPError, httpx.TimeoutException)),
        wait=wait_exponential(multiplier=0.5, min=0.5, max=8.0),
        stop=stop_after_attempt(3),
        reraise=True,
    )
    async def stream_chat(
        self,
        *,
        model: str,
        messages: list[ChatCompletionMessageParam],
        temperature: float = 0.4,
        max_tokens: int = 1024,
    ) -> AsyncIterator[ChatStreamChunk]:
        """Stream token deltas and final usage from a chat completion."""
        with nebius_request_duration.labels(model=model).time():
            stream = await self._client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
                stream=True,
                stream_options={"include_usage": True},
            )
            async for chunk in stream:
                usage = getattr(chunk, "usage", None)
                if usage is not None:
                    yield ChatStreamChunk(
                        input_tokens=int(getattr(usage, "prompt_tokens", 0) or 0),
                        output_tokens=int(getattr(usage, "completion_tokens", 0) or 0),
                    )
                if not chunk.choices:
                    continue
                delta = chunk.choices[0].delta
                if delta and delta.content:
                    nebius_tokens_total.labels(model=model, type="output").inc()
                    yield ChatStreamChunk(text=delta.content)

    async def aclose(self) -> None:
        await self._client.close()


def build_nebius_client() -> NebiusClient:
    """FastAPI dependency. Reuses a single client per process."""
    return _cached_client(get_settings())


_singleton: NebiusClient | None = None


def _cached_client(settings: Settings) -> NebiusClient:
    global _singleton
    if _singleton is None:
        _singleton = NebiusClient(settings)
    return _singleton
