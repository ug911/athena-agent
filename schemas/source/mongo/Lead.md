---
collection: "Lead"
model: "Lead"
source_file: "src/models/Lead.js"
field_count: 5
last_synced: "2026-04-28T10:58:23+00:00"
---

# `Lead` (Mongo collection)

- **Model**: `Lead`
- **Source**: [`src/models/Lead.js`](../../../src/models/Lead.js)
- **Athena counterpart**: try `processed.wise_app_backend__lead` — verify in `schemas/INDEX.md`.

## Indexes

- `[{ registrationToken: 1 }]`
- `[{ classId: 1, email: 1 }, { unique: 1 }]`
- `[{ classId: 1, registrationToken: 1 }, { unique: 1 }]`

## Local sub-schemas referenced

`LeadSchema`

## Fields

| Path | Type | Ref | Enum | Required | Default | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `classId` | `ObjectId` | `classes` |  | required |  |  |
| `name` | `String` |  |  | required |  |  |
| `email` | `String` |  |  | required |  |  |
| `phoneNumber` | `String` |  |  | required |  |  |
| `registrationToken` | `String` |  |  | required | () => Math.random().toString(36).slic… |  |

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
