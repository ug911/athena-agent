---
canonical: backend
table: wise_app_backend__institute_participants_2
type: table
layer: raw
regions:
  in: backend
location: s3://[REDACTED-BUCKET]/production/wise-app-backend/InstituteParticipant
format: INPUTFORMAT
partition_keys: []
schema_parity: identical
last_synced: '2026-08-11T13:08:17+00:00'
sampled_rows: 0
sampled_region: null
---

# `backend.wise_app_backend__institute_participants_2`

## Region availability

| Region | Athena database |
| --- | --- |
| `IN` | `backend` |

_Only present in **IN**._

## Columns (IN)

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` | from deserializer |
| `userid` | `string` | from deserializer |
| `instituteid` | `string` | from deserializer |
| `status` | `string` | from deserializer |
| `createdat` | `string` | from deserializer |
| `updatedat` | `string` | from deserializer |
| `joinedon` | `string` | from deserializer |
| `relation` | `string` | from deserializer |

## DDL


```sql
CREATE EXTERNAL TABLE `backend.wise_app_backend__institute_participants_2`(
  `_id` string COMMENT 'from deserializer', 
  `userid` string COMMENT 'from deserializer', 
  `instituteid` string COMMENT 'from deserializer', 
  `status` string COMMENT 'from deserializer', 
  `createdat` string COMMENT 'from deserializer', 
  `updatedat` string COMMENT 'from deserializer', 
  `joinedon` string COMMENT 'from deserializer', 
  `relation` string COMMENT 'from deserializer')
ROW FORMAT SERDE 
  'org.openx.data.jsonserde.JsonSerDe' 
WITH SERDEPROPERTIES ( 
  'ignore.malformed.json'='true') 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.mapred.TextInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/production/wise-app-backend/InstituteParticipant'
TBLPROPERTIES (
  'compressionType'='gzip', 
  'transient_lastDdlTime'='1732601053')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
