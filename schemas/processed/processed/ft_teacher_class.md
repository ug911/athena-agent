---
database: processed
table: ft_teacher_class
type: view
layer: processed
location: null
format: null
partition_keys: []
last_synced: '2026-04-28T07:11:09+00:00'
sampled_rows: 0
---

# `processed.ft_teacher_class`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `userid` | `string` |  |
| `days_since_user` | `bigint` |  |
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

## DDL

```sql
CREATE VIEW processed.ft_teacher_class AS
SELECT
  userid
, days_since_user
, classes
, class_students
, class_num_students_per_class
, class_low_students
, class_med_students
, class_high_students
, class_days_since_last_class
, class_days_since_first_class
, classes_first_7
, (classes_first_14 - classes_first_7) classes_next_7
, classes_first_14
, (classes_first_30 - classes_first_14) classes_next_14
, classes_first_30
, (classes_first_60 - classes_first_30) classes_next_30
, classes_first_60
, class_num_students_first_7
, (class_num_students_first_14 - class_num_students_first_7) class_num_students_next_7
, class_num_students_first_14
, (class_num_students_first_30 - class_num_students_first_14) class_num_students_next_14
, class_num_students_first_30
, (class_num_students_first_60 - class_num_students_first_30) class_num_students_next_30
, class_num_students_first_60
, classes_last_7
, (classes_last_14 - classes_last_7) classes_last2last_7
, classes_last_14
, (classes_last_30 - classes_last_14) classes_last2last_14
, classes_last_30
, (classes_last_60 - classes_last_30) classes_last2last_30
, classes_last_60
, class_num_students_last_7
, (class_num_students_last_14 - class_num_students_last_7) class_num_students_last2last_7
, class_num_students_last_14
, (class_num_students_last_30 - class_num_students_last_14) class_num_students_last2last_14
, class_num_students_last_30
, (class_num_students_last_60 - class_num_students_last_30) class_num_students_last2last_30
, class_num_students_last_60
FROM
  (
   SELECT
     a.userid
   , days_since_user
   , "count"(*) classes
   , "sum"(num_joinedrequest) class_students
   , "round"(((1E0 * "sum"(num_joinedrequest)) / "count"(*))) class_num_students_per_class
   , "sum"((CASE WHEN (num_joinedrequest < 5) THEN 1 ELSE 0 END)) class_low_students
   , "sum"((CASE WHEN (num_joinedrequest BETWEEN 5 AND 9) THEN 1 ELSE 0 END)) class_med_students
   , "sum"((CASE WHEN (num_joinedrequest > 9) THEN 1 ELSE 0 END)) class_high_students
   , "sum"((CASE WHEN ("date"(a.createdat) > (current_date - INTERVAL  '8' DAY)) THEN 1 ELSE 0 END)) classes_last_7
   , "sum"((CASE WHEN ("date"(a.createdat) > (current_date - INTERVAL  '15' DAY)) THEN 1 ELSE 0 END)) classes_last_14
   , "sum"((CASE WHEN ("date"(a.createdat) > (current_date - INTERVAL  '31' DAY)) THEN 1 ELSE 0 END)) classes_last_30
   , "sum"((CASE WHEN ("date"(a.createdat) > (current_date - INTERVAL  '61' DAY)) THEN 1 ELSE 0 END)) classes_last_60
   , "sum"((CASE WHEN ("date"(a.createdat) > (current_date - INTERVAL  '8' DAY)) THEN num_joinedrequest ELSE 0 END)) class_num_students_last_7
   , "sum"((CASE WHEN ("date"(a.createdat) > (current_date - INTERVAL  '15' DAY)) THEN num_joinedrequest ELSE 0 END)) class_num_students_last_14
   , "sum"((CASE WHEN ("date"(a.createdat) > (current_date - INTERVAL  '31' DAY)) THEN num_joinedrequest ELSE 0 END)) class_num_students_last_30
   , "sum"((CASE WHEN ("date"(a.createdat) > (current_date - INTERVAL  '61' DAY)) THEN num_joinedrequest ELSE 0 END)) class_num_students_last_60
   , "date_diff"('day', "min"("date"(a.createdat)), current_date) class_days_since_first_class
   , "date_diff"('day', "max"("date"(a.createdat)), current_date) class_days_since_last_class
   , "sum"((CASE WHEN (a.createdat < (u.createdat + INTERVAL  '8' DAY)) THEN 1 ELSE 0 END)) classes_first_7
   , "sum"((CASE WHEN (a.createdat < (u.createdat + INTERVAL  '15' DAY)) THEN 1 ELSE 0 END)) classes_first_14
   , "sum"((CASE WHEN (a.createdat < (u.createdat + INTERVAL  '31' DAY)) THEN 1 ELSE 0 END)) classes_first_30
   , "sum"((CASE WHEN (a.createdat < (u.createdat + INTERVAL  '61' DAY)) THEN 1 ELSE 0 END)) classes_first_60
   , "sum"((CASE WHEN (a.createdat < (u.createdat + INTERVAL  '8' DAY)) THEN num_joinedrequest ELSE 0 END)) class_num_students_first_7
   , "sum"((CASE WHEN (a.createdat < (u.createdat + INTERVAL  '15' DAY)) THEN num_joinedrequest ELSE 0 END)) class_num_students_first_14
   , "sum"((CASE WHEN (a.createdat < (u.createdat + INTERVAL  '31' DAY)) THEN num_joinedrequest ELSE 0 END)) class_num_students_first_30
   , "sum"((CASE WHEN (a.createdat < (u.createdat + INTERVAL  '61' DAY)) THEN num_joinedrequest ELSE 0 END)) class_num_students_first_60
   FROM
     ((
      SELECT
        userid
      , class_id
      , "date"(createdat) createdat
      , num_joinedrequest
      FROM
        class
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
