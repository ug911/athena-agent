---
canonical: processed
table: wise_user_stats
type: table
layer: processed
regions:
  in: processed
  na: processed_na
location: s3://[REDACTED-BUCKET]/processed/wise_user_stats/
format: INPUTFORMAT
partition_keys: []
schema_parity: identical
last_synced: '2026-08-11T13:31:23+00:00'
sampled_rows: 200
sampled_region: in
---

# `processed.wise_user_stats`

## Region availability

| Region | Athena database |
| --- | --- |
| `IN` | `processed` |
| `NA` | `processed_na` |

_Schema parity: **identical** across regions._

## Columns (IN)

| Column | Type | Notes |
| --- | --- | --- |
| `owner id` | `string` |  |
| `owner name` | `string` |  |
| `owner email` | `string` |  |
| `owner phone` | `string` |  |
| `owner namespace` | `string` |  |
| `total institutes` | `bigint` |  |
| `enrolled teachers` | `bigint` |  |
| `enrolled students` | `bigint` |  |
| `active teachers` | `bigint` |  |
| `active students` | `bigint` |  |
| `premium expiry` | `date` |  |
| `does owner use their own zoom?` | `string` |  |
| `churn status` | `varchar(37)` |  |
| `meeting in last 7` | `bigint` |  |
| `meeting in last 8 to 14` | `bigint` |  |
| `max meetings in week` | `bigint` |  |
| `avg meetings in week` | `int` |  |
| `last meeting was how many weeks back?` | `int` |  |
| `meeting minutes in last 30` | `int` |  |
| `meeting minutes in last 31 to 60` | `int` |  |
| `meeting minutes in last 61 to 90` | `int` |  |
| `meeting in last 30` | `bigint` |  |
| `meeting in last last 31 to 60` | `bigint` |  |
| `meeting in last last 61 to 90` | `bigint` |  |
| `meeting in last 90` | `bigint` |  |
| `number of weeks with meetings in last 14 weeks` | `bigint` |  |

## Enum-like columns

_String columns with ≤20 distinct values in 200 sampled rows from `IN`. Distribution shown as `value (×count)`._

- `does owner use their own zoom?`: `false (×192)`, `true (×7)`
- `churn status`: `VERY HIGH (No meetings for > 2 weeks) (×7)`, `VERY HIGH (Meetings dropped to < 10%) (×4)`, `MEDIUM (Meetings dropped to < 50%) (×4)`

## DDL

_From `IN` (processed)._

```sql
CREATE EXTERNAL TABLE `processed.wise_user_stats`(
  `owner id` string, 
  `owner name` string, 
  `owner email` string, 
  `owner phone` string, 
  `owner namespace` string, 
  `total institutes` bigint, 
  `enrolled teachers` bigint, 
  `enrolled students` bigint, 
  `active teachers` bigint, 
  `active students` bigint, 
  `premium expiry` date, 
  `does owner use their own zoom?` string, 
  `churn status` varchar(37), 
  `meeting in last 7` bigint, 
  `meeting in last 8 to 14` bigint, 
  `max meetings in week` bigint, 
  `avg meetings in week` int, 
  `last meeting was how many weeks back?` int, 
  `meeting minutes in last 30` int, 
  `meeting minutes in last 31 to 60` int, 
  `meeting minutes in last 61 to 90` int, 
  `meeting in last 30` bigint, 
  `meeting in last last 31 to 60` bigint, 
  `meeting in last last 61 to 90` bigint, 
  `meeting in last 90` bigint, 
  `number of weeks with meetings in last 14 weeks` bigint)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/wise_user_stats/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260811_021237_00142_yrqt7', 
  'trino_version'='0.215-24619-g93e00a8')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
