.PHONY: dev query vectorize

dev:
	uv run uvicorn app.main:app --host $${HOST:-0.0.0.0} --port $${PORT:-8000} --reload

query:
	uv run python scripts/query_goodreads_pinecone.py "Recommend books about political intrigue and empire-building for someone who liked Dune" --show-matches

vectorize:
	uv run python scripts/vectorize_goodreads_to_pinecone.py --data-dir ../../data --embed-batch-size 100 --embed-concurrency 6 --pinecone-batch-size 200 --progress-interval 1000
