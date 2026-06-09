"""In-process short-term memory for local thread continuity."""

from __future__ import annotations

import asyncio
from dataclasses import dataclass, field

from langsmith import traceable

from app.core.langsmith_annotations import process_langsmith_inputs, process_langsmith_outputs


@dataclass
class ThreadMemoryStore:
    """Small local store for recent conversation turns.

    This is intentionally process-local for Cookbook #5. Cookbook #6 replaces it
    with database-backed LangGraph persistence.
    """

    max_messages_per_thread: int = 12
    _threads: dict[str, list[dict[str, str]]] = field(default_factory=dict)
    _lock: asyncio.Lock = field(default_factory=asyncio.Lock)

    @traceable(
        name="thread_memory.get_history",
        run_type="retriever",
        process_inputs=process_langsmith_inputs,
        process_outputs=process_langsmith_outputs,
    )
    async def get_history(self, thread_id: str) -> list[dict[str, str]]:
        """Return a copy of recent messages for a thread."""
        async with self._lock:
            return list(self._threads.get(thread_id, []))

    @traceable(
        name="thread_memory.append_turn",
        run_type="tool",
        process_inputs=process_langsmith_inputs,
        process_outputs=process_langsmith_outputs,
    )
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

    @traceable(
        name="thread_memory.clear",
        run_type="tool",
        process_inputs=process_langsmith_inputs,
        process_outputs=process_langsmith_outputs,
    )
    async def clear(self, thread_id: str) -> bool:
        """Delete a thread if it exists."""
        async with self._lock:
            return self._threads.pop(thread_id, None) is not None


_store = ThreadMemoryStore()


def get_thread_memory_store() -> ThreadMemoryStore:
    """FastAPI dependency for local thread memory."""
    return _store
