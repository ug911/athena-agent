---
database: processed
table: ft_student_tests
type: view
layer: processed
location: null
format: null
partition_keys: []
last_synced: '2026-04-28T07:10:59+00:00'
sampled_rows: 0
---

# `processed.ft_student_tests`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `userid` | `string` |  |
| `num_test_submissions` | `bigint` |  |
| `submitted_tests` | `bigint` |  |
| `submitted_tests_classes` | `bigint` |  |
| `submitted_tests_teachers` | `bigint` |  |
| `submitted_tests_low` | `bigint` |  |
| `submitted_tests_med` | `bigint` |  |
| `submitted_tests_high` | `bigint` |  |
| `submitted_tests_14` | `bigint` |  |
| `submitted_tests_29` | `bigint` |  |

## DDL

```sql
CREATE VIEW processed.ft_student_tests AS
SELECT
  CAST(sub AS varchar) userid
, "count"(*) num_test_submissions
, "count"(DISTINCT testid) submitted_tests
, "count"(DISTINCT classid) submitted_tests_classes
, "count"(DISTINCT userid) submitted_tests_teachers
, "sum"((CASE WHEN ((num_submissions > 1) AND (num_submissions < 5)) THEN 1 ELSE 0 END)) submitted_tests_low
, "sum"((CASE WHEN (num_submissions BETWEEN 5 AND 9) THEN 1 ELSE 0 END)) submitted_tests_med
, "sum"((CASE WHEN (num_submissions > 9) THEN 1 ELSE 0 END)) submitted_tests_high
, "sum"((CASE WHEN ("date"(createdat) > (current_date - INTERVAL  '15' DAY)) THEN 1 ELSE 0 END)) submitted_tests_14
, "sum"((CASE WHEN ("date"(createdat) > (current_date - INTERVAL  '29' DAY)) THEN 1 ELSE 0 END)) submitted_tests_29
FROM
  (tests
CROSS JOIN UNNEST(submissions) t (sub))
WHERE (num_submissions > 0)
GROUP BY 1
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
