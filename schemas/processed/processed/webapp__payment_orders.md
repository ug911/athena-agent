---
database: processed
table: webapp__payment_orders
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/processed/webapp/payment_orders/
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:13:14+00:00'
sampled_rows: 200
---

# `processed.webapp__payment_orders`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` |  |
| `status` | `string` |  |
| `payment_type` | `string` |  |
| `payer_user_id` | `string` |  |
| `payee_user_id` | `string` |  |
| `payment_transaction_id` | `string` |  |
| `amount` | `string` |  |
| `currency` | `string` |  |
| `payout_triggered` | `string` |  |
| `payout_succeeded` | `string` |  |
| `updated_at` | `string` |  |
| `created_at` | `string` |  |
| `razorpay_order_id` | `string` |  |
| `charged_at` | `string` |  |
| `razorpay_payment_id` | `string` |  |
| `payout_id` | `string` |  |

## Enum-like columns

_String columns with ≤20 distinct values in 200 sampled rows. Distribution shown as `value (×count)`._

- `status`: `SUCCEEDED (×103)`, `FAILED (×85)`, `CANCELLED (×5)`, `PENDING_CONFIRMATION (×4)`, `PENDING (×3)`
- `payment_type`: `TRANSFER (×195)`, `COLLECTION (×5)`
- `currency`: `INR (×78)`, `USD (×36)`, `EUR (×26)`, `GBP (×25)`, `AUD (×22)`, `AED (×10)`, `CAD (×2)`, `SGD (×1)`
- `payout_triggered`: `false (×192)`, `true (×8)`
- `payout_succeeded`: `false (×192)`, `true (×8)`

## Inferred JSON structure

_Inferred from 200 sampled rows on 2026-04-28. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `69effa271f2b94000121637f`, `69effa121f2b94000121637e`, `69eff8dc1f2b94000121637a`

### `payer_user_id`

- `$oid` — `string`  e.g. `68f5f4955b9809ae4f182bc2`, `696e6fcc43579bbada7e5633`, `687a0e1b7c49d0a2e7665ce1`

### `payee_user_id`

- `$oid` — `string`  e.g. `688359c50933d0d619d95275`, `66eac79be9526efef5c32eaa`, `682da0bde02699db2764bc61`

### `amount`

- `$numberint` — `string`  e.g. `490000`, `18100`, `52500`

### `updated_at`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1777334828511`, `1777334803685`, `1777334497003`

### `created_at`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1777334823888`, `1777334802648`, `1777334492822`

### `charged_at`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1777334497002`, `1777334494247`, `1777334495544`

### `payout_id`

- `$oid` — `string`  e.g. `69ef90347e9f1c000786b8c7`, `69ef90347e9f1c000786b8c6`, `69ef90347e9f1c000786b8c7`

## DDL

```sql
CREATE EXTERNAL TABLE `processed.webapp__payment_orders`(
  `_id` string, 
  `status` string, 
  `payment_type` string, 
  `payer_user_id` string, 
  `payee_user_id` string, 
  `payment_transaction_id` string, 
  `amount` string, 
  `currency` string, 
  `payout_triggered` string, 
  `payout_succeeded` string, 
  `updated_at` string, 
  `created_at` string, 
  `razorpay_order_id` string, 
  `charged_at` string, 
  `razorpay_payment_id` string, 
  `payout_id` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/webapp/payment_orders/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260428_010727_00007_cazxi', 
  'trino_version'='0.215-24582-g0575ac4')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
