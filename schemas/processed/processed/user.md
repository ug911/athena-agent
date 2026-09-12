---
canonical: processed
table: user
type: view
layer: processed
regions:
  in: processed
  na: processed_na
location: null
format: null
partition_keys: []
schema_parity: identical
last_synced: '2026-08-11T13:19:10+00:00'
sampled_rows: 0
sampled_region: null
---

# `processed.user`

## Region availability

| Region | Athena database |
| --- | --- |
| `IN` | `processed` |
| `NA` | `processed_na` |

_Schema parity: **identical** across regions._

## Columns (IN)

| Column | Type | Notes |
| --- | --- | --- |
| `userid` | `string` |  |
| `name` | `string` |  |
| `phonenumber` | `string` |  |
| `email` | `string` |  |
| `profile` | `string` |  |
| `namespace` | `string` |  |
| `referralcode` | `string` |  |
| `config_namespace` | `string` |  |
| `acquiredby` | `string` |  |
| `config_lang` | `string` |  |
| `createdat` | `date` |  |
| `updatedat` | `date` |  |
| `lastloggedinon` | `date` |  |
| `lastmeetingstartedon` | `date` |  |
| `licensed` | `string` |  |
| `licenseexpireat` | `string` |  |
| `license_plantype` | `string` |  |
| `referrer` | `string` |  |
| `parentid` | `string` |  |

## DDL

_From `IN` (processed)._

```sql
CREATE VIEW processed.user AS
SELECT
  CAST("json_extract"(_id, '$["$oid"]') AS varchar) userid
, name
, phonenumber
, email
, profile
, namespace
, referralcode
, CAST("json_extract"(config, '$["namespace"]') AS varchar) config_namespace
, CAST("json_extract"(acquiredby, '$["$oid"]') AS varchar) acquiredby
, CAST("json_extract"(config, '$["languagepreference"]') AS varchar) config_lang
, "date"("from_unixtime"(TRY_CAST("substr"(TRY_CAST("json_extract"(createdat, '$["$date"]["$numberlong"]') AS varchar), 1, 10) AS double))) createdat
, "date"("from_unixtime"(TRY_CAST("substr"(TRY_CAST("json_extract"(updatedat, '$["$date"]["$numberlong"]') AS varchar), 1, 10) AS double))) updatedat
, "date"("from_unixtime"(TRY_CAST("substr"(TRY_CAST("json_extract"(lastloggedinon, '$["$date"]["$numberlong"]') AS varchar), 1, 10) AS double))) lastloggedinon
, "date"("from_unixtime"(TRY_CAST("substr"(TRY_CAST("json_extract"(lastmeetingstartedon, '$["$date"]["$numberlong"]') AS varchar), 1, 10) AS double))) lastmeetingstartedon
, CAST("json_extract"(premiumconfig, '$["licensed"]') AS varchar) licensed
, CAST("json_extract"(premiumconfig, '$["licenseexpiresat"]["$date"]["$numberlong"]') AS varchar) licenseexpireat
, CAST("json_extract"(premiumconfig, '$["plantype"]') AS varchar) license_plantype
, CAST("json_extract"(referrer, '$["$oid"]') AS varchar) referrer
, CAST("json_extract"(parentid, '$["$oid"]') AS varchar) parentid
FROM
  wise_app_backend__user
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
