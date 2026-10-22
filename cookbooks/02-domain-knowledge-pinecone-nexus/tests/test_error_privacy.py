"""Public error categories must not reveal provider state outside debug development."""

import httpx
import pytest
from openai import AuthenticationError, BadRequestError, NotFoundError, RateLimitError

from app.config import Settings
from app.core.errors import build_error_event


@pytest.mark.parametrize(
    "error_type,status",
    [
        (AuthenticationError, 401),
        (NotFoundError, 404),
        (RateLimitError, 429),
        (BadRequestError, 400),
    ],
)
@pytest.mark.parametrize(
    "env,debug", [("production", True), ("staging", True), ("development", False)]
)
def test_error_category_is_private(error_type, status: int, env: str, debug: bool) -> None:
    settings = Settings(
        _env_file=None,
        nebius_api_key="test",
        pinecone_api_key="test",
        pinecone_index_name="test",
        tavily_api_key="test",
        env=env,
        nebius_debug_errors=debug,
    )
    response = httpx.Response(status, request=httpx.Request("POST", "https://example.com"))
    event = build_error_event(
        error_type("sensitive upstream payload", response=response, body=None),
        settings=settings,
        request_id="correlation-id",
    )
    assert event == {
        "code": "internal_error",
        "detail": "internal error",
        "requestId": "correlation-id",
    }
