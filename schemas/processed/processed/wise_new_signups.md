---
database: processed
table: wise_new_signups
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/processed/wise_new_signups/
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:18:21+00:00'
sampled_rows: 200
---

# `processed.wise_new_signups`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `userid` | `string` |  |
| `name` | `string` |  |
| `email` | `string` |  |
| `phonenumber` | `string` |  |
| `namespace` | `string` |  |
| `createdat` | `date` |  |
| `classes` | `bigint` |  |
| `teachers` | `bigint` |  |
| `students` | `bigint` |  |

## DDL

```sql
CREATE EXTERNAL TABLE `processed.wise_new_signups`(
  `userid` string, 
  `name` string, 
  `email` string, 
  `phonenumber` string, 
  `namespace` string, 
  `createdat` date, 
  `classes` bigint, 
  `teachers` bigint, 
  `students` bigint)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/wise_new_signups/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260428_015627_00043_ainc2', 
  'trino_version'='0.215-24582-g0575ac4')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
