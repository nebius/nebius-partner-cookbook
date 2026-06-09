"""Long-term user memory with a Postgres production backend."""

from __future__ import annotations

import re
import uuid
from collections.abc import Sequence
from dataclasses import dataclass
from datetime import UTC, datetime
from typing import Protocol

import structlog

from app.config import get_settings

logger = structlog.get_logger()

MEMORY_PATTERNS = (
    re.compile(r"\bremember that (?P<fact>.+)", re.IGNORECASE),
    re.compile(
        r"\bmy (?P<subject>favorite [a-z ]+|preferred [a-z ]+) is (?P<value>.+)",
        re.IGNORECASE,
    ),
    re.compile(r"\bi (?:like|love|prefer) (?P<fact>.+)", re.IGNORECASE),
)
SCHEMA_NAME_RE = re.compile(r"^[a-z][a-z0-9_]{0,62}$")


@dataclass(frozen=True)
class MemoryRecord:
    """A durable user memory."""

    id: str
    user_id: str
    text: str
    source: str
    created_at: datetime


class LongTermMemoryStore(Protocol):
    """Storage contract shared by Postgres and test memory backends."""

    async def list_memories(self, user_id: str, *, limit: int) -> list[MemoryRecord]: ...

    async def recall(self, user_id: str, query: str, *, limit: int) -> list[MemoryRecord]: ...

    async def save_memory(self, user_id: str, text: str, *, source: str) -> MemoryRecord: ...

    async def delete_user_memories(self, user_id: str) -> int: ...


class InMemoryLongTermMemoryStore:
    """Test backend with the same semantics as the Postgres store."""

    def __init__(self) -> None:
        self._records: list[MemoryRecord] = []

    async def list_memories(self, user_id: str, *, limit: int) -> list[MemoryRecord]:
        records = [record for record in self._records if record.user_id == user_id]
        return sorted(records, key=lambda record: record.created_at, reverse=True)[:limit]

    async def recall(self, user_id: str, query: str, *, limit: int) -> list[MemoryRecord]:
        records = await self.list_memories(user_id, limit=100)
        query_terms = {term for term in re.findall(r"[a-z0-9]+", query.lower()) if len(term) > 2}
        ranked = sorted(
            records,
            key=lambda record: (
                len(query_terms.intersection(re.findall(r"[a-z0-9]+", record.text.lower()))),
                record.created_at,
            ),
            reverse=True,
        )
        return ranked[:limit]

    async def save_memory(self, user_id: str, text: str, *, source: str) -> MemoryRecord:
        record = MemoryRecord(
            id=str(uuid.uuid4()),
            user_id=user_id,
            text=text,
            source=source,
            created_at=datetime.now(UTC),
        )
        self._records.append(record)
        return record

    async def delete_user_memories(self, user_id: str) -> int:
        before = len(self._records)
        self._records = [record for record in self._records if record.user_id != user_id]
        return before - len(self._records)


class PostgresLongTermMemoryStore:
    """Postgres-backed long-term memory store.

    LangChain's long-term memory docs model durable memory as JSON documents in
    LangGraph stores. This cookbook keeps the database shape explicit so readers
    can inspect and operate it with standard Postgres tooling.
    """

    def __init__(self, database_url: str, schema: str) -> None:
        self._database_url = database_url
        self._schema_sql = _quote_ident(schema)
        self._table_sql = f'{self._schema_sql}."user_memories"'
        self._pool = None

    async def _get_pool(self):
        if self._pool is None:
            import asyncpg

            self._pool = await asyncpg.create_pool(self._database_url, min_size=1, max_size=5)
            async with self._pool.acquire() as conn:
                await conn.execute(f"create schema if not exists {self._schema_sql}")
                await conn.execute(
                    f"""
                    create table if not exists {self._table_sql} (
                        id uuid primary key,
                        user_id text not null,
                        text text not null,
                        source text not null,
                        created_at timestamptz not null default now()
                    )
                    """
                )
                await conn.execute(
                    f"""
                    create index if not exists "user_memories_user_created_idx"
                    on {self._table_sql} (user_id, created_at desc)
                    """
                )
        return self._pool

    async def list_memories(self, user_id: str, *, limit: int) -> list[MemoryRecord]:
        pool = await self._get_pool()
        async with pool.acquire() as conn:
            query = f"""
                select id::text, user_id, text, source, created_at
                from {self._table_sql}
                where user_id = $1
                order by created_at desc
                limit $2
                """  # noqa: S608 - table identifier is schema-validated and quoted.
            rows = await conn.fetch(query, user_id, limit)
        return [_record_from_row(row) for row in rows]

    async def recall(self, user_id: str, query: str, *, limit: int) -> list[MemoryRecord]:
        pool = await self._get_pool()
        async with pool.acquire() as conn:
            recall_query = f"""
                select id::text, user_id, text, source, created_at,
                       ts_rank_cd(
                           to_tsvector('simple', text),
                           plainto_tsquery('simple', $2)
                       ) as rank
                from {self._table_sql}
                where user_id = $1
                order by rank desc, created_at desc
                limit $3
                """  # noqa: S608 - table identifier is schema-validated and quoted.
            rows = await conn.fetch(recall_query, user_id, query, limit)
        return [_record_from_row(row) for row in rows]

    async def save_memory(self, user_id: str, text: str, *, source: str) -> MemoryRecord:
        pool = await self._get_pool()
        memory_id = uuid.uuid4()
        async with pool.acquire() as conn:
            insert_query = f"""
                insert into {self._table_sql} (id, user_id, text, source)
                values ($1, $2, $3, $4)
                returning id::text, user_id, text, source, created_at
                """  # noqa: S608 - table identifier is schema-validated and quoted.
            row = await conn.fetchrow(insert_query, memory_id, user_id, text, source)
        return _record_from_row(row)

    async def delete_user_memories(self, user_id: str) -> int:
        pool = await self._get_pool()
        async with pool.acquire() as conn:
            result = await conn.execute(
                f"delete from {self._table_sql} where user_id = $1",  # noqa: S608
                user_id,
            )
        return int(result.rsplit(" ", 1)[-1])


def _record_from_row(row: object) -> MemoryRecord:
    return MemoryRecord(
        id=str(row["id"]),
        user_id=str(row["user_id"]),
        text=str(row["text"]),
        source=str(row["source"]),
        created_at=row["created_at"],
    )


def _quote_ident(value: str) -> str:
    """Quote a trusted Postgres identifier after strict validation."""
    if not SCHEMA_NAME_RE.fullmatch(value):
        raise ValueError(
            "memory schema must start with a lowercase letter and contain only lowercase "
            "letters, numbers, and underscores"
        )
    return f'"{value}"'


def extract_memories(prompt: str) -> list[str]:
    """Extract explicit user facts worth storing.

    Production agents often use a tool or classifier for this. The cookbook keeps
    extraction deterministic so tests stay network-free.
    """
    memories: list[str] = []
    for pattern in MEMORY_PATTERNS:
        match = pattern.search(prompt.strip())
        if not match:
            continue
        groups = match.groupdict()
        if "subject" in groups and groups.get("subject") and groups.get("value"):
            memories.append(f"User's {groups['subject'].strip()} is {groups['value'].strip()}")
        elif groups.get("fact"):
            memories.append(groups["fact"].strip())
    cleaned: list[str] = []
    seen: set[str] = set()
    for memory in memories:
        value = _clean_memory(memory)
        key = value.lower()
        if value and key not in seen:
            cleaned.append(value)
            seen.add(key)
    return cleaned


def memories_as_history(memories: Sequence[MemoryRecord]) -> list[dict[str, str]]:
    """Convert recalled memories into synthetic context for the writer prompt."""
    if not memories:
        return []
    text = "\n".join(f"- {record.text}" for record in memories)
    return [{"role": "memory", "content": f"Long-term user memories:\n{text}"}]


def _clean_memory(memory: str) -> str:
    value = memory.strip().rstrip(".")
    value = re.sub(r"^i prefer\s+", "", value, flags=re.IGNORECASE)
    return value[:500]


_memory_backend: LongTermMemoryStore | None = None


def get_long_term_memory_store() -> LongTermMemoryStore:
    """FastAPI dependency for long-term memory."""
    global _memory_backend
    if _memory_backend is None:
        settings = get_settings()
        if settings.memory_backend == "memory":
            logger.warning("using_in_memory_long_term_memory")
            _memory_backend = InMemoryLongTermMemoryStore()
        else:
            _memory_backend = PostgresLongTermMemoryStore(
                settings.postgresql_addon_uri,
                settings.memory_schema,
            )
    return _memory_backend
