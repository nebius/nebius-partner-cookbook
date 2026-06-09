"""Stripe remote MCP client for approved payment-link actions."""

from __future__ import annotations

import json
import uuid
from typing import Any

import httpx

from app.config import Settings, get_settings
from app.core.approvals import PaymentLinkResult
from app.core.book_catalog import BookCatalogItem
from app.observability.metrics import stripe_mcp_duration_seconds, stripe_mcp_requests_total


class StripeMCPError(RuntimeError):
    """Raised when the Stripe MCP call fails."""


class StripeMCPClient:
    """Small JSON-RPC client for Stripe's remote MCP server."""

    def __init__(self, settings: Settings) -> None:
        self._base_url = str(settings.stripe_mcp_base_url).rstrip("/")
        self._api_key = settings.stripe_mcp_api_key
        self._timeout = httpx.Timeout(connect=5, read=30, write=10, pool=5)

    async def create_payment_link(
        self,
        *,
        book: BookCatalogItem,
        approval_id: str,
        user_id: str,
        quantity: int = 1,
    ) -> PaymentLinkResult:
        """Create a Stripe Payment Link through MCP."""
        if not book.stripe_price_id:
            raise StripeMCPError(f"Book {book.slug} has no Stripe Price ID.")
        payload = {
            "jsonrpc": "2.0",
            "id": str(uuid.uuid4()),
            "method": "tools/call",
            "params": {
                "name": "create_payment_link",
                "arguments": {
                    "line_items": [{"price": book.stripe_price_id, "quantity": quantity}],
                    "metadata": {
                        "approval_id": approval_id,
                        "user_id": user_id,
                        "book_slug": book.slug,
                        "cookbook": "09-actions-with-mcp-stripe",
                    },
                },
            },
        }
        with stripe_mcp_duration_seconds.labels(tool="create_payment_link").time():
            async with httpx.AsyncClient(timeout=self._timeout) as client:
                response = await client.post(
                    self._base_url,
                    headers={
                        "authorization": f"Bearer {self._api_key}",
                        "content-type": "application/json",
                    },
                    json=payload,
                )
        if response.status_code >= 400:
            stripe_mcp_requests_total.labels(tool="create_payment_link", outcome="error").inc()
            raise StripeMCPError(f"Stripe MCP returned HTTP {response.status_code}.")

        data = response.json()
        if "error" in data:
            stripe_mcp_requests_total.labels(tool="create_payment_link", outcome="error").inc()
            raise StripeMCPError(str(data["error"]))
        result = _parse_payment_link_result(data.get("result"))
        stripe_mcp_requests_total.labels(tool="create_payment_link", outcome="success").inc()
        return result


def _parse_payment_link_result(result: object) -> PaymentLinkResult:
    """Extract a Payment Link URL from common MCP response shapes."""
    candidates = list(_walk_values(result))
    url = next(
        (value for value in candidates if isinstance(value, str) and value.startswith("https://")),
        None,
    )
    payment_link_id = next(
        (value for value in candidates if isinstance(value, str) and value.startswith("plink_")),
        None,
    )
    if not url:
        raise StripeMCPError("Stripe MCP response did not include a checkout URL.")
    return PaymentLinkResult(url=url, stripe_payment_link_id=payment_link_id)


def _walk_values(value: object) -> list[object]:
    values: list[object] = []
    if isinstance(value, dict):
        values.extend(value.values())
        for item in value.values():
            values.extend(_walk_values(item))
    elif isinstance(value, list):
        values.extend(value)
        for item in value:
            values.extend(_walk_values(item))
    elif isinstance(value, str):
        values.append(value)
        try:
            decoded: Any = json.loads(value)
        except json.JSONDecodeError:
            return values
        values.extend(_walk_values(decoded))
    return values


def build_stripe_mcp_client() -> StripeMCPClient:
    """FastAPI dependency for the Stripe MCP client."""
    return StripeMCPClient(get_settings())
