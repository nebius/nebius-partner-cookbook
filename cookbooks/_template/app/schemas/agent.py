"""Request and response models for the agent endpoint."""

from __future__ import annotations

from pydantic import BaseModel, Field


class AgentRunRequest(BaseModel):
    """Payload for POST /agent/run."""

    prompt: str = Field(..., min_length=1, max_length=8_000)
    temperature: float = Field(default=0.4, ge=0.0, le=2.0)
    max_tokens: int = Field(default=1024, ge=1, le=8192)


class AgentEvent(BaseModel):
    """A single SSE event emitted by the agent."""

    name: str
    data: dict[str, object]
