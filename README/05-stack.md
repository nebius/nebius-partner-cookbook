## Stack

The **recipe** stack is deliberately small and boring. Every recipe makes the same technical choices so that what you learn in one cookbook transfers directly to the next. **Blueprints** are not bound by this — a blueprint picks whatever a real application of its kind would use (e.g. a React frontend, LangGraph for orchestration and deployment, Pinecone for knowledge), so its stack is documented in its own README.

### Recipes (Python)

| Layer | Choice | Why |
|---|---|---|
| Language | Python 3.12 | Modern type system, broad ecosystem |
| Package manager | [uv](https://docs.astral.sh/uv/) | Fast, reproducible, lockfile-first |
| HTTP framework | [FastAPI](https://fastapi.tiangolo.com) | Async, Pydantic-native, OpenAPI for free |
| ASGI server | Uvicorn | The boring standard |
| LLM SDK | [openai-python](https://github.com/openai/openai-python) pointed at Nebius | Familiar API, no vendor lock-in to switch later |
| Config | [pydantic-settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/) | Type-safe env validation at boot |
| Logging | [structlog](https://www.structlog.org/) (JSON in prod) | Structured logs you can actually query |
| Metrics | [prometheus-client](https://github.com/prometheus/client_python) | `/metrics` endpoint, standard format |
| Rate limit | FastAPI middleware + Redis fallback | Per-IP daily quotas, Redis when configured, in-memory locally |
| HTTP client | [httpx](https://www.python-httpx.org) with explicit timeouts | First-class async |
| Retries | [tenacity](https://tenacity.readthedocs.io) | Exponential backoff for transient errors |
| Tests | pytest + pytest-asyncio + [respx](https://lundberg.github.io/respx/) | No network in tests |
| Lint/format | [ruff](https://docs.astral.sh/ruff/) | One tool, no mypy (intentional) |

Backend rate limiting is documented in [`docs/rate-limiting.md`](docs/rate-limiting.md), including Redis setup, GitHub/Clever variables, headers, and 429 examples.

### Catalog site (JS/TS)

| Layer | Choice |
|---|---|
| Framework | Next.js 15 (App Router) |
| Runtime in dev/CI | Bun |
| Runtime in prod | Node 22 LTS (on [Clever Cloud](https://www.clever-cloud.com)) |
| Styling | Tailwind CSS + [Radix Themes](https://www.radix-ui.com/themes) |
| Content | Cookbook READMEs compiled to MDX at build time |
| Hosting | Clever Cloud (static + tiny Node runtime) |

### Why these choices

Every choice optimizes for being **boring**, **fast to onboard**, and **production-safe by default**.
