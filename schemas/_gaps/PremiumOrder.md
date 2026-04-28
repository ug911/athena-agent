---
collection: "PremiumOrder"
athena_table: "wise_app_backend__premium_order"
mongo_field_count: 21
athena_field_count: 41
matched: 12
coverage_pct: 57.1
last_diffed: "2026-04-28T11:07:30+00:00"
---

# Schema gap: `PremiumOrder` ↔ `processed.wise_app_backend__premium_order`

- **Mongo source**: [`src/models/PremiumOrder.js`](../source/mongo/PremiumOrder.md)
- **Athena counterpart**: [`schemas/processed/processed/wise_app_backend__premium_order.md`](../processed/processed/wise_app_backend__premium_order.md)
- **Coverage**: 12/21 Mongo fields are present in Athena (**57.1%**).

## In Mongo, missing from Athena

These fields are declared in the Mongoose schema but the Athena lake pipeline doesn't expose them. Either widen the extractor or note the field as JSON-only inside an existing varchar column.

| Path | Type | Ref | Required |
| --- | --- | --- | --- |
| `planDescription` | `String` |  |  |
| `metadata` | `Object` |  |  |
| `streamingGBs` | `Number` |  |  |
| `storageGBs` | `Number` |  |  |
| `commsCredits` | `Number` |  |  |
| `planMetadata.baseAmount` | `amountSchema` |  |  |
| `planMetadata.domesticTransactionFee` | `Number` |  |  |
| `planMetadata.internationalTransactionFee` | `Number` |  |  |
| `planMetadata.storageGBs` | `Number` |  |  |

## In Athena, missing from Mongo

These fields exist in the Athena table but aren't declared in the current Mongoose schema. Likely renamed / deprecated, or added by the lake pipeline (timestamps, flattened helpers).

| Path | Type | Source |
| --- | --- | --- |
| `licensecount` | `string` | column |
| `endsat` | `string` | column |
| `plantype` | `string` | column |
| `premiumplan` | `string` | column |
| `_id.$oid` | `string` | JSON path |
| `licensecount.$numberint` | `string` | JSON path |
| `userid.$oid` | `string` | JSON path |
| `startsfrom.$date` | `object` | JSON path |
| `startsfrom.$date.$numberlong` | `string` | JSON path |
| `endsat.$date` | `object` | JSON path |
| `endsat.$date.$numberlong` | `string` | JSON path |
| `amount.currency` | `string` | JSON path |
| `amount.value` | `object` | JSON path |
| `amount.value.$numberint` | `string` | JSON path |
| `createdat.$date` | `object` | JSON path |
| `createdat.$date.$numberlong` | `string` | JSON path |
| `updatedat.$date` | `object` | JSON path |
| `updatedat.$date.$numberlong` | `string` | JSON path |
| `planmetadata.unitamount.currency` | `string` | JSON path |
| `planmetadata.unitamount.value` | `object` | JSON path |
| `planmetadata.unitamount.value.$numberint` | `string` | JSON path |
| `planmetadata.unitcount.$numberint` | `string` | JSON path |
| `renewson.$date` | `object` | JSON path |
| `renewson.$date.$numberlong` | `string` | JSON path |
| `__v.$numberint` | `string` | JSON path |
