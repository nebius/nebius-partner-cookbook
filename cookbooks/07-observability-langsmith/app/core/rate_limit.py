"""Daily per-IP rate limiting with Redis and in-memory backends."""

from __future__ import annotations

import asyncio
import time
from dataclasses import dataclass
from typing import Any, Protocol

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse, Response
from starlette.types import ASGIApp

WINDOW_SECONDS = 86_400
EXEMPT_PATHS = frozenset(
    {
        "/healthz",
        "/readyz",
        "/metrics",
        "/docs",
        "/openapi.json",
        "/favicon.ico",
    }
)

REDIS_HIT_SCRIPT = """
local current = redis.call("INCR", KEYS[1])
if current == 1 then
  redis.call("EXPIRE", KEYS[1], ARGV[1])
end
local ttl = redis.call("TTL", KEYS[1])
return {current, ttl}
"""


@dataclass(frozen=True)
class RateLimitResult:
    """Result returned by a rate limit store after counting a request."""

    allowed: bool
    limit: int
    remaining: int
    reset_at: int
    retry_after: int


class RateLimitStore(Protocol):
    """Storage contract used by the middleware."""

    async def connect(self) -> None:
        """Open the backing store connection, if needed."""

    async def close(self) -> None:
        """Close the backing store connection, if needed."""

    async def hit(self, key: str, limit: int, window_seconds: int) -> RateLimitResult:
        """Count one request and return the current limit decision."""


class InMemoryRateLimitStore:
    """Process-local rate limit store for local demos and tests."""

    def __init__(self) -> None:
        self._lock = asyncio.Lock()
        self._buckets: dict[str, tuple[int, float]] = {}

    async def connect(self) -> None:
        return None

    async def close(self) -> None:
        return None

    def reset(self) -> None:
        """Clear counters between tests."""
        self._buckets.clear()

    async def hit(self, key: str, limit: int, window_seconds: int) -> RateLimitResult:
        now = time.time()
        async with self._lock:
            count, reset_at = self._buckets.get(key, (0, now + window_seconds))
            if now >= reset_at:
                count = 0
                reset_at = now + window_seconds

            if count >= limit:
                remaining = 0
                retry_after = max(0, int(reset_at - now))
                return RateLimitResult(
                    allowed=False,
                    limit=limit,
                    remaining=remaining,
                    reset_at=int(reset_at),
                    retry_after=retry_after,
                )

            count += 1
            self._buckets[key] = (count, reset_at)
            remaining = max(0, limit - count)
            return RateLimitResult(
                allowed=True,
                limit=limit,
                remaining=remaining,
                reset_at=int(reset_at),
                retry_after=0,
            )


class RedisRateLimitStore:
    """Redis-backed rate limit store for multi-instance deployments."""

    def __init__(self, redis_url: str, prefix: str) -> None:
        self._redis_url = redis_url
        self._prefix = prefix
        self._redis: Any | None = None

    async def connect(self) -> None:
        if self._redis is not None:
            return

        try:
            from redis import asyncio as redis
        except ImportError as exc:  # pragma: no cover - exercised only with missing dependency.
            raise RuntimeError(
                "RATE_LIMIT_REDIS_URL is set, but the 'redis' package is not installed."
            ) from exc

        self._redis = redis.from_url(self._redis_url, encoding="utf-8", decode_responses=True)
        await self._redis.ping()

    async def close(self) -> None:
        if self._redis is None:
            return

        await self._redis.aclose()
        self._redis = None

    async def hit(self, key: str, limit: int, window_seconds: int) -> RateLimitResult:
        if self._redis is None:
            await self.connect()

        redis_client = self._redis
        if redis_client is None:
            raise RuntimeError("Redis rate limit store was not initialized.")

        redis_key = f"{self._prefix}:{key}"
        current, ttl = await redis_client.eval(REDIS_HIT_SCRIPT, 1, redis_key, window_seconds)
        count = int(current)
        ttl_seconds = int(ttl)
        if ttl_seconds < 0:
            await redis_client.expire(redis_key, window_seconds)
            ttl_seconds = window_seconds

        remaining = max(0, limit - count)
        allowed = count <= limit
        retry_after = 0 if allowed else max(0, ttl_seconds)
        reset_at = int(time.time()) + max(0, ttl_seconds)
        return RateLimitResult(
            allowed=allowed,
            limit=limit,
            remaining=remaining,
            reset_at=reset_at,
            retry_after=retry_after,
        )


def build_rate_limit_store(redis_url: str | None, namespace: str) -> RateLimitStore:
    """Create the Redis store when configured, otherwise use process memory."""
    if redis_url and redis_url.strip():
        return RedisRateLimitStore(
            redis_url=redis_url.strip(),
            prefix=f"nebius-cookbook:{namespace}:rate-limit",
        )
    return InMemoryRateLimitStore()


class RateLimitMiddleware(BaseHTTPMiddleware):
    """Reject requests once an IP reaches its daily backend quota."""

    def __init__(
        self,
        app: ASGIApp,
        *,
        enabled: bool,
        requests_per_day: int,
        store: RateLimitStore,
        trust_proxy_headers: bool,
        exempt_paths: frozenset[str] = EXEMPT_PATHS,
    ) -> None:
        super().__init__(app)
        self._enabled = enabled
        self._requests_per_day = requests_per_day
        self._store = store
        self._trust_proxy_headers = trust_proxy_headers
        self._exempt_paths = exempt_paths

    async def dispatch(self, request: Request, call_next: Any) -> Response:
        if not self._enabled or self._is_exempt(request):
            return await call_next(request)

        result = await self._store.hit(
            key=self._client_key(request),
            limit=self._requests_per_day,
            window_seconds=WINDOW_SECONDS,
        )
        headers = self._headers(result)

        if not result.allowed:
            return JSONResponse(
                {
                    "detail": "daily rate limit exceeded",
                    "limit": result.limit,
                    "window": "24h",
                    "retryAfterSeconds": result.retry_after,
                },
                status_code=429,
                headers=headers,
            )

        response = await call_next(request)
        for header, value in headers.items():
            response.headers.setdefault(header, value)
        return response

    def _is_exempt(self, request: Request) -> bool:
        path = request.url.path
        return (
            request.method == "OPTIONS" or path in self._exempt_paths or path.startswith("/docs/")
        )

    def _client_key(self, request: Request) -> str:
        if self._trust_proxy_headers:
            forwarded_for = request.headers.get("x-forwarded-for")
            if forwarded_for:
                return forwarded_for.split(",", maxsplit=1)[0].strip()

            forwarded = request.headers.get("forwarded")
            if forwarded:
                for part in forwarded.split(";"):
                    key, _, value = part.strip().partition("=")
                    if key.lower() == "for" and value:
                        return value.strip('"')

        if request.client is None:
            return "unknown"
        return request.client.host

    @staticmethod
    def _headers(result: RateLimitResult) -> dict[str, str]:
        headers = {
            "X-RateLimit-Limit": str(result.limit),
            "X-RateLimit-Remaining": str(result.remaining),
            "X-RateLimit-Reset": str(result.reset_at),
        }
        if not result.allowed:
            headers["Retry-After"] = str(result.retry_after)
        return headers
