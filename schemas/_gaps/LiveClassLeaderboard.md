---
collection: "LiveClassLeaderboard"
athena_table: "wise_app_backend__live_class_leaderboard"
mongo_field_count: 4
athena_field_count: 26
matched: 4
coverage_pct: 100.0
last_diffed: "2026-04-28T11:07:30+00:00"
---

# Schema gap: `LiveClassLeaderboard` ↔ `processed.wise_app_backend__live_class_leaderboard`

- **Mongo source**: [`src/models/LiveClassLeaderboard.js`](../source/mongo/LiveClassLeaderboard.md)
- **Athena counterpart**: [`schemas/processed/processed/wise_app_backend__live_class_leaderboard.md`](../processed/processed/wise_app_backend__live_class_leaderboard.md)
- **Coverage**: 4/4 Mongo fields are present in Athena (**100.0%**).

## In Mongo, missing from Athena

_None — every Mongo field has a counterpart in Athena._

## In Athena, missing from Mongo

These fields exist in the Athena table but aren't declared in the current Mongoose schema. Likely renamed / deprecated, or added by the lake pipeline (timestamps, flattened helpers).

| Path | Type | Source |
| --- | --- | --- |
| `_id.$oid` | `string` | JSON path |
| `insightid.$oid` | `string` | JSON path |
| `__v.$numberint` | `string` | JSON path |
| `createdat.$date` | `object` | JSON path |
| `createdat.$date.$numberlong` | `string` | JSON path |
| `pointstable.[]` | `object` | JSON path |
| `pointstable.[].pointsdistribution.attention` | `object` | JSON path |
| `pointstable.[].pointsdistribution.attention.$numberint` | `string` | JSON path |
| `pointstable.[].pointsdistribution.bonus` | `object` | JSON path |
| `pointstable.[].pointsdistribution.bonus.$numberint` | `string` | JSON path |
| `pointstable.[].pointsdistribution.poll` | `object` | JSON path |
| `pointstable.[].pointsdistribution.poll.$numberint` | `string` | JSON path |
| `pointstable.[].pointsdistribution.talktime` | `object` | JSON path |
| `pointstable.[].pointsdistribution.talktime.$numberint` | `string` | JSON path |
| `pointstable.[].pointsdistribution.video` | `object` | JSON path |
| `pointstable.[].pointsdistribution.video.$numberint` | `string` | JSON path |
| `updatedat.$date` | `object` | JSON path |
| `updatedat.$date.$numberlong` | `string` | JSON path |
