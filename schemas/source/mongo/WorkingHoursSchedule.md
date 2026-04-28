---
collection: "WorkingHoursSchedule"
model: "WorkingHoursSchedule"
source_file: "src/models/WorkingHoursSchedule.js"
field_count: 8
last_synced: "2026-04-28T10:58:23+00:00"
---

# `WorkingHoursSchedule` (Mongo collection)

- **Model**: `WorkingHoursSchedule`
- **Source**: [`src/models/WorkingHoursSchedule.js`](../../../src/models/WorkingHoursSchedule.js)
- **Athena counterpart**: try `processed.wise_app_backend__working_hours_schedule` or `processed.wise_app_backend__workinghoursschedule` — verify in `schemas/INDEX.md`.

## Indexes

- `[{ instituteId: 1, userId: 1, classId: 1 }, { unique: true }]`

## Local sub-schemas referenced

`slotSchema`, `workingHoursScheduleSchema`

## Fields

| Path | Type | Ref | Enum | Required | Default | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `instituteId` | `ObjectId` | `Institute` |  | required |  |  |
| `userId` | `ObjectId` | `user` |  |  |  |  |
| `classId` | `ObjectId` | `class` |  |  |  |  |
| `timezone` | `String` |  |  |  |  |  |
| `slots[]` | `<slotSchema>` |  |  |  |  |  |
| `slots[].startTime` | `String` |  |  | required |  |  |
| `slots[].endTime` | `String` |  |  | required |  |  |
| `slots[].day` | `String` |  | Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, S… | required |  |  |

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
