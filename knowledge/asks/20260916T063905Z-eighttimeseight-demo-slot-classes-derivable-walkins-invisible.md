# Reconcile 3 vs 13,728 demo sessions for eighttimeseight; are demo sessions derivable?

- **id:** 2cc2b387-4038-4a6c-ba0b-5994bb8c38aa   **from:** executor   **depth:** 0   **utc:** 20260916T063905Z

## Question

Follow-up to your two eighttimeseight answers today (asks 176ab9cb and c3124cec), one narrow question, institute_id 64f1c3d0449bd300b9fe1208, IN. Your second answer found 28 LIVE classes with demo/trial in the CLASS NAME, 13,728 sessions in the daily dump. Your first answer found only 3 demo sessions, by session TITLE, inside the 730-day session_facts_v3 window. Resolve the two: (a) of those 28 demo-named LIVE classes, how many sessions sit inside the session_facts_v3 window, how many are ENDED/conducted, and how many have at least one student with attend_minutes > 0; (b) what are the 28 class names and their date ranges, so we can see if they are a tenant convention or one old batch; (c) check class.metadata.tags and zoom.metadata.tags on those classes for any demo-like tag. Use session_facts_v3.course_name only, no raw zoom scan. A published plan currently states demo sessions are NOT derivable from data; your answer decides whether that is corrected.

## Answer

Institute `64f1c3d0449bd300b9fe1208`, IN. All numbers below from `lake_cdc.session_facts_v3` / `session_participant_facts_v3` (institute-pruned) plus the daily `processed.wise_app_backend__zoom` and the region-pruned raw `__class` table for tags. No raw zoom scan.

## Verdict up front

**The published plan is wrong and should be corrected: demo sessions ARE derivable from data for this tenant.** The rule is `session_facts_v3.course_type = 'LIVE' AND lower(course_name) LIKE '%demo%'`. It matches a deliberate tenant convention ("Demo Slot N", 28 classes built in five batches from Feb 2024 to Mar 2026, 26 still active, 12,610 sessions in the fact window, 1,635 since 1 Aug 2026), not one old batch. There is no tag; the name is the marker.

The earlier "3" was a **title** match, the "13,728" a **class-name** match. Demo Slot sessions carry generic titles, so title matching finds nothing. The two answers were both right about what they measured and only one of them measured the right thing.

**Second correction, the one that matters for quality scoring:** the demo attendees are **invisible to `session_participant_facts_v3`**. Of 12,610 conducted Demo Slot sessions, **0** have any student with `attend_minutes > 0` — yet the daily dump shows 5,447 ENDED sessions with a non-teacher Zoom participant who stayed > 0 s, and Wise's own `participant_count` is > 0 on 12,504 sessions (22,827 total). Those attendees have **no `wiseUserId`**: they are walk-in Zoom joiners (a prospect joining by link, display name not matching any enrolled student), and the fact builder drops every participant row where `wiseUserId IS NULL` (`facts_v3.py:249`). Each Demo Slot class has at most one enrolled student (`max_enrolled_per_class = 1`) and that student never attended (0 matched rows, present or absent, across 13,484 ENDED sessions). So: **demo sessions are derivable; demo *attendance* is not, from the facts.** Any per-student demo score must come from the raw `participants[]` (name + user_email + duration, no user id) or from a fact change.

## (a) Sessions inside the fact window

| measure | value | query |
|---|---|---|
| Demo-named LIVE classes in `session_facts_v3` (730-day window) | **26** | `ffa4b56a` |
| Sessions | **12,610** | `c34ff631` |
| `status = 'ENDED'` | 12,552 | `ffa4b56a` (sum) |
| `is_conducted` | 12,552 | same |
| Sessions with ≥1 student `attend_minutes > 0` in the participant fact | **0** | `ffa4b56a` |
| Sessions with `participant_count > 0` (Wise's own present-count) | 12,504 (Σ 22,827) | `c34ff631` |
| Sessions since 2026-08-01 | 1,635 | `c34ff631` |
| Distinct teachers hosting | 106 | `c34ff631` |
| Median duration | 22 min | `c34ff631` |
| Future-dated | 2 | `ffa4b56a` |

Daily dump, same 26 classes (`0e425493`, `be43476c`): 13,751 sessions total (13,735 ENDED — the extra ~1,100 are older than 730 days, which is the whole gap between "13,728" and "12,610"); 13,484 ENDED sessions with a non-empty `participants[]`; **6,271 non-teacher rows with no `wiseuserid` and duration > 0 across 5,447 sessions**; 0 non-teacher rows *with* a `wiseuserid`; 0 `offline:true` rows. Roughly 40% of demo sessions had a real prospect stay in the room; the rest were teacher-only (no-show) — that split is itself a quality signal the plan can use.

## (b) The 28 class names and date ranges — a convention, built in batches

| batch (created) | classes | session range in fact | sessions |
|---|---|---|---|
| 2024-02-28 | Demo-Slot 1–5 | 2024-09-14 → 2026-09-07 (Slots 4, 5 stop 2025-09) | 3,527 |
| 2025-09-02 | Demo Slot-6, -7, -8, -9, -10 | 2025-09-03 → 2026-09-16 (Slot-7 has 5 sessions, one day) | 2,226 |
| 2025-09-15 | Demo Slot 11–15 | 2025-09-15 → 2026-09-15 | 3,035 |
| 2025-10-22 | Demo Slot 16–20 | 2025-10-23 → 2026-09-16 | 2,319 |
| 2026-03-18 / 03-24 | Demo Slot 21–26 | 2026-03-19 → 2026-09-15 | 1,503 |
| archived (not in fact) | `demo Slot 23` (2026-03-18), `test demo slot` (2026-03-18) | — | 0 |

That is the 28: 26 active + 2 archived LIVE classes. Five batches over 25 months, new slots added as capacity grew, most still running this week. Also present but **not** demo-slot classes: `Ind Trial Class` (ONE_TO_ONE, 2025-02, the "1 ONE_TO_ONE class" from ask c3124cec), and four `classType = DEMO` rooms (`Chess demo`, `Demos` ×2, `demo`; three archived) — the demo-product rooms whose bookings land in PERSONAL classes and never run (ask 176ab9cb).

Full per-class table (class_id, sessions, ended, first/last date) is in query `ffa4b56a`; class ids for the 26 are listed in the Evidence section of the knowledge file.

## (c) Tags — none

- `class.metadata.tags` on all 28 (and the DEMO rooms): `[]` or absent. Query `ef3fd9ea` on `lake_cdc.wise_app_backend__class`, `region='in'`, institute-scoped (the daily `processed.wise_app_backend__class` has no `metadata` column at all).
- `zoom.metadata.tags` on all 13,751 sessions of those classes: **NULL on every row** (`ed082ab3`).
- `settings.maxAllowedParticipants`: unset on all.

Nothing beats the name. Do not wait for a tag.

## Recommended rule for the plan

```sql
-- demo session (this tenant)
course_type = 'LIVE' AND lower(course_name) LIKE '%demo%'      -- 26 classes; add '%trial%' only if you want the 1:1 "Ind Trial Class"
-- demo had a prospect in the room: NOT available from facts; needs participants[] rows with
--   isTeacher <> true AND wiseUserId IS NULL AND duration > 0   (daily dump, bounded to these class ids)
-- exclude course_type = 'PERSONAL' (demo-product bookings, never conducted)
```
Make it institute-scoped: "Demo Slot" is this tenant's convention, not a platform one.

## Confidence

**High** on (a), (b), (c): every number is a direct institute-pruned fact query or a bounded daily-dump query, and the class list comes from the raw class table with ids matching the fact. **High** that the fact hides demo attendees — it is a literal `WHERE wiseUserId IS NOT NULL` in `facts_v3.py` and the daily dump shows 6,271 such rows. **Medium** that the no-`wiseUserId` participants are prospects rather than staff on second devices — inferred from the business shape (one slot class, many teachers, one-off joiners), not from an identity field.

## What I would check next

1. Fact request: `session_participant_facts_v3` should keep unmatched participant rows (student_id NULL, `is_walkin = true`, name/email/duration) or `session_facts_v3` should carry `walkin_count` and `walkin_minutes`. That single change makes demo attendance and "prospect stayed ≥ N minutes" queryable per session.
2. Sample 20 Demo Slot sessions' `participants[].name/user_email` against `registrationformsubmission` for the tenant to confirm walk-ins are the booked prospects (identity check for the medium-confidence point).
3. Re-check the two non-ENDED Demo Slot sessions per class (MISSED/UPCOMING residue) — trivial, but it decides whether "conducted" needs a `status` filter in the plan.

## Evidence

Athena, read-only, all institute-scoped to `64f1c3d0449bd300b9fe1208`:
- `ffa4b56a` — per-class: session_facts_v3 (course_type LIVE, course_name LIKE demo/trial) × participant fact attendees (attend_minutes>0). 26 classes, 12,610 sessions, 0 with attendance.
- `c34ff631` — totals: participant_count>0 on 12,504, Σ 22,827; 106 teachers; median 22 min; max enrolled per class 1; ever_attended 0; 1,635 since Aug.
- `0e425493` — daily zoom for the 26 class ids: 13,751 sessions, 13,735 ENDED, 267 empty participants, 9,936 with ≥2 rows.
- `be43476c` — UNNEST participants on ENDED sessions: 6,271 non-teacher no-wiseuserid rows dur>0 across 5,447 sessions; 0 matched student rows; 0 offline rows. (1.39 GB — the daily zoom CTAS is unpartitioned, any query scans it.)
- `ed082ab3` — zoom.metadata.tags on those sessions: NULL ×13,751.
- `ef3fd9ea` — lake_cdc.wise_app_backend__class region='in', institute match, name LIKE demo/trial: 33 rows = 26 active LIVE Demo Slot + 2 archived LIVE + 4 DEMO rooms + 1 ONE_TO_ONE "Ind Trial Class"; metadata.tags [] / absent everywhere. Ran 120–240 s; needs `timeout_s` ≥ 180.
- `fda19bd6`, `84a4db51` — failed attempts (no `classtype`/`metadata` in daily class table; `CAST(json '[]' AS varchar)` fails — use `json_format`).

Source: `wise-analytics-portal/marts/wise_marts/facts_v3.py:249` — `WHERE oid(wiseUserId) IS NOT NULL` in the `attend` CTE.

Demo Slot class ids (26 active): 65def6963ceb88cced120541, 65def6b0c77dbd3eb83af846, 65def6c625999561b91d63d6, 65def6decd1cfb56e876bf87, 65def6f43ceb88a1ee1207dd, 68b68b1f5f859d0b0cefe24e, 68b68b3dfe84616230066400, 68b68b5b744918c346c3c839, 68b68b7353d620e605d2329a, 68b68b8a744918c346c3cd49, 68c7ba24c31a2334f8b8e0f4, 68c7ba31da6366e0b1609bb8, 68c7ba3e80aae7ba02b74192, 68c7ba4b8cb4472322ee3c50, 68c7ba5980aae7ba02b749ac, 68f87ac1411f9dea7f206924, 68f87ad11ea2041703054d97, 68f87adfdb511ee8487d54eb, 68f87aeed352fb076ad989a0, 68f87afd8fce5f65e574b1de, 69ba40c6c009caefeefad9b9, 69ba40e41b82ec6415c7902e, 69ba41121b82ec6415c79a17, 69ba412325b06aaceaabd036, 69c23b84a5f5242b9aafc5b5, 69c23ba6111d4942353dd19d. Archived: 69ba40f81b82ec6415c79551, 69ba3f8925b06aaceaab629b.

## Gotcha

1. **Title vs class name.** Demo Slot sessions have generic titles; only `course_name` identifies them. A title heuristic returns ~0 and looks like "no demos exist".
2. **The participant fact cannot see walk-ins.** `facts_v3.py:249` drops every participant without `wiseUserId`. For any class whose attendees are prospects joining by link, `session_participant_facts_v3` reports zero attendance while `session_facts_v3.participant_count` is positive. Check `participant_count` before concluding nobody came.
3. `processed.wise_app_backend__class` (daily) has **no `metadata` and no `classtype` column**; tags and classType need the raw `__class` table (region-pruned, ~370 MB, 2–4 min) or the fact's `course_type`.
4. The daily `processed.wise_app_backend__zoom` is an unpartitioned CTAS: every query scans ~1.3 GB regardless of the class filter. Fine for one-offs; not for a scheduled job.
