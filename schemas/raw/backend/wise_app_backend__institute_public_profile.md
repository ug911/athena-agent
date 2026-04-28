---
database: backend
table: wise_app_backend__institute_public_profile
type: table
layer: raw
location: s3://[REDACTED-BUCKET]/production/wise-app-backend/institute_public_profile
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:07:09+00:00'
sampled_rows: 0
---

# `backend.wise_app_backend__institute_public_profile`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` | from deserializer |
| `instituteid` | `string` | from deserializer |
| `__v` | `string` | from deserializer |
| `createdat` | `string` | from deserializer |
| `institutecovers` | `string` | from deserializer |
| `ispublic` | `string` | from deserializer |
| `namespace` | `string` | from deserializer |
| `publishedat` | `string` | from deserializer |
| `sections` | `string` | from deserializer |
| `socialprofile` | `string` | from deserializer |
| `subdomain` | `string` | from deserializer |
| `title` | `string` | from deserializer |
| `updatedat` | `string` | from deserializer |
| `description` | `string` | from deserializer |
| `backgroundcolor` | `string` | from deserializer |
| `ctatext` | `string` | from deserializer |
| `textcolor` | `string` | from deserializer |
| `subdomaincreated` | `string` | from deserializer |

## DDL

```sql
CREATE EXTERNAL TABLE `backend.wise_app_backend__institute_public_profile`(
  `_id` string COMMENT 'from deserializer', 
  `instituteid` string COMMENT 'from deserializer', 
  `__v` string COMMENT 'from deserializer', 
  `createdat` string COMMENT 'from deserializer', 
  `institutecovers` string COMMENT 'from deserializer', 
  `ispublic` string COMMENT 'from deserializer', 
  `namespace` string COMMENT 'from deserializer', 
  `publishedat` string COMMENT 'from deserializer', 
  `sections` string COMMENT 'from deserializer', 
  `socialprofile` string COMMENT 'from deserializer', 
  `subdomain` string COMMENT 'from deserializer', 
  `title` string COMMENT 'from deserializer', 
  `updatedat` string COMMENT 'from deserializer', 
  `description` string COMMENT 'from deserializer', 
  `backgroundcolor` string COMMENT 'from deserializer', 
  `ctatext` string COMMENT 'from deserializer', 
  `textcolor` string COMMENT 'from deserializer', 
  `subdomaincreated` string COMMENT 'from deserializer')
ROW FORMAT SERDE 
  'org.openx.data.jsonserde.JsonSerDe' 
WITH SERDEPROPERTIES ( 
  'ignore.malformed.json'='true') 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.mapred.TextInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/production/wise-app-backend/institute_public_profile'
TBLPROPERTIES (
  'compressionType'='gzip', 
  'transient_lastDdlTime'='1709549774')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
