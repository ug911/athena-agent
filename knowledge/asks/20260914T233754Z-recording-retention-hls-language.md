# Raw-recording retention, HLS retention + key-server auth, and whether a class has a language field

- **id:** 8d661222-8389-4af6-b5ce-e399e1d7a920   **from:** wise-sessions-quality   **depth:** 0   **utc:** 20260914T233754Z

## Question

(1) Retention/lifecycle rule for raw session recordings under `files.wiseapp.live/ephemeral_raw_recordings/`
and `na-files.wiseapp.live/ephemeral_raw_recordings/`? Caller observes MP4s 404ing after ~2 days on
prod and ~3 days on NA. Is that an S3 lifecycle rule, per-region, per-tenant/plan, and what is the
exact number of days? (2) How long is the encrypted HLS under `streaming_videos/.../video.m3u8`
retained, and can the `hls_keys` key server be used with an institute owner's bearer token to play it
server-side? (3) Does a Wise class or session have a language/medium-of-instruction field, and what
controls Zoom transcription language — fixed to English per institute?

## Answer

**(1) It is a Mongo TTL, not (only) an S3 lifecycle rule — and it is per-TENANT, not per-region.**

`src/workers/videoConversionWorker.js:52,93-94`:
```js
const folderPrefix = keepRawRecordings ? 'raw_recordings' : 'ephemeral_raw_recordings';
const expiresInBlob = keepRawRecordings ? {} : {
  expiresIn: customS3 ? moment.utc().add(3, 'month') : moment.utc().add(1, 'day')
}; // DO NOT CHANGE duration for customS3 else empty sessions will get deleted
await RawRecording.updateOne({ sessionId }, { $push: { recordings }, ...expiresInBlob }, { upsert: true });
```
`src/models/RawRecording.js` carries the TTL index `[{ expiresIn: 1 }, { expireAfterSeconds: 0 }]`.

| case | expiresIn | prefix |
|---|---|---|
| normal | **now + 1 day** | `ephemeral_raw_recordings/` |
| `customS3` | **now + 3 months** | `ephemeral_raw_recordings/` |
| `keepRawRecordings` | **not set — no expiry** | `raw_recordings/` |

Both switches are tenant/plan-level; nothing in this path branches on IN vs NA.

**Could not confirm in budget:** whether the S3 *objects* are reaped off that TTL/`DeletedFile` or by
a real bucket lifecycle rule on the prefix. The 2-vs-3-day observation is most likely a lifecycle
rule: S3 expiration evaluates once daily at UTC midnight, which turns a nominal 1 day into an
observed 2–3 and can differ by a day between buckets purely from creation time relative to midnight.
**Consistent with 1 day nominal in both regions** — do not conclude NA is configured differently
without `aws s3api get-bucket-lifecycle-configuration` on both buckets.
Practical: treat raw MP4s as available ~24h post-session, not guaranteed beyond.

**(2) HLS is retained (not ephemeral). The key server accepts a bearer token — with three traps.**

`src/services/fileDeletionService.js:54` treats `streaming_videos` as a protected prefix (with
`upload_files`, `embedded_content`, `session_recordings`, `raw_recordings`), so HLS persists until
explicit deletion — no TTL analogous to the raw path. It is the durable copy.

`src/routes/keyServerRouter.js` accepts the token via `authorization`, `x-wise-token`, `?t=` or
`?token=` (query params exist because HLS players cannot set headers on key requests).

- **Trap 1 — unauthorized does NOT 401, it returns a decoy key.**
  `KeyServerController.getHLSKey`: `if (!authorized) resourceId = resourceId.slice(0, -6) + "c6952e";`
  → HTTP 200 with a wrong key. Playback fails silently with no HTTP error. A successful-looking key
  fetch proves nothing. Outside production the reason is exposed in the `X-Wise-Key-Error` header
  (`VALID` on success) — use staging to debug.
- **Trap 2 — the key is encrypted unless the client is mobile.**
  `shouldEncrypt = req.headers['x-wise-vet'] == '1' || !['ANDROID','IOS'].includes(context.platform)`.
  A server-side consumer gets an encrypted blob: AES-128-CBC with `sha256(nonce)` giving IV
  (bytes 0–16) and key-encryption key (bytes 16–32), IV prepended to the ciphertext.
- **Trap 3 — a bare bearer token may not suffice.** `authorizeRequest` also reads `securityToken`
  (`?st`/`x-wise-vst`), `timeToken` (`?tt`/`x-wise-vtt`) and a namespace (`req.missingNSHeader →
  'MISSING'`). Ran out of budget before establishing which are mandatory.

**(3) No language / medium-of-instruction field exists anywhere relevant.**
- `src/models/Classroom.js` — `grep -n "language"` → **no matches**.
- `src/models/Institute.js` `localeSettings` (194/330) is only
  `{ timeFormat: '12h'|'24h', calendarStartDay: 'MONDAY'|... }` — **no language**.
- `grep -rn "transcription_language|audio_transcription|transcript.*language" src/` → **no matches**.

So transcription language is **not configurable per institute or session from backend-api**; it is
the meeting vendor's default (English in practice, since nothing overrides it). The Zoom
account-level setting is console config, not visible from this repo.
The only adjacent field is a *user* preference, `user.config.languagePreference` (source of the
`processed.user.config_lang` column) — not a class attribute, and **unusable from the warehouse
anyway: the whole `config` column is NULL across `processed` and raw `backend`, 0 of 3,818,378 rows**
(see [[20260910T233546Z-host-backfill-review]]). Medium-of-instruction would need a backend-api
schema addition; CDC picks it up automatically once written.

**Confidence: high** on the TTL mechanism and durations, the tenant-not-region branching,
`streaming_videos` being protected/non-ephemeral, the token-acceptance paths, the decoy-key and
encryption behaviours, and all three language negatives (direct reads and greps over the
authoritative models). **Low on the exact days in (1)** — I established the app-level TTL is 1 day
and not region-branched but could not confirm an S3 lifecycle rule, which is what the 2-vs-3-day gap
most likely reflects; I did not invent a number. **Low on (2)'s authorization policy** — transport
confirmed, policy not. **Caveat:** working tree read, not the deployed commit; NA build parity
unverified.

**Check next:** (1) `aws s3api get-bucket-lifecycle-configuration` on both buckets — one command
each, settles (1); (2) finish `authorizeRequest` (KeyServerController ~line 56) for whether st/tt/
namespace are mandatory; (3) test the key server on staging and read `X-Wise-Key-Error` before
building server-side playback; (4) trace `DeletedFile`/`fileDeletionService` for who deletes the S3
objects; (5) check the Zoom console transcription-language setting for both IN and NA accounts.

## Evidence

backend-api (`~/Documents/wise/backend-api`, read-only):
- `src/workers/videoConversionWorker.js:52` folder prefix switch; `:93-94` expiresIn 1 day /
  3 months + the in-code warning; `:108,124` `streaming_videos/${userId}` HLS output;
  `:221,224,253` `HLS_KEYS_HOST/hls_keys/${keyId}`.
- `src/models/RawRecording.js` — TTL index `[{expiresIn:1},{expireAfterSeconds:0}]`, collection
  `RawRecording`.
- `src/routes/keyServerRouter.js` — token accepted via authorization / x-wise-token / ?t / ?token.
- `src/controllers/KeyServerController.js:16-56` — decoy resourceId on `!authorized`, dummy on
  `partId==1`, `shouldEncrypt` rule, `encryptKey` (sha256(nonce) → IV + KEK), `X-Wise-Key-Error`
  set only outside production; `authorizeRequest` reads t/token/x-wise-token + st/vst + tt/vtt +
  namespace.
- `src/services/fileDeletionService.js:54` — protected prefixes incl. `streaming_videos`.
- `src/services/s3UploadService.js:132` — `streaming_videos/.../video.m3u8` path pattern.
- `src/models/Institute.js:194-197,330` — `localeSettingsSchema` = timeFormat + calendarStartDay only.
- Greps returning **no matches**: `language` in `src/models/Classroom.js`;
  `transcription_language|audio_transcription|transcript.*language` across `src/`.

Prior knowledge reused: `processed.user.config` is 100% NULL (from the host-backfill ask), so
`config_lang` is unusable.

## Gotcha

Two of these are silent-failure designs, which is the pattern worth carrying forward:

**The HLS key server answers an unauthorized request with HTTP 200 and a deliberately wrong key**
rather than a 401. That is intentional (it denies an attacker the signal that the token was wrong),
but it means a legitimate integrator debugging server-side playback gets no diagnostic at all — the
fetch succeeds, the stream just will not decrypt. The `X-Wise-Key-Error` header exists for exactly
this and is suppressed on production, so debugging must happen on staging.

**And "ephemeral" retention is enforced in two different places that nobody should assume are the
same number.** The application sets a 1-day Mongo TTL on the pointer document; the bucket very
likely has its own lifecycle rule on the object. Reading only the code gives you "1 day" and reading
only the bucket gives you the lifecycle number, and the observed behaviour is the *later* of the two
plus S3's once-daily-at-UTC-midnight evaluation. That is how a nominal 1 day is observed as 2 days in
one region and 3 in another without anything being configured differently.
