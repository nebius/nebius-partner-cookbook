"""Agent logic. Pure async generator yielding typed events."""

from __future__ import annotations

import asyncio
from collections.abc import AsyncIterator
from dataclasses import dataclass

from app.core.nebius_client import NebiusClient
from app.schemas.agent import Message

SYSTEM_PROMPT = (
    "You are a helpful, concise assistant. Answer the user's question directly, "
    "without preamble. Use plain text unless markdown adds clarity."
)


@dataclass
class Event:
    name: str
    data: dict[str, object]


class Agent:
    """A single-LLM-call agent. Subclass to add planning, tools, or retrieval."""

    def __init__(self, client: NebiusClient, model: str) -> None:
        self._client = client
        self._model = model

    async def run(
        self,
        prompt: str,
        *,
        history: list[Message] | None = None,
        cancel_event: asyncio.Event | None = None,
    ) -> AsyncIterator[Event]:
        # Async generator: each `yield` is a discrete event the route can turn
        # into an SSE frame. Status events bracket the response; token events
        # carry incremental text.
        yield Event("status", {"phase": "thinking"})

        # Chat-completion message shape: [system, ...history, new user turn].
        # The server is stateless — the client must replay history each call.
        messages: list[dict[str, str]] = [{"role": "system", "content": SYSTEM_PROMPT}]
        if history:
            messages.extend({"role": m.role, "content": m.content} for m in history)
        messages.append({"role": "user", "content": prompt})

        async for token in self._client.stream_chat(
            model=self._model,
            messages=messages,  # type: ignore[arg-type]
        ):
            # Cooperative cancellation: the route sets this when the client
            # disconnects, letting us stop pulling from upstream mid-stream.
            if cancel_event is not None and cancel_event.is_set():
                return
            yield Event("token", {"text": token})

        yield Event("status", {"phase": "done"})
