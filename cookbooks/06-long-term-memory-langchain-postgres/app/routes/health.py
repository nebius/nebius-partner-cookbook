"""Liveness and readiness probes."""

from __future__ import annotations

from fastapi import APIRouter

from app import __version__

router = APIRouter(tags=["health"])


@router.get("/healthz")
async def healthz() -> dict[str, str]:
    """Liveness probe. Returns 200 if the process is up."""
    return {"status": "ok", "version": __version__}


@router.get("/readyz")
async def readyz() -> dict[str, str]:
    """Readiness probe. Currently identical to liveness; extend if you add upstream deps."""
    return {"status": "ready", "version": __version__}
