.PHONY: dev test lint format docker run-docker deploy clean

PORT ?= 8000

dev:
	uv run uvicorn app.main:app --reload --host 0.0.0.0 --port $(PORT)

test:
	uv run pytest -v

lint:
	uv run ruff check
	uv run ruff format --check

format:
	uv run ruff format
	uv run ruff check --fix

docker:
	docker build -t cookbook-template:dev .

run-docker:
	docker run --rm -p $(PORT):8000 --env-file .env cookbook-template:dev

deploy:
	@echo "See docs/deployment.md for Nebius Compute deployment instructions."

clean:
	rm -rf .pytest_cache .ruff_cache __pycache__ .venv
	find . -type d -name __pycache__ -exec rm -rf {} +
