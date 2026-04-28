---
database: processed
table: wise_premium_order
type: view
layer: processed
location: null
format: null
partition_keys: []
last_synced: '2026-04-28T07:18:23+00:00'
sampled_rows: 0
---

# `processed.wise_premium_order`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `premium_order_id` | `string` |  |
| `userid` | `string` |  |
| `startsfrom` | `date` |  |
| `endsat` | `date` |  |
| `createdat` | `date` |  |
| `updatedat` | `date` |  |
| `renewson` | `date` |  |
| `amount_currency` | `string` |  |
| `amount_value` | `string` |  |
| `licensecount` | `string` |  |
| `status` | `string` |  |
| `type` | `string` |  |
| `plantype` | `string` |  |
| `__v` | `string` |  |

## DDL

```sql
CREATE VIEW processed.wise_premium_order AS
SELECT
  CAST("json_extract"("_id", '$["$oid"]') AS varchar) premium_order_id
, CAST("json_extract"("userid", '$["$oid"]') AS varchar) userid
, COALESCE("date"("substr"(TRY_CAST("json_extract"(startsfrom, '$["$date"]') AS varchar), 1, 10)), "date"("from_unixtime"(TRY_CAST("substr"(TRY_CAST("json_extract"(startsfrom, '$["$date"]["$numberlong"]') AS varchar), 1, 10) AS double)))) startsfrom
, COALESCE("date"("substr"(TRY_CAST("json_extract"(endsat, '$["$date"]') AS varchar), 1, 10)), "date"("from_unixtime"(TRY_CAST("substr"(TRY_CAST("json_extract"(endsat, '$["$date"]["$numberlong"]') AS varchar), 1, 10) AS double)))) endsat
, COALESCE("date"("substr"(TRY_CAST("json_extract"(createdat, '$["$date"]') AS varchar), 1, 10)), "date"("from_unixtime"(TRY_CAST("substr"(TRY_CAST("json_extract"(createdat, '$["$date"]["$numberlong"]') AS varchar), 1, 10) AS double)))) createdat
, COALESCE("date"("substr"(TRY_CAST("json_extract"(updatedat, '$["$date"]') AS varchar), 1, 10)), "date"("from_unixtime"(TRY_CAST("substr"(TRY_CAST("json_extract"(updatedat, '$["$date"]["$numberlong"]') AS varchar), 1, 10) AS double)))) updatedat
, COALESCE("date"("substr"(TRY_CAST("json_extract"(renewson, '$["$date"]') AS varchar), 1, 10)), "date"("from_unixtime"(TRY_CAST("substr"(TRY_CAST("json_extract"(renewson, '$["$date"]["$numberlong"]') AS varchar), 1, 10) AS double)))) renewson
, CAST("json_extract"("amount", '$["currency"]') AS varchar) amount_currency
, CAST("json_extract"("amount", '$["value"]["$numberint"]') AS varchar) amount_value
, CAST("json_extract"("licensecount", '$["$numberint"]') AS varchar) licensecount
, "status"
, "type"
, "plantype"
, CAST("json_extract"("__v", '$["$numberint"]') AS varchar) __v
FROM
  "processed"."wise_app_backend__premium_order"
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
