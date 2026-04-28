---
database: processed
table: webapp__payout_users
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/processed/webapp/payout_users/
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:13:21+00:00'
sampled_rows: 200
---

# `processed.webapp__payout_users`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` |  |
| `razorpay_contact_id` | `string` |  |
| `user_id` | `string` |  |
| `updated_at` | `string` |  |
| `created_at` | `string` |  |
| `primary_payout_account_id` | `string` |  |

## Inferred JSON structure

_Inferred from 200 sampled rows on 2026-04-28. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `69b7fff4fa0c76000164d2ee`, `6982e735624652000197d196`, `695b70c6b32d9900017e57a7`

### `user_id`

- `$oid` — `string`  e.g. `658a4aa59e3651f30527edd9`, `68ecbef3b9932c954a59df74`, `6618d87ba46d5d07b4d87f42`

### `updated_at`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1773666293547`, `1770186549896`, `1767600327211`

### `created_at`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1773666292791`, `1770186549188`, `1767600326533`

### `primary_payout_account_id`

- `$oid` — `string`  e.g. `69b7fff5fa0c76000164d2ef`, `6982e735624652000197d197`, `695b70c7b32d9900017e57a8`

## DDL

```sql
CREATE EXTERNAL TABLE `processed.webapp__payout_users`(
  `_id` string, 
  `razorpay_contact_id` string, 
  `user_id` string, 
  `updated_at` string, 
  `created_at` string, 
  `primary_payout_account_id` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/webapp/payout_users/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260428_010750_00088_j4z3f', 
  'trino_version'='0.215-24582-g0575ac4')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
