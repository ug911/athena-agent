# eighttimeseight per-course client sheet: which columns are derivable, and where storage bytes actually live

- **id:** 1090ba57-8f5e-44c9-af21-9a52e65e66fc   **from:** eight-times-eight   **depth:** 0   **utc:** 20260917T071709Z

## Question

Client sheet for tenant namespace 'eighttimeseight' (IN host https://api.wiseapp.live), institute_id
64f1c3d0449bd300b9fe1208, owner user_id 64f1c364d64223528ddb0dce. ONE per-course row set with these
columns, and for each: exactly which Athena table+column in the IN 'processed' database carries it,
or that it is NOT derivable:

(1) Course Name
(2) Course ID
(3) Course type: Group / 1:1 / Recorded (and how PERSONAL type shows up)
(4) Number of live sessions that ACTUALLY RAN (conducted, not merely scheduled) - exact predicate
    (actual start/end time non-null? a status enum? meeting_status?) and what it silently gets wrong
(5) STORAGE ACCUMULATED IN THE COURSE - bytes of recordings and/or uploaded resources attributed to a
    course. THE CRITICAL ONE. Is there ANY fact/dimension table in processed (IN) carrying a file
    size / byte count / recording size / content size per session, per class, per institute? If yes,
    name table+column and say precisely what it covers (recordings only? recordings + uploaded
    resources? transcripts? chat?). If no such column exists in the fact layer, say so plainly and
    say whether the only route is an S3/object-store listing or a Wise API field - do NOT propose
    scanning raw lake_cdc.
(6) Last session at (date+time, and which timezone the column is in)
(7) Number of UPCOMING sessions (scheduled in the future) - which table holds future/scheduled
    sessions, since past-session facts may not

Also confirm: (a) that namespace eighttimeseight maps to IN / 'processed', and the right join from
namespace -> institute -> classes -> sessions; (b) whether 'is_enrolled' on IN has the same defect as
NA (counts REMOVED students as enrolled); (c) whether the class/course dimension in the fact layer
lets me filter out the ~26 'Demo Slot' classes (name contains 'demo') and the PERSONAL course type.

Runnable SQL for the whole sheet if derivable, and an explicit list of any column that is NOT
derivable from the fact layer.

RETURN: answer, confidence (high/medium/low + why), and what to check next.

## Verdict up front — two premise corrections

**1. The fact layer is not in `processed`. It is `lake_cdc.*_facts_v3`.** You asked for "which Athena
table+column in the IN `processed` database". `processed` is the **nightly mongodump CTAS** (~24 h
stale, mostly unpartitioned, JSON-in-varchar). The curated fact layer is
`lake_cdc.session_facts_v3` / `lake_cdc.session_participant_facts_v3`, partitioned
`bucket(64, institute_id)`, refreshed every 15 min, **region-agnostic** (`region` is an ordinary
column; there is no `_na` fact table). Six of your seven columns come from `session_facts_v3`.
I use `processed` only where the fact layer genuinely has nothing — which is exactly column (5).

**2. Storage bytes: a per-file byte count DOES exist, but only for uploaded study materials — never
for recordings.** The fact layer has no size/byte column at all. In `processed` there is exactly one
live per-class byte source:
`processed.study_materials_flat_v3.file_size` (bytes, joinable on `classid`). Recording bytes are
**not derivable from any layer** — the one table that ever carried `filesize`
(`processed.wise_app_backend__zoomrecordings`) **stopped being written on 2023-11-24**, and the live
replacement (`processed.wise_app_backend__raw_recording`) carries `duration` but **no size field at
all**, and is TTL-pruned to ~2 weeks. Recording bytes require an S3 listing. Details in §5.

---

## The per-column table

| # | Column | Source | Derivable? |
|---|---|---|---|
| 1 | Course Name | `lake_cdc.session_facts_v3.course_name` | ✅ |
| 2 | Course ID | `lake_cdc.session_facts_v3.class_id` | ✅ |
| 3 | Course type | `lake_cdc.session_facts_v3.course_type` ∈ `LIVE` / `ONE_TO_ONE` / `PERSONAL` | ✅ (no "Recorded" type — see §3) |
| 4 | Live sessions that actually ran | `count_if(is_conducted)` — **not** a time-nullness test | ✅ with caveats (§4) |
| 5a | Storage — uploaded resources | `processed.study_materials_flat_v3.file_size` (bytes) ⋈ `classid` | ⚠️ partial (§5) |
| 5b | Storage — recordings/transcripts/chat | **nothing, in any layer** | ❌ **NOT DERIVABLE** |
| 6 | Last session at | `max(start_time)` over `is_conducted`, `from_iso8601_timestamp(...)`, **UTC** | ✅ |
| 7 | Upcoming sessions | `session_facts_v3`, `status='UPCOMING' AND session_date` in [today, +90d) | ✅ |

**Explicit NOT-derivable list:** recording bytes; transcript bytes; chat bytes; total per-course or
per-institute storage footprint; any "Recorded course" type; walk-in/demo attendance (prior ask
`2cc2b387`); and — from the fact layer alone — `resource_bytes` for the 45 % of study-material rows
whose `file_size` is `0`.

---

## (a) Namespace → IN, and the join chain

`processed.institute` confirms it in one row (95 KB scanned):

| instituteid | name | namespace | ownerid |
|---|---|---|---|
| `64f1c3d0449bd300b9fe1208` | Eight Times Eight | `eighttimeseight` | `64f1c364d64223528ddb0dce` |

Both of your ids check out, and the namespace matches. **But do not key anything on namespace.**
One client can own many namespaces (`corizo` → 19), namespaces are truncated to ~24 chars, and many
unrelated tenants share `namespace='wise'`. `institute_id` is the only safe tenant key.

**"IN" is the right deployment, but the routing differs by layer:**
- `lake_cdc.*_facts_v3`: **no database swap and no region filter.** One table serves both regions.
  `WHERE institute_id = '64f1c3d0449bd300b9fe1208'` is the whole predicate — it is also the bucket
  partition key, so this prunes to 1/64 (~100 KB–9 MB per query here).
- `processed` (IN) vs `processed_na` (NA): **database swap**, as your playbook says. Correct for the
  study-materials join.
- Raw `lake_cdc.wise_app_backend__*`: `region = 'in'` partition. Not needed for this sheet.

**Join chain for the sheet — it is shorter than you expect:**

```
institute_id  ──(plain column, = bucket partition)──►  lake_cdc.session_facts_v3
                                                         ├─ class_id     (the course)
                                                         ├─ session_id   (the session)
                                                         └─ course_name / course_type / status / times
class_id  ──────────────────────────────────────────►  processed.study_materials_flat_v3.classid
```

There is **no namespace→institute→class→session hop to make**: `session_facts_v3` is already
pre-joined session ⋈ class ⋈ institute ⋈ teacher. You never touch a `class` table for this sheet.
`study_materials_flat_v3` has **no institute column** — scope it by joining `classid` to the
institute's `class_id` set from the fact (that is what the SQL below does).

## (b) `is_enrolled` on IN — **same defect, and it is worse than "counts REMOVED students"**

Measured on `lake_cdc.session_participant_facts_v3`, `institute_id = '64f1c3d0449bd300b9fe1208'`:

| rows | `is_enrolled = true` | distinct students | students with any `is_enrolled=true` |
|---|---|---|---|
| 686,989 | **686,920 (99.990 %)** | 5,776 | 5,770 |

It is effectively a **constant `true`**. Only 69 rows out of 687 k are false. Treat it as carrying
no information on IN, exactly as on NA — do not use it to define an active roster, and do not use it
as a filter (it removes nothing). You said you may not need it: you don't.

Related trap you will hit if you go per-student: **`attended` is not attendance.** It is
`participants[].wiseUserId IS NOT NULL`, and the app pre-lists enrolled students, so it is true for
absentees. Use `attend_minutes > 0`.

## (c) Filtering out Demo Slot and PERSONAL — **yes, both, from the fact alone**

`course_type` and `course_name` are both on `session_facts_v3`, so no dimension join is needed.

Institute-wide `course_type` census (8.9 MB scanned):

| course_type | sessions | classes | conducted | interpretation |
|---|---|---|---|---|
| `LIVE` | 50,069 | 576 | 44,324 | **Group** |
| `ONE_TO_ONE` | 17,506 | 759 | 16,427 | **1:1** |
| `PERSONAL` | 4,822 | **6** | **0** | booking-slot rooms for the demo product — **never conducted, ever** |

The exclusion predicate, confirmed against prior ask `2cc2b387`:

```sql
course_type <> 'PERSONAL'
AND lower(course_name) NOT LIKE '%demo%'
```

- `PERSONAL` is 6 classes / 4,822 sessions with `is_conducted = 0` on **every single row**. It is
  not a course type in any client-facing sense; drop it (or label it "booking slot").
- The demo classes are identified by **class name only** — `Demo Slot N`, 26 active classes. There is
  **no tag**: `class.metadata.tags` and `zoom.metadata.tags` are empty/NULL on all of them, and
  session *title* matching finds 3 rows out of 12,610 (the trap that put "demo is not derivable" into
  a published plan). `lower(course_name) LIKE '%demo%'` is the rule, and it is this **tenant's
  convention, not a platform one**.
- Add `'%trial%'` only if you also want to drop the single `ONE_TO_ONE` class `Ind Trial Class`.
- You will also want to look at the `Backup` / `ETE Backup Sessions N` / `BACKUP 4 OPERATIONS`
  classes — the largest non-demo course on the sheet is literally named `Backup` (1,535 conducted
  sessions). These are operational overflow rooms, not sellable courses. Not my call, but a client
  sheet that ranks `Backup` first will look wrong.

**Effect on this tenant** (one query, 47 MB): after excluding PERSONAL + demo →
**1,309 courses · 48,135 conducted sessions · 527 upcoming in 90 d · 2,096,825,959 resource bytes
(≈ 2.10 GB) across 949 study-material rows.**

---

## (3) Course type — and the missing "Recorded"

`course_type` has exactly three values for this tenant: `LIVE`, `ONE_TO_ONE`, `PERSONAL`. Map them
`Group` / `1:1` / booking-slot.

**There is no `RECORDED` course type.** If "Recorded" on your sheet means "a course delivered as
pre-recorded content", that concept does not exist as a course type in the fact layer. The nearest
thing is a class whose study materials are videos —
`study_materials_flat_v3.file_type IN ('youtube','links','upload_files')` — which is a property of
attached content, not of the course. For this tenant that is 52 classes with YouTube entries and 50
with links. **If you need a Recorded category, say so and it needs a definition first; do not
silently map PERSONAL to it.**

`PERSONAL` shows up as a full course_type row in the fact with a real `class_id` and `course_name`,
4,822 sessions, all future-or-missed, `is_conducted = false` on all of them. It is the demo-product
booking room whose bookings never run.

## (4) Sessions that actually ran — the exact predicate, and what each wrong one does

**Use `is_conducted`.** For this tenant `is_conducted` is exactly equivalent to `status = 'ENDED'`
(60,751 rows, both directions, zero disagreement).

**Do NOT use "actual start/end time non-null".** I tested it and it is a silent 100 % false positive:

| status | rows | `start_time` AND `end_time` both non-null |
|---|---|---|
| ENDED | 60,751 | 60,751 |
| MISSED | 9,661 | 9,661 |
| UPCOMING | 1,729 | 1,729 |
| CANCELLED | 250 | 250 |
| IN_PROGRESS | 6 | 2 |

`start_time` / `end_time` are **scheduled** times, present from the moment the session is created;
they are overwritten with actuals only sometimes, and only for ENDED. Evidence: on CANCELLED,
250/250 start times land on an exact round minute (`ss=0, ms=0`); on ENDED only 31,634/60,751 do —
i.e. ~48 % of ENDED rows carry a real, sub-minute actual timestamp and ~52 % still carry the
schedule. **A nullness test on these columns counts every missed, cancelled and future session as
conducted** — for eighttimeseight it would report 72,397 instead of 60,751, a **+19 % overcount**.

There is no `meeting_status` column on `session_facts_v3`. The status enum is
`ENDED / MISSED / UPCOMING / CANCELLED / IN_PROGRESS`.

**Secondary check that agrees:** `duration_minutes > 0` is true on 60,617 of 60,751 ENDED and on
**0** rows of every other status. So `duration_minutes` *is* actual. The 134-row gap (ENDED with
duration 0) is your honest "ran but zero measured length" bucket.

**What `is_conducted` silently gets wrong — say this on the sheet:**
1. **It counts teacher-only rooms as conducted.** A session where the host opened the room and nobody
   came is `ENDED`. On the demo classes this is ~60 % of sessions (prior ask `2cc2b387`: 12,552
   conducted Demo Slot sessions, only 5,447 with a participant who stayed > 0 s). If you want
   "actually taught", add `participant_count > 0`.
2. **It cannot see walk-ins.** `session_participant_facts_v3` drops every participant with
   `wiseUserId IS NULL` (`facts_v3.py:249`), so demo/prospect attendance reads as **zero** in the
   participant fact while `session_facts_v3.participant_count` is positive. Check
   `participant_count`, not the participant fact, before concluding nobody came.
3. **`MISSED` (9,661 here) is a real category you are discarding.** It is scheduled-and-not-run. I
   return it as its own column in the SQL so the sheet can show it rather than hide it.
4. `IN_PROGRESS` (6 rows) is neither conducted nor upcoming. Rounding error here, but it exists.

## (5) STORAGE — the critical one, answered plainly

I searched `information_schema.columns` across `processed`, `lake_cdc` and `backend` for every column
matching `%size%`, `%byte%`, `%storage%`, `%length%`, `%capacity%`. **Twelve columns exist in the
whole account.** Here is every one, and what it is:

| table.column | grain | status |
|---|---|---|
| `processed.study_materials_flat_v3.file_size` | **per uploaded file, has `classid`** | ✅ **LIVE — the only usable one** |
| `processed.wise_app_backend__zoomrecordings.recordings[].filesize` | per recording file, has `classid` | ❌ **DEAD — last write 2023-11-24** |
| `backend.storage_computation.bytes` | per `user_id`, per folder/path | ❌ **DEAD — a one-off snapshot, `LOCATION .../date=2022-03-10`** |
| `processed.streaming_computation.bytes_mbs` | per `userid` per day | ❌ **DEAD — `LOCATION .../dt=2022-03-13`**, and it is egress anyway |
| `processed.user_streaming_usage.*` (4 `mbs used in …` cols) | per `userid` per day | ⚠️ live but **egress/bandwidth, not storage**, and no class |
| `processed.wise_app_backend__user_streaming_info.totalstreamedgbs` | per `userid` | ⚠️ live but **cumulative streamed GB, not stored GB** |
| `processed.cloudfront_logs` / `cloudfront_file_logs.bytes`, `request_bytes` | per HTTP request | ⚠️ CDN egress, not storage |
| `backend.cloudfront__2025_03_20.*` | per request | ❌ single-day table |

### 5a. Uploaded resources — derivable, with real caveats

`processed.study_materials_flat_v3` is a **view** over `wise_app_backend__study_materials`. It has
`classid`, `userid`, `file_type`, `file_path`, and `file_size` (a **varchar of bytes**, extracted as
`json_extract(r, '$.file.size["$numberint"]')`, defaulting to the string `'0'`).

Fleet-wide: 724,664 rows · 32,788 classes · **7.31 TB** · 326,897 rows (45 %) have `file_size = '0'`.

For eighttimeseight (join `classid` to the institute's `class_id` set — 39.9 MB):

| file_type | rows | classes | `file_size='0'` | bytes |
|---|---|---|---|---|
| `upload_files` | 588 | 99 | **0** | **2,096,805,959 (1.95 GiB)** |
| `links` | 213 | 50 | 211 | 20,000 |
| `youtube` | 148 | 52 | 148 | 0 |

**Good news for this tenant specifically:** every `upload_files` row has a real byte count — the 45 %
zero rate fleet-wide is almost entirely YouTube/external links, which legitimately consume no Wise
storage. So per-course uploaded-resource bytes are trustworthy here.

**Caveats to carry:**
- Only `$numberint` is read by the view. A file **> 2,147,483,647 bytes (2 GiB)** would be stored as
  `$numberLong`/`$numberDouble` and the view returns `'0'` for it. I found no `$numberlong` sizes in
  the recording table, and zero-rate on this tenant's `upload_files` is 0/588, so this is a latent
  risk rather than an observed loss — but a single 3 GB upload would vanish silently.
- `file_size` is a **varchar**: always `try_cast(... AS bigint)`, never bare `CAST`.
- 24 h stale (nightly `mongo_etl`), unlike the 15-min facts. Your sheet will mix freshnesses.
- The view is unpartitioned; every query scans ~32 MB fleet-wide. Fine for a client sheet, not for a
  high-frequency job.
- It attributes a file to the class it was **attached to**, not to who paid for the bytes, and there
  is no dedup — the same S3 object attached to two classes is counted twice.

### 5b. Recordings — **NOT DERIVABLE. Full stop.**

This is the answer you needed most, so here is the whole chain of evidence.

**`lake_cdc.session_facts_v3` has no size column.** I read the full DDL: 46 columns, and the only
volume-ish ones are `duration_minutes`, `participant_count`, `ai_quiz_count`, `live_test_count`.
Nothing about bytes, files, or recordings beyond `has_revision_notes` (a boolean). Same for
`session_participant_facts_v3`. **The fact layer does not know how large anything is.**

**`processed.wise_app_backend__zoomrecordings` — the only table that ever had it, and it is dead.**
This one genuinely looked like the answer: `recordings` is a JSON array whose elements are
`{_id, createdat, duration, filepath, filesize, type}` — real byte counts (`$numberint`), real
durations (seconds), real S3 paths, **and a `classid`**. Fleet totals: 632,155 docs / 391,074
recording entries / **57.99 TB** (40.92 TB untyped + 17.08 TB `RECORDING`; 15,669 `YOUTUBE` entries
carry no size and no path). Encoding census: 375,304 `$numberint`, 101 `$numberdouble`, **0
`$numberlong`**, 15,669 missing.

Then it fails on three counts:
1. **`max(createdat) = 1700819537 = 2023-11-24.`** The collection has not been written in ~34 months.
2. **`sessionid` is a base64 Zoom meeting UUID** (`xa0Ix35zQAatxWYVL+0tZA==`), not a Wise session
   ObjectId — 0 of 632,155 rows match `^[0-9a-f]{24}$`. It cannot be joined to `session_facts_v3` at
   all without a UUID bridge.
3. Consequently **eighttimeseight has exactly zero rows in it.** I ran the `classid` join and got
   `row_count: 0`. Their first session is 2024-09-17, ten months after the table stopped.

`classid` is also JSON-wrapped (`{"$oid":"..."}`) there, which is a second reason a naive join
returns 0 — but the date is the real killer, so don't "fix" the join and think you've found it.

**`processed.wise_app_backend__raw_recording` — live, and it has no size field.** 153,873 docs,
`max(createdat)` = 2026-09-16 (current), `sessionid` is a **proper ObjectId** (153,873/153,873), so
it joins cleanly to `session_facts_v3.session_id`. Its `recordings` array elements have exactly one
key set, on all 331,748 entries: **`_id, duration, partindex, sessionindex, type, url`**. There is
**no `filesize`, no `size`, no `bytes`**. The field was dropped between the two generations of the
recording pipeline.

And it is **TTL-pruned**, so it is useless even as a coverage proxy. Conducted sessions for
eighttimeseight vs. how many have a `raw_recording` pointer:

| month | conducted | with pointer |
|---|---|---|
| 2026-01 … 2026-08 | 2,441 / 2,372 / 2,960 / 3,414 / 4,117 / 3,959 / 4,835 / 4,461 | **0 on every month** |
| 2026-09 (partial) | 2,268 | **156** |

That is the 1-day Mongo TTL on `RawRecording.expiresIn` (3 months for `customS3` tenants, never for
`keepRawRecordings` tenants — see ask `8d661222`). The pointer document is deleted, so the nightly
dump only ever sees the last few days. **`recorded_seconds` from this table is a ~7 % sample of the
current month and 0 % of history.** I return it in the SQL for completeness, clearly labelled, and
you should not put it on a client sheet.

**Transcripts and chat: pointers exist, sizes do not.**
`lake_cdc.wise_app_backend__rawsessiontranscript` and `__rawchat` (and their `processed` twins) carry
`{url, partIndex, sessionIndex, meetingUUID, file}` per file — **no byte count** (ask `e9e89a4e`).
Coverage for this institute is known: **11,594 of 13,212 conducted sessions in 90 d (87.8 %) have a
transcript; 5,238 (39.6 %) have a chat log** — but that is object *counts*, not bytes. VTT and TXT
files are small enough that they are rounding error against MP4/HLS anyway.

### So what IS the route to recording bytes?

**S3 object listing. That is the only route, and there is no Wise API field either.**

- The objects are in `wise-app-s3-bucket` (ap-south-1), fronted by `files.wiseapp.live`
  (`na-files.wiseapp.live` for NA; NA bucket name unknown). Prefixes:
  `streaming_videos/<ownerOID>/…/video.m3u8` (durable HLS),
  `ephemeral_raw_recordings/` (raw MP4, ~24 h), `upload_files/<ownerOID>/` (transcripts, chat,
  study materials), `session_recordings/`, `embedded_content/`.
- `aws s3api list-objects-v2 --bucket wise-app-s3-bucket --prefix streaming_videos/<ownerOID>/`
  gives `Size` per object. **Per-owner it is straightforward; per-COURSE it is not** — the key
  contains `<ownerOID>` and `<sessionOID>`, never a `class_id`. You would list by owner, extract the
  session OID from the key, and join back to `session_facts_v3.session_id → class_id`. That mapping
  does exist and is reliable.
- Cheaper than a full listing: **S3 Inventory** or a CloudWatch `BucketSizeBytes` metric by prefix,
  if either is configured. Worth one check before writing a lister.
- **The Wise API adds nothing.** `UserController.js:1519` returns the stored `files` array verbatim,
  unsigned — the API's values are byte-identical to the lake's, and neither carries a size. There is
  no "storage used" field on the institute or class model.
- **34.2 % of IN transcript files (and 10.6 % of chat files) live on customer-owned S3 buckets**
  (`customS3` tenants: `learn2read-wise-recordings`, `ischoolingwise`, `k12wise`,
  `tutoroot-wise-recordings`, …). A Wise-bucket listing would silently under-count those tenants.
  **eighttimeseight is 100 % on Wise-owned buckets**, so this does not bite you here — but any
  fleet-wide storage number built this way is wrong by a third.

And per your instruction: I am **not** proposing a raw `lake_cdc` scan. It would not help — the
underlying Mongo documents have no size field either, which is the actual reason this column is
missing. The correct fix is a fact:

> **Fact request — `session_storage_facts`**, grain `(institute_id, session_id)`, bucketed on
> `institute_id`: `recording_bytes, recording_seconds, hls_bytes, transcript_bytes, chat_bytes,
> object_count, storage_host`, populated from S3 Inventory joined to the existing pointer tables.
> Roll up to `class_id` for a course sheet. This is the third time a caller has needed bytes per
> session (asks `8d661222`, `e9e89a4e`, this one).

## (6) Last session at — and the timezone

```sql
max(CASE WHEN is_conducted THEN from_iso8601_timestamp(start_time) END)
```

`start_time` / `end_time` are **varchars** holding ISO-8601 with an explicit `Z`:
`2024-09-17T03:30:00.000Z` … `2039-10-22T13:30:00.000Z`. **They are UTC.** `from_iso8601_timestamp`
respects the `Z`, so the result is UTC — for an IN client sheet you will want
`+ interval '5' hour + interval '30' minute` (or `at_timezone(..., 'Asia/Kolkata')`) and you should
label the column, because 03:30 UTC is 09:00 IST and an unlabelled "last session 03:30" reads as
nonsense to the client.

Two things to guard:
- **Gate on `is_conducted`.** Without it, `max(start_time)` returns the furthest-future *scheduled*
  session — for this tenant, **2039-10-22**. That is the single most likely way this column ships
  wrong.
- `session_date` is a proper `DATE` column (and the natural window key); the times are strings. Don't
  mix them without casting.

## (7) Upcoming sessions

`session_facts_v3` **does** carry future sessions — this is one table for past and future, so no
second source is needed. For eighttimeseight:

| measure | value |
|---|---|
| `is_upcoming` flag true | 1,354 |
| `session_date >= current_date` | 1,363 |
| `session_date` within **90 days** | **620** |
| `status='UPCOMING' AND session_date >= current_date` | 1,342 |
| `status='UPCOMING' AND` within 90 d | **602** |
| `max(session_date)` | **2039-10-22** |

**Use `status = 'UPCOMING' AND session_date >= current_date AND session_date < current_date +
interval '90' day` → 602.** Reasons:
- **Bound the window.** Recurring schedules project to **2039** for this tenant (fleet max 2052-10-21).
  Unbounded "upcoming" is 1,363 vs 620 real ones — a **2.2× overcount** of a client-facing number.
- Prefer `status='UPCOMING'` over the `is_upcoming` boolean. `is_upcoming` also flags 12 **CANCELLED**
  sessions, and it is recomputed only for rows the 15-min refresh touches, so it drifts on cold rows
  (it happened to be clean here — 0 rows with `is_upcoming AND session_date < current_date` — but
  that is not guaranteed, whereas the `status` + `session_date` form is evaluated at query time).

---

## Runnable SQL — the whole sheet

```sql
-- intent: eighttimeseight (IN) per-course client sheet: type, conducted/missed counts,
--         uploaded-resource bytes, last conducted session (UTC + IST), upcoming in 90d.
-- Recording BYTES are deliberately absent: no column exists in any layer (see §5b).
WITH s AS (
  SELECT class_id, course_name, course_type, session_id, status,
         is_conducted, start_time, session_date, participant_count
  FROM lake_cdc.session_facts_v3
  WHERE institute_id = '64f1c3d0449bd300b9fe1208'   -- bucket partition: prunes to 1/64
    AND course_type <> 'PERSONAL'                   -- booking-slot rooms, 0 ever conducted
    AND lower(course_name) NOT LIKE '%demo%'        -- 26 'Demo Slot N' classes (tenant convention)
),
agg AS (
  SELECT class_id,
         max(course_name)  AS course_name,
         max(course_type)  AS course_type,
         count_if(is_conducted)                       AS sessions_conducted,
         count_if(is_conducted AND participant_count > 0) AS sessions_with_attendee,
         count_if(status = 'MISSED')                  AS sessions_missed,
         count_if(status = 'CANCELLED')               AS sessions_cancelled,
         max(CASE WHEN is_conducted
                  THEN from_iso8601_timestamp(start_time) END) AS last_session_at_utc,
         count_if(status = 'UPCOMING'
                  AND session_date >= current_date
                  AND session_date <  current_date + interval '90' day) AS upcoming_90d
  FROM s GROUP BY class_id
),
res AS (   -- uploaded study materials: the ONLY live per-class byte source
  SELECT sm.classid AS class_id,
         count(*)                                          AS resource_files,
         count_if(try_cast(sm.file_size AS bigint) > 0)     AS resource_files_sized,
         sum(coalesce(try_cast(sm.file_size AS bigint), 0)) AS resource_bytes
  FROM processed.study_materials_flat_v3 sm
  JOIN (SELECT DISTINCT class_id FROM s) c ON c.class_id = sm.classid
  GROUP BY sm.classid
),
rec AS (   -- duration only, NO bytes, and TTL-pruned to ~2 weeks. Diagnostic, not a sheet column.
  SELECT s.class_id,
         count(DISTINCT rr.sessionid) AS sessions_with_recording_ptr,
         sum(coalesce(try_cast(json_extract_scalar(r, '$.duration["$numberint"]')    AS bigint),
                      try_cast(json_extract_scalar(r, '$.duration["$numberdouble"]') AS bigint),
                      0)) AS recorded_seconds_partial
  FROM processed.wise_app_backend__raw_recording rr
  CROSS JOIN UNNEST(CAST(json_parse(rr.recordings) AS array(json))) t(r)
  JOIN s ON s.session_id = json_extract_scalar(rr.sessionid, '$["$oid"]')
  GROUP BY s.class_id
)
SELECT
  agg.course_name,
  agg.class_id AS course_id,
  CASE agg.course_type WHEN 'LIVE'       THEN 'Group'
                       WHEN 'ONE_TO_ONE' THEN '1:1'
                       WHEN 'PERSONAL'   THEN 'Booking slot (never conducted)'
                       ELSE agg.course_type END          AS course_type,
  agg.sessions_conducted,
  agg.sessions_with_attendee,
  agg.sessions_missed,
  agg.sessions_cancelled,
  coalesce(res.resource_files, 0)                        AS resource_files,
  coalesce(res.resource_files_sized, 0)                  AS resource_files_sized,
  coalesce(res.resource_bytes, 0)                        AS resource_bytes,
  round(coalesce(res.resource_bytes, 0) / 1048576.0, 1)  AS resource_mib,
  CAST(NULL AS bigint)                                   AS recording_bytes,  -- NOT DERIVABLE (§5b)
  coalesce(rec.sessions_with_recording_ptr, 0)           AS recording_ptrs_last_2w,
  coalesce(rec.recorded_seconds_partial, 0)              AS recorded_seconds_last_2w,
  agg.last_session_at_utc,
  agg.last_session_at_utc + interval '5' hour + interval '30' minute AS last_session_at_ist,
  agg.upcoming_90d
FROM agg
LEFT JOIN res ON res.class_id = agg.class_id
LEFT JOIN rec ON rec.class_id = agg.class_id
ORDER BY agg.sessions_conducted DESC
```

Validated: `EXPLAIN` clean, ran at `max_rows=25`. **~58 MB scanned**, ~90 % of which is the two
unpartitioned `processed` tables — the fact side is ~9 MB. For NA, swap `processed` →
`processed_na` and change `institute_id`; **do not** swap the `lake_cdc` names, there is no NA twin.

Top of the result, for sanity (this is the un-excluded run, so demo rows are visible):

| course_name | course_id | type | conducted | resource_bytes | rec_ptrs | last_session_at_utc | upcoming_90d |
|---|---|---|---|---|---|---|---|
| Backup | `6668522e7677051152fc9048` | Group | 1,535 | 0 | 2 | 2026-09-16 14:30:00 | 2 |
| Demo-Slot 1 | `65def6963ceb88cced120541` | Group | 1,010 | 0 | 0 | 2026-09-07 13:19:48 | 0 |
| Demo Slot-10 | `68b68b8a744918c346c3cd49` | Group | 790 | 0 | 5 | 2026-09-17 01:23:53 | 0 |
| Backup session 3 | `6606bc9547f778809f0e8cf5` | Group | 714 | 0 | 0 | 2026-09-15 12:30:00 | 0 |
| ETE Backup Sessions 1 | `657acab6493a3b3d7c724d8a` | Group | 498 | 0 (1 link row) | 1 | 2026-09-16 15:30:00 | 0 |

Note `Backup`'s `14:30:00` vs `Demo Slot-10`'s `01:23:53.364` in the same column — that is the
scheduled-vs-actual `start_time` mixture from §4 showing up in your own data.

---

## Confidence

**High** on: the namespace/institute/owner mapping (single-row exact match); the fact layer being
`lake_cdc` not `processed`; the `course_type` census and the PERSONAL-never-conducted finding (0 of
4,822, exhaustive); `is_conducted ≡ status='ENDED'`; the start/end-time nullness test being a 100 %
false positive across all statuses (exhaustive count, not a sample); the round-minute evidence that
these are scheduled times; `is_enrolled` being 99.990 % true on IN (exhaustive, 686,989 rows); the
90-day upcoming bound and the 2039 horizon; the timezone being UTC (explicit `Z` on every value);
`session_facts_v3` having no size column (read the full 46-column DDL); the `information_schema`
sweep being exhaustive for the five size-ish name patterns across all three databases;
`zoomrecordings` being dead at 2023-11-24 with zero rows for this tenant (ran the join, got 0);
`raw_recording` having no size key on all 331,748 entries; and the `raw_recording` coverage being
0 rows before September (month-by-month, exhaustive).

**Medium** on: "recording bytes are nowhere in the account". I swept column *names* for five
patterns across `processed`/`lake_cdc`/`backend` — a byte count hiding inside an un-suggestively
named JSON varchar in some table I did not unnest would have been missed. I checked the two obvious
recording tables' JSON key sets directly, which is why I'd still bet on this, but it is a name-based
sweep, not a value-based one. Also medium on the `$numberint`-overflow risk for study materials: I
found no case, but I did not go looking for a >2 GiB upload.

**Low / not checked:** whether S3 Inventory or a per-prefix CloudWatch metric already exists for
`wise-app-s3-bucket` (I cannot read AWS config from here — this is the thing that would make §5b's
workaround cheap or expensive); whether `processed.wise_app_backend__zoomrecordings` has a live NA
counterpart; whether the `Backup*` classes should be on a client sheet at all (a business call);
and what "Recorded" is supposed to mean on your sheet.

## What I would check next

1. **`aws s3api list-objects-v2 --bucket wise-app-s3-bucket --prefix streaming_videos/64f1c364d64223528ddb0dce/ --query 'sum(Contents[].Size)'`** — one command against the owner OID you already have. It settles whether the S3 route gives you a real per-course number, and it is the only path to column (5b).
2. Before writing a lister: check for an **S3 Inventory** configuration on the bucket, and for a CloudWatch `BucketSizeBytes` metric with a prefix filter. If Inventory exists, `session_storage_facts` is a day of work instead of a week.
3. **Decide what "Recorded" means** and tell me — if it is "class has video study materials", that is derivable today from `study_materials_flat_v3.file_type`; if it is a product type, it does not exist in the data and the column should be dropped from the sheet.
4. **Decide on the `Backup*` / `ETE Backup Sessions*` classes.** They are the largest non-demo courses and almost certainly operational, not sellable.
5. If you want "actually taught" rather than "room opened", add `participant_count > 0` and compare the two columns on the demo-excluded set — I've put both in the SQL so you can see the gap before choosing.
6. Sanity-check the sheet's freshness story with the client: columns 1,2,3,4,6,7 are ~30 min stale; column 5a is up to 24 h stale. Worth a footnote.

## Evidence

All read-only Athena, IN. Query ids as returned by the MCP server.

- `0702b7ce` — `processed.institute` for `64f1c3d0449bd300b9fe1208` → Eight Times Eight / `eighttimeseight` / owner `64f1c364d64223528ddb0dce`. 95 KB.
- `describe_table lake_cdc.session_facts_v3` — full 46-column DDL, `PARTITIONED BY (bucket(64, institute_id))`. **No size/byte column.**
- `7fa712c5` — `information_schema.columns` sweep over `processed`/`lake_cdc`/`backend` for `%size%|%byte%|%storage%|%length%|%capacity%` → **12 columns total**, listed in §5. 317 KB.
- `18051b27` — `information_schema.tables` sweep for `%record%|%storage%|%transcript%|%chat%|%file%|%material%|%stream%|%video%` → 40 tables.
- `2c899e36` — `course_type` census: LIVE 50,069/576 classes/44,324 conducted · ONE_TO_ONE 17,506/759/16,427 · PERSONAL 4,822/6/**0**. 8.9 MB.
- `a9638d44` — status census: ENDED 60,751 (=`is_conducted`, `duration_minutes>0` on 60,617) · MISSED 9,661 · UPCOMING 1,729 · CANCELLED 250 · IN_PROGRESS 6. `end_time` non-null on **every** row of every status.
- `28be36bb` — round-minute test: CANCELLED 250/250 round; ENDED 31,634/60,751 → ~52 % of ENDED still carry the schedule, proving start/end are scheduled-with-partial-overwrite.
- `6e023ea1` — upcoming: `is_upcoming` 1,354 · `session_date>=today` 1,363 · **90 d 620** · `status='UPCOMING'` + 90 d **602** · stale flag 0 · `max(session_date)` **2039-10-22**.
- `4f0c208c` — `is_enrolled` on IN: 686,920 true / 686,989 rows; 5,770 of 5,776 students. 1.4 MB.
- `da287a4d` — `study_materials_flat_v3` fleet: 724,664 rows / 32,788 classes / 7.31 TB / 326,897 rows `file_size='0'` / 22 NULL.
- `0d8f4a6b` — same view joined to this institute's `class_id` set: `upload_files` 588 rows / 99 classes / **2,096,805,959 bytes** / 0 zero-sized; `links` 213 (211 zero); `youtube` 148 (all zero). 39.9 MB.
- `describe_table processed.study_materials_flat_v3` — it is a VIEW; `file_size` is `json_extract(r,'$.file.size["$numberint"]')` with `ELSE CAST(0 AS varchar)`.
- `61bd2839` / `17bdd343` / `ad1c8d3b` / `bcea9a3f` / `754f528b` — `zoomrecordings`: 632,155 docs / 632,069 sessions / 25,351 classes; element keys `_id, createdat, duration, filepath, filesize[, type]`; filesize encoding 375,304 `$numberint`, 101 `$numberdouble`, **0 `$numberlong`**, 15,669 missing (all `YOUTUBE`); totals 40.92 TB untyped + 17.08 TB `RECORDING`.
- `14e3b2ed` — `zoomrecordings` **`max(createdat) = 1700819537` = 2023-11-24**; `min` 2021-01-11; `sessionid` matches `^[0-9a-f]{24}$` on **0** of 632,155 rows (it is a base64 Zoom meeting UUID); `classid` non-null 632,137 but JSON-wrapped.
- `a8f1a2f7` / `c9482c56` — sample rows showing `classid = {"$oid":"..."}` and `sessionid = 'xa0Ix35zQAatxWYVL+0tZA=='`.
- `dde72461` — `zoomrecordings` ⋈ this institute's `class_id` set → **`row_count: 0`**.
- `7fa6e12c` / `027c8262` — `processed.wise_app_backend__raw_recording`: 153,873 docs, `sessionid` a valid OID on **153,873/153,873**, `max(createdat)` = 2026-09-16 (live), `min` 2025-01-27; element keys on all 331,748 entries are exactly `_id, duration, partindex, sessionindex, type, url` — **no size field**.
- `133d77d9` — `raw_recording` coverage for this institute by month: 0 pointers for Jan–Aug 2026 (28,559 conducted), 156 of 2,268 in Sep. Confirms the 1-day `RawRecording.expiresIn` TTL.
- `describe_table` on `processed.streaming_computation` (`LOCATION .../dt=2022-03-13`), `backend.storage_computation` (`LOCATION .../date=2022-03-10`, 496,253 rows, `user_id` grain), `processed.user_streaming_usage` (4 `mbs used in …` egress columns), `processed.wise_app_backend__user_streaming_info` (`totalstreamedgbs`).
- `989d90bc` — the full sheet query, 25 rows, 57.6 MB.
- `f6319faa` — demo+PERSONAL-excluded totals: 1,309 courses · 48,135 conducted · 527 upcoming 90 d · 2,096,825,959 resource bytes / 949 rows. 47.3 MB.

Prior knowledge reused (not re-derived): `2cc2b387` (Demo Slot classes are name-only, 26 active, no
tags, walk-ins dropped by `facts_v3.py:249`); `e9e89a4e` (transcript/chat pointer tables, key shapes,
87.8 %/39.6 % coverage for this institute, 34.2 % IN custom-S3 share, API returns `files` verbatim);
`8d661222` (`RawRecording.expiresIn` TTL 1 day / 3 months customS3 / none for `keepRawRecordings`,
`streaming_videos` durable); `COMPACT.md` §1–3, §6.1–6.4.

## Gotcha

**A byte count existed, was joinable to a course, and was abandoned.**
`zoomrecordings.recordings[].filesize` is exactly the column this sheet needs — bytes, duration,
path, and a `classid` — with 57.99 TB of real data in it. It stopped being written on 2023-11-24, and
the pipeline that replaced it **dropped the size field**: `raw_recording` keeps `duration` and `url`
and nothing else. So the capability regressed, silently, and the only trace is a stale table that
still describes itself as current in the catalog.

Worse, it fails *closed* in a way that looks like a join bug. The `classid` there is JSON-wrapped and
the `sessionid` is a base64 Zoom UUID, so the first join anyone writes returns zero rows. The natural
next move is to fix the extraction — and you still get zero rows, because the tenant simply
post-dates the table. Someone will spend a day on the `$oid` wrapper before checking
`max(createdat)`. **Check a table's high-water mark before debugging its join keys.**

Third: the same tenant's `start_time` column mixes scheduled and actual timestamps *within the
ENDED status* — 48 % actual, 52 % schedule. Both look like valid timestamps, and `max()` over them
returns something plausible either way. There is no flag distinguishing them; the only tell is
whether the seconds are zero.
