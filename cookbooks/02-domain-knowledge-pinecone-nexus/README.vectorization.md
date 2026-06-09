# Vectorizing Goodreads datasets into Pinecone

The script in this recipe will:

1. analyze available Goodreads JSON dumps,
2. build a text payload from books, authors, works, and genres,
3. call Nebius embeddings with `Qwen/Qwen3-Embedding-8B`, and
4. pipeline concurrent embedding requests into Pinecone upserts in fixed-size batches.

## Files

Use datasets from the Goodreads mirror in one of these forms:

- `goodreads_books.json` or `goodreads_books.json.gz`
- `goodreads_book_authors.json` or `goodreads_book_authors.json.gz`
- `goodreads_book_works.json` or `goodreads_book_works.json.gz`
- `goodreads_book_genres_initial.json` or `goodreads_book_genres_initial.json.gz`

## Install

```bash
cd cookbooks/02-domain-knowledge-pinecone-nexus
uv sync
```

Load environment variables:

```bash
cp .env.vectorize.example .env.local
```

## Analyze only

```bash
cd cookbooks/02-domain-knowledge-pinecone-nexus
uv run python scripts/vectorize_goodreads_to_pinecone.py \
  --data-dir ../../data \
  --analyze-only
```

## Run with throughput defaults

```bash
cd cookbooks/02-domain-knowledge-pinecone-nexus
chmod +x scripts/run_vectorize_goodreads.sh
export PINECONE_INDEX_NAME=books-demo
export PINECONE_NAMESPACE=goodreads
export DATA_DIR=../../data
export EMBED_BATCH_SIZE=100
export EMBED_CONCURRENCY=6
export MAX_PENDING_EMBED_BATCHES=12
export PINECONE_BATCH_SIZE=200
export PROGRESS_INTERVAL=1000
./scripts/run_vectorize_goodreads.sh
```

If you only want to run the vectorizer command directly:

```bash
cd cookbooks/02-domain-knowledge-pinecone-nexus
uv run python scripts/vectorize_goodreads_to_pinecone.py \
  --data-dir ../../data \
  --embed-batch-size 100 \
  --embed-concurrency 6 \
  --pinecone-batch-size 200 \
  --progress-interval 1000
```

For a lower-noise debug run, you can still force one embedding request per
record:

```bash
cd cookbooks/02-domain-knowledge-pinecone-nexus
uv run python scripts/vectorize_goodreads_to_pinecone.py \
  --data-dir ../../data \
  --embed-batch-size 1 \
  --embed-concurrency 1 \
  --progress-interval 500
```

## Notes

- `--embed-concurrency` is the main throughput knob; start around `6` and raise it carefully.
- `--max-pending-embed-batches` bounds in-memory work queued between embedding and upsert.
- `--pinecone-batch-size` stays fixed at `150` or `200` for predictable index writes.
- To use `150` per Pinecone batch:

```bash
--pinecone-batch-size 150
```
- Books are prioritized and enriched with author names and genre labels when available.
- You can skip datasets with `--skip-books`, `--skip-authors`, and `--skip-genres`.
- Use `--include-empty-text` if you want to keep records with no extractable text.
- Progress is printed every `N` upserts using `--progress-interval N`.
