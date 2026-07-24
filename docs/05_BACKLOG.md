# Backlog

## Done

- [x] Flask single-page feedback form
- [x] Postgres persistence
- [x] Success / write-another flow
- [x] Drop Next.js / Vercel-oriented stack
- [x] Docs for product, architecture, DB, hosting

## Now

- [ ] Create Neon (or other) database
- [ ] Set local `.env`
- [ ] Deploy to Render (or Railway / Fly)
- [ ] Confirm rows appear in DB after a test submit

## Later (optional)

- [ ] Very light password-protected read-only list page
- [ ] CSV export
- [ ] Rate limiting / spam protection
- [ ] Email notify on new feedback
- [ ] Status field (`new` / `reviewed`)

## Decision log

| Date | Decision |
| --- | --- |
| 2026-07-24 | Start on Next.js + admin UI |
| 2026-07-24 | Rebuild on Flask; admin = DB table only; host outside Vercel |
