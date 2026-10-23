"""Run thread-memory regression cases without a model or network."""

from __future__ import annotations

import asyncio
import json
import logging
from pathlib import Path
from typing import TypedDict

from app.core.thread_memory import ThreadMemoryStore


class Turn(TypedDict):
    user: str
    assistant: str


class MemoryCase(TypedDict):
    name: str
    threadId: str
    maxMessages: int
    turns: list[Turn]
    expectedContents: list[str]


async def evaluate() -> None:
    cases_path = Path(__file__).parents[1] / "evals" / "memory_cases.json"
    cases: list[MemoryCase] = json.loads(cases_path.read_text(encoding="utf-8"))
    failures: list[str] = []

    for case in cases:
        store = ThreadMemoryStore(max_messages_per_thread=case["maxMessages"])
        for turn in case["turns"]:
            await store.append_turn(
                case["threadId"],
                user=turn["user"],
                assistant=turn["assistant"],
            )

        history = await store.get_history(case["threadId"])
        contents = [message["content"] for message in history]
        if contents != case["expectedContents"]:
            failures.append(
                f"{case['name']}: expected {case['expectedContents']!r}, got {contents!r}"
            )
        if await store.get_history("unrelated-thread"):
            failures.append(f"{case['name']}: memory leaked into an unrelated thread")
        if not await store.clear(case["threadId"]):
            failures.append(f"{case['name']}: reset did not report deletion")
        if await store.get_history(case["threadId"]):
            failures.append(f"{case['name']}: reset retained messages")

    if failures:
        raise SystemExit("Memory evaluation failed:\n- " + "\n- ".join(failures))
    logging.info("memory_evaluation_passed cases=%d", len(cases))


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    asyncio.run(evaluate())
