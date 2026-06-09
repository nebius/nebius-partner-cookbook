"""Best-effort Nebius model pricing lookup."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import httpx

from app.config import Settings


@dataclass(frozen=True)
class TokenPrices:
    input_per_million: float = 0.0
    output_per_million: float = 0.0
    embedding_per_million: float = 0.0
    source: str = "env"


class NebiusPricing:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        self.base_url = str(settings.nebius_base_url).rstrip("/")
        if not self.base_url.endswith("/v1"):
            self.base_url = f"{self.base_url}/v1"
        self._cached: TokenPrices | None = None

    def get_prices(self) -> TokenPrices:
        if self._cached is not None:
            return self._cached

        env_prices = TokenPrices(
            input_per_million=self.settings.nebius_input_price_per_million_tokens,
            output_per_million=self.settings.nebius_output_price_per_million_tokens,
            embedding_per_million=self.settings.nebius_embedding_price_per_million_tokens,
            source="env",
        )
        if not self.settings.nebius_enable_pricing_lookup:
            self._cached = env_prices
            return self._cached

        try:
            catalog = self._fetch_catalog()
            answer_model = self._find_model(catalog, self.settings.nebius_model)
            embedding_model = self._find_model(catalog, self.settings.nebius_embedding_model)

            input_price = self._first_price(answer_model, ("input", "prompt"))
            output_price = self._first_price(answer_model, ("output", "completion", "generated"))
            embedding_price = self._first_price(embedding_model, ("embedding", "input", "prompt"))

            self._cached = TokenPrices(
                input_per_million=input_price or env_prices.input_per_million,
                output_per_million=output_price or env_prices.output_per_million,
                embedding_per_million=embedding_price or env_prices.embedding_per_million,
                source="nebius-models-api",
            )
            return self._cached
        except Exception:
            self._cached = env_prices
            return self._cached

    def _fetch_catalog(self) -> list[dict[str, Any]]:
        response = httpx.get(
            f"{self.base_url}/models",
            params={"verbose": "true"},
            headers={
                "Authorization": f"Bearer {self.settings.nebius_api_key}",
                "accept": "application/json",
            },
            timeout=5.0,
        )
        response.raise_for_status()
        payload = response.json()
        data = payload.get("data", [])
        if not isinstance(data, list):
            return []
        return [item for item in data if isinstance(item, dict)]

    def _find_model(self, catalog: list[dict[str, Any]], model_id: str) -> dict[str, Any]:
        for model in catalog:
            if model.get("id") == model_id:
                return model
        return {}

    def _first_price(self, model: dict[str, Any], key_hints: tuple[str, ...]) -> float:
        for path, value in self._walk(model):
            path_text = ".".join(path).lower()
            if not all(hint in path_text for hint in key_hints[:1]):
                continue
            if not any(unit in path_text for unit in ("million", "1m", "per_m")):
                continue
            price = self._coerce_price(value, path)
            if price is not None:
                return price

        for path, value in self._walk(model):
            path_text = ".".join(path).lower()
            if any(hint in path_text for hint in key_hints):
                price = self._coerce_price(value, path)
                if price is not None:
                    return price

        return 0.0

    def _walk(self, value: Any, path: tuple[str, ...] = ()) -> list[tuple[tuple[str, ...], Any]]:
        if isinstance(value, dict):
            rows: list[tuple[tuple[str, ...], Any]] = []
            for key, child in value.items():
                rows.extend(self._walk(child, (*path, str(key))))
            return rows
        if isinstance(value, list):
            rows = []
            for index, child in enumerate(value):
                rows.extend(self._walk(child, (*path, str(index))))
            return rows
        return [(path, value)]

    def _coerce_price(self, value: Any, path: tuple[str, ...]) -> float | None:
        if isinstance(value, bool):
            return None
        if isinstance(value, (int, float)) and value >= 0:
            return self._normalize_price_per_million(float(value), path)
        if isinstance(value, str):
            normalized = value.strip().replace("$", "").replace(",", "")
            try:
                price = float(normalized)
            except ValueError:
                return None
            if price >= 0:
                return self._normalize_price_per_million(price, path)
        return None

    def _normalize_price_per_million(self, price: float, path: tuple[str, ...]) -> float:
        path_text = ".".join(path).lower()
        if any(unit in path_text for unit in ("million", "1m", "per_m")):
            return price
        if price > 0 and price < 0.01:
            return price * 1_000_000
        return price
