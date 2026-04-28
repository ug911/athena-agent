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

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
