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

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
