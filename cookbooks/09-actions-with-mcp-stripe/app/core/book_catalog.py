"""Local book catalog used by the Stripe action demo."""

from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path

from pydantic import BaseModel, Field, computed_field

SUPPORTED_CURRENCIES = ("usd", "eur", "gbp", "sgd")


class BookCatalogItem(BaseModel):
    """A fictional book that can be sold through a Stripe test checkout link."""

    slug: str = Field(..., min_length=1)
    title: str = Field(..., min_length=1)
    author: str = Field(..., min_length=1)
    isbn: str = Field(..., min_length=13, max_length=13, pattern=r"^\d{13}$")
    description: str = Field(..., min_length=1)
    prices: dict[str, int] = Field(..., min_length=1)
    cover_image_path: str | None = None
    stripe_product_id: str | None = None
    stripe_price_id: str | None = None

    @computed_field
    @property
    def amount(self) -> int:
        """Default USD amount used for compact approval displays."""
        return self.prices["usd"]

    @computed_field
    @property
    def currency(self) -> str:
        """Default currency for compact approval displays."""
        return "usd"

    @computed_field
    @property
    def formatted_prices(self) -> dict[str, str]:
        """Human-friendly prices for UI and docs responses."""
        return {currency: _format_minor_units(amount) for currency, amount in self.prices.items()}


class BookCatalog(BaseModel):
    """Loaded catalog with simple deterministic selection."""

    books: list[BookCatalogItem]

    def require_actionable_books(self) -> list[BookCatalogItem]:
        """Return books with Stripe Price IDs, or raise a useful setup error."""
        actionable = [book for book in self.books if book.stripe_price_id]
        if not actionable:
            raise RuntimeError(
                "No Stripe Price IDs found. Run `make seed-stripe-books` before approving "
                "checkout actions."
            )
        return actionable

    def select_for_prompt(self, prompt: str) -> BookCatalogItem:
        """Select the best matching book for a purchase prompt."""
        books = self.require_actionable_books()
        lower = prompt.lower()
        for book in books:
            if book.slug.replace("-", " ") in lower or book.title.lower() in lower:
                return book
        for book in books:
            if any(token and token in lower for token in book.author.lower().split()):
                return book
        return books[0]


def _format_minor_units(amount: int) -> str:
    return f"{amount / 100:.2f}"


def load_book_catalog(path: str) -> BookCatalog:
    """Load a book catalog JSON file from disk."""
    return _load_book_catalog(str(Path(path).expanduser().resolve()))


@lru_cache(maxsize=8)
def _load_book_catalog(resolved_path: str) -> BookCatalog:
    path = Path(resolved_path)
    if not path.exists():
        raise RuntimeError(
            f"Book catalog not found at {path}. Run `make seed-stripe-books` to create it."
        )
    data = json.loads(path.read_text(encoding="utf-8"))
    books = data["books"] if isinstance(data, dict) and "books" in data else data
    return BookCatalog(books=[BookCatalogItem.model_validate(item) for item in books])
