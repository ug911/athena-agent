---
database: processed
table: wise_app_backend__zoom
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/zoom/
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:18:07+00:00'
sampled_rows: 200
---

# `processed.wise_app_backend__zoom`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` |  |
| `attendancerecorded` | `string` |  |
| `mettingended` | `string` |  |
| `webhookreceived` | `string` |  |
| `licensed` | `string` |  |
| `disablecommenting` | `string` |  |
| `mettingid` | `string` |  |
| `start_url` | `string` |  |
| `join_url` | `string` |  |
| `classid` | `string` |  |
| `userid` | `string` |  |
| `meetinguuid` | `string` |  |
| `start_time` | `string` |  |
| `participants` | `string` |  |
| `comments` | `string` |  |
| `createdat` | `string` |  |
| `updatedat` | `string` |  |
| `__v` | `string` |  |
| `timezone` | `string` |  |
| `duration` | `string` |  |
| `end_time` | `string` |  |
| `scheduledstarttime` | `string` |  |
| `scheduledendtime` | `string` |  |
| `participant` | `string` |  |
| `maxparticipantduration` | `string` |  |
| `metadata` | `string` |  |
| `meetingstarted` | `string` |  |
| `archived` | `string` |  |
| `type` | `string` |  |
| `meetingstatus` | `string` |  |
| `title` | `string` |  |
| `password` | `string` |  |
| `recordings` | `string` |  |
| `rawrecordings` | `string` |  |
| `recordingshared` | `string` |  |
| `location` | `string` |  |

## Enum-like columns

_String columns with ≤20 distinct values in 200 sampled rows. Distribution shown as `value (×count)`._

- `attendancerecorded`: `true (×161)`, `false (×39)`
- `mettingended`: `true (×149)`, `false (×51)`
- `licensed`: `true (×148)`, `false (×52)`
- `disablecommenting`: `false (×200)`
- `start_url`: `- (×144)`
- `join_url`: `- (×144)`
- `meetingstarted`: `true (×148)`, `false (×52)`
- `archived`: `false (×197)`, `true (×3)`
- `type`: `SCHEDULED (×142)`, `AD_HOC (×58)`
- `meetingstatus`: `ENDED (×149)`, `UPCOMING (×35)`, `MISSED (×12)`, `CANCELLED (×4)`
- `recordingshared`: `true (×76)`, `false (×18)`

## Inferred JSON structure

_Inferred from 200 sampled rows on 2026-04-28. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `67a1d83840756c5f51da39e6`, `695e69874a1d77ab2c9202ca`, `695e6a99a5097e0527ab72a6`

### `classid`

- `$oid` — `string`  e.g. `67a1d06d2628b531bebc40a1`, `693a4baa30d50e7789ca2f41`, `695e56edfe4a1366ea6e1da0`

### `userid`

- `$oid` — `string`  e.g. `66cdc5f537bd18687b678691`, `695e179928118f629e483933`, `6874de2e7c49d0a2e779dbdc`

### `start_time`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1739845800000`, `1783492200000`, `1767795353474`

### `participants`

  - `[]` — `object`
    - `absolutepercentattendance` — `object`
      - `$numberint` — `string`  e.g. `99`, `97`, `68`
    - `customerkey` — `string`  e.g. `NA|Z_67a2d0c910b0279ce6935bfc`, `NA|Z_67a2d0c910b0279ce6935bfc`, `NA|Z_66ce7823ac2b1909cc0ed8b0`
    - `duration` — `object`
      - `$numberint` — `string`  e.g. `2926`, `2905`, `1667`
    - `firstentrytime` — `object`
      - `$date` — `object`
        - `$numberlong` — `string`  e.g. `1767795367000`, `1767795387000`, `1767886188000`
    - `inmeetingduration` — `object`
      - `$numberint` — `string`  e.g. `2926`, `2888`, `1667`
    - `isteacher` — `bool`  e.g. `true`, `false`, `true`
    - `lastexittime` — `object`
      - `$date` — `object`
        - `$numberlong` — `string`  e.g. `1767798293000`, `1767798292000`, `1767887855000`
    - `name` — `string`  e.g. `[REDACTED]`
    - `relativepercentattendance` — `object`
      - `$numberint` — `string`  e.g. `100`, `98`, `69`
    - `user_email` — `string`  e.g. `[REDACTED]`
    - `user_id` — `string`  e.g. `16795648`, `16797696`, `16798720`
    - `wiseuserid` — `object`
      - `$oid` — `string`  e.g. `6874de2e7c49d0a2e779dbdc`, `66c0a7e9c446c9dc064dd3f1`, `6940fa30e6d9baa1da2ae883`

### `comments`



### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1738659896759`, `1767795079052`, `1767795353475`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1739853552334`, `1767795079052`, `1767798607913`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

### `duration`

- `$numberint` — `string`  e.g. `2926000`, `1667000`, `9398000`

### `end_time`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1767798293000`, `1767887855000`, `1767805324000`

### `scheduledstarttime`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1739845800000`, `1783492200000`, `1767886200000`

### `scheduledendtime`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1739851200000`, `1783495800000`, `1767889800000`

### `participant`

- `$numberint` — `string`  e.g. `1`, `0`, `11`

### `maxparticipantduration`

- `$numberint` — `string`  e.g. `2905`, `0`, `9324`

### `metadata`

- `autorecord` — `bool`  e.g. `true`, `true`, `true`
- `cancellationmetadata` — `object`
  - `approved` — `bool`  e.g. `false`
  - `requestedby` — `string`  e.g. `694708b128118f629eeef690`
  - `requestedon` — `object`
    - `$date` — `object`
      - `$numberlong` — `string`  e.g. `1770421555637`
  - `requestnote` — `string`  e.g. `Sorry I am going on holiday this mid-term so I can’t have my`
- `endedby` — `string`  e.g. `6763b746b9579e4c94f4fe1c`, `68a82e3adc426fe2bd3335c8`, `6736eeb39dcd88eb74e5386a`
- `endreason` — `string`  e.g. `end_meeting`, `start_new`, `end_meeting`
- `isownerzoom` — `bool`  e.g. `false`, `false`, `false`
- `lensenabled` — `bool`  e.g. `false`, `false`, `false`
- `ownerid` — `object`
  - `$oid` — `string`  e.g. `64f9654d3bb4912ed85547d1`, `662a38bb7952f676b4f5493e`, `65c99aa5f556af274e65837e`
- `paiduser` — `bool`  e.g. `true`, `true`, `true`
- `poolname` — `string`  e.g. `DEFAULT`, `DEFAULT`, `DEFAULT`
- `recurrenceid` — `string`  e.g. `67a1d83840756c5f51da39d9`, `695e69874a1d77ab2c9202ad`, `695e6b3437f7882b9bb92e3a`
- `registrationenabled` — `bool`  e.g. `true`, `true`, `true`
- `restartedsessions` — `array<object>|array<unknown>`
  - `restartedsessions[]` — `object`
    - `meetinguuid` — `string`  e.g. `DI1iZzPBQLyLyRmFNiLR7A==`
    - `sessionid` — `object`
      - `$oid` — `string`  e.g. `6916f87e565cee7720051a1c`
- `tags` — `` (nullable)
- `waitingmeeting` — `bool`  e.g. `true`
- `webinar` — `bool`  e.g. `false`, `false`, `false`
- `zoomadminaccountid` — `string`  e.g. `63f8b2037eb779515cf43d21`, `63f8b2037eb779515cf43d21`, `63f8b2037eb779515cf43d21`
- `zoomuseraccountid` — `string`  e.g. `66fa93bcc493790018d7b429`, `681db5c6d7bfefa6dad4d01a`, `66fa77d1763295008ca2dda1`
- `zoomuserid` — `string`  e.g. `zWOg8ExdSc-J8iide_YVuQ`, `ktrOYCJOQJ-dHF0KZ0gSRQ`, `XeW1TnxIRyOMjhg2K-kcdw`

### `recordings`

  - `[]` — `object`
    - `_id` — `object`
      - `$oid` — `string`  e.g. `695e9b0340ae8ceb5adfc546`, `695ea7284e6b5229fe752171`, `695e8fb6e43a15e488a3ab01`
    - `duration` — `object`
      - `$numberint` — `string`  e.g. `9395`, `3981`, `1792`
    - `file` — `object`
      - `_id` — `object`
        - `$oid` — `string`  e.g. `692476df9ccea6b19ade8dc1`, `69170c3bfee67c6d82d6e5f1`, `6917134b4073436bcf0e9ddf`
      - `filename` — `string`  e.g. `video.m3u8`, `video.m3u8`, `video.m3u8`
      - `path` — `string`  e.g. `https://streaming.wiseapp.live/video-player/wise-video-playe`, `https://streaming.wiseapp.live/video-player/wise-video-playe`, `https://streaming.wiseapp.live/video-player/wise-video-playe`
      - `s3filepath` — `string`  e.g. `https://wise-app-s3-bucket.s3-ap-south-1.amazonaws.com/strea`, `https://wise-app-s3-bucket.s3-ap-south-1.amazonaws.com/strea`, `https://wise-app-s3-bucket.s3-ap-south-1.amazonaws.com/strea`
      - `s3key` — `string`  e.g. `streaming_videos/66fbb998e82bde040df69db5/695e6cc7e4335a33aa`, `streaming_videos/687e42910933d0d619f41d47/695e74a34a1d77ab2c`, `streaming_videos/67bc781cf6b7db0bcc3b51cb/695e82e356b0de8685`
      - `size` — `object`
        - `$numberint` — `string`  e.g. `183288189`, `112798249`, `62792552`
      - `subtype` — `string`  e.g. `hls_video`, `hls_video`, `hls_video`
      - `type` — `string`  e.g. `video`, `video`, `video`
    - `partindex` — `object`
      - `$numberint` — `string`  e.g. `1`, `1`, `1`
    - `sessionindex` — `object`
      - `$numberint` — `string`  e.g. `1`, `1`, `1`
    - `type` — `string`  e.g. `RECORDING`, `RECORDING`, `YOUTUBE`
    - `url` — `string`  e.g. `https://streaming.wiseapp.live/video-player/wise-video-playe`, `https://streaming.wiseapp.live/video-player/wise-video-playe`, `https://www.youtube.com/watch?v=mG7WL8V_2EI`

### `rawrecordings`



## DDL

```sql
CREATE EXTERNAL TABLE `processed.wise_app_backend__zoom`(
  `_id` string, 
  `attendancerecorded` string, 
  `mettingended` string, 
  `webhookreceived` string, 
  `licensed` string, 
  `disablecommenting` string, 
  `mettingid` string, 
  `start_url` string, 
  `join_url` string, 
  `classid` string, 
  `userid` string, 
  `meetinguuid` string, 
  `start_time` string, 
  `participants` string, 
  `comments` string, 
  `createdat` string, 
  `updatedat` string, 
  `__v` string, 
  `timezone` string, 
  `duration` string, 
  `end_time` string, 
  `scheduledstarttime` string, 
  `scheduledendtime` string, 
  `participant` string, 
  `maxparticipantduration` string, 
  `metadata` string, 
  `meetingstarted` string, 
  `archived` string, 
  `type` string, 
  `meetingstatus` string, 
  `title` string, 
  `password` string, 
  `recordings` string, 
  `rawrecordings` string, 
  `recordingshared` string, 
  `location` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/wise-app-backend/zoom/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260428_015156_00169_vgjsv', 
  'trino_version'='0.215-24582-g0575ac4')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->

## Notes

- **Canonical "session" table.** One row = one Zoom meeting on Wise's platform. `_id` is the session id, `classid` links to `processed.class`, `userid` is the **host teacher**, `metadata.ownerid` is the class owner (may differ from host for co-taught classes).
- **License accounting.** One running session = one Zoom license held from `start_time` to `end_time`. Use sweep-line on `(start_time, +1) / (end_time, -1)` for concurrency. `metadata.zoomadminaccountid` distinguishes Wise-pool licenses from BYO customer accounts — filter on it when measuring **Wise's** license usage. `OFFLINE`, `CANCELLED`, and `MISSED` sessions do **not** consume a license; exclude from license math.
- **Times are Mongo-encoded epoch-millis** under `$.{$date}.{$numberlong}` — confirmed **UTC**. Same encoding for `start_time`, `end_time`, `scheduledstarttime`, `scheduledendtime`, `createdat`, `updatedat`, and per-participant `firstentrytime` / `lastexittime`.
- **`end_time IS NULL` means the session never started** (missed). It does **not** mean "currently live". `meetingstatus = 'ENDED'` is set when the session actually ends, and `end_time` is that timestamp — the two should agree.
- **`participants` JSON array.** Each element = one attendee. `firstentrytime` / `lastexittime` give a single window per participant per session — rejoin gaps are not tracked, treat the window as authoritative. `isteacher: true` reliably flags hosts/co-teachers; use it to split student concurrency from total participant concurrency. Unnesting is ~3 GB for 28 days — materialize if reusing.
- **`meetingstatus` values seen**: `ENDED`, `UPCOMING`, `CANCELLED`, `MISSED`. For past/completed sessions filter on `meetingstatus = 'ENDED'`.
- **`type` values**: `SCHEDULED`, `AD_HOC`, `OFFLINE`. Exclude `OFFLINE` from license/concurrency calculations.
- **Ingestion**: full Mongo collection dump once per day → near-real-time questions are not possible; same-day data may be missing or partial. Scope time windows accordingly (e.g. trailing 28d is reliable; "last hour" is not).
- **No `namespace` column on this table.** Join to `processed.class` on `classid` to get the tenant namespace — namespace is the canonical tenant identifier for billing/license accounting.
