---
collection: "LensRoomConfig"
athena_table: "wise_app_backend__lens_room_config"
mongo_field_count: 19
athena_field_count: 18
matched: 7
coverage_pct: 36.8
last_diffed: "2026-04-28T11:07:30+00:00"
---

# Schema gap: `LensRoomConfig` ↔ `processed.wise_app_backend__lens_room_config`

- **Mongo source**: [`src/models/LensRoomConfig.js`](../source/mongo/LensRoomConfig.md)
- **Athena counterpart**: [`schemas/processed/processed/wise_app_backend__lens_room_config.md`](../processed/processed/wise_app_backend__lens_room_config.md)
- **Coverage**: 7/19 Mongo fields are present in Athena (**36.8%**).

## In Mongo, missing from Athena

These fields are declared in the Mongoose schema but the Athena lake pipeline doesn't expose them. Either widen the extractor or note the field as JSON-only inside an existing varchar column.

| Path | Type | Ref | Required |
| --- | --- | --- | --- |
| `polls[].question` | `String` |  | required |
| `polls[].questionType` | `String` |  |  |
| `polls[].options` | `<PollOptionsSchema>` |  | required |
| `polls[].type` | `String` |  | required |
| `polls[].correctAnswers` | `Array<String>` |  |  |
| `polls[].maxAnswers` | `Number` |  |  |
| `polls[].isWordCloud` | `Boolean` |  |  |
| `feedbackConfig.enabled` | `Boolean` |  |  |
| `feedbackConfig.question` | `String` |  |  |
| `discussionConfig.enabled` | `Boolean` |  |  |
| `discussionConfig.autoApproval` | `Boolean` |  |  |
| `discussionConfig.allowAnonymous` | `Boolean` |  |  |

## In Athena, missing from Mongo

These fields exist in the Athena table but aren't declared in the current Mongoose schema. Likely renamed / deprecated, or added by the lake pipeline (timestamps, flattened helpers).

| Path | Type | Source |
| --- | --- | --- |
| `_id.$oid` | `string` | JSON path |
| `classid.$oid` | `string` | JSON path |
| `__v.$numberint` | `string` | JSON path |
| `createdat.$date` | `object` | JSON path |
| `createdat.$date.$numberlong` | `string` | JSON path |
| `updatedat.$date` | `object` | JSON path |
| `updatedat.$date.$numberlong` | `string` | JSON path |
