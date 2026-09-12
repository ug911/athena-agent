---
canonical: processed
table: webapp__payment_orders
type: table
layer: processed
regions:
  in: processed
  na: processed_na
location: s3://[REDACTED-BUCKET]/processed/webapp/payment_orders/
format: INPUTFORMAT
partition_keys: []
schema_parity: identical
last_synced: '2026-08-11T13:19:50+00:00'
sampled_rows: 200
sampled_region: in
---

# `processed.webapp__payment_orders`

## Region availability

| Region | Athena database |
| --- | --- |
| `IN` | `processed` |
| `NA` | `processed_na` |

_Schema parity: **identical** across regions._

## Columns (IN)

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

_String columns with ≤20 distinct values in 200 sampled rows from `IN`. Distribution shown as `value (×count)`._

- `status`: `SUCCEEDED (×125)`, `FAILED (×64)`, `CANCELLED (×8)`, `PENDING (×3)`
- `payment_type`: `TRANSFER (×190)`, `COLLECTION (×10)`
- `currency`: `INR (×103)`, `AED (×44)`, `USD (×33)`, `ILS (×6)`, `GBP (×5)`, `EUR (×4)`, `AUD (×3)`, `CAD (×2)`
- `payout_triggered`: `false (×199)`, `true (×1)`
- `payout_succeeded`: `false (×199)`, `true (×1)`

## Inferred JSON structure

_Inferred from 200 sampled rows from `IN` on 2026-08-11. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `6a7a6a16aac4fa0001e48810`, `6a7a697faac4fa0001e4880d`, `6a7a6911dc7a8b00013cd886`

### `payer_user_id`

- `$oid` — `string`  e.g. `69135412d1e46605c6684439`, `68c436b169bf3cf7e163e8ff`, `69a7f31413cc1073afe3359e`

### `payee_user_id`

- `$oid` — `string`  e.g. `67e5941b1212d98ff5fc467f`, `66eac79be9526efef5c32eaa`, `5f24052520955e1aff464606`

### `amount`

- `$numberint` — `string`  e.g. `52138`, `27000`, `4160`

### `updated_at`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1786407447248`, `1786407299353`, `1786407189101`

### `created_at`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1786407446209`, `1786407295233`, `1786407185699`

### `charged_at`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1786407299280`, `1786407189033`, `1786402562992`

### `payout_id`

- `$oid` — `string`  e.g. `6a79fdb49b6926000791f237`

## DDL

_From `IN` (processed)._

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
  'trino_query_id'='20260811_011553_00025_ahw6v', 
  'trino_version'='0.215-24619-g93e00a8')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
