# Simulation — Testing Before Production with Snowglobe

> 🚧 **Scaffold only.** This recipe is planned but not yet implemented. This folder currently holds metadata and documentation for the Snowglobe testing cookbook.

Recipe **10 of 10** in the Agent Blueprint Recipes arc:

> Foundation → Knowledge → Grounding → Orchestration → Thread Memory → User Memory → Observability → Guardrails → Actions → **Simulation**

You've built, remembered, observed, guarded, and connected the agent to human-approved actions.
You still do not know how the complete system behaves across the thousands of conversations you will never hand-test.

## What you'll build

A FastAPI service plus a simulation harness around Snowglobe:

1. **Generate** — Snowglobe produces synthetic personas and scenarios.
2. **Run** — each scenario is played against the action-capable agent.
3. **Score** — transcripts are judged for failures, regressions, edge-case behavior, and unsafe action handling.
4. **Gate** — a smoke suite can run in CI before release.

## Planned endpoints

| Method | Path | Purpose |
| ------ | ---- | ------- |
| POST | `/agent/run` | Run the agent under test and stream SSE events. |
| POST | `/simulate` | Launch a Snowglobe simulation batch and return scored results. |
| GET | `/healthz` | Liveness probe. |
| GET | `/readyz` | Readiness probe. |
| GET | `/metrics` | Prometheus scrape endpoint. |

## Planned scenario suite

- Valid book recommendations that depend on stored reader preferences.
- Topic-boundary drift such as cooking, news, or script execution requests.
- Prompt-injection attempts that try to disable guardrails or approval checks.
- PII handling during otherwise valid book conversations.
- Unauthorized checkout attempts that must not call Stripe.
- Approved and rejected checkout flows for the fictional book purchase.

## Design decisions

**Simulation complements tests.** Unit tests verify known cases.
Snowglobe samples the unknown conversational surface.

**Memory stays isolated.** When this recipe gets its runtime app, it should reuse the shared Postgres database from cookbooks #6-#9 with an environment-derived schema: `dev_cbk_10` locally and `prod_cbk_10` when `ENV=production`.
That keeps simulated user memories separate from the action cookbook's `prod_cbk_09.user_memories` table.

**Gate on deltas.** Absolute LLM-judge scores are noisy.
The CI story should compare against a baseline and fail on meaningful regression.

**Mock Snowglobe in tests.** No network calls run by default.
Live simulation requires LangSmith/Snowglobe credentials and Stripe test-mode keys for action scenarios.

## Reference

- Snowglobe — [snowglobetx.com](https://snowglobetx.com)
- LangSmith — [docs.langchain.com/langsmith/home](https://docs.langchain.com/langsmith/home)

## License

MIT
