---
collection: "ChessGame"
athena_table: "wise_app_backend__chess_game"
mongo_field_count: 28
athena_field_count: 45
matched: 26
coverage_pct: 92.9
last_diffed: "2026-04-28T11:07:30+00:00"
---

# Schema gap: `ChessGame` ↔ `processed.wise_app_backend__chess_game`

- **Mongo source**: [`src/models/ChessGame.js`](../source/mongo/ChessGame.md)
- **Athena counterpart**: [`schemas/processed/processed/wise_app_backend__chess_game.md`](../processed/processed/wise_app_backend__chess_game.md)
- **Coverage**: 26/28 Mongo fields are present in Athena (**92.9%**).

## In Mongo, missing from Athena

These fields are declared in the Mongoose schema but the Athena lake pipeline doesn't expose them. Either widen the extractor or note the field as JSON-only inside an existing varchar column.

| Path | Type | Ref | Required |
| --- | --- | --- | --- |
| `startFEN` | `String` |  |  |
| `duration` | `Number` |  |  |

## In Athena, missing from Mongo

These fields exist in the Athena table but aren't declared in the current Mongoose schema. Likely renamed / deprecated, or added by the lake pipeline (timestamps, flattened helpers).

| Path | Type | Source |
| --- | --- | --- |
| `_id.$oid` | `string` | JSON path |
| `classid.$oid` | `string` | JSON path |
| `starttime.$date` | `object` | JSON path |
| `starttime.$date.$numberlong` | `string` | JSON path |
| `history.[]` | `object` | JSON path |
| `history.[].createdat` | `object` | JSON path |
| `history.[].createdat.$date` | `object` | JSON path |
| `history.[].createdat.$date.$numberlong` | `string` | JSON path |
| `createdat.$date` | `object` | JSON path |
| `createdat.$date.$numberlong` | `string` | JSON path |
| `updatedat.$date` | `object` | JSON path |
| `updatedat.$date.$numberlong` | `string` | JSON path |
| `__v.$numberint` | `string` | JSON path |
| `endtime.$date` | `object` | JSON path |
| `endtime.$date.$numberlong` | `string` | JSON path |
