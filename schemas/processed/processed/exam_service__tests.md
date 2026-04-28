---
database: processed
table: exam_service__tests
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/processed/exam-service/tests/
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:10:46+00:00'
sampled_rows: 200
---

# `processed.exam_service__tests`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` |  |
| `active` | `string` |  |
| `display_results` | `string` |  |
| `status` | `string` |  |
| `_type` | `string` |  |
| `name` | `string` |  |
| `class_id` | `string` |  |
| `user_id` | `string` |  |
| `jumbled_questions` | `string` |  |
| `mock_test` | `string` |  |
| `disable_commenting` | `string` |  |
| `updated_at` | `string` |  |
| `created_at` | `string` |  |
| `test_question` | `string` |  |
| `answers` | `string` |  |
| `question_count` | `string` |  |
| `correct_marks` | `string` |  |
| `description` | `string` |  |
| `duration` | `string` |  |
| `end_time` | `string` |  |
| `incorrect_marks` | `string` |  |
| `max_marks` | `string` |  |
| `start_time` | `string` |  |
| `analysis` | `string` |  |
| `total_present` | `string` |  |
| `questions` | `string` |  |
| `publish_results` | `string` |  |

## Enum-like columns

_String columns with ≤20 distinct values in 200 sampled rows. Distribution shown as `value (×count)`._

- `active`: `true (×196)`, `false (×4)`
- `display_results`: `true (×200)`
- `status`: `ACTIVE (×166)`, `DRAFT (×23)`, `GRADED (×11)`
- `_type`: `UserInputOmrTest (×129)`, `OmrTest (×71)`
- `jumbled_questions`: `false (×198)`, `true (×2)`
- `mock_test`: `true (×179)`, `false (×21)`
- `disable_commenting`: `false (×200)`
- `description`: `Another test about our planet (×31)`, `Here are some questions about forests and animals (×24)`, `Test about galaxy facts and features (×21)`, `Test about our planet (×15)`, `Test your knowledge on wildlife and ecosystems. (×8)`, `Another test about solar system planets (×7)`, `A test about solar system planets (×7)`, `100 MCQs in 110 minutes (×3)`, `10MCQ (×1)`, `Please read all the questions properly before answering (×1)`, `सभी प्रश्न करना अनिवार्य है  (×1)`, `🌸 (×1)`, `Monthly test 1 (×1)`, `The Answers for Fill in Blank questions should be in the following format:
Quotient (space) 'R' reminder (e.g. 23 R5) (×1)`, `DPT-M-6 Sets -27.04.26 (×1)`, `DPT B-7 Fertilization & Pollen–Pistil Interaction 27.04.26 (×1)`, `Please complete and submit your answers here. Thank you.  (×1)`

## Inferred JSON structure

_Inferred from 200 sampled rows on 2026-04-28. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `69ef9f5cfb9af90001d3dea7`, `69ef9279c57c5d0001121110`, `69ef91b8c57c5d00011210df`

### `class_id`

- `$oid` — `string`  e.g. `69ef9a483458a63e06f8553c`, `69cfc03c0dcffd79edb23fde`, `69cfc3df67cb06ce5ab7bb1d`

### `user_id`

- `$oid` — `string`  e.g. `69d6055d98ee51775f4c2d13`, `69c4d0aa59c459d1a1bbcca2`, `69c4d0aa59c459d1a1bbcca2`

### `updated_at`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1777311628612`, `1774636195924`, `1774979204541`

### `created_at`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1777311628606`, `1777308281250`, `1777308087969`

### `test_question`

  - `[]` — `object`
    - `_id` — `object`
      - `$oid` — `string`  e.g. `65e7248da85a170001fcf065`, `65e7248da85a170001fcf065`, `65e7248da85a170001fcf065`
    - `filename` — `string`  e.g. `economy full length (1).pdf`, `economy full length (1).pdf`, `economy full length (1).pdf`
    - `path` — `string`  e.g. `https://files.wiseapp.live/upload_files/60dd848250b02dd2549f`, `https://files.wiseapp.live/upload_files/60dd848250b02dd2549f`, `https://files.wiseapp.live/upload_files/60dd848250b02dd2549f`
    - `question_type` — `string`  e.g. `ATTACHMENT`, `ATTACHMENT`, `ATTACHMENT`
    - `s3_filepath` — `string`  e.g. `https://wise-app-s3-bucket.s3-ap-south-1.amazonaws.com/uploa`, `https://wise-app-s3-bucket.s3-ap-south-1.amazonaws.com/uploa`, `https://wise-app-s3-bucket.s3-ap-south-1.amazonaws.com/uploa`
    - `s3_key` — `string`  e.g. `upload_files/60dd848250b02dd2549fda9e/upload_697ca115-4d43-4`, `upload_files/60dd848250b02dd2549fda9e/upload_697ca115-4d43-4`, `upload_files/60dd848250b02dd2549fda9e/upload_697ca115-4d43-4`
    - `size` — `object`
      - `$numberint` — `string`  e.g. `1015454`, `1015454`, `1015454`
    - `type` — `string`  e.g. `application/pdf`, `application/pdf`, `application/pdf`

### `answers`

- `<oid>` — `string`  e.g. `a`, `c`, `d`

### `duration`

- `$numberint` — `string`  e.g. `10`, `45`, `30`

### `end_time`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1777305720000`, `1777303500000`, `1777317600000`

### `max_marks`

- `$numberint` — `string`  e.g. `3`, `180`, `120`

### `start_time`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1777303920000`, `1777302600000`, `1777311000000`

### `analysis`

- `<oid>` — `object`
  - `attempted_by` — `object`
    - `$numberint` — `string`  e.g. `1`, `1`, `1`
  - `attempted_correctly` — `object`
    - `$numberint` — `string`  e.g. `0`, `1`, `1`

### `total_present`

- `$numberint` — `string`  e.g. `0`, `1`, `1`

### `questions`

  - `[]` — `object`
    - `_id` — `object`
      - `$oid` — `string`  e.g. `69ef9f748fe9dd0001a27213`, `69c685c663a491000101f85c`, `69c686acbb45f0000124cb85`
    - `_type` — `string`  e.g. `UserInputTestQuestion`, `UserInputTestQuestion`, `UserInputTestQuestion`
    - `archived` — `bool`  e.g. `false`, `false`, `false`
    - `attachments` — `array<object>`
      - `[].attachments[]` — `object`
        - `_id` — `object`
          - `$oid` — `string`  e.g. `68a854dc17b4640001b7a18d`, `69ef7955fb9af90001d3ddc1`, `69ef79bffb9af90001d3ddc3`
        - `filename` — `string`  e.g. `Screenshot (329).png`, `36840.jpg`, `36841.jpg`
        - `path` — `string`  e.g. `https://files.wiseapp.live/upload_files/6710a35793270d624a99`, `https://files.wiseapp.live/upload_files/6710a35793270d624a99`, `https://files.wiseapp.live/upload_files/6710a35793270d624a99`
        - `s3_filepath` — `string`  e.g. `https://wise-app-s3-bucket.s3-ap-south-1.amazonaws.com/uploa`, `https://wise-app-s3-bucket.s3-ap-south-1.amazonaws.com/uploa`, `https://wise-app-s3-bucket.s3-ap-south-1.amazonaws.com/uploa`
        - `s3_key` — `string`  e.g. `upload_files/6710a35793270d624a996439/upload_5b05c902-2052-4`, `upload_files/6710a35793270d624a996439/upload_3e25d2cf-7f76-4`, `upload_files/6710a35793270d624a996439/upload_c0a07a13-ec58-4`
        - `size` — `object`
          - `$numberint` — `string`  e.g. `80018`, `343456`, `231741`
        - `type` — `string`  e.g. `image/png`, `image/jpeg`, `image/jpeg`
    - `created_at` — `object`
      - `$date` — `object`
        - `$numberlong` — `string`  e.g. `1777299921974`, `1777299921975`, `1777299921976`
    - `option_count` — `object`
      - `$numberint` — `string`  e.g. `3`
    - `options` — `object` (nullable)
      - `a` — `string`  e.g. `<p>4</p>`, `<p>  Dinoseb </p>`, `<p>  MCA  </p>`
      - `b` — `string`  e.g. `<p>5</p>`, `<p> Nitrofen</p>`, `<p>   TCA</p>`
      - `c` — `string`  e.g. `<p>6</p>`, `<p>  Pendimethalin </p>`, `<p>Dicamba</p>`
      - `d` — `string`  e.g. `<p>7</p>`, `<p> Oxadiazon </p>`, `<p>   Dalapon</p>`
    - `question_type` — `string`  e.g. `MCQ_SINGLE_CORRECT`, `MCQ_SINGLE_CORRECT`, `MCQ_SINGLE_CORRECT`
    - `text` — `string`  e.g. `<p>What is 2+2?</p>`, `<p>Incidence of stem rot of groundnut reduced by-</p>`, `<p>The only chloro-propionic acid herbicide-</p>`
    - `updated_at` — `object`
      - `$date` — `object`
        - `$numberlong` — `string`  e.g. `1774902526219`, `1777006576880`, `1777305959957`

## DDL

```sql
CREATE EXTERNAL TABLE `processed.exam_service__tests`(
  `_id` string, 
  `active` string, 
  `display_results` string, 
  `status` string, 
  `_type` string, 
  `name` string, 
  `class_id` string, 
  `user_id` string, 
  `jumbled_questions` string, 
  `mock_test` string, 
  `disable_commenting` string, 
  `updated_at` string, 
  `created_at` string, 
  `test_question` string, 
  `answers` string, 
  `question_count` string, 
  `correct_marks` string, 
  `description` string, 
  `duration` string, 
  `end_time` string, 
  `incorrect_marks` string, 
  `max_marks` string, 
  `start_time` string, 
  `analysis` string, 
  `total_present` string, 
  `questions` string, 
  `publish_results` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/exam-service/tests/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260428_001002_00045_zt2z8', 
  'trino_version'='0.215-24582-g0575ac4')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
