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

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
