---
database: processed
table: mat_zoomers
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/processed/materialized/zoomers/process_date=2021-08-11_v2/
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:11:38+00:00'
sampled_rows: 0
---

# `processed.mat_zoomers`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `userid` | `string` |  |
| `zoom_id` | `string` |  |
| `classid` | `string` |  |
| `attendancerecorded` | `string` |  |
| `mettingended` | `string` |  |
| `duration` | `int` |  |
| `start_time` | `string` |  |
| `end_time` | `string` |  |
| `createdat` | `string` |  |
| `updatedat` | `string` |  |
| `start_time_date` | `date` |  |
| `end_time_date` | `date` |  |
| `createdat_date` | `date` |  |
| `updatedat_date` | `date` |  |
| `maxparticipantduration` | `string` |  |
| `participants` | `bigint` |  |

## DDL

```sql
CREATE EXTERNAL TABLE `processed.mat_zoomers`(
  `userid` string COMMENT '', 
  `zoom_id` string COMMENT '', 
  `classid` string COMMENT '', 
  `attendancerecorded` string COMMENT '', 
  `mettingended` string COMMENT '', 
  `duration` int COMMENT '', 
  `start_time` string COMMENT '', 
  `end_time` string COMMENT '', 
  `createdat` string COMMENT '', 
  `updatedat` string COMMENT '', 
  `start_time_date` date COMMENT '', 
  `end_time_date` date COMMENT '', 
  `createdat_date` date COMMENT '', 
  `updatedat_date` date COMMENT '', 
  `maxparticipantduration` string COMMENT '', 
  `participants` bigint COMMENT '')
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/materialized/zoomers/process_date=2021-08-11_v2/'
TBLPROPERTIES (
  'has_encrypted_data'='false', 
  'presto_query_id'='20210812_085314_00063_4nt66')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
