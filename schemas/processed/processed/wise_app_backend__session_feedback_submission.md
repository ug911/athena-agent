---
database: processed
table: wise_app_backend__session_feedback_submission
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/session_feedback_submission/
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:17:13+00:00'
sampled_rows: 200
---

# `processed.wise_app_backend__session_feedback_submission`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` |  |
| `classid` | `string` |  |
| `profile` | `string` |  |
| `sessionid` | `string` |  |
| `userid` | `string` |  |
| `__v` | `string` |  |
| `answers` | `string` |  |
| `comment` | `string` |  |
| `commenttext` | `string` |  |
| `createdat` | `string` |  |
| `rating` | `string` |  |
| `sessionstatus` | `string` |  |
| `updatedat` | `string` |  |
| `metadata` | `string` |  |
| `creditsconsumed` | `string` |  |

## Enum-like columns

_String columns with ≤20 distinct values in 200 sampled rows. Distribution shown as `value (×count)`._

- `profile`: `student (×170)`, `teacher (×30)`
- `sessionstatus`: `COMPLETED (×29)`, `NOT_COMPLETED (×1)`

## Inferred JSON structure

_Inferred from 200 sampled rows on 2026-04-28. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `69e2434998ee51775f915f37`, `69e2434b98ee51775f916713`, `69e2434b98ee51775f9167f4`

### `classid`

- `$oid` — `string`  e.g. `69d2c1aea0de3c39ab58aa86`, `6889c018f909c7a84eeff782`, `6889c018f909c7a84eeff782`

### `sessionid`

- `$oid` — `string`  e.g. `69d2c1d3c53c1c7b0922e1db`, `69e1e40c297803e18bd08aec`, `69e1e40c297803e18bd08aec`

### `userid`

- `$oid` — `string`  e.g. `69cfeafa59c459d1a13b5c38`, `6853ead42960eb38db6394d8`, `6853b5122960eb38db46d6e3`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

### `answers`

  - `[]` — `object`
    - `_id` — `object`
      - `$oid` — `string`  e.g. `69e2434f2eb83d9666355117`, `69e2434f2eb83d9666355118`, `69e24362443c34ccbea968b4`
    - `answer` — `string`  e.g. `Devoir and il faut
reading article`, `Lesson 24`, `Types of keyboard instruments, Introduction to Keyboard, Dif`
    - `options` — `map<int,_>|object`
      - `<int>` — `string`  e.g. `Class`, `Exam`, `Worksheet`
    - `questiontext` — `string`  e.g. `Topics covered`, `Comments`, `Topics covered`
    - `type` — `string`  e.g. `SHORT_ANSWER`, `LONG_ANSWER`, `SHORT_ANSWER`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1776436041183`, `1776436043258`, `1776436043895`

### `rating`

- `$numberint` — `string`  e.g. `10`, `10`, `7`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1776436041183`, `1776436043258`, `1776436043895`

### `metadata`

- `autosubmitted` — `bool`  e.g. `true`, `true`, `true`

### `creditsconsumed`

- `$numberdouble` — `string`  e.g. `1.5`
- `$numberint` — `string`  e.g. `1`, `0`, `1`

## DDL

```sql
CREATE EXTERNAL TABLE `processed.wise_app_backend__session_feedback_submission`(
  `_id` string, 
  `classid` string, 
  `profile` string, 
  `sessionid` string, 
  `userid` string, 
  `__v` string, 
  `answers` string, 
  `comment` string, 
  `commenttext` string, 
  `createdat` string, 
  `rating` string, 
  `sessionstatus` string, 
  `updatedat` string, 
  `metadata` string, 
  `creditsconsumed` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/wise-app-backend/session_feedback_submission/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260428_011646_00007_g6fbh', 
  'trino_version'='0.215-24582-g0575ac4')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
