---
canonical: processed
table: rudder_lens
type: table
layer: processed
regions:
  in: processed
location: s3://[REDACTED-BUCKET]/processed/rudder_lens
format: INPUTFORMAT
partition_keys:
- dt
schema_parity: identical
last_synced: '2026-08-11T13:17:47+00:00'
sampled_rows: 200
sampled_region: in
---

# `processed.rudder_lens`

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

- `type`: `page (×132)`, `track (×65)`, `identify (×3)`
- `event`: `room-clicked (×14)`, `start-meeting (×12)`, `session-row-clicked (×6)`, `poll-voted (×6)`, `Link Clicked (×4)`, `see-all-meetings (×4)`, `delete-room (×3)`, `open-settings-page (×2)`, `create-room (×2)`, `unmute-participant (×2)`, `Create room
 (×2)`, `Video played (×1)`, `mute-participant (×1)`, `copy-meeting-link (×1)`, `copy-room-link (×1)`, `logout (×1)`, `update-user-profile (×1)`
- `channel`: `web (×200)`
- `context_app_version`: `2.44.0 (×200)`
- `context_timezone`: `GMT+0530 (×93)`, `GMT+0000 (×60)`, `GMT+0700 (×22)`, `GMT-0800 (×17)`, `GMT-0500 (×3)`, `GMT+0100 (×2)`, `GMT+0500 (×1)`, `GMT-0300 (×1)`, `GMT+0545 (×1)`
- `context_locale`: `en-US (×87)`, `en-IN (×52)`, `pt-PT (×41)`, `en-SG (×12)`, `en (×3)`, `en-GB (×2)`, `vi-VN (×1)`, `es-US (×1)`, `es-MX (×1)`
- `dt`: `2023-11-10 (×173)`, `2023-11-12 (×27)`

## DDL


```sql
CREATE EXTERNAL TABLE `processed.rudder_lens`(
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
  'transient_lastDdlTime'='1699863782')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
