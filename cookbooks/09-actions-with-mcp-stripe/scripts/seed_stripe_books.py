"""Create Stripe test-mode Products and Prices for the cookbook catalog."""

from __future__ import annotations

import argparse
import asyncio
import json
import os
from pathlib import Path
from typing import Any

import httpx

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE = ROOT / "scripts" / "data" / "books.json"
DEFAULT_OUTPUT = ROOT / "data" / "stripe_books.json"
STRIPE_API_BASE = "https://api.stripe.com/v1"


class SeedError(RuntimeError):
    """Raised when the seed command cannot complete."""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument(
        "--image-base-url",
        default=os.environ.get("STRIPE_IMAGE_BASE_URL"),
        help="Optional public base URL for cover images. Local files are stored as metadata only.",
    )
    parser.add_argument("--force", action="store_true", help="Create fresh products and prices.")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Validate input without calling Stripe.",
    )
    return parser.parse_args()


async def seed_books(
    *,
    source: Path = DEFAULT_SOURCE,
    output: Path = DEFAULT_OUTPUT,
    force: bool = False,
    dry_run: bool = False,
    stripe_secret_key: str | None = None,
    image_base_url: str | None = None,
) -> dict[str, Any]:
    """Seed Stripe Products/Prices and write the generated catalog."""
    if await asyncio.to_thread(output.exists) and not force and not dry_run:
        existing = await asyncio.to_thread(output.read_text, encoding="utf-8")
        payload = json.loads(existing)
        if _catalog_uses_deterministic_product_ids(payload):
            if image_base_url:
                secret_key = stripe_secret_key or os.environ.get("STRIPE_SECRET_KEY")
                if not secret_key:
                    raise SeedError("STRIPE_SECRET_KEY is required to sync Stripe product images.")
                await _sync_existing_product_images(
                    payload,
                    stripe_secret_key=secret_key,
                    image_base_url=image_base_url,
                )
            return payload
    books = _load_books(source)
    _normalize_cover_paths(books, source.parent)
    missing_covers = [
        book["cover_image_path"]
        for book in books
        if book.get("cover_image_path") and not book.get("cover_image_exists")
    ]
    if missing_covers:
        missing = ", ".join(missing_covers)
        raise SeedError(f"Missing local cover image(s) next to {source}: {missing}")
    if dry_run:
        return {"books": books, "dryRun": True}

    secret_key = stripe_secret_key or os.environ.get("STRIPE_SECRET_KEY")
    if not secret_key:
        raise SeedError("STRIPE_SECRET_KEY is required to seed Stripe products.")

    seeded: list[dict[str, Any]] = []
    async with httpx.AsyncClient(
        base_url=STRIPE_API_BASE,
        auth=(secret_key, ""),
        timeout=httpx.Timeout(connect=5, read=30, write=10, pool=5),
    ) as client:
        for book in books:
            product = await _create_or_update_product(client, book, image_base_url=image_base_url)
            price = await _create_price(client, book, product["id"])
            seeded.append(
                {
                    **book,
                    "stripe_product_id": product["id"],
                    "stripe_price_id": price["id"],
                }
            )

    await asyncio.to_thread(output.parent.mkdir, parents=True, exist_ok=True)
    payload = {"books": seeded}
    await asyncio.to_thread(
        output.write_text,
        json.dumps(payload, indent=2) + "\n",
        encoding="utf-8",
    )
    return payload


def _load_books(source: Path) -> list[dict[str, Any]]:
    data = json.loads(source.read_text(encoding="utf-8"))
    books = data["books"] if isinstance(data, dict) and "books" in data else data
    if not isinstance(books, list) or not books:
        raise SeedError("Book seed file must contain a non-empty books array.")
    return [dict(book) for book in books]


def _normalize_cover_paths(books: list[dict[str, Any]], source_dir: Path) -> None:
    """Keep cover paths relative to the JSON file and flag missing local images."""
    for book in books:
        cover_path = book.get("cover_image_path")
        if not isinstance(cover_path, str) or not cover_path:
            continue
        local_path = source_dir / cover_path
        book["cover_image_exists"] = local_path.exists()


def _catalog_uses_deterministic_product_ids(payload: dict[str, Any]) -> bool:
    books = payload.get("books", [])
    if not isinstance(books, list) or not books:
        return False
    for book in books:
        if not isinstance(book, dict):
            return False
        if book.get("stripe_product_id") != _stripe_product_id(book):
            return False
    return True


def _stripe_product_id(book: dict[str, Any]) -> str:
    isbn = str(book["isbn"]).replace("-", "")
    return f"nebius_partners_book_{isbn}"


def _product_payload(
    book: dict[str, Any],
    *,
    image_base_url: str | None,
    include_id: bool,
) -> dict[str, str]:
    data = {
        "name": str(book["title"]),
        "description": str(book["description"]),
        "metadata[nebius_cookbook_slug]": str(book["slug"]),
        "metadata[nebius_cookbook]": "09-actions-with-mcp-stripe",
        "metadata[isbn]": str(book["isbn"]),
        "metadata[cover_image_path]": str(book.get("cover_image_path", "")),
    }
    if include_id:
        data["id"] = _stripe_product_id(book)
    image_url = _cover_image_url(image_base_url, book)
    if image_url:
        data["images[0]"] = image_url
    return data


async def _create_or_update_product(
    client: httpx.AsyncClient,
    book: dict[str, Any],
    *,
    image_base_url: str | None,
) -> dict[str, Any]:
    product_id = _stripe_product_id(book)
    existing = await client.get(f"/products/{product_id}")
    if existing.status_code == 200:
        response = await client.post(
            f"/products/{product_id}",
            data=_product_payload(book, image_base_url=image_base_url, include_id=False),
        )
        response.raise_for_status()
        return response.json()
    if existing.status_code != 404:
        existing.raise_for_status()

    response = await client.post(
        "/products",
        data=_product_payload(book, image_base_url=image_base_url, include_id=True),
    )
    response.raise_for_status()
    return response.json()


async def _sync_existing_product_images(
    payload: dict[str, Any],
    *,
    stripe_secret_key: str,
    image_base_url: str,
) -> None:
    books = payload.get("books", [])
    if not isinstance(books, list):
        raise SeedError("Generated catalog must contain a books array.")

    async with httpx.AsyncClient(
        base_url=STRIPE_API_BASE,
        auth=(stripe_secret_key, ""),
        timeout=httpx.Timeout(connect=5, read=30, write=10, pool=5),
    ) as client:
        for book in books:
            if not isinstance(book, dict):
                continue
            product_id = book.get("stripe_product_id")
            image_url = _cover_image_url(image_base_url, book)
            if not product_id or not image_url:
                continue
            response = await client.post(
                f"/products/{product_id}",
                data={"images[0]": image_url},
            )
            response.raise_for_status()


def _cover_image_url(image_base_url: str | None, book: dict[str, Any]) -> str | None:
    cover_path = book.get("cover_image_path")
    if not image_base_url or not isinstance(cover_path, str) or not cover_path:
        return None
    return f"{image_base_url.rstrip('/')}/{cover_path}"


async def _create_price(
    client: httpx.AsyncClient,
    book: dict[str, Any],
    product_id: str,
) -> dict[str, Any]:
    prices = book["prices"]
    data = {
        "product": product_id,
        "currency": "usd",
        "unit_amount": str(prices["usd"]),
        "metadata[nebius_cookbook_slug]": book["slug"],
        "metadata[nebius_cookbook]": "09-actions-with-mcp-stripe",
        "metadata[isbn]": book["isbn"],
        "metadata[cover_image_path]": book.get("cover_image_path", ""),
    }
    for currency in ("eur", "gbp", "sgd"):
        data[f"currency_options[{currency}][unit_amount]"] = str(prices[currency])

    response = await client.post(
        "/prices",
        data=data,
    )
    response.raise_for_status()
    return response.json()


async def _main() -> None:
    args = parse_args()
    payload = await seed_books(
        source=args.source,
        output=args.output,
        force=args.force,
        dry_run=args.dry_run,
        image_base_url=args.image_base_url,
    )
    count = len(payload.get("books", []))
    mode = "validated" if args.dry_run else "seeded"
    print(f"{mode} {count} books")
    if not args.dry_run:
        print(f"wrote {args.output}")


if __name__ == "__main__":
    asyncio.run(_main())
