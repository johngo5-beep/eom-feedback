# EOM Feedback

Simple Flask app: one public form, submissions stored in Postgres. No admin UI — review rows in the database.

## Stack

- Flask + Jinja
- Postgres (Neon or any provider)
- gunicorn for production

## Local setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
```

Edit `.env`:

```env
DATABASE_URL=postgresql://...
SECRET_KEY=some-long-random-string
```

Run:

```bash
python app.py
```

Open http://127.0.0.1:5000

## Form fields

- Application Section (required)
- Comment (required)
- Your Position (optional)

## Admin

Query the table (newest first):

```sql
SELECT created_at, section, position, comment
FROM feedback_submissions
ORDER BY created_at DESC;
```

## Deploy

Do **not** use Vercel for this app. Use **Render**, Railway, or Fly.io.

See [docs/07_DEPLOYMENT.md](docs/07_DEPLOYMENT.md).

## Docs

| File | Topic |
| --- | --- |
| [docs/01_PRODUCT.md](docs/01_PRODUCT.md) | Product |
| [docs/02_ARCHITECTURE.md](docs/02_ARCHITECTURE.md) | Architecture |
| [docs/03_DATABASE.md](docs/03_DATABASE.md) | Database |
| [docs/04_UI.md](docs/04_UI.md) | UI |
| [docs/05_BACKLOG.md](docs/05_BACKLOG.md) | Backlog |
| [docs/06_API.md](docs/06_API.md) | HTTP endpoints |
| [docs/07_DEPLOYMENT.md](docs/07_DEPLOYMENT.md) | Hosting |
