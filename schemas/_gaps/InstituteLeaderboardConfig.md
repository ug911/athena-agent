---
collection: "InstituteLeaderboardConfig"
athena_table: "wise_app_backend__institute_leaderboard_config"
mongo_field_count: 9
athena_field_count: 25
matched: 9
coverage_pct: 100.0
last_diffed: "2026-04-28T11:07:30+00:00"
---

# Schema gap: `InstituteLeaderboardConfig` ↔ `processed.wise_app_backend__institute_leaderboard_config`

- **Mongo source**: [`src/models/InstituteLeaderboardConfig.js`](../source/mongo/InstituteLeaderboardConfig.md)
- **Athena counterpart**: [`schemas/processed/processed/wise_app_backend__institute_leaderboard_config.md`](../processed/processed/wise_app_backend__institute_leaderboard_config.md)
- **Coverage**: 9/9 Mongo fields are present in Athena (**100.0%**).

## In Mongo, missing from Athena

_None — every Mongo field has a counterpart in Athena._

## In Athena, missing from Mongo

These fields exist in the Athena table but aren't declared in the current Mongoose schema. Likely renamed / deprecated, or added by the lake pipeline (timestamps, flattened helpers).

| Path | Type | Source |
| --- | --- | --- |
| `_id.$oid` | `string` | JSON path |
| `instituteid.$oid` | `string` | JSON path |
| `__v.$numberint` | `string` | JSON path |
| `createdat.$date` | `object` | JSON path |
| `createdat.$date.$numberlong` | `string` | JSON path |
| `levels.[]` | `object` | JSON path |
| `levels.[].index.$numberint` | `string` | JSON path |
| `levels.[].thresholdpoints.$numberint` | `string` | JSON path |
| `pointconfigurations.[]` | `object` | JSON path |
| `pointconfigurations.[].points.$numberint` | `string` | JSON path |
| `updatedat.$date` | `object` | JSON path |
| `updatedat.$date.$numberlong` | `string` | JSON path |
