---
collection: "SavedCommunication"
athena_table: "wise_app_backend__saved_communication"
mongo_field_count: 11
athena_field_count: 18
matched: 5
coverage_pct: 45.5
last_diffed: "2026-04-28T11:07:30+00:00"
---

# Schema gap: `SavedCommunication` ↔ `processed.wise_app_backend__saved_communication`

- **Mongo source**: [`src/models/SavedCommunication.js`](../source/mongo/SavedCommunication.md)
- **Athena counterpart**: [`schemas/processed/processed/wise_app_backend__saved_communication.md`](../processed/processed/wise_app_backend__saved_communication.md)
- **Coverage**: 5/11 Mongo fields are present in Athena (**45.5%**).

## In Mongo, missing from Athena

These fields are declared in the Mongoose schema but the Athena lake pipeline doesn't expose them. Either widen the extractor or note the field as JSON-only inside an existing varchar column.

| Path | Type | Ref | Required |
| --- | --- | --- | --- |
| `instituteId` | `ObjectId` | `Institute` |  |
| `classId` | `ObjectId` | `class` |  |
| `notificationId` | `String` |  |  |
| `customIntegration` | `Boolean` |  |  |
| `title` | `String` |  |  |
| `statusMetadata` | `<inline-schema>` |  |  |

## In Athena, missing from Mongo

These fields exist in the Athena table but aren't declared in the current Mongoose schema. Likely renamed / deprecated, or added by the lake pipeline (timestamps, flattened helpers).

| Path | Type | Source |
| --- | --- | --- |
| `_id.$oid` | `string` | JSON path |
| `userid.$oid` | `string` | JSON path |
| `ownerid.$oid` | `string` | JSON path |
| `creditsused.$numberint` | `string` | JSON path |
| `createdat.$date` | `object` | JSON path |
| `createdat.$date.$numberlong` | `string` | JSON path |
| `updatedat.$date` | `object` | JSON path |
| `updatedat.$date.$numberlong` | `string` | JSON path |
| `__v.$numberint` | `string` | JSON path |
