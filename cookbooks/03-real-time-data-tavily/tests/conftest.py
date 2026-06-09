"""Shared test fixtures."""

from __future__ import annotations

import os

import pytest

os.environ.setdefault("NEBIUS_API_KEY", "test-nebius")
os.environ.setdefault("PINECONE_API_KEY", "test-pinecone")
os.environ.setdefault("PINECONE_INDEX_NAME", "test-index")
os.environ.setdefault("TAVILY_API_KEY", "test-tavily")
os.environ.setdefault("NEBIUS_ENABLE_PRICING_LOOKUP", "false")
os.environ["RATE_LIMIT_REDIS_URL"] = ""


@pytest.fixture(autouse=True)
def _reset_settings_cache():
    from app.config import get_settings
    from app.main import app

    get_settings.cache_clear()
    reset = getattr(app.state.rate_limit_store, "reset", None)
    if callable(reset):
        reset()
    yield
    get_settings.cache_clear()
    if callable(reset):
        reset()
