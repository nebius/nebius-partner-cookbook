"""Prometheus counters and histograms, plus the request-timing middleware."""

from __future__ import annotations

import time
from collections.abc import Awaitable, Callable

from prometheus_client import Counter, Histogram
from starlette.requests import Request
from starlette.responses import Response

http_requests_total = Counter(
    "http_requests_total",
    "Total HTTP requests.",
    labelnames=("method", "path", "status"),
)

http_request_duration_seconds = Histogram(
    "http_request_duration_seconds",
    "HTTP request duration, in seconds.",
    labelnames=("method", "path"),
    buckets=(0.01, 0.05, 0.1, 0.25, 0.5, 1.0, 2.5, 5.0, 10.0, 30.0, 60.0),
)

nebius_tokens_total = Counter(
    "nebius_tokens_total",
    "Tokens emitted by Nebius streams.",
    labelnames=("model", "type"),
)

nebius_request_duration = Histogram(
    "nebius_request_duration_seconds",
    "Duration of Nebius chat completion requests.",
    labelnames=("model",),
    buckets=(0.1, 0.25, 0.5, 1.0, 2.5, 5.0, 10.0, 30.0, 60.0, 120.0),
)

agent_route_total = Counter(
    "agent_route_total",
    "Total agent requests by selected LangGraph route.",
    labelnames=("route",),
)

agent_first_token_seconds = Histogram(
    "agent_first_token_seconds",
    "Time from agent start to first streamed token.",
    labelnames=("route",),
    buckets=(0.1, 0.25, 0.5, 1.0, 1.2, 1.5, 2.5, 5.0, 10.0, 30.0, 60.0),
)

guardrail_events_total = Counter(
    "guardrail_events_total",
    "Total guardrail decisions.",
    labelnames=("stage", "rule", "outcome"),
)

approval_events_total = Counter(
    "approval_events_total",
    "Total approval lifecycle events.",
    labelnames=("status",),
)

stripe_mcp_requests_total = Counter(
    "stripe_mcp_requests_total",
    "Total Stripe MCP tool calls.",
    labelnames=("tool", "outcome"),
)

stripe_mcp_duration_seconds = Histogram(
    "stripe_mcp_duration_seconds",
    "Duration of Stripe MCP tool calls.",
    labelnames=("tool",),
    buckets=(0.05, 0.1, 0.25, 0.5, 1.0, 2.5, 5.0, 10.0, 30.0),
)


async def metrics_middleware(
    request: Request,
    call_next: Callable[[Request], Awaitable[Response]],
) -> Response:
    """Record per-request counters and latency."""
    start = time.perf_counter()
    response = await call_next(request)
    elapsed = time.perf_counter() - start
    path = request.url.path
    http_requests_total.labels(
        method=request.method, path=path, status=str(response.status_code)
    ).inc()
    http_request_duration_seconds.labels(method=request.method, path=path).observe(elapsed)
    return response
