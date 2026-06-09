"""Long-term memory inspection and deletion endpoints."""

from __future__ import annotations

from fastapi import APIRouter, Depends

from app.config import Settings, get_settings
from app.core.long_term_memory import LongTermMemoryStore, get_long_term_memory_store

router = APIRouter()


@router.get("/memory/{user_id}")
async def list_user_memories(
    user_id: str,
    settings: Settings = Depends(get_settings),
    memory: LongTermMemoryStore = Depends(get_long_term_memory_store),
) -> dict[str, object]:
    """List long-term memories for a user."""
    records = await memory.list_memories(user_id, limit=settings.long_term_memory_limit)
    return {
        "userId": user_id,
        "memories": [
            {
                "id": record.id,
                "text": record.text,
                "source": record.source,
                "createdAt": record.created_at.isoformat(),
            }
            for record in records
        ],
    }


@router.get("/memory/{user_id}/summary")
async def summarize_user_memories(
    user_id: str,
    settings: Settings = Depends(get_settings),
    memory: LongTermMemoryStore = Depends(get_long_term_memory_store),
) -> dict[str, object]:
    """Summarize what the agent currently knows about a user."""
    records = await memory.list_memories(user_id, limit=settings.long_term_memory_limit)
    if records:
        summary = "The agent knows:\n" + "\n".join(f"- {record.text}" for record in records)
    else:
        summary = "The agent has no long-term memories stored for this user."
    return {
        "userId": user_id,
        "summary": summary,
        "memoryCount": len(records),
        "memories": [
            {
                "id": record.id,
                "text": record.text,
                "source": record.source,
                "createdAt": record.created_at.isoformat(),
            }
            for record in records
        ],
    }


@router.delete("/memory/{user_id}")
async def delete_user_memories(
    user_id: str,
    memory: LongTermMemoryStore = Depends(get_long_term_memory_store),
) -> dict[str, object]:
    """Delete long-term memories for a user."""
    deleted = await memory.delete_user_memories(user_id)
    return {"userId": user_id, "deleted": deleted}
