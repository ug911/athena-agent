---
canonical: processed
table: upsc_live_classrooms
type: view
layer: processed
regions:
  in: processed
location: null
format: null
partition_keys: []
schema_parity: identical
last_synced: '2026-08-11T13:18:58+00:00'
sampled_rows: 0
sampled_region: null
---

# `processed.upsc_live_classrooms`

## Region availability

| Region | Athena database |
| --- | --- |
| `IN` | `processed` |

_Only present in **IN**._

## Columns (IN)

| Column | Type | Notes |
| --- | --- | --- |
| `userid` | `string` |  |
| `teacher_name` | `string` |  |
| `phonenumber` | `string` |  |
| `class_id` | `string` |  |
| `just_classnumber` | `string` |  |
| `class_type` | `varchar(7)` |  |
| `days_since_class_creation` | `bigint` |  |
| `class_name` | `string` |  |
| `subject` | `string` |  |
| `students` | `bigint` |  |

## DDL


```sql
CREATE VIEW processed.upsc_live_classrooms AS
SELECT
  b.userid
, b.name teacher_name
, phonenumber
, class_id
, just_classnumber
, (CASE WHEN (settings_openclassroom = 'true') THEN 'public' ELSE 'private' END) class_type
, "date_diff"('day', "date"(a.createdat), current_date) days_since_class_creation
, a.name class_name
, subject
, num_joinedrequest students
FROM
  ((
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
   , settings_openclassroom
   FROM
     processed.class
   WHERE ((namespace = 'wise_upsc') AND (archived = 'false'))
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
ORDER BY 2 ASC
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
