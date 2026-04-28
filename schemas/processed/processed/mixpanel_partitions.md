---
database: processed
table: mixpanel_partitions
type: view
layer: processed
location: null
format: null
partition_keys: []
last_synced: '2026-04-28T07:11:51+00:00'
sampled_rows: 0
---

# `processed.mixpanel_partitions`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `year` | `int` |  |
| `month` | `int` |  |
| `day` | `int` |  |
| `events` | `bigint` |  |

## DDL

```sql
CREATE VIEW processed.mixpanel_partitions AS
SELECT
  year
, month
, day
, "count"(*) events
FROM
  mixpanel__events
GROUP BY 1, 2, 3
ORDER BY 1 DESC, 2 DESC, 3 DESC
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
