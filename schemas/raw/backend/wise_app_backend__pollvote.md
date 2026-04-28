---
database: backend
table: wise_app_backend__pollvote
type: table
layer: raw
location: s3://[REDACTED-BUCKET]/production/wise-app-backend/pollvote
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:08:04+00:00'
sampled_rows: 0
---

# `backend.wise_app_backend__pollvote`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` | from deserializer |
| `pollid` | `string` | from deserializer |
| `userid` | `string` | from deserializer |
| `answer` | `string` | from deserializer |
| `createdat` | `string` | from deserializer |
| `updatedat` | `string` | from deserializer |
| `__v` | `string` | from deserializer |

## DDL

```sql
CREATE EXTERNAL TABLE `backend.wise_app_backend__pollvote`(
  `_id` string COMMENT 'from deserializer', 
  `pollid` string COMMENT 'from deserializer', 
  `userid` string COMMENT 'from deserializer', 
  `answer` string COMMENT 'from deserializer', 
  `createdat` string COMMENT 'from deserializer', 
  `updatedat` string COMMENT 'from deserializer', 
  `__v` string COMMENT 'from deserializer')
ROW FORMAT SERDE 
  'org.openx.data.jsonserde.JsonSerDe' 
WITH SERDEPROPERTIES ( 
  'ignore.malformed.json'='true') 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.mapred.TextInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/production/wise-app-backend/pollvote'
TBLPROPERTIES (
  'compressionType'='gzip', 
  'transient_lastDdlTime'='1641897432')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
