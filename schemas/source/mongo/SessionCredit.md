---
collection: "SessionCredit"
model: "SessionCredit"
source_file: "src/models/SessionCredit.js"
field_count: 8
last_synced: "2026-04-28T10:58:23+00:00"
---

# `SessionCredit` (Mongo collection)

- **Model**: `SessionCredit`
- **Source**: [`src/models/SessionCredit.js`](../../../src/models/SessionCredit.js)
- **Athena counterpart**: try `processed.wise_app_backend__session_credit` or `processed.wise_app_backend__sessioncredit` — verify in `schemas/INDEX.md`.

## Indexes

- `[{ userId: 1, classId: 1, instituteId: 1 }]`

## Local sub-schemas referenced

`sessionCreditsSchema`

## Fields

| Path | Type | Ref | Enum | Required | Default | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `classId` | `ObjectId` | `class` |  |  |  |  |
| `userId` | `ObjectId` | `user` |  | required |  |  |
| `instituteId` | `ObjectId` | `Institute` |  |  |  |  |
| `assignedBy` | `ObjectId` | `user` |  | required |  |  |
| `credit` | `Number` |  |  | required |  |  |
| `note` | `String` |  |  |  |  |  |
| `type` | `String` |  | TYPE_CREDIT, TYPE_DEBIT |  | TYPE_CREDIT |  |
| `metadata` | `<inline-schema>` |  |  |  |  |  |

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
