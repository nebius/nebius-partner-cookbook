"""Bind a request ID for routes and worker-thread logs."""

from __future__ import annotations

import uuid
from collections.abc import Awaitable, Callable

import structlog
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response


class RequestIDMiddleware(BaseHTTPMiddleware):
    async def dispatch(
        self, request: Request, call_next: Callable[[Request], Awaitable[Response]]
    ) -> Response:
        request_id = request.headers.get("x-request-id") or uuid.uuid4().hex
        request.state.request_id = request_id
        with structlog.contextvars.bound_contextvars(request_id=request_id, path=request.url.path):
            response = await call_next(request)
            response.headers["x-request-id"] = request_id
            return response
