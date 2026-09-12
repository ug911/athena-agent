---
canonical: processed
table: webapp__payout_users
type: table
layer: processed
regions:
  in: processed
  na: processed_na
location: s3://[REDACTED-BUCKET]/processed/webapp/payout_users/
format: INPUTFORMAT
partition_keys: []
schema_parity: identical
last_synced: '2026-08-11T13:20:07+00:00'
sampled_rows: 200
sampled_region: in
---

# `processed.webapp__payout_users`

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
| `razorpay_contact_id` | `string` |  |
| `user_id` | `string` |  |
| `updated_at` | `string` |  |
| `created_at` | `string` |  |
| `primary_payout_account_id` | `string` |  |

## Inferred JSON structure

_Inferred from 200 sampled rows from `IN` on 2026-08-11. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `6a69af91b151c70001f5972d`, `6a047b5f24d71500017af76c`, `69b7fff4fa0c76000164d2ee`

### `user_id`

- `$oid` — `string`  e.g. `6a69a791002fa65af6ef1ab9`, `6a00bc278b92db95a279be8b`, `658a4aa59e3651f30527edd9`

### `updated_at`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1785311122559`, `1778678623991`, `1773666293547`

### `created_at`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1785311121717`, `1778678623262`, `1773666292791`

### `primary_payout_account_id`

- `$oid` — `string`  e.g. `6a69af92b151c70001f5972e`, `6a047b5f24d71500017af76d`, `69b7fff5fa0c76000164d2ef`

## DDL

_From `IN` (processed)._

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
  'trino_query_id'='20260811_011529_00025_qq29b', 
  'trino_version'='0.215-24619-g93e00a8')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
