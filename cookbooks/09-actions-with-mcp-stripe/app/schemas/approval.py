"""Schemas for human-approved Stripe actions."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, Field, HttpUrl


class ApprovalDecisionRequest(BaseModel):
    """Payload for POST /approvals/{approval_id}."""

    decision: Literal["approve", "reject"]


class ApprovalBook(BaseModel):
    """Book metadata attached to a pending action."""

    slug: str
    title: str
    author: str
    amount: int
    currency: str
    prices: dict[str, int]


class ApprovalResponse(BaseModel):
    """Response returned after an approval decision."""

    approval_id: str = Field(..., alias="approvalId")
    status: Literal["pending", "completed", "rejected", "expired"]
    book: ApprovalBook
    checkout_url: HttpUrl | None = Field(default=None, alias="checkoutUrl")
    stripe_payment_link_id: str | None = Field(default=None, alias="stripePaymentLinkId")
    message: str

    model_config = {"populate_by_name": True}
