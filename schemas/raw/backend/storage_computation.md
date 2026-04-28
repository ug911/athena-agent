---
database: backend
table: storage_computation
type: table
layer: raw
location: s3://[REDACTED-BUCKET]/storage_computation/date=2022-03-10
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:04:54+00:00'
sampled_rows: 0
---

# `backend.storage_computation`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `folder` | `string` |  |
| `bytes` | `bigint` |  |
| `objects` | `int` |  |
| `path` | `string` |  |
| `user_id` | `string` |  |

## DDL

```sql
CREATE EXTERNAL TABLE `backend.storage_computation`(
  `folder` string, 
  `bytes` bigint, 
  `objects` int, 
  `path` string, 
  `user_id` string)
ROW FORMAT DELIMITED 
  FIELDS TERMINATED BY ',' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.mapred.TextInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/storage_computation/date=2022-03-10'
TBLPROPERTIES (
  'has_encrypted_data'='false', 
  'transient_lastDdlTime'='1646939007')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
