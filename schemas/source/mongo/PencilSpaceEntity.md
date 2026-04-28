---
collection: "PencilSpaceEntity"
model: "PencilSpaceEntity"
source_file: "src/models/PencilSpaceEntity.js"
field_count: 2
last_synced: "2026-04-28T10:58:23+00:00"
---

# `PencilSpaceEntity` (Mongo collection)

- **Model**: `PencilSpaceEntity`
- **Source**: [`src/models/PencilSpaceEntity.js`](../../../src/models/PencilSpaceEntity.js)
- **Athena counterpart**: try `processed.wise_app_backend__pencil_space_entity` or `processed.wise_app_backend__pencilspaceentity` — verify in `schemas/INDEX.md`.

## Indexes

- `[{ wiseId: 1 }]`

## Local sub-schemas referenced

`pencilSpaceEntitySchema`

## Fields

| Path | Type | Ref | Enum | Required | Default | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `wiseId` | `ObjectId` |  |  | required |  |  |
| `pencilId` | `String` |  |  | required |  |  |

## Usage (from backend-api)

_7 call site(s) found across `controllers/`, `services/`, `repositories/`, `workers/`, `helpers/`._

### Query methods

- `.create` × 3
- `.find` × 2
- `.findOne` × 2

### Top call sites

- `src/services/PencilSpacesIntegrationService.js` × 6
- `src/services/meetingAttendanceService.js` × 1

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
