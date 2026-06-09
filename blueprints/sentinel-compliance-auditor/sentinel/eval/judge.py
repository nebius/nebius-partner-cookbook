"""LLM-as-judge for freeform Q&A answers.

Caveat: by default the judge uses the same Nebius model that's being graded.
That's a known self-grading bias — documented in the eval comparison output.
For the demo it keeps cost down and the relative ranking (naive vs agentic)
is what we care about, not absolute scores.
"""
from __future__ import annotations

import json
import re

from sentinel.config import NEBIUS_MODELS

JUDGE_PROMPT = """You are a strict regulatory-compliance answer grader. Score the candidate answer against the reference on two axes:

- correctness (0 = wrong / missing, 1 = partially correct or vague, 2 = fully correct and on-point)
- citations (0 = no specific citation, 1 = some citations but missing or wrong sections, 2 = cites the expected regulation(s) and section(s))

Question:
{question}

Reference answer:
{reference}

Expected citations:
{citations}

Candidate answer:
{candidate}

Respond with ONLY a JSON object in this exact form (no markdown, no commentary):
{{"correctness": 0|1|2, "citations": 0|1|2, "rationale": "one-sentence justification"}}"""


JUDGE_MODEL = NEBIUS_MODELS["deepseek-v4-pro"]


def _build_judge_model():
    from sentinel.chat_model import build_chat_model

    return build_chat_model(
        "nebius",
        model=JUDGE_MODEL,
        temperature=0.0,
        max_tokens=400,
        extra_metadata={"eval_mode": "judge"},
    )


def _extract_json(text: str) -> dict | None:
    if not text:
        return None
    # Strip ``` fences if present.
    fence = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", text, re.DOTALL)
    if fence:
        text = fence.group(1)
    start = text.find("{")
    end = text.rfind("}")
    if start < 0 or end <= start:
        return None
    try:
        return json.loads(text[start : end + 1])
    except json.JSONDecodeError:
        return None


def judge_answer(question: str, reference: str, citations: list[dict], candidate: str) -> dict:
    """Return {correctness, citations, rationale, input_tokens, output_tokens}.

    Scores are in [0, 2]; -1 indicates the judge call failed to return parseable JSON.
    """
    citation_str = (
        "\n".join(f"- {c.get('regulation', '')}: {c.get('section', '')}" for c in citations)
        if citations
        else "(none specified)"
    )
    prompt = JUDGE_PROMPT.format(
        question=question,
        reference=reference or "(none)",
        citations=citation_str,
        candidate=candidate or "(empty)",
    )

    model = _build_judge_model()
    response = model.invoke([{"role": "user", "content": prompt}])
    content = response.content if hasattr(response, "content") else str(response)
    parsed = _extract_json(content) or {}
    usage = getattr(response, "usage_metadata", None) or {}

    def _score(val) -> int:
        try:
            n = int(val)
        except (TypeError, ValueError):
            return -1
        return n if n in (0, 1, 2) else -1

    return {
        "correctness": _score(parsed.get("correctness")),
        "citations": _score(parsed.get("citations")),
        "rationale": parsed.get("rationale", "") if isinstance(parsed.get("rationale"), str) else "",
        "input_tokens": usage.get("input_tokens", 0),
        "output_tokens": usage.get("output_tokens", 0),
        "raw": content,
    }
