# TEMPLATE_TITLE

> **Note:** This is the cookbook template. Replace this README with the real one when bootstrapping a recipe via `bun run new`.

A one-paragraph description of what this recipe demonstrates and who it's for. Lead with the developer pain it addresses.

## What you'll build

A production-shape FastAPI service that…

## Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/)
- A Nebius API key — get one from the [Nebius console](https://nebius.com)

## Run it

```bash
cp .env.example .env
# Open .env and fill NEBIUS_API_KEY

uv sync
make dev
```

Then in another terminal:

```bash
curl -N -X POST http://localhost:8000/agent/run \
  -H 'content-type: application/json' \
  -d '{"prompt":"Hello"}'
```

## Walk-through

…

## Going further

- Cookbook NN — link to the next recipe in the sequence

## License

MIT
