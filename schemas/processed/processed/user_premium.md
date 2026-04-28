---
database: processed
table: user_premium
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/production/control_map/user_premium
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:12:59+00:00'
sampled_rows: 200
---

# `processed.user_premium`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `userid` | `string` |  |
| `premium_end_date` | `date` |  |
| `valid_premium` | `boolean` |  |

## DDL

```sql
CREATE EXTERNAL TABLE `processed.user_premium`(
  `userid` string, 
  `premium_end_date` date, 
  `valid_premium` boolean)
ROW FORMAT DELIMITED 
  FIELDS TERMINATED BY ',' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.mapred.TextInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/production/control_map/user_premium'
TBLPROPERTIES (
  'has_encrypted_data'='false', 
  'transient_lastDdlTime'='1656056726')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
