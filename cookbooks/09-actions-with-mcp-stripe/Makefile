.PHONY: dev seed-stripe-books test lint format docker run-docker deploy clean

PORT ?= 8000

dev:
	uv run uvicorn app.main:app --reload --host 0.0.0.0 --port $(PORT)

seed-stripe-books:
	uv run python scripts/seed_stripe_books.py

test:
	uv run pytest -v

lint:
	uv run ruff check
	uv run ruff format --check

format:
	uv run ruff format
	uv run ruff check --fix

docker:
	docker build -t cookbook-09-actions:dev .

run-docker:
	docker run --rm -p $(PORT):8000 --env-file .env cookbook-09-actions:dev

deploy:
	@echo "See docs/deployment.md for Nebius Compute deployment instructions."

clean:
	rm -rf .pytest_cache .ruff_cache __pycache__ .venv
	find . -type d -name __pycache__ -exec rm -rf {} +
