"""Deploy smoke test: every graph in langgraph.json must import and build.

Catches the classic "renamed a builder, forgot langgraph.json" failure before
`make deploy` ships it — LangGraph Cloud builds all graphs in one process, so
one broken entry fails the whole deployment.
"""
from __future__ import annotations

import importlib
import json
from pathlib import Path

import pytest

_LANGGRAPH_JSON = Path(__file__).resolve().parent.parent / "langgraph.json"
_GRAPHS = json.loads(_LANGGRAPH_JSON.read_text())["graphs"]


@pytest.mark.parametrize("graph_id,target", sorted(_GRAPHS.items()))
def test_graph_entry_builds(graph_id: str, target: str):
    path, attr = target.split(":")
    module_name = path.removeprefix("./").replace("/", ".").removesuffix(".py")
    module = importlib.import_module(module_name)
    factory = getattr(module, attr)
    graph = factory()
    assert hasattr(graph, "invoke"), f"{graph_id}: factory did not return a runnable graph"


def test_langgraph_json_has_expected_graph_count():
    assert len(_GRAPHS) == 7, sorted(_GRAPHS)
