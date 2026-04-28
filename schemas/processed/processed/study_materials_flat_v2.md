---
database: processed
table: study_materials_flat_v2
type: view
layer: processed
location: null
format: null
partition_keys: []
last_synced: '2026-04-28T07:12:31+00:00'
sampled_rows: 0
---

# `processed.study_materials_flat_v2`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `userid` | `string` |  |
| `classid` | `string` |  |
| `study_material_id` | `string` |  |
| `createdat` | `string` |  |
| `name` | `string` |  |
| `description` | `string` |  |
| `file_path` | `string` |  |
| `file_path_domain` | `string` |  |
| `file_type` | `varchar(18)` |  |

## DDL

```sql
CREATE VIEW processed.study_materials_flat_v2 AS
WITH
  data AS (
   SELECT
     userid
   , classid
   , CAST("json_extract"(r, '$[_id]["$oid"]') AS varchar) study_material_id
   , CAST("json_extract"(r, '$.file.path') AS varchar) file_path
   , "element_at"("split"((CASE WHEN (CAST("json_extract"(r, '$.file.path') AS varchar) IS NULL) THEN CAST("json_extract"(r, '$.youtubeurl') AS varchar) ELSE CAST("json_extract"(r, '$.file.path') AS varchar) END), '/'), 3) file_path_domain
   , "element_at"("split"((CASE WHEN (CAST("json_extract"(r, '$.file.path') AS varchar) IS NULL) THEN CAST("json_extract"(r, '$.youtubeurl') AS varchar) ELSE CAST("json_extract"(r, '$.file.path') AS varchar) END), '/'), 4) file_path_folder
   , (CASE WHEN (CAST("json_extract"(r, '$.file.type') AS varchar) IS NULL) THEN CAST("json_extract"(r, '$.type') AS varchar) ELSE CAST("json_extract"(r, '$.file.type') AS varchar) END) file_type
   , COALESCE("substr"(TRY_CAST("json_extract"(r, '$[createdat]["$date"]') AS varchar), 1, 10), CAST("date"("from_unixtime"(TRY_CAST("substr"(TRY_CAST("json_extract"(r, '$[createdat]["$date"]["$numberlong"]') AS varchar), 1, 10) AS double))) AS VARCHAR)) createdat
   , CAST("json_extract"(r, '$.name') AS varchar) name
   , CAST("json_extract"(r, '$.description') AS varchar) description
   FROM
     ((
      SELECT
        CAST("json_extract"(userid, '$["$oid"]') AS varchar) userid
      , CAST("json_extract"(classid, '$["$oid"]') AS varchar) classid
      , CAST("json_extract"(_id, '$["$oid"]') AS varchar) folder_id
      , CAST("json_parse"(resources) AS array(json)) rs
      FROM
        wise_app_backend__study_materials
      WHERE (type IN ('folder'))
   ) 
   CROSS JOIN UNNEST(rs) t (r))
UNION ALL (
      SELECT
        CAST("json_extract"(userid, '$["$oid"]') AS varchar) userid
      , CAST("json_extract"(classid, '$["$oid"]') AS varchar) classid
      , CAST("json_extract"(_id, '$["$oid"]') AS varchar) study_material_id
      , CAST("json_extract"(file, '$.path') AS varchar) file_path
      , "element_at"("split"(CAST("json_extract"(file, '$.path') AS varchar), '/'), 3) file_path_domain
      , "element_at"("split"(CAST("json_extract"(file, '$.path') AS varchar), '/'), 4) file_path_folder
      , CAST("json_extract"(file, '$.type') AS varchar) file_type
      , COALESCE("substr"(TRY_CAST("json_extract"(createdat, '$["$date"]') AS varchar), 1, 10), CAST("date"("from_unixtime"(TRY_CAST("substr"(TRY_CAST("json_extract"(createdat, '$["$date"]["$numberlong"]') AS varchar), 1, 10) AS double))) AS VARCHAR)) createdat
      , CAST("json_extract"(file, '$.name') AS varchar) name
      , CAST("json_extract"(file, '$.description') AS varchar) description
      FROM
        wise_app_backend__study_materials
      WHERE (type IN ('file'))
   ) UNION ALL (
      SELECT
        CAST("json_extract"(userid, '$["$oid"]') AS varchar) userid
      , CAST("json_extract"(classid, '$["$oid"]') AS varchar) classid
      , CAST("json_extract"(_id, '$["$oid"]') AS varchar) study_material_id
      , youtubeurl file_path
      , "element_at"("split"(youtubeurl, '/'), 3) file_path_domain
      , "element_at"("split"(youtubeurl, '/'), 3) file_path_folder
      , (CASE WHEN (youtubeurl LIKE '%youtu%') THEN 'youtube' WHEN (youtubeurl LIKE '%drive.google%') THEN 'drive' ELSE 'others' END) file_type
      , COALESCE("substr"(TRY_CAST("json_extract"(createdat, '$["$date"]') AS varchar), 1, 10), CAST("date"("from_unixtime"(TRY_CAST("substr"(TRY_CAST("json_extract"(createdat, '$["$date"]["$numberlong"]') AS varchar), 1, 10) AS double))) AS VARCHAR)) createdat
      , CAST("json_extract"(file, '$.name') AS varchar) name
      , CAST("json_extract"(file, '$.description') AS varchar) description
      FROM
        wise_app_backend__study_materials
      WHERE (type IN ('video'))
   ) ) 
SELECT
  userid
, classid
, study_material_id
, createdat
, name
, description
, file_path
, file_path_domain
, (CASE WHEN (file_path_folder = 'upload_files') THEN 'upload_files' WHEN (file_path_folder = 'session_recordings') THEN 'session_recordings' WHEN (file_path_folder = 'video-player') THEN 'video_player' WHEN (file_type = 'youtube') THEN 'youtube' WHEN (file_type = 'drive') THEN 'drive' ELSE 'links' END) file_type
FROM
  data
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
