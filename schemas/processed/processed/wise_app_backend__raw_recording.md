---
canonical: processed
table: wise_app_backend__raw_recording
type: table
layer: processed
regions:
  in: processed
  na: processed_na
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/raw_recording/
format: INPUTFORMAT
partition_keys: []
schema_parity: identical
last_synced: '2026-08-11T13:27:01+00:00'
sampled_rows: 200
sampled_region: in
---

# `processed.wise_app_backend__raw_recording`

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
| `sessionid` | `string` |  |
| `__v` | `string` |  |
| `createdat` | `string` |  |
| `recordings` | `string` |  |
| `updatedat` | `string` |  |

## Inferred JSON structure

_Inferred from 200 sampled rows from `IN` on 2026-08-11. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `67978b3547d4866738e46a02`, `679b21bd47d48667388a7ab4`, `679b46a547d48667389950f0`

### `sessionid`

- `$oid` — `string`  e.g. `67978abfa5520afaa5fa45cd`, `679b2165174176fdee8fea73`, `679b463303e788ee928ad747`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1737984821298`, `1738219965737`, `1738229413342`

### `recordings`

  - `[]` — `object`
    - `_id` — `object`
      - `$oid` — `string`  e.g. `67978b35a4b3434623f1b212`, `679b21bd12d28b40c77d6947`, `679b46a533cb34c905e0a3ec`
    - `duration` — `object`
      - `$numberint` — `string`  e.g. `3`, `7`, `17`
    - `partindex` — `object`
      - `$numberint` — `string`  e.g. `1`, `1`, `1`
    - `sessionindex` — `object`
      - `$numberint` — `string`  e.g. `1`, `1`, `1`
    - `type` — `string`  e.g. `RECORDING`, `RECORDING`, `RECORDING`
    - `url` — `string`  e.g. `https://files.wiseapp.live/raw_recordings/5f15aca19aa2c74eba`, `https://files.wiseapp.live/raw_recordings/5f15aca19aa2c74eba`, `https://files.wiseapp.live/raw_recordings/5f15aca19aa2c74eba`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1737984821298`, `1738219965737`, `1738229413342`

## DDL

_From `IN` (processed)._

```sql
CREATE EXTERNAL TABLE `processed.wise_app_backend__raw_recording`(
  `_id` string, 
  `sessionid` string, 
  `__v` string, 
  `createdat` string, 
  `recordings` string, 
  `updatedat` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/wise-app-backend/raw_recording/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260811_012732_00061_ytt3p', 
  'trino_version'='0.215-24619-g93e00a8')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
