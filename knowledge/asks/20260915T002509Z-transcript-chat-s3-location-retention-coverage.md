# Where session transcript VTTs and chat logs live in S3, whether a lake table maps them, retention, access and coverage

- **id:** e9e89a4e-d922-4069-bafe-907f2984b7f6   **from:** wise-student-reports   **depth:** 0   **utc:** 20260915T002509Z

## Question

Read-only ask about session transcript VTTs and chat logs in S3, answered from the lake and code, no
escalation, marking unconfirmed items UNKNOWN. Caller's premise: transcript VTTs already live in S3
within the Wise ecosystem and can be reached without going back through the Wise API session by
session. Six parts: (1) bucket/key shape/prefix and position relative to `streaming_videos/` and
`ephemeral_raw_recordings/`; (2) is there a lake table mapping session → transcript object key, or
must it be derived; (3) retention — TTL like raw MP4s, or persist; (4) what can read them — wise-1
GCP service account vs a Wise AWS credential (names only), and are the URLs public; (5) coverage for
ThinkTank Jr (`69b84f3c99b41087144ba02e`, NA) and Eight Times Eight (`64f1c3d0449bd300b9fe1208`, IN)
over conducted sessions in the last 90 days; (6) the same six answers for `rawChats`.

## Answer

**Premise is TRUE, with one large exception.** Both mapping tables exist and are current:
`lake_cdc.wise_app_backend__rawsessiontranscript` (in 2,381,861 docs / 2,421,082 files; na 50,820 /
51,903) and `lake_cdc.wise_app_backend__rawchat`, latest `ingested_at` 2026-09-15 00:12 UTC.
**The API adds nothing** — `UserController.js:1519` is `session.rawTranscript = rawTranscript?.files
|| []`, returning the stored array verbatim, unsigned. The lake URL is byte-identical to the API's.

**The exception: 34.2% of IN transcript files live on customer-owned S3 buckets** (`customS3`
tenants), not Wise's. NA is 100% Wise-owned.

**(1) Location.** Bucket `wise-app-s3-bucket`, `ap-south-1`, fronted by CDN `files.wiseapp.live`
(mapping visible in `fileDeletionWorker.js:12`); NA uses `na-files.wiseapp.live` — **NA bucket name
UNKNOWN**. Key shape, 100% uniform on Wise buckets (51,903/51,903 NA):
`https://{na-,}files.wiseapp.live/upload_files/<ownerOID>/<sessionOID>-transcript-<sessionIndex>.<partIndex>.vtt`
⚠ The caller's observed `-transcript-<n>.vtt` is **wrong — there are two numbers**
(sessionIndex.partIndex). Prefix is `upload_files/`: not `streaming_videos/`, not
`ephemeral_raw_recordings/`; own prefix, same bucket.

IN host split of 2,421,082 files: `files.wiseapp.live` 1,593,544 (65.8%); custom 827,538 (34.2%) —
`learn2read-wise-recordings` 439,440, `ischoolingwise` 238,536, `k12wise` 97,216,
`tutoroot-wise-recordings` 38,008, `tr-n-video-support` 11,806, `topmate-call-recordingsv2` 2,525,
`rawlivevideorecordings` 7. Custom prefixes vary (`recordings/`, `class_recordings/`,
`wise-production/`, `wise_zoom_recordings/`, sometimes `upload_files/<OID>/`).

**⚠ CORRECTION to my earlier ask `8d661222`:** I described these as "**protected** prefixes" from
`fileDeletionService.js:54`. That was a misread. The line is `validateDBFilesPath`, a sanity guard
that throws if a key queued for deletion is **not** under a known prefix — it asserts the deletion
pipeline handles only known prefixes, it does **not** make them undeletable.

**(2) Mapping — the table exists; do not derive.** Doc shape
`{ sessionId: ObjectId(ref 'zoom'), files: [{url, partIndex, sessionIndex, meetingUUID, file}] }`,
unique index on `sessionId`. Extract with
`json_extract_scalar(doc,'$["sessionId"]["$oid"]')` + `UNNEST(cast(json_extract(doc,'$.files') AS
array(json)))`, `WHERE region='na'`. Joins to `session_facts_v3.session_id`. Derivation is unsafe:
the `<ownerOID>` segment is not derivable from the session id, and a third of IN files sit on other
hosts and prefixes entirely.

**(3) Retention — persists, no TTL.** `RawSessionTranscript` has only
`[{sessionId:1},{unique:true}]`; `RawChat` likewise. Neither has `expiresIn`. Control: `RawRecording`
*does* carry `[{expiresIn:1},{expireAfterSeconds:0}]`. Deletion is event-driven only, via
`DeletedFile` → queue → S3 delete (`entityType` includes `SESSION`); `DeletedFile`'s own 30-day TTL
(`expireAfterSeconds: 2592000` on `deletedAt`) expires the bookkeeping record, not the file.
**S3 lifecycle on `upload_files/`: UNKNOWN** — cannot read bucket config from the repos.

**(4) Access.** Credential names only: `AWS_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY`, `AWS_REGION`,
`AWS_S3_URL`, `FILES_S3_CDN_HOST` (plus `STREAMING_CDN_HOST`, `HLS_KEYS_HOST`,
`HLS_KEYS_ENCRYPTION`). **A GCP service account cannot authenticate to S3** — S3 takes AWS SigV4 or
unauthenticated access, so either the CDN serves them openly (no credential needed) or an AWS
credential is required. Whether wise-1 has one provisioned: **UNKNOWN**.
URLs public: consistent with the caller's observation and nothing in code contradicts it — stored
values carry no query string/signature/expiry, the API signs nothing on read
(`UserController.js:1516-1519`), and `getSignedUrl` does not appear on this path. **But the CDN/
bucket policy itself is UNKNOWN.** If they are world-readable, every transcript is retrievable by
anyone with the URL, which contains only two ObjectIds — a finding for the bucket owner.
Custom-S3 tenants are in customer AWS accounts; cross-account access **UNKNOWN**.

**(5) Coverage, conducted sessions last 90d** (`session_facts_v3.is_conducted` LEFT JOIN pointers):

| institute | region | conducted | transcript | chat |
|---|---|---|---|---|
| Eight Times Eight `64f1c3d0449bd300b9fe1208` | in | 13,212 | **11,594 = 87.8%** | 5,238 = 39.6% |
| ThinkTank Jr `69b84f3c99b41087144ba02e` | na | 6,056 | **5,540 = 91.5%** | 929 = 15.3% |

Transcript coverage is comparable across regions (87.8 vs 91.5); a 2-institute sample cannot
separate regional from tenant effects. The chat gap (39.6 vs 15.3) is almost certainly behavioural —
a chat file exists only if someone chatted — not a pipeline defect. **Both institutes are 100% on
Wise-owned buckets**, so the custom-S3 problem does not affect either. The missing ~9–12%: cause
**UNKNOWN** (recording disabled / session too short / transcription failed / worker never ran — none
tested).

**(6) Chat.** Same bucket/prefix, `-chat-<sessionIndex>.<partIndex>.txt`. NA 100% Wise-owned (5,659
files); IN 76,388 of 85,436 Wise-owned (89.4%), 9,048 (10.6%) custom — a much smaller custom share
than transcripts. Table `lake_cdc.wise_app_backend__rawchat`, identical shape and extraction.
Retention, access: identical to transcripts. **Guard:** `UserController.js:1516` reads
`rawChat?.chats || rawChat?.files` — a legacy `chats` field is checked *before* `files`. The model
declares only `files`, so `chats` is presumably vestigial, but whether any lake doc carries it is
**UNKNOWN** and worth one query before building on `$.files` alone.

**Confidence: high** on both tables' existence/shape/freshness/counts, the URL patterns and custom-S3
split (100% of files pattern-matched, no residue), the absence of TTL on both models (read against
`RawRecording`'s TTL as a control), the API returning `files` verbatim unsigned, the bucket name and
credential names, and the coverage percentages (full 90-day conducted set, not sampled).
**Medium** on full backfillability: I verified **pointers, not objects**, and `ingested_at` is CDC
arrival time, not file age. **Low/UNKNOWN** (flagged, not reasoned out): NA bucket name; any
`upload_files/` lifecycle rule; whether the CDN truly allows unauthenticated GET; whether wise-1 has
an AWS credential; cross-account access to customer buckets; the cause of the missing 9–12%; and
whether any `RawChat` doc uses `chats`.

**Check next:** (1) `curl -I` the **oldest** transcript pointer you can find — one request settles
backfillability, the only thing my medium confidence rests on; (2)
`aws s3api get-bucket-lifecycle-configuration --bucket wise-app-s3-bucket`; (3) test an
unauthenticated GET from outside any Wise network; (4) map `institute_id` → host in the lake before
scoping IN coverage; (5) one query for `$.chats` presence; (6) read pointers from the lake, not the
API — two bucket-pruned queries return every URL for a tenant, identical to the API's values.

## Evidence

backend-api (read-only):
- `src/models/RawSessionTranscript.js` — collection `RawSessionTranscript`, indexes
  `[{sessionId:1},{unique:true}]` only; `files: [{url, partIndex, sessionIndex, meetingUUID, file}]`.
- `src/models/RawChat.js` — collection `RawChat`, `sessionId` unique, same `files` shape, no TTL.
- `src/models/RawRecording.js` — control: `[{expiresIn:1},{expireAfterSeconds:0}]`.
- `src/models/DeletedFile.js` — `[{deletedAt:1},{expireAfterSeconds:2592000}]`, entityType enum
  includes `SESSION`.
- `src/controllers/UserController.js:1490-1491,1506-1519` — `RawChat.findOne`/
  `RawSessionTranscript.findOne` gated on `showSessionFiles`; `session.rawChats = rawChat?.chats ||
  rawChat?.files || []`; `session.rawTranscript = rawTranscript?.files || []`.
- `src/workers/fileDeletionWorker.js:12` — strips `https://wise-app-s3-bucket.s3.ap-south-1.amazonaws.com/`
  and `https://files.wiseapp.live/` interchangeably ⇒ bucket ↔ CDN mapping.
- `src/services/fileDeletionService.js:54` — `validateDBFilesPath`, the guard I previously misread.
- `env.sample:7,8,12,13,15` — credential/config NAMES (values are placeholders, not reproduced).
- `grep getSignedUrl|signedUrl src/services/s3UploadService.js` → no matches on this path.

Athena (read-only), by query id:
- `092ccf75` — transcript table counts/freshness per region.
- `d01b4343` — NA transcript URL pattern, single pattern 51,903/51,903.
- `910dc803` — IN transcript + IN/NA chat host patterns (the custom-S3 split).
- `afedce60` — 90-day conducted coverage for both institutes.
- `1f8ea0a8` — per-institute host check: both 100% Wise-owned.

## Gotcha

The premise was right but for a reason worth stating precisely: **the Wise API is a pass-through
here.** `session.rawTranscript = rawTranscript?.files || []` does no signing, no rewriting, no
authorization-scoped URL minting. So anyone walking the API session-by-session to collect transcript
URLs is paying N round trips to read a value that two bucket-pruned lake queries return in full. The
general lesson: before building an API-walking collector, check whether the collection is landed in
`lake_cdc` — `RawSessionTranscript` and `RawChat` both are, and neither is obvious from the ghl-style
table names.

Second, the trap that would have bitten a derivation approach: the key is
`<sessionOID>-transcript-<sessionIndex>.<partIndex>.vtt` — **two** numbers, not one, and the path
carries the **owner** ObjectId which cannot be derived from the session id. Worse, 34.2% of IN files
are not on a Wise host at all. A rule inferred from a handful of observed NA URLs would look correct,
validate cleanly against NA, and silently fail for a third of IN.

Third, a correction to my own earlier answer: `fileDeletionService.js:54` is a deletion-input guard,
not a protected-prefix list. I had read it as the latter in ask `8d661222`. The retention conclusion
survives — transcripts genuinely have no TTL — but it rests on the models, not on that line.
