---
collection: "study materials"
model: "studyMaterials"
source_file: "src/models/Resource.js"
field_count: 25
last_synced: "2026-04-28T10:58:23+00:00"
---

# `study materials` (Mongo collection)

- **Model**: `studyMaterials`
- **Source**: [`src/models/Resource.js`](../../../src/models/Resource.js)
- **Athena counterpart**: try `processed.wise_app_backend__study materials` — verify in `schemas/INDEX.md`.

## Local sub-schemas referenced

`resourcesSchema`, `studyMaterialsSchema`

## Fields

| Path | Type | Ref | Enum | Required | Default | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `name` | `String` |  |  | required |  |  |
| `type` | `String` |  | video, file, folder, embedded | required |  |  |
| `resources[]` | `<resourcesSchema>` |  |  |  | undefined |  |
| `resources[].name` | `String` |  |  | required |  |  |
| `resources[].description` | `String` |  |  |  |  |  |
| `resources[].type` | `String` |  | file, video | required |  |  |
| `resources[].subtype` | `String` |  |  |  |  |  |
| `resources[].youtubeURL` | `String` |  |  |  |  |  |
| `resources[].link` | `String` |  |  |  |  |  |
| `resources[].file` | `attachmentSchema` |  |  |  |  |  |
| `resources[].createdAt` | `Date` |  |  |  | Date.now |  |
| `resources[].metadata` | `Object` |  |  |  |  |  |
| `link` | `String` |  |  |  |  |  |
| `subtype` | `String` |  | youtube, hls_video, h5p, link |  |  |  |
| `file` | `attachmentSchema` |  |  |  |  |  |
| `description` | `String` |  |  |  |  |  |
| `youtubeURL` | `String` |  |  |  |  |  |
| `userId` | `ObjectId` | `user` |  | required |  |  |
| `classId` | `ObjectId` | `class` |  |  |  |  |
| `lastCommentedAt` | `Date` |  |  |  |  |  |
| `disableCommenting` | `Boolean` |  |  |  | false |  |
| `comments` | `Array<commentsSchema>` |  |  |  |  |  |
| `public` | `Boolean` |  |  |  |  |  |
| `thumbnail` | `String` |  |  |  |  |  |
| `metadata` | `Object` |  |  |  |  |  |

## Usage (from backend-api)

_34 call site(s) found across `controllers/`, `services/`, `repositories/`, `workers/`, `helpers/`._

### Query methods

- `.findOne` × 8
- `.aggregate` × 7
- `.updateOne` × 6
- `.find` × 6
- `.deleteMany` × 2
- `.insertMany` × 2
- `.create` × 1
- `.findOneAndUpdate` × 1
- `.updateMany` × 1

### Populated fields (join hints)

Fields commonly hydrated via `.populate(...)` — in Athena, these are the joins worth pre-computing or caching.

- `userId` × 1

### Top call sites

- `src/services/resourceLibraryService.js` × 10
- `src/workers/dataTransferWorker.js` × 6
- `src/controllers/ResourceController.js` × 5
- `src/services/classroomService.js` × 3
- `src/workers/videoConversionWorker.js` × 2
- `src/controllers/UserController.js` × 1
- `src/services/classroomSectionService.js` × 1
- `src/services/classroomCleanupService.js` × 1

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
