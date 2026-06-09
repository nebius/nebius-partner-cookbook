# Adding a cookbook

A step-by-step guide to shipping a new recipe. For the contribution workflow, see [`../CONTRIBUTING.md`](../CONTRIBUTING.md). For how the monorepo fits together, see [`architecture.md`](./architecture.md).

## Before you start

A new cookbook earns its place by demonstrating one concrete piece of the prototype → production journey for AI agents. If you can't say "this recipe teaches the reader X, which the existing cookbooks don't cover," stop and write that down first.

A good cookbook proposal answers four questions:

1. **The pain.** What is the developer trying to do that hurts today?
2. **The fix.** What does the cookbook show, in one paragraph?
3. **The boundary.** What is explicitly *not* in this cookbook?
4. **The next step.** Which existing cookbook does this one follow from, and which future one builds on it?

Open a draft PR with just the proposal in `cookbooks/NN-<slug>/recipe.json` before writing code. It is much cheaper to iterate on scope than on a half-built FastAPI app.

## Step 1 — Bootstrap

```bash
bun run new
```

The interactive prompt asks for:

- Title (e.g. "Streaming RAG with Pinecone Nexus")
- Slug (defaults to a slugified title)
- Difficulty (`beginner` / `intermediate` / `advanced`)

It picks the next `order` number, copies `cookbooks/_template/` to `cookbooks/NN-<slug>/`, and pre-fills `recipe.json` with your inputs and today's date.

## Step 2 — Edit `recipe.json`

The schema lives at [`schemas/recipe.schema.json`](../schemas/recipe.schema.json). The fields you'll touch most:

- `tagline` — one sentence that ends up under the title in the catalog
- `story.problem`, `story.solution`, `story.outcome` — the README story arc compressed to three sentences each
- `stack.primary` and `stack.secondary` — what powers it
- `models` — `id` + `role` for each model the cookbook uses
- `prerequisites` — be honest, "Python 3.12 and a Nebius key" is fine
- `nextRecipe` — slug of the recipe this links to, if any

Validate as you go:

```bash
bun run validate
```

## Step 3 — Refresh the root README

```bash
bun run build:readme
```

This regenerates the table of recipes at the repo root. Commit `README.md` alongside your `recipe.json`. CI runs `bun run build:readme --check` and fails if the working tree drifts.

## Step 4 — Implement the FastAPI app

Build inside `cookbooks/NN-<slug>/app/`. The template gives you:

- Pydantic-validated settings (`app/config.py`)
- A Nebius client wrapper with timeouts and retries (`app/core/nebius_client.py`)
- A streaming agent example (`app/core/agent.py`)
- An SSE route (`app/routes/agent.py`) with heartbeat and client-disconnect handling
- Healthchecks, metrics, structlog, security headers, rate limiting, CORS — all wired up

Your job is to make the cookbook *teach* something. Replace `app/core/agent.py` with the logic your story promised. Add or remove routes as needed. Keep the observability and middleware. Keep the contract — Pydantic models on every boundary, settings via `pydantic-settings`, async everywhere.
Rate limiting details and env examples live in [`rate-limiting.md`](./rate-limiting.md).

## Step 5 — Tests

Every route gets at least one happy-path test. Every external call is mocked with [respx](https://lundberg.github.io/respx/). No test makes a network request.

```bash
cd cookbooks/NN-<slug>
make test
```

If your cookbook adds a new external dependency (e.g. Tavily), add the mock in `tests/conftest.py` or per-test, and add it to `pyproject.toml`.

## Step 6 — Dockerfile, Makefile, env

The `_template` ships with all three. Update:

- `Dockerfile` only if you add a system-level dep (e.g. `libpq` for Postgres)
- `Makefile` if you add a new top-level workflow (e.g. `make seed`)
- `.env.example` for **every** required env var, with placeholder values and inline comments

## Step 7 — Write the cookbook README

Cookbook READMEs are hand-written and single-file (no composition pattern). Use this structure:

1. **Title and tagline** as `<h1>` and a `>` blockquote
2. **One-paragraph hook** that names the pain and the fix
3. **What you'll build** — table of endpoints or a tree of the app dir
4. **Prerequisites** — terse, copy-pasteable
5. **Run it** — clone, configure, run; a sample `curl` against the live endpoint
6. **Walk-through** — the *teaching* section. Diagrams welcome. Code snippets with file pointers.
7. **Test it** — `make test`, one sentence on what's mocked
8. **Ship it** — Docker build, deploy pointer
9. **Going further** — link to the next cookbook and to 1–3 extension ideas
10. **License** — point at the root LICENSE

## Step 8 — Run the full check locally

```bash
bun run check                # validates recipes + README composition
cd cookbooks/NN-<slug>
make lint
make test
```

## Step 9 — Open the PR

Conventional commit prefix `feat(cookbook-NN)` (or `cookbook-NN/<topic>` branch). PR description should answer the four questions from "Before you start." CI must be green before review.

## Step 10 — Flag conventions you had to break

If your recipe needed something that contradicts the existing conventions documented in [`../CONTRIBUTING.md`](../CONTRIBUTING.md) or [`architecture.md`](./architecture.md), don't hide the deviation. Open the PR with the convention update alongside the code change and explain *why* in the PR description — the docs follow the code, not the other way around.
