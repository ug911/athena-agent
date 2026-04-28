---
collection: "transaction"
athena_table: "wise_app_backend__transaction"
mongo_field_count: 17
athena_field_count: 62
matched: 13
coverage_pct: 76.5
last_diffed: "2026-04-28T11:07:30+00:00"
---

# Schema gap: `transaction` ↔ `processed.wise_app_backend__transaction`

- **Mongo source**: [`src/models/Transaction.js`](../source/mongo/transaction.md)
- **Athena counterpart**: [`schemas/processed/processed/wise_app_backend__transaction.md`](../processed/processed/wise_app_backend__transaction.md)
- **Coverage**: 13/17 Mongo fields are present in Athena (**76.5%**).

## In Mongo, missing from Athena

These fields are declared in the Mongoose schema but the Athena lake pipeline doesn't expose them. Either widen the extractor or note the field as JSON-only inside an existing varchar column.

| Path | Type | Ref | Required |
| --- | --- | --- | --- |
| `lineItems[]` | `<lineItemSchema>` |  |  |
| `preTaxAmount` | `amountSchema` |  |  |
| `taxLineItems[]` | `<taxLineItemSchema>` |  |  |
| `taxLineItems[].description` | `String` |  |  |

## In Athena, missing from Mongo

These fields exist in the Athena table but aren't declared in the current Mongoose schema. Likely renamed / deprecated, or added by the lake pipeline (timestamps, flattened helpers).

| Path | Type | Source |
| --- | --- | --- |
| `_id.$oid` | `string` | JSON path |
| `metadata.amount_metadata` | `object` | JSON path |
| `metadata.amount_metadata.original_amount` | `object` | JSON path |
| `metadata.amount_metadata.original_amount.$numberint` | `string` | JSON path |
| `metadata.amount_metadata.payout_amount` | `object` | JSON path |
| `metadata.amount_metadata.payout_amount.$numberint` | `string` | JSON path |
| `metadata.amount_metadata.transaction_fee` | `object` | JSON path |
| `metadata.amount_metadata.transaction_fee.$numberint` | `string` | JSON path |
| `metadata.amount_metadata.transaction_fee_percent` | `object` | JSON path |
| `metadata.amount_metadata.transaction_fee_percent.$numberint` | `string` | JSON path |
| `metadata.chargeon` | `object` | JSON path |
| `metadata.chargeon.$date` | `object` | JSON path |
| `metadata.chargeon.$date.$numberlong` | `string` | JSON path |
| `metadata.classid` | `string` | JSON path |
| `metadata.classname` | `string` | JSON path |
| `metadata.display` | `string` | JSON path |
| `metadata.dueon` | `object|string` | JSON path |
| `metadata.dueon.$date` | `object` | JSON path |
| `metadata.dueon.$date.$numberlong` | `string` | JSON path |
| `metadata.inactive` | `bool` | JSON path |
| `metadata.index` | `object` | JSON path |
| `metadata.index.$numberint` | `string` | JSON path |
| `metadata.installmentid` | `string` | JSON path |
| `metadata.invoicenumber` | `string` | JSON path |
| `metadata.invoicetype` | `string` | JSON path |
| `metadata.migrate` | `bool` | JSON path |
| `metadata.migrated` | `bool` | JSON path |
| `metadata.paid` | `bool` | JSON path |
| `metadata.payment_ids` | `array<string>` | JSON path |
| `metadata.payment_ids.payment_ids[]` | `string` | JSON path |
| `metadata.payment_order_id` | `string` | JSON path |
| `metadata.paymentoptionid` | `string` | JSON path |
| `metadata.payout_id` | `string` | JSON path |
| `metadata.payout_metadata` | `object` | JSON path |
| `metadata.payout_metadata.account_type` | `string` | JSON path |
| `metadata.payout_metadata.masked_account` | `string` | JSON path |
| `metadata.plantype` | `string` | JSON path |
| `metadata.reason_code` | `string` | JSON path |
| `metadata.reversed` | `bool` | JSON path |
| `metadata.subject` | `string` | JSON path |
| `senderid.$oid` | `string` | JSON path |
| `receiverid.$oid` | `string` | JSON path |
| `amount.currency` | `string` | JSON path |
| `amount.value` | `object` | JSON path |
| `amount.value.$numberint` | `string` | JSON path |
| `createdat.$date` | `object` | JSON path |
| `createdat.$date.$numberlong` | `string` | JSON path |
| `__v.$numberint` | `string` | JSON path |
| `chargedat.$date` | `object` | JSON path |
| `chargedat.$date.$numberlong` | `string` | JSON path |
