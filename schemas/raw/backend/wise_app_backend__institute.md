---
database: backend
table: wise_app_backend__institute
type: table
layer: raw
location: s3://[REDACTED-BUCKET]/production/wise-app-backend/Institute
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:06:52+00:00'
sampled_rows: 0
---

# `backend.wise_app_backend__institute`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` | from deserializer |
| `name` | `string` | from deserializer |
| `namespace` | `string` | from deserializer |
| `ownerid` | `string` | from deserializer |
| `createdat` | `string` | from deserializer |
| `updatedat` | `string` | from deserializer |
| `settings` | `string` | from deserializer |
| `metadata` | `string` | from deserializer |

## DDL

```sql
CREATE EXTERNAL TABLE `backend.wise_app_backend__institute`(
  `_id` string COMMENT 'from deserializer', 
  `name` string COMMENT 'from deserializer', 
  `namespace` string COMMENT 'from deserializer', 
  `ownerid` string COMMENT 'from deserializer', 
  `createdat` string COMMENT 'from deserializer', 
  `updatedat` string COMMENT 'from deserializer', 
  `settings` string COMMENT 'from deserializer', 
  `metadata` string COMMENT 'from deserializer')
ROW FORMAT SERDE 
  'org.openx.data.jsonserde.JsonSerDe' 
WITH SERDEPROPERTIES ( 
  'ignore.malformed.json'='true') 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.mapred.TextInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/production/wise-app-backend/Institute'
TBLPROPERTIES (
  'compressionType'='gzip', 
  'transient_lastDdlTime'='1756813695')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
