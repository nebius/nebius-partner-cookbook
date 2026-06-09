"""Feedback models for LangSmith run annotation."""

from __future__ import annotations

from pydantic import BaseModel, Field


class FeedbackRequest(BaseModel):
    """Payload for POST /feedback."""

    run_id: str = Field(..., min_length=1)
    key: str = Field(default="user_rating", min_length=1, max_length=80)
    score: float | int | bool | None = Field(default=None)
    comment: str | None = Field(default=None, max_length=2_000)
