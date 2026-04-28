---
database: processed
table: ft_teacher_tests
type: view
layer: processed
location: null
format: null
partition_keys: []
last_synced: '2026-04-28T07:11:16+00:00'
sampled_rows: 0
---

# `processed.ft_teacher_tests`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `userid` | `string` |  |
| `days_since_user` | `bigint` |  |
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

## DDL

```sql
CREATE VIEW processed.ft_teacher_tests AS
SELECT
  userid
, days_since_user
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
, (tests_first_14 - tests_first_7) tests_next_7
, tests_first_14
, (tests_first_30 - tests_first_14) tests_next_14
, tests_first_30
, (tests_first_60 - tests_first_30) tests_next_30
, tests_first_60
, test_num_submissions_first_7
, (test_num_submissions_first_14 - test_num_submissions_first_7) test_num_submissions_next_7
, test_num_submissions_first_14
, (test_num_submissions_first_30 - test_num_submissions_first_14) test_num_submissions_next_14
, test_num_submissions_first_30
, (test_num_submissions_first_60 - test_num_submissions_first_30) test_num_submissions_next_30
, test_num_submissions_first_60
, tests_last_7
, (tests_last_14 - tests_last_7) tests_last2last_7
, tests_last_14
, (tests_last_30 - tests_last_14) tests_last2last_14
, tests_last_30
, (tests_last_60 - tests_last_30) tests_last2last_30
, tests_last_60
, test_num_submissions_last_7
, (test_num_submissions_last_14 - test_num_submissions_last_7) test_num_submissions_last2last_7
, test_num_submissions_last_14
, (test_num_submissions_last_30 - test_num_submissions_last_14) test_num_submissions_last2last_14
, test_num_submissions_last_30
, (test_num_submissions_last_60 - test_num_submissions_last_30) test_num_submissions_last2last_30
, test_num_submissions_last_60
FROM
  (
   SELECT
     a.userid
   , days_since_user
   , "count"(*) tests
   , "sum"(num_submissions) test_submissions
   , "round"(((1E0 * "sum"(num_submissions)) / "count"(*))) test_num_submissions_per_test
   , "count"(DISTINCT classid) test_classes
   , "sum"((CASE WHEN (num_submissions < 5) THEN 1 ELSE 0 END)) test_low_submissions
   , "sum"((CASE WHEN (num_submissions BETWEEN 5 AND 9) THEN 1 ELSE 0 END)) test_med_submissions
   , "sum"((CASE WHEN (num_submissions > 9) THEN 1 ELSE 0 END)) test_high_submissions
   , "sum"((CASE WHEN ("date"(a.createdat) > (current_date - INTERVAL  '8' DAY)) THEN 1 ELSE 0 END)) tests_last_7
   , "sum"((CASE WHEN ("date"(a.createdat) > (current_date - INTERVAL  '15' DAY)) THEN 1 ELSE 0 END)) tests_last_14
   , "sum"((CASE WHEN ("date"(a.createdat) > (current_date - INTERVAL  '31' DAY)) THEN 1 ELSE 0 END)) tests_last_30
   , "sum"((CASE WHEN ("date"(a.createdat) > (current_date - INTERVAL  '61' DAY)) THEN 1 ELSE 0 END)) tests_last_60
   , "sum"((CASE WHEN ("date"(a.createdat) > (current_date - INTERVAL  '8' DAY)) THEN num_submissions ELSE 0 END)) test_num_submissions_last_7
   , "sum"((CASE WHEN ("date"(a.createdat) > (current_date - INTERVAL  '15' DAY)) THEN num_submissions ELSE 0 END)) test_num_submissions_last_14
   , "sum"((CASE WHEN ("date"(a.createdat) > (current_date - INTERVAL  '31' DAY)) THEN num_submissions ELSE 0 END)) test_num_submissions_last_30
   , "sum"((CASE WHEN ("date"(a.createdat) > (current_date - INTERVAL  '61' DAY)) THEN num_submissions ELSE 0 END)) test_num_submissions_last_60
   , "date_diff"('day', "min"("date"(a.createdat)), current_date) test_days_since_first_test
   , "date_diff"('day', "max"("date"(a.createdat)), current_date) test_days_since_last_test
   , "sum"((CASE WHEN (a.createdat < (u.createdat + INTERVAL  '8' DAY)) THEN 1 ELSE 0 END)) tests_first_7
   , "sum"((CASE WHEN (a.createdat < (u.createdat + INTERVAL  '15' DAY)) THEN 1 ELSE 0 END)) tests_first_14
   , "sum"((CASE WHEN (a.createdat < (u.createdat + INTERVAL  '31' DAY)) THEN 1 ELSE 0 END)) tests_first_30
   , "sum"((CASE WHEN (a.createdat < (u.createdat + INTERVAL  '61' DAY)) THEN 1 ELSE 0 END)) tests_first_60
   , "sum"((CASE WHEN (a.createdat < (u.createdat + INTERVAL  '8' DAY)) THEN num_submissions ELSE 0 END)) test_num_submissions_first_7
   , "sum"((CASE WHEN (a.createdat < (u.createdat + INTERVAL  '15' DAY)) THEN num_submissions ELSE 0 END)) test_num_submissions_first_14
   , "sum"((CASE WHEN (a.createdat < (u.createdat + INTERVAL  '31' DAY)) THEN num_submissions ELSE 0 END)) test_num_submissions_first_30
   , "sum"((CASE WHEN (a.createdat < (u.createdat + INTERVAL  '61' DAY)) THEN num_submissions ELSE 0 END)) test_num_submissions_first_60
   FROM
     ((
      SELECT
        userid
      , classid
      , "date"(createdat) createdat
      , testid
      , num_submissions
      FROM
        tests
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
