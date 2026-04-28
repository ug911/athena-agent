---
database: backend
table: rudder_lens
type: table
layer: raw
location: s3://[REDACTED-BUCKET]/production/primary/rudder-logs/2JquM2gXCDOlHiy1G4RzKFZby2A
format: INPUTFORMAT
partition_keys:
- dt
last_synced: '2026-04-28T07:04:43+00:00'
sampled_rows: 0
---

# `backend.rudder_lens`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `type` | `string` | from deserializer |
| `event` | `string` | from deserializer |
| `sentat` | `string` | from deserializer |
| `channel` | `string` | from deserializer |
| `context` | `map<string,string>` | from deserializer |
| `rudderid` | `string` | from deserializer |
| `messageid` | `string` | from deserializer |
| `timestamp` | `string` | from deserializer |
| `properties` | `map<string,string>` | from deserializer |
| `receivedat` | `string` | from deserializer |
| `request_ip` | `string` | from deserializer |
| `anonymousid` | `string` | from deserializer |
| `integrations` | `map<string,string>` | from deserializer |
| `originaltimestamp` | `string` | from deserializer |
| `dt` | `string` |  |

**Partition keys:** `dt`

## DDL

```sql
CREATE EXTERNAL TABLE `backend.rudder_lens`(
  `type` string COMMENT 'from deserializer', 
  `event` string COMMENT 'from deserializer', 
  `sentat` string COMMENT 'from deserializer', 
  `channel` string COMMENT 'from deserializer', 
  `context` map<string,string> COMMENT 'from deserializer', 
  `rudderid` string COMMENT 'from deserializer', 
  `messageid` string COMMENT 'from deserializer', 
  `timestamp` string COMMENT 'from deserializer', 
  `properties` map<string,string> COMMENT 'from deserializer', 
  `receivedat` string COMMENT 'from deserializer', 
  `request_ip` string COMMENT 'from deserializer', 
  `anonymousid` string COMMENT 'from deserializer', 
  `integrations` map<string,string> COMMENT 'from deserializer', 
  `originaltimestamp` string COMMENT 'from deserializer')
PARTITIONED BY ( 
  `dt` string)
ROW FORMAT SERDE 
  'org.openx.data.jsonserde.JsonSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.mapred.TextInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.IgnoreKeyTextOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/production/primary/rudder-logs/2JquM2gXCDOlHiy1G4RzKFZby2A'
TBLPROPERTIES (
  'has_encrypted_data'='false', 
  'transient_lastDdlTime'='1674631687')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
