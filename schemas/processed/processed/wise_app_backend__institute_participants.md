---
database: processed
table: wise_app_backend__institute_participants
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/InstituteParticipant/
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:15:22+00:00'
sampled_rows: 200
---

# `processed.wise_app_backend__institute_participants`

## Columns

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

_String columns with ≤20 distinct values in 200 sampled rows. Distribution shown as `value (×count)`._

- `status`: `ACCEPTED (×197)`, `REMOVED (×3)`
- `relation`: `STUDENT (×200)`

## Inferred JSON structure

_Inferred from 200 sampled rows on 2026-04-28. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `61fc0768ee51c8e2c8a19cd3`, `61fc0768ee51c8e2c8a19ccd`, `61fc0768ee51c8e2c8a19ce9`

### `userid`

- `$oid` — `string`  e.g. `6185db7baf8026914c95e68e`, `61851ab166950d5f5355c10f`, `61866f418f01d67e945b5307`

### `instituteid`

- `$oid` — `string`  e.g. `61fc06b54b31f9e992f780b5`, `61fc06b54b31f9e992f780b5`, `61fc06b54b31f9e992f780b5`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1643906920319`, `1643906920319`, `1643906920319`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1683827553981`, `1776494181912`, `1643906924948`

### `joinedon`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1683827553980`, `1695808388331`, `1643906924925`

### `metadata`

- `tags` — `array<unknown>`

## DDL

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
  'trino_query_id'='20260428_003452_00034_t28hb', 
  'trino_version'='0.215-24582-g0575ac4')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
