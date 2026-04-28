---
database: backend
table: webapp__marketing_templates
type: table
layer: raw
location: s3://[REDACTED-BUCKET]/production/webapp/marketing_templates
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:05:02+00:00'
sampled_rows: 0
---

# `backend.webapp__marketing_templates`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` | from deserializer |
| `archived` | `string` | from deserializer |
| `html_template` | `string` | from deserializer |
| `preview_image` | `string` | from deserializer |
| `image_height` | `string` | from deserializer |
| `image_width` | `string` | from deserializer |
| `updated_at` | `string` | from deserializer |
| `created_at` | `string` | from deserializer |
| `template_variables` | `string` | from deserializer |
| `target` | `string` | from deserializer |
| `category` | `string` | from deserializer |

## DDL

```sql
CREATE EXTERNAL TABLE `backend.webapp__marketing_templates`(
  `_id` string COMMENT 'from deserializer', 
  `archived` string COMMENT 'from deserializer', 
  `html_template` string COMMENT 'from deserializer', 
  `preview_image` string COMMENT 'from deserializer', 
  `image_height` string COMMENT 'from deserializer', 
  `image_width` string COMMENT 'from deserializer', 
  `updated_at` string COMMENT 'from deserializer', 
  `created_at` string COMMENT 'from deserializer', 
  `template_variables` string COMMENT 'from deserializer', 
  `target` string COMMENT 'from deserializer', 
  `category` string COMMENT 'from deserializer')
ROW FORMAT SERDE 
  'org.openx.data.jsonserde.JsonSerDe' 
WITH SERDEPROPERTIES ( 
  'ignore.malformed.json'='true') 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.mapred.TextInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/production/webapp/marketing_templates'
TBLPROPERTIES (
  'compressionType'='gzip', 
  'transient_lastDdlTime'='1641895707')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
