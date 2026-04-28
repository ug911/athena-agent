---
database: processed
table: rudder_lens
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/processed/rudder_lens
format: INPUTFORMAT
partition_keys:
- dt
last_synced: '2026-04-28T07:12:00+00:00'
sampled_rows: 200
---

# `processed.rudder_lens`

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

- `type`: `page (×145)`, `track (×55)`
- `event`: `start-meeting (×23)`, `Link Clicked (×7)`, `session-row-clicked (×5)`, `room-clicked (×4)`, `copy-room-link (×3)`, `poll-voted (×2)`, `see-all-meetings (×2)`, `Create room
 (×2)`, `create-poll (×1)`, `create-room (×1)`, `refresh (×1)`, `open-settings-page (×1)`, `logout (×1)`, `update-user-profile (×1)`, `polls-tool-clicked (×1)`
- `channel`: `web (×200)`
- `context_app_version`: `2.44.0 (×199)`, `2.32.0 (×1)`
- `context_timezone`: `GMT+0530 (×69)`, `GMT+0700 (×54)`, `GMT+0000 (×37)`, `GMT-0800 (×21)`, `GMT+0500 (×8)`, `GMT+0100 (×6)`, `GMT-0300 (×1)`, `GMT+0300 (×1)`, `GMT-0600 (×1)`, `GMT+0545 (×1)`
- `context_locale`: `en-US (×113)`, `en-IN (×35)`, `pt-PT (×28)`, `en-PK (×6)`, `en-SG (×5)`, `vi-VN (×5)`, `en-GB (×4)`, `en (×2)`, `pt-BR (×2)`
- `dt`: `2023-11-10 (×126)`, `2023-11-11 (×72)`, `2023-11-12 (×2)`

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
