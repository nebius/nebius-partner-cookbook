"""Collect the checked-in offline evaluation in the normal test suite."""

import asyncio

from scripts.evaluate_memory import evaluate


def test_offline_evaluation() -> None:
    asyncio.run(evaluate())
