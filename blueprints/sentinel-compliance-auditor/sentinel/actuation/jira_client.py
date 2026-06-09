"""Thin sync wrapper around the Jira Cloud REST API v3. Basic auth via API token."""
from __future__ import annotations

import base64
import logging
from typing import Any

logger = logging.getLogger(__name__)

SEVERITY_TO_PRIORITY = {
    "critical": "Highest",
    "high": "High",
    "medium": "Medium",
    "low": "Low",
    "info": "Lowest",
}


class JiraClient:
    """Sync client for Jira Cloud REST API v3. One method: create_issue."""

    def __init__(self, base_url: str, email: str, api_token: str, project_key: str, issue_type: str = "Task") -> None:
        import httpx

        self._site = base_url.rstrip("/")
        self._project_key = project_key
        self._issue_type = issue_type
        creds = f"{email}:{api_token}".encode()
        auth = "Basic " + base64.b64encode(creds).decode()
        self._http = httpx.Client(
            timeout=httpx.Timeout(connect=5.0, read=30.0, write=10.0, pool=5.0),
            headers={
                "Authorization": auth,
                "Accept": "application/json",
                "Content-Type": "application/json",
            },
        )

    def create_issue(
        self,
        *,
        summary: str,
        description: str,
        labels: list[str],
        priority: str | None = None,
    ) -> dict[str, str]:
        """POST /rest/api/3/issue. Returns {'key': 'SENT-42', 'url': '...'}."""
        fields: dict[str, Any] = {
            "project": {"key": self._project_key},
            "summary": summary[:240],
            "issuetype": {"name": self._issue_type},
            "labels": labels,
            "description": _plain_text_to_adf(description),
        }
        if priority:
            fields["priority"] = {"name": priority}

        resp = self._http.post(f"{self._site}/rest/api/3/issue", json={"fields": fields})
        resp.raise_for_status()
        data = resp.json()
        key = data["key"]
        return {"key": key, "url": f"{self._site}/browse/{key}"}

    def list_issues(
        self,
        *,
        jql: str,
        fields: list[str] | None = None,
        max_results: int = 100,
    ) -> list[dict[str, Any]]:
        """POST /rest/api/3/search/jql. Returns the `issues` array (truncated at max_results)."""
        body: dict[str, Any] = {
            "jql": jql,
            "fields": fields or ["summary", "status", "priority", "labels", "created", "updated"],
            "maxResults": max_results,
        }
        resp = self._http.post(f"{self._site}/rest/api/3/search/jql", json=body)
        resp.raise_for_status()
        return resp.json().get("issues", [])

    def close(self) -> None:
        self._http.close()


def _plain_text_to_adf(text: str) -> dict[str, Any]:
    """Wrap plain text into Atlassian Document Format. One paragraph per blank-line block."""
    blocks = [b for b in text.split("\n\n") if b.strip()] or [""]
    return {
        "type": "doc",
        "version": 1,
        "content": [
            {"type": "paragraph", "content": [{"type": "text", "text": block}]} for block in blocks
        ],
    }
