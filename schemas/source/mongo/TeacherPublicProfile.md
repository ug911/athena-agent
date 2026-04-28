---
collection: "TeacherPublicProfile"
model: "TeacherPublicProfile"
source_file: "src/models/TeacherPublicProfile.js"
field_count: 9
last_synced: "2026-04-28T10:58:23+00:00"
---

# `TeacherPublicProfile` (Mongo collection)

- **Model**: `TeacherPublicProfile`
- **Source**: [`src/models/TeacherPublicProfile.js`](../../../src/models/TeacherPublicProfile.js)
- **Athena counterpart**: try `processed.wise_app_backend__teacher_public_profile` or `processed.wise_app_backend__teacherpublicprofile` — verify in `schemas/INDEX.md`.

## Indexes

- `[{ userId: 1, instituteId: 1 }, { unique: true }]`

## Local sub-schemas referenced

`teacherPublicProfileSchema`

## Fields

| Path | Type | Ref | Enum | Required | Default | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `userId` | `ObjectId` | `user` |  | required |  |  |
| `instituteId` | `ObjectId` | `institute` |  | required |  |  |
| `description` | `String` |  |  |  |  |  |
| `teacherCovers` | `Array<coverSchema>` |  |  |  |  |  |
| `tagline` | `String` |  |  |  |  |  |
| `reviews` | `Array<reviewSchema>` |  |  |  |  |  |
| `displayTags` | `Array<String>` |  |  |  |  |  |
| `videoLink` | `String` |  |  |  |  |  |
| `rating` | `Number` |  |  |  |  |  |

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
