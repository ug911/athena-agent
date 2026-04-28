---
database: backend
table: wise_app_backend__event
type: table
layer: raw
location: s3://[REDACTED-BUCKET]/production/wise-app-backend/event
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:06:41+00:00'
sampled_rows: 0
---

# `backend.wise_app_backend__event`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` | from deserializer |
| `eventid` | `string` | from deserializer |
| `eventname` | `string` | from deserializer |
| `payload` | `string` | from deserializer |
| `eventtimestamp` | `string` | from deserializer |
| `__v` | `string` | from deserializer |

## DDL

```sql
CREATE EXTERNAL TABLE `backend.wise_app_backend__event`(
  `_id` string COMMENT 'from deserializer', 
  `eventid` string COMMENT 'from deserializer', 
  `eventname` string COMMENT 'from deserializer', 
  `payload` string COMMENT 'from deserializer', 
  `eventtimestamp` string COMMENT 'from deserializer', 
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
  's3://[REDACTED-BUCKET]/production/wise-app-backend/event'
TBLPROPERTIES (
  'compressionType'='gzip', 
  'transient_lastDdlTime'='1626548262')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
