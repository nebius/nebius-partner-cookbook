"""Deterministic routing policy tests do not call a model."""

from __future__ import annotations

import pytest

from app.core.routing import bounded_output_tokens, classify_request


@pytest.mark.parametrize(
    ("prompt", "expected_route", "expected_need"),
    [
        ("Explain the ending of Dune.", "direct", "direct_answer"),
        ("Recommend books about climate.", "deliberate", "curated_recommendation"),
        ("What is the latest edition of Dune?", "deliberate", "fresh_publication_context"),
        (
            "Recommend recent climate fiction.",
            "deliberate",
            "curated_plus_fresh_context",
        ),
    ],
)
def test_classify_request(
    prompt: str,
    expected_route: str,
    expected_need: str,
) -> None:
    decision = classify_request(prompt)

    assert decision.route == expected_route
    assert decision.context_need == expected_need


def test_history_can_make_a_follow_up_a_recommendation() -> None:
    decision = classify_request(
        "More like that, please.",
        [{"role": "user", "content": "Recommend books about fitness."}],
    )

    assert decision.context_need == "curated_recommendation"


def test_token_budget_is_code_owned() -> None:
    assert (
        bounded_output_tokens(
            2_048,
            route="direct",
            direct_limit=384,
            deliberate_limit=700,
        )
        == 384
    )
    assert (
        bounded_output_tokens(
            120,
            route="deliberate",
            direct_limit=384,
            deliberate_limit=700,
        )
        == 120
    )
