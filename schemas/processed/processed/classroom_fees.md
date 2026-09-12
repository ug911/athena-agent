---
canonical: processed
table: classroom_fees
type: view
layer: processed
regions:
  in: processed
location: null
format: null
partition_keys: []
schema_parity: identical
last_synced: '2026-08-11T13:14:43+00:00'
sampled_rows: 0
sampled_region: null
---

# `processed.classroom_fees`

## Region availability

| Region | Athena database |
| --- | --- |
| `IN` | `processed` |

_Only present in **IN**._

## Columns (IN)

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` |  |
| `classid` | `string` |  |
| `createdat` | `timestamp` |  |
| `updatedat` | `timestamp` |  |
| `paymentoptions` | `string` |  |
| `num_paymentoptions` | `bigint` |  |
| `metadata` | `string` |  |

## DDL


```sql
CREATE VIEW processed.classroom_fees AS
SELECT
  CAST(JSON_EXTRACT(_id, '$["$oid"]') AS VARCHAR) _id
, CAST(JSON_EXTRACT(classid, '$["$oid"]') AS VARCHAR) classid
, FROM_UNIXTIME(CAST(SUBSTR(CAST(JSON_EXTRACT(createdat, '$["$date"]["$numberlong"]') AS VARCHAR), 1, 10) AS DOUBLE)) createdat
, FROM_UNIXTIME(CAST(SUBSTR(CAST(JSON_EXTRACT(updatedat, '$["$date"]["$numberlong"]') AS VARCHAR), 1, 10) AS DOUBLE)) updatedat
, paymentoptions
, CARDINALITY(CAST(JSON_PARSE(paymentoptions) AS ARRAY(JSON))) num_paymentoptions
, metadata
FROM
  wise_app_backend__classroom_fees
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
