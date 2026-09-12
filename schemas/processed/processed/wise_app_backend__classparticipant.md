---
canonical: processed
table: wise_app_backend__classparticipant
type: table
layer: processed
regions:
  in: processed
  na: processed_na
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/classparticipant/
format: INPUTFORMAT
partition_keys: []
schema_parity: identical
last_synced: '2026-08-11T13:21:58+00:00'
sampled_rows: 200
sampled_region: in
---

# `processed.wise_app_backend__classparticipant`

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
| `classid` | `string` |  |
| `relation` | `string` |  |
| `status` | `string` |  |
| `createdat` | `string` |  |
| `updatedat` | `string` |  |
| `__v` | `string` |  |
| `joinedon` | `string` |  |

## Enum-like columns

_String columns with ≤20 distinct values in 200 sampled rows from `IN`. Distribution shown as `value (×count)`._

- `relation`: `STUDENT (×180)`, `ADMIN (×20)`
- `status`: `ACCEPTED (×170)`, `REMOVED (×30)`

## Inferred JSON structure

_Inferred from 200 sampled rows from `IN` on 2026-08-11. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `61c09c2049685400070cf53d`, `61c09c2049685400070cf53c`, `61c09c2049685400070cf53f`

### `userid`

- `$oid` — `string`  e.g. `5f6f076ead4a1522dec687ae`, `5f75c7fe35bd837d9849dae3`, `6034f91bb365446805ed0993`

### `classid`

- `$oid` — `string`  e.g. `60375804c2f97a9938fd9dad`, `60375804c2f97a9938fd9dad`, `60375804c2f97a9938fd9dad`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1640012832962`, `1640012832962`, `1640012832962`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1640012832962`, `1657956856887`, `1640012832962`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

### `joinedon`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1614239748866`, `1657956856886`, `1614239748866`

## DDL

_From `IN` (processed)._

```sql
CREATE EXTERNAL TABLE `processed.wise_app_backend__classparticipant`(
  `_id` string, 
  `userid` string, 
  `classid` string, 
  `relation` string, 
  `status` string, 
  `createdat` string, 
  `updatedat` string, 
  `__v` string, 
  `joinedon` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/wise-app-backend/classparticipant/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260811_003250_00007_55w9t', 
  'trino_version'='0.215-24619-g93e00a8')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
