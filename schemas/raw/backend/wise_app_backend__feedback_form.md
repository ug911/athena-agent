---
database: backend
table: wise_app_backend__feedback_form
type: table
layer: raw
location: s3://[REDACTED-BUCKET]/production/wise-app-backend/feedback_form
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:06:43+00:00'
sampled_rows: 0
---

# `backend.wise_app_backend__feedback_form`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` | from deserializer |
| `instituteid` | `string` | from deserializer |
| `profile` | `string` | from deserializer |
| `__v` | `string` | from deserializer |
| `commenttext` | `string` | from deserializer |
| `createdat` | `string` | from deserializer |
| `enabled` | `string` | from deserializer |
| `questions` | `string` | from deserializer |
| `updatedat` | `string` | from deserializer |

## DDL

```sql
CREATE EXTERNAL TABLE `backend.wise_app_backend__feedback_form`(
  `_id` string COMMENT 'from deserializer', 
  `instituteid` string COMMENT 'from deserializer', 
  `profile` string COMMENT 'from deserializer', 
  `__v` string COMMENT 'from deserializer', 
  `commenttext` string COMMENT 'from deserializer', 
  `createdat` string COMMENT 'from deserializer', 
  `enabled` string COMMENT 'from deserializer', 
  `questions` string COMMENT 'from deserializer', 
  `updatedat` string COMMENT 'from deserializer')
ROW FORMAT SERDE 
  'org.openx.data.jsonserde.JsonSerDe' 
WITH SERDEPROPERTIES ( 
  'ignore.malformed.json'='true') 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.mapred.TextInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/production/wise-app-backend/feedback_form'
TBLPROPERTIES (
  'compressionType'='gzip', 
  'transient_lastDdlTime'='1709549753')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
