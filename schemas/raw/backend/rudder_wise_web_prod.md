---
database: backend
table: rudder_wise_web_prod
type: table
layer: raw
location: s3://[REDACTED-BUCKET]/production/primary/rudder-logs/1yXs3gEWXXMzNVPGEZ4GaaYSH7B
format: INPUTFORMAT
partition_keys:
- dt
last_synced: '2026-04-28T07:04:49+00:00'
sampled_rows: 0
---

# `backend.rudder_wise_web_prod`

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
CREATE EXTERNAL TABLE `backend.rudder_wise_web_prod`(
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
  's3://[REDACTED-BUCKET]/production/primary/rudder-logs/1yXs3gEWXXMzNVPGEZ4GaaYSH7B'
TBLPROPERTIES (
  'case.insensitive'='false', 
  'has_encrypted_data'='false', 
  'last_modified_by'='hadoop', 
  'last_modified_time'='1690796634', 
  'transient_lastDdlTime'='1697021515')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
