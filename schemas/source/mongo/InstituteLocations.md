---
collection: "InstituteLocations"
model: "InstituteLocations"
source_file: "src/models/InstituteLocations.js"
field_count: 2
last_synced: "2026-04-28T10:58:23+00:00"
---

# `InstituteLocations` (Mongo collection)

- **Model**: `InstituteLocations`
- **Source**: [`src/models/InstituteLocations.js`](../../../src/models/InstituteLocations.js)
- **Athena counterpart**: try `processed.wise_app_backend__institute_locations` or `processed.wise_app_backend__institutelocations` — verify in `schemas/INDEX.md`.

## Indexes

- `[{ instituteId: 1 }, { unique: true }]`

## Local sub-schemas referenced

`instituteLocationsSchema`

## Fields

| Path | Type | Ref | Enum | Required | Default | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `instituteId` | `ObjectId` | `Institute` |  | required |  |  |
| `locations` | `Array<String>` |  |  |  |  |  |

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
