---
collection: "LensEvent"
athena_table: "wise_app_backend__lens_event"
mongo_field_count: 4
athena_field_count: 21
matched: 4
coverage_pct: 100.0
last_diffed: "2026-04-28T11:07:30+00:00"
---

# Schema gap: `LensEvent` ↔ `processed.wise_app_backend__lens_event`

- **Mongo source**: [`src/models/LensEvent.js`](../source/mongo/LensEvent.md)
- **Athena counterpart**: [`schemas/processed/processed/wise_app_backend__lens_event.md`](../processed/processed/wise_app_backend__lens_event.md)
- **Coverage**: 4/4 Mongo fields are present in Athena (**100.0%**).

## In Mongo, missing from Athena

_None — every Mongo field has a counterpart in Athena._

## In Athena, missing from Mongo

These fields exist in the Athena table but aren't declared in the current Mongoose schema. Likely renamed / deprecated, or added by the lake pipeline (timestamps, flattened helpers).

| Path | Type | Source |
| --- | --- | --- |
| `_id.$oid` | `string` | JSON path |
| `insightid.$oid` | `string` | JSON path |
| `eventpayload.category` | `string` | JSON path |
| `eventpayload.criteria` | `string` | JSON path |
| `eventpayload.points` | `object` | JSON path |
| `eventpayload.points.$numberint` | `string` | JSON path |
| `eventpayload.pollid` | `string` | JSON path |
| `createdat.$date` | `object` | JSON path |
| `createdat.$date.$numberlong` | `string` | JSON path |
| `updatedat.$date` | `object` | JSON path |
| `updatedat.$date.$numberlong` | `string` | JSON path |
| `__v.$numberint` | `string` | JSON path |
