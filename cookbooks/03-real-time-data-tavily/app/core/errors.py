"""Safe client-facing error classification for SSE routes."""

from __future__ import annotations

import httpx
from openai import (
    APIConnectionError,
    APIStatusError,
    APITimeoutError,
    AuthenticationError,
    BadRequestError,
    NotFoundError,
    RateLimitError,
)
from tavily.errors import (
    BadRequestError as TavilyBadRequestError,
)
from tavily.errors import (
    ForbiddenError,
    InvalidAPIKeyError,
    MissingAPIKeyError,
    UsageLimitExceededError,
)
from tavily.errors import (
    TimeoutError as TavilyTimeoutError,
)

from app.config import Settings


def build_error_event(
    exc: Exception,
    *,
    settings: Settings,
    request_id: str,
) -> dict[str, object]:
    """Return a diagnosable development error without exposing upstream payloads."""
    code = "internal_error"
    detail = "internal error"

    if isinstance(exc, (InvalidAPIKeyError, MissingAPIKeyError, ForbiddenError)):
        code = "web_authentication_error"
        detail = "Tavily rejected the configured API key or access permissions."
    elif isinstance(exc, UsageLimitExceededError):
        code = "web_usage_limit_exceeded"
        detail = "Tavily usage is exhausted. Check the account quota before retrying."
    elif isinstance(exc, TavilyBadRequestError):
        code = "web_bad_request"
        detail = "Tavily rejected the search parameters."
    elif isinstance(exc, TavilyTimeoutError):
        code = "web_timeout"
        detail = "Tavily did not respond before the configured timeout."
    elif isinstance(exc, AuthenticationError):
        code = "upstream_authentication_error"
        detail = "Token Factory rejected the configured API key."
    elif isinstance(exc, NotFoundError):
        code = "upstream_model_not_found"
        detail = "Token Factory could not find the configured model or endpoint."
    elif isinstance(exc, (APITimeoutError, httpx.TimeoutException)):
        code = "upstream_timeout"
        detail = "Token Factory did not respond before the configured timeout."
    elif isinstance(exc, RateLimitError):
        code = "upstream_rate_limited"
        detail = "Token Factory rate-limited the request."
    elif isinstance(exc, BadRequestError):
        code = "upstream_bad_request"
        detail = "Token Factory rejected the request parameters."
    elif isinstance(exc, (APIConnectionError, httpx.NetworkError)):
        code = "upstream_unavailable"
        detail = "Token Factory could not be reached."
    elif isinstance(exc, APIStatusError) and exc.status_code >= 500:
        code = "upstream_unavailable"
        detail = "Token Factory returned a server error."

    event: dict[str, object] = {
        "code": "internal_error",
        "detail": "internal error",
        "requestId": request_id,
    }
    if settings.env == "development" and settings.nebius_debug_errors:
        event["code"] = code
        event["detail"] = detail
        event["upstreamType"] = type(exc).__name__
        if isinstance(exc, APIStatusError):
            event["upstreamStatus"] = exc.status_code
    return event
