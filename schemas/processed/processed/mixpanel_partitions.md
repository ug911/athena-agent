---
canonical: processed
table: mixpanel_partitions
type: view
layer: processed
regions:
  in: processed
location: null
format: null
partition_keys: []
schema_parity: identical
last_synced: '2026-08-11T13:17:34+00:00'
sampled_rows: 0
sampled_region: null
---

# `processed.mixpanel_partitions`

## Region availability

| Region | Athena database |
| --- | --- |
| `IN` | `processed` |

_Only present in **IN**._

## Columns (IN)

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
