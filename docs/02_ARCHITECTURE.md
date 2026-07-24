# Architecture

## Stack

| Layer | Choice |
| --- | --- |
| Framework | Flask 3 |
| Templates | Jinja2 |
| Database | Postgres (e.g. Neon) |
| Driver | psycopg 3 |
| Server | gunicorn |
| Hosting | Render (recommended), Railway, or Fly.io |

## Shape

```
Browser  →  GET/POST /  →  Flask  →  Postgres (feedback_submissions)
Admin    →  Neon / SQL client (no web admin UI)
```

## Project layout

```
app.py              # Flask app factory + entrypoint
routes.py           # Single-page GET/POST handlers
db.py               # Connection + schema ensure + insert
templates/          # Jinja HTML
static/             # CSS
requirements.txt
Procfile            # gunicorn for PaaS
render.yaml         # optional Render blueprint
docs/               # product & ops docs
```

## Routes

| Method | Path | Purpose |
| --- | --- | --- |
| `GET` | `/` | Show empty form |
| `POST` | `/` | Validate, insert, show thank-you state |
| `GET` | `/again` | Redirect to fresh form |

## Design choices

- Server-rendered HTML only — no SPA
- Schema created automatically on startup (`CREATE TABLE IF NOT EXISTS`)
- Validation in the route layer (small app; no separate service layer yet)
- Secrets via environment variables (`DATABASE_URL`, `SECRET_KEY`)

## Non-goals

- Next.js / React admin
- Vercel as primary host (Python WSGI fits Render/Railway/Fly better)
- Multi-user auth
