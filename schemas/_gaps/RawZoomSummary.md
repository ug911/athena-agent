---
collection: "RawZoomSummary"
athena_table: "wise_app_backend__rawzoomsummary"
mongo_field_count: 6
athena_field_count: 21
matched: 6
coverage_pct: 100.0
last_diffed: "2026-04-28T11:07:30+00:00"
---

# Schema gap: `RawZoomSummary` ↔ `processed.wise_app_backend__rawzoomsummary`

- **Mongo source**: [`src/models/RawZoomSummary.js`](../source/mongo/RawZoomSummary.md)
- **Athena counterpart**: [`schemas/processed/processed/wise_app_backend__rawzoomsummary.md`](../processed/processed/wise_app_backend__rawzoomsummary.md)
- **Coverage**: 6/6 Mongo fields are present in Athena (**100.0%**).

## In Mongo, missing from Athena

_None — every Mongo field has a counterpart in Athena._

## In Athena, missing from Mongo

These fields exist in the Athena table but aren't declared in the current Mongoose schema. Likely renamed / deprecated, or added by the lake pipeline (timestamps, flattened helpers).

| Path | Type | Source |
| --- | --- | --- |
| `_id.$oid` | `string` | JSON path |
| `createdat.$date` | `object` | JSON path |
| `createdat.$date.$numberlong` | `string` | JSON path |
| `updatedat.$date` | `object` | JSON path |
| `updatedat.$date.$numberlong` | `string` | JSON path |
| `sessionid.$oid` | `string` | JSON path |
| `summaries.[]` | `object` | JSON path |
| `summaries.[]._id` | `object` | JSON path |
| `summaries.[]._id.$oid` | `string` | JSON path |
| `summaries.[].summarydetails.[].summarydetails[].label` | `string` | JSON path |
| `summaries.[].summarydetails.[].summarydetails[].summary` | `string` | JSON path |
