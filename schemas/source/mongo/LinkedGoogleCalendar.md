---
collection: "LinkedGoogleCalendar"
model: "LinkedGoogleCalendar"
source_file: "src/models/LinkedGoogleCalendar.js"
field_count: 10
last_synced: "2026-04-28T10:58:23+00:00"
---

# `LinkedGoogleCalendar` (Mongo collection)

- **Model**: `LinkedGoogleCalendar`
- **Source**: [`src/models/LinkedGoogleCalendar.js`](../../../src/models/LinkedGoogleCalendar.js)
- **Athena counterpart**: try `processed.wise_app_backend__linked_google_calendar` or `processed.wise_app_backend__linkedgooglecalendar` — verify in `schemas/INDEX.md`.

## Indexes

- `[{ email: 1, calendarId: 1 }]`

## Local sub-schemas referenced

`linkedGoogleCalendarSchema`

## Fields

| Path | Type | Ref | Enum | Required | Default | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `userId` | `ObjectId` | `user` |  | required |  |  |
| `calendarId` | `String` |  |  | required |  |  |
| `channelId` | `String` |  |  |  |  |  |
| `resourceId` | `String` |  |  |  |  |  |
| `email` | `String` |  |  | required |  |  |
| `refreshToken` | `String` |  |  | required |  |  |
| `displayName` | `String` |  |  |  |  |  |
| `accessRole` | `String` |  |  |  |  |  |
| `lastSyncAt` | `Date` |  |  |  |  |  |
| `write` | `Boolean` |  |  |  |  |  |

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
