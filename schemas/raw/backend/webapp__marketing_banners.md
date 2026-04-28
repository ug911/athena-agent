---
database: backend
table: webapp__marketing_banners
type: table
layer: raw
location: s3://[REDACTED-BUCKET]/production/webapp/marketing_banners
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:04:57+00:00'
sampled_rows: 0
---

# `backend.webapp__marketing_banners`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` | from deserializer |
| `template_id` | `string` | from deserializer |
| `user_id` | `string` | from deserializer |
| `image_url` | `string` | from deserializer |
| `updated_at` | `string` | from deserializer |
| `created_at` | `string` | from deserializer |

## DDL

```sql
CREATE EXTERNAL TABLE `backend.webapp__marketing_banners`(
  `_id` string COMMENT 'from deserializer', 
  `template_id` string COMMENT 'from deserializer', 
  `user_id` string COMMENT 'from deserializer', 
  `image_url` string COMMENT 'from deserializer', 
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
  's3://[REDACTED-BUCKET]/production/webapp/marketing_banners'
TBLPROPERTIES (
  'compressionType'='gzip', 
  'transient_lastDdlTime'='1641895688')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
