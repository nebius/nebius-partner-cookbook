# Benchmarking cookbook recipes

Benchmark the system around the model, not a model in isolation.
Use one checked-in workload version, one model, and identical settings for at least five runs.

Write one JSON object per run to a JSONL trace:

```json
{"model":"Qwen/Qwen3-30B-A3B-Instruct-2507","workloadVersion":"book-follow-up-v1","inputTokens":742,"outputTokens":219,"latencySeconds":11.2,"costUsd":0.004}
```

Keep full tool-call arguments, results, and per-tool latency in a private trace when they may contain sensitive data.
The publishable summary contains only the model, workload version, run count, measurement date, and medians.

Generate the `recipe.json` benchmark block with:

```bash
bun run benchmark:summarize path/to/runs.jsonl
```

Record input and output tokens separately.
Repeated conversation and tool context can make input tokens dominate agent cost, and a combined total hides that design signal.

Do not compare models across different prompts, tool policies, context windows, or scorer versions.
Treat small differences from five-run samples as directional and disclose known scorer defects.

### Missing stream usage

`nebius_tokens_total` records token counts reported by the provider.
A proxy that drops the final usage frame leaves those totals incomplete; chunks are not a reliable token count.
The streaming cookbooks expose `nebius_streams_without_usage_total{model}` and log `nebius_stream_usage_missing` for missing or null usage fields.
Check this counter before using token totals for a benchmark, and configure the proxy to preserve `stream_options` and the final usage frame.
