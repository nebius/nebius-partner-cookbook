# Third-Party License Notices

This file summarizes third-party software, services, datasets, and assets referenced by the Nebius Cookbook.
It complements [`LICENSE`](./LICENSE) and [`TRADEMARK.md`](./TRADEMARK.md).

The source code written for this repository is licensed under the MIT License unless a file says otherwise.
Third-party packages and assets remain under their own licenses and terms.

## JavaScript and TypeScript Packages

Exact resolved versions are recorded in [`bun.lock`](./bun.lock).
The table below lists direct third-party dependencies from the root workspace, the catalog app, and local packages.

| Package | License |
| --- | --- |
| `@next/eslint-plugin-next` | MIT |
| `@radix-ui/react-icons` | MIT |
| `@radix-ui/themes` | MIT |
| `@tailwindcss/postcss` | MIT |
| `@types/bun` | MIT |
| `@types/mdx` | MIT |
| `@types/node` | MIT |
| `@types/react` | MIT |
| `@types/react-dom` | MIT |
| `ajv` | MIT |
| `ajv-formats` | MIT |
| `clsx` | MIT |
| `eslint` | MIT |
| `eslint-config-next` | MIT |
| `eslint-plugin-jsx-a11y` | MIT |
| `eslint-plugin-react` | MIT |
| `eslint-plugin-react-hooks` | MIT |
| `json-schema-to-typescript` | MIT |
| `lucide-react` | ISC |
| `next` | MIT |
| `next-mdx-remote` | MPL-2.0 |
| `react` | MIT |
| `react-dom` | MIT |
| `react-markdown` | MIT |
| `remark` | MIT |
| `remark-gfm` | MIT |
| `tailwindcss` | MIT |
| `typescript` | Apache-2.0 |

Notable transitive dependency: Next.js may install `sharp` and platform-specific `@img/sharp-libvips-*` packages for image processing.
The `sharp` package is Apache-2.0, while the prebuilt libvips packages are LGPL-3.0-or-later.

## Python Packages

Each cookbook is an independent `uv` project.
Exact resolved versions are recorded in each cookbook's `uv.lock`.
The table below lists the direct third-party Python dependencies used across the cookbook projects.

| Package | License |
| --- | --- |
| `asyncpg` | Apache-2.0 |
| `fastapi` | MIT |
| `httpx` | BSD-3-Clause |
| `langchain` | MIT |
| `langgraph` | MIT |
| `langsmith` | MIT |
| `openai` | Apache-2.0 |
| `pinecone` | Apache-2.0 |
| `prometheus-client` | Apache-2.0 AND BSD-2-Clause |
| `pydantic` | MIT |
| `pydantic-settings` | MIT |
| `pytest` | MIT |
| `pytest-asyncio` | Apache-2.0 |
| `respx` | BSD-3-Clause |
| `ruff` | MIT |
| `slowapi` | MIT |
| `structlog` | MIT OR Apache-2.0 |
| `tavily-python` | MIT |
| `tenacity` | Apache-2.0 |
| `uvicorn` | BSD-3-Clause |

Notable transitive Python licenses seen in local environments include MPL-2.0 packages such as `certifi`, `orjson`, and `tqdm`.
Their license texts and notices are supplied by the packages themselves.

## Fonts

The web app uses Google Fonts through `next/font/google` and OpenGraph image generation.

| Font | Source | License |
| --- | --- | --- |
| IBM Plex Sans | Google Fonts | SIL Open Font License 1.1 |
| IBM Plex Mono | Google Fonts | SIL Open Font License 1.1 |
| Jersey 15 | Google Fonts | SIL Open Font License 1.1 |

## Brand Assets

The Nebius logo and Nebius wordmark are not licensed under this repository's MIT License.
See [`TRADEMARK.md`](./TRADEMARK.md) for the Nebius trademark and logo notice.

Other third-party names used in this repository, including OpenAI, Pinecone, Tavily, LangChain, LangGraph, LangSmith, Stripe, Snowglobe, Docker, Python, Bun, Next.js, React, FastAPI, and Clever Cloud, are the property of their respective owners.
Their appearance here is for identification and integration documentation only.

## Images and Generated Assets

The fictional book cover PNG files used by cookbook 09 and the catalog app include C2PA provenance metadata indicating generation with OpenAI image tooling.
They are included as project assets for the fictional demo catalog.

Generated OpenGraph images are produced by the app at build or request time from local recipe metadata, CSS-like styling, and the fonts listed above.

## Goodreads Dataset

The repository references the UCSD Goodreads Book Graph dataset for educational retrieval examples.
The dataset files are not committed to git and must not be redistributed through this project.
See [`TRADEMARK.md`](./TRADEMARK.md) and [`data/README.md`](./data/README.md) for the dataset notice.

## Containers and Runtime Images

Cookbook Dockerfiles use `python:3.12-slim` as the base image and copy `uv` from `ghcr.io/astral-sh/uv`.
Those container images include their own upstream software and operating system package licenses.
If redistributing built container images, include or provide access to the license notices supplied by the base images and installed packages.

## Updating This File

When dependencies change, update this file alongside the lockfiles.
Use [`bun.lock`](./bun.lock) for JavaScript and TypeScript packages, and each cookbook's `uv.lock` plus installed package metadata for Python packages.
