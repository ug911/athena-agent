---
canonical: backend
table: wise_app_backend__study_materials
type: table
layer: raw
regions:
  in: backend
  na: backend_na
location: s3://[REDACTED-BUCKET]/production/wise-app-backend/study_materials
format: INPUTFORMAT
partition_keys: []
schema_parity: drift
last_synced: '2026-08-11T13:11:50+00:00'
sampled_rows: 0
sampled_region: null
---

# `backend.wise_app_backend__study_materials`

## Region availability

| Region | Athena database |
| --- | --- |
| `IN` | `backend` |
| `NA` | `backend_na` |

_⚠ Schema parity: **drift** — see Region drift section below._

## Columns (IN)

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` | from deserializer |
| `userid` | `string` | from deserializer |
| `name` | `string` | from deserializer |
| `description` | `string` | from deserializer |
| `type` | `string` | from deserializer |
| `classid` | `string` | from deserializer |
| `youtubeurl` | `string` | from deserializer |
| `subtype` | `string` | from deserializer |
| `resources` | `string` | from deserializer |
| `createdat` | `string` | from deserializer |
| `attachments` | `string` | from deserializer |
| `comments` | `string` | from deserializer |
| `__v` | `string` | from deserializer |
| `file` | `string` | from deserializer |
| `lastcommentedat` | `string` | from deserializer |

## Region drift

### `IN` (backend) vs `NA` (backend_na)

- Only in `NA`: `date`, `disablecommenting`, `time`

## DDL

### `IN` (backend)

```sql
CREATE EXTERNAL TABLE `backend.wise_app_backend__study_materials`(
  `_id` string COMMENT 'from deserializer', 
  `userid` string COMMENT 'from deserializer', 
  `name` string COMMENT 'from deserializer', 
  `description` string COMMENT 'from deserializer', 
  `type` string COMMENT 'from deserializer', 
  `classid` string COMMENT 'from deserializer', 
  `youtubeurl` string COMMENT 'from deserializer', 
  `subtype` string COMMENT 'from deserializer', 
  `resources` string COMMENT 'from deserializer', 
  `createdat` string COMMENT 'from deserializer', 
  `attachments` string COMMENT 'from deserializer', 
  `comments` string COMMENT 'from deserializer', 
  `__v` string COMMENT 'from deserializer', 
  `file` string COMMENT 'from deserializer', 
  `lastcommentedat` string COMMENT 'from deserializer')
ROW FORMAT SERDE 
  'org.openx.data.jsonserde.JsonSerDe' 
WITH SERDEPROPERTIES ( 
  'ignore.malformed.json'='true') 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.mapred.TextInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/production/wise-app-backend/study_materials'
TBLPROPERTIES (
  'compressionType'='gzip', 
  'transient_lastDdlTime'='1715597405')
```

### `NA` (backend_na)

```sql
CREATE EXTERNAL TABLE `backend_na.wise_app_backend__study_materials`(
  `_id` string COMMENT 'from deserializer', 
  `disablecommenting` string COMMENT 'from deserializer', 
  `name` string COMMENT 'from deserializer', 
  `description` string COMMENT 'from deserializer', 
  `date` string COMMENT 'from deserializer', 
  `time` string COMMENT 'from deserializer', 
  `userid` string COMMENT 'from deserializer', 
  `type` string COMMENT 'from deserializer', 
  `classid` string COMMENT 'from deserializer', 
  `youtubeurl` string COMMENT 'from deserializer', 
  `subtype` string COMMENT 'from deserializer', 
  `resources` string COMMENT 'from deserializer', 
  `createdat` string COMMENT 'from deserializer', 
  `attachments` string COMMENT 'from deserializer', 
  `comments` string COMMENT 'from deserializer', 
  `__v` string COMMENT 'from deserializer', 
  `file` string COMMENT 'from deserializer', 
  `lastcommentedat` string COMMENT 'from deserializer')
ROW FORMAT SERDE 
  'org.openx.data.jsonserde.JsonSerDe' 
WITH SERDEPROPERTIES ( 
  'ignore.malformed.json'='true') 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.mapred.TextInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/production_na/wise-app-backend/study_materials'
TBLPROPERTIES (
  'compressionType'='gzip', 
  'transient_lastDdlTime'='1759743521')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
