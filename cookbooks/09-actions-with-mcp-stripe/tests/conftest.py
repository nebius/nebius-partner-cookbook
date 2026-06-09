"""Shared test fixtures. No network is ever hit: respx mocks Nebius."""

from __future__ import annotations

import json
import os

import pytest

os.environ.setdefault("NEBIUS_API_KEY", "test-key")
os.environ.setdefault("ENV", "development")
os.environ.setdefault("LOG_LEVEL", "warning")
os.environ.setdefault("CORS_ORIGINS", "http://localhost:3000")
os.environ.setdefault("LANGSMITH_TRACING", "false")
os.environ.setdefault("MEMORY_BACKEND", "memory")
os.environ.setdefault("STRIPE_MCP_API_KEY", "rk_test_mock")
os.environ.setdefault("STRIPE_SECRET_KEY", "sk_test_mock")
os.environ["RATE_LIMIT_REDIS_URL"] = ""


@pytest.fixture(autouse=True)
def _reset_settings_cache(tmp_path):
    """Ensure settings are re-read for every test."""
    catalog_path = tmp_path / "stripe_books.json"
    catalog_path.write_text(
        json.dumps(
            {
                "books": [
                    {
                        "slug": "the-nebius-cloud-atlas",
                        "title": "The Nebius Cloud Atlas",
                        "author": "Nia Vector",
                        "isbn": "9781600000010",
                        "description": "A fictional book for tests.",
                        "prices": {"usd": 1499, "eur": 1399, "gbp": 1199, "sgd": 1999},
                        "cover_image_path": "the-nebius-cloud-atlas.png",
                        "stripe_product_id": "prod_test_nebius",
                        "stripe_price_id": "price_test_nebius",
                    }
                ]
            }
        ),
        encoding="utf-8",
    )
    os.environ["BOOK_CATALOG_PATH"] = str(catalog_path)

    import app.core.approvals as approvals
    import app.core.book_catalog as book_catalog
    import app.core.langsmith_observability as langsmith_observability
    import app.core.long_term_memory as long_term_memory
    from app.config import get_settings
    from app.main import app

    get_settings.cache_clear()
    reset = getattr(app.state.rate_limit_store, "reset", None)
    if callable(reset):
        reset()
    approvals._approval_store = approvals.ApprovalStore()
    book_catalog._load_book_catalog.cache_clear()
    langsmith_observability._observer = None
    long_term_memory._memory_backend = long_term_memory.InMemoryLongTermMemoryStore()
    yield
    get_settings.cache_clear()
    if callable(reset):
        reset()
    approvals._approval_store = None
    book_catalog._load_book_catalog.cache_clear()
    langsmith_observability._observer = None
    long_term_memory._memory_backend = None
