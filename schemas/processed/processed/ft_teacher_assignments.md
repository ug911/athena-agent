---
database: processed
table: ft_teacher_assignments
type: view
layer: processed
location: null
format: null
partition_keys: []
last_synced: '2026-04-28T07:11:07+00:00'
sampled_rows: 0
---

# `processed.ft_teacher_assignments`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `userid` | `string` |  |
| `days_since_user` | `bigint` |  |
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

## DDL

```sql
CREATE VIEW processed.ft_teacher_assignments AS
SELECT
  userid
, days_since_user
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
, (assignments_first_14 - assignments_first_7) assignments_next_7
, assignments_first_14
, (assignments_first_30 - assignments_first_14) assignments_next_14
, assignments_first_30
, (assignments_first_60 - assignments_first_30) assignments_next_30
, assignments_first_60
, assignment_num_submissions_first_7
, (assignment_num_submissions_first_14 - assignment_num_submissions_first_7) assignment_num_submissions_next_7
, assignment_num_submissions_first_14
, (assignment_num_submissions_first_30 - assignment_num_submissions_first_14) assignment_num_submissions_next_14
, assignment_num_submissions_first_30
, (assignment_num_submissions_first_60 - assignment_num_submissions_first_30) assignment_num_submissions_next_30
, assignment_num_submissions_first_60
, assignments_last_7
, (assignments_last_14 - assignments_last_7) assignments_last2last_7
, assignments_last_14
, (assignments_last_30 - assignments_last_14) assignments_last2last_14
, assignments_last_30
, (assignments_last_60 - assignments_last_30) assignments_last2last_30
, assignments_last_60
, assignment_num_submissions_last_7
, (assignment_num_submissions_last_14 - assignment_num_submissions_last_7) assignment_num_submissions_last2last_7
, assignment_num_submissions_last_14
, (assignment_num_submissions_last_30 - assignment_num_submissions_last_14) assignment_num_submissions_last2last_14
, assignment_num_submissions_last_30
, (assignment_num_submissions_last_60 - assignment_num_submissions_last_30) assignment_num_submissions_last2last_30
, assignment_num_submissions_last_60
FROM
  (
   SELECT
     a.userid
   , days_since_user
   , "count"(*) assignments
   , "sum"(num_submissions) assignment_submissions
   , "round"(((1E0 * "sum"(num_submissions)) / "count"(*))) assignment_num_submissions_per_assignment
   , "count"(DISTINCT classid) assignment_classes
   , "sum"((CASE WHEN (num_submissions < 5) THEN 1 ELSE 0 END)) assignment_low_submissions
   , "sum"((CASE WHEN (num_submissions BETWEEN 5 AND 9) THEN 1 ELSE 0 END)) assignment_med_submissions
   , "sum"((CASE WHEN (num_submissions > 9) THEN 1 ELSE 0 END)) assignment_high_submissions
   , "sum"((CASE WHEN ("date"(a.createdat) > (current_date - INTERVAL  '8' DAY)) THEN 1 ELSE 0 END)) assignments_last_7
   , "sum"((CASE WHEN ("date"(a.createdat) > (current_date - INTERVAL  '15' DAY)) THEN 1 ELSE 0 END)) assignments_last_14
   , "sum"((CASE WHEN ("date"(a.createdat) > (current_date - INTERVAL  '31' DAY)) THEN 1 ELSE 0 END)) assignments_last_30
   , "sum"((CASE WHEN ("date"(a.createdat) > (current_date - INTERVAL  '61' DAY)) THEN 1 ELSE 0 END)) assignments_last_60
   , "sum"((CASE WHEN ("date"(a.createdat) > (current_date - INTERVAL  '8' DAY)) THEN num_submissions ELSE 0 END)) assignment_num_submissions_last_7
   , "sum"((CASE WHEN ("date"(a.createdat) > (current_date - INTERVAL  '15' DAY)) THEN num_submissions ELSE 0 END)) assignment_num_submissions_last_14
   , "sum"((CASE WHEN ("date"(a.createdat) > (current_date - INTERVAL  '31' DAY)) THEN num_submissions ELSE 0 END)) assignment_num_submissions_last_30
   , "sum"((CASE WHEN ("date"(a.createdat) > (current_date - INTERVAL  '61' DAY)) THEN num_submissions ELSE 0 END)) assignment_num_submissions_last_60
   , "date_diff"('day', "min"("date"(a.createdat)), current_date) assignment_days_since_first_assignment
   , "date_diff"('day', "max"("date"(a.createdat)), current_date) assignment_days_since_last_assignment
   , "sum"((CASE WHEN (a.createdat < (u.createdat + INTERVAL  '8' DAY)) THEN 1 ELSE 0 END)) assignments_first_7
   , "sum"((CASE WHEN (a.createdat < (u.createdat + INTERVAL  '15' DAY)) THEN 1 ELSE 0 END)) assignments_first_14
   , "sum"((CASE WHEN (a.createdat < (u.createdat + INTERVAL  '31' DAY)) THEN 1 ELSE 0 END)) assignments_first_30
   , "sum"((CASE WHEN (a.createdat < (u.createdat + INTERVAL  '61' DAY)) THEN 1 ELSE 0 END)) assignments_first_60
   , "sum"((CASE WHEN (a.createdat < (u.createdat + INTERVAL  '8' DAY)) THEN num_submissions ELSE 0 END)) assignment_num_submissions_first_7
   , "sum"((CASE WHEN (a.createdat < (u.createdat + INTERVAL  '15' DAY)) THEN num_submissions ELSE 0 END)) assignment_num_submissions_first_14
   , "sum"((CASE WHEN (a.createdat < (u.createdat + INTERVAL  '31' DAY)) THEN num_submissions ELSE 0 END)) assignment_num_submissions_first_30
   , "sum"((CASE WHEN (a.createdat < (u.createdat + INTERVAL  '61' DAY)) THEN num_submissions ELSE 0 END)) assignment_num_submissions_first_60
   FROM
     ((
      SELECT
        userid
      , classid
      , "date"(createdat) createdat
      , assignment_id
      , num_submissions
      FROM
        assignments
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
