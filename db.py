from __future__ import annotations

from flask import Flask, current_app, g
import psycopg


def get_connection() -> psycopg.Connection:
    if "db_conn" not in g:
        g.db_conn = psycopg.connect(current_app.config["DATABASE_URL"])
    return g.db_conn


def close_connection(_: Exception | None = None) -> None:
    conn = g.pop("db_conn", None)
    if conn is not None:
        conn.close()


def init_db(app: Flask) -> None:
    app.teardown_appcontext(close_connection)

    with app.app_context():
        conn = get_connection()
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
    with conn.cursor() as cur:
        cur.execute(
            """
            INSERT INTO feedback_submissions (section, comment, position)
            VALUES (%s, %s, %s)
            """,
            (section, comment, position),
        )
    conn.commit()
