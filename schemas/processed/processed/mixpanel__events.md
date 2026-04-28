---
database: processed
table: mixpanel__events
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/mixpanel/processed_events
format: INPUTFORMAT
partition_keys:
- year
- month
- day
last_synced: '2026-04-28T07:11:42+00:00'
sampled_rows: 0
---

# `processed.mixpanel__events`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `event` | `string` |  |
| `time` | `string` |  |
| `distinct_id` | `string` |  |
| `city` | `string` |  |
| `device_id` | `string` |  |
| `distinct_id_before_identity` | `string` |  |
| `insert_id` | `string` |  |
| `lib_version` | `string` |  |
| `mp_api_endpoint` | `string` |  |
| `os` | `string` |  |
| `region` | `string` |  |
| `screen_height` | `string` |  |
| `screen_width` | `string` |  |
| `user_id` | `string` |  |
| `mp_country_code` | `string` |  |
| `mp_lib` | `string` |  |
| `mp_processing_time_ms` | `string` |  |
| `app_build_number` | `string` |  |
| `app_release` | `string` |  |
| `app_version` | `string` |  |
| `app_version_string` | `string` |  |
| `bluetooth_enabled` | `string` |  |
| `bluetooth_version` | `string` |  |
| `brand` | `string` |  |
| `carrier` | `string` |  |
| `google_play_services` | `string` |  |
| `had_persisted_distinct_id` | `string` |  |
| `has_nfc` | `string` |  |
| `has_telephone` | `string` |  |
| `manufacturer` | `string` |  |
| `model` | `string` |  |
| `os_version` | `string` |  |
| `screen_dpi` | `string` |  |
| `wifi` | `string` |  |
| `platform` | `string` |  |
| `profile_type` | `string` |  |
| `referrer` | `string` |  |
| `utm_medium` | `string` |  |
| `utm_source` | `string` |  |
| `number_of_classrooms` | `string` |  |
| `classroom_id` | `string` |  |
| `subject` | `string` |  |
| `init_error_code` | `string` |  |
| `init_internal_error_code` | `string` |  |
| `prop_meeting_status` | `string` |  |
| `properties` | `map<string,string>` |  |
| `year` | `int` |  |
| `month` | `int` |  |
| `day` | `int` |  |

**Partition keys:** `year`, `month`, `day`

## DDL

```sql
CREATE EXTERNAL TABLE `processed.mixpanel__events`(
  `event` string COMMENT '', 
  `time` string COMMENT '', 
  `distinct_id` string COMMENT '', 
  `city` string COMMENT '', 
  `device_id` string COMMENT '', 
  `distinct_id_before_identity` string COMMENT '', 
  `insert_id` string COMMENT '', 
  `lib_version` string COMMENT '', 
  `mp_api_endpoint` string COMMENT '', 
  `os` string COMMENT '', 
  `region` string COMMENT '', 
  `screen_height` string COMMENT '', 
  `screen_width` string COMMENT '', 
  `user_id` string COMMENT '', 
  `mp_country_code` string COMMENT '', 
  `mp_lib` string COMMENT '', 
  `mp_processing_time_ms` string COMMENT '', 
  `app_build_number` string COMMENT '', 
  `app_release` string COMMENT '', 
  `app_version` string COMMENT '', 
  `app_version_string` string COMMENT '', 
  `bluetooth_enabled` string COMMENT '', 
  `bluetooth_version` string COMMENT '', 
  `brand` string COMMENT '', 
  `carrier` string COMMENT '', 
  `google_play_services` string COMMENT '', 
  `had_persisted_distinct_id` string COMMENT '', 
  `has_nfc` string COMMENT '', 
  `has_telephone` string COMMENT '', 
  `manufacturer` string COMMENT '', 
  `model` string COMMENT '', 
  `os_version` string COMMENT '', 
  `screen_dpi` string COMMENT '', 
  `wifi` string COMMENT '', 
  `platform` string COMMENT '', 
  `profile_type` string COMMENT '', 
  `referrer` string COMMENT '', 
  `utm_medium` string COMMENT '', 
  `utm_source` string COMMENT '', 
  `number_of_classrooms` string COMMENT '', 
  `classroom_id` string COMMENT '', 
  `subject` string COMMENT '', 
  `init_error_code` string COMMENT '', 
  `init_internal_error_code` string COMMENT '', 
  `prop_meeting_status` string COMMENT '', 
  `properties` map<string,string> COMMENT '')
PARTITIONED BY ( 
  `year` int, 
  `month` int, 
  `day` int)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/mixpanel/processed_events'
TBLPROPERTIES (
  'has_encrypted_data'='false', 
  'parquet.compression'='GZIP', 
  'presto_query_id'='20210805_125215_00054_9edip', 
  'transient_lastDdlTime'='1628242698')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
