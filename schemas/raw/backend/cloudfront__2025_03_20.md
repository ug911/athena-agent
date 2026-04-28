---
database: backend
table: cloudfront__2025_03_20
type: table
layer: raw
location: s3://[REDACTED-BUCKET]/cloudfront-logs/dt=2025-03-20
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:04:15+00:00'
sampled_rows: 0
---

# `backend.cloudfront__2025_03_20`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `date` | `date` |  |
| `time` | `string` |  |
| `location` | `string` |  |
| `bytes` | `bigint` |  |
| `request_ip` | `string` |  |
| `method` | `string` |  |
| `host` | `string` |  |
| `uri` | `string` |  |
| `status` | `int` |  |
| `referrer` | `string` |  |
| `user_agent` | `string` |  |
| `query_string` | `string` |  |
| `cookie` | `string` |  |
| `result_type` | `string` |  |
| `request_id` | `string` |  |
| `host_header` | `string` |  |
| `request_protocol` | `string` |  |
| `request_bytes` | `bigint` |  |
| `time_taken` | `float` |  |
| `xforwarded_for` | `string` |  |
| `ssl_protocol` | `string` |  |
| `ssl_cipher` | `string` |  |
| `response_result_type` | `string` |  |
| `http_version` | `string` |  |
| `fle_status` | `string` |  |
| `fle_encrypted_fields` | `int` |  |
| `c_port` | `int` |  |
| `time_to_first_byte` | `float` |  |
| `x_edge_detailed_result_type` | `string` |  |
| `sc_content_type` | `string` |  |
| `sc_content_len` | `bigint` |  |
| `sc_range_start` | `bigint` |  |
| `sc_range_end` | `bigint` |  |

## DDL

```sql
CREATE EXTERNAL TABLE `backend.cloudfront__2025_03_20`(
  `date` date, 
  `time` string, 
  `location` string, 
  `bytes` bigint, 
  `request_ip` string, 
  `method` string, 
  `host` string, 
  `uri` string, 
  `status` int, 
  `referrer` string, 
  `user_agent` string, 
  `query_string` string, 
  `cookie` string, 
  `result_type` string, 
  `request_id` string, 
  `host_header` string, 
  `request_protocol` string, 
  `request_bytes` bigint, 
  `time_taken` float, 
  `xforwarded_for` string, 
  `ssl_protocol` string, 
  `ssl_cipher` string, 
  `response_result_type` string, 
  `http_version` string, 
  `fle_status` string, 
  `fle_encrypted_fields` int, 
  `c_port` int, 
  `time_to_first_byte` float, 
  `x_edge_detailed_result_type` string, 
  `sc_content_type` string, 
  `sc_content_len` bigint, 
  `sc_range_start` bigint, 
  `sc_range_end` bigint)
ROW FORMAT DELIMITED 
  FIELDS TERMINATED BY '\t' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.mapred.TextInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/cloudfront-logs/dt=2025-03-20'
TBLPROPERTIES (
  'skip.header.line.count'='2', 
  'transient_lastDdlTime'='1742561333')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
