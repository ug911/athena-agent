---
canonical: processed
table: rudder_wise_prod
type: table
layer: processed
regions:
  in: processed
location: s3://[REDACTED-BUCKET]/processed/rudder_wise_prod
format: INPUTFORMAT
partition_keys:
- dt
schema_parity: identical
last_synced: '2026-08-11T13:17:59+00:00'
sampled_rows: 200
sampled_region: in
---

# `processed.rudder_wise_prod`

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

- `type`: `track (×154)`, `screen (×46)`
- `event`: `generic_error (×71)`, `Application Opened (×33)`, `Application Backgrounded (×33)`, `ui.main.MainActivity (×27)`, `ui.splash.SplashActivity (×19)`, `app_open (×16)`, `status_notification_click (×1)`
- `sentat`: `2026-05-19T03:11:04.868Z (×50)`, `2026-05-19T14:40:32.144Z (×50)`, `2026-05-19T08:48:34.147Z (×42)`, `2026-05-19T06:27:55.730Z (×41)`, `2026-05-19T11:11:17.211Z (×12)`, `2026-05-19T10:58:44.818Z (×5)`
- `channel`: `mobile (×200)`
- `rudderid`: `8ea90270-3e90-4ec4-84b5-81d42a3eb919 (×50)`, `94331022-b40a-48e8-8808-6495e04c6ae1 (×50)`, `01f87d50-d60d-4e00-99c6-453246375813 (×42)`, `27ea1c13-bc54-45a3-9d52-db7f60fdcf1b (×41)`, `d15ce4b3-3f97-4db0-91a8-39314ca080df (×12)`, `37ae1266-2e16-4463-897d-30d579c90f1c (×5)`
- `context_app_version`: `4.3.6 (×91)`, `7.3 (×50)`, `3.7.0 (×42)`, `4.0.8 (×12)`, `4.5.4 (×5)`
- `context_app_build`: `306 (×91)`, `363 (×50)`, `246 (×42)`, `277 (×12)`, `326 (×5)`
- `context_os_name`: `Android (×200)`
- `context_os_version`: `16 (×50)`, `10 (×50)`, `12 (×46)`, `8.1.0 (×42)`, `13 (×12)`
- `context_device_type`: `Android (×200)`
- `context_device_manufacturer`: `realme (×55)`, `vivo (×54)`, `LENOVO (×50)`, `samsung (×41)`
- `context_device_model`: `RMX3997 (×50)`, `Lenovo TB-X606V (×50)`, `vivo 1811 (×42)`, `SM-A217F (×41)`, `V2025 (×12)`, `RMX3092 (×5)`
- `context_network_wifi`: `false (×167)`, `true (×33)`
- `context_network_carrier`: `airtel (×92)`, `JIO 4G (×53)`, `IND airtel (×15)`
- `context_timezone`: `Asia/Kolkata (×200)`
- `context_locale`: `en-GB (×91)`, `en-IN (×55)`, `en-US (×54)`
- `receivedat`: `2026-05-19T03:11:05.387Z (×50)`, `2026-05-19T14:40:34.576Z (×50)`, `2026-05-19T08:48:38.339Z (×42)`, `2026-05-19T06:27:55.839Z (×41)`, `2026-05-19T11:11:18.774Z (×12)`, `2026-05-19T10:58:46.552Z (×5)`
- `request_ip`: `106.192.249.169 (×50)`, `110.224.242.191 (×50)`, `27.61.122.112 (×42)`, `157.32.213.6 (×41)`, `49.42.34.219 (×12)`, `106.192.86.38 (×5)`
- `anonymousid`: `5bb47031b1d1e796 (×50)`, `89acf176b0dd8d42 (×50)`, `12a2a831c5f841b3 (×42)`, `9771d71a3f04c8a9 (×41)`, `b19ccf63b62bfc19 (×12)`, `891af063fd369399 (×5)`
- `dt`: `2026-05-19 (×200)`

## DDL


```sql
CREATE EXTERNAL TABLE `processed.rudder_wise_prod`(
  `type` string COMMENT '', 
  `event` string COMMENT '', 
  `sentat` string COMMENT '', 
  `channel` string COMMENT '', 
  `rudderid` string COMMENT '', 
  `messageid` string COMMENT '', 
  `timestamp` string COMMENT '', 
  `context_app_version` string COMMENT '', 
  `context_app_build` string COMMENT '', 
  `context_traits_wise_id` string COMMENT '', 
  `context_traits_phone` string COMMENT '', 
  `context_os_name` string COMMENT '', 
  `context_os_version` string COMMENT '', 
  `context_device_type` string COMMENT '', 
  `context_device_manufacturer` string COMMENT '', 
  `context_device_model` string COMMENT '', 
  `context_network_wifi` string COMMENT '', 
  `context_network_carrier` string COMMENT '', 
  `context_timezone` string COMMENT '', 
  `context_useragent` string COMMENT '', 
  `context_locale` string COMMENT '', 
  `properties` map<string,string> COMMENT '', 
  `receivedat` string COMMENT '', 
  `request_ip` string COMMENT '', 
  `anonymousid` string COMMENT '', 
  `integrations` map<string,string> COMMENT '', 
  `originaltimestamp` string COMMENT '')
PARTITIONED BY ( 
  `dt` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/rudder_wise_prod'
TBLPROPERTIES (
  'has_encrypted_data'='false', 
  'parquet.compression'='GZIP', 
  'presto_query_id'='20220210_091940_00044_3fibv', 
  'transient_lastDdlTime'='1644485225')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
