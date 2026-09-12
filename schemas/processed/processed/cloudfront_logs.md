---
canonical: processed
table: cloudfront_logs
type: table
layer: processed
regions:
  in: processed
location: s3://[REDACTED-BUCKET]/production/cloudfront-logs
format: INPUTFORMAT
partition_keys:
- dt
schema_parity: identical
last_synced: '2026-08-11T13:14:58+00:00'
sampled_rows: 200
sampled_region: in
---

# `processed.cloudfront_logs`

## Region availability

| Region | Athena database |
| --- | --- |
| `IN` | `processed` |

_Only present in **IN**._

## Columns (IN)

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
| `dt` | `string` |  |

**Partition keys:** `dt`

## Enum-like columns

_String columns with ≤20 distinct values in 200 sampled rows from `IN`. Distribution shown as `value (×count)`._

- `location`: `CCU50-P1 (×52)`, `MAA50-P2 (×39)`, `DEL54-P4 (×37)`, `BLR50-C3 (×34)`, `HYD50-C2 (×26)`, `BOM78-P6 (×8)`, `PNQ50-P1 (×3)`, `BOM78-P4 (×1)`
- `method`: `GET (×200)`
- `host`: `d1qt34njyktlf8.cloudfront.net (×200)`
- `referrer`: `- (×200)`
- `query_string`: `- (×148)`, `token=[REDACTED-JWT] (×52)`
- `cookie`: `- (×200)`
- `result_type`: `Miss (×158)`, `Hit (×36)`, `RefreshHit (×4)`, `Error (×2)`
- `host_header`: `streaming.wiseapp.live (×200)`
- `request_protocol`: `https (×200)`
- `xforwarded_for`: `- (×200)`
- `ssl_protocol`: `TLSv1.3 (×174)`, `TLSv1.2 (×26)`
- `ssl_cipher`: `TLS_AES_128_GCM_SHA256 (×174)`, `ECDHE-RSA-AES128-GCM-SHA256 (×26)`
- `response_result_type`: `Miss (×160)`, `Hit (×36)`, `RefreshHit (×4)`
- `http_version`: `HTTP/1.1 (×115)`, `HTTP/2.0 (×85)`
- `fle_status`: `- (×200)`
- `x_edge_detailed_result_type`: `Miss (×158)`, `Hit (×36)`, `RefreshHit (×4)`, `ClientCommError (×2)`
- `sc_content_type`: `application/octet-stream (×200)`
- `dt`: `2023-07-10 (×192)`, `2022-12-30 (×7)`, `2022-07-15 (×1)`

## DDL


```sql
CREATE EXTERNAL TABLE `processed.cloudfront_logs`(
  `date` date COMMENT '', 
  `time` string COMMENT '', 
  `location` string COMMENT '', 
  `bytes` bigint COMMENT '', 
  `request_ip` string COMMENT '', 
  `method` string COMMENT '', 
  `host` string COMMENT '', 
  `uri` string COMMENT '', 
  `status` int COMMENT '', 
  `referrer` string COMMENT '', 
  `user_agent` string COMMENT '', 
  `query_string` string COMMENT '', 
  `cookie` string COMMENT '', 
  `result_type` string COMMENT '', 
  `request_id` string COMMENT '', 
  `host_header` string COMMENT '', 
  `request_protocol` string COMMENT '', 
  `request_bytes` bigint COMMENT '', 
  `time_taken` float COMMENT '', 
  `xforwarded_for` string COMMENT '', 
  `ssl_protocol` string COMMENT '', 
  `ssl_cipher` string COMMENT '', 
  `response_result_type` string COMMENT '', 
  `http_version` string COMMENT '', 
  `fle_status` string COMMENT '', 
  `fle_encrypted_fields` int COMMENT '', 
  `c_port` int COMMENT '', 
  `time_to_first_byte` float COMMENT '', 
  `x_edge_detailed_result_type` string COMMENT '', 
  `sc_content_type` string COMMENT '', 
  `sc_content_len` bigint COMMENT '', 
  `sc_range_start` bigint COMMENT '', 
  `sc_range_end` bigint COMMENT '')
PARTITIONED BY ( 
  `dt` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/production/cloudfront-logs'
TBLPROPERTIES (
  'has_encrypted_data'='false', 
  'parquet.compression'='GZIP', 
  'presto_query_id'='20220116_172839_00068_x7w8r', 
  'transient_lastDdlTime'='1642354210')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
