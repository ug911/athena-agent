---
canonical: processed
table: wise_app_backend__institute_participants
type: table
layer: processed
regions:
  in: processed
  na: processed_na
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/InstituteParticipant/
format: INPUTFORMAT
partition_keys: []
schema_parity: identical
last_synced: '2026-08-11T13:24:12+00:00'
sampled_rows: 200
sampled_region: in
---

# `processed.wise_app_backend__institute_participants`

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
| `userid` | `string` |  |
| `instituteid` | `string` |  |
| `status` | `string` |  |
| `createdat` | `string` |  |
| `updatedat` | `string` |  |
| `joinedon` | `string` |  |
| `relation` | `string` |  |
| `metadata` | `string` |  |

## Enum-like columns

_String columns with ≤20 distinct values in 200 sampled rows from `IN`. Distribution shown as `value (×count)`._

- `status`: `ACCEPTED (×196)`, `REQUESTED (×3)`, `REMOVED (×1)`
- `relation`: `STUDENT (×200)`

## Inferred JSON structure

_Inferred from 200 sampled rows from `IN` on 2026-08-11. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `6204ba217c8bccdb3dca5b5d`, `6204ba217c8bccdb3dca5bc0`, `6204ba8f7c8bccdb3dcaa3dd`

### `userid`

- `$oid` — `string`  e.g. `654b5f870e9e880016d92703`, `654b5f870e9e880016d927ed`, `654b5f870e9e880016d92759`

### `instituteid`

- `$oid` — `string`  e.g. `6203ee45bba3e339aec3763b`, `6203ee45bba3e339aec3763b`, `6203ee45bba3e339aec3763b`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1644476961045`, `1644476961236`, `1644477071366`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1699438518723`, `1699438518723`, `1742321562956`

### `joinedon`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1644845296328`, `1644847768145`, `1644994796887`

### `metadata`

- `tags` — `array<unknown>`

## DDL

_From `IN` (processed)._

```sql
CREATE EXTERNAL TABLE `processed.wise_app_backend__institute_participants`(
  `_id` string, 
  `userid` string, 
  `instituteid` string, 
  `status` string, 
  `createdat` string, 
  `updatedat` string, 
  `joinedon` string, 
  `relation` string, 
  `metadata` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/wise-app-backend/InstituteParticipant/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260811_003811_00034_kwvzt', 
  'trino_version'='0.215-24619-g93e00a8')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
