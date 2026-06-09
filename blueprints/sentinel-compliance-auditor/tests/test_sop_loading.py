"""Regression tests for SOP loading and parsing."""
from __future__ import annotations


import pytest

from sentinel.models import SOPChunk
from sentinel.retrieval.ingest import parse_sop
from sentinel.retrieval.local import load_sop_chunks


@pytest.fixture
def sop_file(tmp_path):
    content = """---
sop_id: SOP-TEST-001
title: Test SOP
business_unit: information_security
regulations:
  - HIPAA
  - SOC 2
---

## 1. Purpose

This SOP defines the test procedure.

## 2. Scope

Applies to all test systems.

## 3. Procedures

Step 1: Do the thing.
Step 2: Verify the thing.
"""
    fp = tmp_path / "sop_test_001.md"
    fp.write_text(content)
    return fp


@pytest.fixture
def sop_no_frontmatter(tmp_path):
    content = "## Section One\n\nSome content here.\n\n## Section Two\n\nMore content."
    fp = tmp_path / "no_frontmatter.md"
    fp.write_text(content)
    return fp


class TestParseSop:
    def test_frontmatter_extracted(self, sop_file):
        parsed = parse_sop(sop_file)
        fm = parsed["frontmatter"]
        assert fm["sop_id"] == "SOP-TEST-001"
        assert fm["title"] == "Test SOP"
        assert "HIPAA" in fm["regulations"]

    def test_body_extracted(self, sop_file):
        parsed = parse_sop(sop_file)
        assert "## 1. Purpose" in parsed["body"]
        assert "## 3. Procedures" in parsed["body"]

    def test_no_frontmatter(self, sop_no_frontmatter):
        parsed = parse_sop(sop_no_frontmatter)
        assert parsed["frontmatter"] == {}
        assert "Section One" in parsed["body"]

    def test_path_preserved(self, sop_file):
        parsed = parse_sop(sop_file)
        assert parsed["path"] == str(sop_file)


class TestLoadSopChunks:
    def test_splits_by_section(self, sop_file):
        parsed = parse_sop(sop_file)
        chunks = load_sop_chunks(parsed)
        assert len(chunks) == 3
        assert all(isinstance(c, SOPChunk) for c in chunks)

    def test_section_headers(self, sop_file):
        parsed = parse_sop(sop_file)
        chunks = load_sop_chunks(parsed)
        headers = [c.section for c in chunks]
        assert "1. Purpose" in headers
        assert "2. Scope" in headers
        assert "3. Procedures" in headers

    def test_metadata_propagated(self, sop_file):
        parsed = parse_sop(sop_file)
        chunks = load_sop_chunks(parsed)
        for c in chunks:
            assert c.sop_id == "SOP-TEST-001"
            assert c.title == "Test SOP"
            assert c.business_unit == "information_security"

    def test_empty_body(self):
        parsed = {"frontmatter": {"sop_id": "X", "title": "T", "business_unit": "BU"}, "body": ""}
        chunks = load_sop_chunks(parsed)
        assert chunks == []

    def test_single_section(self):
        parsed = {
            "frontmatter": {"sop_id": "X", "title": "T", "business_unit": "BU"},
            "body": "## Only Section\n\nContent here.",
        }
        chunks = load_sop_chunks(parsed)
        assert len(chunks) == 1
        assert chunks[0].section == "Only Section"

    def test_body_without_headers(self):
        parsed = {
            "frontmatter": {"sop_id": "X", "title": "T", "business_unit": "BU"},
            "body": "Plain text with no headers at all.",
        }
        chunks = load_sop_chunks(parsed)
        assert len(chunks) == 1
        assert chunks[0].section == ""
