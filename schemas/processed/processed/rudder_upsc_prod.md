---
database: processed
table: rudder_upsc_prod
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/processed/rudder_upsc_prod/dt=2022-01-31/
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:12:05+00:00'
sampled_rows: 0
---

# `processed.rudder_upsc_prod`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `type` | `string` |  |
| `event` | `string` |  |
| `sentat` | `string` |  |
| `channel` | `string` |  |
| `context` | `map<string,string>` |  |
| `rudderid` | `string` |  |
| `messageid` | `string` |  |
| `timestamp` | `string` |  |
| `properties` | `map<string,string>` |  |
| `receivedat` | `string` |  |
| `request_ip` | `string` |  |
| `anonymousid` | `string` |  |
| `integrations` | `map<string,string>` |  |
| `originaltimestamp` | `string` |  |
| `dt` | `string` |  |

## DDL

```sql
CREATE EXTERNAL TABLE `processed.rudder_upsc_prod`(
  `type` string COMMENT '', 
  `event` string COMMENT '', 
  `sentat` string COMMENT '', 
  `channel` string COMMENT '', 
  `context` map<string,string> COMMENT '', 
  `rudderid` string COMMENT '', 
  `messageid` string COMMENT '', 
  `timestamp` string COMMENT '', 
  `properties` map<string,string> COMMENT '', 
  `receivedat` string COMMENT '', 
  `request_ip` string COMMENT '', 
  `anonymousid` string COMMENT '', 
  `integrations` map<string,string> COMMENT '', 
  `originaltimestamp` string COMMENT '', 
  `dt` string COMMENT '')
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/rudder_upsc_prod/dt=2022-01-31/'
TBLPROPERTIES (
  'has_encrypted_data'='false', 
  'parquet.compression'='GZIP', 
  'presto_query_id'='20220207_121255_00097_ee4mj')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
