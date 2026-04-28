---
database: processed
table: rudder_wise_prod
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/processed/rudder_wise_prod
format: INPUTFORMAT
partition_keys:
- dt
last_synced: '2026-04-28T07:12:08+00:00'
sampled_rows: 200
---

# `processed.rudder_wise_prod`

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

- `type`: `track (×137)`, `screen (×57)`, `identify (×6)`
- `sentat`: `2023-11-06T02:38:20.577Z (×50)`, `2022-07-18T00:00:20.611Z (×50)`, `2022-07-18T00:45:50.748Z (×35)`, `2023-08-26T01:43:45.469Z (×30)`, `2022-07-18T00:22:28.589Z (×21)`, `2023-11-06T03:56:45.508Z (×7)`, `2023-11-06T02:19:08.072Z (×6)`, `2023-08-26T01:43:51.763Z (×1)`
- `channel`: `mobile (×200)`
- `rudderid`: `820b60d9-325f-4beb-b31c-12dab548ab4a (×50)`, `326ad69b-7b6e-468a-b0c8-120b2e333c89 (×50)`, `0d79b9ad-e27f-4076-9fcf-164090ec79a0 (×35)`, `f1ee6e3e-2b2e-47c3-9420-55a81e1caf35 (×30)`, `00d12123-a814-446c-ad31-a4bfb25a81e3 (×21)`, `645c41b2-ee24-444f-9267-4ae321f7f707 (×7)`, `706185f0-f654-4f7d-a5cf-12aa26bc6c74 (×6)`, `46bf0bd8-724d-4815-a950-6d94a30a2d09 (×1)`
- `context_app_version`: `4.0.9 (×85)`, `4.9 (×56)`, `1.0 (×30)`, `4.0.8 (×21)`, `4.5.4 (×8)`
- `context_app_build`: `278 (×85)`, `338 (×56)`, `2 (×30)`, `277 (×21)`, `326 (×8)`
- `context_traits_wise_id`: `6544c60d74fc473446089e5c (×50)`, `62ceee321fce2e6a4fb2af82 (×50)`, `62c6779bafd1677f020858f6 (×35)`, `60d2c00483163c44707c0e01 (×21)`, `6314a32fbe58c410d6171478 (×7)`, `6259833c80ffa0585d1fe887 (×6)`, `64e16e71090e7b04b164062d (×1)`
- `context_os_name`: `Android (×200)`
- `context_os_version`: `11 (×63)`, `10 (×50)`, `9 (×50)`, `12 (×30)`, `8.1.0 (×6)`, `13 (×1)`
- `context_device_type`: `Android (×200)`
- `context_device_manufacturer`: `realme (×58)`, `Xiaomi (×50)`, `HUAWEI (×50)`, `OPPO (×35)`, `vivo (×7)`
- `context_device_model`: `M2006C3MII (×50)`, `INE-LX2 (×50)`, `CPH2269 (×35)`, `RMX3612 (×30)`, `RMX3261 (×21)`, `RMX3430 (×7)`, `vivo 1820 (×6)`, `V2059 (×1)`
- `context_network_wifi`: `false (×171)`, `true (×29)`
- `context_network_carrier`: `JIO 4G (×87)`, `Jio 4G (×56)`, `Mobitel (×50)`, `Vodafone IN (×6)`, `NT 3G (×1)`
- `context_timezone`: `Asia/Kolkata (×149)`, `Asia/Colombo (×50)`, `Asia/Kathmandu (×1)`
- `context_locale`: `en-IN (×101)`, `en-GB (×50)`, `en-US (×49)`
- `receivedat`: `2023-11-06T02:38:20.702Z (×50)`, `2022-07-18T00:00:10.132Z (×50)`, `2022-07-18T00:46:07.361Z (×35)`, `2023-08-26T01:43:47.486Z (×30)`, `2022-07-18T00:22:30.882Z (×21)`, `2023-11-06T04:01:11.074Z (×7)`, `2023-11-06T02:19:09.106Z (×6)`, `2023-08-26T01:43:53.434Z (×1)`
- `request_ip`: `157.49.64.163 (×50)`, `212.104.224.100 (×50)`, `157.36.48.215 (×35)`, `152.58.171.235 (×30)`, `117.228.176.221 (×21)`, `157.44.134.204 (×7)`, `42.111.161.31 (×6)`, `103.181.226.96 (×1)`
- `anonymousid`: `b35928c0a0122ddc (×50)`, `771343b33b3bf942 (×50)`, `fbc6f6043b41ea37 (×35)`, `279a8892bd61e261 (×30)`, `5ae9602a275c915e (×21)`, `b349d8fbee613f7c (×7)`, `bd629a5697e7c5a1 (×6)`, `7de6b906bdba41a8 (×1)`
- `dt`: `2022-07-18 (×106)`, `2023-11-06 (×63)`, `2023-08-26 (×31)`

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
