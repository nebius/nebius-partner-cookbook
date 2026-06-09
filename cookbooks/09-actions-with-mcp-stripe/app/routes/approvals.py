"""Approval endpoint for side-effectful Stripe MCP actions."""

from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException

from app.core.approvals import ApprovalRecord, ApprovalStore, get_approval_store
from app.core.stripe_mcp import StripeMCPClient, StripeMCPError, build_stripe_mcp_client
from app.schemas.approval import ApprovalBook, ApprovalDecisionRequest, ApprovalResponse

router = APIRouter()


@router.post("/approvals/{approval_id}", response_model=ApprovalResponse)
async def decide_approval(
    approval_id: str,
    payload: ApprovalDecisionRequest,
    approvals: ApprovalStore = Depends(get_approval_store),
    stripe_mcp: StripeMCPClient = Depends(build_stripe_mcp_client),
) -> ApprovalResponse:
    """Approve or reject a pending Stripe action."""
    record = approvals.get(approval_id)
    if record is None:
        raise HTTPException(status_code=404, detail="approval not found")
    if record.status == "expired":
        raise HTTPException(status_code=410, detail="approval expired")
    if record.status in {"completed", "rejected"}:
        return _response(record, message=f"approval already {record.status}")

    if payload.decision == "reject":
        return _response(approvals.reject(approval_id), message="action rejected")

    try:
        result = await stripe_mcp.create_payment_link(
            book=record.book,
            approval_id=record.id,
            user_id=record.user_id,
        )
    except StripeMCPError as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc
    return _response(approvals.complete(approval_id, result), message="checkout link created")


def _response(record: ApprovalRecord, *, message: str) -> ApprovalResponse:
    return ApprovalResponse(
        approvalId=record.id,
        status=record.status,
        book=ApprovalBook(
            slug=record.book.slug,
            title=record.book.title,
            author=record.book.author,
            amount=record.book.amount,
            currency=record.book.currency,
            prices=record.book.prices,
        ),
        checkoutUrl=record.checkout_url,
        stripePaymentLinkId=record.stripe_payment_link_id,
        message=message,
    )
