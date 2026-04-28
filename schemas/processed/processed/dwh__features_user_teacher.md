---
database: processed
table: dwh__features_user_teacher
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/processed/features_user_teacher/process_date=2026-004-27/
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:10:36+00:00'
sampled_rows: 200
---

# `processed.dwh__features_user_teacher`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `userid` | `string` |  |
| `name` | `string` |  |
| `phonenumber` | `string` |  |
| `email` | `string` |  |
| `profile` | `string` |  |
| `namespace` | `string` |  |
| `licensed` | `string` |  |
| `license_plantype` | `string` |  |
| `createdat` | `date` |  |
| `licenseexpireat` | `string` |  |
| `lastloggedinon` | `date` |  |
| `lastmeetingstartedon` | `date` |  |
| `days_since_user` | `bigint` |  |
| `days_since_login` | `bigint` |  |
| `days_since_lastmeeting` | `bigint` |  |
| `classes` | `bigint` |  |
| `class_students` | `bigint` |  |
| `class_num_students_per_class` | `double` |  |
| `class_low_students` | `bigint` |  |
| `class_med_students` | `bigint` |  |
| `class_high_students` | `bigint` |  |
| `class_days_since_last_class` | `bigint` |  |
| `class_days_since_first_class` | `bigint` |  |
| `classes_first_7` | `bigint` |  |
| `classes_next_7` | `bigint` |  |
| `classes_first_14` | `bigint` |  |
| `classes_next_14` | `bigint` |  |
| `classes_first_30` | `bigint` |  |
| `classes_next_30` | `bigint` |  |
| `classes_first_60` | `bigint` |  |
| `class_num_students_first_7` | `bigint` |  |
| `class_num_students_next_7` | `bigint` |  |
| `class_num_students_first_14` | `bigint` |  |
| `class_num_students_next_14` | `bigint` |  |
| `class_num_students_first_30` | `bigint` |  |
| `class_num_students_next_30` | `bigint` |  |
| `class_num_students_first_60` | `bigint` |  |
| `classes_last_7` | `bigint` |  |
| `classes_last2last_7` | `bigint` |  |
| `classes_last_14` | `bigint` |  |
| `classes_last2last_14` | `bigint` |  |
| `classes_last_30` | `bigint` |  |
| `classes_last2last_30` | `bigint` |  |
| `classes_last_60` | `bigint` |  |
| `class_num_students_last_7` | `bigint` |  |
| `class_num_students_last2last_7` | `bigint` |  |
| `class_num_students_last_14` | `bigint` |  |
| `class_num_students_last2last_14` | `bigint` |  |
| `class_num_students_last_30` | `bigint` |  |
| `class_num_students_last2last_30` | `bigint` |  |
| `class_num_students_last_60` | `bigint` |  |
| `announcements` | `bigint` |  |
| `announcement_comments` | `bigint` |  |
| `announcement_comments_per_announcement` | `double` |  |
| `announcement_classes` | `bigint` |  |
| `announcement_low_comments` | `bigint` |  |
| `announcement_med_comments` | `bigint` |  |
| `announcement_high_comments` | `bigint` |  |
| `announcement_days_since_last_announcement` | `bigint` |  |
| `announcement_days_since_first_announcement` | `bigint` |  |
| `announcements_first_7` | `bigint` |  |
| `announcements_next_7` | `bigint` |  |
| `announcements_first_14` | `bigint` |  |
| `announcements_next_14` | `bigint` |  |
| `announcements_first_30` | `bigint` |  |
| `announcements_next_30` | `bigint` |  |
| `announcements_first_60` | `bigint` |  |
| `announcement_comments_first_7` | `bigint` |  |
| `announcement_comments_next_7` | `bigint` |  |
| `announcement_comments_first_14` | `bigint` |  |
| `announcement_comments_next_14` | `bigint` |  |
| `announcement_comments_first_30` | `bigint` |  |
| `announcement_comments_next_30` | `bigint` |  |
| `announcement_comments_first_60` | `bigint` |  |
| `announcements_last_7` | `bigint` |  |
| `announcements_last2last_7` | `bigint` |  |
| `announcements_last_14` | `bigint` |  |
| `announcements_last2last_14` | `bigint` |  |
| `announcements_last_30` | `bigint` |  |
| `announcements_last2last_30` | `bigint` |  |
| `announcements_last_60` | `bigint` |  |
| `announcement_comments_last_7` | `bigint` |  |
| `announcement_comments_last2last_7` | `bigint` |  |
| `announcement_comments_last_14` | `bigint` |  |
| `announcement_comments_last2last_14` | `bigint` |  |
| `announcement_comments_last_30` | `bigint` |  |
| `announcement_comments_last2last_30` | `bigint` |  |
| `announcement_comments_last_60` | `bigint` |  |
| `assignments` | `bigint` |  |
| `assignment_submissions` | `bigint` |  |
| `assignment_num_submissions_per_assignment` | `double` |  |
| `assignment_classes` | `bigint` |  |
| `assignment_low_submissions` | `bigint` |  |
| `assignment_med_submissions` | `bigint` |  |
| `assignment_high_submissions` | `bigint` |  |
| `assignment_days_since_last_assignment` | `bigint` |  |
| `assignment_days_since_first_assignment` | `bigint` |  |
| `assignments_first_7` | `bigint` |  |
| `assignments_next_7` | `bigint` |  |
| `assignments_first_14` | `bigint` |  |
| `assignments_next_14` | `bigint` |  |
| `assignments_first_30` | `bigint` |  |
| `assignments_next_30` | `bigint` |  |
| `assignments_first_60` | `bigint` |  |
| `assignment_num_submissions_first_7` | `bigint` |  |
| `assignment_num_submissions_next_7` | `bigint` |  |
| `assignment_num_submissions_first_14` | `bigint` |  |
| `assignment_num_submissions_next_14` | `bigint` |  |
| `assignment_num_submissions_first_30` | `bigint` |  |
| `assignment_num_submissions_next_30` | `bigint` |  |
| `assignment_num_submissions_first_60` | `bigint` |  |
| `assignments_last_7` | `bigint` |  |
| `assignments_last2last_7` | `bigint` |  |
| `assignments_last_14` | `bigint` |  |
| `assignments_last2last_14` | `bigint` |  |
| `assignments_last_30` | `bigint` |  |
| `assignments_last2last_30` | `bigint` |  |
| `assignments_last_60` | `bigint` |  |
| `assignment_num_submissions_last_7` | `bigint` |  |
| `assignment_num_submissions_last2last_7` | `bigint` |  |
| `assignment_num_submissions_last_14` | `bigint` |  |
| `assignment_num_submissions_last2last_14` | `bigint` |  |
| `assignment_num_submissions_last_30` | `bigint` |  |
| `assignment_num_submissions_last2last_30` | `bigint` |  |
| `assignment_num_submissions_last_60` | `bigint` |  |
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
| `tests` | `bigint` |  |
| `test_submissions` | `bigint` |  |
| `test_num_submissions_per_test` | `double` |  |
| `test_classes` | `bigint` |  |
| `test_low_submissions` | `bigint` |  |
| `test_med_submissions` | `bigint` |  |
| `test_high_submissions` | `bigint` |  |
| `test_days_since_last_test` | `bigint` |  |
| `test_days_since_first_test` | `bigint` |  |
| `tests_first_7` | `bigint` |  |
| `tests_next_7` | `bigint` |  |
| `tests_first_14` | `bigint` |  |
| `tests_next_14` | `bigint` |  |
| `tests_first_30` | `bigint` |  |
| `tests_next_30` | `bigint` |  |
| `tests_first_60` | `bigint` |  |
| `test_num_submissions_first_7` | `bigint` |  |
| `test_num_submissions_next_7` | `bigint` |  |
| `test_num_submissions_first_14` | `bigint` |  |
| `test_num_submissions_next_14` | `bigint` |  |
| `test_num_submissions_first_30` | `bigint` |  |
| `test_num_submissions_next_30` | `bigint` |  |
| `test_num_submissions_first_60` | `bigint` |  |
| `tests_last_7` | `bigint` |  |
| `tests_last2last_7` | `bigint` |  |
| `tests_last_14` | `bigint` |  |
| `tests_last2last_14` | `bigint` |  |
| `tests_last_30` | `bigint` |  |
| `tests_last2last_30` | `bigint` |  |
| `tests_last_60` | `bigint` |  |
| `test_num_submissions_last_7` | `bigint` |  |
| `test_num_submissions_last2last_7` | `bigint` |  |
| `test_num_submissions_last_14` | `bigint` |  |
| `test_num_submissions_last2last_14` | `bigint` |  |
| `test_num_submissions_last_30` | `bigint` |  |
| `test_num_submissions_last2last_30` | `bigint` |  |
| `test_num_submissions_last_60` | `bigint` |  |
| `zooms` | `bigint` |  |
| `zoom_avg_duration` | `double` |  |
| `zoom_avg_participants` | `double` |  |
| `zoom_participants` | `bigint` |  |
| `zoom_participants_per_zoom` | `double` |  |
| `zoom_classes` | `bigint` |  |
| `zoom_low_participants` | `bigint` |  |
| `zoom_med_participants` | `bigint` |  |
| `zoom_high_participants` | `bigint` |  |
| `zoom_days_since_last_zoom` | `bigint` |  |
| `zoom_days_since_first_zoom` | `bigint` |  |
| `zooms_first_7` | `bigint` |  |
| `zooms_next_7` | `bigint` |  |
| `zooms_first_14` | `bigint` |  |
| `zooms_next_14` | `bigint` |  |
| `zooms_first_30` | `bigint` |  |
| `zooms_next_30` | `bigint` |  |
| `zooms_first_60` | `bigint` |  |
| `zoom_participant_first_7` | `bigint` |  |
| `zoom_participant_next_7` | `bigint` |  |
| `zoom_participant_first_14` | `bigint` |  |
| `zoom_participant_next_14` | `bigint` |  |
| `zoom_participant_first_30` | `bigint` |  |
| `zoom_participant_next_30` | `bigint` |  |
| `zoom_participant_first_60` | `bigint` |  |
| `zooms_last_7` | `bigint` |  |
| `zooms_last2last_7` | `bigint` |  |
| `zooms_last_14` | `bigint` |  |
| `zooms_last2last_14` | `bigint` |  |
| `zooms_last_30` | `bigint` |  |
| `zooms_last2last_30` | `bigint` |  |
| `zooms_last_60` | `bigint` |  |
| `zoom_participant_last_7` | `bigint` |  |
| `zoom_participant_last2last_7` | `bigint` |  |
| `zoom_participant_last_14` | `bigint` |  |
| `zoom_participant_last2last_14` | `bigint` |  |
| `zoom_participant_last_30` | `bigint` |  |
| `zoom_participant_last2last_30` | `bigint` |  |
| `zoom_participant_last_60` | `bigint` |  |

## Enum-like columns

_String columns with ≤20 distinct values in 200 sampled rows. Distribution shown as `value (×count)`._

- `profile`: `student (×170)`, `teacher (×30)`
- `namespace`: `wise (×200)`

## DDL

```sql
CREATE EXTERNAL TABLE `processed.dwh__features_user_teacher`(
  `userid` string, 
  `name` string, 
  `phonenumber` string, 
  `email` string, 
  `profile` string, 
  `namespace` string, 
  `licensed` string, 
  `license_plantype` string, 
  `createdat` date, 
  `licenseexpireat` string, 
  `lastloggedinon` date, 
  `lastmeetingstartedon` date, 
  `days_since_user` bigint, 
  `days_since_login` bigint, 
  `days_since_lastmeeting` bigint, 
  `classes` bigint, 
  `class_students` bigint, 
  `class_num_students_per_class` double, 
  `class_low_students` bigint, 
  `class_med_students` bigint, 
  `class_high_students` bigint, 
  `class_days_since_last_class` bigint, 
  `class_days_since_first_class` bigint, 
  `classes_first_7` bigint, 
  `classes_next_7` bigint, 
  `classes_first_14` bigint, 
  `classes_next_14` bigint, 
  `classes_first_30` bigint, 
  `classes_next_30` bigint, 
  `classes_first_60` bigint, 
  `class_num_students_first_7` bigint, 
  `class_num_students_next_7` bigint, 
  `class_num_students_first_14` bigint, 
  `class_num_students_next_14` bigint, 
  `class_num_students_first_30` bigint, 
  `class_num_students_next_30` bigint, 
  `class_num_students_first_60` bigint, 
  `classes_last_7` bigint, 
  `classes_last2last_7` bigint, 
  `classes_last_14` bigint, 
  `classes_last2last_14` bigint, 
  `classes_last_30` bigint, 
  `classes_last2last_30` bigint, 
  `classes_last_60` bigint, 
  `class_num_students_last_7` bigint, 
  `class_num_students_last2last_7` bigint, 
  `class_num_students_last_14` bigint, 
  `class_num_students_last2last_14` bigint, 
  `class_num_students_last_30` bigint, 
  `class_num_students_last2last_30` bigint, 
  `class_num_students_last_60` bigint, 
  `announcements` bigint, 
  `announcement_comments` bigint, 
  `announcement_comments_per_announcement` double, 
  `announcement_classes` bigint, 
  `announcement_low_comments` bigint, 
  `announcement_med_comments` bigint, 
  `announcement_high_comments` bigint, 
  `announcement_days_since_last_announcement` bigint, 
  `announcement_days_since_first_announcement` bigint, 
  `announcements_first_7` bigint, 
  `announcements_next_7` bigint, 
  `announcements_first_14` bigint, 
  `announcements_next_14` bigint, 
  `announcements_first_30` bigint, 
  `announcements_next_30` bigint, 
  `announcements_first_60` bigint, 
  `announcement_comments_first_7` bigint, 
  `announcement_comments_next_7` bigint, 
  `announcement_comments_first_14` bigint, 
  `announcement_comments_next_14` bigint, 
  `announcement_comments_first_30` bigint, 
  `announcement_comments_next_30` bigint, 
  `announcement_comments_first_60` bigint, 
  `announcements_last_7` bigint, 
  `announcements_last2last_7` bigint, 
  `announcements_last_14` bigint, 
  `announcements_last2last_14` bigint, 
  `announcements_last_30` bigint, 
  `announcements_last2last_30` bigint, 
  `announcements_last_60` bigint, 
  `announcement_comments_last_7` bigint, 
  `announcement_comments_last2last_7` bigint, 
  `announcement_comments_last_14` bigint, 
  `announcement_comments_last2last_14` bigint, 
  `announcement_comments_last_30` bigint, 
  `announcement_comments_last2last_30` bigint, 
  `announcement_comments_last_60` bigint, 
  `assignments` bigint, 
  `assignment_submissions` bigint, 
  `assignment_num_submissions_per_assignment` double, 
  `assignment_classes` bigint, 
  `assignment_low_submissions` bigint, 
  `assignment_med_submissions` bigint, 
  `assignment_high_submissions` bigint, 
  `assignment_days_since_last_assignment` bigint, 
  `assignment_days_since_first_assignment` bigint, 
  `assignments_first_7` bigint, 
  `assignments_next_7` bigint, 
  `assignments_first_14` bigint, 
  `assignments_next_14` bigint, 
  `assignments_first_30` bigint, 
  `assignments_next_30` bigint, 
  `assignments_first_60` bigint, 
  `assignment_num_submissions_first_7` bigint, 
  `assignment_num_submissions_next_7` bigint, 
  `assignment_num_submissions_first_14` bigint, 
  `assignment_num_submissions_next_14` bigint, 
  `assignment_num_submissions_first_30` bigint, 
  `assignment_num_submissions_next_30` bigint, 
  `assignment_num_submissions_first_60` bigint, 
  `assignments_last_7` bigint, 
  `assignments_last2last_7` bigint, 
  `assignments_last_14` bigint, 
  `assignments_last2last_14` bigint, 
  `assignments_last_30` bigint, 
  `assignments_last2last_30` bigint, 
  `assignments_last_60` bigint, 
  `assignment_num_submissions_last_7` bigint, 
  `assignment_num_submissions_last2last_7` bigint, 
  `assignment_num_submissions_last_14` bigint, 
  `assignment_num_submissions_last2last_14` bigint, 
  `assignment_num_submissions_last_30` bigint, 
  `assignment_num_submissions_last2last_30` bigint, 
  `assignment_num_submissions_last_60` bigint, 
  `study_materials` bigint, 
  `study_materials_upload_files` bigint, 
  `study_materials_session_recordings` bigint, 
  `study_materials_video_player` bigint, 
  `study_materials_drive` bigint, 
  `study_materials_youtube` bigint, 
  `study_materials_links` bigint, 
  `study_material_classes` bigint, 
  `study_material_in_resource_library` bigint, 
  `study_materials_last_7` bigint, 
  `study_materials_last2last_7` bigint, 
  `study_materials_last_14` bigint, 
  `study_materials_last2last_14` bigint, 
  `study_materials_last_30` bigint, 
  `study_materials_last2last_30` bigint, 
  `study_materials_last_60` bigint, 
  `study_material_days_since_first_study_material` bigint, 
  `study_material_days_since_last_study_material` bigint, 
  `study_materials_first_7` bigint, 
  `study_materials_next_7` bigint, 
  `study_materials_first_14` bigint, 
  `study_materials_next_14` bigint, 
  `study_materials_first_30` bigint, 
  `study_materials_next_30` bigint, 
  `study_materials_first_60` bigint, 
  `study_materials_last_7_session_recordings` bigint, 
  `study_materials_last2last_7_session_recordings` bigint, 
  `study_materials_last_14_session_recordings` bigint, 
  `study_materials_last2last_14_session_recordings` bigint, 
  `study_materials_last_30_session_recordings` bigint, 
  `study_materials_last2last_30_session_recordings` bigint, 
  `study_materials_last_60_session_recordings` bigint, 
  `study_materials_first_7_session_recordings` bigint, 
  `study_materials_next_7_session_recordings` bigint, 
  `study_materials_first_14_session_recordings` bigint, 
  `study_materials_next_14_session_recordings` bigint, 
  `study_materials_first_30_session_recordings` bigint, 
  `study_materials_next_30_session_recordings` bigint, 
  `study_materials_first_60_session_recordings` bigint, 
  `study_materials_last_7_video_player` bigint, 
  `study_materials_last2last_7_video_player` bigint, 
  `study_materials_last_14_video_player` bigint, 
  `study_materials_last2last_14_video_player` bigint, 
  `study_materials_last_30_video_player` bigint, 
  `study_materials_last2last_30_video_player` bigint, 
  `study_materials_last_60_video_player` bigint, 
  `study_materials_first_7_video_player` bigint, 
  `study_materials_next_7_video_player` bigint, 
  `study_materials_first_14_video_player` bigint, 
  `study_materials_next_14_video_player` bigint, 
  `study_materials_first_30_video_player` bigint, 
  `study_materials_next_30_video_player` bigint, 
  `study_materials_first_60_video_player` bigint, 
  `tests` bigint, 
  `test_submissions` bigint, 
  `test_num_submissions_per_test` double, 
  `test_classes` bigint, 
  `test_low_submissions` bigint, 
  `test_med_submissions` bigint, 
  `test_high_submissions` bigint, 
  `test_days_since_last_test` bigint, 
  `test_days_since_first_test` bigint, 
  `tests_first_7` bigint, 
  `tests_next_7` bigint, 
  `tests_first_14` bigint, 
  `tests_next_14` bigint, 
  `tests_first_30` bigint, 
  `tests_next_30` bigint, 
  `tests_first_60` bigint, 
  `test_num_submissions_first_7` bigint, 
  `test_num_submissions_next_7` bigint, 
  `test_num_submissions_first_14` bigint, 
  `test_num_submissions_next_14` bigint, 
  `test_num_submissions_first_30` bigint, 
  `test_num_submissions_next_30` bigint, 
  `test_num_submissions_first_60` bigint, 
  `tests_last_7` bigint, 
  `tests_last2last_7` bigint, 
  `tests_last_14` bigint, 
  `tests_last2last_14` bigint, 
  `tests_last_30` bigint, 
  `tests_last2last_30` bigint, 
  `tests_last_60` bigint, 
  `test_num_submissions_last_7` bigint, 
  `test_num_submissions_last2last_7` bigint, 
  `test_num_submissions_last_14` bigint, 
  `test_num_submissions_last2last_14` bigint, 
  `test_num_submissions_last_30` bigint, 
  `test_num_submissions_last2last_30` bigint, 
  `test_num_submissions_last_60` bigint, 
  `zooms` bigint, 
  `zoom_avg_duration` double, 
  `zoom_avg_participants` double, 
  `zoom_participants` bigint, 
  `zoom_participants_per_zoom` double, 
  `zoom_classes` bigint, 
  `zoom_low_participants` bigint, 
  `zoom_med_participants` bigint, 
  `zoom_high_participants` bigint, 
  `zoom_days_since_last_zoom` bigint, 
  `zoom_days_since_first_zoom` bigint, 
  `zooms_first_7` bigint, 
  `zooms_next_7` bigint, 
  `zooms_first_14` bigint, 
  `zooms_next_14` bigint, 
  `zooms_first_30` bigint, 
  `zooms_next_30` bigint, 
  `zooms_first_60` bigint, 
  `zoom_participant_first_7` bigint, 
  `zoom_participant_next_7` bigint, 
  `zoom_participant_first_14` bigint, 
  `zoom_participant_next_14` bigint, 
  `zoom_participant_first_30` bigint, 
  `zoom_participant_next_30` bigint, 
  `zoom_participant_first_60` bigint, 
  `zooms_last_7` bigint, 
  `zooms_last2last_7` bigint, 
  `zooms_last_14` bigint, 
  `zooms_last2last_14` bigint, 
  `zooms_last_30` bigint, 
  `zooms_last2last_30` bigint, 
  `zooms_last_60` bigint, 
  `zoom_participant_last_7` bigint, 
  `zoom_participant_last2last_7` bigint, 
  `zoom_participant_last_14` bigint, 
  `zoom_participant_last2last_14` bigint, 
  `zoom_participant_last_30` bigint, 
  `zoom_participant_last2last_30` bigint, 
  `zoom_participant_last_60` bigint)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/features_user_teacher/process_date=2026-004-27/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260428_015326_00322_f326i', 
  'trino_version'='0.215-24582-g0575ac4')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
