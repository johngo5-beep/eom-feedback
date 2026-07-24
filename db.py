from __future__ import annotations

import sqlite3
import uuid
from pathlib import Path
from urllib.parse import urlparse

from flask import Flask, current_app, g

try:
    import psycopg
except ImportError:  # pragma: no cover
    psycopg = None  # type: ignore


def _is_sqlite(url: str) -> bool:
    return url.startswith("sqlite:")


def get_connection():
    if "db_conn" not in g:
        url = current_app.config["DATABASE_URL"]
        if _is_sqlite(url):
            raw_path = url.removeprefix("sqlite:///")
            path = Path(raw_path)
            if not path.is_absolute():
                path = Path(current_app.root_path) / path
            path.parent.mkdir(parents=True, exist_ok=True)
            conn = sqlite3.connect(path)
            conn.row_factory = sqlite3.Row
            g.db_conn = conn
            g.db_kind = "sqlite"
        else:
            if psycopg is None:
                raise RuntimeError("psycopg is required for Postgres DATABASE_URL")
            g.db_conn = psycopg.connect(url)
            g.db_kind = "postgres"
    return g.db_conn


def close_connection(_: BaseException | None = None) -> None:
    conn = g.pop("db_conn", None)
    g.pop("db_kind", None)
    if conn is not None:
        conn.close()


def init_db(app: Flask) -> None:
    app.teardown_appcontext(close_connection)

    with app.app_context():
        conn = get_connection()
        if g.db_kind == "sqlite":
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS feedback_submissions (
                    id TEXT PRIMARY KEY,
                    section TEXT NOT NULL,
                    comment TEXT NOT NULL,
                    position TEXT,
                    created_at TEXT NOT NULL DEFAULT (datetime('now'))
                )
                """
            )
            conn.execute(
                """
                CREATE INDEX IF NOT EXISTS feedback_submissions_created_at_idx
                ON feedback_submissions (created_at DESC)
                """
            )
            conn.commit()
        else:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    CREATE TABLE IF NOT EXISTS feedback_submissions (
                        id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
                        section TEXT NOT NULL,
                        comment TEXT NOT NULL,
                        position TEXT,
                        created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
                    );
                    """
                )
                cur.execute(
                    """
                    CREATE INDEX IF NOT EXISTS feedback_submissions_created_at_idx
                    ON feedback_submissions (created_at DESC);
                    """
                )
            conn.commit()


def insert_feedback(section: str, comment: str, position: str | None) -> None:
    conn = get_connection()
    if g.db_kind == "sqlite":
        conn.execute(
            """
            INSERT INTO feedback_submissions (id, section, comment, position)
            VALUES (?, ?, ?, ?)
            """,
            (str(uuid.uuid4()), section, comment, position),
        )
        conn.commit()
        return

    with conn.cursor() as cur:
        cur.execute(
            """
            INSERT INTO feedback_submissions (section, comment, position)
            VALUES (%s, %s, %s)
            """,
            (section, comment, position),
        )
    conn.commit()


def describe_database_target(url: str) -> str:
    if _is_sqlite(url):
        return f"SQLite ({url})"
    parsed = urlparse(url)
    host = parsed.hostname or "unknown-host"
    db = (parsed.path or "/").lstrip("/") or "postgres"
    return f"Postgres {db}@{host}"
