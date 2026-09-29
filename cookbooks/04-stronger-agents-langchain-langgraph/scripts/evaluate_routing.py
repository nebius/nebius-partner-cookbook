"""Run the checked-in routing evaluation without model or network calls."""

from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import TypedDict

from app.core.routing import ContextNeed, RouteName, classify_request


class RoutingCase(TypedDict):
    name: str
    prompt: str
    route: RouteName
    contextNeed: ContextNeed


def main() -> None:
    cases_path = Path(__file__).parents[1] / "evals" / "routing_cases.json"
    cases: list[RoutingCase] = json.loads(cases_path.read_text(encoding="utf-8"))
    failures: list[str] = []

    for case in cases:
        decision = classify_request(case["prompt"])
        if decision.route != case["route"] or decision.context_need != case["contextNeed"]:
            failures.append(
                f"{case['name']}: expected {case['route']}/{case['contextNeed']}, "
                f"got {decision.route}/{decision.context_need}"
            )

    if failures:
        raise SystemExit("Routing evaluation failed:\n- " + "\n- ".join(failures))
    logging.info("routing_evaluation_passed cases=%d", len(cases))


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    main()
