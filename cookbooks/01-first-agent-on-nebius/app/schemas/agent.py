"""Request and response models for the agent endpoint."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, Field


class Message(BaseModel):
    """A single prior turn supplied by the client."""

    role: Literal["user", "assistant"]
    content: str = Field(..., min_length=1, max_length=8_000)


class AgentRunRequest(BaseModel):
    """Payload for POST /agent/run."""

    prompt: str = Field(..., min_length=1, max_length=8_000)
    history: list[Message] = Field(default_factory=list, max_length=40)
    temperature: float = Field(default=0.4, ge=0.0, le=2.0)
    max_tokens: int = Field(default=1024, ge=1, le=8192)


class AgentEvent(BaseModel):
    """A single SSE event emitted by the agent."""

    name: str
    data: dict[str, object]
