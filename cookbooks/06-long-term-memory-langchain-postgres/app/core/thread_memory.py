"""In-process short-term memory for local thread continuity."""

from __future__ import annotations

import asyncio
from dataclasses import dataclass, field


@dataclass
class ThreadMemoryStore:
    """Small local store for recent conversation turns.

    This is intentionally process-local for Cookbook #5. Cookbook #6 replaces it
    with database-backed LangGraph persistence.
    """

    max_messages_per_thread: int = 12
    _threads: dict[str, list[dict[str, str]]] = field(default_factory=dict)
    _lock: asyncio.Lock = field(default_factory=asyncio.Lock)

    async def get_history(self, thread_id: str) -> list[dict[str, str]]:
        """Return a copy of recent messages for a thread."""
        async with self._lock:
            return list(self._threads.get(thread_id, []))

    async def append_turn(self, thread_id: str, *, user: str, assistant: str) -> int:
        """Append a completed user/assistant turn and return retained message count."""
        async with self._lock:
            messages = self._threads.setdefault(thread_id, [])
            messages.extend(
                [
                    {"role": "user", "content": user},
                    {"role": "assistant", "content": assistant},
                ]
            )
            del messages[: max(0, len(messages) - self.max_messages_per_thread)]
            return len(messages)

    async def clear(self, thread_id: str) -> bool:
        """Delete a thread if it exists."""
        async with self._lock:
            return self._threads.pop(thread_id, None) is not None


_store = ThreadMemoryStore()


def get_thread_memory_store() -> ThreadMemoryStore:
    """FastAPI dependency for local thread memory."""
    return _store
