---
canonical: processed
table: webapp__payout_accounts
type: table
layer: processed
regions:
  in: processed
  na: processed_na
location: s3://[REDACTED-BUCKET]/processed/webapp/payout_accounts/
format: INPUTFORMAT
partition_keys: []
schema_parity: identical
last_synced: '2026-08-11T13:20:00+00:00'
sampled_rows: 200
sampled_region: in
---

# `processed.webapp__payout_accounts`

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
| `vpa` | `string` |  |
| `account_type` | `string` |  |
| `payout_user_id` | `string` |  |
| `razorpay_fund_account_id` | `string` |  |
| `updated_at` | `string` |  |
| `created_at` | `string` |  |

## Enum-like columns

_String columns with ≤20 distinct values in 200 sampled rows from `IN`. Distribution shown as `value (×count)`._

- `account_type`: `bank_account (×198)`, `vpa (×2)`

## Inferred JSON structure

_Inferred from 200 sampled rows from `IN` on 2026-08-11. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `6a69af92b151c70001f5972e`, `6a672885bfca940001e7c149`, `6a047b5f24d71500017af76d`

### `payout_user_id`

- `$oid` — `string`  e.g. `6a69af91b151c70001f5972d`, `602f592027b3040001731cf3`, `6a047b5f24d71500017af76c`

### `updated_at`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1785311122512`, `1785145477868`, `1778678623941`

### `created_at`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1785311122512`, `1785145477868`, `1778678623941`

## DDL

_From `IN` (processed)._

```sql
CREATE EXTERNAL TABLE `processed.webapp__payout_accounts`(
  `_id` string, 
  `vpa` string, 
  `account_type` string, 
  `payout_user_id` string, 
  `razorpay_fund_account_id` string, 
  `updated_at` string, 
  `created_at` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/webapp/payout_accounts/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260811_011530_00007_8428a', 
  'trino_version'='0.215-24619-g93e00a8')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
