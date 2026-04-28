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

## Usage (from backend-api)

_21 call site(s) found across `controllers/`, `services/`, `repositories/`, `workers/`, `helpers/`._

### Query methods

- `.findOne` × 7
- `.find` × 7
- `.updateOne` × 3
- `.aggregate` × 1
- `.create` × 1
- `.deleteOne` × 1
- `.deleteMany` × 1

### Top call sites

- `src/controllers/UserController.js` × 8
- `src/services/GoogleCalendarIntegrationService.js` × 6
- `src/workers/genericAsyncJobWorker.js` × 4
- `src/controllers/GoogleCalendarWebhookController.js` × 1
- `src/services/instituteAnalyticsService.js` × 1
- `src/workers/dataTransferWorker.js` × 1

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
