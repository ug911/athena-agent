---
database: processed
table: wise_app_backend__vendor_configuration
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/VendorConfiguration/
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:17:51+00:00'
sampled_rows: 200
---

# `processed.wise_app_backend__vendor_configuration`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` |  |
| `userid` | `string` |  |
| `webhooks` | `string` |  |
| `createdat` | `string` |  |
| `updatedat` | `string` |  |
| `__v` | `string` |  |

## Inferred JSON structure

_Inferred from 200 sampled rows on 2026-04-28. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `62aad9e52d986f0022c8217f`, `62ac0f94d9c16b002342b6d1`, `64747a8c7aa3589fab228e70`

### `userid`

- `$oid` — `string`  e.g. `6270c3ba05f7a631abb3be88`, `6238668770c3360adddee5e7`, `63b5269d04c8f235eb5f4c77`

### `webhooks`

  - `[]` — `object`
    - `_id` — `object`
      - `$oid` — `string`  e.g. `684c0178f0107734e8b10f79`, `6530f75d8ee13548263ca7a4`, `6530f7744b6813fbc73bb4c5`
    - `auth` — `string`  e.g. `c0c54be07f12f1aaeed8027e9de3529d`, `66443c3808d7d4ef15fc827206fdd2e7`, `1c20ebfeeb24e524c7a860c8cd283686`
    - `enabled` — `bool`  e.g. `true`, `true`, `true`
    - `events` — `array<string>`
      - `[].events[]` — `string`  e.g. `MeetingStartedEvent`, `MeetingEndedEvent`, `ParticipantJoinedMeetingEvent`
    - `method` — `string`  e.g. `POST`, `POST`, `POST`
    - `name` — `string`  e.g. `Webhook Subscription 1`, `Webhook Subscription 1`, `Webhook Subscription 2`
    - `url` — `string`  e.g. `https://engg.yourphysio.in/api/events/treatmentzoomevents`, `https://bambinos.live/api/wise/meeting-ended`, `https://bambinos.live/api/wise/participant-joined`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1655364069755`, `1655443348262`, `1655443348262`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1742456924317`, `1742456924317`, `1742456924317`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

## DDL

```sql
CREATE EXTERNAL TABLE `processed.wise_app_backend__vendor_configuration`(
  `_id` string, 
  `userid` string, 
  `webhooks` string, 
  `createdat` string, 
  `updatedat` string, 
  `__v` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/wise-app-backend/VendorConfiguration/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260428_012236_00043_qvvav', 
  'trino_version'='0.215-24582-g0575ac4')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
