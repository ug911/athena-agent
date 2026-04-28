---
database: backend
table: wise_app_backend__zoomrecordings
type: table
layer: raw
location: s3://[REDACTED-BUCKET]/production/wise-app-backend/zoomRecordings
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:10:07+00:00'
sampled_rows: 0
---

# `backend.wise_app_backend__zoomrecordings`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` | from deserializer |
| `createdat` | `string` | from deserializer |
| `sessionid` | `string` | from deserializer |
| `recordings` | `string` | from deserializer |
| `__v` | `string` | from deserializer |
| `zoomobjectid` | `string` | from deserializer |
| `classid` | `string` | from deserializer |
| `userid` | `string` | from deserializer |

## DDL

```sql
CREATE EXTERNAL TABLE `backend.wise_app_backend__zoomrecordings`(
  `_id` string COMMENT 'from deserializer', 
  `createdat` string COMMENT 'from deserializer', 
  `sessionid` string COMMENT 'from deserializer', 
  `recordings` string COMMENT 'from deserializer', 
  `__v` string COMMENT 'from deserializer', 
  `zoomobjectid` string COMMENT 'from deserializer', 
  `classid` string COMMENT 'from deserializer', 
  `userid` string COMMENT 'from deserializer')
ROW FORMAT SERDE 
  'org.openx.data.jsonserde.JsonSerDe' 
WITH SERDEPROPERTIES ( 
  'ignore.malformed.json'='true') 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.mapred.TextInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/production/wise-app-backend/zoomRecordings'
TBLPROPERTIES (
  'compressionType'='gzip', 
  'transient_lastDdlTime'='1626548358')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
