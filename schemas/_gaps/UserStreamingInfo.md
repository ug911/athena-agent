---
collection: "UserStreamingInfo"
athena_table: "wise_app_backend__user_streaming_info"
mongo_field_count: 19
athena_field_count: 29
matched: 11
coverage_pct: 57.9
last_diffed: "2026-04-28T11:07:30+00:00"
---

# Schema gap: `UserStreamingInfo` ↔ `processed.wise_app_backend__user_streaming_info`

- **Mongo source**: [`src/models/UserUsageInfo.js`](../source/mongo/UserStreamingInfo.md)
- **Athena counterpart**: [`schemas/processed/processed/wise_app_backend__user_streaming_info.md`](../processed/processed/wise_app_backend__user_streaming_info.md)
- **Coverage**: 11/19 Mongo fields are present in Athena (**57.9%**).

## In Mongo, missing from Athena

These fields are declared in the Mongoose schema but the Athena lake pipeline doesn't expose them. Either widen the extractor or note the field as JSON-only inside an existing varchar column.

| Path | Type | Ref | Required |
| --- | --- | --- | --- |
| `storageUsage[]` | `<storageInfoSchema>` |  |  |
| `storageUsage[].consumedGBs` | `Number` |  | required |
| `communicationUsage[]` | `<communicationEntry>` |  |  |
| `communicationUsage[].whatsapp` | `Number` |  | required |
| `communicationUsage[].email` | `Number` |  | required |
| `communicationUsage[].creditsUsed` | `Number` |  | required |
| `communicationUsage[].creditsRemaining` | `Number` |  | required |
| `totalCreditsUsed` | `Number` |  | required |

## In Athena, missing from Mongo

These fields exist in the Athena table but aren't declared in the current Mongoose schema. Likely renamed / deprecated, or added by the lake pipeline (timestamps, flattened helpers).

| Path | Type | Source |
| --- | --- | --- |
| `_id.$oid` | `string` | JSON path |
| `userid.$oid` | `string` | JSON path |
| `streamingusage.[]` | `object` | JSON path |
| `streamingusage.[].consumedmbs.$numberint` | `string` | JSON path |
| `streamingusage.[].date.$date` | `object` | JSON path |
| `streamingusage.[].date.$date.$numberlong` | `string` | JSON path |
| `streamingusage.[].remaininggbs.$numberdouble` | `string` | JSON path |
| `streamingusage.[].remaininggbs.$numberint` | `string` | JSON path |
| `streamingusage.[].uniquerequestips.$numberint` | `string` | JSON path |
| `streamingusage.[].uniquestreamedvideos.$numberint` | `string` | JSON path |
| `totalstreamedgbs.$numberdouble` | `string` | JSON path |
| `totalstreamedgbs.$numberint` | `string` | JSON path |
| `createdat.$date` | `object` | JSON path |
| `createdat.$date.$numberlong` | `string` | JSON path |
| `updatedat.$date` | `object` | JSON path |
| `updatedat.$date.$numberlong` | `string` | JSON path |
| `__v.$numberint` | `string` | JSON path |
