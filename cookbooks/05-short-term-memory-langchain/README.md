# Thread Memory — Short-Term Memory with LangChain

> Let the agent continue one conversation without forcing the client to replay every previous turn.

Recipe **05 of 10** in the Agent Blueprint Recipes arc:

> Foundation → Knowledge → Grounding → Orchestration → **Thread Memory** → User Memory → Observability → Guardrails → Actions → Simulation

Cookbook #4 made orchestration explicit with LangGraph.
This recipe keeps that orchestration and adds the next production capability: short-term memory inside one conversation thread.

The boundary matters.
Short-term memory is not a user profile and it is not durable personalization.
It is the recent thread state that lets a user ask "what about the second one?" and get an answer that knows what "the second one" refers to.

Durable memory starts in Cookbook #6.
This cookbook intentionally uses process-local memory so the first memory concept is easy to inspect, test, and reset.

## What you'll build

A production-shape FastAPI service that extends the orchestrated book agent:

1. **Inherited orchestration** — the `direct` / `deliberate` LangGraph route from Cookbook #4 still chooses the response path.
2. **Thread identity** — every agent call includes a stable `thread_id`.
3. **Short-term state** — the service remembers recent user and assistant turns for that thread.
4. **Bounded context** — only the most recent messages are injected into the next Nebius call.
5. **Reset** — `DELETE /threads/{thread_id}` clears local thread state.
6. **Network-free tests** — tests mock Nebius with `respx`.

```text
POST /agent/run ──► thread_id ──► load recent turns ──► LangGraph route ──► Nebius stream ──► SSE
                         ▲                                                        │
                         └──────────────── save user + assistant turn ◄───────────┘

DELETE /threads/{thread_id} ──► clear local thread state
```

## Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/)
- A Nebius API key from the [Nebius console](https://nebius.com)
- Docker (optional)

## Run it

```bash
cp .env.example .env
# Open .env and fill NEBIUS_API_KEY.

uv sync
make dev
```

Start a thread:

```bash
curl -N -X POST http://localhost:8000/agent/run \
  -H 'content-type: application/json' \
  -d '{"thread_id":"demo-thread","prompt":"Recommend three books about product strategy."}'
```

Follow up with the same `thread_id`:

```bash
curl -N -X POST http://localhost:8000/agent/run \
  -H 'content-type: application/json' \
  -d '{"thread_id":"demo-thread","prompt":"Which of those is best for a founder?"}'
```

The second request receives the first turn as thread context.
The SSE stream includes memory status:

```text
event: status
data: {"phase":"memory_loaded","threadId":"demo-thread","messages":2}

event: status
data: {"phase":"routed","route":"deliberate","contextNeed":"curated_recommendation"}

event: token
data: {"text":"..."}

event: status
data: {"phase":"memory_saved","threadId":"demo-thread","messages":4}
```

Reset the thread:

```bash
curl -X DELETE http://localhost:8000/threads/demo-thread
```

## API Contract

### `POST /agent/run`

Runs the agent and streams named SSE events.

Request:

```json
{
  "thread_id": "demo-thread",
  "prompt": "Which of those is best for a founder?",
  "temperature": 0.4,
  "max_tokens": 1024,
  "history": []
}
```

Fields:

| Field | Required | Purpose |
| ----- | -------- | ------- |
| `thread_id` | yes | Stable conversation key for server-side short-term memory. |
| `prompt` | yes | Current user request. |
| `temperature` | no | Passed to the Nebius chat call. |
| `max_tokens` | no | Clamped by the inherited LangGraph route budget. |
| `history` | no | Optional one-off context from the client. Server memory is loaded separately. |

SSE events:

| Event | Meaning |
| ----- | ------- |
| `status` | Phase transitions such as `memory_loaded`, `routed`, `writing`, `first_token`, and `memory_saved`. |
| `token` | Nebius token deltas plus the final usage footer. |
| `done` | Stream completion. |
| `error` | Recoverable API-level failure. |
| `heartbeat` | Long-running connection heartbeat. |

### `DELETE /threads/{thread_id}`

Clears process-local memory for a thread.

Response:

```json
{
  "threadId": "demo-thread",
  "deleted": true
}
```

## How It Works

The request model makes `thread_id` required.
That is the only API shape change from Cookbook #4.

```python
class AgentRunRequest(BaseModel):
    """Payload for POST /agent/run."""

    thread_id: str = Field(..., min_length=1, max_length=120, pattern="^[A-Za-z0-9_.:-]+$")
    prompt: str = Field(..., min_length=1, max_length=8_000)
    temperature: float = Field(default=0.4, ge=0.0, le=2.0)
    max_tokens: int = Field(default=1024, ge=1, le=8192)
    history: list[ChatHistoryMessage] = Field(default_factory=list, max_length=12)
```

The memory store is deliberately small.
It keeps recent messages per thread, trims old messages, and returns copies so route handlers cannot mutate internal state accidentally.

```python
@dataclass
class ThreadMemoryStore:
    max_messages_per_thread: int = 12
    _threads: dict[str, list[dict[str, str]]] = field(default_factory=dict)
    _lock: asyncio.Lock = field(default_factory=asyncio.Lock)

    async def get_history(self, thread_id: str) -> list[dict[str, str]]:
        async with self._lock:
            return list(self._threads.get(thread_id, []))

    async def append_turn(self, thread_id: str, *, user: str, assistant: str) -> int:
        async with self._lock:
            messages = self._threads.setdefault(thread_id, [])
            messages.extend(
                [
                    {"role": "user", "content": user},
                    {"role": "assistant", "content": assistant},
                ]
            )
            del messages[: max(0, len(messages) - self.max_messages_per_thread)]
            return len(messages)
```

The route composes stored thread memory with any client-provided history before invoking the inherited LangGraph agent.

```python
stored_history = await memory.get_history(payload.thread_id)
history = [*stored_history, *(item.model_dump() for item in payload.history)]

async for event in agent.run(
    payload.prompt,
    options=AgentRunOptions(
        temperature=payload.temperature,
        max_tokens=payload.max_tokens,
        history=history,
    ),
    cancel_event=cancel_event,
):
    yield _sse(event.name, event.data)
```

After the stream completes, the route saves the new turn.
It stores only the assistant answer text, not the operational metrics footer.

```python
retained = await memory.append_turn(
    payload.thread_id,
    user=payload.prompt,
    assistant="".join(assistant_chunks).strip(),
)

yield _sse(
    "status",
    {
        "phase": "memory_saved",
        "threadId": payload.thread_id,
        "messages": retained,
    },
)
```

The inherited prompt builder from Cookbook #4 already knows how to use recent history.
If history exists, it wraps the current prompt with conversation context:

```python
if history:
    recent = history[-6:]
    context = "\n".join(
        f"{item['role']}: {item['content'][:800]}"
        for item in recent
        if item.get("content")
    )
    prompt = (
        "Recent conversation context:\n"
        f"{context}\n\nCurrent user request:\n{prompt}\n\n"
        "Resolve references like 'that topic' from the recent conversation."
    )
```

That is the production move: memory stays outside the FastAPI transport layer, but the route remains explicit about when memory is loaded and saved.

## Configuration

| Env var | Default | Purpose |
| ------- | ------- | ------- |
| `NEBIUS_API_KEY` | required | Nebius API key. |
| `NEBIUS_BASE_URL` | `https://api.studio.nebius.ai/v1/` | OpenAI-compatible Nebius endpoint. |
| `NEBIUS_MODEL` | `meta-llama/Llama-3.3-70B-Instruct` | Chat model. |
| `DIRECT_RESPONSE_MAX_TOKENS` | `384` | Fast-path output cap inherited from Cookbook #4. |
| `DELIBERATE_RESPONSE_MAX_TOKENS` | `700` | Deliberate-path output cap inherited from Cookbook #4. |
| `FIRST_TOKEN_TARGET_MS` | `1200` | Target exposed in routing status events. |
| `CORS_ORIGINS` | `http://localhost:3000` | Browser allowlist. |
| `LOG_LEVEL` | `info` | Structured logging level. |

## Design Decisions

**Thread memory is scoped by `thread_id`.** The server does not try to infer continuity from IP address, cookies, or prompt content.
The client or application layer owns the conversation id.

**Memory is process-local in this recipe.** That keeps the first memory cookbook runnable in minutes and makes the concept easy to inspect.
It also means memory disappears on restart and is not shared across replicas.
Cookbook #6 introduces durable user memory with Postgres.

**Recall is bounded.** The store keeps a maximum of 12 messages per thread and the prompt builder uses only recent history.
Unbounded transcript replay is a hidden latency and cost bug.

**The route emits memory phases.** `memory_loaded` and `memory_saved` make memory behavior observable in the SSE stream and web playground.

## Production Checklist

- Derive `thread_id` from an authenticated session or server-created conversation id.
- Do not let users read or delete arbitrary thread ids without authorization.
- Move thread state to a shared store before running multiple replicas.
- Add summarization once long threads exceed the prompt budget.
- Keep memory writes after successful model completion so failed runs do not pollute context.
- Redact sensitive content before storing thread messages if your product accepts PII.

## Failure Modes

| Symptom | Likely cause | Handling |
| ------- | ------------ | -------- |
| Follow-up loses context | Client changed `thread_id` | Keep one stable id per conversation. |
| Different users see shared context | Thread ids are guessable or reused | Generate ids server-side and authorize access. |
| Memory disappears after deploy | Process-local store restarted | Move persistence to a database-backed checkpoint or store. |
| Latency grows over time | Too much transcript replay | Trim, summarize, or cap recent messages. |
| Bad answer becomes future context | Failed run was stored | Store only after successful completion and consider moderation before save. |

## Test It

```bash
uv run pytest
uv run ruff check
uv run ruff format --check
```

The tests mock the Nebius streaming endpoint with `respx`.
They verify that a second request with the same `thread_id` receives stored context and that `DELETE /threads/{thread_id}` clears it.

## Going Further

- Add summarization once thread state grows beyond the context budget.
- Store checkpoints in Postgres for durable thread continuity.
- Derive `thread_id` from an authenticated session rather than trusting arbitrary client input.
- Add UI affordances for starting and clearing conversations.
- Continue to Cookbook #6 for durable user memory across threads.

## Reference

- LangChain short-term memory — [docs.langchain.com/oss/python/langchain/short-term-memory](https://docs.langchain.com/oss/python/langchain/short-term-memory)

## License

MIT
