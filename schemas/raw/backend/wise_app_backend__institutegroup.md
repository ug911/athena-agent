---
canonical: backend
table: wise_app_backend__institutegroup
type: table
layer: raw
regions:
  in: backend
  na: backend_na
location: s3://[REDACTED-BUCKET]/production/wise-app-backend/InstituteGroup
format: INPUTFORMAT
partition_keys: []
schema_parity: identical
last_synced: '2026-08-11T13:08:35+00:00'
sampled_rows: 0
sampled_region: null
---

# `backend.wise_app_backend__institutegroup`

## Region availability

| Region | Athena database |
| --- | --- |
| `IN` | `backend` |
| `NA` | `backend_na` |

_Schema parity: **identical** across regions._

## Columns (IN)

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` | from deserializer |
| `createdat` | `string` | from deserializer |
| `updatedat` | `string` | from deserializer |
| `name` | `string` | from deserializer |
| `type` | `string` | from deserializer |
| `instituteid` | `string` | from deserializer |

## DDL

_From `IN` (backend)._

```sql
CREATE EXTERNAL TABLE `backend.wise_app_backend__institutegroup`(
  `_id` string COMMENT 'from deserializer', 
  `createdat` string COMMENT 'from deserializer', 
  `updatedat` string COMMENT 'from deserializer', 
  `name` string COMMENT 'from deserializer', 
  `type` string COMMENT 'from deserializer', 
  `instituteid` string COMMENT 'from deserializer')
ROW FORMAT SERDE 
  'org.openx.data.jsonserde.JsonSerDe' 
WITH SERDEPROPERTIES ( 
  'ignore.malformed.json'='true') 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.mapred.TextInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/production/wise-app-backend/InstituteGroup'
TBLPROPERTIES (
  'compressionType'='gzip', 
  'transient_lastDdlTime'='1743015786')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
