---
database: processed
table: wise_app_backend__manualattendance
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/ManualAttendance/
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:16:20+00:00'
sampled_rows: 200
---

# `processed.wise_app_backend__manualattendance`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` |  |
| `createdat` | `string` |  |
| `updatedat` | `string` |  |
| `sessionid` | `string` |  |
| `participants` | `string` |  |

## Inferred JSON structure

_Inferred from 200 sampled rows on 2026-04-28. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `69ed876b90f02a5152a21218`, `69ed877d57b91a77cb965951`, `69ed877ec448cf37584e89fe`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1777174379415`, `1777174397888`, `1777174398404`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1777174379415`, `1777177858585`, `1777181274477`

### `sessionid`

- `$oid` — `string`  e.g. `69ed876ba54268e1c07686a0`, `69e48af621b681516ad16f4a`, `69cb3186c59c3f0b423207c6`

### `participants`

  - `[]` — `object`
    - `firstentrytime` — `object`
      - `$date` — `object`
        - `$numberlong` — `string`  e.g. `1777174478497`, `1777174437853`, `1777174527530`
    - `lastexittime` — `object`
      - `$date` — `object`
        - `$numberlong` — `string`  e.g. `1777177858585`, `1777181274477`, `1777178724629`
    - `left` — `bool`  e.g. `true`, `true`, `true`
    - `live` — `bool`  e.g. `false`, `false`, `false`
    - `manual` — `bool`  e.g. `true`, `true`
    - `present` — `bool`  e.g. `false`, `false`, `false`
    - `userid` — `object`
      - `$oid` — `string`  e.g. `69e08be298ee51775fcfbc6d`, `69e08e1398ee51775fd1164a`, `69e090ff98ee51775fd3b781`
    - `username` — `string`  e.g. `[REDACTED]`
    - `userprofilepicture` — `string`  e.g. `https://cdn.wiseapp.live/images/institute_thumbnail/12.png`, `https://files.wiseapp.live/upload_files/68cbf9f8ea9d48d39012`, `https://files.wiseapp.live/upload_files/64fecbcec47b39bb3f97`

## DDL

```sql
CREATE EXTERNAL TABLE `processed.wise_app_backend__manualattendance`(
  `_id` string, 
  `createdat` string, 
  `updatedat` string, 
  `sessionid` string, 
  `participants` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/wise-app-backend/ManualAttendance/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260428_005854_00106_68n3s', 
  'trino_version'='0.215-24582-g0575ac4')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
