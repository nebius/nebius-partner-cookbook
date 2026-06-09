"""In-memory approval store for side-effectful Stripe actions."""

from __future__ import annotations

import uuid
from dataclasses import dataclass
from datetime import UTC, datetime, timedelta
from typing import Literal

from app.core.book_catalog import BookCatalogItem
from app.observability.metrics import approval_events_total

ApprovalStatus = Literal["pending", "completed", "rejected", "expired"]


@dataclass(frozen=True)
class PaymentLinkResult:
    """Result returned by Stripe MCP after creating a payment link."""

    url: str
    stripe_payment_link_id: str | None = None


@dataclass
class ApprovalRecord:
    """Pending or completed approval for one external action."""

    id: str
    thread_id: str
    user_id: str
    prompt: str
    book: BookCatalogItem
    created_at: datetime
    expires_at: datetime
    status: ApprovalStatus = "pending"
    checkout_url: str | None = None
    stripe_payment_link_id: str | None = None

    @property
    def is_expired(self) -> bool:
        return self.status == "pending" and datetime.now(UTC) >= self.expires_at


class ApprovalStore:
    """Process-local approval store for the cookbook demo."""

    def __init__(self) -> None:
        self._records: dict[str, ApprovalRecord] = {}

    def create(
        self,
        *,
        thread_id: str,
        user_id: str,
        prompt: str,
        book: BookCatalogItem,
        ttl_seconds: int,
    ) -> ApprovalRecord:
        """Create a pending approval."""
        now = datetime.now(UTC)
        record = ApprovalRecord(
            id=str(uuid.uuid4()),
            thread_id=thread_id,
            user_id=user_id,
            prompt=prompt,
            book=book,
            created_at=now,
            expires_at=now + timedelta(seconds=ttl_seconds),
        )
        self._records[record.id] = record
        approval_events_total.labels(status="created").inc()
        return record

    def get(self, approval_id: str) -> ApprovalRecord | None:
        """Return one approval if it exists."""
        record = self._records.get(approval_id)
        if record and record.is_expired:
            record.status = "expired"
            approval_events_total.labels(status="expired").inc()
        return record

    def reject(self, approval_id: str) -> ApprovalRecord:
        """Reject a pending approval."""
        record = self._require_pending(approval_id)
        record.status = "rejected"
        approval_events_total.labels(status="rejected").inc()
        return record

    def complete(self, approval_id: str, result: PaymentLinkResult) -> ApprovalRecord:
        """Mark a pending approval as completed."""
        record = self._require_pending(approval_id)
        record.status = "completed"
        record.checkout_url = result.url
        record.stripe_payment_link_id = result.stripe_payment_link_id
        approval_events_total.labels(status="completed").inc()
        return record

    def _require_pending(self, approval_id: str) -> ApprovalRecord:
        record = self.get(approval_id)
        if record is None:
            raise KeyError(approval_id)
        if record.status != "pending":
            raise ValueError(record.status)
        return record


_approval_store: ApprovalStore | None = None


def get_approval_store() -> ApprovalStore:
    """FastAPI dependency for approvals."""
    global _approval_store
    if _approval_store is None:
        _approval_store = ApprovalStore()
    return _approval_store
