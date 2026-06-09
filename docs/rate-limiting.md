# Backend rate limiting

Each cookbook backend has a daily per-IP rate limiter.
It protects the FastAPI app before route handlers run, so a blocked request does not call Nebius, Pinecone, Tavily, Stripe, or open a Server-Sent Events stream.

## Configuration

Every backend reads the same settings from `.env` or the deployment environment:

```dotenv
RATE_LIMIT_ENABLED=true
RATE_LIMIT_REQUESTS_PER_DAY=25
RATE_LIMIT_REDIS_URL=
RATE_LIMIT_TRUST_PROXY_HEADERS=false
```

`RATE_LIMIT_ENABLED` turns the limiter on or off.
`RATE_LIMIT_REQUESTS_PER_DAY` is the per-IP quota for a rolling 24-hour window.
`RATE_LIMIT_REDIS_URL` switches the store from in-memory counters to Redis.
`RATE_LIMIT_TRUST_PROXY_HEADERS` makes the limiter read `X-Forwarded-For` or `Forwarded` headers instead of `request.client.host`.

Use `RATE_LIMIT_TRUST_PROXY_HEADERS=true` only when the backend is behind a trusted ingress, load balancer, or platform proxy that overwrites client-supplied forwarding headers.
On a directly exposed local app, keep it `false`.

## Local Redis

Start Redis locally:

```bash
docker run --rm -p 6379:6379 redis:8-alpine
```

Then configure a cookbook `.env`:

```dotenv
RATE_LIMIT_ENABLED=true
RATE_LIMIT_REQUESTS_PER_DAY=25
RATE_LIMIT_REDIS_URL=redis://localhost:6379/0
RATE_LIMIT_TRUST_PROXY_HEADERS=false
```

If `RATE_LIMIT_REDIS_URL` is empty, the backend uses a process-local in-memory store.
That is fine for tests and single-process demos, but counters reset on restart and are not shared across replicas.

## Production deployment

For Clever Cloud, keep non-secret limiter settings as GitHub repository variables:

```bash
gh variable set RATE_LIMIT_ENABLED --body true
gh variable set RATE_LIMIT_REQUESTS_PER_DAY --body 25
gh variable set RATE_LIMIT_TRUST_PROXY_HEADERS --body true
```

Do not store `RATE_LIMIT_REDIS_URL` as a GitHub repository variable when using a linked Redis add-on.
Let the platform inject the Redis connection string or set it directly in the target backend environment.

The deploy workflow syncs the three non-secret variables listed above into each configured cookbook backend.

## Response contract

When the limit is exceeded, the backend returns plain JSON with HTTP `429`.
Streaming endpoints are rejected before an SSE stream starts.

```http
HTTP/1.1 429 Too Many Requests
Retry-After: 12345
X-RateLimit-Limit: 25
X-RateLimit-Remaining: 0
X-RateLimit-Reset: 1780420000
Content-Type: application/json
```

```json
{
  "detail": "daily rate limit exceeded",
  "limit": 25,
  "window": "24h",
  "retryAfterSeconds": 12345
}
```

Allowed requests include:

```http
X-RateLimit-Limit: 25
X-RateLimit-Remaining: 24
X-RateLimit-Reset: 1780420000
```

Operational endpoints are exempt:

```text
/healthz
/readyz
/metrics
/docs
/openapi.json
```

## Implementation shape

Each cookbook is autonomous, so the same middleware lives in every cookbook under `app/core/rate_limit.py`.
The app selects Redis only when `RATE_LIMIT_REDIS_URL` is configured:

```python
app.state.rate_limit_store = build_rate_limit_store(
    settings.rate_limit_redis_url,
    namespace=app.state.cookbook_slug,
)
```

The middleware is registered before route work:

```python
app.add_middleware(
    RateLimitMiddleware,
    enabled=settings.rate_limit_enabled,
    requests_per_day=settings.rate_limit_requests_per_day,
    store=app.state.rate_limit_store,
    trust_proxy_headers=settings.rate_limit_trust_proxy_headers,
)
```

Redis counting is atomic.
The first request creates the key and sets a 24-hour TTL; later requests increment the same key until the window expires.
