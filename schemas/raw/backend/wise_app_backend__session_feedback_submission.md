---
database: backend
table: wise_app_backend__session_feedback_submission
type: table
layer: raw
location: s3://[REDACTED-BUCKET]/production/wise-app-backend/session_feedback_submission
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:08:54+00:00'
sampled_rows: 0
---

# `backend.wise_app_backend__session_feedback_submission`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` | from deserializer |
| `classid` | `string` | from deserializer |
| `profile` | `string` | from deserializer |
| `sessionid` | `string` | from deserializer |
| `userid` | `string` | from deserializer |
| `__v` | `string` | from deserializer |
| `answers` | `string` | from deserializer |
| `comment` | `string` | from deserializer |
| `commenttext` | `string` | from deserializer |
| `createdat` | `string` | from deserializer |
| `rating` | `string` | from deserializer |
| `sessionstatus` | `string` | from deserializer |
| `updatedat` | `string` | from deserializer |
| `metadata` | `string` | from deserializer |
| `creditsconsumed` | `string` | from deserializer |

## DDL

```sql
CREATE EXTERNAL TABLE `backend.wise_app_backend__session_feedback_submission`(
  `_id` string COMMENT 'from deserializer', 
  `classid` string COMMENT 'from deserializer', 
  `profile` string COMMENT 'from deserializer', 
  `sessionid` string COMMENT 'from deserializer', 
  `userid` string COMMENT 'from deserializer', 
  `__v` string COMMENT 'from deserializer', 
  `answers` string COMMENT 'from deserializer', 
  `comment` string COMMENT 'from deserializer', 
  `commenttext` string COMMENT 'from deserializer', 
  `createdat` string COMMENT 'from deserializer', 
  `rating` string COMMENT 'from deserializer', 
  `sessionstatus` string COMMENT 'from deserializer', 
  `updatedat` string COMMENT 'from deserializer', 
  `metadata` string COMMENT 'from deserializer', 
  `creditsconsumed` string COMMENT 'from deserializer')
ROW FORMAT SERDE 
  'org.openx.data.jsonserde.JsonSerDe' 
WITH SERDEPROPERTIES ( 
  'ignore.malformed.json'='true') 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.mapred.TextInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/production/wise-app-backend/session_feedback_submission'
TBLPROPERTIES (
  'compressionType'='gzip', 
  'transient_lastDdlTime'='1729166269')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
