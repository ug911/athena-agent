---
database: processed
table: wise_app_backend__live_class_discussion
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/live_class_discussion/
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:16:03+00:00'
sampled_rows: 200
---

# `processed.wise_app_backend__live_class_discussion`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` |  |
| `anonymous` | `string` |  |
| `upvoted` | `string` |  |
| `status` | `string` |  |
| `userid` | `string` |  |
| `question` | `string` |  |
| `insightid` | `string` |  |
| `replies` | `string` |  |
| `createdat` | `string` |  |
| `updatedat` | `string` |  |
| `__v` | `string` |  |
| `editedby` | `string` |  |
| `pinned` | `string` |  |
| `starred` | `string` |  |
| `edited` | `string` |  |

## Enum-like columns

_String columns with ≤20 distinct values in 200 sampled rows. Distribution shown as `value (×count)`._

- `anonymous`: `false (×153)`, `true (×47)`
- `status`: `APPROVED (×121)`, `RESOLVED (×53)`, `CREATED (×26)`
- `editedby`: `host (×17)`, `cohost (×3)`
- `pinned`: `true (×6)`, `false (×6)`
- `starred`: `true (×9)`, `false (×6)`

## Inferred JSON structure

_Inferred from 200 sampled rows on 2026-04-28. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `644f8e46d7e8fd2a7828dd73`, `644f8fda71ff481c06051caa`, `644f8fec5c29bade363bda19`

### `upvoted`

  - `[]` — `string`  e.g. `637f57f1c266ea8050b35606`, `637b622df533727ffc0d6ecd`, `637b62a31aeff37812fca17e`

### `insightid`

- `$oid` — `string`  e.g. `644f8d7dfb7e2ae52a3a2ee2`, `644f8d7dfb7e2ae52a3a2ee2`, `644f8d7dfb7e2ae52a3a2ee2`

### `replies`

  - `[]` — `object`
    - `_id` — `object`
      - `$oid` — `string`  e.g. `644f8e7149cc61f33076f5ff`, `644f8fe171ff4837fd051dc7`, `644f900e6ec70da2dd05fcaa`
    - `createdat` — `object`
      - `$date` — `object`
        - `$numberlong` — `string`  e.g. `1682935409404`, `1682935777554`, `1682935822663`
    - `reply` — `string`  e.g. `Jo First ke baad gya tha. `, `22`, `Jaipur :)`
    - `updatedat` — `object`
      - `$date` — `object`
        - `$numberlong` — `string`  e.g. `1682935409404`, `1682935777554`, `1682935822663`
    - `userid` — `string`  e.g. `637f2d37abf8c70bf7fd93f1`, `637f2d37abf8c70bf7fd93f1`, `637f2d37abf8c70bf7fd93f1`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1682935366994`, `1682935770733`, `1682935788114`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1682936028469`, `1682935783847`, `1682936086955`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

## DDL

```sql
CREATE EXTERNAL TABLE `processed.wise_app_backend__live_class_discussion`(
  `_id` string, 
  `anonymous` string, 
  `upvoted` string, 
  `status` string, 
  `userid` string, 
  `question` string, 
  `insightid` string, 
  `replies` string, 
  `createdat` string, 
  `updatedat` string, 
  `__v` string, 
  `editedby` string, 
  `pinned` string, 
  `starred` string, 
  `edited` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/wise-app-backend/live_class_discussion/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260428_005758_00151_9tvgb', 
  'trino_version'='0.215-24582-g0575ac4')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
