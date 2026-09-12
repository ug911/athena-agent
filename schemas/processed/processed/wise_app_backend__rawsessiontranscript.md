---
canonical: processed
table: wise_app_backend__rawsessiontranscript
type: table
layer: processed
regions:
  in: processed
  na: processed_na
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/RawSessionTranscript/
format: INPUTFORMAT
partition_keys: []
schema_parity: identical
last_synced: '2026-08-11T13:27:17+00:00'
sampled_rows: 200
sampled_region: in
---

# `processed.wise_app_backend__rawsessiontranscript`

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
| `sessionid` | `string` |  |
| `files` | `string` |  |

## Inferred JSON structure

_Inferred from 200 sampled rows from `IN` on 2026-08-11. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `673b1dab2d8443c68211dd2e`, `673b1daf2d8443c68211e318`, `673b1dc12d8443c68211f5a6`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1731927467408`, `1731927471129`, `1731927489442`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1731927467408`, `1731927471129`, `1731927555760`

### `sessionid`

- `$oid` — `string`  e.g. `673b181a12d580cab7eb2cc8`, `673b1763bd6472468e6cd0e8`, `673b1d531cfe134c72b5def4`

### `files`

  - `[]` — `object`
    - `_id` — `object`
      - `$oid` — `string`  e.g. `673b1dabbfebad470324da48`, `673b1daf2e86e530246c49ae`, `673b1dc12e86e506da6c49c7`
    - `file` — `object`
      - `_id` — `object`
        - `$oid` — `string`  e.g. `673b1dabbfebad562624da49`, `673b1daf2e86e554ce6c49af`, `673b1dc12e86e526fb6c49c8`
      - `filename` — `string`  e.g. `673b181a12d580cab7eb2cc8-transcript-1.1.vtt`, `673b1763bd6472468e6cd0e8-transcript-1.1.vtt`, `673b1d531cfe134c72b5def4-transcript-1.1.vtt`
      - `path` — `string`  e.g. `https://files.wiseapp.live/upload_files/64fecbcec47b39bb3f97`, `https://learn2read-wise-recordings.s3.amazonaws.com/class_re`, `https://files.wiseapp.live/upload_files/66b0e0445d0cd024862f`
      - `s3filepath` — `string`  e.g. `https://wise-app-s3-bucket.s3-ap-south-1.amazonaws.com/uploa`, `https://learn2read-wise-recordings.s3.amazonaws.com/class_re`, `https://wise-app-s3-bucket.s3-ap-south-1.amazonaws.com/uploa`
      - `s3key` — `string`  e.g. `upload_files/64fecbcec47b39bb3f976657/673b181a12d580cab7eb2c`, `class_recordings/673b1763bd6472468e6cd0e8-transcript-1.1.vtt`, `upload_files/66b0e0445d0cd024862f32c8/673b1d531cfe134c72b5de`
      - `type` — `string`  e.g. `text`, `text`, `text`
    - `meetinguuid` — `string`  e.g. `02KMv4h1Sn+MXNSXe0T6/w==`, `mqj4F9K9Rg+SVVs7W4JhcA==`, `UsVYpo9URV+RbA9UYeHbxQ==`
    - `partindex` — `object`
      - `$numberint` — `string`  e.g. `1`, `1`, `1`
    - `sessionindex` — `object`
      - `$numberint` — `string`  e.g. `1`, `1`, `1`
    - `url` — `string`  e.g. `https://files.wiseapp.live/upload_files/64fecbcec47b39bb3f97`, `https://learn2read-wise-recordings.s3.amazonaws.com/class_re`, `https://files.wiseapp.live/upload_files/66b0e0445d0cd024862f`

## DDL

_From `IN` (processed)._

```sql
CREATE EXTERNAL TABLE `processed.wise_app_backend__rawsessiontranscript`(
  `_id` string, 
  `createdat` string, 
  `updatedat` string, 
  `sessionid` string, 
  `files` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/wise-app-backend/RawSessionTranscript/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260811_012624_00151_68yef', 
  'trino_version'='0.215-24619-g93e00a8')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->

### Transcript availability

- **`files` is a JSON array and can be empty**, so a row does not imply a transcript exists.
  Gate on `files IS NOT NULL AND files <> '[]'`.
- `files[].file.filename` looks like `<sessionid>-transcript-<sessionindex>.<partindex>.vtt`; a long session
  can produce several parts/segments, hence multiple entries per row.
- Join on `json_extract_scalar(sessionid, '$["$oid"]') = zoomers_v3.zoom_id`.
- Transcript coverage runs consistently *below* AI-summary coverage
  (`wise_app_backend__rawzoomsummary`) in both regions — do not treat the two as interchangeable
  proxies for "session had AI processing".
