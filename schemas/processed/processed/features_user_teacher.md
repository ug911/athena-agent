---
database: processed
table: features_user_teacher
type: view
layer: processed
location: null
format: null
partition_keys: []
last_synced: '2026-04-28T07:10:50+00:00'
sampled_rows: 0
---

# `processed.features_user_teacher`

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

## DDL

```sql
CREATE VIEW processed.features_user_teacher AS
SELECT
  u.userid
, name
, phonenumber
, email
, profile
, namespace
, licensed
, license_plantype
, createdat
, licenseexpireat
, lastloggedinon
, lastmeetingstartedon
, "date_diff"('day', createdat, current_date) days_since_user
, "date_diff"('day', lastloggedinon, current_date) days_since_login
, "date_diff"('day', lastmeetingstartedon, current_date) days_since_lastmeeting
, classes
, class_students
, class_num_students_per_class
, class_low_students
, class_med_students
, class_high_students
, class_days_since_last_class
, class_days_since_first_class
, classes_first_7
, classes_next_7
, classes_first_14
, classes_next_14
, classes_first_30
, classes_next_30
, classes_first_60
, class_num_students_first_7
, class_num_students_next_7
, class_num_students_first_14
, class_num_students_next_14
, class_num_students_first_30
, class_num_students_next_30
, class_num_students_first_60
, classes_last_7
, classes_last2last_7
, classes_last_14
, classes_last2last_14
, classes_last_30
, classes_last2last_30
, classes_last_60
, class_num_students_last_7
, class_num_students_last2last_7
, class_num_students_last_14
, class_num_students_last2last_14
, class_num_students_last_30
, class_num_students_last2last_30
, class_num_students_last_60
, announcements
, announcement_comments
, announcement_comments_per_announcement
, announcement_classes
, announcement_low_comments
, announcement_med_comments
, announcement_high_comments
, announcement_days_since_last_announcement
, announcement_days_since_first_announcement
, announcements_first_7
, announcements_next_7
, announcements_first_14
, announcements_next_14
, announcements_first_30
, announcements_next_30
, announcements_first_60
, announcement_comments_first_7
, announcement_comments_next_7
, announcement_comments_first_14
, announcement_comments_next_14
, announcement_comments_first_30
, announcement_comments_next_30
, announcement_comments_first_60
, announcements_last_7
, announcements_last2last_7
, announcements_last_14
, announcements_last2last_14
, announcements_last_30
, announcements_last2last_30
, announcements_last_60
, announcement_comments_last_7
, announcement_comments_last2last_7
, announcement_comments_last_14
, announcement_comments_last2last_14
, announcement_comments_last_30
, announcement_comments_last2last_30
, announcement_comments_last_60
, assignments
, assignment_submissions
, assignment_num_submissions_per_assignment
, assignment_classes
, assignment_low_submissions
, assignment_med_submissions
, assignment_high_submissions
, assignment_days_since_last_assignment
, assignment_days_since_first_assignment
, assignments_first_7
, assignments_next_7
, assignments_first_14
, assignments_next_14
, assignments_first_30
, assignments_next_30
, assignments_first_60
, assignment_num_submissions_first_7
, assignment_num_submissions_next_7
, assignment_num_submissions_first_14
, assignment_num_submissions_next_14
, assignment_num_submissions_first_30
, assignment_num_submissions_next_30
, assignment_num_submissions_first_60
, assignments_last_7
, assignments_last2last_7
, assignments_last_14
, assignments_last2last_14
, assignments_last_30
, assignments_last2last_30
, assignments_last_60
, assignment_num_submissions_last_7
, assignment_num_submissions_last2last_7
, assignment_num_submissions_last_14
, assignment_num_submissions_last2last_14
, assignment_num_submissions_last_30
, assignment_num_submissions_last2last_30
, assignment_num_submissions_last_60
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
, study_materials_last2last_7
, study_materials_last_14
, study_materials_last2last_14
, study_materials_last_30
, study_materials_last2last_30
, study_materials_last_60
, study_material_days_since_first_study_material
, study_material_days_since_last_study_material
, study_materials_first_7
, study_materials_next_7
, study_materials_first_14
, study_materials_next_14
, study_materials_first_30
, study_materials_next_30
, study_materials_first_60
, study_materials_last_7_session_recordings
, study_materials_last2last_7_session_recordings
, study_materials_last_14_session_recordings
, study_materials_last2last_14_session_recordings
, study_materials_last_30_session_recordings
, study_materials_last2last_30_session_recordings
, study_materials_last_60_session_recordings
, study_materials_first_7_session_recordings
, study_materials_next_7_session_recordings
, study_materials_first_14_session_recordings
, study_materials_next_14_session_recordings
, study_materials_first_30_session_recordings
, study_materials_next_30_session_recordings
, study_materials_first_60_session_recordings
, study_materials_last_7_video_player
, study_materials_last2last_7_video_player
, study_materials_last_14_video_player
, study_materials_last2last_14_video_player
, study_materials_last_30_video_player
, study_materials_last2last_30_video_player
, study_materials_last_60_video_player
, study_materials_first_7_video_player
, study_materials_next_7_video_player
, study_materials_first_14_video_player
, study_materials_next_14_video_player
, study_materials_first_30_video_player
, study_materials_next_30_video_player
, study_materials_first_60_video_player
, tests
, test_submissions
, test_num_submissions_per_test
, test_classes
, test_low_submissions
, test_med_submissions
, test_high_submissions
, test_days_since_last_test
, test_days_since_first_test
, tests_first_7
, tests_next_7
, tests_first_14
, tests_next_14
, tests_first_30
, tests_next_30
, tests_first_60
, test_num_submissions_first_7
, test_num_submissions_next_7
, test_num_submissions_first_14
, test_num_submissions_next_14
, test_num_submissions_first_30
, test_num_submissions_next_30
, test_num_submissions_first_60
, tests_last_7
, tests_last2last_7
, tests_last_14
, tests_last2last_14
, tests_last_30
, tests_last2last_30
, tests_last_60
, test_num_submissions_last_7
, test_num_submissions_last2last_7
, test_num_submissions_last_14
, test_num_submissions_last2last_14
, test_num_submissions_last_30
, test_num_submissions_last2last_30
, test_num_submissions_last_60
, zooms
, zoom_avg_duration
, zoom_avg_participants
, zoom_participants
, zoom_participants_per_zoom
, zoom_classes
, zoom_low_participants
, zoom_med_participants
, zoom_high_participants
, zoom_days_since_last_zoom
, zoom_days_since_first_zoom
, zooms_first_7
, zooms_next_7
, zooms_first_14
, zooms_next_14
, zooms_first_30
, zooms_next_30
, zooms_first_60
, zoom_participant_first_7
, zoom_participant_next_7
, zoom_participant_first_14
, zoom_participant_next_14
, zoom_participant_first_30
, zoom_participant_next_30
, zoom_participant_first_60
, zooms_last_7
, zooms_last2last_7
, zooms_last_14
, zooms_last2last_14
, zooms_last_30
, zooms_last2last_30
, zooms_last_60
, zoom_participant_last_7
, zoom_participant_last2last_7
, zoom_participant_last_14
, zoom_participant_last2last_14
, zoom_participant_last_30
, zoom_participant_last2last_30
, zoom_participant_last_60
FROM
  (((((((
   SELECT *
   FROM
     user
)  u
LEFT JOIN (
   SELECT *
   FROM
     ft_teacher_class
)  c ON (u.userid = c.userid))
LEFT JOIN (
   SELECT *
   FROM
     ft_teacher_announcements
)  d ON (u.userid = d.userid))
LEFT JOIN (
   SELECT *
   FROM
     ft_teacher_assignments
)  a ON (u.userid = a.userid))
LEFT JOIN (
   SELECT *
   FROM
     ft_teacher_study_materials
)  s ON (u.userid = s.userid))
LEFT JOIN (
   SELECT *
   FROM
     ft_teacher_tests
)  t ON (u.userid = t.userid))
LEFT JOIN (
   SELECT *
   FROM
     ft_teacher_zooms
)  z ON (u.userid = z.userid))
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
