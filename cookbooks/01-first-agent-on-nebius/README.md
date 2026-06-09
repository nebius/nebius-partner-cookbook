# Your First Agent on Nebius

> A production-grade FastAPI agent with streaming, observability, and zero magic.

Recipe **01 of 10** in the Agent Blueprint Recipes arc:

> **Foundation** → Knowledge → Grounding → Orchestration → Thread Memory → User Memory → Observability → Guardrails → Actions → Simulation

You called OpenAI from a Python script and it worked. Now what?

This recipe is the bridge between that script and something you would actually deploy. It is a small FastAPI service that streams a Nebius chat completion as Server-Sent Events. The Nebius integration is one line. Everything else — the structured logs, the Prometheus metrics, the rate limit, the security headers, the Dockerfile, the tests — is the shape of a service you can hand to ops without blushing.

It is deliberately *not* an agent framework. There is no planner, no tool loop, no graph. The point is to get the boundaries right — config, transport, observability, lifecycle — so that the recipes that follow can add capability without re-litigating infrastructure.

## What you'll build

A single-endpoint API:

| Endpoint | Description |
|---|---|
| `POST /agent/run` | Streams `status`, `token`, `done` SSE events |
| `GET /healthz` | Liveness probe |
| `GET /readyz` | Readiness probe |
| `GET /metrics` | Prometheus scrape endpoint |
| `GET /docs` | OpenAPI / Swagger UI |

Everything is typed, every env var validated, every request tagged with a request ID, every Nebius call wrapped in tenacity-backed retries.
This foundation recipe intentionally has no database dependency.
It is also the deployment baseline that later recipes extend.

## Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) — `curl -LsSf https://astral.sh/uv/install.sh | sh`
- A Nebius API key — get one from the [Nebius console](https://nebius.com)
- (optional) Docker, if you want to build the production image

No partner service account is needed until the knowledge and memory recipes.

## Run it

```bash
git clone https://github.com/nebius/nebius-partner-cookbook.git
cd nebius-cookbook/cookbooks/01-first-agent-on-nebius

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

You'll see SSE events arriving:

```
event: status
data: {"phase":"thinking"}

event: token
data: {"text":"Nebius"}

event: token
data: {"text":" Token"}

…

event: status
data: {"phase":"done"}

event: done
data: {}
```

### Multi-turn requests

The server is **stateless** — it keeps no session. To hold a conversation, the client replays prior turns in the request body:

```bash
curl -N -X POST http://localhost:8000/agent/run \
  -H 'content-type: application/json' \
  -d '{
        "prompt": "And who maintains it?",
        "history": [
          {"role": "user", "content": "What is Nebius AgentKit?"},
          {"role": "assistant", "content": "It is ..."}
        ]
      }'
```

`history` is optional and capped (40 turns, 8 KB per message) by the request schema. Statelessness is a deliberate architectural choice — see *Design decisions* below.
Cookbook #5 adds thread memory after this baseline is clear.

## Walk-through

### The directory

```
app/
├── main.py              # FastAPI app, lifespan, middleware
├── config.py            # Pydantic Settings, validated at boot
├── routes/
│   ├── agent.py         # POST /agent/run with SSE
│   └── health.py        # /healthz, /readyz
├── schemas/
│   └── agent.py         # Pydantic I/O models
├── core/
│   ├── nebius_client.py # OpenAI SDK pointed at Nebius
│   └── agent.py         # The agent logic
└── observability/
    ├── logging.py       # structlog (JSON in prod)
    ├── metrics.py       # Prometheus counters/histograms
    └── middleware.py    # Request IDs, security headers, body-size limit
```

The split is by *boundary*, not by layer: `core/` is the only place that knows about Nebius, `routes/` is the only place that knows about HTTP and SSE, `observability/` is cross-cutting. You can unit-test `core/agent.py` without standing up a server, and you can change the transport (SSE → WebSocket) without touching `core/`.

### The Nebius integration

The SDK swap is one line — `base_url` points at Nebius:

```python
AsyncOpenAI(
    api_key=settings.nebius_api_key,
    base_url=str(settings.nebius_base_url),  # https://api.studio.nebius.ai/v1/
    timeout=httpx.Timeout(connect=5.0, read=60.0, write=10.0, pool=5.0),
    max_retries=0,  # retries are owned by tenacity, not the SDK
)
```

Nebius AgentKit is OpenAI-wire-compatible, so the OpenAI SDK works unchanged — the same `chat.completions.create(...)` call, the same streaming protocol. That compatibility is the reason every recipe in this cookbook can stay on one client library.
Later cookbooks keep this client boundary and add capabilities around it.

Two decisions worth calling out:

- **Timeouts are split, not global.** A 5 s connect timeout fails fast on a dead endpoint; a 60 s read timeout tolerates a slow generation. A single global timeout forces you to choose one or the other.
- **`max_retries=0` on the SDK.** Retry policy lives in `tenacity` (see below) so it is visible, testable, and swappable in one place. Two retry layers stacked silently is a production incident waiting to happen.

`build_nebius_client()` returns a **process-wide singleton**. The point is the underlying `httpx` connection pool: reusing it avoids a TLS handshake on every request. A fresh client per request is a common and expensive mistake.

### Retries

```python
@retry(
    retry=retry_if_exception_type((httpx.HTTPError, httpx.TimeoutException)),
    wait=wait_exponential(multiplier=0.5, min=0.5, max=8.0),
    stop=stop_after_attempt(3),
    reraise=True,
)
```

Retries fire on **transport** errors only. A 4xx (bad key, malformed request) or a content error is not retried — replaying it just burns quota and latency for the same failure. Exponential backoff with a cap keeps a struggling upstream from being hammered.

### The observability

Every request gets a UUID request ID, returned in the `x-request-id` header and bound to the structlog context so every log line for that request carries it. In production (`ENV=production`) logs render as JSON; in dev they render as human-readable lines. One renderer swap, same call sites.

A sample log line in production:

```json
{
  "event": "agent_started",
  "level": "info",
  "request_id": "9a8f3c…",
  "path": "/agent/run",
  "model": "meta-llama/Llama-3.3-70B-Instruct",
  "timestamp": "2026-06-04T12:31:42.103Z"
}
```

Prometheus metrics include:

- `http_requests_total{method,path,status}` — request counter
- `http_request_duration_seconds{method,path}` — latency histogram
- `nebius_tokens_total{model,type}` — tokens streamed back from Nebius
- `nebius_request_duration_seconds{model}` — Nebius call duration

The `path` label is the **route template** (`/agent/run`), not the raw URL — a deliberate choice, since high-cardinality labels (per-user, per-ID paths) are the fastest way to melt a Prometheus instance.
Later recipes keep these same metrics while adding memory, guardrails, and actions.

### The streaming

The route handler returns a `StreamingResponse` with `text/event-stream`. Events are *named* — `status`, `token`, `done`, `heartbeat`, `error` — rather than raw text, so a client can `switch` on the event name instead of parsing prose. The agent itself is an `async` generator yielding typed `Event`s; the route's only job is to serialise each one into the SSE wire format.

Two production details that are easy to miss:

- **Heartbeats.** A `heartbeat` event is emitted every 15 s of silence. Idle SSE streams are killed by load balancers and proxies; the heartbeat keeps the connection scored as live. The response also sets `x-accel-buffering: no` so nginx forwards chunks immediately instead of buffering the whole body.
- **Disconnect cancellation.** A background task polls `request.is_disconnected()` and sets a `cancel_event`. The agent checks it between tokens and stops pulling from Nebius the moment the client goes away — otherwise a user closing a tab still costs you a full generation.

### The hardening

- The daily per-IP rate limiter protects backend routes before they call Nebius; it uses Redis when `RATE_LIMIT_REDIS_URL` is set and process-local memory otherwise (`RATE_LIMIT_REQUESTS_PER_DAY`, default 25).
- CORS is allowlist-based — `CORS_ORIGINS` is parsed and validated at boot, never `*`.
- Security headers: `x-content-type-options`, `referrer-policy`, `strict-transport-security`.
- Request bodies above 64 KB are rejected with 413 *before* the body is read, via a `content-length` check in middleware.
- Lifespan handlers log startup and shutdown; on shutdown the HTTP client is closed and in-flight requests are allowed to drain.

**Middleware order is load-bearing.** ASGI wraps middleware last-added-runs-first, so the stack is arranged so CORS, size checks, security headers, request IDs, metrics, and rate limiting all happen before route work. Re-ordering `add_middleware` calls silently changes behaviour — there is a comment in `main.py` spelling out the request path.

#### Rate limiting

The limiter is enabled by default and allows 25 backend requests per IP per rolling 24-hour window.
Set these values in `.env`:

```dotenv
RATE_LIMIT_ENABLED=true
RATE_LIMIT_REQUESTS_PER_DAY=25
RATE_LIMIT_REDIS_URL=
RATE_LIMIT_TRUST_PROXY_HEADERS=false
```

Leave `RATE_LIMIT_REDIS_URL` empty for local in-memory counters, or point it at Redis for a shared counter across replicas:

```dotenv
RATE_LIMIT_REDIS_URL=redis://localhost:6379/0
```

When the quota is exceeded, the backend returns JSON `429` before opening an SSE stream:

```json
{
  "detail": "daily rate limit exceeded",
  "limit": 25,
  "window": "24h",
  "retryAfterSeconds": 12345
}
```

See the full deployment notes in [`docs/rate-limiting.md`](../../docs/rate-limiting.md).

## Design decisions

**Why a stateless server?** No session store means any instance can serve any request — horizontal scaling is just "add a replica," and a crash loses nothing. The cost is bandwidth: the client resends history each turn. For a chat workload that is a few KB; when it stops being cheap (long transcripts, RAG context), the answer is a server-side store keyed by session ID, not in-process state. Recipe #5 (Short-Term Memory) takes that step deliberately.

**Why no agent framework?** A framework would hide exactly the boundaries this recipe exists to show. `core/agent.py` is ~50 lines and is explicitly designed to be subclassed — the later recipes add planning, knowledge, and tools on top of this same shape.

**Why duplicate infrastructure per cookbook?** Every recipe is autonomous: cloning one directory is enough to run it, with no shared base package. That costs some duplication and buys a reader the ability to study one cookbook in isolation. It is a documentation decision, not an architectural recommendation — in a real monorepo, factor the common middleware into a shared library.

## Failure modes

| Symptom | Cause | Handling |
|---|---|---|
| 500 on first request | `NEBIUS_API_KEY` unset or invalid | Settings validate at boot; a bad key surfaces on first Nebius call as a non-retried 4xx |
| Stream stalls, no tokens | Upstream slow generation | 60 s read timeout, then a retried `httpx.TimeoutException`; client sees an `error` event |
| Stream ends early | Client disconnected | Expected — disconnect watcher cancels the upstream call |
| 429 responses | Daily per-IP rate limit hit | Back off; raise `RATE_LIMIT_REQUESTS_PER_DAY` only behind authentication |
| 413 responses | Body over 64 KB | Raise `MAX_REQUEST_BYTES`, or trim client-side `history` |

The `except Exception` in the route logs the full stack trace but emits only `{"detail": "internal error"}` to the client — internal details never cross the wire.

## Test it

```bash
make test
```

Tests use [respx](https://lundberg.github.io/respx/) to mock every Nebius call. No network is hit. CI passes on a laptop in airplane mode — which also means the test suite is a faithful, runnable spec of the SSE contract.

## Ship it

Build the production image:

```bash
make docker
```

The Dockerfile is multi-stage, uses [`astral-sh/uv`](https://github.com/astral-sh/uv) for the build, and ends in a slim Python 3.12 image running as a non-root user with a healthcheck wired to `/healthz`.

Deployment-specific instructions for Nebius Compute live in [`docs/deployment.md`](../../docs/deployment.md).

## Going further

- **Cookbook #2 — [Domain Knowledge with Pinecone Nexus](../02-domain-knowledge-pinecone-nexus/)** — give the agent a grounded, compiled knowledge base instead of a frozen training cutoff.
- **Tracing.** Feed an inbound `traceparent` into the request-ID middleware and emit OpenTelemetry spans around the Nebius call — the structlog context is already the right place to bind a trace ID.
- **Authentication.** Drop a JWT verifier in as a FastAPI `Depends`; it composes cleanly with the existing rate limiter and request-ID middleware.
- **Backpressure.** Under heavy fan-out, cap concurrent Nebius calls with an `asyncio.Semaphore` in the client so one traffic spike can't open unbounded upstream connections.

## License

MIT — see [`LICENSE`](../../LICENSE).
