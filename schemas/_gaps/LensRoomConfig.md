---
collection: "LensRoomConfig"
athena_table: "wise_app_backend__lens_room_config"
mongo_field_count: 19
athena_field_count: 55
matched: 19
coverage_pct: 100.0
last_diffed: "2026-09-08T08:05:41+00:00"
---

# Schema gap: `LensRoomConfig` ↔ `processed.wise_app_backend__lens_room_config`

- **Mongo source**: [`src/models/LensRoomConfig.js`](../source/mongo/LensRoomConfig.md)
- **Athena counterpart**: [`schemas/processed/processed/wise_app_backend__lens_room_config.md`](../processed/processed/wise_app_backend__lens_room_config.md)
- **Coverage**: 19/19 Mongo fields are present in Athena (**100.0%**).

## In Mongo, missing from Athena

_None — every Mongo field has a counterpart in Athena._

## In Athena, missing from Mongo

These fields exist in the Athena table but aren't declared in the current Mongoose schema. Likely renamed / deprecated, or added by the lake pipeline (timestamps, flattened helpers).

| Path | Type | Source |
| --- | --- | --- |
| `_id.$oid` | `string` | JSON path |
| `classid.$oid` | `string` | JSON path |
| `__v.$numberint` | `string` | JSON path |
| `createdat.$date` | `object` | JSON path |
| `createdat.$date.$numberlong` | `string` | JSON path |
| `polls.[]` | `object` | JSON path |
| `polls.[].maxanswers.$numberint` | `string` | JSON path |
| `polls.[].options.a` | `object` | JSON path |
| `polls.[].options.a.text` | `string` | JSON path |
| `polls.[].options.b` | `object` | JSON path |
| `polls.[].options.b.text` | `string` | JSON path |
| `polls.[].options.c` | `object` | JSON path |
| `polls.[].options.c.text` | `string` | JSON path |
| `polls.[].options.d` | `object` | JSON path |
| `polls.[].options.d.text` | `string` | JSON path |
| `polls.[].options.e` | `object` | JSON path |
| `polls.[].options.e.text` | `string` | JSON path |
| `updatedat.$date` | `object` | JSON path |
| `updatedat.$date.$numberlong` | `string` | JSON path |
| `leaderboardconfig.configurations` | `array<object>` | JSON path |
| `leaderboardconfig.configurations.configurations[]` | `object` | JSON path |
| `leaderboardconfig.configurations.configurations[].category` | `string` | JSON path |
| `leaderboardconfig.configurations.configurations[].criteria` | `string` | JSON path |
| `leaderboardconfig.configurations.configurations[].duration` | `object` | JSON path |
| `leaderboardconfig.configurations.configurations[].duration.$numberint` | `string` | JSON path |
| `leaderboardconfig.configurations.configurations[].points` | `object` | JSON path |
| `leaderboardconfig.configurations.configurations[].points.$numberint` | `string` | JSON path |
| `leaderboardconfig.visibletoparticipants` | `bool` | JSON path |
| `agendaids.[]` | `object` | JSON path |
| `agendaids.[].$oid` | `string` | JSON path |
