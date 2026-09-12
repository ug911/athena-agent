---
canonical: backend
table: wise_app_backend__classparticipant
type: table
layer: raw
regions:
  in: backend
  na: backend_na
location: s3://[REDACTED-BUCKET]/production/wise-app-backend/classparticipant
format: INPUTFORMAT
partition_keys: []
schema_parity: identical
last_synced: '2026-08-11T13:06:12+00:00'
sampled_rows: 0
sampled_region: null
---

# `backend.wise_app_backend__classparticipant`

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
| `userid` | `string` | from deserializer |
| `classid` | `string` | from deserializer |
| `relation` | `string` | from deserializer |
| `status` | `string` | from deserializer |
| `createdat` | `string` | from deserializer |
| `updatedat` | `string` | from deserializer |
| `__v` | `string` | from deserializer |
| `joinedon` | `string` | from deserializer |

## DDL

_From `IN` (backend)._

```sql
CREATE EXTERNAL TABLE `backend.wise_app_backend__classparticipant`(
  `_id` string COMMENT 'from deserializer', 
  `userid` string COMMENT 'from deserializer', 
  `classid` string COMMENT 'from deserializer', 
  `relation` string COMMENT 'from deserializer', 
  `status` string COMMENT 'from deserializer', 
  `createdat` string COMMENT 'from deserializer', 
  `updatedat` string COMMENT 'from deserializer', 
  `__v` string COMMENT 'from deserializer', 
  `joinedon` string COMMENT 'from deserializer')
ROW FORMAT SERDE 
  'org.openx.data.jsonserde.JsonSerDe' 
WITH SERDEPROPERTIES ( 
  'ignore.malformed.json'='true') 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.mapred.TextInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/production/wise-app-backend/classparticipant'
TBLPROPERTIES (
  'compressionType'='gzip', 
  'transient_lastDdlTime'='1641897443')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
