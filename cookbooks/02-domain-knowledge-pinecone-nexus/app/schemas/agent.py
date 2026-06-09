"""Request and response schemas for the book recommendation endpoint."""

from __future__ import annotations

from pydantic import BaseModel, Field


class AgentRunRequest(BaseModel):
    prompt: str = Field(
        ...,
        min_length=1,
        max_length=4_000,
        examples=[
            "Recommend books about political intrigue for someone who liked Dune.",
            "I just read The Left Hand of Darkness. What should I read next?",
        ],
    )
    top_k: int = Field(default=10, ge=1, le=50)
    related_top_k: int = Field(default=4, ge=1, le=20)
    include_related: bool = Field(default=True)
