---
collection: "GoogleCalendarEvent"
model: "GoogleCalendarEvent"
source_file: "src/models/GoogleCalendarEvent.js"
field_count: 8
last_synced: "2026-04-28T10:58:23+00:00"
---

# `GoogleCalendarEvent` (Mongo collection)

- **Model**: `GoogleCalendarEvent`
- **Source**: [`src/models/GoogleCalendarEvent.js`](../../../src/models/GoogleCalendarEvent.js)
- **Athena counterpart**: try `processed.wise_app_backend__google_calendar_event` or `processed.wise_app_backend__googlecalendarevent` — verify in `schemas/INDEX.md`.

## Indexes

- `[{ googleEventId: 1, userId: 1 }, { unique: true }]`
- `[{ startTime: 1 }, { expireAfterSeconds: 2592000 }]`

## Local sub-schemas referenced

`calendarEventSchema`

## Fields

| Path | Type | Ref | Enum | Required | Default | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `userId` | `ObjectId` | `user` |  | required |  |  |
| `startTime` | `Date` |  |  | required |  |  |
| `endTime` | `Date` |  |  | required |  |  |
| `title` | `String` |  |  | required |  |  |
| `description` | `String` |  |  |  |  |  |
| `googleEventId` | `String` |  |  | required |  |  |
| `linkedGoogleCalendarId` | `ObjectId` | `LinkedGoogleCalendar` |  |  |  |  |
| `sessionId` | `ObjectId` | `zoom` |  |  |  |  |

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
