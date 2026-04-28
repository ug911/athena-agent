---
database: processed
table: streaming_computation
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/production/streaming_computation/dt=2022-03-13/
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:12:23+00:00'
sampled_rows: 0
---

# `processed.streaming_computation`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `dt` | `string` |  |
| `userid` | `string` |  |
| `bytes_mbs` | `double` |  |
| `unique_request_ips` | `bigint` |  |
| `top_uris` | `array<array<string>>` |  |

## DDL

```sql
CREATE EXTERNAL TABLE `processed.streaming_computation`(
  `dt` string COMMENT '', 
  `userid` string COMMENT '', 
  `bytes_mbs` double COMMENT '', 
  `unique_request_ips` bigint COMMENT '', 
  `top_uris` array<array<string>> COMMENT '')
CLUSTERED BY ( 
  dt) 
INTO 1 BUCKETS
ROW FORMAT DELIMITED 
  FIELDS TERMINATED BY ',' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.mapred.TextInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/production/streaming_computation/dt=2022-03-13/'
TBLPROPERTIES (
  'bucketing_format'='hive', 
  'bucketing_version'='1', 
  'has_encrypted_data'='false', 
  'presto_query_id'='20220314_193321_00025_tfkk9', 
  'write.compression'='GZIP')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
