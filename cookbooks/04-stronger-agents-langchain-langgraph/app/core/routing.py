"""Deterministic routing and budget primitives for the orchestration graph."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal, TypedDict

RouteName = Literal["direct", "deliberate"]
ContextNeed = Literal[
    "direct_answer",
    "curated_recommendation",
    "fresh_publication_context",
    "curated_plus_fresh_context",
]

FRESH_CONTEXT_MARKERS = (
    "today",
    "latest",
    "current",
    "recent",
    "pricing",
    "price",
    "benchmark",
    "grounding",
    "compare",
    "review",
    "published",
    "publication",
    "since ",
    "2026",
)

RECOMMENDATION_MARKERS = (
    "recommend",
    "what should i read",
    "read next",
    "more books",
    "books on",
    "books about",
    "similar to",
    "i loved",
    "i liked",
)


class RouteStateUpdate(TypedDict):
    route: RouteName
    context_need: ContextNeed
    route_reason: str


@dataclass(frozen=True)
class RouteDecision:
    route: RouteName
    context_need: ContextNeed
    reason: str

    def to_state_update(self) -> RouteStateUpdate:
        return {
            "route": self.route,
            "context_need": self.context_need,
            "route_reason": self.reason,
        }


def classify_request(prompt: str, history: list[dict[str, str]] | None = None) -> RouteDecision:
    """Classify work with inspectable rules instead of a probabilistic model call."""
    history_text = " ".join(item.get("content", "") for item in (history or [])[-4:])
    normalized = f"{history_text} {prompt.strip()}".lower()
    needs_fresh_context = any(marker in normalized for marker in FRESH_CONTEXT_MARKERS)
    needs_recommendations = any(marker in normalized for marker in RECOMMENDATION_MARKERS)

    if needs_fresh_context and needs_recommendations:
        context_need: ContextNeed = "curated_plus_fresh_context"
        reason = "recommendation request also depends on recent publication or review context"
    elif needs_fresh_context:
        context_need = "fresh_publication_context"
        reason = "question depends on latest/current publication context"
    elif needs_recommendations:
        context_need = "curated_recommendation"
        reason = "question asks for taste or topic-based book recommendations"
    else:
        context_need = "direct_answer"
        reason = "question can be answered directly without extra context"

    route: RouteName = (
        "deliberate" if len(prompt.strip()) > 280 or context_need != "direct_answer" else "direct"
    )
    return RouteDecision(route=route, context_need=context_need, reason=reason)


def bounded_output_tokens(
    requested: int,
    *,
    route: RouteName,
    direct_limit: int,
    deliberate_limit: int,
) -> int:
    """Apply the selected route's deterministic output-cost ceiling."""
    route_limit = direct_limit if route == "direct" else deliberate_limit
    return min(requested, route_limit)
