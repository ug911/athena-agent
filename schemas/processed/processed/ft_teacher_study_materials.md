---
database: processed
table: ft_teacher_study_materials
type: view
layer: processed
location: null
format: null
partition_keys: []
last_synced: '2026-04-28T07:11:12+00:00'
sampled_rows: 0
---

# `processed.ft_teacher_study_materials`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `userid` | `string` |  |
| `days_since_user` | `bigint` |  |
| `study_materials` | `bigint` |  |
| `study_materials_upload_files` | `bigint` |  |
| `study_materials_session_recordings` | `bigint` |  |
| `study_materials_video_player` | `bigint` |  |
| `study_materials_drive` | `bigint` |  |
| `study_materials_youtube` | `bigint` |  |
| `study_materials_links` | `bigint` |  |
| `study_material_classes` | `bigint` |  |
| `study_material_in_resource_library` | `bigint` |  |
| `study_materials_last_7` | `bigint` |  |
| `study_materials_last2last_7` | `bigint` |  |
| `study_materials_last_14` | `bigint` |  |
| `study_materials_last2last_14` | `bigint` |  |
| `study_materials_last_30` | `bigint` |  |
| `study_materials_last2last_30` | `bigint` |  |
| `study_materials_last_60` | `bigint` |  |
| `study_material_days_since_first_study_material` | `bigint` |  |
| `study_material_days_since_last_study_material` | `bigint` |  |
| `study_materials_first_7` | `bigint` |  |
| `study_materials_next_7` | `bigint` |  |
| `study_materials_first_14` | `bigint` |  |
| `study_materials_next_14` | `bigint` |  |
| `study_materials_first_30` | `bigint` |  |
| `study_materials_next_30` | `bigint` |  |
| `study_materials_first_60` | `bigint` |  |
| `study_materials_last_7_session_recordings` | `bigint` |  |
| `study_materials_last2last_7_session_recordings` | `bigint` |  |
| `study_materials_last_14_session_recordings` | `bigint` |  |
| `study_materials_last2last_14_session_recordings` | `bigint` |  |
| `study_materials_last_30_session_recordings` | `bigint` |  |
| `study_materials_last2last_30_session_recordings` | `bigint` |  |
| `study_materials_last_60_session_recordings` | `bigint` |  |
| `study_materials_first_7_session_recordings` | `bigint` |  |
| `study_materials_next_7_session_recordings` | `bigint` |  |
| `study_materials_first_14_session_recordings` | `bigint` |  |
| `study_materials_next_14_session_recordings` | `bigint` |  |
| `study_materials_first_30_session_recordings` | `bigint` |  |
| `study_materials_next_30_session_recordings` | `bigint` |  |
| `study_materials_first_60_session_recordings` | `bigint` |  |
| `study_materials_last_7_video_player` | `bigint` |  |
| `study_materials_last2last_7_video_player` | `bigint` |  |
| `study_materials_last_14_video_player` | `bigint` |  |
| `study_materials_last2last_14_video_player` | `bigint` |  |
| `study_materials_last_30_video_player` | `bigint` |  |
| `study_materials_last2last_30_video_player` | `bigint` |  |
| `study_materials_last_60_video_player` | `bigint` |  |
| `study_materials_first_7_video_player` | `bigint` |  |
| `study_materials_next_7_video_player` | `bigint` |  |
| `study_materials_first_14_video_player` | `bigint` |  |
| `study_materials_next_14_video_player` | `bigint` |  |
| `study_materials_first_30_video_player` | `bigint` |  |
| `study_materials_next_30_video_player` | `bigint` |  |
| `study_materials_first_60_video_player` | `bigint` |  |

## DDL

```sql
CREATE VIEW processed.ft_teacher_study_materials AS
SELECT
  userid
, days_since_user
, study_materials
, study_materials_upload_files
, study_materials_session_recordings
, study_materials_video_player
, study_materials_drive
, study_materials_youtube
, study_materials_links
, study_material_classes
, study_material_in_resource_library
, study_materials_last_7
, (study_materials_last_14 - study_materials_last_7) study_materials_last2last_7
, study_materials_last_14
, (study_materials_last_30 - study_materials_last_14) study_materials_last2last_14
, study_materials_last_30
, (study_materials_last_60 - study_materials_last_30) study_materials_last2last_30
, study_materials_last_60
, study_material_days_since_first_study_material
, study_material_days_since_last_study_material
, study_materials_first_7
, (study_materials_first_14 - study_materials_first_7) study_materials_next_7
, study_materials_first_14
, (study_materials_first_30 - study_materials_first_14) study_materials_next_14
, study_materials_first_30
, (study_materials_first_60 - study_materials_first_30) study_materials_next_30
, study_materials_first_60
, study_materials_last_7_session_recordings
, (study_materials_last_14_session_recordings - study_materials_last_7_session_recordings) study_materials_last2last_7_session_recordings
, study_materials_last_14_session_recordings
, (study_materials_last_30_session_recordings - study_materials_last_14_session_recordings) study_materials_last2last_14_session_recordings
, study_materials_last_30_session_recordings
, (study_materials_last_60_session_recordings - study_materials_last_30_session_recordings) study_materials_last2last_30_session_recordings
, study_materials_last_60_session_recordings
, study_materials_first_7_session_recordings
, (study_materials_first_14_session_recordings - study_materials_first_7_session_recordings) study_materials_next_7_session_recordings
, study_materials_first_14_session_recordings
, (study_materials_first_30_session_recordings - study_materials_first_14_session_recordings) study_materials_next_14_session_recordings
, study_materials_first_30_session_recordings
, (study_materials_first_60_session_recordings - study_materials_first_30_session_recordings) study_materials_next_30_session_recordings
, study_materials_first_60_session_recordings
, study_materials_last_7_video_player
, (study_materials_last_14_video_player - study_materials_last_7_video_player) study_materials_last2last_7_video_player
, study_materials_last_14_video_player
, (study_materials_last_30_video_player - study_materials_last_14_video_player) study_materials_last2last_14_video_player
, study_materials_last_30_video_player
, (study_materials_last_60_video_player - study_materials_last_30_video_player) study_materials_last2last_30_video_player
, study_materials_last_60_video_player
, study_materials_first_7_video_player
, (study_materials_first_14_video_player - study_materials_first_7_video_player) study_materials_next_7_video_player
, study_materials_first_14_video_player
, (study_materials_first_30_video_player - study_materials_first_14_video_player) study_materials_next_14_video_player
, study_materials_first_30_video_player
, (study_materials_first_60_video_player - study_materials_first_30_video_player) study_materials_next_30_video_player
, study_materials_first_60_video_player
FROM
  (
   SELECT
     a.userid
   , days_since_user
   , "count"(*) study_materials
   , "sum"((CASE WHEN (file_type = 'upload_files') THEN 1 ELSE 0 END)) study_materials_upload_files
   , "sum"((CASE WHEN (file_type = 'session_recordings') THEN 1 ELSE 0 END)) study_materials_session_recordings
   , "sum"((CASE WHEN (file_type = 'video_player') THEN 1 ELSE 0 END)) study_materials_video_player
   , "sum"((CASE WHEN (file_type = 'drive') THEN 1 ELSE 0 END)) study_materials_drive
   , "sum"((CASE WHEN (file_type = 'youtube') THEN 1 ELSE 0 END)) study_materials_youtube
   , "sum"((CASE WHEN (file_type = 'links') THEN 1 ELSE 0 END)) study_materials_links
   , "count"(DISTINCT classid) study_material_classes
   , "sum"((CASE WHEN (classid IS NULL) THEN 1 ELSE 0 END)) study_material_in_resource_library
   , "sum"((CASE WHEN ("date"(a.createdat) > (current_date - INTERVAL  '8' DAY)) THEN 1 ELSE 0 END)) study_materials_last_7
   , "sum"((CASE WHEN ("date"(a.createdat) > (current_date - INTERVAL  '15' DAY)) THEN 1 ELSE 0 END)) study_materials_last_14
   , "sum"((CASE WHEN ("date"(a.createdat) > (current_date - INTERVAL  '31' DAY)) THEN 1 ELSE 0 END)) study_materials_last_30
   , "sum"((CASE WHEN ("date"(a.createdat) > (current_date - INTERVAL  '61' DAY)) THEN 1 ELSE 0 END)) study_materials_last_60
   , "date_diff"('day', "min"("date"(a.createdat)), current_date) study_material_days_since_first_study_material
   , "date_diff"('day', "max"("date"(a.createdat)), current_date) study_material_days_since_last_study_material
   , "sum"((CASE WHEN (a.createdat < (u.createdat + INTERVAL  '8' DAY)) THEN 1 ELSE 0 END)) study_materials_first_7
   , "sum"((CASE WHEN (a.createdat < (u.createdat + INTERVAL  '15' DAY)) THEN 1 ELSE 0 END)) study_materials_first_14
   , "sum"((CASE WHEN (a.createdat < (u.createdat + INTERVAL  '31' DAY)) THEN 1 ELSE 0 END)) study_materials_first_30
   , "sum"((CASE WHEN (a.createdat < (u.createdat + INTERVAL  '61' DAY)) THEN 1 ELSE 0 END)) study_materials_first_60
   , "sum"((CASE WHEN (("date"(a.createdat) > (current_date - INTERVAL  '8' DAY)) AND (file_type = 'session_recordings')) THEN 1 ELSE 0 END)) study_materials_last_7_session_recordings
   , "sum"((CASE WHEN (("date"(a.createdat) > (current_date - INTERVAL  '15' DAY)) AND (file_type = 'session_recordings')) THEN 1 ELSE 0 END)) study_materials_last_14_session_recordings
   , "sum"((CASE WHEN (("date"(a.createdat) > (current_date - INTERVAL  '31' DAY)) AND (file_type = 'session_recordings')) THEN 1 ELSE 0 END)) study_materials_last_30_session_recordings
   , "sum"((CASE WHEN (("date"(a.createdat) > (current_date - INTERVAL  '61' DAY)) AND (file_type = 'session_recordings')) THEN 1 ELSE 0 END)) study_materials_last_60_session_recordings
   , "sum"((CASE WHEN ((a.createdat < (u.createdat + INTERVAL  '8' DAY)) AND (file_type = 'session_recordings')) THEN 1 ELSE 0 END)) study_materials_first_7_session_recordings
   , "sum"((CASE WHEN ((a.createdat < (u.createdat + INTERVAL  '15' DAY)) AND (file_type = 'session_recordings')) THEN 1 ELSE 0 END)) study_materials_first_14_session_recordings
   , "sum"((CASE WHEN ((a.createdat < (u.createdat + INTERVAL  '31' DAY)) AND (file_type = 'session_recordings')) THEN 1 ELSE 0 END)) study_materials_first_30_session_recordings
   , "sum"((CASE WHEN ((a.createdat < (u.createdat + INTERVAL  '61' DAY)) AND (file_type = 'session_recordings')) THEN 1 ELSE 0 END)) study_materials_first_60_session_recordings
   , "sum"((CASE WHEN (("date"(a.createdat) > (current_date - INTERVAL  '8' DAY)) AND (file_type = 'video_player')) THEN 1 ELSE 0 END)) study_materials_last_7_video_player
   , "sum"((CASE WHEN (("date"(a.createdat) > (current_date - INTERVAL  '15' DAY)) AND (file_type = 'video_player')) THEN 1 ELSE 0 END)) study_materials_last_14_video_player
   , "sum"((CASE WHEN (("date"(a.createdat) > (current_date - INTERVAL  '31' DAY)) AND (file_type = 'video_player')) THEN 1 ELSE 0 END)) study_materials_last_30_video_player
   , "sum"((CASE WHEN (("date"(a.createdat) > (current_date - INTERVAL  '61' DAY)) AND (file_type = 'video_player')) THEN 1 ELSE 0 END)) study_materials_last_60_video_player
   , "sum"((CASE WHEN ((a.createdat < (u.createdat + INTERVAL  '8' DAY)) AND (file_type = 'video_player')) THEN 1 ELSE 0 END)) study_materials_first_7_video_player
   , "sum"((CASE WHEN ((a.createdat < (u.createdat + INTERVAL  '15' DAY)) AND (file_type = 'video_player')) THEN 1 ELSE 0 END)) study_materials_first_14_video_player
   , "sum"((CASE WHEN ((a.createdat < (u.createdat + INTERVAL  '31' DAY)) AND (file_type = 'video_player')) THEN 1 ELSE 0 END)) study_materials_first_30_video_player
   , "sum"((CASE WHEN ((a.createdat < (u.createdat + INTERVAL  '61' DAY)) AND (file_type = 'video_player')) THEN 1 ELSE 0 END)) study_materials_first_60_video_player
   FROM
     ((
      SELECT
        userid
      , classid
      , "date"(createdat) createdat
      , study_material_id
      , file_type
      FROM
        study_materials_flat_v2
   )  a
   INNER JOIN (
      SELECT
        userid
      , createdat
      , "date_diff"('day', createdat, current_date) days_since_user
      FROM
        user
   )  u ON (a.userid = u.userid))
   GROUP BY 1, 2
)
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
