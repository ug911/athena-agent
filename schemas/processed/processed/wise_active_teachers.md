---
canonical: processed
table: wise_active_teachers
type: table
layer: processed
regions:
  in: processed
  na: processed_na
location: s3://[REDACTED-BUCKET]/processed/wise_active_teachers/
format: INPUTFORMAT
partition_keys: []
schema_parity: identical
last_synced: '2026-08-11T13:20:33+00:00'
sampled_rows: 200
sampled_region: in
---

# `processed.wise_active_teachers`

## Region availability

| Region | Athena database |
| --- | --- |
| `IN` | `processed` |
| `NA` | `processed_na` |

_Schema parity: **identical** across regions._

## Columns (IN)

| Column | Type | Notes |
| --- | --- | --- |
| `ownerid` | `string` |  |
| `name` | `string` |  |
| `email` | `string` |  |
| `phonenumber` | `string` |  |
| `namespace` | `string` |  |
| `institutes` | `bigint` |  |
| `classes` | `bigint` |  |
| `students` | `bigint` |  |
| `teachers` | `bigint` |  |
| `active_teachers` | `bigint` |  |

## DDL

_From `IN` (processed)._

```sql
CREATE EXTERNAL TABLE `processed.wise_active_teachers`(
  `ownerid` string, 
  `name` string, 
  `email` string, 
  `phonenumber` string, 
  `namespace` string, 
  `institutes` bigint, 
  `classes` bigint, 
  `students` bigint, 
  `teachers` bigint, 
  `active_teachers` bigint)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/wise_active_teachers/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260811_021142_00097_zkjhx', 
  'trino_version'='0.215-24619-g93e00a8')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
