---
database: processed
table: user_streaming_usage
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/processed/user_streaming_usage/process_date=2026-004-27/
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:13:03+00:00'
sampled_rows: 200
---

# `processed.user_streaming_usage`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `userid` | `string` |  |
| `dt` | `string` |  |
| `mbs used in watching videos` | `double` |  |
| `mbs used in downloading videos by admin` | `double` |  |
| `mbs used in students viewing embedded content` | `double` |  |
| `mbs used in viewing pdfs or resources` | `double` |  |

## Enum-like columns

_String columns with ≤20 distinct values in 200 sampled rows. Distribution shown as `value (×count)`._

- `userid`: `maint (×200)`

## DDL

```sql
CREATE EXTERNAL TABLE `processed.user_streaming_usage`(
  `userid` string, 
  `dt` string, 
  `mbs used in watching videos` double, 
  `mbs used in downloading videos by admin` double, 
  `mbs used in students viewing embedded content` double, 
  `mbs used in viewing pdfs or resources` double)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/user_streaming_usage/process_date=2026-004-27/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260428_015522_00124_tdb7m', 
  'trino_version'='0.215-24582-g0575ac4')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
