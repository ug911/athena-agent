---
canonical: processed
table: wise_app_backend__session_feedback_submission
type: table
layer: processed
regions:
  in: processed
  na: processed_na
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/session_feedback_submission/
format: INPUTFORMAT
partition_keys: []
schema_parity: drift
last_synced: '2026-08-11T13:28:09+00:00'
sampled_rows: 200
sampled_region: in
---

# `processed.wise_app_backend__session_feedback_submission`

## Region availability

| Region | Athena database |
| --- | --- |
| `IN` | `processed` |
| `NA` | `processed_na` |

_⚠ Schema parity: **drift** — see Region drift section below._

## Columns (IN)

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` |  |
| `classid` | `string` |  |
| `profile` | `string` |  |
| `sessionid` | `string` |  |
| `userid` | `string` |  |
| `__v` | `string` |  |
| `answers` | `string` |  |
| `comment` | `string` |  |
| `commenttext` | `string` |  |
| `createdat` | `string` |  |
| `rating` | `string` |  |
| `sessionstatus` | `string` |  |
| `updatedat` | `string` |  |
| `metadata` | `string` |  |
| `creditsconsumed` | `string` |  |

## Region drift

### `IN` (processed) vs `NA` (processed_na)

- Only in `IN`: `creditsconsumed`

## Enum-like columns

_String columns with ≤20 distinct values in 200 sampled rows from `IN`. Distribution shown as `value (×count)`._

- `profile`: `student (×200)`

## Inferred JSON structure

_Inferred from 200 sampled rows from `IN` on 2026-08-11. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `65604ba6d58aa2003433cf68`, `65604ba6d58aa2003433cf74`, `65604ba6d58aa2003433cf7c`

### `classid`

- `$oid` — `string`  e.g. `63f5ea2b8c8228a85d3802e8`, `63fc63b2605312396c0c5e81`, `63fc63b2605312396c0c5e81`

### `sessionid`

- `$oid` — `string`  e.g. `641059a1547ace4bc8f3186b`, `63fc63e823d4343554560b25`, `63ff477fc2bbdb61f8bbfd49`

### `userid`

- `$oid` — `string`  e.g. `63b6c2416b3447561b408c00`, `63809a4bfab7fa014d91fba2`, `637b2efbb83202bbf7505385`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

### `answers`



### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1700809638521`, `1700809638521`, `1700809638521`

### `rating`

- `$numberint` — `string`  e.g. `4`, `10`, `8`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1700809638521`, `1700809638521`, `1700809638521`

### `metadata`

- `unauthusername` — `string`  e.g. `Ghazis`, `Adesh`, `Falguni`

## DDL

### `IN` (processed)

```sql
CREATE EXTERNAL TABLE `processed.wise_app_backend__session_feedback_submission`(
  `_id` string, 
  `classid` string, 
  `profile` string, 
  `sessionid` string, 
  `userid` string, 
  `__v` string, 
  `answers` string, 
  `comment` string, 
  `commenttext` string, 
  `createdat` string, 
  `rating` string, 
  `sessionstatus` string, 
  `updatedat` string, 
  `metadata` string, 
  `creditsconsumed` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/wise-app-backend/session_feedback_submission/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260811_012728_00115_fgy3c', 
  'trino_version'='0.215-24619-g93e00a8')
```

### `NA` (processed_na)

```sql
CREATE EXTERNAL TABLE `processed_na.wise_app_backend__session_feedback_submission`(
  `_id` string, 
  `classid` string, 
  `profile` string, 
  `sessionid` string, 
  `userid` string, 
  `__v` string, 
  `answers` string, 
  `comment` string, 
  `commenttext` string, 
  `createdat` string, 
  `rating` string, 
  `sessionstatus` string, 
  `updatedat` string, 
  `metadata` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed_na/wise-app-backend/session_feedback_submission/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260811_004058_00052_vy6up', 
  'trino_version'='0.215-24619-g93e00a8')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
