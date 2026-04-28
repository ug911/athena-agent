---
database: processed
table: wise_app_backend__saved_communication
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/saved_communication/
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:17:04+00:00'
sampled_rows: 200
---

# `processed.wise_app_backend__saved_communication`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` |  |
| `userid` | `string` |  |
| `ownerid` | `string` |  |
| `creditsused` | `string` |  |
| `type` | `string` |  |
| `category` | `string` |  |
| `createdat` | `string` |  |
| `updatedat` | `string` |  |
| `__v` | `string` |  |

## Enum-like columns

_String columns with ≤20 distinct values in 200 sampled rows. Distribution shown as `value (×count)`._

- `type`: `EMAIL (×143)`, `WHATSAPP (×57)`
- `category`: `LearnerAddedToClassroom (×64)`, `WiseStudentInvite (×24)`, `SessionUpdated (×21)`, `SessionReminder_10 (×18)`, `InstructorAddedToClassroom (×12)`, `SessionReminder_60 (×11)`, `SessionStarted (×10)`, `UnreadChatReminder (×8)`, `SessionNotStartedAdminReminder (×8)`, `EmailOTP (×6)`, `SessionFeedback (×4)`, `PhoneOTP (×4)`, `SessionCreditUpdates (×4)`, `CertificateCreation (×2)`, `LoginPin (×2)`, `SessionNotStartedTeacherReminder (×1)`, `PremiumPurchase (×1)`

## Inferred JSON structure

_Inferred from 200 sampled rows on 2026-04-28. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `690304dd2d0531ab76c8122c`, `690304de8d98067b8fffc3db`, `690304dea817a24443351626`

### `userid`

- `$oid` — `string`  e.g. `683412a9b213e9ac49783355`, `6819d48ebc3f5953432867c7`, `683ae789b213e9ac492452c1`

### `ownerid`

- `$oid` — `string`  e.g. `6819d48ebc3f5953432867c7`, `6819d48ebc3f5953432867c7`, `6819d48ebc3f5953432867c7`

### `creditsused`

- `$numberint` — `string`  e.g. `1`, `1`, `60`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1761805533533`, `1761805534417`, `1761805534803`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1761805535205`, `1761805536898`, `1761805534803`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

## DDL

```sql
CREATE EXTERNAL TABLE `processed.wise_app_backend__saved_communication`(
  `_id` string, 
  `userid` string, 
  `ownerid` string, 
  `creditsused` string, 
  `type` string, 
  `category` string, 
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
  's3://[REDACTED-BUCKET]/processed/wise-app-backend/saved_communication/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260428_011813_00070_brnxs', 
  'trino_version'='0.215-24582-g0575ac4')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
