---
database: processed
table: transaction
type: view
layer: processed
location: null
format: null
partition_keys: []
last_synced: '2026-04-28T07:12:40+00:00'
sampled_rows: 0
---

# `processed.transaction`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` |  |
| `senderid` | `string` |  |
| `receiverid` | `string` |  |
| `amount_value` | `int` |  |
| `amount_currency` | `string` |  |
| `type` | `string` |  |
| `status` | `string` |  |
| `note` | `string` |  |
| `metadata` | `string` |  |
| `classid` | `string` |  |
| `paid` | `string` |  |
| `installment_index` | `string` |  |
| `invoicetype` | `string` |  |
| `invoicenumber` | `string` |  |
| `paymentoptionid` | `string` |  |
| `installmentid` | `string` |  |
| `dueon` | `timestamp` |  |
| `chargeon` | `timestamp` |  |
| `reason_code` | `string` |  |
| `plantype` | `string` |  |
| `payout_id` | `string` |  |
| `payment_order_id` | `string` |  |
| `transactiontype` | `string` |  |
| `chargedat` | `timestamp` |  |

## DDL

```sql
CREATE VIEW processed.transaction AS
SELECT
  CAST(JSON_EXTRACT(_id, '$["$oid"]') AS VARCHAR) _id
, CAST(JSON_EXTRACT(senderid, '$["$oid"]') AS VARCHAR) senderid
, CAST(JSON_EXTRACT(receiverid, '$["$oid"]') AS VARCHAR) receiverid
, (CAST(JSON_EXTRACT(amount, '$["value"]["$numberint"]') AS INTEGER) / 100) amount_value
, CAST(JSON_EXTRACT(amount, '$["currency"]') AS VARCHAR) amount_currency
, type
, status
, note
, metadata
, (CASE WHEN (CAST(JSON_EXTRACT(metadata, '$["classid"]["$oid"]') AS VARCHAR) IS NULL) THEN CAST(JSON_EXTRACT(metadata, '$["classid"]') AS VARCHAR) ELSE CAST(JSON_EXTRACT(metadata, '$["classid"]["$oid"]') AS VARCHAR) END) classid
, CAST(JSON_EXTRACT(metadata, '$["paid"]') AS VARCHAR) paid
, CAST(JSON_EXTRACT(metadata, '$["index"]["$numberint"]') AS VARCHAR) installment_index
, CAST(JSON_EXTRACT(metadata, '$["invoicetype"]') AS VARCHAR) invoicetype
, CAST(JSON_EXTRACT(metadata, '$["invoicenumber"]') AS VARCHAR) invoicenumber
, (CASE WHEN (CAST(JSON_EXTRACT(metadata, '$["paymentoptionid"]["$oid"]') AS VARCHAR) IS NULL) THEN CAST(JSON_EXTRACT(metadata, '$["paymentoptionid"]') AS VARCHAR) ELSE CAST(JSON_EXTRACT(metadata, '$["paymentoptionid"]["$oid"]') AS VARCHAR) END) paymentoptionid
, (CASE WHEN (CAST(JSON_EXTRACT(metadata, '$["installmentid"]["$oid"]') AS VARCHAR) IS NULL) THEN CAST(JSON_EXTRACT(metadata, '$["installmentid"]') AS VARCHAR) ELSE CAST(JSON_EXTRACT(metadata, '$["installmentid"]["$oid"]') AS VARCHAR) END) installmentid
, FROM_UNIXTIME(CAST(SUBSTR(CAST(JSON_EXTRACT(metadata, '$["dueon"]["$date"]["$numberlong"]') AS VARCHAR), 1, 10) AS DOUBLE)) dueon
, FROM_UNIXTIME(CAST(SUBSTR(CAST(JSON_EXTRACT(metadata, '$["chargeon"]["$date"]["$numberlong"]') AS VARCHAR), 1, 10) AS DOUBLE)) chargeon
, CAST(JSON_EXTRACT(metadata, '$["reason_code"]') AS VARCHAR) reason_code
, CAST(JSON_EXTRACT(metadata, '$["plantype"]') AS VARCHAR) plantype
, (CASE WHEN (CAST(JSON_EXTRACT(metadata, '$["payout_id"]["$oid"]') AS VARCHAR) IS NULL) THEN CAST(JSON_EXTRACT(metadata, '$["payout_id"]') AS VARCHAR) ELSE CAST(JSON_EXTRACT(metadata, '$["payout_id"]["$oid"]') AS VARCHAR) END) payout_id
, (CASE WHEN (CAST(JSON_EXTRACT(metadata, '$["payment_order_id"]["$oid"]') AS VARCHAR) IS NULL) THEN CAST(JSON_EXTRACT(metadata, '$["payment_order_id"]') AS VARCHAR) ELSE CAST(JSON_EXTRACT(metadata, '$["payment_order_id"]["$oid"]') AS VARCHAR) END) payment_order_id
, transactiontype
, FROM_UNIXTIME(CAST(SUBSTR(CAST(JSON_EXTRACT(chargedat, '$["$date"]["$numberlong"]') AS VARCHAR), 1, 10) AS DOUBLE)) chargedat
FROM
  wise_app_backend__transaction
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
