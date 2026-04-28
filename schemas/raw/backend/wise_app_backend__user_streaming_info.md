---
database: backend
table: wise_app_backend__user_streaming_info
type: table
layer: raw
location: s3://[REDACTED-BUCKET]/production/wise-app-backend/UserStreamingInfo
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:09:24+00:00'
sampled_rows: 0
---

# `backend.wise_app_backend__user_streaming_info`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` | from deserializer |
| `userid` | `string` | from deserializer |
| `streamingusage` | `string` | from deserializer |
| `totalstreamedgbs` | `string` | from deserializer |
| `createdat` | `string` | from deserializer |
| `updatedat` | `string` | from deserializer |
| `__v` | `string` | from deserializer |

## DDL

```sql
CREATE EXTERNAL TABLE `backend.wise_app_backend__user_streaming_info`(
  `_id` string COMMENT 'from deserializer', 
  `userid` string COMMENT 'from deserializer', 
  `streamingusage` string COMMENT 'from deserializer', 
  `totalstreamedgbs` string COMMENT 'from deserializer', 
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
  's3://[REDACTED-BUCKET]/production/wise-app-backend/UserStreamingInfo'
TBLPROPERTIES (
  'compressionType'='gzip', 
  'transient_lastDdlTime'='1659965077')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
