---
collection: "VendorConfiguration"
athena_table: "wise_app_backend__vendor_configuration"
mongo_field_count: 19
athena_field_count: 23
matched: 10
coverage_pct: 52.6
last_diffed: "2026-04-28T11:07:30+00:00"
---

# Schema gap: `VendorConfiguration` ↔ `processed.wise_app_backend__vendor_configuration`

- **Mongo source**: [`src/models/VendorConfiguration.js`](../source/mongo/VendorConfiguration.md)
- **Athena counterpart**: [`schemas/processed/processed/wise_app_backend__vendor_configuration.md`](../processed/processed/wise_app_backend__vendor_configuration.md)
- **Coverage**: 10/19 Mongo fields are present in Athena (**52.6%**).

## In Mongo, missing from Athena

These fields are declared in the Mongoose schema but the Athena lake pipeline doesn't expose them. Either widen the extractor or note the field as JSON-only inside an existing varchar column.

| Path | Type | Ref | Required |
| --- | --- | --- | --- |
| `apiAccess` | `<apiAccessSchema>` |  |  |
| `apiAccess.apiKeys` | `Array<String>` |  |  |
| `s3Configuration` | `<s3ConfigurationSchema>` |  |  |
| `s3Configuration.accessKeyId` | `String` |  | required |
| `s3Configuration.secretAccessKey` | `String` |  | required |
| `s3Configuration.region` | `String` |  |  |
| `s3Configuration.bucketName` | `String` |  | required |
| `s3Configuration.pathPrefix` | `String` |  | required |
| `s3Configuration.aclConfig` | `Object` |  |  |

## In Athena, missing from Mongo

These fields exist in the Athena table but aren't declared in the current Mongoose schema. Likely renamed / deprecated, or added by the lake pipeline (timestamps, flattened helpers).

| Path | Type | Source |
| --- | --- | --- |
| `_id.$oid` | `string` | JSON path |
| `userid.$oid` | `string` | JSON path |
| `webhooks.[]` | `object` | JSON path |
| `webhooks.[]._id` | `object` | JSON path |
| `webhooks.[]._id.$oid` | `string` | JSON path |
| `createdat.$date` | `object` | JSON path |
| `createdat.$date.$numberlong` | `string` | JSON path |
| `updatedat.$date` | `object` | JSON path |
| `updatedat.$date.$numberlong` | `string` | JSON path |
| `__v.$numberint` | `string` | JSON path |
