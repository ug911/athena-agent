---
database: processed
table: wise_app_backend__institutegroupmember
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/InstituteGroupMember/
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:15:34+00:00'
sampled_rows: 200
---

# `processed.wise_app_backend__institutegroupmember`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` |  |
| `createdat` | `string` |  |
| `updatedat` | `string` |  |
| `groupid` | `string` |  |
| `type` | `string` |  |
| `memberid` | `string` |  |

## Enum-like columns

_String columns with ≤20 distinct values in 200 sampled rows. Distribution shown as `value (×count)`._

- `type`: `STUDENT (×145)`, `CLASSROOM (×55)`

## Inferred JSON structure

_Inferred from 200 sampled rows on 2026-04-28. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `676b935e4e221e2f26dcc4e5`, `676b935f4f01146216369e46`, `676b93608a131be2f1337948`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1735103326965`, `1735103327865`, `1735103328703`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1735103326965`, `1735103327865`, `1735103328703`

### `groupid`

- `$oid` — `string`  e.g. `676b92558a131b71d43371c3`, `676b92558a131b71d43371c3`, `676b92558a131b71d43371c3`

### `memberid`

- `$oid` — `string`  e.g. `675d4909ce9d3f277b43042c`, `675d48eaaeb366d0d252e9b4`, `6762b8432c0fad669ebca884`

## DDL

```sql
CREATE EXTERNAL TABLE `processed.wise_app_backend__institutegroupmember`(
  `_id` string, 
  `createdat` string, 
  `updatedat` string, 
  `groupid` string, 
  `type` string, 
  `memberid` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/wise-app-backend/InstituteGroupMember/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260428_003553_00070_2rp8x', 
  'trino_version'='0.215-24582-g0575ac4')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
