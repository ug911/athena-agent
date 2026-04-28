---
database: processed
table: ft_student_assignments
type: view
layer: processed
location: null
format: null
partition_keys: []
last_synced: '2026-04-28T07:10:55+00:00'
sampled_rows: 0
---

# `processed.ft_student_assignments`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `userid` | `string` |  |
| `num_assignment_submissions` | `bigint` |  |
| `submitted_assignments` | `bigint` |  |
| `submitted_assignments_classes` | `bigint` |  |
| `submitted_assignments_teachers` | `bigint` |  |
| `submitted_assignments_low` | `bigint` |  |
| `submitted_assignments_med` | `bigint` |  |
| `submitted_assignments_high` | `bigint` |  |
| `submitted_assignments_14` | `bigint` |  |
| `submitted_assignments_29` | `bigint` |  |

## DDL

```sql
CREATE VIEW processed.ft_student_assignments AS
SELECT
  CAST(sub AS varchar) userid
, "count"(*) num_assignment_submissions
, "count"(DISTINCT assignment_id) submitted_assignments
, "count"(DISTINCT classid) submitted_assignments_classes
, "count"(DISTINCT userid) submitted_assignments_teachers
, "sum"((CASE WHEN ((num_submissions > 1) AND (num_submissions < 5)) THEN 1 ELSE 0 END)) submitted_assignments_low
, "sum"((CASE WHEN (num_submissions BETWEEN 5 AND 9) THEN 1 ELSE 0 END)) submitted_assignments_med
, "sum"((CASE WHEN (num_submissions > 9) THEN 1 ELSE 0 END)) submitted_assignments_high
, "sum"((CASE WHEN ("date"(createdat) > (current_date - INTERVAL  '15' DAY)) THEN 1 ELSE 0 END)) submitted_assignments_14
, "sum"((CASE WHEN ("date"(createdat) > (current_date - INTERVAL  '29' DAY)) THEN 1 ELSE 0 END)) submitted_assignments_29
FROM
  (assignments
CROSS JOIN UNNEST(submissions) t (sub))
WHERE (num_submissions > 0)
GROUP BY 1
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
