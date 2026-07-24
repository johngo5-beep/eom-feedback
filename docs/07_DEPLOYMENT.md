# Deployment

Vercel is a poor fit for a small Flask (WSGI) app. Prefer a Python-friendly host.

## Recommended: Render

1. Push this repo to GitHub.
2. Create a free Postgres database (Neon is fine, or Render Postgres).
3. In [Render](https://render.com) → **New → Web Service** → connect the repo.
4. Settings:
   - **Runtime:** Python
   - **Build:** `pip install -r requirements.txt`
   - **Start:** `gunicorn app:app --bind 0.0.0.0:$PORT`
5. Environment variables:
   - `DATABASE_URL` — your Postgres URL
   - `SECRET_KEY` — long random string (or let Render generate one)
6. Deploy. Open the public URL and submit a test feedback.
7. In Neon (or your SQL client), run:

```sql
SELECT * FROM feedback_submissions ORDER BY created_at DESC;
```

Optional: `render.yaml` in the repo can be used as a Blueprint.

## Alternatives

| Platform | Notes |
| --- | --- |
| **Railway** | Connect repo, add Postgres plugin or external Neon URL, start with gunicorn |
| **Fly.io** | `fly launch`, set secrets, scale a small machine |
| **PythonAnywhere** | Simple for beginners; less “git push” oriented |
| **VPS** (Hetzner, etc.) | nginx + gunicorn + systemd — more control, more ops |

## Local run

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# edit .env with DATABASE_URL and SECRET_KEY
python app.py
```

Open http://127.0.0.1:5000

## Checklist

- [ ] `DATABASE_URL` set in host
- [ ] `SECRET_KEY` set in host
- [ ] First deploy creates `feedback_submissions`
- [ ] Test submit from the live URL
- [ ] Row visible in DB
