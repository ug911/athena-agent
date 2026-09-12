---
canonical: processed
table: study_materials
type: view
layer: processed
regions:
  in: processed
  na: processed_na
location: null
format: null
partition_keys: []
schema_parity: identical
last_synced: '2026-08-11T13:18:36+00:00'
sampled_rows: 0
sampled_region: null
---

# `processed.study_materials`

## Region availability

| Region | Athena database |
| --- | --- |
| `IN` | `processed` |
| `NA` | `processed_na` |

_Schema parity: **identical** across regions._

## Columns (IN)

| Column | Type | Notes |
| --- | --- | --- |
| `userid` | `string` |  |
| `classid` | `string` |  |
| `study_material_id` | `string` |  |
| `type` | `string` |  |
| `num_attachments` | `bigint` |  |
| `attachment_types` | `array<string>` |  |
| `attachment_subtypes` | `array<string>` |  |
| `attachment_fullurls` | `array<string>` |  |
| `attachment_urls` | `array<string>` |  |
| `attachment_filepaths` | `array<string>` |  |
| `createdat` | `date` |  |
| `youtubeurl` | `string` |  |
| `subtype` | `string` |  |
| `comments` | `string` |  |
| `file` | `string` |  |
| `lastcommentedat` | `string` |  |

## DDL

_From `IN` (processed)._

```sql
CREATE VIEW processed.study_materials AS
SELECT
  CAST("json_extract"(userid, '$["$oid"]') AS varchar) userid
, CAST("json_extract"(classid, '$["$oid"]') AS varchar) classid
, CAST("json_extract"(_id, '$["$oid"]') AS varchar) study_material_id
, type
, "cardinality"(CAST("json_parse"(resources) AS array(json))) num_attachments
, "transform"(CAST("json_parse"(resources) AS array(json)), (x) -> CAST("json_extract"(x, '$.type') AS varchar)) attachment_types
, "transform"(CAST("json_parse"(resources) AS array(json)), (x) -> CAST("json_extract"(x, '$.subtype') AS varchar)) attachment_subtypes
, "transform"(CAST("json_parse"(resources) AS array(json)), (x) -> CAST("json_extract"(x, '$.youtubeurl') AS varchar)) attachment_fullurls
, "transform"(CAST("json_parse"(resources) AS array(json)), (x) -> "element_at"("split"(CAST("json_extract"(x, '$.youtubeurl') AS varchar), '/'), 3)) attachment_urls
, "transform"(CAST("json_parse"(resources) AS array(json)), (x) -> "element_at"("split"(CAST("json_extract"(x, '$.file.path') AS varchar), '.'), "cardinality"("split"(CAST("json_extract"(x, '$.file.path') AS varchar), '.')))) attachment_filepaths
, "date"("from_unixtime"(TRY_CAST("substr"(TRY_CAST("json_extract"(createdat, '$["$date"]["$numberlong"]') AS varchar), 1, 10) AS double))) createdat
, youtubeurl
, subtype
, comments
, file
, lastcommentedat
FROM
  wise_app_backend__study_materials
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
