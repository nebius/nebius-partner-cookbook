"""Tests for the Stripe catalog seed script."""

from __future__ import annotations

import json
import os

import httpx
import pytest
import respx

from scripts.seed_stripe_books import seed_books


@pytest.mark.asyncio
@respx.mock
async def test_seed_books_creates_products_prices_and_writes_catalog(tmp_path) -> None:
    source = tmp_path / "books.json"
    output = tmp_path / "generated" / "stripe_books.json"
    source.write_text(
        json.dumps(
            {
                "books": [
                    {
                        "slug": "test-book",
                        "title": "Test Book",
                        "author": "Ada Reader",
                        "isbn": "9781600000997",
                        "description": "A test book.",
                        "prices": {"usd": 1200, "eur": 1100, "gbp": 950, "sgd": 1600},
                        "cover_image_path": "test-book.png",
                    }
                ]
            }
        ),
        encoding="utf-8",
    )
    (tmp_path / "test-book.png").write_bytes(b"fake image")
    product_id = "nebius_partners_book_9781600000997"
    product_get_route = respx.get(f"https://api.stripe.com/v1/products/{product_id}").mock(
        return_value=httpx.Response(404, json={"error": {"type": "invalid_request_error"}})
    )
    product_route = respx.post("https://api.stripe.com/v1/products").mock(
        return_value=httpx.Response(200, json={"id": product_id})
    )
    price_route = respx.post("https://api.stripe.com/v1/prices").mock(
        return_value=httpx.Response(200, json={"id": "price_test_123"})
    )

    payload = await seed_books(
        source=source,
        output=output,
        stripe_secret_key=os.environ["STRIPE_SECRET_KEY"],
        image_base_url="https://cdn.example.test/books",
    )

    assert payload["books"][0]["stripe_product_id"] == product_id
    assert payload["books"][0]["stripe_price_id"] == "price_test_123"
    assert json.loads(output.read_text(encoding="utf-8")) == payload
    assert product_get_route.calls.call_count == 1
    assert product_route.calls.call_count == 1
    assert price_route.calls.call_count == 1
    product_body = product_route.calls.last.request.content.decode("utf-8")
    assert "id=nebius_partners_book_9781600000997" in product_body
    assert "metadata%5Bisbn%5D=9781600000997" in product_body
    assert "metadata%5Bcover_image_path%5D=test-book.png" in product_body
    assert "images%5B0%5D=https%3A%2F%2Fcdn.example.test%2Fbooks%2Ftest-book.png" in product_body
    price_body = price_route.calls.last.request.content.decode("utf-8")
    assert "metadata%5Bisbn%5D=9781600000997" in price_body
    assert "metadata%5Bcover_image_path%5D=test-book.png" in price_body
    assert "unit_amount=1200" in price_body
    assert "currency_options%5Beur%5D%5Bunit_amount%5D=1100" in price_body
    assert "currency_options%5Bgbp%5D%5Bunit_amount%5D=950" in price_body
    assert "currency_options%5Bsgd%5D%5Bunit_amount%5D=1600" in price_body


@pytest.mark.asyncio
@respx.mock
async def test_seed_books_reuses_existing_output_without_force(tmp_path) -> None:
    source = tmp_path / "books.json"
    output = tmp_path / "generated" / "stripe_books.json"
    source.write_text('{"books":[]}', encoding="utf-8")
    output.parent.mkdir(parents=True)
    existing_payload = {
        "books": [
            {
                "slug": "existing",
                "isbn": "9781600000997",
                "stripe_product_id": "nebius_partners_book_9781600000997",
                "stripe_price_id": "price_existing_123",
            }
        ]
    }
    output.write_text(json.dumps(existing_payload), encoding="utf-8")

    payload = await seed_books(
        source=source,
        output=output,
        stripe_secret_key=os.environ["STRIPE_SECRET_KEY"],
    )

    assert payload == existing_payload


@pytest.mark.asyncio
@respx.mock
async def test_seed_books_syncs_images_for_existing_output(tmp_path) -> None:
    source = tmp_path / "books.json"
    output = tmp_path / "generated" / "stripe_books.json"
    source.write_text('{"books":[]}', encoding="utf-8")
    output.parent.mkdir(parents=True)
    output.write_text(
        json.dumps(
            {
                "books": [
                    {
                        "slug": "existing",
                        "cover_image_path": "existing.png",
                        "isbn": "9781600000997",
                        "stripe_product_id": "nebius_partners_book_9781600000997",
                        "stripe_price_id": "price_existing_123",
                    }
                ]
            }
        ),
        encoding="utf-8",
    )
    product_route = respx.post(
        "https://api.stripe.com/v1/products/nebius_partners_book_9781600000997"
    ).mock(return_value=httpx.Response(200, json={"id": "nebius_partners_book_9781600000997"}))

    payload = await seed_books(
        source=source,
        output=output,
        stripe_secret_key=os.environ["STRIPE_SECRET_KEY"],
        image_base_url="https://cdn.example.test/books",
    )

    assert payload["books"][0]["stripe_product_id"] == "nebius_partners_book_9781600000997"
    assert product_route.calls.call_count == 1
    product_body = product_route.calls.last.request.content.decode("utf-8")
    assert "images%5B0%5D=https%3A%2F%2Fcdn.example.test%2Fbooks%2Fexisting.png" in product_body
