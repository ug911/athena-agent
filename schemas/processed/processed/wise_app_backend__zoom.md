---
canonical: processed
table: wise_app_backend__zoom
type: table
layer: processed
regions:
  in: processed
  na: processed_na
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/zoom/
format: INPUTFORMAT
partition_keys: []
schema_parity: identical
last_synced: '2026-08-11T13:30:26+00:00'
sampled_rows: 200
sampled_region: in
---

# `processed.wise_app_backend__zoom`

## Region availability

| Region | Athena database |
| --- | --- |
| `IN` | `processed` |
| `NA` | `processed_na` |

_Schema parity: **identical** across regions._

## Columns (IN)

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

_String columns with ≤20 distinct values in 200 sampled rows from `IN`. Distribution shown as `value (×count)`._

- `attendancerecorded`: `true (×147)`, `false (×53)`
- `mettingended`: `true (×139)`, `false (×61)`
- `licensed`: `true (×137)`, `false (×63)`
- `disablecommenting`: `false (×200)`
- `start_url`: `- (×66)`
- `join_url`: `- (×66)`
- `meetingstarted`: `true (×132)`, `false (×68)`
- `archived`: `false (×195)`, `true (×5)`
- `type`: `SCHEDULED (×132)`, `AD_HOC (×65)`, `OFFLINE (×3)`
- `meetingstatus`: `ENDED (×139)`, `UPCOMING (×49)`, `MISSED (×7)`, `CANCELLED (×5)`
- `recordingshared`: `true (×76)`, `false (×19)`

## Inferred JSON structure

_Inferred from 200 sampled rows from `IN` on 2026-08-11. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `660f8c26561c412a02219dd9`, `660f9164a2154a9f1854c828`, `660f934c13579480bad63137`

### `classid`

- `$oid` — `string`  e.g. `65e8755fece1d121b1d5c659`, `660f91300b999f25d5bb779a`, `660f93170b999f611dbbbd53`

### `userid`

- `$oid` — `string`  e.g. `65e17e842f91ac1adab7f63a`, `657ffeaad12ab976d21e9c65`, `65fe711f8b9cc6ebd8f6b536`

### `start_time`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1712575473361`, `1712813408882`, `1716268513658`

### `participants`

  - `[]` — `object`
    - `absolutepercentattendance` — `object`
      - `$numberint` — `string`  e.g. `87`, `31`, `97`
    - `attendancepercentage` — `object`
      - `$numberint` — `string`  e.g. `0`, `0`, `0`
    - `credits` — `object`
      - `$numberdouble` — `string`  e.g. `0.75`
      - `$numberint` — `string`  e.g. `1`, `1`, `1`
    - `customerkey` — `string`  e.g. `NA|Z_6694fa4fc94d26ab471b2630`, `NA|U_6669400f567ebeb8fb24032e`, `NA|U_667c0a1edf5e936cd3a269ef`
    - `duration` — `object`
      - `$numberint` — `string`  e.g. `2179`, `0`, `0`
    - `firstentrytime` — `object`
      - `$date` — `object`
        - `$numberlong` — `string`  e.g. `1712575756000`, `1712575489000`, `1712577219000`
    - `inmeetingduration` — `object`
      - `$numberint` — `string`  e.g. `1692`, `2025`, `3673`
    - `isteacher` — `bool`  e.g. `true`, `true`, `true`
    - `lastexittime` — `object`
      - `$date` — `object`
        - `$numberlong` — `string`  e.g. `1712577985000`, `1712577992000`, `1712577991000`
    - `name` — `string`  e.g. `[REDACTED]`
    - `offline` — `bool`  e.g. `false`, `true`, `false`
    - `relativepercentattendance` — `object`
      - `$numberint` — `string`  e.g. `100`, `35`, `100`
    - `user_email` — `string`  e.g. `[REDACTED]`
    - `user_id` — `string`  e.g. `16805888`, `16778240`, `16812032`
    - `userduration` — `object`
      - `$numberint` — `string`  e.g. `0`, `0`, `0`
    - `wiseuserid` — `object`
      - `$oid` — `string`  e.g. `65fbd7c1e202d2817cbbf53e`, `6613c7343cfccf97cff4583e`, `660e9b0e79ef94fdb4d03f11`

### `comments`



### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1712294950025`, `1712296292319`, `1712296780047`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1712579105998`, `1728042851748`, `1728042851748`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

### `duration`

- `$numberint` — `string`  e.g. `2503000`, `3589000`, `3661000`

### `end_time`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1712577992000`, `1712817004000`, `1716272181000`

### `scheduledstarttime`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1712575800000`, `1712813400763`, `1716267600678`

### `scheduledendtime`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1712579400000`, `1712817000763`, `1716271200678`

### `participant`

- `$numberint` — `string`  e.g. `3`, `1`, `1`

### `maxparticipantduration`

- `$numberint` — `string`  e.g. `2179`, `3468`, `3625`

### `metadata`

- `autorecord` — `bool`  e.g. `true`, `true`, `true`
- `endedby` — `string`  e.g. `6a2ffff1904c8925d456d619`, `69d4e18998ee51775f3010e8`
- `endreason` — `string`  e.g. `host_waiting`, `waiting_meeting_cron`, `waiting_meeting_cron`
- `isownerzoom` — `bool`  e.g. `false`, `false`, `false`
- `lensenabled` — `bool`  e.g. `false`, `true`, `true`
- `linkwashing` — `bool`  e.g. `true`
- `ownerid` — `object`
  - `$oid` — `string`  e.g. `65c9cb4799d4bfaa0c260207`, `64dcd26ce94bcfef6f8625b7`, `64dcd26ce94bcfef6f8625b7`
- `paiduser` — `bool`  e.g. `true`, `true`, `true`
- `poolname` — `string`  e.g. `DEFAULT`, `DEFAULT`, `DEFAULT`
- `recurrenceid` — `string`  e.g. `6a4e02d541b9900549694781`, `6a4e03d6ed0591b31de62db3`, `6a4e03e6b9a4e5a6750fe4a2`
- `registrationenabled` — `bool`  e.g. `true`, `true`
- `restartedsessions` — `array<object>|array<unknown>`
  - `restartedsessions[]` — `object`
    - `meetinguuid` — `string`  e.g. `jgaPdUjERBm/tqfryen0kA==`, `pf9c66I6Q9SkVnwKupUvkw==`, `AzpLUmHmRZGcRvnzaDkZGg==`
    - `sessionid` — `object`
      - `$oid` — `string`  e.g. `6a4e4d013447d975a55643dc`, `6a4e283fca57d945203becf4`, `6a4e2877321882d97aae27da`
- `waitingmeeting` — `bool`  e.g. `true`, `true`, `true`
- `webinar` — `bool`  e.g. `false`, `false`, `false`
- `zoomadminaccountid` — `string`  e.g. `63f8b2037eb779515cf43d21`, `63f8b2037eb779515cf43d21`, `63f8b2037eb779515cf43d21`
- `zoomuseraccountid` — `string`  e.g. `66fa77e2763295008ca2dde9`, `66fa77e9763295008ca2de05`, `66fa77bc763295008ca2dd45`
- `zoomuserid` — `string`  e.g. `VVwE2b6wR0i8daiiTMqYvg`, `totq-tR6RvObP8S-sEzqkA`, `XHoOtdXnQb603i6s2lQUZA`

### `recordings`

  - `[]` — `object`
    - `_id` — `object`
      - `$oid` — `string`  e.g. `6613e221a6a86f4944bce4ae`, `660fce8f1ab65459bb82df4a`, `660fa3cbae710aaddc410af2`
    - `duration` — `object`
      - `$numberint` — `string`  e.g. `2500`, `412`, `3446`
    - `file` — `object`
      - `_id` — `object`
        - `$oid` — `string`  e.g. `6613e221a6a86f98d7bce4af`, `660fce8f1ab654003382df4b`, `660fa3cbae710a0b18410af3`
      - `filename` — `string`  e.g. `video.m3u8`, `video.m3u8`, `video.m3u8`
      - `path` — `string`  e.g. `https://streaming.wiseapp.live/video-player/wise-video-playe`, `https://streaming.wiseapp.live/video-player/wise-video-playe`, `https://streaming.wiseapp.live/video-player/wise-video-playe`
      - `s3filepath` — `string`  e.g. `https://wise-app-s3-bucket.s3-ap-south-1.amazonaws.com/strea`, `https://wise-app-s3-bucket.s3-ap-south-1.amazonaws.com/strea`, `https://wise-app-s3-bucket.s3-ap-south-1.amazonaws.com/strea`
      - `s3key` — `string`  e.g. `streaming_videos/65c9cb4799d4bfaa0c260207/660f8c26561c412a02`, `streaming_videos/653360da131853429f1684bb/660fcbbf65f0367107`, `streaming_videos/64f1c364d64223528ddb0dce/660f942da2154aee3e`
      - `size` — `object`
        - `$numberint` — `string`  e.g. `85659036`, `15142750`, `73093631`
      - `subtype` — `string`  e.g. `hls_video`, `hls_video`, `hls_video`
      - `type` — `string`  e.g. `video`, `video`, `video`
    - `partindex` — `object`
      - `$numberint` — `string`  e.g. `1`, `1`, `1`
    - `sessionindex` — `object`
      - `$numberint` — `string`  e.g. `1`, `1`, `1`
    - `type` — `string`  e.g. `RECORDING`, `RECORDING`, `RECORDING`
    - `url` — `string`  e.g. `https://streaming.wiseapp.live/video-player/wise-video-playe`, `https://streaming.wiseapp.live/video-player/wise-video-playe`, `https://streaming.wiseapp.live/video-player/wise-video-playe`

### `rawrecordings`



## DDL

_From `IN` (processed)._

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
  'trino_query_id'='20260811_020726_00007_6egjx', 
  'trino_version'='0.215-24619-g93e00a8')
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
