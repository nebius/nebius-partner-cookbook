"""Regression tests for config constants and pricing."""
from __future__ import annotations

from sentinel.config import (
    MODEL,
    OPENAI_MODEL,
    NEBIUS_BASE_URL,
    PRICING,
    SOP_BUSINESS_UNITS,
    EMBEDDING_DIMENSION,
    EMBEDDING_MODEL,
)


class TestPricing:
    def test_deepseek_pricing_exists(self):
        assert MODEL in PRICING
        p = PRICING[MODEL]
        assert p["input"] > 0
        assert p["output"] > 0

    def test_openai_pricing_exists(self):
        assert OPENAI_MODEL in PRICING
        p = PRICING[OPENAI_MODEL]
        assert p["input"] > 0
        assert p["output"] > 0

    def test_output_more_expensive_than_input(self):
        for model, p in PRICING.items():
            assert p["output"] >= p["input"], f"{model}: output should cost >= input"


class TestConstants:
    def test_model_names(self):
        assert MODEL == "deepseek-ai/DeepSeek-V4-Pro"
        assert OPENAI_MODEL == "gpt-5.5"

    def test_nebius_base_url(self):
        assert NEBIUS_BASE_URL.startswith("https://")
        assert "nebius" in NEBIUS_BASE_URL

    def test_embedding_config(self):
        assert EMBEDDING_DIMENSION == 4096
        assert "Qwen" in EMBEDDING_MODEL

    def test_business_units(self):
        assert len(SOP_BUSINESS_UNITS) == 10
        assert "01_ai_ml_engineering" in SOP_BUSINESS_UNITS
        assert "05_information_security" in SOP_BUSINESS_UNITS
        for bu in SOP_BUSINESS_UNITS:
            assert bu[0:2].isdigit(), f"Business unit '{bu}' should start with number prefix"
