# Product

## Name

EOM Feedback

## Vision

A lightweight internal web app where EOM users submit feedback in one place — instead of scattering it across chats, email, and personal messages.

Fast, minimal, no training required.

## Goal

- Collect structured feedback
- Store every submission permanently in one database table
- Let the administrator review submissions directly in the database
- Keep the product to a single public page

## Users

Internal employees who use the EOM application.

## User flow

1. Open the app
2. Fill the feedback form
3. Submit
4. Row is saved in Postgres
5. See confirmation
6. Optionally submit again via **Write one more feedback**

## Feedback page (only page)

### Fields

| Field | Type | Required | Notes |
| --- | --- | --- | --- |
| Application Section | Dropdown | Yes | General, Entities, Matrices, Forecast, Integration to Core system |
| Comment | Textarea | Yes | Free text |
| Your Position | Text | No | Any value (e.g. Category Manager, Purchaser) |

### Submit

Button label: **Submit**

### After success

- Form fields become read-only
- Message: **Thank you for your feedback!**
- Button: **Write one more feedback** (clears form and returns to a fresh submit state)

## Storage

Each row stores:

- submission date/time
- application section
- comment
- user position (nullable)

## Administration

There is **no admin web page**.

The sole administrator reviews feedback in the database table `feedback_submissions` (Neon console, TablePlus, `psql`, etc.), newest first via `created_at`.

## Non-functional

- Simple, lightweight, responsive, fast
- Easy to host on a small Python platform (Render, Railway, Fly.io, …)

## Out of scope (for now)

- Admin UI / login
- Search, filters, export
- Status workflow, email notifications, analytics
