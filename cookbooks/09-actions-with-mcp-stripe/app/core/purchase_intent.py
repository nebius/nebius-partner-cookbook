"""Deterministic purchase-intent detection for the cookbook action."""

from __future__ import annotations

PURCHASE_MARKERS = (
    "buy",
    "checkout",
    "payment link",
    "purchase",
    "order",
    "pay for",
)


def is_purchase_intent(prompt: str) -> bool:
    """Return true when a book prompt asks for a checkout action."""
    lower = prompt.lower()
    return any(marker in lower for marker in PURCHASE_MARKERS)
