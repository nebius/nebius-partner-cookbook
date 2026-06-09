"""Rate limit behavior stays local and deterministic in tests."""

from __future__ import annotations

from fastapi.testclient import TestClient
from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import PlainTextResponse
from starlette.routing import Route

from app.core.rate_limit import (
    InMemoryRateLimitStore,
    RateLimitMiddleware,
    RedisRateLimitStore,
    build_rate_limit_store,
)
from app.main import app


def test_daily_rate_limit_returns_429_after_quota() -> None:
    with TestClient(app) as client:
        for _ in range(25):
            response = client.get("/__rate_limit_probe__")
            assert response.status_code == 404
            assert response.headers["X-RateLimit-Limit"] == "25"

        response = client.get("/__rate_limit_probe__")

    assert response.status_code == 429
    assert response.json()["detail"] == "daily rate limit exceeded"
    assert response.json()["limit"] == 25
    assert response.headers["Retry-After"].isdigit()
    assert response.headers["X-RateLimit-Remaining"] == "0"


def test_health_routes_are_exempt_from_rate_limit() -> None:
    with TestClient(app) as client:
        for _ in range(30):
            response = client.get("/healthz")
            assert response.status_code == 200
            assert "X-RateLimit-Limit" not in response.headers


def test_rate_limit_can_be_disabled() -> None:
    async def ok(_request: Request) -> PlainTextResponse:
        return PlainTextResponse("ok")

    local_app = Starlette(routes=[Route("/probe", ok)])
    local_app.add_middleware(
        RateLimitMiddleware,
        enabled=False,
        requests_per_day=1,
        store=InMemoryRateLimitStore(),
        trust_proxy_headers=False,
    )

    with TestClient(local_app) as client:
        assert client.get("/probe").status_code == 200
        assert client.get("/probe").status_code == 200


def test_redis_url_selects_redis_store() -> None:
    store = build_rate_limit_store("redis://localhost:6379/0", namespace="test")

    assert isinstance(store, RedisRateLimitStore)
