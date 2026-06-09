"""Agent logic. Pure async generator yielding typed events."""

from __future__ import annotations

import asyncio
from collections.abc import AsyncIterator
from dataclasses import dataclass

from app.core.nebius_client import NebiusClient

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
        cancel_event: asyncio.Event | None = None,
    ) -> AsyncIterator[Event]:
        yield Event("status", {"phase": "thinking"})

        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ]

        async for token in self._client.stream_chat(
            model=self._model, messages=messages  # type: ignore[arg-type]
        ):
            if cancel_event is not None and cancel_event.is_set():
                return
            yield Event("token", {"text": token})

        yield Event("status", {"phase": "done"})
