## Getting started

### Run a recipe

Every recipe is independent. Pick one, clone the repo, and follow the recipe's own README.

```bash
git clone https://github.com/nebius/nebius-partner-cookbook.git
cd cookbook/cookbooks/01-first-agent-on-nebius

cp .env.example .env
# Open .env and fill NEBIUS_API_KEY

uv sync
make dev
```

In another terminal:

```bash
curl -N -X POST http://localhost:8000/agent/run \
  -H 'content-type: application/json' \
  -d '{"prompt":"Explain Nebius AgentKit in one paragraph."}'
```

You should see Server-Sent Events streaming back, with `status`, `token`, and `done` events.

### Run a blueprint

Blueprints are larger, self-contained applications under [`blueprints/`](./blueprints/). Each has its own README, `Makefile`, and setup. For example, the Sentinel compliance auditor:

```bash
git clone https://github.com/nebius/nebius-partner-cookbook.git
cd nebius-partner-cookbook/blueprints/sentinel-compliance-auditor

cp .env.example .env
# Fill NEBIUS_API_KEY, PINECONE_API_KEY, TAVILY_API_KEY

make install
make ingest && make ingest-regulations   # build the Pinecone knowledge base
make dev                                  # LangGraph dev server
make ui                                   # FastAPI + React UI
```

See [`blueprints/sentinel-compliance-auditor/README.md`](./blueprints/sentinel-compliance-auditor/README.md) for the full walkthrough.

### Prerequisites

A laptop with:

- **Python 3.12** and [**uv**](https://docs.astral.sh/uv/) — for running cookbook recipes
- **Node 22** and [**Bun ≥ 1.1**](https://bun.sh) — only if you're working on the catalog site or build scripts
- A **Nebius API key** — get one from the [Nebius console](https://nebius.com)
- Optional: **Docker** — for building production images

If you only plan to read code and run one recipe, Python and uv are all you need.

### Work on the catalog site

The Next.js site that hosts this catalog lives in `app/`.

```bash
bun install
bun run build:content   # compile recipe + blueprint READMEs to MDX
cd app
bun run dev
```
