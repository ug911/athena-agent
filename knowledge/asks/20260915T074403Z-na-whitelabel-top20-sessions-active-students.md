# NA whitelabel top-20 by conducted sessions, Aug vs 1–15 Sep 2026, with active students

Query: `examples/na-whitelabel-top20-sessions-active-students.sql`. Query id 29afe43b, 2.37 GB scanned
(the spf_v3 join carries no literal `institute_id`, so no bucket pruning — acceptable one-off).

## Verified this session
- **`is_conducted` = `meetingStatus IN ('ENDED','STARTED')`** — read from
  `wise-analytics-portal/marts/wise_marts/facts_v3.py:165`. Companion check NA Aug 1–Sep 15 2026:
  ENDED 18,354 (true) · CANCELLED 2,895 · UPCOMING 1,987 · MISSED 1,611 · IN_PROGRESS 6 (all false).
  STARTED never appears in this window. (query d61bf5fa)
- **`is_enrolled` source** (`facts_v3.py:262`): `classparticipant WHERE relation='STUDENT'`, **no status
  filter**. NA STUDENT rows: REMOVED 17,293 / ACCEPTED 15,981 / REQUESTED 2 (5b2dcc4e). Use
  `status='ACCEPTED'` from raw classparticipant for enrolment. No roster fact exists (still "fact needed").
- **Tenant key**: whitelabel namespace, via `processed_na.institute.namespace` (daily). `journey-school`
  spans two institutes (Journey School 69de64c2 + Journey School US 6a28f4cf) — merged as one tenant.
- **Demo clones**: eight NA institutes named "Bright Future Academy" created Sep 2026 with 10–12 sessions
  each, namespace `wise-demo` or NULL (not yet in the daily institute dump). Excluded. The real
  `brightfutureacademy` (6a3bdc66, custom host academy.brightfuture.es) is a genuine tenant — kept.
- `wise` NA hostnames: na-wl.wiseapp.live, na-web.wise.live, web.wiseapp.us. `wise-demo`: demo.us.wise.live.

## Definitions used
- Session = `is_conducted`. Sep window 1–15 inclusive, and 15 Sep is today (partial day, ~30 min fact lag).
- Active student (classroom-based, user's definition) = distinct ACCEPTED STUDENT in any class that held a
  conducted session in the month. Attendance-based = distinct `spf_v3.attended` student in the month.
- Attendance can exceed classroom count (thinktankjr Aug 352 vs 337): attendees since REMOVED from the class
  or attending without an ACCEPTED enrolment. Where classroom ≫ attendance (mathwave Sep 140 vs 25) a large
  class is enrolled but few attend.
- Excluded tenants: wise, wise-demo, make-up-testing, makeuptesting, acme (none of the last three had NA
  sessions in the window), plus NULL-namespace institutes.

## CORRECTION 2026-09-16 — the attendance-based column above is inflated
`spf_v3.attended` means "present in the session's `participants[]` list", which the app pre-populates
with enrolled students; it is NOT "showed up". Verified on eighttimeseight Aug 2026: `attended=true`
11,645 rows, of which only 2,734 have `attend_minutes > 0` (b8236e0b). Use `attend_minutes > 0`.
Recomputed for the 20 tenants (dd1823ee, run 16 Sep so Sep 1–15 now complete):

| tenant | Aug listed → real | Sep 1–15 listed → real |
|---|---|---|
| thinktankjr | 352 → 341 | 335 → 332 |
| takalam | 257 → 246 | 289 → 266 |
| journey-school | 230 → 212 | 228 → 201 |
| kyo-standard-test-prep | 315 → 295 | 260 → 227 |
| therapsy | 217 → **112** | 295 → **115** |
| my-private-professor | 110 → 99 | 106 → 94 |
| next-level-education | 152 → **63** | 117 → **58** |
| eliteedge-advisors | 79 → 76 | 64 → 62 |
| exploreapollotuition | 23 → 22 | 68 → 66 |
| dyscalculia-tutoring | 75 → 67 | 59 → 51 |
| pirates | 97 → **39** | 93 → **52** |
| smartwill | 348 → 295 | 371 → 299 |
| mathwave-education-acade | 11 → 4 | 25 → 11 |
| brightfutureacademy | 63 → 53 | 115 → 74 |
| english-in-the-us | 40 → 38 | 36 → 34 |
| bora-portuguese | 31 → 26 | 32 → 29 |
| nlenglishacademy | 159 → 152 | 158 → 145 |
| mathszx-1522 | 18 → 15 | 21 → 18 |
| afshar | 46 → 41 | 51 → 44 |
| sira | 5 → 3 | 4 → 3 |

Session counts and classroom-based counts are unaffected. The example SQL has been fixed.
