---
collection: "TempData"
model: "TempData"
source_file: "src/models/TempData.js"
field_count: 6
last_synced: "2026-04-28T10:58:23+00:00"
---

# `TempData` (Mongo collection)

- **Model**: `TempData`
- **Source**: [`src/models/TempData.js`](../../../src/models/TempData.js)
- **Athena counterpart**: try `processed.wise_app_backend__temp_data` or `processed.wise_app_backend__tempdata` — verify in `schemas/INDEX.md`.

## Indexes

- `[{ userId: 1 }]`
- `[{ createdAt: 1 }, { expireAfterSeconds: 1296000 }]`

## Local sub-schemas referenced

`tempDataSchema`

## Fields

| Path | Type | Ref | Enum | Required | Default | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `instituteId` | `ObjectId` | `Institute` |  |  |  |  |
| `userId` | `ObjectId` | `user` |  |  |  |  |
| `classId` | `ObjectId` | `class` |  |  |  |  |
| `type` | `String` |  | CLASSROOM_CREATION, COUPON_DISCOUNT | required |  |  |
| `data` | `Object` |  |  |  | {} |  |
| `processed` | `Boolean` |  |  |  |  |  |

## Usage (from backend-api)

_6 call site(s) found across `controllers/`, `services/`, `repositories/`, `workers/`, `helpers/`._

### Query methods

- `.findOne` × 2
- `.updateOne` × 2
- `.create` × 2

### Top call sites

- `src/services/feeService.js` × 4
- `src/services/instituteAdmissionService.js` × 2

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
