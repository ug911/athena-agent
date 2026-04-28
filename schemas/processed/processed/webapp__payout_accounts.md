---
database: processed
table: webapp__payout_accounts
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/processed/webapp/payout_accounts/
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:13:17+00:00'
sampled_rows: 200
---

# `processed.webapp__payout_accounts`

## Columns

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

_String columns with ≤20 distinct values in 200 sampled rows. Distribution shown as `value (×count)`._

- `account_type`: `bank_account (×198)`, `vpa (×2)`

## Inferred JSON structure

_Inferred from 200 sampled rows on 2026-04-28. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `69b7fff5fa0c76000164d2ef`, `6982e735624652000197d197`, `695b70c7b32d9900017e57a8`

### `payout_user_id`

- `$oid` — `string`  e.g. `69b7fff4fa0c76000164d2ee`, `6982e735624652000197d196`, `695b70c6b32d9900017e57a7`

### `updated_at`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1773666293539`, `1770186549888`, `1767600327202`

### `created_at`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1773666293539`, `1770186549888`, `1767600327202`

## DDL

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
  'trino_query_id'='20260428_010750_00043_cc48y', 
  'trino_version'='0.215-24582-g0575ac4')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
