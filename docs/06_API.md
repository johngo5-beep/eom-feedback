# API

This app is **form-first**, not a JSON API.

## HTTP endpoints

### `GET /`

Renders the feedback page (empty form).

### `POST /`

`Content-Type: application/x-www-form-urlencoded`

| Field | Required |
| --- | --- |
| `section` | Yes — one of the allowed dropdown values |
| `comment` | Yes |
| `position` | No |

**Success:** HTML page with thank-you state (HTTP 200).  
**Validation failure:** HTML page with flash errors (HTTP 400).  
**Server/DB failure:** HTML page with error flash (HTTP 500).

### `GET /again`

Redirects to `GET /` for a fresh form.

## Why no JSON API

MVP needs one browser form. Add JSON endpoints later only if another system must submit feedback programmatically.
