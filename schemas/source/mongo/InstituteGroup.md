---
collection: "InstituteGroup"
model: "InstituteGroup"
source_file: "src/models/InstituteGroup.js"
field_count: 3
last_synced: "2026-04-28T10:58:23+00:00"
---

# `InstituteGroup` (Mongo collection)

- **Model**: `InstituteGroup`
- **Source**: [`src/models/InstituteGroup.js`](../../../src/models/InstituteGroup.js)
- **Athena counterpart**: try `processed.wise_app_backend__institute_group` or `processed.wise_app_backend__institutegroup` — verify in `schemas/INDEX.md`.

## Indexes

- `[{ instituteId: 1 }]`

## Local sub-schemas referenced

`instituteGroupSchema`

## Fields

| Path | Type | Ref | Enum | Required | Default | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `name` | `String` |  |  | required |  |  |
| `instituteId` | `ObjectId` | `Institute` |  | required |  |  |
| `type` | `String` |  | <ALL_GROUP_TYPES> | required |  |  |

## Usage (from backend-api)

_10 call site(s) found across `controllers/`, `services/`, `repositories/`, `workers/`, `helpers/`._

### Query methods

- `.findOne` × 5
- `.create` × 1
- `.updateOne` × 1
- `.deleteOne` × 1
- `.find` × 1
- `.aggregate` × 1

### Top call sites

- `src/controllers/InstituteController.js` × 6
- `src/services/instituteGroupService.js` × 3
- `src/services/instituteAdmissionService.js` × 1

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
