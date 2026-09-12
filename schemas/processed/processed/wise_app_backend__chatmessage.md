---
canonical: processed
table: wise_app_backend__chatmessage
type: table
layer: processed
regions:
  in: processed
  na: processed_na
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/ChatMessage/
format: INPUTFORMAT
partition_keys: []
schema_parity: identical
last_synced: '2026-08-11T13:21:31+00:00'
sampled_rows: 200
sampled_region: in
---

# `processed.wise_app_backend__chatmessage`

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
| `createdat` | `string` |  |
| `updatedat` | `string` |  |
| `chatid` | `string` |  |
| `senderid` | `string` |  |
| `message` | `string` |  |
| `attachments` | `string` |  |

## Inferred JSON structure

_Inferred from 200 sampled rows from `IN` on 2026-08-11. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `67c00cd141bf6a8380eca099`, `67c00ce89822ae02c0c45bfc`, `67c00e2c41bf6a8380ecc52b`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1740639441175`, `1740639464725`, `1740639788990`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1740639441175`, `1740639464725`, `1740639788990`

### `chatid`

- `$oid` — `string`  e.g. `67c00cc4f6b7db0bccf35f18`, `67c00cc4f6b7db0bccf35f18`, `67c00e14f6b7db0bccf42e50`

### `senderid`

- `$oid` — `string`  e.g. `66224320782dfcbe299ba9a4`, `66224320782dfcbe299ba9a4`, `66dfad062c667e74defcd0d0`

### `attachments`

  - `[]` — `object`
    - `_id` — `object`
      - `$oid` — `string`  e.g. `67c05f894002a60d53151159`, `67c03ba1ad3553a79aa5e6ce`, `67c08adfb455f3e1a1758133`
    - `filename` — `string`  e.g. `BMW X1 Diesel.pdf`, `recording-1740651446153.mp3`, `recording-1740671705654.mp3`
    - `path` — `string`  e.g. `https://files.wiseapp.live/upload_files/63edf333d0f46c85b4ca`, `https://files.wiseapp.live/upload_files/678f7a24014dea0655a6`, `https://files.wiseapp.live/upload_files/654e5d12484e1be27bd3`
    - `s3filepath` — `string`  e.g. `https://wise-app-s3-bucket.s3-ap-south-1.amazonaws.com/uploa`, `https://wise-app-s3-bucket.s3-ap-south-1.amazonaws.com/uploa`, `https://wise-app-s3-bucket.s3-ap-south-1.amazonaws.com/uploa`
    - `s3key` — `string`  e.g. `upload_files/63edf333d0f46c85b4cad726/upload_d01bdcd7-d3a8-4`, `upload_files/678f7a24014dea0655a6b5be/upload_fd5ab1dc-cf42-4`, `upload_files/654e5d12484e1be27bd3aa3c/upload_4d783584-18e2-4`
    - `size` — `object`
      - `$numberint` — `string`  e.g. `130026`, `53680`, `144959`
    - `type` — `string`  e.g. `pdf`, `audio`, `audio`

## DDL

_From `IN` (processed)._

```sql
CREATE EXTERNAL TABLE `processed.wise_app_backend__chatmessage`(
  `_id` string, 
  `createdat` string, 
  `updatedat` string, 
  `chatid` string, 
  `senderid` string, 
  `message` string, 
  `attachments` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/wise-app-backend/ChatMessage/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260811_003354_00007_ekd7b', 
  'trino_version'='0.215-24619-g93e00a8')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
