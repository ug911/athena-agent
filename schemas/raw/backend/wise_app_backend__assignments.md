---
database: backend
table: wise_app_backend__assignments
type: table
layer: raw
location: s3://[REDACTED-BUCKET]/production/wise-app-backend/assignments
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:05:43+00:00'
sampled_rows: 0
---

# `backend.wise_app_backend__assignments`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` | from deserializer |
| `disablecommenting` | `string` | from deserializer |
| `topic` | `string` | from deserializer |
| `submissiondate` | `string` | from deserializer |
| `userid` | `string` | from deserializer |
| `submissiontime` | `string` | from deserializer |
| `description` | `string` | from deserializer |
| `maxmarks` | `string` | from deserializer |
| `attachments` | `string` | from deserializer |
| `classid` | `string` | from deserializer |
| `solutions` | `string` | from deserializer |
| `submission` | `string` | from deserializer |
| `createdat` | `string` | from deserializer |
| `comments` | `string` | from deserializer |
| `__v` | `string` | from deserializer |
| `submitby` | `string` | from deserializer |
| `starttime` | `string` | from deserializer |
| `criteria` | `string` | from deserializer |
| `public` | `string` | from deserializer |
| `thumbnail` | `string` | from deserializer |

## DDL

```sql
CREATE EXTERNAL TABLE `backend.wise_app_backend__assignments`(
  `_id` string COMMENT 'from deserializer', 
  `disablecommenting` string COMMENT 'from deserializer', 
  `topic` string COMMENT 'from deserializer', 
  `submissiondate` string COMMENT 'from deserializer', 
  `userid` string COMMENT 'from deserializer', 
  `submissiontime` string COMMENT 'from deserializer', 
  `description` string COMMENT 'from deserializer', 
  `maxmarks` string COMMENT 'from deserializer', 
  `attachments` string COMMENT 'from deserializer', 
  `classid` string COMMENT 'from deserializer', 
  `solutions` string COMMENT 'from deserializer', 
  `submission` string COMMENT 'from deserializer', 
  `createdat` string COMMENT 'from deserializer', 
  `comments` string COMMENT 'from deserializer', 
  `__v` string COMMENT 'from deserializer', 
  `submitby` string COMMENT 'from deserializer', 
  `starttime` string COMMENT 'from deserializer', 
  `criteria` string COMMENT 'from deserializer', 
  `public` string COMMENT 'from deserializer', 
  `thumbnail` string COMMENT 'from deserializer')
ROW FORMAT SERDE 
  'org.openx.data.jsonserde.JsonSerDe' 
WITH SERDEPROPERTIES ( 
  'ignore.malformed.json'='true') 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.mapred.TextInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/production/wise-app-backend/assignments'
TBLPROPERTIES (
  'compressionType'='gzip', 
  'transient_lastDdlTime'='1743481626')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
