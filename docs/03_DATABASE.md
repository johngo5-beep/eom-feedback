# Database

## Engine

Postgres. Free tier options that work well: **Neon**, Render Postgres, Railway Postgres.

## Table: `feedback_submissions`

| Column | Type | Notes |
| --- | --- | --- |
| `id` | `uuid` | Primary key (`gen_random_uuid()`) |
| `section` | `text` | Application section |
| `comment` | `text` | Feedback body |
| `position` | `text` | Optional; nullable |
| `created_at` | `timestamptz` | Default `now()` |

Index: `(created_at DESC)`.

The app creates this table (and index) automatically on startup if missing.

## Admin query (newest first)

```sql
SELECT created_at, section, position, comment
FROM feedback_submissions
ORDER BY created_at DESC;
```

## Environment

```env
DATABASE_URL=postgresql://user:password@host/dbname?sslmode=require
```

Use the pooled or direct Neon URL; keep SSL on for hosted Postgres.

## Notes

- No ORM — plain SQL via psycopg
- No migrations tool — schema is tiny and idempotent
- Backups: rely on your Postgres provider
