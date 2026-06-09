"""Pydantic Settings — every env var is validated at boot."""

from __future__ import annotations

from functools import lru_cache
from typing import Annotated, Literal

from pydantic import Field, HttpUrl, field_validator
from pydantic_settings import BaseSettings, NoDecode, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings. Read once at boot, then injected via Depends()."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=False,
    )

    # Nebius
    nebius_api_key: str = Field(..., min_length=1, description="Nebius AgentKit API key")
    nebius_base_url: HttpUrl = Field(default=HttpUrl("https://api.studio.nebius.ai/v1/"))
    nebius_model: str = Field(default="meta-llama/Llama-3.3-70B-Instruct")
    nebius_embedding_model: str = Field(default="Qwen/Qwen3-Embedding-8B")
    nebius_input_price_per_million_tokens: float = Field(default=0.0, ge=0.0)
    nebius_output_price_per_million_tokens: float = Field(default=0.0, ge=0.0)
    nebius_embedding_price_per_million_tokens: float = Field(default=0.0, ge=0.0)
    nebius_enable_pricing_lookup: bool = Field(default=True)

    # Inherited context layers from cookbook 02 and 03.
    pinecone_api_key: str | None = Field(default=None)
    pinecone_index_name: str | None = Field(default=None)
    pinecone_namespace: str | None = Field(default=None)
    tavily_api_key: str | None = Field(default=None)
    tavily_search_depth: Literal["basic", "advanced"] = Field(default="basic")
    tavily_max_results: int = Field(default=5, ge=1, le=10)

    # Server
    host: str = Field(default="0.0.0.0")
    port: int = Field(default=8000, ge=1, le=65535)
    env: Literal["development", "staging", "production"] = Field(default="development")

    # Security
    cors_origins: Annotated[list[str], NoDecode] = Field(
        default_factory=lambda: ["http://localhost:3000"]
    )
    allow_localhost_cors: bool = Field(default=True)
    max_request_bytes: int = Field(default=65_536, ge=1024)

    # Observability
    log_level: Literal["debug", "info", "warning", "error"] = Field(default="info")

    # Limits
    rate_limit_enabled: bool = Field(default=True)
    rate_limit_requests_per_day: int = Field(default=25, ge=1)
    rate_limit_redis_url: str | None = Field(default=None)
    rate_limit_trust_proxy_headers: bool = Field(default=False)
    request_timeout_seconds: int = Field(default=60, ge=1)
    direct_response_max_tokens: int = Field(default=384, ge=64, le=8192)
    deliberate_response_max_tokens: int = Field(default=700, ge=128, le=8192)
    first_token_target_ms: int = Field(default=1200, ge=100)

    @field_validator("cors_origins", mode="before")
    @classmethod
    def _split_cors_origins(cls, value: object) -> object:
        """Accept either a JSON list or a comma-separated string from env."""
        if isinstance(value, str):
            value = value.strip()
            if value.startswith("["):
                return value
            return [v.strip() for v in value.split(",") if v.strip()]
        return value

    @field_validator("pinecone_namespace", mode="before")
    @classmethod
    def _normalize_pinecone_namespace(cls, value: object) -> object:
        """Treat Pinecone's console label for the default namespace as no namespace."""
        if isinstance(value, str):
            value = value.strip()
            if value.lower() in {"", "__default__", "default"}:
                return None
        return value


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """Memoized settings accessor. Use this everywhere — never call Settings() directly."""
    return Settings()  # type: ignore[call-arg]
