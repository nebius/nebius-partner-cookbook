# Grounding — Real-Time Data with Tavily

Recipe **03 of 10** in the Agent Blueprint Recipes arc:

> Foundation → Knowledge → **Grounding** → Orchestration → Thread Memory → User Memory → Observability → Guardrails → Actions → Simulation

Cookbook #2 gave us a Pinecone-backed book recommender over a Goodreads-style
corpus.
That is useful domain memory, but it is still a snapshot.
The data stops around 2017, which is almost a decade old for a reader asking
what to buy, what edition exists, what is newly released, or what is currently
available.

A static vector dataset is also the wrong place for commercial facts.
Pricing, availability, bestseller context, formats, editions, and review buzz
change constantly.
Trying to bake those into the vector index would make ingestion heavier while
still going stale quickly.

So cookbook #3 keeps the book memory from cookbook #2 and adds the missing
layer: **live grounding with Tavily**, a Nebius partner.
Pinecone answers "what in my curated corpus is semantically relevant?".
Tavily answers "what changed on the web since this corpus was built?".
Nebius then synthesizes both into one streamed recommendation.

## What you'll build

A FastAPI service that answers book recommendation questions with this fixed
pipeline:

```mermaid
flowchart LR
    A[User book request] --> B[Nebius embedding]
    B --> C[Pinecone book knowledge]
    C --> D[Related books by author, theme, year]
    D --> E[Tavily fresh web search]
    E --> F[Nebius answer model]
    F --> G[SSE recommendation]
```

The route streams each phase to the client:

- `agent_message` events for human-readable progress
- `status` events for machine-readable phase changes
- `context` with the Pinecone book candidates
- `sources` with the Tavily web sources
- `token` events for the final answer
- `done` with elapsed time, token usage, and estimated cost

## Why Tavily here?

The vector index is intentionally curated and stable.
That makes it good for semantic recommendations, same-author expansion,
same-theme expansion, and same-year expansion.
It is not good for facts that move every week.

Tavily is used for freshness signals only:

- newer books adjacent to the reader's request
- current editions or formats
- availability and pricing context
- current discussion, reviews, awards, or bestseller context

The answer model receives both contexts and is instructed to keep them separate:
Goodreads/Pinecone citations use `[1]`, `[2]`, `[3]`; Tavily web citations use
`[W1]`, `[W2]`, `[W3]`.

## Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/)
- A Nebius API key
- A Pinecone API key
- A Tavily API key
- The Goodreads book vectors from cookbook #2 already upserted into Pinecone

## Run it

```bash
cd cookbooks/03-real-time-data-tavily
uv sync
cp .env.example .env
```

Fill:

```bash
NEBIUS_API_KEY=...
PINECONE_API_KEY=...
PINECONE_INDEX_NAME=books-demo
TAVILY_API_KEY=...
```

Then start the backend:

```bash
make dev
```

Send a request:

```bash
curl -N -X POST http://localhost:8000/agent/run \
  -H 'content-type: application/json' \
  -d '{
    "prompt": "Find cozy fantasy books launched after 2021 with recent review context",
    "top_k": 10,
    "related_top_k": 4,
    "include_related": true
  }'
```

## Sample SSE flow

```text
event: agent_message
data: {"text":"I am mapping your Dune request into the book index."}

event: status
data: {"phase":"embedding","message":"Preparing the semantic query"}

event: status
data: {"phase":"knowledge","message":"Requesting Pinecone Knowledge"}

event: context
data: {"books":[...]}

event: status
data: {"phase":"searching","message":"Requesting Tavily Results"}

event: sources
data: {"items":[...]}

event: status
data: {"phase":"synthesizing","message":"Synthesizing"}

event: token
data: {"text":"If you liked Dune..."}

event: token
data: {"text":"\n\n---\nTime: 4.31s | Tokens: 36 embed, 1420 in, 390 out | Cost: $0.000312"}

event: done
data: {"embeddingTokens":36,"inputTokens":1420,"outputTokens":390,"totalTokens":1846,"costUsd":0.000312,"elapsedSeconds":4.31}
```

## How it differs from cookbook #2

Cookbook #2 stops after Pinecone knowledge.
That is enough when the answer should stay inside the static corpus.

Cookbook #3 adds one more step before synthesis:

```python
fresh_sources = rag.search_fresh_context(prompt, books)
stream = rag.stream_synthesis(prompt, books, fresh_sources)
```

The Tavily query is built from the original user request plus the strongest
retrieved book titles.
That gives Tavily enough context to search for current information around the
reader's intent instead of doing a generic web search.

## Data and vectorization

This recipe reuses the same Pinecone index created in cookbook #2.
If you have not built it yet, run the vectorization flow there first:

```bash
cd cookbooks/02-domain-knowledge-pinecone-nexus
uv sync
uv run python scripts/vectorize_goodreads_to_pinecone.py \
  --data-dir ../../data \
  --embed-batch-size 100 \
  --embed-concurrency 6 \
  --pinecone-batch-size 200 \
  --progress-interval 1000
```

You can use your own data instead of Goodreads.
The only requirement is that your vectors carry enough metadata for the serving
path to render useful context: title, authors, themes or genres, ratings or
quality signals, and publication year when available.

## Configuration

| Variable | Required | Purpose |
|---|---:|---|
| `NEBIUS_API_KEY` | yes | Nebius Token Factory API key |
| `NEBIUS_MODEL` | no | Chat model for progress and synthesis |
| `NEBIUS_EMBEDDING_MODEL` | no | Embedding model for Pinecone knowledge |
| `PINECONE_API_KEY` | yes | Pinecone API key |
| `PINECONE_INDEX_NAME` | yes | Index containing the book vectors |
| `PINECONE_NAMESPACE` | no | Namespace for the Goodreads vectors |
| `TAVILY_API_KEY` | yes | Tavily API key |
| `TAVILY_SEARCH_DEPTH` | no | `basic` or `advanced` |
| `TAVILY_MAX_RESULTS` | no | Fresh web sources to fetch per request |

## Failure modes to design for

| Symptom | Cause | Handling |
|---|---|---|
| Good semantic matches but stale answer | Pinecone corpus is old | Tavily adds fresh web context before synthesis |
| Fresh sources are noisy | Web results are broader than the corpus | Keep Tavily capped and use it only for freshness claims |
| No Tavily results | Query is too narrow or web is unavailable | Still answer from Pinecone and avoid fresh claims |
| Missing citations | Model ignored the format | Add a critic/eval step in a later cookbook |

## Test it

```bash
uv run pytest
uv run ruff check
uv run ruff format --check
```

The tests monkeypatch Nebius, Pinecone, and Tavily, so they do not call the
network by default.

## Going further

- Add a dedicated small-model query planner before Tavily if you want multiple
  live searches per request.
- Cache Tavily responses for a few minutes to avoid repeat searches during demos.
- Add a critic pass that rejects uncited fresh claims before streaming `done`.
- Cookbook #4 rewrites the hand-wired flow as a LangGraph so planning,
  retrieval, writing, and memory have explicit state boundaries.

## License

MIT — see [`LICENSE`](../../LICENSE).
