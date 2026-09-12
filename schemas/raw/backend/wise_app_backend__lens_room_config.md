---
canonical: backend
table: wise_app_backend__lens_room_config
type: table
layer: raw
regions:
  in: backend
  na: backend_na
location: s3://[REDACTED-BUCKET]/production/wise-app-backend/lens_room_config
format: INPUTFORMAT
partition_keys: []
schema_parity: identical
last_synced: '2026-08-11T13:09:13+00:00'
sampled_rows: 0
sampled_region: null
---

# `backend.wise_app_backend__lens_room_config`

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
| `classid` | `string` | from deserializer |
| `__v` | `string` | from deserializer |
| `createdat` | `string` | from deserializer |
| `polls` | `string` | from deserializer |
| `updatedat` | `string` | from deserializer |
| `feedbackconfig` | `string` | from deserializer |
| `leaderboardconfig` | `string` | from deserializer |
| `discussionconfig` | `string` | from deserializer |
| `allowzoomforhost` | `string` | from deserializer |
| `agendaids` | `string` | from deserializer |

## DDL

_From `IN` (backend)._

```sql
CREATE EXTERNAL TABLE `backend.wise_app_backend__lens_room_config`(
  `_id` string COMMENT 'from deserializer', 
  `classid` string COMMENT 'from deserializer', 
  `__v` string COMMENT 'from deserializer', 
  `createdat` string COMMENT 'from deserializer', 
  `polls` string COMMENT 'from deserializer', 
  `updatedat` string COMMENT 'from deserializer', 
  `feedbackconfig` string COMMENT 'from deserializer', 
  `leaderboardconfig` string COMMENT 'from deserializer', 
  `discussionconfig` string COMMENT 'from deserializer', 
  `allowzoomforhost` string COMMENT 'from deserializer', 
  `agendaids` string COMMENT 'from deserializer')
ROW FORMAT SERDE 
  'org.openx.data.jsonserde.JsonSerDe' 
WITH SERDEPROPERTIES ( 
  'ignore.malformed.json'='true') 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.mapred.TextInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/production/wise-app-backend/lens_room_config'
TBLPROPERTIES (
  'compressionType'='gzip', 
  'transient_lastDdlTime'='1709549815')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
