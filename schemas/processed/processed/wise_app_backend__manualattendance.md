---
canonical: processed
table: wise_app_backend__manualattendance
type: table
layer: processed
regions:
  in: processed
  na: processed_na
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/ManualAttendance/
format: INPUTFORMAT
partition_keys: []
schema_parity: identical
last_synced: '2026-08-11T13:26:23+00:00'
sampled_rows: 200
sampled_region: in
---

# `processed.wise_app_backend__manualattendance`

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
| `createdat` | `string` |  |
| `updatedat` | `string` |  |
| `sessionid` | `string` |  |
| `participants` | `string` |  |

## Inferred JSON structure

_Inferred from 200 sampled rows from `IN` on 2026-08-11. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `6a77c9037822a1b6a6e71523`, `6a77c91b7fe8cfed4caeace3`, `6a77c91f7822a1b6a6e71538`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1786235139723`, `1786235163087`, `1786235167865`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1786238914580`, `1786239093360`, `1786239131987`

### `sessionid`

- `$oid` — `string`  e.g. `6a75f010c8c1bf8780bad982`, `6a77c91bdf1d164deb625353`, `6a7697c6dcd50f08d655bdf3`

### `participants`

  - `[]` — `object`
    - `firstentrytime` — `object`
      - `$date` — `object`
        - `$numberlong` — `string`  e.g. `1786235484855`, `1786235391824`, `1786235396828`
    - `lastexittime` — `object`
      - `$date` — `object`
        - `$numberlong` — `string`  e.g. `1786238914580`, `1786239093360`, `1786239131987`
    - `left` — `bool`  e.g. `true`, `true`, `true`
    - `live` — `bool`  e.g. `false`, `true`, `false`
    - `manual` — `bool`  e.g. `true`, `true`
    - `present` — `bool`  e.g. `false`, `true`, `false`
    - `userid` — `object`
      - `$oid` — `string`  e.g. `66f1e51192c7561e6a69c21e`, `69edb4c100512973d7ab55e8`, `69dd80fe98ee51775f06e77f`
    - `username` — `string`  e.g. `[REDACTED]`
    - `userprofilepicture` — `string`  e.g. `https://files.wiseapp.live/upload_files/68cbf9f8ea9d48d39012`, `https://files.wiseapp.live/upload_files/6a3a7cb4edb08f03486a`, `https://files.wiseapp.live/upload_files/6a23bffa7b439147de7e`

## DDL

_From `IN` (processed)._

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
  'trino_query_id'='20260811_010155_00187_ggfbe', 
  'trino_version'='0.215-24619-g93e00a8')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
