# Review the host-backfill query for correctness — which namespaces hosted on IN/NA would it silently miss?

- **id:** 935e61a2-6f27-4e46-b5dd-0f01b9fa446e   **from:** ghl-registry   **depth:** 0   **utc:** 20260910T233546Z

## Question

Review the host-backfill query in wise-ghl-client-registry/sync_registry.py
(`load_host_lookup()`, re-keying `?/<ns>` to `<region>/<ns>` in step 6 of `merge()`).

Verbatim SQL, run once per region over `("IN","processed")` and `("NA","processed_na")`:

```sql
SELECT DISTINCT namespace FROM (
  SELECT namespace        FROM {db}.institute WHERE namespace        IN ({lst})
  UNION ALL SELECT namespace        FROM {db}.user WHERE namespace        IN ({lst})
  UNION ALL SELECT config_namespace FROM {db}.user WHERE config_namespace IN ({lst})
)
```

Is it right, and what would it silently get wrong? Caller cares most about FALSE NEGATIVES —
a namespace that IS hosted on IN or NA but the query fails to find (wrong tables/columns, case
or whitespace differences, stale processed snapshots vs lake_cdc, namespaces stored only on
institute_public_profile or elsewhere, deleted/renamed institutes) — which would leave a client
wrongly marked host-unknown. Also: is processed vs processed_na the correct IN/NA split, and can
any namespace legitimately exist in both?

Caller's observed run (2026-09-11): 23 resolved, 0 found in both regions, 6 found in neither
(integraleducation, lgleducationlimited, skillpete-educational, shambhala-edutech, tstp,
whitelabel). Caller's unchecked assumptions: the three columns are the right ones and are exact
case-sensitive untrimmed matches; processed/processed_na are current; absence ⇒ does not exist.

## Answer

Returns nothing wrong (no false positives) but is much weaker than assumed, and has confirmed
false negatives. **The caller's premise "absent from all three columns in both DBs ⇒ does not
exist" is wrong.**

**The three-column defence is really one column.**
- `user.config_namespace` is **0 non-null out of 3,818,378** in IN. The view derives it from
  `config`, and `config` is NULL for every row in `processed` AND in raw `backend` — the Mongo
  flattener never carries it. That UNION arm can never match. (Bonus latent bug: the view uses
  `CAST(json_extract(...) AS varchar)`, which would return the value *with JSON quotes*; it
  should be `json_extract_scalar`. Moot while `config` is NULL, breaks on any backfill.)
- `institute.namespace` contributes **0** namespaces not already in `user.namespace` (2,687 rows
  vs 10,500 distinct user namespaces — strict subset).
- So the query == `SELECT DISTINCT namespace FROM {db}.user`, paying for two extra scans.

**4 of the 6 "found in neither" ARE hosted:**

| Looked up | Actually stored as | Region | Users |
|---|---|---|---|
| `shambhala-edutech` | `shambhala` | IN | **324** (updated 2026-09-09, live) |
| `skillpete-educational` | `skillpete-educational-se` | IN | 9 |
| `integraleducation` | `integral` | NA | 4 |
| `whitelabel` | `whitelabel-institute`, `besser-whitelabel` | IN | 1, 4 (likely generic) |
| `lgleducationlimited` | nothing anywhere | — | true negative |
| `tstp` | nothing anywhere | — | true negative |

**Root cause: namespace is a ~24-char TRUNCATED slug + optional `-NNNN` suffix**, not a case or
whitespace problem. Over 12,007 distinct namespaces: max length 30, **619 exactly 24 chars**,
51 over 24, 516 with a 4-digit suffix, **0 untrimmed, 0 containing uppercase**. Smoking guns:
`note-garden-school-of-mu` (from "…school-of-music"), `sonajapan-japanese-langu-6179`
("language"), `skillpete-educational-se` (exactly 24). Exact `=` against a hand-typed name
cannot survive this. Hyphenation is also unstable: `super-sheldon` and `supersheldon` coexist.
Case/whitespace is a non-issue warehouse-side, but normalise the *probe* side anyway.

**processed / processed_na IS the correct IN/NA split** — confirmed by `lake_cdc`'s `region`
partition (`in`/`na`) and by volume (IN 3.82M users, NA 93,947). But it is stale: **11
namespaces exist in `lake_cdc` and not in `processed`** (IN 8, NA 3), all last written
2026-09-10 — i.e. created after the daily dump. New tenants are exactly what a sales/Slack
registry asks about, and the per-calendar-day negative cache keeps them unknown until tomorrow.

**`lake_cdc.wise_app_backend__user` is the better source.** Iceberg,
`PARTITIONED BY (region)` with values `in`/`na`, columns `_id, region, doc, op, ts, ingested_at`,
namespace at `$.namespace` in `doc`. One query covers both regions and returns region as a
column; fresh to 2026-09-10 23:20/23:26; superset (+1,399 IN, +106 NA rows). `op` is
`seed`/`insert`/`update` with **no `delete`** — so Mongo-deleted docs persist in CDC but vanish
from the daily full dump, which answers the deleted/renamed-institute worry directly. Costs
~800MB scanned because `doc` is wide; fine once daily, not per-namespace.

**Yes, a namespace can legitimately exist in both regions — 27 do**, and the "IN wins" tie-break
is wrong for several: `jhmi` is 51 IN / **206 NA**; `institute` 1 IN / 51 NA; `online` 1/9;
`linkedin` 1/6. The set is two genuinely dual tenants (`jhmi`, `vmotiv8` 403/7), the shared
`wise` (2,445,641/1,700) and `wise-demo` (37,685/8,581) internal tenants, and a tail of 1–5-user
cross-region signup leakage. Tie-break on user count + last-write recency, and blocklist
`wise`/`wise-demo` from host inference. "0 found in both" is plausible for a 29-namespace
sample, not evidence the mechanism is absent.

**`institute_public_profile` adds 0 novel namespaces** (1,643 rows) — that hypothesis is
disproved, no need to add it. Its `subdomain` is an ObjectId, not a vanity slug, so useless as a
lookup key.

**Bigger modelling problem flagged: a namespace is not a client.** One client owns many
namespaces (each signup mints a fresh `-NNNN`): `corizo` 19, `llri` 14, `super-sheldon` 13
(+8 as `supersheldon`), `lanstitut` 10 — so `<region>/<namespace>` fragments them. Conversely
many distinct real customers share `namespace='wise'` ("Rick Classes", "DIGITAL BUSINESS
ACADEMY", "The Good Harvest School", "SIP Abacus Kasavanahalli") — self-serve signups have no
namespace of their own, so no namespace lookup can ever resolve their host.

Recommended replacement: single `lake_cdc` query grouping by region + namespace + normalised
stem (`regexp_replace(regexp_replace(lower(ns),'-[0-9]{2,5}$',''),'[^a-z0-9]','')`) with users
and `max(ingested_at)`; exact match first, then 24-char stem-prefix fallback **behind a generic
stem blocklist** — measured collision offenders: `student` (39 variants), empty (24), `corizo`
(19), `abc` (17), `llri` (14), `na` (11), `a` (8), `none` (7), plus `wise`, `wise-demo`,
`institute`, `school`, `learner`, `test`.

**Confidence: high** on all mechanical findings (measured, not reasoned). **Medium** on two:
the truncation constant being exactly 24 is inferred from the length distribution rather than
read from code; and the `whitelabel` attribution looks generic/internal, don't auto-resolve it.
Row counts are as of the 2026-09-11 warehouse state.

**Check next:** (1) confirm the truncation rule in backend-api code, not data —
`grep -rn "namespace" --include=*.ts | grep -i "slug\|substring\|slice\|24\|truncate"`;
(2) re-run all 199 unknowns against the `lake_cdc` query with stem fallback + blocklist;
(3) re-key the 27 dual-region namespaces by users + recency and diff vs "IN wins" (`jhmi` is
mis-keyed today); (4) decide policy for the 170 name-only records and the `wise`-namespace
clients — namespace lookup structurally cannot help them, mark "host-unresolvable" not
"host-unknown"; (5) split the cache by outcome so negatives retry sooner than a calendar day.

## Evidence

Files read:
- `schemas/processed/processed/user.md` — view DDL: `config_namespace` =
  `CAST(json_extract(config,'$["namespace"]') AS varchar)`; base `wise_app_backend__user`.
- `schemas/processed/processed/institute.md` — view DDL; human note "Multiple institutes per
  namespace" (`leadiasacademy` → 6 institutes).
- `schemas/INDEX.md:31,59` — `processed.institute` and `processed.user` are **views**, IN+NA identical.
- `semantics/glossary.md:20-21`, `semantics/joins.md:13` — namespace = tenant key, spans institutes.
- `knowledge/COMPACT.md` — IN=`processed`, NA=`processed_na`; no prior asks (`knowledge/asks/` empty but for `.gitkeep`).

Athena queries (via `athena` MCP, read-only):
- `count(*), count(config_namespace), count(namespace), count(DISTINCT namespace)` on
  `processed.user` → 3818378 / **0** / 3818378 / 10500. (query 7140215a)
- `count(config)` on `processed.wise_app_backend__user` → 0; on `backend.wise_app_backend__user`
  → 0 of 3818378 (714MB scanned). (ee7bfecf, d3e2a6cc)
- `information_schema.columns` on `backend.wise_app_backend__user` LIKE %config%/%namespace% →
  only `config`, `namespace`, `premiumconfig`. (b87a53be)
- Fuzzy `regexp_replace(lower(ns),'[^a-z0-9]','')` match of the 6 across
  institute+user × IN+NA → **0 rows**. (3212977c)
- `regexp_like(lower(ns),'integral|lgl|skillpete|shambhala|tstp|whitelabel')` across the same 4
  relations → `besser-whitelabel` IN, `integral` NA, `shambhala` IN, `skillpete-educational-se`
  IN, `whitelabel-institute` IN. (8bec8652)
- Per-source row counts for those → all from `*.user`, none from `*.institute`;
  `shambhala` 324 IN, `skillpete-educational-se` 9 IN, `integral` 4 NA. (eb7e086f)
- Same 6 against institute `name` / `institute_public_profile.title` in both regions → 0 rows.
  (6e36620d, afaa1d07)
- Set arithmetic: IN 10500 ns, NA 1534 ns, **27 in both**, institute-not-in-user **0**. (6b1558e8)
- The 27 dual namespaces with per-region user counts. (04a12fcf)
- `institute_public_profile`: 1643 ns, **0** not in user, subdomain differs in 1643/1643;
  sample shows subdomain = ObjectId, and many real customers under `namespace='wise'`.
  (3f7da1d7, 004f0457)
- `list_databases()` → includes `lake_cdc`, `cdc_raw`, `control_map`, `backend_paper`,
  `processed_paper`. `control_map` holds only date/inactive-teacher maps — not a region map.
- `describe_table(lake_cdc, wise_app_backend__user)` → Iceberg,
  `PARTITIONED BY (region)`, cols `_id, region, doc, op, ts, ingested_at`,
  `s3://wise-atlas-data-lake/cdc/iceberg/lake_cdc/wise_app_backend__user`.
- `lake_cdc` per-region counts/freshness → in 3819777 rows, latest `2026-09-10 23:20:01`;
  na 94053, latest `2026-09-10 23:26:08`; earliest 2026-06-11; 3 distinct `op`
  (`seed`/`insert`/`update`, no `delete`). (66d87075, 43cac104)
- lake_cdc-minus-processed namespace diff → IN 8, NA 3; all 11 last written 2026-09-10
  (`tutoring-3594`, `sonajapan-japanese-langu-6179`, `ravi-sir-palwal`,
  `note-garden-school-of-mu`, `impetus-learning-7634`, …). (bfc3535a, d5a4f76b)
- Length/shape stats over 12007 distinct ns → max 30, **619 exactly 24**, 51 >24, 516 with
  `-[0-9]{4}$`, **0 untrimmed, 0 uppercase**. (62407db0)
- Stem-collision census (`regexp_replace(ns,'-[0-9]{2,5}$','')`) → `student` 39, empty 24,
  `corizo` 19, `abc` 17, `llri` 14, `super-sheldon` 13, `na` 11, `lanstitut` 10, `learner` 8,
  `a` 8, `supersheldon` 8, `none` 7. (654a9162)

## Gotcha

Three things that are each individually enough to produce a wrongly "host-unknown" client:

1. **`user.config_namespace` is *always* NULL — 0/3,818,378 — because the source `config` column is NULL
   in processed AND raw.** A UNION arm that has never matched anything since the view was
   written. It reads as redundancy and is actually nothing. Same for
   `institute.namespace`, which is a strict subset of `user.namespace` (0 novel values).
   A query that looks like it triangulates across three columns queries exactly one.
2. **`namespace` is a ~24-char truncated slug, sometimes plus `-NNNN`.** `skillpete-educational`
   is stored as `skillpete-educational-se` — 24 chars exactly. `note-garden-school-of-mu` lost
   "sic". No amount of case-folding or trimming finds these; only stem/prefix matching does. And
   the warehouse itself is perfectly clean on case and whitespace (0/12,007), so the obvious
   hypothesis is the wrong one.
3. **The `-NNNN` suffix is not tenant identity — it is per-signup.** `corizo` is 19 namespaces,
   `super-sheldon` 13. So loosening to stem matching without a generic-stem blocklist
   (`student` alone has 39 variants; 24 namespaces are bare `-NNNN` with an empty stem) trades
   today's false negatives for tomorrow's false positives.

Plus: `wise` and `wise-demo` are shared internal tenants living in **both** regions with
millions of rows — any host-inference rule keyed on namespace must exclude them explicitly, or
every self-serve client under `namespace='wise'` resolves to "hosted in IN" for free and wrongly.
