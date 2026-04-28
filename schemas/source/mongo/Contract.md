---
collection: "Contract"
model: "Contract"
source_file: "src/models/Contract.js"
field_count: 5
last_synced: "2026-04-28T10:58:23+00:00"
---

# `Contract` (Mongo collection)

- **Model**: `Contract`
- **Source**: [`src/models/Contract.js`](../../../src/models/Contract.js)
- **Athena counterpart**: try `processed.wise_app_backend__contract` — verify in `schemas/INDEX.md`.

## Indexes

- `[{ instituteId: 1 }, { unique: true }]`

## Local sub-schemas referenced

`contractSchema`

## Fields

| Path | Type | Ref | Enum | Required | Default | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `instituteId` | `ObjectId` | `Institute` |  | required |  |  |
| `title` | `String` |  |  | required |  |  |
| `contractFile` | `attachmentSchema` |  |  | required |  |  |
| `mandatory` | `Boolean` |  |  |  | true |  |
| `questions` | `Array<registrationFormQuestionSchema>` |  |  |  |  |  |

## Usage (from backend-api)

_11 call site(s) found across `controllers/`, `services/`, `repositories/`, `workers/`, `helpers/`._

### Query methods

- `.findOne` × 5
- `.find` × 3
- `.create` × 1
- `.findOneAndUpdate` × 1
- `.deleteOne` × 1

### Top call sites

- `src/services/contractService.js` × 6
- `src/controllers/InstituteController.js` × 2
- `src/controllers/StudentController.js` × 1
- `src/services/instituteService.js` × 1
- `src/services/instituteAnalyticsService.js` × 1

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
