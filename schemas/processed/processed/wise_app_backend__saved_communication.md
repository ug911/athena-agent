---
canonical: processed
table: wise_app_backend__saved_communication
type: table
layer: processed
regions:
  in: processed
  na: processed_na
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/saved_communication/
format: INPUTFORMAT
partition_keys: []
schema_parity: identical
last_synced: '2026-08-11T13:27:48+00:00'
sampled_rows: 200
sampled_region: in
---

# `processed.wise_app_backend__saved_communication`

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
| `ownerid` | `string` |  |
| `creditsused` | `string` |  |
| `type` | `string` |  |
| `category` | `string` |  |
| `createdat` | `string` |  |
| `updatedat` | `string` |  |
| `__v` | `string` |  |

## Enum-like columns

_String columns with ≤20 distinct values in 200 sampled rows from `IN`. Distribution shown as `value (×count)`._

- `type`: `EMAIL (×128)`, `WHATSAPP (×72)`
- `category`: `LearnerAddedToClassroom (×75)`, `SessionUpdated (×39)`, `SessionReminder_60 (×28)`, `EmailOTP (×9)`, `LoginPin (×9)`, `PhoneOTP (×8)`, `WiseStudentInvite (×6)`, `InstructorAddedToClassroom (×6)`, `SessionReminder_10 (×6)`, `SessionReminder_1440 (×5)`, `SessionStarted (×3)`, `SessionFeedback (×3)`, `UnreadChatReminder (×1)`, `SessionNotStartedTeacherReminder (×1)`, `FeeAdded (×1)`

## Inferred JSON structure

_Inferred from 200 sampled rows from `IN` on 2026-08-11. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `698d81d241083a79f48c7233`, `698d81ed986aa71472ad2c49`, `698d8201114d8ca60b212859`

### `userid`

- `$oid` — `string`  e.g. `696bddb443579bbadaca7f2a`, `694669e728118f629e7eb0b7`, `68e60408b4de7252dfcb935a`

### `ownerid`

- `$oid` — `string`  e.g. `66a9dff1797744d1c7b5b3d7`, `68b97e5969bf3cf7e1f7aada`, `687e42910933d0d619f41d47`

### `creditsused`

- `$numberint` — `string`  e.g. `1`, `0`, `1`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1770881490391`, `1770881517457`, `1770881537316`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1770881491849`, `1770881517457`, `1770881540274`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

## DDL

_From `IN` (processed)._

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
  'trino_query_id'='20260811_012537_00169_m83um', 
  'trino_version'='0.215-24619-g93e00a8')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
