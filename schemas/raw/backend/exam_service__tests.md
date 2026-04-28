---
database: backend
table: exam_service__tests
type: table
layer: raw
location: s3://[REDACTED-BUCKET]/production/exam-service/tests
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:04:24+00:00'
sampled_rows: 0
---

# `backend.exam_service__tests`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` | from deserializer |
| `active` | `string` | from deserializer |
| `display_results` | `string` | from deserializer |
| `status` | `string` | from deserializer |
| `_type` | `string` | from deserializer |
| `name` | `string` | from deserializer |
| `class_id` | `string` | from deserializer |
| `user_id` | `string` | from deserializer |
| `jumbled_questions` | `string` | from deserializer |
| `mock_test` | `string` | from deserializer |
| `disable_commenting` | `string` | from deserializer |
| `updated_at` | `string` | from deserializer |
| `created_at` | `string` | from deserializer |
| `test_question` | `string` | from deserializer |
| `answers` | `string` | from deserializer |
| `question_count` | `string` | from deserializer |
| `correct_marks` | `string` | from deserializer |
| `description` | `string` | from deserializer |
| `duration` | `string` | from deserializer |
| `end_time` | `string` | from deserializer |
| `incorrect_marks` | `string` | from deserializer |
| `max_marks` | `string` | from deserializer |
| `start_time` | `string` | from deserializer |
| `analysis` | `string` | from deserializer |
| `total_present` | `string` | from deserializer |
| `questions` | `string` | from deserializer |
| `publish_results` | `string` | from deserializer |

## DDL

```sql
CREATE EXTERNAL TABLE `backend.exam_service__tests`(
  `_id` string COMMENT 'from deserializer', 
  `active` string COMMENT 'from deserializer', 
  `display_results` string COMMENT 'from deserializer', 
  `status` string COMMENT 'from deserializer', 
  `_type` string COMMENT 'from deserializer', 
  `name` string COMMENT 'from deserializer', 
  `class_id` string COMMENT 'from deserializer', 
  `user_id` string COMMENT 'from deserializer', 
  `jumbled_questions` string COMMENT 'from deserializer', 
  `mock_test` string COMMENT 'from deserializer', 
  `disable_commenting` string COMMENT 'from deserializer', 
  `updated_at` string COMMENT 'from deserializer', 
  `created_at` string COMMENT 'from deserializer', 
  `test_question` string COMMENT 'from deserializer', 
  `answers` string COMMENT 'from deserializer', 
  `question_count` string COMMENT 'from deserializer', 
  `correct_marks` string COMMENT 'from deserializer', 
  `description` string COMMENT 'from deserializer', 
  `duration` string COMMENT 'from deserializer', 
  `end_time` string COMMENT 'from deserializer', 
  `incorrect_marks` string COMMENT 'from deserializer', 
  `max_marks` string COMMENT 'from deserializer', 
  `start_time` string COMMENT 'from deserializer', 
  `analysis` string COMMENT 'from deserializer', 
  `total_present` string COMMENT 'from deserializer', 
  `questions` string COMMENT 'from deserializer', 
  `publish_results` string COMMENT 'from deserializer')
ROW FORMAT SERDE 
  'org.openx.data.jsonserde.JsonSerDe' 
WITH SERDEPROPERTIES ( 
  'ignore.malformed.json'='true') 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.mapred.TextInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/production/exam-service/tests'
TBLPROPERTIES (
  'compressionType'='gzip', 
  'transient_lastDdlTime'='1626548215')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
