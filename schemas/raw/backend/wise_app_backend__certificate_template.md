---
database: backend
table: wise_app_backend__certificate_template
type: table
layer: raw
location: s3://[REDACTED-BUCKET]/production/wise-app-backend/certificate_template
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:05:45+00:00'
sampled_rows: 0
---

# `backend.wise_app_backend__certificate_template`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` | from deserializer |
| `archived` | `string` | from deserializer |
| `htmltemplate` | `string` | from deserializer |
| `variables` | `string` | from deserializer |
| `previewimage` | `string` | from deserializer |
| `imagewidth` | `string` | from deserializer |
| `imageheight` | `string` | from deserializer |
| `__v` | `string` | from deserializer |
| `createdat` | `string` | from deserializer |
| `updatedat` | `string` | from deserializer |

## DDL

```sql
CREATE EXTERNAL TABLE `backend.wise_app_backend__certificate_template`(
  `_id` string COMMENT 'from deserializer', 
  `archived` string COMMENT 'from deserializer', 
  `htmltemplate` string COMMENT 'from deserializer', 
  `variables` string COMMENT 'from deserializer', 
  `previewimage` string COMMENT 'from deserializer', 
  `imagewidth` string COMMENT 'from deserializer', 
  `imageheight` string COMMENT 'from deserializer', 
  `__v` string COMMENT 'from deserializer', 
  `createdat` string COMMENT 'from deserializer', 
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
  's3://[REDACTED-BUCKET]/production/wise-app-backend/certificate_template'
TBLPROPERTIES (
  'compressionType'='gzip', 
  'transient_lastDdlTime'='1709549389')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
