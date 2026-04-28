---
database: backend
table: wise_app_backend__zoom
type: table
layer: raw
location: s3://[REDACTED-BUCKET]/production/wise-app-backend/zoom
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:09:56+00:00'
sampled_rows: 0
---

# `backend.wise_app_backend__zoom`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` | from deserializer |
| `attendancerecorded` | `string` | from deserializer |
| `mettingended` | `string` | from deserializer |
| `webhookreceived` | `string` | from deserializer |
| `licensed` | `string` | from deserializer |
| `disablecommenting` | `string` | from deserializer |
| `mettingid` | `string` | from deserializer |
| `start_url` | `string` | from deserializer |
| `join_url` | `string` | from deserializer |
| `classid` | `string` | from deserializer |
| `userid` | `string` | from deserializer |
| `meetinguuid` | `string` | from deserializer |
| `start_time` | `string` | from deserializer |
| `participants` | `string` | from deserializer |
| `comments` | `string` | from deserializer |
| `createdat` | `string` | from deserializer |
| `updatedat` | `string` | from deserializer |
| `__v` | `string` | from deserializer |
| `timezone` | `string` | from deserializer |
| `duration` | `string` | from deserializer |
| `end_time` | `string` | from deserializer |
| `scheduledstarttime` | `string` | from deserializer |
| `scheduledendtime` | `string` | from deserializer |
| `participant` | `string` | from deserializer |
| `maxparticipantduration` | `string` | from deserializer |
| `metadata` | `string` | from deserializer |
| `meetingstarted` | `string` | from deserializer |
| `archived` | `string` | from deserializer |
| `type` | `string` | from deserializer |
| `meetingstatus` | `string` | from deserializer |
| `title` | `string` | from deserializer |
| `password` | `string` | from deserializer |
| `recordings` | `string` | from deserializer |
| `rawrecordings` | `string` | from deserializer |
| `recordingshared` | `string` | from deserializer |
| `location` | `string` | from deserializer |

## DDL

```sql
CREATE EXTERNAL TABLE `backend.wise_app_backend__zoom`(
  `_id` string COMMENT 'from deserializer', 
  `attendancerecorded` string COMMENT 'from deserializer', 
  `mettingended` string COMMENT 'from deserializer', 
  `webhookreceived` string COMMENT 'from deserializer', 
  `licensed` string COMMENT 'from deserializer', 
  `disablecommenting` string COMMENT 'from deserializer', 
  `mettingid` string COMMENT 'from deserializer', 
  `start_url` string COMMENT 'from deserializer', 
  `join_url` string COMMENT 'from deserializer', 
  `classid` string COMMENT 'from deserializer', 
  `userid` string COMMENT 'from deserializer', 
  `meetinguuid` string COMMENT 'from deserializer', 
  `start_time` string COMMENT 'from deserializer', 
  `participants` string COMMENT 'from deserializer', 
  `comments` string COMMENT 'from deserializer', 
  `createdat` string COMMENT 'from deserializer', 
  `updatedat` string COMMENT 'from deserializer', 
  `__v` string COMMENT 'from deserializer', 
  `timezone` string COMMENT 'from deserializer', 
  `duration` string COMMENT 'from deserializer', 
  `end_time` string COMMENT 'from deserializer', 
  `scheduledstarttime` string COMMENT 'from deserializer', 
  `scheduledendtime` string COMMENT 'from deserializer', 
  `participant` string COMMENT 'from deserializer', 
  `maxparticipantduration` string COMMENT 'from deserializer', 
  `metadata` string COMMENT 'from deserializer', 
  `meetingstarted` string COMMENT 'from deserializer', 
  `archived` string COMMENT 'from deserializer', 
  `type` string COMMENT 'from deserializer', 
  `meetingstatus` string COMMENT 'from deserializer', 
  `title` string COMMENT 'from deserializer', 
  `password` string COMMENT 'from deserializer', 
  `recordings` string COMMENT 'from deserializer', 
  `rawrecordings` string COMMENT 'from deserializer', 
  `recordingshared` string COMMENT 'from deserializer', 
  `location` string COMMENT 'from deserializer')
ROW FORMAT SERDE 
  'org.openx.data.jsonserde.JsonSerDe' 
WITH SERDEPROPERTIES ( 
  'ignore.malformed.json'='true') 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.mapred.TextInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/production/wise-app-backend/zoom'
TBLPROPERTIES (
  'compressionType'='gzip', 
  'transient_lastDdlTime'='1770275797')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
