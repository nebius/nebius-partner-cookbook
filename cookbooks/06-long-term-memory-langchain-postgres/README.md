# User Memory — Long-Term Memory with LangChain and Postgres

> Persist user preferences and facts across conversation threads with a Postgres-backed memory layer.

Recipe **06 of 10** in the Agent Blueprint Recipes arc:

> Foundation → Knowledge → Grounding → Orchestration → Thread Memory → **User Memory** → Observability → Guardrails → Actions → Simulation

This recipe keeps the progression intact.
It still uses the LangGraph orchestration from Cookbook #4 and the short-term `thread_id` memory from Cookbook #5.
It adds durable `user_id` memory backed by Postgres so the agent can remember useful facts across new threads and process restarts.

The demo stays intentionally explicit.
The request body includes `user_id` because this cookbook has no auth layer.
In production, derive `user_id` from authenticated identity and ignore any user identifier supplied by the client.

## What you'll build

A FastAPI service that extends the orchestrated, thread-aware book agent:

1. **Inherited orchestration** — the `direct` / `deliberate` LangGraph route still chooses the response path.
2. **Inherited thread memory** — `thread_id` still loads and saves recent conversation turns.
3. **Postgres-backed user memory** — long-term facts and preferences survive process restarts.
4. **Bounded recall** — a small set of relevant memories is injected before the model writes.
5. **Privacy operations** — list, summarize, and delete endpoints let users inspect and remove stored context.
6. **Network-free tests** — tests use an in-memory backend and `respx`, so CI never calls Nebius or Postgres by default.

```text
request ──► thread_id ──► short-term checkpoint ──┐
        └─► user_id ─────► Postgres memory store ─┼─► LangGraph route ──► Nebius stream
                                                    └─► bounded recall
```

## Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/)
- Docker for local Postgres
- A Nebius API key from the [Nebius console](https://nebius.com)

## Run it

```bash
cp .env.example .env
# Open .env and fill NEBIUS_API_KEY.

docker compose up -d postgres
uv sync
make dev
```

In another terminal, store a durable user preference:

```bash
curl -N -X POST http://localhost:8000/agent/run \
  -H 'content-type: application/json' \
  -d '{"thread_id":"thread-a","user_id":"reader-42","prompt":"Remember that I prefer concise science fiction recommendations."}'
```

Then ask from a different thread:

```bash
curl -N -X POST http://localhost:8000/agent/run \
  -H 'content-type: application/json' \
  -d '{"thread_id":"thread-b","user_id":"reader-42","prompt":"Recommend one book for me."}'
```

The SSE stream includes memory status events:

```text
event: status
data: {"phase":"memory_loaded","threadId":"thread-b","userId":"reader-42","messages":0,"longTermMemories":1}

event: status
data: {"phase":"routed","route":"deliberate","contextNeed":"curated_recommendation"}

event: token
data: {"text":"..."}
```

## API Contract

### `POST /agent/run`

Runs the agent and streams named SSE events.

Request:

```json
{
  "thread_id": "thread-b",
  "user_id": "reader-42",
  "prompt": "Recommend one book for me.",
  "temperature": 0.4,
  "max_tokens": 1024,
  "history": []
}
```

Important request fields:

| Field | Required | Purpose |
| ----- | -------- | ------- |
| `thread_id` | yes | Short-term conversation continuity. |
| `user_id` | yes | Long-term memory namespace for this demo. |
| `prompt` | yes | Current user request. |
| `history` | no | Optional client-provided context; server-side memory is loaded separately. |

SSE events:

| Event | Meaning |
| ----- | ------- |
| `status` | Phase transitions such as `memory_loaded`, `routed`, `writing`, and `memory_saved`. |
| `token` | Nebius token deltas plus the final usage footer. |
| `done` | Final usage payload. |
| `error` | Recoverable API-level failure. |
| `heartbeat` | Long-running connection heartbeat. |

### Memory Endpoints

| Method | Path | Purpose |
| ------ | ---- | ------- |
| `GET` | `/memory/{user_id}` | List stored long-term memories. |
| `GET` | `/memory/{user_id}/summary` | Summarize what the agent knows about the user. |
| `DELETE` | `/memory/{user_id}` | Delete stored long-term memories for privacy or account deletion. |
| `DELETE` | `/threads/{thread_id}` | Delete process-local short-term thread memory. |

Example memory summary:

```bash
curl http://localhost:8000/memory/reader-42/summary
```

## Configuration

Every setting is validated by Pydantic at boot.
Copy `.env.example` and keep secrets out of code.

| Env var | Default | Purpose |
| ------- | ------- | ------- |
| `NEBIUS_API_KEY` | required | Nebius API key. |
| `NEBIUS_BASE_URL` | `https://api.studio.nebius.ai/v1/` | OpenAI-compatible Nebius endpoint. |
| `NEBIUS_MODEL` | `meta-llama/Llama-3.3-70B-Instruct` | Chat model. |
| `MEMORY_BACKEND` | `postgres` | `postgres` for local/prod, `memory` for tests. |
| `POSTGRESQL_ADDON_URI` | local Postgres URL | Postgres connection string. Clever Cloud injects this when a Postgres add-on is linked. |
| `LONG_TERM_MEMORY_LIMIT` | `5` | Maximum memories recalled or listed. |
| `CORS_ORIGINS` | `http://localhost:3000` | Browser allowlist. |
| `LOG_LEVEL` | `info` | Structured logging level. |

## Sharing one Postgres database

Postgres schemas let multiple cookbooks share one database without sharing tables.
Think of a schema as a folder inside the database: cookbook #6 writes to `dev_cbk_06.user_memories` locally and `prod_cbk_06.user_memories` in production.
The schema name is built from `ENV` and the cookbook number, so there is no extra environment variable to maintain.
Cookbooks #7-#10 inherit the same pattern with their own schemas, for example `prod_cbk_07`, `prod_cbk_08`, `prod_cbk_09`, and `prod_cbk_10`.

That gives you one managed Postgres instance, one connection URI, and isolated tables per cookbook.
The app creates the configured schema and `user_memories` table on first use.
For local development, keep `ENV=development`, which produces the `dev_cbk_NN` schemas.
For Clever Cloud, link the same Postgres add-on to each cookbook app.
Clever injects `POSTGRESQL_ADDON_URI`, which the app uses as its only Postgres connection string.
Set `ENV=production` and the app automatically uses `prod_cbk_06` for this cookbook.

## Implementation Notes

Long-term memory lives in `app/core/long_term_memory.py`.
The production backend creates a schema-qualified `user_memories` table and indexes records by `user_id` and `created_at`.
The test backend implements the same contract in memory.

Recall is deliberately bounded.
The agent never injects the full memory store into a prompt.
The route asks the long-term store for relevant memories, converts them into synthetic context, and then lets the inherited LangGraph route decide whether the prompt is direct or deliberate.

Memory extraction is deterministic in this cookbook.
It stores explicit user facts such as "remember that..." and "my favorite author is...".
A production system can replace this with a model-assisted memory writer, but keep the same privacy and deletion contracts.

## Production Checklist

- Derive `user_id` from auth instead of trusting request JSON.
- Use a managed Postgres instance with backups, migrations, and connection pooling.
- Keep `ENV=production` in deployed cookbook apps so memory lands in `prod_cbk_NN` schemas.
- Add row-level tenancy controls if multiple customers share the same database.
- Decide retention windows for user memories and checkpoints.
- Keep deletion paths tested because privacy workflows are product behavior, not admin utilities.
- Review stored memories for PII before expanding extraction beyond explicit user preferences.

## Failure Modes

| Symptom | Likely cause | Handling |
| ------- | ------------ | -------- |
| Agent forgets within one thread | Unstable `thread_id` | Keep `thread_id` stable per conversation and expose reset explicitly. |
| Agent forgets across threads | Missing or wrong `user_id` | Derive `user_id` from authenticated identity in production. |
| Memory leaks between users | Client-controlled `user_id` in a real app | Never trust request JSON for identity outside this demo. |
| Token usage grows | Too many recalled memories | Lower `LONG_TERM_MEMORY_LIMIT` or summarize memories. |
| Stale preferences affect answers | User changed their mind | Prefer newer memories and expose delete/edit flows. |

## Test It

```bash
uv run pytest
uv run ruff check
uv run ruff format --check
```

The tests mock Nebius with `respx`.
They use `MEMORY_BACKEND=memory`, so they do not require Postgres or network access.

## Going Further

- Replace deterministic extraction with a dedicated memory-writer node.
- Store memory provenance so users can see which prompt created a memory.
- Add edit endpoints for user-corrected memories.
- Move thread checkpoints to Postgres alongside long-term memory.
- Continue to Cookbook #7 to trace the full memory path with LangSmith.

## Reference

- LangChain long-term memory — [docs.langchain.com/oss/python/langchain/long-term-memory](https://docs.langchain.com/oss/python/langchain/long-term-memory)

## License

MIT
