---
database: processed
table: webapp__marketing_templates
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/processed/webapp/marketing_templates/
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:13:10+00:00'
sampled_rows: 181
---

# `processed.webapp__marketing_templates`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` |  |
| `archived` | `string` |  |
| `html_template` | `string` |  |
| `preview_image` | `string` |  |
| `image_height` | `string` |  |
| `image_width` | `string` |  |
| `updated_at` | `string` |  |
| `created_at` | `string` |  |
| `template_variables` | `string` |  |
| `target` | `string` |  |
| `category` | `string` |  |

## Enum-like columns

_String columns with ≤20 distinct values in 181 sampled rows. Distribution shown as `value (×count)`._

- `archived`: `false (×99)`, `true (×82)`
- `target`: `all (×130)`, `teacher (×43)`, `student (×8)`
- `category`: `greeting (×72)`, `marketing (×69)`, `motivational (×21)`, `session (×5)`, `test (×5)`, `assessment (×5)`, `entity_test (×1)`, `entity_assessment (×1)`, `entity_generic_upsc (×1)`, `testing (×1)`

## Inferred JSON structure

_Inferred from 181 sampled rows on 2026-04-28. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `6076588a6268e508b124b515`, `62517ce374db6f0098e7663a`, `62260e0ad5e0de009ae8293e`

### `image_height`

- `$numberint` — `string`  e.g. `360`, `360`, `360`

### `image_width`

- `$numberint` — `string`  e.g. `360`, `360`, `360`

### `updated_at`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1681404650085`, `1680093155028`, `1678085530425`

### `created_at`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1681404650085`, `1680093155028`, `1678085530425`

### `template_variables`

  - `[]` — `object`
    - `_id` — `object`
      - `$oid` — `string`  e.g. `6076588a6268e508b124b516`, `62517ce374db6f0098e7663b`, `62260e0ad5e0de009ae8293f`
    - `char_limit` — `object`
      - `$numberint` — `string`  e.g. `20`, `25`, `25`
    - `default_value` — `string`  e.g. `How to start preparing for UPSC?`, `Live Session`, `by`
    - `display_name` — `string`  e.g. `[REDACTED]`
    - `name` — `string`  e.g. `user_name`, `user_name`, `user_name`
    - `type` — `string`  e.g. `TEXT`, `TEXT`, `TEXT`

## DDL

```sql
CREATE EXTERNAL TABLE `processed.webapp__marketing_templates`(
  `_id` string, 
  `archived` string, 
  `html_template` string, 
  `preview_image` string, 
  `image_height` string, 
  `image_width` string, 
  `updated_at` string, 
  `created_at` string, 
  `template_variables` string, 
  `target` string, 
  `category` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/webapp/marketing_templates/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260428_010727_00007_77phh', 
  'trino_version'='0.215-24582-g0575ac4')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
