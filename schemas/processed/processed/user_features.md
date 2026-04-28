---
database: processed
table: user_features
type: view
layer: processed
location: null
format: null
partition_keys: []
last_synced: '2026-04-28T07:12:56+00:00'
sampled_rows: 0
---

# `processed.user_features`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `userid` | `string` |  |
| `name` | `string` |  |
| `phonenumber` | `string` |  |
| `profile` | `string` |  |
| `namespace` | `string` |  |
| `referralcode` | `string` |  |
| `announcements` | `bigint` |  |
| `announcements_14` | `bigint` |  |
| `announcements_29` | `bigint` |  |
| `announcements_classes` | `bigint` |  |
| `announcements_high` | `bigint` |  |
| `announcements_low` | `bigint` |  |
| `announcements_med` | `bigint` |  |
| `anouncement_teachers` | `bigint` |  |
| `assignments` | `bigint` |  |
| `assignments_14` | `bigint` |  |
| `assignments_29` | `bigint` |  |
| `assignments_classes` | `bigint` |  |
| `assignments_high` | `bigint` |  |
| `assignments_low` | `bigint` |  |
| `assignments_med` | `bigint` |  |
| `assignments_teachers` | `bigint` |  |
| `attended_zooms` | `bigint` |  |
| `attended_zooms_14` | `bigint` |  |
| `attended_zooms_29` | `bigint` |  |
| `attended_zooms_classes` | `bigint` |  |
| `attended_zooms_high` | `bigint` |  |
| `attended_zooms_low` | `bigint` |  |
| `attended_zooms_med` | `bigint` |  |
| `attended_zooms_teachers` | `bigint` |  |
| `attending_classes` | `bigint` |  |
| `attending_low_classes` | `bigint` |  |
| `attending_med_classes` | `bigint` |  |
| `attending_pow_classes` | `bigint` |  |
| `avg_attending_duration` | `double` |  |
| `avg_duration` | `double` |  |
| `avg_attending_participants` | `double` |  |
| `avg_participants` | `double` |  |
| `class_14` | `bigint` |  |
| `class_29` | `bigint` |  |
| `classes` | `bigint` |  |
| `commented_announcements` | `bigint` |  |
| `commented_announcements_14` | `bigint` |  |
| `commented_announcements_29` | `bigint` |  |
| `commented_announcements_classes` | `bigint` |  |
| `commented_announcements_high` | `bigint` |  |
| `commented_announcements_low` | `bigint` |  |
| `commented_announcements_med` | `bigint` |  |
| `commented_announcements_teachers` | `bigint` |  |
| `comments` | `bigint` |  |
| `comments_per_announcement` | `double` |  |
| `days_since_first_zoom_student` | `bigint` |  |
| `days_since_first_zoom` | `bigint` |  |
| `days_since_last_zoom_student` | `bigint` |  |
| `days_since_last_zoom` | `bigint` |  |
| `first_zoom_on_student` | `date` |  |
| `first_zoom_on` | `date` |  |
| `highest_strength` | `bigint` |  |
| `last_zoom_on_student` | `date` |  |
| `last_zoom_on` | `date` |  |
| `low_classes` | `bigint` |  |
| `med_classes` | `bigint` |  |
| `num_attachments` | `bigint` |  |
| `num_comments` | `bigint` |  |
| `num_submissions` | `bigint` |  |
| `pow_classes` | `bigint` |  |
| `students` | `bigint` |  |
| `students_class_14` | `bigint` |  |
| `students_class_29` | `bigint` |  |
| `study_materials` | `bigint` |  |
| `study_materials_14` | `bigint` |  |
| `study_materials_29` | `bigint` |  |
| `study_materials_classes` | `bigint` |  |
| `study_materials_teachers` | `bigint` |  |
| `num_assignment_submissions` | `bigint` |  |
| `num_test_submissions` | `bigint` |  |
| `submitted_assignments` | `bigint` |  |
| `submitted_assignments_14` | `bigint` |  |
| `submitted_assignments_29` | `bigint` |  |
| `submitted_assignments_classes` | `bigint` |  |
| `submitted_assignments_high` | `bigint` |  |
| `submitted_assignments_low` | `bigint` |  |
| `submitted_assignments_med` | `bigint` |  |
| `submitted_assignments_teachers` | `bigint` |  |
| `submitted_tests` | `bigint` |  |
| `submitted_tests_14` | `bigint` |  |
| `submitted_tests_29` | `bigint` |  |
| `submitted_tests_classes` | `bigint` |  |
| `submitted_tests_high` | `bigint` |  |
| `submitted_tests_low` | `bigint` |  |
| `submitted_tests_med` | `bigint` |  |
| `submitted_tests_teachers` | `bigint` |  |
| `test_classes` | `bigint` |  |
| `test_teachers` | `bigint` |  |
| `tests` | `bigint` |  |
| `tests_14` | `bigint` |  |
| `tests_29` | `bigint` |  |
| `tests_high` | `bigint` |  |
| `tests_low` | `bigint` |  |
| `tests_med` | `bigint` |  |
| `total_class_duration` | `bigint` |  |
| `total_duration` | `bigint` |  |
| `total_submissions` | `bigint` |  |
| `unique_study_materials` | `bigint` |  |
| `videos` | `bigint` |  |
| `youtubeurls` | `bigint` |  |
| `zoom_classes` | `bigint` |  |
| `zoom_teachers` | `bigint` |  |
| `zooms` | `bigint` |  |
| `zooms_14` | `bigint` |  |
| `zooms_29` | `bigint` |  |
| `zooms_high` | `bigint` |  |
| `zooms_low` | `bigint` |  |
| `zooms_med` | `bigint` |  |
| `days_since_first_study_materials` | `bigint` |  |
| `days_since_last_study_materials` | `bigint` |  |
| `days_since_first_announcement` | `bigint` |  |
| `days_since_last_announcement` | `bigint` |  |
| `days_since_first_assignment` | `bigint` |  |
| `days_since_last_assignment` | `bigint` |  |
| `days_since_first_test` | `bigint` |  |
| `days_since_last_test` | `bigint` |  |

## DDL

```sql
CREATE VIEW processed.user_features AS
SELECT
  a.userid
, name
, phonenumber
, profile
, namespace
, referralcode
, announcements
, announcements_14
, announcements_29
, announcements_classes
, announcements_high
, announcements_low
, announcements_med
, anouncement_teachers
, assignments
, assignments_14
, assignments_29
, assignments_classes
, assignments_high
, assignments_low
, assignments_med
, assignments_teachers
, attended_zooms
, attended_zooms_14
, attended_zooms_29
, attended_zooms_classes
, attended_zooms_high
, attended_zooms_low
, attended_zooms_med
, attended_zooms_teachers
, attending_classes
, attending_low_classes
, attending_med_classes
, attending_pow_classes
, avg_attending_duration
, avg_duration
, avg_attending_participants
, avg_participants
, class_14
, class_29
, classes
, commented_announcements
, commented_announcements_14
, commented_announcements_29
, commented_announcements_classes
, commented_announcements_high
, commented_announcements_low
, commented_announcements_med
, commented_announcements_teachers
, comments
, comments_per_announcement
, days_since_first_zoom_student
, days_since_first_zoom
, days_since_last_zoom_student
, days_since_last_zoom
, first_zoom_on_student
, first_zoom_on
, highest_strength
, last_zoom_on_student
, last_zoom_on
, low_classes
, med_classes
, num_attachments
, num_comments
, num_submissions
, pow_classes
, students
, students_class_14
, students_class_29
, study_materials
, study_materials_14
, study_materials_29
, study_materials_classes
, study_materials_teachers
, num_assignment_submissions
, num_test_submissions
, submitted_assignments
, submitted_assignments_14
, submitted_assignments_29
, submitted_assignments_classes
, submitted_assignments_high
, submitted_assignments_low
, submitted_assignments_med
, submitted_assignments_teachers
, submitted_tests
, submitted_tests_14
, submitted_tests_29
, submitted_tests_classes
, submitted_tests_high
, submitted_tests_low
, submitted_tests_med
, submitted_tests_teachers
, test_classes
, test_teachers
, tests
, tests_14
, tests_29
, tests_high
, tests_low
, tests_med
, total_class_duration
, total_duration
, total_submissions
, unique_study_materials
, videos
, youtubeurls
, zoom_classes
, zoom_teachers
, zooms
, zooms_14
, zooms_29
, zooms_high
, zooms_low
, zooms_med
, days_since_first_study_materials
, days_since_last_study_materials
, days_since_first_announcement
, days_since_last_announcement
, days_since_first_assignment
, days_since_last_assignment
, days_since_first_test
, days_since_last_test
FROM
  ((((((((((((
   SELECT *
   FROM
     user
)  a
LEFT JOIN (
   SELECT *
   FROM
     ft_teacher_announcements
)  b ON (b.userid = a.userid))
LEFT JOIN (
   SELECT *
   FROM
     ft_teacher_assignments
)  c ON (c.userid = a.userid))
LEFT JOIN (
   SELECT *
   FROM
     ft_student_zooms
)  d ON (d.userid = a.userid))
LEFT JOIN (
   SELECT *
   FROM
     ft_student_class
)  e ON (e.userid = a.userid))
LEFT JOIN (
   SELECT *
   FROM
     ft_teacher_zooms
)  f ON (f.userid = a.userid))
LEFT JOIN (
   SELECT *
   FROM
     ft_teacher_class
)  h ON (h.userid = a.userid))
LEFT JOIN (
   SELECT *
   FROM
     ft_student_announcements
)  i ON (i.userid = a.userid))
LEFT JOIN (
   SELECT *
   FROM
     ft_teacher_study_materials
)  j ON (j.userid = a.userid))
LEFT JOIN (
   SELECT *
   FROM
     ft_student_assignments
)  k ON (k.userid = a.userid))
LEFT JOIN (
   SELECT *
   FROM
     ft_student_tests
)  l ON (l.userid = a.userid))
LEFT JOIN (
   SELECT *
   FROM
     ft_teacher_tests
)  m ON (m.userid = a.userid))
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
