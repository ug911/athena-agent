---
database: processed
table: ft_student_class
type: view
layer: processed
location: null
format: null
partition_keys: []
last_synced: '2026-04-28T07:10:57+00:00'
sampled_rows: 0
---

# `processed.ft_student_class`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `userid` | `string` |  |
| `highest_strength` | `bigint` |  |
| `attending_classes` | `bigint` |  |
| `attending_low_classes` | `bigint` |  |
| `attending_med_classes` | `bigint` |  |
| `attending_pow_classes` | `bigint` |  |

## DDL

```sql
CREATE VIEW processed.ft_student_class AS
SELECT
  userid
, "max"(students) highest_strength
, "count"(DISTINCT class_id) attending_classes
, "sum"((CASE WHEN ((students > 1) AND (students < 5)) THEN 1 ELSE 0 END)) attending_low_classes
, "sum"((CASE WHEN ((students > 4) AND (students < 10)) THEN 1 ELSE 0 END)) attending_med_classes
, "sum"((CASE WHEN (students > 9) THEN 1 ELSE 0 END)) attending_pow_classes
FROM
  (
   SELECT
     CAST(student AS varchar) userid
   , x.class_id
   , students
   FROM
     ((
      SELECT
        userid
      , class_id
      , student
      FROM
        (class
      CROSS JOIN UNNEST(joinedrequests) t (student))
      WHERE (archived = 'false')
   )  x
   INNER JOIN (
      SELECT
        class_id
      , num_joinedrequest students
      FROM
        class
   )  y ON (x.class_id = y.class_id))
   WHERE (userid <> student)
)  foo
GROUP BY 1
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
