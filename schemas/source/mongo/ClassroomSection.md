---
collection: "ClassroomSection"
model: "ClassroomSection"
source_file: "src/models/ClassroomSection.js"
field_count: 12
last_synced: "2026-04-28T10:58:23+00:00"
---

# `ClassroomSection` (Mongo collection)

- **Model**: `ClassroomSection`
- **Source**: [`src/models/ClassroomSection.js`](../../../src/models/ClassroomSection.js)
- **Athena counterpart**: try `processed.wise_app_backend__classroom_section` or `processed.wise_app_backend__classroomsection` — verify in `schemas/INDEX.md`.

## Indexes

- `[{ classId: 1 }]`

## Local sub-schemas referenced

`classroomSectionSchema`, `dripSettingSchema`, `entitySchema`

## Fields

| Path | Type | Ref | Enum | Required | Default | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `classId` | `ObjectId` | `class` |  | required |  |  |
| `name` | `String` |  |  | required |  |  |
| `sortKey` | `Number` |  |  | required |  |  |
| `entities[]` | `<entitySchema>` |  |  |  |  |  |
| `entities[].entityId` | `ObjectId` |  |  | required |  |  |
| `entities[].entityType` | `String` |  | <ALL_ENTITIES> | required |  |  |
| `entities[].public` | `Boolean` |  |  |  |  |  |
| `dripSettings` | `<dripSettingSchema>` |  |  |  |  |  |
| `dripSettings.enableDaysAfter` | `Number` |  |  |  |  |  |
| `dripSettings.enableOn` | `Date` |  |  |  |  |  |
| `sequentialLearning` | `Boolean` |  |  |  |  |  |
| `other` | `Boolean` |  |  |  |  |  |

## Usage (from backend-api)

_40 call site(s) found across `controllers/`, `services/`, `repositories/`, `workers/`, `helpers/`._

### Query methods

- `.find` × 8
- `.findOne` × 6
- `.create` × 5
- `.aggregate` × 5
- `.updateOne` × 4
- `.updateMany` × 3
- `.bulkWrite` × 3
- `.findOneAndUpdate` × 2
- `.insertMany` × 1
- `.deleteOne` × 1
- `.deleteMany` × 1
- `.countDocuments` × 1

### Populated fields (join hints)

Fields commonly hydrated via `.populate(...)` — in Athena, these are the joins worth pre-computing or caching.

- `classId` × 1

### Top call sites

- `src/services/classroomSectionService.js` × 21
- `src/services/classroomService.js` × 11
- `src/services/dataCheckService.js` × 2
- `src/services/DemoAccountService.js` × 1
- `src/services/entityWebhookService.js` × 1
- `src/services/classroomCleanupService.js` × 1
- `src/services/classroomAnalyticService.js` × 1
- `src/services/entityService.js` × 1

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
