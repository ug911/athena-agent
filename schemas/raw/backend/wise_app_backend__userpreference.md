---
database: backend
table: wise_app_backend__userpreference
type: table
layer: raw
location: s3://[REDACTED-BUCKET]/production/wise-app-backend/userPreference
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:09:34+00:00'
sampled_rows: 0
---

# `backend.wise_app_backend__userpreference`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` | from deserializer |
| `userid` | `string` | from deserializer |
| `__v` | `string` | from deserializer |
| `registration` | `string` | from deserializer |

## DDL

```sql
CREATE EXTERNAL TABLE `backend.wise_app_backend__userpreference`(
  `_id` string COMMENT 'from deserializer', 
  `userid` string COMMENT 'from deserializer', 
  `__v` string COMMENT 'from deserializer', 
  `registration` string COMMENT 'from deserializer')
ROW FORMAT SERDE 
  'org.openx.data.jsonserde.JsonSerDe' 
WITH SERDEPROPERTIES ( 
  'ignore.malformed.json'='true') 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.mapred.TextInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/production/wise-app-backend/userPreference'
TBLPROPERTIES (
  'compressionType'='gzip', 
  'transient_lastDdlTime'='1626548316')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
