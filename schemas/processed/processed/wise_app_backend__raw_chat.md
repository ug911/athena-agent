---
database: processed
table: wise_app_backend__raw_chat
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/raw_chat/
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:16:35+00:00'
sampled_rows: 200
---

# `processed.wise_app_backend__raw_chat`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` |  |
| `sessionid` | `string` |  |
| `chats` | `string` |  |
| `createdat` | `string` |  |
| `updatedat` | `string` |  |
| `__v` | `string` |  |

## Inferred JSON structure

_Inferred from 200 sampled rows on 2026-04-28. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `6476fefdc6930fca022fb543`, `6476ffceeeb6961f6e7c85b0`, `6477029ade9da3f540ecebca`

### `sessionid`

- `$oid` — `string`  e.g. `646ef96e083b5fe7942417ed`, `6476fe7404fd281b504a53a8`, `6476f65ea64cbbc02bc43334`

### `chats`

  - `[]` — `object`
    - `_id` — `object`
      - `$oid` — `string`  e.g. `6476fefdc6930fbd082fb544`, `6476ffceeeb69697967c85b1`, `6476ffceeeb69688917c85b2`
    - `partindex` — `object`
      - `$numberint` — `string`  e.g. `1`, `1`, `2`
    - `url` — `string`  e.g. `https://files.wiseapp.live/ephemeral_files/624c0829ed7eb6875`, `https://files.wiseapp.live/ephemeral_files/5f154a7e88cd37040`, `https://files.wiseapp.live/ephemeral_files/5f154a7e88cd37040`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1685520125029`, `1685520334401`, `1685521050779`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1749450819995`, `1749450819995`, `1749450819995`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

## DDL

```sql
CREATE EXTERNAL TABLE `processed.wise_app_backend__raw_chat`(
  `_id` string, 
  `sessionid` string, 
  `chats` string, 
  `createdat` string, 
  `updatedat` string, 
  `__v` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/wise-app-backend/raw_chat/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260428_011720_00016_bvnah', 
  'trino_version'='0.215-24582-g0575ac4')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
