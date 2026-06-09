"""FastAPI app entry point. Lifespan, middleware, and route wiring."""

from __future__ import annotations

import asyncio
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

import structlog
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from prometheus_client import CONTENT_TYPE_LATEST, generate_latest
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response

from app import __version__
from app.config import get_settings
from app.core.rate_limit import RateLimitMiddleware, build_rate_limit_store
from app.observability.logging import configure_logging
from app.observability.metrics import metrics_middleware
from app.observability.middleware import (
    RequestIDMiddleware,
    SecurityHeadersMiddleware,
    SizeLimitMiddleware,
)
from app.routes import agent, feedback, health, memory, threads

logger = structlog.get_logger()


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    settings = get_settings()
    configure_logging(settings.log_level, settings.env)
    logger.info(
        "startup",
        version=__version__,
        env=settings.env,
        model=settings.nebius_model,
    )
    await app.state.rate_limit_store.connect()
    try:
        yield
    finally:
        logger.info("shutdown")
        await app.state.rate_limit_store.close()
        await asyncio.sleep(0)


app = FastAPI(
    title="Nebius Cookbook — Adding Guardrails with LangChain",
    version=__version__,
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url=None,
)

settings = get_settings()
localhost_cors_regex = (
    r"^https?://(localhost|127\.0\.0\.1|\[::1\])(:\d+)?$"
    if settings.env == "development" and settings.allow_localhost_cors
    else None
)
app.state.rate_limit_store = build_rate_limit_store(
    settings.rate_limit_redis_url,
    namespace="08-adding-guardrails-langchain",
)

app.add_middleware(
    RateLimitMiddleware,
    enabled=settings.rate_limit_enabled,
    requests_per_day=settings.rate_limit_requests_per_day,
    store=app.state.rate_limit_store,
    trust_proxy_headers=settings.rate_limit_trust_proxy_headers,
)
app.add_middleware(BaseHTTPMiddleware, dispatch=metrics_middleware)
app.add_middleware(RequestIDMiddleware)
app.add_middleware(SecurityHeadersMiddleware)
app.add_middleware(SizeLimitMiddleware, max_bytes=settings.max_request_bytes)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_origin_regex=localhost_cors_regex,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
    allow_credentials=False,
    max_age=600,
)


@app.get("/metrics")
async def metrics() -> Response:
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)


app.include_router(health.router)
app.include_router(agent.router, prefix="/agent")
app.include_router(feedback.router)
app.include_router(threads.router)
app.include_router(memory.router)
