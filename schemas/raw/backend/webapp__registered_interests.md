---
database: backend
table: webapp__registered_interests
type: table
layer: raw
location: s3://[REDACTED-BUCKET]/production/webapp/registered_interests
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:05:26+00:00'
sampled_rows: 0
---

# `backend.webapp__registered_interests`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` | from deserializer |
| `phone_number` | `string` | from deserializer |
| `registered_for` | `string` | from deserializer |
| `name` | `string` | from deserializer |
| `email` | `string` | from deserializer |
| `updated_at` | `string` | from deserializer |
| `created_at` | `string` | from deserializer |

## DDL

```sql
CREATE EXTERNAL TABLE `backend.webapp__registered_interests`(
  `_id` string COMMENT 'from deserializer', 
  `phone_number` string COMMENT 'from deserializer', 
  `registered_for` string COMMENT 'from deserializer', 
  `name` string COMMENT 'from deserializer', 
  `email` string COMMENT 'from deserializer', 
  `updated_at` string COMMENT 'from deserializer', 
  `created_at` string COMMENT 'from deserializer')
ROW FORMAT SERDE 
  'org.openx.data.jsonserde.JsonSerDe' 
WITH SERDEPROPERTIES ( 
  'ignore.malformed.json'='true') 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.mapred.TextInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/production/webapp/registered_interests'
TBLPROPERTIES (
  'compressionType'='gzip', 
  'transient_lastDdlTime'='1641895713')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
