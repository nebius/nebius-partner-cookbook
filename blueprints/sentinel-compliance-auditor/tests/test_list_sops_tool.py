"""Tests for the list_sops LangChain tool synonym/discovery behavior."""
from __future__ import annotations

from sentinel.graph.tools import list_sops


def test_list_sops_empty_query_returns_all():
    result = list_sops.invoke({"query": ""})
    assert "SOP-CLIN-" in result
    assert "SOP-AIML-" in result
    assert not result.startswith("No SOPs found")


def test_list_sops_fda_synonym_maps_to_clinical():
    result = list_sops.invoke({"query": "FDA"})
    assert "SOP-CLIN-" in result
    assert not result.startswith("No SOPs found")


def test_list_sops_samd_synonym_maps_to_clinical():
    result = list_sops.invoke({"query": "SaMD"})
    assert "SOP-CLIN-" in result


def test_list_sops_machine_learning_synonym_maps_to_aiml():
    result = list_sops.invoke({"query": "machine learning"})
    assert "SOP-AIML-" in result


def test_list_sops_exact_business_unit_still_works():
    result = list_sops.invoke({"query": "Clinical AI Products"})
    assert "SOP-CLIN-" in result
