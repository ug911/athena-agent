---
database: backend
table: wise_app_backend__live_class_discussion
type: table
layer: raw
location: s3://[REDACTED-BUCKET]/production/wise-app-backend/live_class_discussion
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:07:42+00:00'
sampled_rows: 0
---

# `backend.wise_app_backend__live_class_discussion`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` | from deserializer |
| `anonymous` | `string` | from deserializer |
| `upvoted` | `string` | from deserializer |
| `status` | `string` | from deserializer |
| `userid` | `string` | from deserializer |
| `question` | `string` | from deserializer |
| `insightid` | `string` | from deserializer |
| `replies` | `string` | from deserializer |
| `createdat` | `string` | from deserializer |
| `updatedat` | `string` | from deserializer |
| `__v` | `string` | from deserializer |
| `editedby` | `string` | from deserializer |
| `pinned` | `string` | from deserializer |
| `starred` | `string` | from deserializer |
| `edited` | `string` | from deserializer |

## DDL

```sql
CREATE EXTERNAL TABLE `backend.wise_app_backend__live_class_discussion`(
  `_id` string COMMENT 'from deserializer', 
  `anonymous` string COMMENT 'from deserializer', 
  `upvoted` string COMMENT 'from deserializer', 
  `status` string COMMENT 'from deserializer', 
  `userid` string COMMENT 'from deserializer', 
  `question` string COMMENT 'from deserializer', 
  `insightid` string COMMENT 'from deserializer', 
  `replies` string COMMENT 'from deserializer', 
  `createdat` string COMMENT 'from deserializer', 
  `updatedat` string COMMENT 'from deserializer', 
  `__v` string COMMENT 'from deserializer', 
  `editedby` string COMMENT 'from deserializer', 
  `pinned` string COMMENT 'from deserializer', 
  `starred` string COMMENT 'from deserializer', 
  `edited` string COMMENT 'from deserializer')
ROW FORMAT SERDE 
  'org.openx.data.jsonserde.JsonSerDe' 
WITH SERDEPROPERTIES ( 
  'ignore.malformed.json'='true') 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.mapred.TextInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/production/wise-app-backend/live_class_discussion'
TBLPROPERTIES (
  'compressionType'='gzip', 
  'transient_lastDdlTime'='1709549836')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
