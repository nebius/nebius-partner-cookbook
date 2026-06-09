"""Request and response models for the agent endpoint."""

from __future__ import annotations

from pydantic import BaseModel, Field


class ChatHistoryMessage(BaseModel):
    """A previous chat turn sent by the playground client."""

    role: str = Field(..., pattern="^(user|assistant)$")
    content: str = Field(..., min_length=1, max_length=8_000)


class AgentRunRequest(BaseModel):
    """Payload for POST /agent/run."""

    thread_id: str = Field(..., min_length=1, max_length=120, pattern="^[A-Za-z0-9_.:-]+$")
    prompt: str = Field(..., min_length=1, max_length=8_000)
    temperature: float = Field(default=0.4, ge=0.0, le=2.0)
    max_tokens: int = Field(default=1024, ge=1, le=8192)
    history: list[ChatHistoryMessage] = Field(
        default_factory=list,
        max_length=12,
        description="Optional one-off context. Stored thread memory is loaded by thread_id.",
    )


class AgentEvent(BaseModel):
    """A single SSE event emitted by the agent."""

    name: str
    data: dict[str, object]
