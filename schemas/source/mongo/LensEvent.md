---
collection: "LensEvent"
model: "LensEvent"
source_file: "src/models/LensEvent.js"
field_count: 4
last_synced: "2026-04-28T10:58:23+00:00"
---

# `LensEvent` (Mongo collection)

- **Model**: `LensEvent`
- **Source**: [`src/models/LensEvent.js`](../../../src/models/LensEvent.js)
- **Athena counterpart**: try `processed.wise_app_backend__lens_event` or `processed.wise_app_backend__lensevent` — verify in `schemas/INDEX.md`.

## Indexes

- `[{ insightId: 1 }]`

## Local sub-schemas referenced

`LensEventSchema`

## Fields

| Path | Type | Ref | Enum | Required | Default | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `insightId` | `ObjectId` | `LiveClassInsight` |  | required |  |  |
| `eventName` | `String` |  |  | required |  |  |
| `userId` | `String` |  |  | required |  |  |
| `eventPayload` | `Object` |  |  |  |  |  |

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
