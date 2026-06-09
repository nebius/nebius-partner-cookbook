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
    nebius_input_price_per_million_tokens: float = Field(default=0.0, ge=0.0)
    nebius_output_price_per_million_tokens: float = Field(default=0.0, ge=0.0)
    nebius_enable_pricing_lookup: bool = Field(default=True)

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
    langsmith_tracing: bool = Field(default=False)
    langsmith_api_key: str | None = Field(default=None)
    langsmith_project: str = Field(default="nebius-cookbook-actions")
    langsmith_endpoint: HttpUrl = Field(default=HttpUrl("https://api.smith.langchain.com"))

    # Long-term memory inherited from Cookbook #6
    memory_backend: Literal["postgres", "memory"] = Field(default="postgres")
    postgresql_addon_uri: str = Field(
        default="postgresql://postgres:postgres@localhost:5432/nebius_cookbook"
    )
    long_term_memory_limit: int = Field(default=5, ge=1, le=20)

    # Guardrails
    guardrails_enabled: bool = Field(default=True)
    guardrails_topic: str = Field(default="books and reading recommendations")
    guardrails_max_output_chars: int = Field(default=6_000, ge=500, le=20_000)

    # Stripe MCP actions
    stripe_mcp_base_url: HttpUrl = Field(default=HttpUrl("https://mcp.stripe.com"))
    stripe_mcp_api_key: str = Field(default="sk_test_replace_me", min_length=1)
    stripe_secret_key: str = Field(
        default="sk_test_replace_me",
        min_length=1,
        description="Used by the seed script only; runtime actions use STRIPE_MCP_API_KEY.",
    )
    book_catalog_path: str = Field(default="data/stripe_books.json")
    approval_ttl_seconds: int = Field(default=900, ge=30, le=86_400)

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

    @property
    def memory_schema(self) -> str:
        """Build the Postgres schema name from the deployment environment."""
        prefix = "prod" if self.env == "production" else "dev"
        return f"{prefix}_cbk_09"


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """Memoized settings accessor. Use this everywhere — never call Settings() directly."""
    return Settings()  # type: ignore[call-arg]
