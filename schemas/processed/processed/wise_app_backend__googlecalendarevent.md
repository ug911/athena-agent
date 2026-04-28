---
database: processed
table: wise_app_backend__googlecalendarevent
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/GoogleCalendarEvent/
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:15:08+00:00'
sampled_rows: 200
---

# `processed.wise_app_backend__googlecalendarevent`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` |  |
| `createdat` | `string` |  |
| `updatedat` | `string` |  |
| `sessionid` | `string` |  |
| `userid` | `string` |  |
| `starttime` | `string` |  |
| `endtime` | `string` |  |
| `title` | `string` |  |
| `description` | `string` |  |
| `googleeventid` | `string` |  |

## Enum-like columns

_String columns with ≤20 distinct values in 200 sampled rows. Distribution shown as `value (×count)`._

- `title`: `Gio | Physics Lessons (×195)`, `Live Session - 2nd Jun (×1)`, `Live Session - 30th Oct (Fractions) (×1)`, `Live Session - 25th Oct(Fractions) (×1)`, `Live Session - 19th Oct (Numbers) (×1)`, `Percentages (×1)`

## Inferred JSON structure

_Inferred from 200 sampled rows on 2026-04-28. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `67003d7f0a7f79e93fa1d1af`, `67455c582d8443c682716cbf`, `67455c7b2d8443c682717ab9`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1728068991941`, `1732598872299`, `1732598907959`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1764831846231`, `1764831846233`, `1764831846233`

### `sessionid`

- `$oid` — `string`  e.g. `665c89681e4b8464972a62e7`, `6721fbba4cd5d415c005c394`, `671bb97bf073cf0b1803faa4`

### `userid`

- `$oid` — `string`  e.g. `649aadffdfe873e1a57c72ae`, `660d334037a4d6855e315af6`, `660d334037a4d6855e315af6`

### `starttime`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1774918800000`, `1776128400000`, `1775523600000`

### `endtime`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1774922400000`, `1776132000000`, `1775527200000`

## DDL

```sql
CREATE EXTERNAL TABLE `processed.wise_app_backend__googlecalendarevent`(
  `_id` string, 
  `createdat` string, 
  `updatedat` string, 
  `sessionid` string, 
  `userid` string, 
  `starttime` string, 
  `endtime` string, 
  `title` string, 
  `description` string, 
  `googleeventid` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/wise-app-backend/GoogleCalendarEvent/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260428_003457_00016_by5i2', 
  'trino_version'='0.215-24582-g0575ac4')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
