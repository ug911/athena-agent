---
canonical: processed
table: wise_app_backend__lens_event
type: table
layer: processed
regions:
  in: processed
  na: processed_na
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/lens_event/
format: INPUTFORMAT
partition_keys: []
schema_parity: identical
last_synced: '2026-08-11T13:25:09+00:00'
sampled_rows: 200
sampled_region: in
---

# `processed.wise_app_backend__lens_event`

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
| `eventname` | `string` |  |
| `insightid` | `string` |  |
| `userid` | `string` |  |
| `eventpayload` | `string` |  |
| `createdat` | `string` |  |
| `updatedat` | `string` |  |
| `__v` | `string` |  |

## Enum-like columns

_String columns with ≤20 distinct values in 200 sampled rows from `IN`. Distribution shown as `value (×count)`._

- `eventname`: `POINTS_GIVEN (×200)`
- `userid`: `637b62a31aeff37812fca17e (×31)`, `6384cb5d679f553a2dd30200 (×28)`, `63b6c2416b3447561b408c00 (×25)`, `637db5ae5d97ca7a012a3881 (×22)`, `637f58a5d95c8032c9d29a1b (×18)`, `632aac01f185a4b296b8f6cf (×18)`, `637f56d4d3e3e7a22f76a37f (×17)`, `6374d83e271de900dd26a83f (×15)`, `637b2efbb83202bbf7505385 (×11)`, `637b906ea203ae0c580b293d (×6)`, `637f57f1c266ea8050b35606 (×5)`, `637b6347c96d3fa2f3cc5c15 (×3)`, `63809a4bfab7fa014d91fba2 (×1)`

## Inferred JSON structure

_Inferred from 200 sampled rows from `IN` on 2026-08-11. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `643544cb4c9ea7329ebfa096`, `643544cb4c9ea7cfd8bfa097`, `643544cb4c9ea70797bfa098`

### `insightid`

- `$oid` — `string`  e.g. `643541f443e715be7e832670`, `643541f443e715be7e832670`, `643541f443e715be7e832670`

### `eventpayload`

- `category` — `string`  e.g. `attention`, `attention`, `attention`
- `criteria` — `string`  e.g. `streak`, `streak`, `streak`
- `points` — `object`
  - `$numberint` — `string`  e.g. `5`, `5`, `5`
- `userid` — `string`  e.g. `6374d83e271de900dd26a83f`, `637b906ea203ae0c580b293d`, `637f58a5d95c8032c9d29a1b`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1681212619592`, `1681212619599`, `1681212619599`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1681212619592`, `1681212619599`, `1681212619599`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

## DDL

_From `IN` (processed)._

```sql
CREATE EXTERNAL TABLE `processed.wise_app_backend__lens_event`(
  `_id` string, 
  `eventname` string, 
  `insightid` string, 
  `userid` string, 
  `eventpayload` string, 
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
  's3://[REDACTED-BUCKET]/processed/wise-app-backend/lens_event/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260811_010315_00016_465my', 
  'trino_version'='0.215-24619-g93e00a8')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
