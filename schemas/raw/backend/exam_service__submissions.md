---
canonical: backend
table: exam_service__submissions
type: table
layer: raw
regions:
  in: backend
  na: backend_na
location: s3://[REDACTED-BUCKET]/production/exam-service/submissions
format: INPUTFORMAT
partition_keys: []
schema_parity: identical
last_synced: '2026-08-11T13:03:08+00:00'
sampled_rows: 0
sampled_region: null
---

# `backend.exam_service__submissions`

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
| `status` | `string` | from deserializer |
| `marks_obtained` | `string` | from deserializer |
| `test_id` | `string` | from deserializer |
| `user_id` | `string` | from deserializer |
| `user_name` | `string` | from deserializer |
| `answers` | `string` | from deserializer |
| `start_time` | `string` | from deserializer |
| `updated_at` | `string` | from deserializer |
| `created_at` | `string` | from deserializer |
| `end_time` | `string` | from deserializer |
| `rank` | `string` | from deserializer |

## DDL

_From `IN` (backend)._

```sql
CREATE EXTERNAL TABLE `backend.exam_service__submissions`(
  `_id` string COMMENT 'from deserializer', 
  `status` string COMMENT 'from deserializer', 
  `marks_obtained` string COMMENT 'from deserializer', 
  `test_id` string COMMENT 'from deserializer', 
  `user_id` string COMMENT 'from deserializer', 
  `user_name` string COMMENT 'from deserializer', 
  `answers` string COMMENT 'from deserializer', 
  `start_time` string COMMENT 'from deserializer', 
  `updated_at` string COMMENT 'from deserializer', 
  `created_at` string COMMENT 'from deserializer', 
  `end_time` string COMMENT 'from deserializer', 
  `rank` string COMMENT 'from deserializer')
ROW FORMAT SERDE 
  'org.openx.data.jsonserde.JsonSerDe' 
WITH SERDEPROPERTIES ( 
  'ignore.malformed.json'='true') 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.mapred.TextInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/production/exam-service/submissions'
TBLPROPERTIES (
  'compressionType'='gzip', 
  'transient_lastDdlTime'='1626529205')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
