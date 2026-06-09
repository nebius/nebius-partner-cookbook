# Actions — Making Actions with MCP and Stripe

> Let a guarded book agent create a Stripe test-mode checkout link, but only after explicit user approval.

Recipe **09 of 10** in the Agent Blueprint Recipes arc:

> Foundation → Knowledge → Grounding → Orchestration → Thread Memory → User Memory → Observability → Guardrails → **Actions** → Simulation

Cookbook #8 taught the agent to refuse unsafe or off-topic requests.
This recipe keeps that full stack and adds one new production capability: the agent can propose an external action.
The model never gets uncontrolled authority.
It can request a checkout action, but the FastAPI service owns approval, policy, audit events, and the Stripe MCP call.

## What you'll build

A FastAPI service that extends the guarded memory agent:

1. **Inherited agent stack** — LangGraph routing, thread memory, Postgres user memory, LangSmith tracing, guardrails, SSE, and metrics stay in place.
2. **Seeded book catalog** — three fictional books live in `scripts/data/books.json`, with illustration paths ready for your assets.
3. **Stripe setup script** — `make seed-stripe-books` creates Stripe test-mode Products and Prices through Stripe REST and writes `data/stripe_books.json`.
4. **Remote Stripe MCP runtime** — approved actions call `https://mcp.stripe.com` with the `create_payment_link` tool.
5. **Human approval** — `/agent/run` emits `approval_required`; `/approvals/{approval_id}` approves or rejects the side effect.

```text
book purchase prompt
  └─► input guardrails
      └─► select seeded book
          └─► create pending approval
              ├─► reject: no Stripe call
              └─► approve: Stripe MCP create_payment_link
```

## Quickstart

```bash
cd cookbooks/09-actions-with-mcp-stripe
uv sync
cp .env.example .env
```

Fill these values in `.env`:

```bash
NEBIUS_API_KEY=...
STRIPE_SECRET_KEY=sk_test_or_sandbox_seed_key
STRIPE_MCP_API_KEY=rk_test_or_sandbox_restricted_key
```

Start Postgres for inherited long-term memory:

```bash
docker compose up -d postgres
```

Create the Stripe test catalog:

```bash
make seed-stripe-books
```

Run the app:

```bash
make dev
```

In the web playground, open recipe 09 and ask:

```text
I want to buy The Nebius Cloud Atlas.
```

The assistant will emit an approval card.
Approving it calls Stripe MCP and returns a test checkout URL.

## Environment

| Variable | Default | Purpose |
| --- | --- | --- |
| `NEBIUS_API_KEY` | required | Nebius AgentKit API key. |
| `STRIPE_SECRET_KEY` | `sk_test_replace_me` | Setup-only key used by `make seed-stripe-books`. |
| `STRIPE_MCP_API_KEY` | `rk_test_replace_me` | Runtime key used to call remote Stripe MCP. |
| `STRIPE_MCP_BASE_URL` | `https://mcp.stripe.com` | Remote Stripe MCP endpoint. |
| `BOOK_CATALOG_PATH` | `data/stripe_books.json` | Generated catalog with Stripe Product and Price IDs. |
| `APPROVAL_TTL_SECONDS` | `900` | Time window for approving a pending action. |
| `MEMORY_BACKEND` | `postgres` | Inherited long-term memory backend. |
| `POSTGRESQL_ADDON_URI` | local Postgres URL | Inherited memory database. Clever Cloud injects this when a Postgres add-on is linked. |
| `LANGSMITH_TRACING` | `false` | Enables LangSmith SaaS traces when credentials are configured. |

Cookbooks #6-#10 can share one Postgres database by using different schemas.
The schema is derived from `ENV` and the cookbook number: `dev_cbk_09` locally, `prod_cbk_09` when `ENV=production`.
The app creates `prod_cbk_09.user_memories` on first use, separate from the memory tables used by the previous cookbooks.

## Stripe MCP and Sandboxes

Stripe MCP exposes Stripe API operations as MCP tools, including `create_payment_link`.
This cookbook uses the remote MCP endpoint instead of a local `npx @stripe/mcp` subprocess so the Python service stays simple to run and easy to mock in tests.

**Use a Stripe Sandbox or test-mode account.**
**Never use live keys for this cookbook.**

Stripe Sandboxes are newer than the classic global test-mode toggle.
Think of a Sandbox as an isolated Stripe environment with its own API keys, objects, settings, and test data.
That is useful for agent work because you can give the agent a realistic account shape without letting it touch your real Stripe account or pollute a shared test-mode setup.

Classic test mode is still enough for local experimentation.
A Sandbox is the stronger choice when you want repeatable demos, CI smoke tests, or multiple isolated agent environments.
For this cookbook, the recommended setup is:

- one Sandbox dedicated to the cookbook demo;
- one setup key for creating the fake Products and Prices;
- one restricted runtime key for the remote MCP server;
- no live-mode objects, prices, customers, or checkout links.

This separation mirrors a production control boundary.
Operators prepare the commerce catalog.
The agent can only request a narrow runtime action after the user approves it.

Recommended key model:

- Use `STRIPE_SECRET_KEY` only for the operator seed step.
- Use `STRIPE_MCP_API_KEY` for the running app.
- Prefer a restricted key for MCP that can create Payment Links from existing Prices and cannot perform broad account operations.
- Rotate both keys after demos or CI smoke tests.

The seed script deliberately uses Stripe REST instead of MCP.
Seeding is an operator task: create Products and multi-currency Prices once, then let the runtime agent use MCP only for the approved action.
Each book gets one Stripe Price with USD as the default currency and EUR, GBP, and SGD configured through Stripe `currency_options`.

## Why Stripe MCP here?

Stripe is a good final cookbook action because it is concrete, high stakes, and easy to keep safe in test mode.
Creating a checkout link is visibly different from answering a question, but it is still small enough to understand in one recipe.
It also makes the approval pattern obvious: payment-related side effects should never happen just because the model suggested them.

Other MCP servers could participate in the same flow:

- **Catalog or CMS MCP** to fetch approved book metadata before checkout.
- **Inventory MCP** to confirm a book or bundle is available.
- **CRM MCP** to associate the approved action with a demo user or account.
- **Email MCP** to send the checkout link after approval.
- **Ticketing or audit MCP** to record the approval trail for compliance.
- **Knowledge-base MCP** to fetch refund, tax, or shipping policy before the agent explains the checkout.

The important pattern stays the same regardless of the MCP provider:

```text
model proposes action → backend validates policy → user approves → MCP tool executes
```

Do not let tool discovery become tool authority.
MCP gives the agent a standardized way to reach tools, but your application still decides which tools are allowed, what arguments are valid, who can approve them, and what gets logged.

## Seed catalog

The source catalog is committed at:

```text
scripts/data/books.json
```

It contains ten fictional books that will be created in the Stripe Sandbox.
Each book uses a single Stripe Price with USD as the default and EUR, GBP, and SGD as multi-currency options:

| Book | Author | ISBN-13 | USD | EUR | GBP | SGD |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| `The Nebius Cloud Atlas` | Nia Vector | `9781600000010` | $14.99 | €13.99 | £11.99 | S$19.99 |
| `Pinecones in the Vector Garden` | Ada Embedding | `9781600000027` | $12.99 | €11.99 | £10.99 | S$17.99 |
| `Agent at the End of the Prompt` | Lila Chain | `9781600000034` | $10.99 | €9.99 | £8.99 | S$14.99 |
| `The Checkout Graph` | Max Token | `9781600000041` | $15.99 | €14.99 | £12.99 | S$21.99 |
| `Embeddings & Espresso` | Clara Context | `9781600000058` | $13.99 | €12.99 | £10.99 | S$18.99 |
| `The Retrieval Society` | Jonas Index | `9781600000065` | $16.99 | €15.99 | £13.99 | S$22.99 |
| `Guardrails for Dreaming Machines` | Mira Policy | `9781600000072` | $9.99 | €8.99 | £7.99 | S$13.99 |
| `Ten Thousand Tiny Agents` | Theo Router | `9781600000089` | $14.99 | €13.99 | £11.99 | S$19.99 |
| `The Sandbox Bookshop` | Samira Stripe | `9781600000096` | $12.99 | €11.99 | £10.99 | S$17.99 |
| `When the Model Learned to Read` | Lucie Latency | `9781600000102` | $11.99 | €10.99 | £9.99 | S$15.99 |

Each item includes a `cover_image_path` in the same folder as `books.json`.
The same PNG files are duplicated in the catalog web app at:

```text
app/public/assets/09-book-covers/
```

After deployment, they are publicly available under:

```text
https://nebius-partners-cookbooks.cleverapps.io/assets/09-book-covers/<cover-filename>.png
```

Each ISBN is fictional but has a valid ISBN-13 check digit and is added to Stripe Product and Price metadata as `isbn`.
The seed script also uses that ISBN to create deterministic Stripe Product IDs in this format:

```text
nebius_partners_book_<isbn>
```

For example, `The Nebius Cloud Atlas` is created as:

```text
nebius_partners_book_9781600000010
```

The seed script stores the cover filename in Stripe metadata as `cover_image_path`.
Stripe Product images are public URLs, not local file uploads.
If you set `STRIPE_IMAGE_BASE_URL`, the seed script sends `images[0]` for each Stripe Product by joining that public base URL with the cover filename.
If `data/stripe_books.json` already exists, rerunning the seed script with `STRIPE_IMAGE_BASE_URL` set backfills the image URL on each existing Stripe Product without creating new Products or Prices.
If an older generated catalog contains random `prod_...` Product IDs, rerunning the seed script creates or updates the deterministic `nebius_partners_book_<isbn>` Products and writes a fresh catalog.

For the hosted cookbook site, use:

```bash
STRIPE_IMAGE_BASE_URL=https://nebius-partners-cookbooks.cleverapps.io/assets/09-book-covers
```

The generated catalog is:

```text
data/stripe_books.json
```

It is gitignored because Stripe Price IDs are still generated by Stripe and are account-specific.
The Product IDs are deterministic; the Price IDs are the runtime handles passed to Stripe MCP when creating a Payment Link.

Useful commands:

```bash
uv run python scripts/seed_stripe_books.py --dry-run
uv run python scripts/seed_stripe_books.py --force
```

## API

### `POST /agent/run`

Normal book prompts still use the guarded Nebius agent.
Purchase prompts create a pending approval instead of calling Stripe.

```bash
curl -N -X POST http://localhost:8000/agent/run \
  -H 'content-type: application/json' \
  -d '{"thread_id":"checkout-demo","user_id":"reader-42","prompt":"I want to buy The Nebius Cloud Atlas."}'
```

Relevant SSE events:

```text
event: status
data: {"phase":"input_guardrail","rule":"all","outcome":"passed"}

event: approval_required
data: {"approvalId":"...","action":"stripe.create_payment_link","book":{"title":"The Nebius Cloud Atlas","amount":1499,"currency":"usd"}}

event: answer
data: {"text":"I can create a Stripe test-mode checkout link ... but I need your approval first."}
```

### `POST /approvals/{approval_id}`

Approve:

```bash
curl -X POST http://localhost:8000/approvals/$APPROVAL_ID \
  -H 'content-type: application/json' \
  -d '{"decision":"approve"}'
```

Reject:

```bash
curl -X POST http://localhost:8000/approvals/$APPROVAL_ID \
  -H 'content-type: application/json' \
  -d '{"decision":"reject"}'
```

Approvals are process-local in this recipe.
Move them to Postgres or Redis before using this pattern across replicas.

## GitHub Actions and live keys

Default CI must stay network-free.
Tests mock Nebius, Stripe REST, and Stripe MCP with `respx`.

If you add an optional manual smoke workflow, keep it opt-in and use a Stripe Sandbox.
Suggested GitHub Actions secrets:

- `NEBIUS_API_KEY`
- `STRIPE_SECRET_KEY`
- `STRIPE_MCP_API_KEY`

Keep live Stripe smoke tests out of pull requests unless the workflow is explicitly marked as sandbox-only.
It is fine to expose generated `data/stripe_books.json` for this demo because it only contains fictional books and sandbox object IDs.

## Observability

Inherited metrics remain available on `/metrics`.
This recipe adds:

- `approval_events_total{status}`
- `stripe_mcp_requests_total{tool,outcome}`
- `stripe_mcp_duration_seconds{tool}`

LangSmith traces record the prompt, thread, user, environment, and model when tracing is enabled.
The Stripe key values and checkout URLs are not logged by the app.

## Tests

```bash
make test
make lint
```

The test suite covers:

- guarded normal book answers
- non-book refusal
- prompt-injection refusal
- PII redaction
- approval creation without Stripe calls
- rejected approvals
- approved Stripe MCP calls
- idempotent completed approvals
- expired approvals
- Stripe REST seed script behavior

## Going further

- Persist approvals in Postgres with row-level ownership by authenticated user.
- Add webhook handling for `checkout.session.completed`.
- Use Stripe restricted keys per environment and rotate them from CI.
- Continue to Cookbook #10 to test the complete action-capable agent with Snowglobe.

## Reference

- Stripe MCP — [docs.stripe.com/mcp](https://docs.stripe.com/mcp)
- Stripe Sandboxes — [docs.stripe.com/sandboxes](https://docs.stripe.com/sandboxes)
- Stripe test mode — [docs.stripe.com/test-mode](https://docs.stripe.com/test-mode)
- Stripe API keys — [docs.stripe.com/keys](https://docs.stripe.com/keys)
- LangChain MCP — [docs.langchain.com/oss/python/langchain/mcp](https://docs.langchain.com/oss/python/langchain/mcp)

## License

MIT
