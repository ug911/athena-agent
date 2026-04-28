---
collection: "EmailSupression"
model: "EmailSupression"
source_file: "src/models/EmailSupression.js"
field_count: 3
last_synced: "2026-04-28T10:58:23+00:00"
---

# `EmailSupression` (Mongo collection)

- **Model**: `EmailSupression`
- **Source**: [`src/models/EmailSupression.js`](../../../src/models/EmailSupression.js)
- **Athena counterpart**: try `processed.wise_app_backend__email_supression` or `processed.wise_app_backend__emailsupression` — verify in `schemas/INDEX.md`.

## Indexes

- `[{ email: 1 }, { unique: true }]`

## Local sub-schemas referenced

`emailSupressionSchema`

## Fields

| Path | Type | Ref | Enum | Required | Default | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `email` | `String` |  |  | required |  |  |
| `reason` | `String` |  | INVALID, BOUNCE | required |  |  |
| `metadata` | `Object` |  |  |  |  |  |

## Usage (from backend-api)

_6 call site(s) found across `controllers/`, `services/`, `repositories/`, `workers/`, `helpers/`._

### Query methods

- `.updateOne` × 2
- `.exists` × 2
- `.deleteOne` × 1
- `.find` × 1

### Top call sites

- `src/services/communications/emailService.js` × 2
- `src/controllers/AWSWebhookController.js` × 1
- `src/controllers/DevAPIController.js` × 1
- `src/controllers/InstituteController.js` × 1
- `src/services/communications/notificationService.js` × 1

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
