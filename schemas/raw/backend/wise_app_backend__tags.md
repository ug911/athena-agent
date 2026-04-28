---
database: backend
table: wise_app_backend__tags
type: table
layer: raw
location: s3://[REDACTED-BUCKET]/production/wise-app-backend/tags
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:09:02+00:00'
sampled_rows: 0
---

# `backend.wise_app_backend__tags`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` | from deserializer |
| `type` | `string` | from deserializer |
| `tag` | `string` | from deserializer |
| `searchterm` | `string` | from deserializer |

## DDL

```sql
CREATE EXTERNAL TABLE `backend.wise_app_backend__tags`(
  `_id` string COMMENT 'from deserializer', 
  `type` string COMMENT 'from deserializer', 
  `tag` string COMMENT 'from deserializer', 
  `searchterm` string COMMENT 'from deserializer')
ROW FORMAT SERDE 
  'org.openx.data.jsonserde.JsonSerDe' 
WITH SERDEPROPERTIES ( 
  'ignore.malformed.json'='true') 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.mapred.TextInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/production/wise-app-backend/tags'
TBLPROPERTIES (
  'compressionType'='gzip', 
  'transient_lastDdlTime'='1626548289')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
