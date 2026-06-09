"""Thread memory management endpoints."""

from __future__ import annotations

from fastapi import APIRouter, Depends

from app.core.thread_memory import ThreadMemoryStore, get_thread_memory_store

router = APIRouter()


@router.delete("/threads/{thread_id}")
async def delete_thread(
    thread_id: str,
    memory: ThreadMemoryStore = Depends(get_thread_memory_store),
) -> dict[str, object]:
    """Clear process-local memory for a conversation thread."""
    deleted = await memory.clear(thread_id)
    return {"threadId": thread_id, "deleted": deleted}
