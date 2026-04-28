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

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
