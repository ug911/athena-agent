---
collection: "VideoKeyRecord"
model: "VideoKeyRecord"
source_file: "src/models/VideoKeyRecord.js"
field_count: 7
last_synced: "2026-04-28T10:58:23+00:00"
---

# `VideoKeyRecord` (Mongo collection)

- **Model**: `VideoKeyRecord`
- **Source**: [`src/models/VideoKeyRecord.js`](../../../src/models/VideoKeyRecord.js)
- **Athena counterpart**: try `processed.wise_app_backend__video_key_record` or `processed.wise_app_backend__videokeyrecord` — verify in `schemas/INDEX.md`.

## Indexes

- `[{ keyId: 1, entityId: 1 }, { unique: true }]`
- `[{ indexFile: 1 }]`
- `[{ classId: 1 }]`

## Local sub-schemas referenced

`VideoKeyRecordSchema`

## Fields

| Path | Type | Ref | Enum | Required | Default | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `keyId` | `String` |  |  | required |  |  |
| `entityId` | `ObjectId` |  |  | required |  |  |
| `classId` | `ObjectId` | `class` |  | required |  |  |
| `entityType` | `String` |  | SESSION, RESOURCE | required |  |  |
| `instituteId` | `ObjectId` | `Institute` |  | required |  |  |
| `namespace` | `String` |  |  | required |  |  |
| `indexFile` | `String` |  |  | required |  |  |

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
