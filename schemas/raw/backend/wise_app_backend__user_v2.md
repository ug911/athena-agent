---
database: backend
table: wise_app_backend__user_v2
type: table
layer: raw
location: s3://[REDACTED-BUCKET]/production/wise-app-backend/user
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:09:28+00:00'
sampled_rows: 0
---

# `backend.wise_app_backend__user_v2`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` | from deserializer |
| `namespace` | `string` | from deserializer |
| `isadmin` | `string` | from deserializer |
| `activesessions` | `string` | from deserializer |
| `block` | `string` | from deserializer |
| `profilepicture` | `string` | from deserializer |
| `pendingrequest` | `string` | from deserializer |
| `joinedrequest` | `string` | from deserializer |
| `adminpendingrequest` | `string` | from deserializer |
| `adminrequest` | `string` | from deserializer |
| `publicprofile` | `string` | from deserializer |
| `premiumconfig` | `string` | from deserializer |
| `name` | `string` | from deserializer |
| `profile` | `string` | from deserializer |
| `phonenumber` | `string` | from deserializer |
| `config` | `string` | from deserializer |
| `createdat` | `string` | from deserializer |
| `notificationtokens` | `string` | from deserializer |
| `__v` | `string` | from deserializer |
| `lastloggedinon` | `string` | from deserializer |
| `acquiredby` | `string` | from deserializer |
| `referralcode` | `string` | from deserializer |
| `referrallink` | `string` | from deserializer |
| `zoomaccountid` | `string` | from deserializer |
| `zoomprefix` | `string` | from deserializer |
| `zoomuserid` | `string` | from deserializer |
| `lastmeetingstartedon` | `string` | from deserializer |
| `uuid` | `string` | from deserializer |
| `updatedat` | `string` | from deserializer |
| `identities` | `string` | from deserializer |
| `email` | `string` | from deserializer |
| `referrer` | `string` | from deserializer |
| `loginpin` | `string` | from deserializer |
| `sessions` | `string` | from deserializer |
| `settings` | `string` | from deserializer |
| `parentid` | `string` | from deserializer |

## DDL

```sql
CREATE EXTERNAL TABLE `backend.wise_app_backend__user_v2`(
  `_id` string COMMENT 'from deserializer', 
  `namespace` string COMMENT 'from deserializer', 
  `isadmin` string COMMENT 'from deserializer', 
  `activesessions` string COMMENT 'from deserializer', 
  `block` string COMMENT 'from deserializer', 
  `profilepicture` string COMMENT 'from deserializer', 
  `pendingrequest` string COMMENT 'from deserializer', 
  `joinedrequest` string COMMENT 'from deserializer', 
  `adminpendingrequest` string COMMENT 'from deserializer', 
  `adminrequest` string COMMENT 'from deserializer', 
  `publicprofile` string COMMENT 'from deserializer', 
  `premiumconfig` string COMMENT 'from deserializer', 
  `name` string COMMENT 'from deserializer', 
  `profile` string COMMENT 'from deserializer', 
  `phonenumber` string COMMENT 'from deserializer', 
  `config` string COMMENT 'from deserializer', 
  `createdat` string COMMENT 'from deserializer', 
  `notificationtokens` string COMMENT 'from deserializer', 
  `__v` string COMMENT 'from deserializer', 
  `lastloggedinon` string COMMENT 'from deserializer', 
  `acquiredby` string COMMENT 'from deserializer', 
  `referralcode` string COMMENT 'from deserializer', 
  `referrallink` string COMMENT 'from deserializer', 
  `zoomaccountid` string COMMENT 'from deserializer', 
  `zoomprefix` string COMMENT 'from deserializer', 
  `zoomuserid` string COMMENT 'from deserializer', 
  `lastmeetingstartedon` string COMMENT 'from deserializer', 
  `uuid` string COMMENT 'from deserializer', 
  `updatedat` string COMMENT 'from deserializer', 
  `identities` string COMMENT 'from deserializer', 
  `email` string COMMENT 'from deserializer', 
  `referrer` string COMMENT 'from deserializer', 
  `loginpin` string COMMENT 'from deserializer', 
  `sessions` string COMMENT 'from deserializer', 
  `settings` string COMMENT 'from deserializer', 
  `parentid` string COMMENT 'from deserializer')
ROW FORMAT SERDE 
  'org.openx.data.jsonserde.JsonSerDe' 
WITH SERDEPROPERTIES ( 
  'ignore.malformed.json'='true') 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.mapred.TextInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/production/wise-app-backend/user'
TBLPROPERTIES (
  'compressionType'='gzip', 
  'transient_lastDdlTime'='1764860741')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
