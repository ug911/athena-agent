---
canonical: processed
table: wise_app_backend__vendor_configuration
type: table
layer: processed
regions:
  in: processed
  na: processed_na
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/VendorConfiguration/
format: INPUTFORMAT
partition_keys: []
schema_parity: identical
last_synced: '2026-08-11T13:29:36+00:00'
sampled_rows: 200
sampled_region: in
---

# `processed.wise_app_backend__vendor_configuration`

## Region availability

| Region | Athena database |
| --- | --- |
| `IN` | `processed` |
| `NA` | `processed_na` |

_Schema parity: **identical** across regions._

## Columns (IN)

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` |  |
| `userid` | `string` |  |
| `webhooks` | `string` |  |
| `createdat` | `string` |  |
| `updatedat` | `string` |  |
| `__v` | `string` |  |

## Inferred JSON structure

_Inferred from 200 sampled rows from `IN` on 2026-08-11. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `62aad9e52d986f0022c8217f`, `6476fbbaf17d1d6787862b15`, `6476fbbaf17d1d6787862b1e`

### `userid`

- `$oid` — `string`  e.g. `6270c3ba05f7a631abb3be88`, `62739bfc5de04b201c5fa934`, `62cbb342cdd40f67cc08b16d`

### `webhooks`

  - `[]` — `object`
    - `_id` — `object`
      - `$oid` — `string`  e.g. `66e284892c810c7fcf8f8721`, `66f2e256c74cc82f77e207db`, `654a605afd7c34119f9b7a98`
    - `auth` — `string`  e.g. `65da68852b830209f6bcbeac32e0840a`, `65da68852b830209f6bcbeac32e0840a`, `baae216b0f69fce47114b826ba109aab`
    - `enabled` — `bool`  e.g. `true`, `true`, `true`
    - `events` — `array<string>`
      - `[].events[]` — `string`  e.g. `MeetingStartedEvent`, `MeetingEndedEvent`, `ParticipantJoinedMeetingEvent`
    - `method` — `string`  e.g. `POST`, `POST`, `POST`
    - `name` — `string`  e.g. `Webhook Subscription 1`, `Webhook Subscription`, `Webhook Subscription`
    - `url` — `string`  e.g. `https://engg.yourphysio.in/api/events/treatmentzoomevents`, `https://api-qadmin.eapp.vidyamandir.com/qadmin/zoom/webhooke`, `https://api-qadmin.devtest.thestudypod.com/quiz/zoom/webhook`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1655364069755`, `1685519290462`, `1685519290462`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1742456924317`, `1742564647941`, `1742456924317`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

## DDL

_From `IN` (processed)._

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
  'trino_query_id'='20260811_013231_00007_jw5xe', 
  'trino_version'='0.215-24619-g93e00a8')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
