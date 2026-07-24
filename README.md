# EOM Feedback

Next.js 15 app for collecting public feedback and reviewing submissions in an admin area.

## Stack

- Next.js 15 (App Router)
- TypeScript
- Tailwind CSS v4
- ESLint

## Getting started

```bash
npm install
cp .env.example .env.local
npm run dev
```

Open [http://localhost:3000](http://localhost:3000).

| Route | Purpose |
| --- | --- |
| `/` | Public feedback form |
| `/admin` | Admin overview |
| `/admin/responses` | Feedback responses list |
| `/api/feedback` | Feedback API (stubs) |

## Project structure

```
src/
  app/                 # App Router pages and API routes
  components/          # UI by domain (feedback, admin, layout, ui)
  hooks/               # Shared React hooks
  lib/                 # Utilities, constants, env helpers
  types/               # Shared TypeScript types
```

Business logic (validation, storage, auth) is intentionally not implemented yet.

## Scripts

```bash
npm run dev      # Development server (Turbopack)
npm run build    # Production build
npm run start    # Start production server
npm run lint     # ESLint
```

## Deploy on Vercel

1. Push this repository to GitHub (repo: `eom-feedback`).
2. Import the project in [Vercel](https://vercel.com/new).
3. Framework preset: **Next.js** (auto-detected).
4. Build command: `npm run build` · Output: default (`.next`).
5. Add environment variables from `.env.example` in the Vercel project settings when you introduce them.
6. Deploy.

No `vercel.json` is required for the default Next.js setup.
