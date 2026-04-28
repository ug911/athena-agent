---
database: processed
table: rudder_wise_web_prod
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/processed/rudder_lens
format: INPUTFORMAT
partition_keys:
- dt
last_synced: '2026-04-28T07:12:10+00:00'
sampled_rows: 200
---

# `processed.rudder_wise_web_prod`

## Columns

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

_String columns with ≤20 distinct values in 200 sampled rows. Distribution shown as `value (×count)`._

- `type`: `page (×136)`, `track (×59)`, `identify (×5)`
- `event`: `Page View (×20)`, `timeline-card-clicked (×6)`, `refresh (×5)`, `start_test_link (×3)`, `View answer key & Your responses (×3)`, `omr_answer (×3)`, `display_start_time (×1)`, `update-user-profile (×1)`
- `channel`: `web (×200)`
- `context_app_version`: `2.44.0 (×153)`, `1.33.0 (×47)`
- `context_timezone`: `GMT+0530 (×139)`, `GMT-0600 (×4)`, `GMT+0400 (×3)`, `GMT+0800 (×3)`, `GMT-0800 (×2)`, `GMT+0300 (×1)`, `GMT-0500 (×1)`
- `context_locale`: `en-IN (×95)`, `en-US (×68)`, `en-GB (×35)`, `ar-EG (×1)`, `en-in (×1)`
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
