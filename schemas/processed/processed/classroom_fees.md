---
database: processed
table: classroom_fees
type: view
layer: processed
location: null
format: null
partition_keys: []
last_synced: '2026-04-28T07:10:23+00:00'
sampled_rows: 0
---

# `processed.classroom_fees`

## Columns

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
