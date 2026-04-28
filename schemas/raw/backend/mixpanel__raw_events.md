---
database: backend
table: mixpanel__raw_events
type: table
layer: raw
location: s3://[REDACTED-BUCKET]/mixpanel/raw_extract
format: INPUTFORMAT
partition_keys:
- year
- month
- day
last_synced: '2026-04-28T07:04:29+00:00'
sampled_rows: 0
---

# `backend.mixpanel__raw_events`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `event` | `string` | from deserializer |
| `properties` | `string` | from deserializer |
| `year` | `int` |  |
| `month` | `int` |  |
| `day` | `int` |  |

**Partition keys:** `year`, `month`, `day`

## DDL

```sql
CREATE EXTERNAL TABLE `backend.mixpanel__raw_events`(
  `event` string COMMENT 'from deserializer', 
  `properties` string COMMENT 'from deserializer')
PARTITIONED BY ( 
  `year` int, 
  `month` int, 
  `day` int)
ROW FORMAT SERDE 
  'org.openx.data.jsonserde.JsonSerDe' 
WITH SERDEPROPERTIES ( 
  'ignore.malformed.json'='true') 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.mapred.TextInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.IgnoreKeyTextOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/mixpanel/raw_extract'
TBLPROPERTIES (
  'has_encrypted_data'='false', 
  'transient_lastDdlTime'='1629354306')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
