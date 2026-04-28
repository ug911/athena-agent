---
collection: "ClassroomPublicProfile"
model: "ClassroomPublicProfile"
source_file: "src/models/ClassroomPublicProfile.js"
field_count: 9
last_synced: "2026-04-28T10:58:23+00:00"
---

# `ClassroomPublicProfile` (Mongo collection)

- **Model**: `ClassroomPublicProfile`
- **Source**: [`src/models/ClassroomPublicProfile.js`](../../../src/models/ClassroomPublicProfile.js)
- **Athena counterpart**: try `processed.wise_app_backend__classroom_public_profile` or `processed.wise_app_backend__classroompublicprofile` — verify in `schemas/INDEX.md`.

## Indexes

- `[{ classId: 1 }, { unique: true }]`
- `[{ instituteId: 1 }]`

## Local sub-schemas referenced

`ClassroomPublicProfileSchema`, `highlightsSchema`

## Fields

| Path | Type | Ref | Enum | Required | Default | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `classId` | `ObjectId` | `class` |  | required |  |  |
| `title` | `String` |  |  |  |  |  |
| `subTitle` | `String` |  |  |  |  |  |
| `description` | `String` |  |  |  |  |  |
| `highlights` | `<highlightsSchema>` |  |  |  |  |  |
| `highlights.title` | `String` |  |  |  |  |  |
| `highlights.points` | `Array<String>` |  |  |  |  |  |
| `public` | `Boolean` |  |  |  | true |  |
| `reviews` | `Array<reviewSchema>` |  |  |  |  |  |

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
