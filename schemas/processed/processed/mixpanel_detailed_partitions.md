---
database: processed
table: mixpanel_detailed_partitions
type: view
layer: processed
location: null
format: null
partition_keys: []
last_synced: '2026-04-28T07:11:44+00:00'
sampled_rows: 0
---

# `processed.mixpanel_detailed_partitions`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `year` | `int` |  |
| `month` | `int` |  |
| `day` | `int` |  |
| `events` | `bigint` |  |
| `distinct_id` | `bigint` |  |
| `device_id` | `bigint` |  |
| `distinct_id_before_identity` | `bigint` |  |
| `user_id` | `bigint` |  |

## DDL

```sql
CREATE VIEW processed.mixpanel_detailed_partitions AS
SELECT
  year
, month
, day
, "count"(*) events
, "count"(DISTINCT distinct_id) distinct_id
, "count"(DISTINCT device_id) device_id
, "count"(DISTINCT distinct_id_before_identity) distinct_id_before_identity
, "count"(DISTINCT user_id) user_id
FROM
  mixpanel__events
GROUP BY 1, 2, 3
ORDER BY 1 DESC, 2 DESC, 3 DESC
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
