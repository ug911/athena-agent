---
collection: "TeacherLeave"
model: "TeacherLeave"
source_file: "src/models/TeacherLeave.js"
field_count: 6
last_synced: "2026-04-28T10:58:23+00:00"
---

# `TeacherLeave` (Mongo collection)

- **Model**: `TeacherLeave`
- **Source**: [`src/models/TeacherLeave.js`](../../../src/models/TeacherLeave.js)
- **Athena counterpart**: try `processed.wise_app_backend__teacher_leave` or `processed.wise_app_backend__teacherleave` — verify in `schemas/INDEX.md`.

## Indexes

- `[{ userId: 1 }]`
- `[{ instituteId: 1 }]`

## Local sub-schemas referenced

`teacherLeaveSchema`

## Fields

| Path | Type | Ref | Enum | Required | Default | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `instituteId` | `ObjectId` | `Institute` |  | required |  |  |
| `userId` | `ObjectId` | `user` |  |  |  |  |
| `type` | `String` |  | HALF, FULL | required |  |  |
| `startTime` | `Date` |  |  | required |  |  |
| `endTime` | `Date` |  |  | required |  |  |
| `reason` | `String` |  |  |  |  |  |

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
