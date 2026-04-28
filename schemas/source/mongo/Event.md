---
collection: "Event"
model: "event"
source_file: "src/models/DBEvent.js"
field_count: 5
last_synced: "2026-04-28T10:58:23+00:00"
---

# `Event` (Mongo collection)

- **Model**: `event`
- **Source**: [`src/models/DBEvent.js`](../../../src/models/DBEvent.js)
- **Athena counterpart**: try `processed.wise_app_backend__event` — verify in `schemas/INDEX.md`.

## Indexes

- `[{ expiresAt: 1 }, { expireAfterSeconds: 0 }]`
- `[{ eventId: 1 }, { unique: true }]`
- `[{ 'payload.user.id': 1 }]`

## Local sub-schemas referenced

`eventSchema`

## Fields

| Path | Type | Ref | Enum | Required | Default | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `eventId` | `String` |  |  | required, unique |  |  |
| `eventName` | `String` |  |  | required |  |  |
| `eventTimestamp` | `Date` |  |  |  | Date.now |  |
| `expiresAt` | `Date` |  |  |  | () => moment().add(180, 'day').toDate() |  |
| `payload` | `Object` |  |  |  |  |  |

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
