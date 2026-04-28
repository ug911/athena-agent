---
database: backend
table: wise_app_backend__classroom_public_profile
type: table
layer: raw
location: s3://[REDACTED-BUCKET]/production/wise-app-backend/classroom_public_profile
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:06:21+00:00'
sampled_rows: 0
---

# `backend.wise_app_backend__classroom_public_profile`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` | from deserializer |
| `classid` | `string` | from deserializer |
| `__v` | `string` | from deserializer |
| `classcovers` | `string` | from deserializer |
| `createdat` | `string` | from deserializer |
| `description` | `string` | from deserializer |
| `subtitle` | `string` | from deserializer |
| `title` | `string` | from deserializer |
| `updatedat` | `string` | from deserializer |

## DDL

```sql
CREATE EXTERNAL TABLE `backend.wise_app_backend__classroom_public_profile`(
  `_id` string COMMENT 'from deserializer', 
  `classid` string COMMENT 'from deserializer', 
  `__v` string COMMENT 'from deserializer', 
  `classcovers` string COMMENT 'from deserializer', 
  `createdat` string COMMENT 'from deserializer', 
  `description` string COMMENT 'from deserializer', 
  `subtitle` string COMMENT 'from deserializer', 
  `title` string COMMENT 'from deserializer', 
  `updatedat` string COMMENT 'from deserializer')
ROW FORMAT SERDE 
  'org.openx.data.jsonserde.JsonSerDe' 
WITH SERDEPROPERTIES ( 
  'ignore.malformed.json'='true') 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.mapred.TextInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/production/wise-app-backend/classroom_public_profile'
TBLPROPERTIES (
  'compressionType'='gzip', 
  'transient_lastDdlTime'='1709549691')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
