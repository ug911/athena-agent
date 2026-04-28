---
database: backend
table: wise_app_backend__whitelabel
type: table
layer: raw
location: s3://[REDACTED-BUCKET]/production/wise-app-backend/Whitelabel
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:09:49+00:00'
sampled_rows: 0
---

# `backend.wise_app_backend__whitelabel`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` | from deserializer |
| `featureconfig` | `string` | from deserializer |
| `hostnames` | `string` | from deserializer |
| `adminuserids` | `string` | from deserializer |
| `displayconfig` | `string` | from deserializer |
| `namespace` | `string` | from deserializer |
| `apphash` | `string` | from deserializer |
| `__v` | `string` | from deserializer |
| `createdat` | `string` | from deserializer |
| `updatedat` | `string` | from deserializer |
| `versionconfig` | `string` | from deserializer |
| `systemconfig` | `string` | from deserializer |
| `disabled` | `string` | from deserializer |
| `contactmobile` | `string` | from deserializer |
| `trialclassid` | `string` | from deserializer |
| `faqurl` | `string` | from deserializer |
| `privacypolicyurl` | `string` | from deserializer |
| `customauthconfig` | `string` | from deserializer |
| `defaultinstituteid` | `string` | from deserializer |
| `maxlogins` | `string` | from deserializer |
| `additionalconfig` | `string` | from deserializer |

## DDL

```sql
CREATE EXTERNAL TABLE `backend.wise_app_backend__whitelabel`(
  `_id` string COMMENT 'from deserializer', 
  `featureconfig` string COMMENT 'from deserializer', 
  `hostnames` string COMMENT 'from deserializer', 
  `adminuserids` string COMMENT 'from deserializer', 
  `displayconfig` string COMMENT 'from deserializer', 
  `namespace` string COMMENT 'from deserializer', 
  `apphash` string COMMENT 'from deserializer', 
  `__v` string COMMENT 'from deserializer', 
  `createdat` string COMMENT 'from deserializer', 
  `updatedat` string COMMENT 'from deserializer', 
  `versionconfig` string COMMENT 'from deserializer', 
  `systemconfig` string COMMENT 'from deserializer', 
  `disabled` string COMMENT 'from deserializer', 
  `contactmobile` string COMMENT 'from deserializer', 
  `trialclassid` string COMMENT 'from deserializer', 
  `faqurl` string COMMENT 'from deserializer', 
  `privacypolicyurl` string COMMENT 'from deserializer', 
  `customauthconfig` string COMMENT 'from deserializer', 
  `defaultinstituteid` string COMMENT 'from deserializer', 
  `maxlogins` string COMMENT 'from deserializer', 
  `additionalconfig` string COMMENT 'from deserializer')
ROW FORMAT SERDE 
  'org.openx.data.jsonserde.JsonSerDe' 
WITH SERDEPROPERTIES ( 
  'ignore.malformed.json'='true') 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.mapred.TextInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/production/wise-app-backend/Whitelabel'
TBLPROPERTIES (
  'compressionType'='gzip', 
  'transient_lastDdlTime'='1709557985')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
