---
collection: "InstituteTags"
model: "InstituteTags"
source_file: "src/models/InstituteTags.js"
field_count: 2
last_synced: "2026-04-28T10:58:23+00:00"
---

# `InstituteTags` (Mongo collection)

- **Model**: `InstituteTags`
- **Source**: [`src/models/InstituteTags.js`](../../../src/models/InstituteTags.js)
- **Athena counterpart**: try `processed.wise_app_backend__institute_tags` or `processed.wise_app_backend__institutetags` — verify in `schemas/INDEX.md`.

## Indexes

- `[{ instituteId: 1 }, { unique: true }]`

## Local sub-schemas referenced

`instituteTagsSchema`

## Fields

| Path | Type | Ref | Enum | Required | Default | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `instituteId` | `ObjectId` | `Institute` |  | required |  |  |
| `tags` | `Array<String>` |  |  |  |  |  |

## Usage (from backend-api)

_5 call site(s) found across `controllers/`, `services/`, `repositories/`, `workers/`, `helpers/`._

### Query methods

- `.findOne` × 2
- `.updateOne` × 2
- `.findOneAndUpdate` × 1

### Top call sites

- `src/controllers/InstituteController.js` × 3
- `src/services/instituteService.js` × 2

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
