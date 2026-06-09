"""Runtime settings for the book RAG plus Tavily freshness service."""

from __future__ import annotations

from functools import lru_cache
from typing import Annotated, Literal

from pydantic import Field, HttpUrl, field_validator
from pydantic_settings import BaseSettings, NoDecode, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(".env.local", ".env"),
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=False,
    )

    nebius_api_key: str = Field(..., min_length=1)
    nebius_base_url: HttpUrl = Field(default=HttpUrl("https://api.studio.nebius.ai/v1/"))
    nebius_model: str = Field(default="meta-llama/Llama-3.3-70B-Instruct")
    nebius_embedding_model: str = Field(default="Qwen/Qwen3-Embedding-8B")

    pinecone_api_key: str = Field(..., min_length=1)
    pinecone_index_name: str = Field(..., min_length=1)
    pinecone_namespace: str | None = Field(default=None)

    tavily_api_key: str = Field(..., min_length=1)
    tavily_search_depth: Literal["basic", "advanced"] = Field(default="basic")
    tavily_max_results: int = Field(default=5, ge=1, le=10)

    host: str = Field(default="0.0.0.0")
    port: int = Field(default=8000, ge=1, le=65535)
    env: Literal["development", "staging", "production"] = Field(default="development")
    cors_origins: Annotated[list[str], NoDecode] = Field(
        default_factory=lambda: ["http://localhost:3000"]
    )

    rate_limit_enabled: bool = Field(default=True)
    rate_limit_requests_per_day: int = Field(default=25, ge=1)
    rate_limit_redis_url: str | None = Field(default=None)
    rate_limit_trust_proxy_headers: bool = Field(default=False)

    retrieval_top_k: int = Field(default=10, ge=1, le=50)
    related_top_k: int = Field(default=4, ge=1, le=20)
    answer_max_tokens: int = Field(default=900, ge=1, le=4096)
    answer_temperature: float = Field(default=0.2, ge=0.0, le=2.0)
    nebius_input_price_per_million_tokens: float = Field(default=0.0, ge=0.0)
    nebius_output_price_per_million_tokens: float = Field(default=0.0, ge=0.0)
    nebius_embedding_price_per_million_tokens: float = Field(default=0.0, ge=0.0)
    nebius_enable_pricing_lookup: bool = Field(default=True)

    @field_validator("cors_origins", mode="before")
    @classmethod
    def _split_cors_origins(cls, value: object) -> object:
        if isinstance(value, str):
            value = value.strip()
            if value.startswith("["):
                return value
            return [item.strip() for item in value.split(",") if item.strip()]
        return value


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()  # type: ignore[call-arg]
