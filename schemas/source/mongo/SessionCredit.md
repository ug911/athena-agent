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

## Usage (from backend-api)

_10 call site(s) found across `controllers/`, `services/`, `repositories/`, `workers/`, `helpers/`._

### Query methods

- `.updateOne` × 2
- `.aggregate` × 2
- `.updateMany` × 1
- `.deleteOne` × 1
- `.insertMany` × 1
- `.create` × 1
- `.deleteMany` × 1
- `.find` × 1

### Top call sites

- `src/controllers/InstituteController.js` × 3
- `src/services/sessionCreditService.js` × 3
- `src/workers/dataTransferWorker.js` × 2
- `src/services/DemoAccountService.js` × 1
- `src/services/classroomCleanupService.js` × 1

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
