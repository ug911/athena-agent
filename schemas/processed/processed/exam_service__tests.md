---
canonical: processed
table: exam_service__tests
type: table
layer: processed
regions:
  in: processed
  na: processed_na
location: s3://[REDACTED-BUCKET]/processed/exam-service/tests/
format: INPUTFORMAT
partition_keys: []
schema_parity: identical
last_synced: '2026-08-11T13:15:45+00:00'
sampled_rows: 200
sampled_region: in
---

# `processed.exam_service__tests`

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

_String columns with ≤20 distinct values in 200 sampled rows from `IN`. Distribution shown as `value (×count)`._

- `active`: `true (×197)`, `false (×3)`
- `display_results`: `true (×200)`
- `status`: `ACTIVE (×195)`, `DRAFT (×5)`
- `_type`: `UserInputOmrTest (×148)`, `OmrTest (×52)`
- `jumbled_questions`: `false (×200)`
- `mock_test`: `true (×195)`, `false (×5)`
- `disable_commenting`: `false (×200)`
- `description`: `Another test about our planet (×20)`, `Here are some questions about forests and animals (×15)`, `Test about galaxy facts and features (×15)`, `Test about our planet (×10)`, `Test your knowledge on wildlife and ecosystems. (×5)`, `Another test about solar system planets (×5)`, `A test about solar system planets (×5)`, `Use of calculators is strictly not allowed during the test. Malpractice will lead to immediate disqualification. (×4)`, `Complete during tutoring. (×1)`, `Complete before next week (×1)`, `BIOLOGY (10-08-26) (×1)`, `DPT-M-40  Inverse Trigonometric Functions - 10.08.26 (×1)`, `DPT B-6 Molecular Basis Of Inheritance-  Replication 10-08-26 (×1)`, `DPT-P-50 Significant Figures, Rounding off and Order of Magnitude + Vernier Callipers  10-08-26 (×1)`, `DPT-P-51 Significant Figures, Rounding off and Order of Magnitude + Vernier Callipers  10-08-26 (×1)`

## Inferred JSON structure

_Inferred from 200 sampled rows from `IN` on 2026-08-11. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `6a7a3fc217b47e0001d686bf`, `6a7a3e94c65e5c0001f5ef99`, `6a7a3df117b47e0001d68672`

### `class_id`

- `$oid` — `string`  e.g. `67facb4381c96ece3b36660f`, `67facb4381c96ece3b36660f`, `6a7a3df0cf11c6de7f445d2a`

### `user_id`

- `$oid` — `string`  e.g. `67e5941b1212d98ff5fc467f`, `67e5941b1212d98ff5fc467f`, `6a7a3df0cf11c6de7f445cd8`

### `updated_at`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1786397619532`, `1786398842731`, `1786396145453`

### `created_at`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1786397496429`, `1786396395104`, `1786396145453`

### `test_question`

  - `[]` — `object`
    - `_id` — `object`
      - `$oid` — `string`  e.g. `69f6512afb9af90001d427f1`, `69dc13c5ee0b01000170dfa4`, `6a7a085479f8a7000125dfaf`
    - `filename` — `string`  e.g. `ACT H31 Reading Part 2.pdf`, `ACT H31 Part 1.pdf`, `iSkew Verbal 50 minutes.pdf`
    - `path` — `string`  e.g. `https://files.wiseapp.live/upload_files/67eb9399f218d7da9f77`, `https://files.wiseapp.live/upload_files/67eb9399f218d7da9f77`, `https://files.wiseapp.live/upload_files/6955460d28118f629e0b`
    - `question_type` — `string`  e.g. `ATTACHMENT`, `ATTACHMENT`, `ATTACHMENT`
    - `s3_filepath` — `string`  e.g. `https://wise-app-s3-bucket.s3-ap-south-1.amazonaws.com/uploa`, `https://wise-app-s3-bucket.s3-ap-south-1.amazonaws.com/uploa`, `https://wise-app-s3-bucket.s3-ap-south-1.amazonaws.com/uploa`
    - `s3_key` — `string`  e.g. `upload_files/67eb9399f218d7da9f776ac8/upload_035aad92-5ec0-4`, `upload_files/67eb9399f218d7da9f776ac8/upload_67306beb-1115-4`, `upload_files/6955460d28118f629e0b8403/upload_9d164ad8-88be-4`
    - `size` — `object`
      - `$numberint` — `string`  e.g. `695827`, `422596`, `197011`
    - `type` — `string`  e.g. `application/pdf`, `application/pdf`, `application/pdf`

### `answers`

- `<oid>` — `string`  e.g. `c`, `b`, `a`

### `duration`

- `$numberint` — `string`  e.g. `21`, `17`, `20`

### `end_time`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1787290800000`

### `max_marks`

- `$numberint` — `string`  e.g. `30`, `17`, `10`

### `start_time`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1787290200000`

### `analysis`

- `<oid>` — `object`
  - `attempted_by` — `object`
    - `$numberint` — `string`  e.g. `1`, `2`, `23`
  - `attempted_correctly` — `object`
    - `$numberint` — `string`  e.g. `1`, `0`, `2`

### `total_present`

- `$numberint` — `string`  e.g. `1`, `1`, `1`

### `questions`

  - `[]` — `object`
    - `_id` — `object`
      - `$oid` — `string`  e.g. `6a7a432ac65e5c0001f5ef9c`, `6a7a432ac65e5c0001f5ef9d`, `6a7a432ac65e5c0001f5ef9e`
    - `_type` — `string`  e.g. `OmrQuestion`, `OmrQuestion`, `OmrQuestion`
    - `archived` — `bool`  e.g. `false`, `false`, `false`
    - `attachments` — `array<object>`
      - `[].attachments[]` — `object`
        - `_id` — `object`
          - `$oid` — `string`  e.g. `6a7a140d79f8a7000125dffb`
        - `filename` — `string`  e.g. `Knowleggia Flyer 1.png`
        - `path` — `string`  e.g. `https://files.wiseapp.live/upload_files/6a5f20db2ad8f3b4389a`
        - `s3_filepath` — `string`  e.g. `https://wise-app-s3-bucket.s3-ap-south-1.amazonaws.com/uploa`
        - `s3_key` — `string`  e.g. `upload_files/6a5f20db2ad8f3b4389a5f81/upload_b056f104-603c-4`
        - `size` — `object`
          - `$numberint` — `string`  e.g. `415048`
        - `type` — `string`  e.g. `image/png`
    - `created_at` — `object`
      - `$date` — `object`
        - `$numberlong` — `string`  e.g. `1786397482811`, `1786397482812`, `1786397482812`
    - `options` — `object`
      - `a` — `string`  e.g. `a`, `a`, `a`
      - `b` — `string`  e.g. `b`, `b`, `b`
      - `c` — `string`  e.g. `c`, `c`, `c`
      - `d` — `string`  e.g. `d`, `d`, `d`
      - `e` — `string`  e.g. `e`, `e`, `e`
    - `question_type` — `string`  e.g. `MCQ_SINGLE_CORRECT`, `MCQ_SINGLE_CORRECT`, `MCQ_SINGLE_CORRECT`
    - `text` — `string`  e.g. `What is the largest forest in the world?`, `Which of the following is NOT a type of forest biome?`, `What is the Earth's largest continent by area?`
    - `updated_at` — `object`
      - `$date` — `object`
        - `$numberlong` — `string`  e.g. `1786397482811`, `1786397482812`, `1786397482812`

## DDL

_From `IN` (processed)._

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
  'trino_query_id'='20260811_000930_00025_3kvci', 
  'trino_version'='0.215-24619-g93e00a8')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
