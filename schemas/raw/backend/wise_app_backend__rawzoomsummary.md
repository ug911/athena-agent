---
database: backend
table: wise_app_backend__rawzoomsummary
type: table
layer: raw
location: s3://[REDACTED-BUCKET]/production/wise-app-backend/RawZoomSummary
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:08:29+00:00'
sampled_rows: 0
---

# `backend.wise_app_backend__rawzoomsummary`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` | from deserializer |
| `createdat` | `string` | from deserializer |
| `updatedat` | `string` | from deserializer |
| `sessionid` | `string` | from deserializer |
| `summaries` | `string` | from deserializer |

## DDL

```sql
CREATE EXTERNAL TABLE `backend.wise_app_backend__rawzoomsummary`(
  `_id` string COMMENT 'from deserializer', 
  `createdat` string COMMENT 'from deserializer', 
  `updatedat` string COMMENT 'from deserializer', 
  `sessionid` string COMMENT 'from deserializer', 
  `summaries` string COMMENT 'from deserializer')
ROW FORMAT SERDE 
  'org.openx.data.jsonserde.JsonSerDe' 
WITH SERDEPROPERTIES ( 
  'ignore.malformed.json'='true') 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.mapred.TextInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/production/wise-app-backend/RawZoomSummary'
TBLPROPERTIES (
  'compressionType'='gzip', 
  'transient_lastDdlTime'='1743015852')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
