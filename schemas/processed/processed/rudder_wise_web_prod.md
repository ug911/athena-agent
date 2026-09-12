---
canonical: processed
table: rudder_wise_web_prod
type: table
layer: processed
regions:
  in: processed
location: s3://[REDACTED-BUCKET]/processed/rudder_lens
format: INPUTFORMAT
partition_keys:
- dt
schema_parity: identical
last_synced: '2026-08-11T13:18:03+00:00'
sampled_rows: 200
sampled_region: in
---

# `processed.rudder_wise_web_prod`

## Region availability

| Region | Athena database |
| --- | --- |
| `IN` | `processed` |

_Only present in **IN**._

## Columns (IN)

| Column | Type | Notes |
| --- | --- | --- |
| `type` | `string` |  |
| `event` | `string` |  |
| `sentat` | `string` |  |
| `channel` | `string` |  |
| `rudderid` | `string` |  |
| `messageid` | `string` |  |
| `timestamp` | `string` |  |
| `context_app_version` | `string` |  |
| `context_app_build` | `string` |  |
| `context_traits_wise_id` | `string` |  |
| `context_traits_phone` | `string` |  |
| `context_os_name` | `string` |  |
| `context_os_version` | `string` |  |
| `context_device_type` | `string` |  |
| `context_device_manufacturer` | `string` |  |
| `context_device_model` | `string` |  |
| `context_network_wifi` | `string` |  |
| `context_network_carrier` | `string` |  |
| `context_timezone` | `string` |  |
| `context_useragent` | `string` |  |
| `context_locale` | `string` |  |
| `properties` | `map<string,string>` |  |
| `receivedat` | `string` |  |
| `request_ip` | `string` |  |
| `anonymousid` | `string` |  |
| `integrations` | `map<string,string>` |  |
| `originaltimestamp` | `string` |  |
| `dt` | `string` |  |

**Partition keys:** `dt`

## Enum-like columns

_String columns with ≤20 distinct values in 200 sampled rows from `IN`. Distribution shown as `value (×count)`._

- `type`: `page (×181)`, `track (×14)`, `identify (×5)`
- `channel`: `web (×200)`
- `context_app_version`: `2.44.0 (×188)`, `1.33.0 (×11)`, `2.43.0 (×1)`
- `context_timezone`: `GMT+0530 (×177)`, `GMT+0400 (×4)`, `GMT+0300 (×2)`, `GMT-0800 (×2)`, `GMT+0800 (×2)`, `GMT-0600 (×1)`
- `context_locale`: `en-IN (×91)`, `en-US (×65)`, `en-GB (×42)`, `ur (×1)`, `en-in (×1)`
- `dt`: `2023-11-13 (×200)`

## DDL


```sql
CREATE EXTERNAL TABLE `processed.rudder_wise_web_prod`(
  `type` string, 
  `event` string, 
  `sentat` string, 
  `channel` string, 
  `rudderid` string, 
  `messageid` string, 
  `timestamp` string, 
  `context_app_version` string, 
  `context_app_build` string, 
  `context_traits_wise_id` string, 
  `context_traits_phone` string, 
  `context_os_name` string, 
  `context_os_version` string, 
  `context_device_type` string, 
  `context_device_manufacturer` string, 
  `context_device_model` string, 
  `context_network_wifi` string, 
  `context_network_carrier` string, 
  `context_timezone` string, 
  `context_useragent` string, 
  `context_locale` string, 
  `properties` map<string,string>, 
  `receivedat` string, 
  `request_ip` string, 
  `anonymousid` string, 
  `integrations` map<string,string>, 
  `originaltimestamp` string)
PARTITIONED BY ( 
  `dt` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/rudder_lens'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'presto_query_id'='20231113_081520_00017_4j6yr', 
  'presto_version'='0.215-19668-g14a68eb', 
  'totalSize'='-1', 
  'transactional'='false', 
  'transient_lastDdlTime'='1699865506')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
