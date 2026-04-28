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

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
