# Contributing to the Nebius Cookbook

Thanks for considering a contribution. This file is the entry point for new contributors.

## Before you start

Read these, in order:

1. [`docs/architecture.md`](./docs/architecture.md) — how the monorepo is organized and why
2. [`docs/adding-a-cookbook.md`](./docs/adding-a-cookbook.md) — step-by-step for new recipes
3. The latest two cookbooks under [`cookbooks/`](./cookbooks/) — they are the reference for what "production-shaped" looks like

## The shape of a contribution

We accept three kinds of contributions:

- **A new cookbook.** Bootstrap with `bun run new`, then follow the workflow in `docs/adding-a-cookbook.md`.
- **An improvement to an existing cookbook.** Bug fix, dependency bump, doc clarification, accessibility fix.
- **Tooling, scripts, or app changes.** The Next.js site, the build scripts, the schemas, the CI workflows.

## Hard requirements (the short version)

- Each cookbook is **autonomous**. No imports between cookbooks. Duplication is fine.
- Code must be **production-shaped**. Type hints, error handling, observability, healthchecks, Dockerfile.
- Tests must pass with **no network access**. Mock Nebius and partner APIs with `respx`.
- Secrets go through **Pydantic Settings**. Never `os.getenv` directly.
- `recipe.json` must validate against `schemas/recipe.schema.json`. CI enforces this.
- The root `README.md` is **generated**. Edit sources in `README/` and run `bun run build:readme`.

## Submitting

1. Fork and branch (`cookbook-NN/description`, `app/description`, or `infra/description`).
2. Make your change. Run `bun run check` and `bun run test:cookbooks` locally.
3. Open a PR. CI must be green before review.
4. Squash merge by default. Conventional Commits (`feat(cookbook-03): …`).

## Questions

Open a GitHub issue with the label `question` or reach out to the maintainers listed in `README.md`.
