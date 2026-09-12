---
canonical: backend
table: wise_app_backend__liveclassinsight
type: table
layer: raw
regions:
  in: backend
  na: backend_na
location: s3://[REDACTED-BUCKET]/production/wise-app-backend/liveclassinsight
format: INPUTFORMAT
partition_keys: []
schema_parity: identical
last_synced: '2026-08-11T13:09:47+00:00'
sampled_rows: 0
sampled_region: null
---

# `backend.wise_app_backend__liveclassinsight`

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
| `meetingid` | `string` | from deserializer |
| `meetingpassword` | `string` | from deserializer |
| `meetinguuid` | `string` | from deserializer |
| `createdat` | `string` | from deserializer |
| `updatedat` | `string` | from deserializer |
| `starttime` | `string` | from deserializer |
| `endtime` | `string` | from deserializer |
| `sessionid` | `string` | from deserializer |
| `userid` | `string` | from deserializer |
| `userratings` | `string` | from deserializer |
| `participants` | `string` | from deserializer |
| `__v` | `string` | from deserializer |

## DDL

_From `IN` (backend)._

```sql
CREATE EXTERNAL TABLE `backend.wise_app_backend__liveclassinsight`(
  `_id` string COMMENT 'from deserializer', 
  `meetingid` string COMMENT 'from deserializer', 
  `meetingpassword` string COMMENT 'from deserializer', 
  `meetinguuid` string COMMENT 'from deserializer', 
  `createdat` string COMMENT 'from deserializer', 
  `updatedat` string COMMENT 'from deserializer', 
  `starttime` string COMMENT 'from deserializer', 
  `endtime` string COMMENT 'from deserializer', 
  `sessionid` string COMMENT 'from deserializer', 
  `userid` string COMMENT 'from deserializer', 
  `userratings` string COMMENT 'from deserializer', 
  `participants` string COMMENT 'from deserializer', 
  `__v` string COMMENT 'from deserializer')
ROW FORMAT SERDE 
  'org.openx.data.jsonserde.JsonSerDe' 
WITH SERDEPROPERTIES ( 
  'ignore.malformed.json'='true') 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.mapred.TextInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/production/wise-app-backend/liveclassinsight'
TBLPROPERTIES (
  'compressionType'='gzip', 
  'transient_lastDdlTime'='1680254133')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
