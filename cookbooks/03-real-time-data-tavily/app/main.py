"""FastAPI app for the Pinecone-backed book RAG plus Tavily freshness recipe."""

from __future__ import annotations

from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app import __version__
from app.config import get_settings
from app.core.rate_limit import RateLimitMiddleware, build_rate_limit_store
from app.routes import agent, health


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    await app.state.rate_limit_store.connect()
    try:
        yield
    finally:
        await app.state.rate_limit_store.close()


settings = get_settings()

app = FastAPI(
    title="Real-Time Book Data with Pinecone and Tavily",
    version=__version__,
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url=None,
)

app.state.rate_limit_store = build_rate_limit_store(
    settings.rate_limit_redis_url,
    namespace="03-real-time-data-tavily",
)

app.add_middleware(
    RateLimitMiddleware,
    enabled=settings.rate_limit_enabled,
    requests_per_day=settings.rate_limit_requests_per_day,
    store=app.state.rate_limit_store,
    trust_proxy_headers=settings.rate_limit_trust_proxy_headers,
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
    allow_credentials=False,
)

app.include_router(health.router)
app.include_router(agent.router, prefix="/agent")
