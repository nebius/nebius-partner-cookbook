"""Thin wrapper around the OpenAI SDK pointed at Nebius AgentKit."""

from __future__ import annotations

from collections.abc import AsyncIterator

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


class NebiusClient:
    """Async client for chat completions on Nebius AgentKit."""

    def __init__(self, settings: Settings) -> None:
        self._settings = settings
        # Nebius AgentKit is OpenAI-compatible: point the OpenAI SDK at its
        # base URL and the same `chat.completions` calls work unchanged.
        self._client = AsyncOpenAI(
            api_key=settings.nebius_api_key,
            base_url=str(settings.nebius_base_url),
            timeout=httpx.Timeout(connect=5.0, read=60.0, write=10.0, pool=5.0),
            max_retries=0,  # we own retries via tenacity
        )

    # Retry only on transport errors. Logical errors (4xx, bad payload) propagate
    # immediately — retrying them just wastes quota.
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
    ) -> AsyncIterator[str]:
        """Stream raw token deltas from a chat completion."""
        with nebius_request_duration.labels(model=model).time():
            stream = await self._client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
                stream=True,
            )
            async for chunk in stream:
                if not chunk.choices:
                    continue
                delta = chunk.choices[0].delta
                if delta and delta.content:
                    nebius_tokens_total.labels(model=model, type="output").inc()
                    yield delta.content

    async def aclose(self) -> None:
        await self._client.close()


def build_nebius_client() -> NebiusClient:
    """FastAPI dependency. Reuses a single client per process.

    Sharing one `AsyncOpenAI` instance is important: it keeps the underlying httpx
    connection pool alive, so we don't pay TLS handshake cost on every request.
    """
    return _cached_client(get_settings())


_singleton: NebiusClient | None = None


def _cached_client(settings: Settings) -> NebiusClient:
    global _singleton
    if _singleton is None:
        _singleton = NebiusClient(settings)
    return _singleton
