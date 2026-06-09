"""LangSmith feedback endpoint."""

from __future__ import annotations

from fastapi import APIRouter, Depends

from app.core.langsmith_observability import LangSmithObserver, get_langsmith_observer
from app.schemas.feedback import FeedbackRequest

router = APIRouter()


@router.post("/feedback")
async def create_feedback(
    payload: FeedbackRequest,
    observer: LangSmithObserver = Depends(get_langsmith_observer),
) -> dict[str, object]:
    """Attach user or reviewer feedback to a LangSmith run."""
    accepted = await observer.create_feedback(
        run_id=payload.run_id,
        key=payload.key,
        score=payload.score,
        comment=payload.comment,
    )
    return {"runId": payload.run_id, "accepted": accepted}
