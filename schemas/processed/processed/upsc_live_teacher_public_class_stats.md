---
database: processed
table: upsc_live_teacher_public_class_stats
type: view
layer: processed
location: null
format: null
partition_keys: []
last_synced: '2026-04-28T07:12:49+00:00'
sampled_rows: 0
---

# `processed.upsc_live_teacher_public_class_stats`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `userid` | `string` |  |
| `name` | `string` |  |
| `phonenumber` | `string` |  |
| `classes` | `bigint` |  |
| `classrooms_since_days` | `bigint` |  |
| `max_students_in_one_class` | `bigint` |  |
| `assignments_last_week` | `bigint` |  |
| `tests_last_week` | `bigint` |  |
| `live_class_last_week` | `bigint` |  |
| `announcements_last_week` | `bigint` |  |
| `assignment_submissions_last_week` | `bigint` |  |
| `test_submissions_last_week` | `bigint` |  |
| `live_class_participants_last_week` | `bigint` |  |
| `announcement_comments_last_week` | `bigint` |  |
| `assignments_last2last_week` | `bigint` |  |
| `tests_last2last_week` | `bigint` |  |
| `live_class_last2last_week` | `bigint` |  |
| `announcements_last2last_week` | `bigint` |  |
| `assignment_submissions_last2last_week` | `bigint` |  |
| `test_submissions_last2last_week` | `bigint` |  |
| `live_class_participants_last2last_week` | `bigint` |  |
| `announcement_comments_last2last_week` | `bigint` |  |
| `assignments_last_month` | `bigint` |  |
| `tests_last_month` | `bigint` |  |
| `live_class_last_month` | `bigint` |  |
| `announcements_last_month` | `bigint` |  |
| `assignment_submissions_last_month` | `bigint` |  |
| `test_submissions_last_month` | `bigint` |  |
| `live_class_participants_last_month` | `bigint` |  |
| `announcement_comments_last_month` | `bigint` |  |
| `assignments_last2last_month` | `bigint` |  |
| `tests_last2last_month` | `bigint` |  |
| `live_class_last2last_month` | `bigint` |  |
| `announcements_last2last_month` | `bigint` |  |
| `assignment_submissions_last2last_month` | `bigint` |  |
| `test_submissions_last2last_month` | `bigint` |  |
| `live_class_participants_last2last_month` | `bigint` |  |
| `announcement_comments_last2last_month` | `bigint` |  |

## DDL

```sql
CREATE VIEW processed.upsc_live_teacher_public_class_stats AS
SELECT
  b.userid
, b.name
, b.phonenumber
, "count"(DISTINCT a.class_id) classes
, "max"("date_diff"('day', "date"(a.createdat), current_date)) classrooms_since_days
, "max"(num_joinedrequest) max_students_in_one_class
, "sum"(assignments_last_week) assignments_last_week
, "sum"(tests_last_week) tests_last_week
, "sum"(live_class_last_week) live_class_last_week
, "sum"(announcements_last_week) announcements_last_week
, "sum"(assignment_submissions_last_week) assignment_submissions_last_week
, "sum"(test_submissions_last_week) test_submissions_last_week
, "sum"(live_class_participants_last_week) live_class_participants_last_week
, "sum"(announcement_comments_last_week) announcement_comments_last_week
, "sum"(assignments_last2last_week) assignments_last2last_week
, "sum"(tests_last2last_week) tests_last2last_week
, "sum"(live_class_last2last_week) live_class_last2last_week
, "sum"(announcements_last2last_week) announcements_last2last_week
, "sum"(assignment_submissions_last2last_week) assignment_submissions_last2last_week
, "sum"(test_submissions_last2last_week) test_submissions_last2last_week
, "sum"(live_class_participants_last2last_week) live_class_participants_last2last_week
, "sum"(announcement_comments_last2last_week) announcement_comments_last2last_week
, "sum"(assignments_last_month) assignments_last_month
, "sum"(tests_last_month) tests_last_month
, "sum"(live_class_last_month) live_class_last_month
, "sum"(announcements_last_month) announcements_last_month
, "sum"(assignment_submissions_last_month) assignment_submissions_last_month
, "sum"(test_submissions_last_month) test_submissions_last_month
, "sum"(live_class_participants_last_month) live_class_participants_last_month
, "sum"(announcement_comments_last_month) announcement_comments_last_month
, "sum"(assignments_last2last_month) assignments_last2last_month
, "sum"(tests_last2last_month) tests_last2last_month
, "sum"(live_class_last2last_month) live_class_last2last_month
, "sum"(announcements_last2last_month) announcements_last2last_month
, "sum"(assignment_submissions_last2last_month) assignment_submissions_last2last_month
, "sum"(test_submissions_last2last_month) test_submissions_last2last_month
, "sum"(live_class_participants_last2last_month) live_class_participants_last2last_month
, "sum"(announcement_comments_last2last_month) announcement_comments_last2last_month
FROM
  ((((((
   SELECT
     class_id
   , createdat
   , just_classnumber
   , userid
   , archived
   , name
   , subject
   , num_joinedrequest
   , num_coteachers
   FROM
     processed.class
   WHERE (((namespace = 'wise_upsc') AND (archived = 'false')) AND (settings_openclassroom = 'true'))
)  a
LEFT JOIN (
   SELECT
     userid
   , name
   , phonenumber
   FROM
     processed.user
   WHERE (namespace = 'wise_upsc')
)  b ON (a.userid = b.userid))
LEFT JOIN (
   SELECT
     userid
   , classid
   , "sum"((CASE WHEN ("date"(createdat) > (current_date - INTERVAL  '8' DAY)) THEN 1 ELSE 0 END)) assignments_last_week
   , "sum"((CASE WHEN (("date"(createdat) > (current_date - INTERVAL  '15' DAY)) AND ("date"(createdat) < (current_date - INTERVAL  '7' DAY))) THEN 1 ELSE 0 END)) assignments_last2last_week
   , "sum"((CASE WHEN ("date"(createdat) > (current_date - INTERVAL  '31' DAY)) THEN 1 ELSE 0 END)) assignments_last_month
   , "sum"((CASE WHEN (("date"(createdat) > (current_date - INTERVAL  '61' DAY)) AND ("date"(createdat) < (current_date - INTERVAL  '30' DAY))) THEN 1 ELSE 0 END)) assignments_last2last_month
   , "sum"((CASE WHEN ("date"(createdat) > (current_date - INTERVAL  '8' DAY)) THEN num_submissions ELSE 0 END)) assignment_submissions_last_week
   , "sum"((CASE WHEN (("date"(createdat) > (current_date - INTERVAL  '15' DAY)) AND ("date"(createdat) < (current_date - INTERVAL  '7' DAY))) THEN num_submissions ELSE 0 END)) assignment_submissions_last2last_week
   , "sum"((CASE WHEN ("date"(createdat) > (current_date - INTERVAL  '31' DAY)) THEN num_submissions ELSE 0 END)) assignment_submissions_last_month
   , "sum"((CASE WHEN (("date"(createdat) > (current_date - INTERVAL  '61' DAY)) AND ("date"(createdat) < (current_date - INTERVAL  '30' DAY))) THEN num_submissions ELSE 0 END)) assignment_submissions_last2last_month
   FROM
     processed.assignments
   GROUP BY 1, 2
)  ass ON (ass.classid = a.class_id))
LEFT JOIN (
   SELECT
     userid
   , classid
   , "sum"((CASE WHEN ("date"(createdat) > (current_date - INTERVAL  '8' DAY)) THEN 1 ELSE 0 END)) tests_last_week
   , "sum"((CASE WHEN (("date"(createdat) > (current_date - INTERVAL  '15' DAY)) AND ("date"(createdat) < (current_date - INTERVAL  '7' DAY))) THEN 1 ELSE 0 END)) tests_last2last_week
   , "sum"((CASE WHEN ("date"(createdat) > (current_date - INTERVAL  '31' DAY)) THEN 1 ELSE 0 END)) tests_last_month
   , "sum"((CASE WHEN (("date"(createdat) > (current_date - INTERVAL  '61' DAY)) AND ("date"(createdat) < (current_date - INTERVAL  '30' DAY))) THEN 1 ELSE 0 END)) tests_last2last_month
   , "sum"((CASE WHEN ("date"(createdat) > (current_date - INTERVAL  '8' DAY)) THEN num_submissions ELSE 0 END)) test_submissions_last_week
   , "sum"((CASE WHEN (("date"(createdat) > (current_date - INTERVAL  '15' DAY)) AND ("date"(createdat) < (current_date - INTERVAL  '7' DAY))) THEN num_submissions ELSE 0 END)) test_submissions_last2last_week
   , "sum"((CASE WHEN ("date"(createdat) > (current_date - INTERVAL  '31' DAY)) THEN num_submissions ELSE 0 END)) test_submissions_last_month
   , "sum"((CASE WHEN (("date"(createdat) > (current_date - INTERVAL  '61' DAY)) AND ("date"(createdat) < (current_date - INTERVAL  '30' DAY))) THEN num_submissions ELSE 0 END)) test_submissions_last2last_month
   FROM
     processed.tests
   GROUP BY 1, 2
)  tst ON (tst.classid = a.class_id))
LEFT JOIN (
   SELECT
     userid
   , classid
   , "sum"((CASE WHEN ("date"(createdat) > (current_date - INTERVAL  '8' DAY)) THEN 1 ELSE 0 END)) live_class_last_week
   , "sum"((CASE WHEN (("date"(createdat) > (current_date - INTERVAL  '15' DAY)) AND ("date"(createdat) < (current_date - INTERVAL  '7' DAY))) THEN 1 ELSE 0 END)) live_class_last2last_week
   , "sum"((CASE WHEN ("date"(createdat) > (current_date - INTERVAL  '31' DAY)) THEN 1 ELSE 0 END)) live_class_last_month
   , "sum"((CASE WHEN (("date"(createdat) > (current_date - INTERVAL  '61' DAY)) AND ("date"(createdat) < (current_date - INTERVAL  '30' DAY))) THEN 1 ELSE 0 END)) live_class_last2last_month
   , "sum"((CASE WHEN ("date"(createdat) > (current_date - INTERVAL  '8' DAY)) THEN participant ELSE 0 END)) live_class_participants_last_week
   , "sum"((CASE WHEN (("date"(createdat) > (current_date - INTERVAL  '15' DAY)) AND ("date"(createdat) < (current_date - INTERVAL  '7' DAY))) THEN participant ELSE 0 END)) live_class_participants_last2last_week
   , "sum"((CASE WHEN ("date"(createdat) > (current_date - INTERVAL  '31' DAY)) THEN participant ELSE 0 END)) live_class_participants_last_month
   , "sum"((CASE WHEN (("date"(createdat) > (current_date - INTERVAL  '61' DAY)) AND ("date"(createdat) < (current_date - INTERVAL  '30' DAY))) THEN participant ELSE 0 END)) live_class_participants_last2last_month
   FROM
     processed.zoomers
   GROUP BY 1, 2
)  zoom ON (zoom.classid = a.class_id))
LEFT JOIN (
   SELECT
     userid
   , classid
   , "sum"((CASE WHEN ("date"(createdat) > (current_date - INTERVAL  '8' DAY)) THEN 1 ELSE 0 END)) announcements_last_week
   , "sum"((CASE WHEN (("date"(createdat) > (current_date - INTERVAL  '15' DAY)) AND ("date"(createdat) < (current_date - INTERVAL  '7' DAY))) THEN 1 ELSE 0 END)) announcements_last2last_week
   , "sum"((CASE WHEN ("date"(createdat) > (current_date - INTERVAL  '31' DAY)) THEN 1 ELSE 0 END)) announcements_last_month
   , "sum"((CASE WHEN (("date"(createdat) > (current_date - INTERVAL  '61' DAY)) AND ("date"(createdat) < (current_date - INTERVAL  '30' DAY))) THEN 1 ELSE 0 END)) announcements_last2last_month
   , "sum"((CASE WHEN ("date"(createdat) > (current_date - INTERVAL  '8' DAY)) THEN comments ELSE 0 END)) announcement_comments_last_week
   , "sum"((CASE WHEN (("date"(createdat) > (current_date - INTERVAL  '15' DAY)) AND ("date"(createdat) < (current_date - INTERVAL  '7' DAY))) THEN comments ELSE 0 END)) announcement_comments_last2last_week
   , "sum"((CASE WHEN ("date"(createdat) > (current_date - INTERVAL  '31' DAY)) THEN comments ELSE 0 END)) announcement_comments_last_month
   , "sum"((CASE WHEN (("date"(createdat) > (current_date - INTERVAL  '61' DAY)) AND ("date"(createdat) < (current_date - INTERVAL  '30' DAY))) THEN comments ELSE 0 END)) announcement_comments_last2last_month
   FROM
     processed.announcements
   GROUP BY 1, 2
)  ann ON (ann.classid = a.class_id))
GROUP BY 1, 2, 3
ORDER BY 1 ASC
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
