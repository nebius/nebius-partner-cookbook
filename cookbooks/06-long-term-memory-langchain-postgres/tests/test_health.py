"""Healthcheck route smoke tests."""

from __future__ import annotations

from fastapi.testclient import TestClient

from app.main import app


def test_healthz() -> None:
    with TestClient(app) as client:
        response = client.get("/healthz")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_readyz() -> None:
    with TestClient(app) as client:
        response = client.get("/readyz")
    assert response.status_code == 200
    assert response.json()["status"] == "ready"


def test_development_cors_allows_any_localhost_port() -> None:
    with TestClient(app) as client:
        response = client.get("/healthz", headers={"Origin": "http://localhost:3001"})

    assert response.status_code == 200
    assert response.headers["access-control-allow-origin"] == "http://localhost:3001"
