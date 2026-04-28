---
collection: "RawZoomSummary"
model: "RawZoomSummary"
source_file: "src/models/RawZoomSummary.js"
field_count: 6
last_synced: "2026-04-28T10:58:23+00:00"
---

# `RawZoomSummary` (Mongo collection)

- **Model**: `RawZoomSummary`
- **Source**: [`src/models/RawZoomSummary.js`](../../../src/models/RawZoomSummary.js)
- **Athena counterpart**: try `processed.wise_app_backend__raw_zoom_summary` or `processed.wise_app_backend__rawzoomsummary` — verify in `schemas/INDEX.md`.

## Indexes

- `[{ sessionId: 1 }, { unique: true }]`

## Local sub-schemas referenced

`rawZoomSummarySchema`, `summarySchema`

## Fields

| Path | Type | Ref | Enum | Required | Default | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `sessionId` | `ObjectId` | `zoom` |  | required |  |  |
| `summaries[]` | `<summarySchema>` |  |  |  |  |  |
| `summaries[].summaryTitle` | `String` |  |  |  |  |  |
| `summaries[].summaryOverview` | `String` |  |  |  |  |  |
| `summaries[].summaryDetails` | `Array` |  |  |  |  |  |
| `summaries[].meetingUUID` | `String` |  |  |  |  |  |

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
