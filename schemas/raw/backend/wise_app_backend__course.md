---
database: backend
table: wise_app_backend__course
type: table
layer: raw
location: s3://[REDACTED-BUCKET]/production/wise-app-backend/course
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:06:28+00:00'
sampled_rows: 0
---

# `backend.wise_app_backend__course`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` | from deserializer |
| `coursetype` | `string` | from deserializer |
| `classroomids` | `string` | from deserializer |
| `instituteid` | `string` | from deserializer |
| `title` | `string` | from deserializer |
| `coursecovers` | `string` | from deserializer |
| `createdat` | `string` | from deserializer |
| `updatedat` | `string` | from deserializer |
| `__v` | `string` | from deserializer |
| `subtitle` | `string` | from deserializer |
| `description` | `string` | from deserializer |

## DDL

```sql
CREATE EXTERNAL TABLE `backend.wise_app_backend__course`(
  `_id` string COMMENT 'from deserializer', 
  `coursetype` string COMMENT 'from deserializer', 
  `classroomids` string COMMENT 'from deserializer', 
  `instituteid` string COMMENT 'from deserializer', 
  `title` string COMMENT 'from deserializer', 
  `coursecovers` string COMMENT 'from deserializer', 
  `createdat` string COMMENT 'from deserializer', 
  `updatedat` string COMMENT 'from deserializer', 
  `__v` string COMMENT 'from deserializer', 
  `subtitle` string COMMENT 'from deserializer', 
  `description` string COMMENT 'from deserializer')
ROW FORMAT SERDE 
  'org.openx.data.jsonserde.JsonSerDe' 
WITH SERDEPROPERTIES ( 
  'ignore.malformed.json'='true') 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.mapred.TextInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/production/wise-app-backend/course'
TBLPROPERTIES (
  'compressionType'='gzip', 
  'transient_lastDdlTime'='1709549711')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
