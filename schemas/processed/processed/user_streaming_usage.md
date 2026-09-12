---
canonical: processed
table: user_streaming_usage
type: table
layer: processed
regions:
  in: processed
location: s3://[REDACTED-BUCKET]/processed/user_streaming_usage/process_date=2026-008-10/
format: INPUTFORMAT
partition_keys: []
schema_parity: identical
last_synced: '2026-08-11T13:19:23+00:00'
sampled_rows: 200
sampled_region: in
---

# `processed.user_streaming_usage`

## Region availability

| Region | Athena database |
| --- | --- |
| `IN` | `processed` |

_Only present in **IN**._

## Columns (IN)

| Column | Type | Notes |
| --- | --- | --- |
| `userid` | `string` |  |
| `dt` | `string` |  |
| `mbs used in watching videos` | `double` |  |
| `mbs used in downloading videos by admin` | `double` |  |
| `mbs used in students viewing embedded content` | `double` |  |
| `mbs used in viewing pdfs or resources` | `double` |  |

## Enum-like columns

_String columns with ≤20 distinct values in 200 sampled rows from `IN`. Distribution shown as `value (×count)`._

- `userid`: `679f1cf14ddebe41d57ba708 (×99)`, `6799aad0b6ecf218cb8980ba (×88)`, `679e4523ca4ec636aac1d588 (×3)`, `6799db5d429f370dfd793279 (×2)`, `679b65746c1071462ca3daf0 (×2)`, `6799d904441065473076b889 (×1)`, `6799db8e634099271bf2c791 (×1)`, `679a111e93cb7d34368e70e4 (×1)`, `679a53a36fcbccc9a6e68737 (×1)`, `679a5f6740f7d229bf0882dc (×1)`, `679a5f6740f7d22bba0882d7 (×1)`

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
  's3://[REDACTED-BUCKET]/processed/user_streaming_usage/process_date=2026-008-10/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260811_021058_00007_563dc', 
  'trino_version'='0.215-24619-g93e00a8')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
