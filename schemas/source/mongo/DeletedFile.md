---
collection: "DeletedFile"
model: "DeletedFile"
source_file: "src/models/DeletedFile.js"
field_count: 10
last_synced: "2026-04-28T10:58:23+00:00"
---

# `DeletedFile` (Mongo collection)

- **Model**: `DeletedFile`
- **Source**: [`src/models/DeletedFile.js`](../../../src/models/DeletedFile.js)
- **Athena counterpart**: try `processed.wise_app_backend__deleted_file` or `processed.wise_app_backend__deletedfile` — verify in `schemas/INDEX.md`.

## Indexes

- `[{ createdAt: 1 }]`
- `[{ deletedAt: 1 }, { expireAfterSeconds: 2592000 }]`

## Local sub-schemas referenced

`deletedFileSchema`

## Fields

| Path | Type | Ref | Enum | Required | Default | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `entityType` | `String` |  | RESOURCE, SESSION, DISCUSSION, ASSESSMENT, TEST, CONTRACT | required |  |  |
| `file` | `attachmentSchema` |  |  |  |  |  |
| `deletedFromS3` | `Boolean` |  |  |  | false |  |
| `failed` | `Boolean` |  |  |  |  |  |
| `error` | `String` |  |  |  |  |  |
| `skippedDeletion` | `Boolean` |  |  |  |  |  |
| `classId` | `ObjectId` | `class` |  |  |  |  |
| `entityId` | `ObjectId` |  |  |  |  |  |
| `deletedAt` | `Date` |  |  |  |  |  |
| `skipValidation` | `Boolean` |  |  |  |  |  |

## Usage (from backend-api)

_5 call site(s) found across `controllers/`, `services/`, `repositories/`, `workers/`, `helpers/`._

### Query methods

- `.updateOne` × 3
- `.find` × 1
- `.insertMany` × 1

### Top call sites

- `src/services/fileDeletionService.js` × 2
- `src/workers/fileDeletionWorker.js` × 2
- `src/services/s3UploadService.js` × 1

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
