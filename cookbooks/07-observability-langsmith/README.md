# Observability — Observability with LangSmith

> Trace, inspect, annotate, and debug a stateful Nebius-backed agent with LangSmith.

Recipe **07 of 10** in the Agent Blueprint Recipes arc:

> Foundation → Knowledge → Grounding → Orchestration → Thread Memory → User Memory → **Observability** → Guardrails → Actions → Simulation

By this point the agent can answer, orchestrate, remember a thread, and persist user memory in Postgres.
The next production problem is visibility.
When a run is bad, slow, expensive, or surprising, logs alone do not show the full chain of prompt, memory, route, model call, and output.

This recipe keeps everything from Cookbook #6 and adds LangSmith as the agent-run observability layer.
Prometheus still answers aggregate service questions.
LangSmith answers per-run behavior questions.

## What is a trace?

A trace is the complete execution tree for one agent request.
The root run is the request-level operation, and each meaningful internal step is a child run, often called a span.
In this cookbook the root run is `agent.run`.
Its children show memory recall, graph routing, prompt rendering, the Nebius model stream, memory persistence, and feedback correlation.

That tree matters in production because an agent failure is rarely just "the model was bad."
It may be bad recalled memory, an unexpected route, a bloated prompt, a slow model stream, a malformed output, or user feedback attached after the response.
Logs can show that each step happened.
A trace shows how the steps fit together for the exact request a reviewer is investigating.

## What you'll build

A FastAPI service that extends the long-term-memory agent:

1. **Inherited orchestration** — the LangGraph route from Cookbook #4 still chooses the response path.
2. **Inherited memory** — `thread_id`, `user_id`, Postgres memory, memory summary, and deletion endpoints remain intact.
3. **LangSmith tracing** — each run is traced with metadata, tags, redacted previews, and annotated child spans.
4. **Feedback capture** — reviewers can attach feedback to a LangSmith run.
5. **Privacy-aware telemetry** — traces store previews and identifiers, not raw secrets or unnecessary PII.
6. **Credential-free local runs** — tracing is off by default so the recipe works without a LangSmith account.

```text
request ──► memory recall ──► LangGraph route ──► Nebius stream ──► SSE
              │                    │                  │
              └────────────────────┴──────────────────┘
                              LangSmith trace
```

## Trace Shape

The code uses LangSmith annotations on the functions that are useful to inspect:

| Span | Run type | Why it exists |
| ---- | -------- | ------------- |
| `agent.run` | `chain` | Root request trace and feedback target. |
| `agent.load_context` | `retriever` | Loads short-term thread history and long-term user memories. |
| `thread_memory.get_history` | `retriever` | Shows whether local thread memory contributed context. |
| `long_term_memory.postgres.recall` | `retriever` | Shows durable user memory lookup. |
| `agent.stream_response` | `chain` | Streams the graph and writer path. |
| `agent.route_request` | `chain` | Records the graph routing decision. |
| `agent.render_prompt_messages` | `chain` | Shows prompt assembly after memory injection. |
| `nebius.chat_stream` | `llm` | Measures the Nebius model call and token usage. |
| `agent.persist_context` | `tool` | Saves short-term and long-term memory after the answer. |
| `long_term_memory.extract_memories` | `chain` | Shows deterministic memory extraction. |

The annotations use `process_inputs`, `process_outputs`, and stream reducers from `app/core/langsmith_annotations.py`.
That keeps traces readable and prevents streamed token chunks, secrets, and common direct identifiers from being stored verbatim.

## Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/)
- Postgres 15+ running locally
- A Nebius API key from the [Nebius console](https://nebius.com)
- A LangSmith API key from [LangSmith](https://docs.langchain.com/langsmith/home)

## Run it

```bash
cp .env.example .env
# Fill NEBIUS_API_KEY and LANGSMITH_API_KEY.

createdb nebius_cookbook
uv sync
make dev
```

Run the traced agent:

```bash
curl -N -X POST http://localhost:8000/agent/run \
  -H 'content-type: application/json' \
  -d '{"thread_id":"trace-demo","user_id":"reader-42","prompt":"Recommend one short book about observability."}'
```

When tracing is disabled, the response still works and `langsmithRunId` is `null`.
When tracing is enabled, `memory_loaded` includes the LangSmith run id.

```text
event: status
data: {"phase":"memory_loaded","threadId":"trace-demo","userId":"reader-42","langsmithRunId":"...","messages":0,"longTermMemories":0}
```

Attach feedback to a run:

```bash
curl -X POST http://localhost:8000/feedback \
  -H 'content-type: application/json' \
  -d '{"run_id":"RUN_ID_FROM_STREAM","key":"user_rating","score":1,"comment":"Useful answer."}'
```

## API Contract

### `POST /agent/run`

Runs the inherited memory agent and optionally creates a LangSmith trace.

Request:

```json
{
  "thread_id": "trace-demo",
  "user_id": "reader-42",
  "prompt": "Recommend one short book about observability.",
  "temperature": 0.4,
  "max_tokens": 1024,
  "history": []
}
```

Key SSE additions:

| Field | Location | Meaning |
| ----- | -------- | ------- |
| `langsmithRunId` | `status.phase=memory_loaded` | LangSmith run id, or `null` when tracing is disabled. |
| `userId` | `status.phase=memory_loaded` | User namespace used for memory recall and trace metadata. |
| `longTermMemories` | `status.phase=memory_loaded` | Count of recalled memories. |

### `POST /feedback`

Attaches user or reviewer feedback to a LangSmith run.

Request:

```json
{
  "run_id": "6f1328d2-...",
  "key": "user_rating",
  "score": 1,
  "comment": "Useful answer."
}
```

Response:

```json
{
  "runId": "6f1328d2-...",
  "accepted": true
}
```

If LangSmith is disabled, the endpoint returns `accepted: false` instead of failing local development.

### Inherited Endpoints

| Method | Path | Purpose |
| ------ | ---- | ------- |
| `GET` | `/memory/{user_id}` | List inherited long-term memories. |
| `GET` | `/memory/{user_id}/summary` | Summarize what the agent knows about a user. |
| `DELETE` | `/memory/{user_id}` | Delete inherited long-term memories. |
| `DELETE` | `/threads/{thread_id}` | Delete inherited short-term thread memory. |
| `GET` | `/metrics` | Prometheus scrape endpoint. |
| `GET` | `/healthz` | Liveness probe. |
| `GET` | `/readyz` | Readiness probe. |

## Configuration

| Env var | Default | Purpose |
| ------- | ------- | ------- |
| `LANGSMITH_TRACING` | `true` | Enables LangSmith API calls. |
| `LANGSMITH_API_KEY` | unset | LangSmith API key. |
| `LANGSMITH_PROJECT` | `Agent Blueprint Recipes` | LangSmith project name. |
| `LANGSMITH_ENDPOINT` | `https://eu.api.smith.langchain.com` | LangSmith API URL. |
| `MEMORY_BACKEND` | `postgres` | Inherited memory backend. |
| `POSTGRESQL_ADDON_URI` | local Postgres URL | Inherited memory database. Clever Cloud injects this when a Postgres add-on is linked. |
| `NEBIUS_API_KEY` | required | Nebius API key. |

Cookbooks #6-#10 can share one Postgres database by using different schemas.
The schema is derived from `ENV` and the cookbook number: `dev_cbk_07` locally, `prod_cbk_07` when `ENV=production`.
The app creates `prod_cbk_07.user_memories` on first use, separate from cookbook #6's `prod_cbk_06.user_memories`.

## Implementation Notes

`app/core/langsmith_observability.py` is a narrow adapter around `langsmith.Client` and the LangSmith trace context manager.
It creates a root `agent.run` trace before memory recall and generation, closes it after the final answer, and stores feedback through `/feedback`.

The adapter redacts emails and phone numbers before sending prompt and output previews.
It records `cookbook`, `env`, `thread_id`, and `user_id` as metadata.
Those identifiers are useful for debugging, but they still count as user-related data in many systems, so treat LangSmith as a production telemetry destination.

The annotation pattern is intentionally small:

```python
from langsmith import traceable

from app.core.langsmith_annotations import (
    process_langsmith_inputs,
    process_langsmith_outputs,
)


@traceable(
    name="agent.route_request",
    run_type="chain",
    process_inputs=process_langsmith_inputs,
    process_outputs=process_langsmith_outputs,
)
def route_request(state: AgentState) -> dict[str, str]:
    ...
```

For streaming functions, the cookbook uses a reducer so the trace captures a compact summary instead of every emitted chunk:

```python
@traceable(
    name="nebius.chat_stream",
    run_type="llm",
    metadata={"provider": "nebius"},
    process_inputs=process_langsmith_inputs,
    reduce_fn=summarize_chat_chunks,
)
async def stream_chat(...) -> AsyncIterator[ChatStreamChunk]:
    ...
```

The route opens the request-level trace and lets annotated child spans attach to it:

```python
with observer.trace_agent_run(
    prompt=payload.prompt,
    thread_id=payload.thread_id,
    user_id=payload.user_id,
    model=settings.nebius_model,
    env=settings.env,
) as trace_run:
    ...
    trace_run.finish(output=assistant_answer)
```

Tracing failures do not break the agent response.
If LangSmith is unavailable, the service logs a warning and continues.
That is intentional because observability should not become an availability dependency for the agent path.

## Using Traces in Production

Use traces when you need to answer request-level questions:

- Which memory records were recalled before the answer?
- Did the graph choose the direct path or the deliberate path?
- What prompt was assembled after context injection?
- How long did the Nebius stream take to produce the first token?
- Which model, environment, route, user namespace, and thread produced the run?
- Which feedback score or review comment belongs to the exact run?

Use LangSmith projects as operational boundaries.
Development, staging, and production should be separate projects, or at least consistently separated with tags and metadata.
This cookbook defaults to the EU LangSmith endpoint and an `Agent Blueprint Recipes` project for the public demo, but a production rollout should choose project names that match the deployment environment.

Keep Prometheus and LangSmith side by side.
Prometheus should page you when aggregate latency, traffic, or error rates move.
LangSmith should help you inspect the specific runs behind those metrics, compare traces, attach feedback, and turn failed runs into future evaluation examples.

For sensitive deployments, decide the trace policy before launch.
Common controls are redaction, hashed user identifiers, reduced output previews, environment-specific projects, trace sampling, and disabling tracing for regulated workflows.
Never place raw secrets, access tokens, or full customer records in trace metadata.

## Production Checklist

- Use separate LangSmith projects for development, staging, and production.
- Redact or hash identifiers if your privacy policy requires it.
- Decide which prompt and output previews are allowed in traces.
- Attach deployment version, model id, and cookbook name to every trace.
- Use annotation reducers for streaming responses and large retrieved payloads.
- Keep Prometheus metrics for service-level latency and error rates.
- Use LangSmith for run-level debugging, feedback review, and qualitative failure analysis.

## Failure Modes

| Symptom | Likely cause | Handling |
| ------- | ------------ | -------- |
| `langsmithRunId` is `null` | Tracing disabled or missing key | Set `LANGSMITH_TRACING=true` and configure `LANGSMITH_API_KEY`. |
| Feedback returns `accepted:false` | LangSmith disabled | Enable tracing before using feedback in production. |
| Traces contain sensitive data | Overly broad previews or metadata | Redact previews and avoid raw PII in metadata. |
| Agent works but trace is missing | LangSmith API error | Check logs for `langsmith_*_failed` warnings. |
| Prometheus looks healthy but answer is bad | Aggregate metrics hide behavior | Inspect the LangSmith trace and attach feedback. |

## Test It

```bash
uv run pytest
uv run ruff check
uv run ruff format --check
```

Tests keep `LANGSMITH_TRACING=false`.
They verify the disabled path and feedback endpoint without calling LangSmith.

## Going Further

- Add trace links to the web playground when `langsmithRunId` is present.
- Add evaluator feedback keys for correctness, helpfulness, and groundedness.
- Export failed-run examples into datasets for future evaluation.
- Continue to Cookbook #8 to enforce guardrails on the same observable agent.

## Reference

- LangSmith docs — [docs.langchain.com/langsmith/home](https://docs.langchain.com/langsmith/home)
- LangSmith custom instrumentation — [docs.langchain.com/langsmith/annotate-code](https://docs.langchain.com/langsmith/annotate-code)
- LangChain observability — [docs.langchain.com/oss/python/langchain/observability](https://docs.langchain.com/oss/python/langchain/observability)

## License

MIT
