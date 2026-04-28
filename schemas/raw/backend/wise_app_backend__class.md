---
database: backend
table: wise_app_backend__class
type: table
layer: raw
location: s3://[REDACTED-BUCKET]/production/wise-app-backend/class
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:05:59+00:00'
sampled_rows: 0
---

# `backend.wise_app_backend__class`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` | from deserializer |
| `namespace` | `string` | from deserializer |
| `zoomlink` | `string` | from deserializer |
| `pendingadmins` | `string` | from deserializer |
| `admins` | `string` | from deserializer |
| `pendingrequest` | `string` | from deserializer |
| `joinedrequest` | `string` | from deserializer |
| `coteacherrequests` | `string` | from deserializer |
| `coteachers` | `string` | from deserializer |
| `archived` | `string` | from deserializer |
| `disablereminder` | `string` | from deserializer |
| `lockclassroom` | `string` | from deserializer |
| `subject` | `string` | from deserializer |
| `timing` | `string` | from deserializer |
| `userid` | `string` | from deserializer |
| `name` | `string` | from deserializer |
| `classnumber` | `string` | from deserializer |
| `timingversion` | `string` | from deserializer |
| `schedule` | `string` | from deserializer |
| `settings` | `string` | from deserializer |
| `oldschedules` | `string` | from deserializer |
| `createdat` | `string` | from deserializer |
| `deletedstudents` | `string` | from deserializer |
| `suspendedstudents` | `string` | from deserializer |
| `instituteid` | `string` | from deserializer |
| `__v` | `string` | from deserializer |

## DDL

```sql
CREATE EXTERNAL TABLE `backend.wise_app_backend__class`(
  `_id` string COMMENT 'from deserializer', 
  `namespace` string COMMENT 'from deserializer', 
  `zoomlink` string COMMENT 'from deserializer', 
  `pendingadmins` string COMMENT 'from deserializer', 
  `admins` string COMMENT 'from deserializer', 
  `pendingrequest` string COMMENT 'from deserializer', 
  `joinedrequest` string COMMENT 'from deserializer', 
  `coteacherrequests` string COMMENT 'from deserializer', 
  `coteachers` string COMMENT 'from deserializer', 
  `archived` string COMMENT 'from deserializer', 
  `disablereminder` string COMMENT 'from deserializer', 
  `lockclassroom` string COMMENT 'from deserializer', 
  `subject` string COMMENT 'from deserializer', 
  `timing` string COMMENT 'from deserializer', 
  `userid` string COMMENT 'from deserializer', 
  `name` string COMMENT 'from deserializer', 
  `classnumber` string COMMENT 'from deserializer', 
  `timingversion` string COMMENT 'from deserializer', 
  `schedule` string COMMENT 'from deserializer', 
  `settings` string COMMENT 'from deserializer', 
  `oldschedules` string COMMENT 'from deserializer', 
  `createdat` string COMMENT 'from deserializer', 
  `deletedstudents` string COMMENT 'from deserializer', 
  `suspendedstudents` string COMMENT 'from deserializer', 
  `instituteid` string COMMENT 'from deserializer', 
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
  's3://[REDACTED-BUCKET]/production/wise-app-backend/class'
TBLPROPERTIES (
  'compressionType'='gzip', 
  'transient_lastDdlTime'='1661434151')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
