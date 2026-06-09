#!/usr/bin/env python3
"""Probe whether each configured model accepts the `max_tokens` parameter.

Resolves the documented constraint that some Nebius models reject
`max_tokens` / `max_completion_tokens` (see CLAUDE.md and the DeepSeek-only
branch in `sentinel/graph/tools.py:_build_subagent_model`). For every model in
`NEBIUS_MODELS` (plus the OpenAI `gpt-5.5`), this makes one tiny live chat
completion with the parameter set and reports accept / reject / error.

The probe uses the raw OpenAI SDK (not ChatOpenAI) so it sends exactly the
parameter being tested, with nothing else that could muddy the result.

Usage:
    python3 scripts/check_max_tokens_support.py
    python3 scripts/check_max_tokens_support.py --param max_completion_tokens
    python3 scripts/check_max_tokens_support.py --value 256

Requires NEBIUS_API_KEY (to test the Nebius models) and OPENAI_API_KEY (to
test gpt-5.5). Models whose provider key is unset are skipped.
"""
from __future__ import annotations

import argparse
import sys

from openai import (
    APIError,
    AuthenticationError,
    BadRequestError,
    NotFoundError,
    OpenAI,
)

from sentinel.config import (
    NEBIUS_API_KEY,
    NEBIUS_BASE_URL,
    NEBIUS_MODELS,
    OPENAI_API_KEY,
    OPENAI_MODEL,
)

# (label, model_id, provider, base_url, api_key)
def _targets() -> list[tuple[str, str, str, str | None, str]]:
    targets: list[tuple[str, str, str, str | None, str]] = []
    for key, model_id in NEBIUS_MODELS.items():
        targets.append((key, model_id, "nebius", NEBIUS_BASE_URL, NEBIUS_API_KEY))
    targets.append(("openai", OPENAI_MODEL, "openai", None, OPENAI_API_KEY))
    return targets


def _probe(model_id: str, base_url: str | None, api_key: str, param: str, value: int) -> tuple[str, str]:
    """Return (status, detail). status is ACCEPTS / REJECTS / SKIP / ERROR."""
    if not api_key:
        return "SKIP", "provider API key not set"
    client = OpenAI(api_key=api_key, base_url=base_url, timeout=60.0, max_retries=0)
    try:
        client.chat.completions.create(
            model=model_id,
            messages=[{"role": "user", "content": "ping"}],
            **{param: value},
        )
        return "ACCEPTS", f"call succeeded with {param}={value}"
    except BadRequestError as e:
        # 400 — the most likely signal that the parameter is unsupported.
        return "REJECTS", _short(e)
    except NotFoundError as e:
        return "ERROR", f"model not found / unavailable: {_short(e)}"
    except AuthenticationError as e:
        return "ERROR", f"auth failed: {_short(e)}"
    except APIError as e:
        return "ERROR", _short(e)
    except Exception as e:  # network, timeout, etc.
        return "ERROR", f"{type(e).__name__}: {e}"


def _short(exc: Exception) -> str:
    msg = str(exc).replace("\n", " ").strip()
    return msg[:200] + ("…" if len(msg) > 200 else "")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--param",
        default="max_tokens",
        choices=["max_tokens", "max_completion_tokens"],
        help="which parameter to probe (default: max_tokens)",
    )
    ap.add_argument(
        "--value",
        type=int,
        default=16_000,
        help="value to send for the parameter (default: 16000, matching MODEL_MAX_TOKENS)",
    )
    args = ap.parse_args()

    targets = _targets()
    print(f"Probing {args.param}={args.value} across {len(targets)} model(s)\n")

    rows: list[tuple[str, str, str, str]] = []
    for label, model_id, provider, base_url, api_key in targets:
        status, detail = _probe(model_id, base_url, api_key, args.param, args.value)
        rows.append((label, f"{provider}:{model_id}", status, detail))

    label_w = max(len(r[0]) for r in rows)
    model_w = max(len(r[1]) for r in rows)
    for label, model, status, detail in rows:
        mark = {"ACCEPTS": "✓", "REJECTS": "✗", "SKIP": "·", "ERROR": "!"}[status]
        print(f"  {mark} {label.ljust(label_w)}  {model.ljust(model_w)}  {status:<8}  {detail}")

    accepts = [r[0] for r in rows if r[2] == "ACCEPTS"]
    rejects = [r[0] for r in rows if r[2] == "REJECTS"]
    print(f"\nAccepts {args.param}: {', '.join(accepts) or '(none)'}")
    print(f"Rejects {args.param}: {', '.join(rejects) or '(none)'}")
    if any(r[2] == "ERROR" for r in rows):
        print("Some probes errored (not a clean accept/reject) — see details above.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
