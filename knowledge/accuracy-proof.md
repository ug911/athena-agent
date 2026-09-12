# The accuracy proof — how we prove the ghl_sync optimisation changed nothing

Owner: **athena-agent** (data model + verification). Implementation: **airflow**.
Written 2026-09-12. Accuracy is the hard constraint; wall clock and cost are the optimisation.

---

## 0. The thing this document exists to prevent

A before/after diff **cannot catch a bug that is present in both before and after.**

That is not a hypothetical. Three measured examples from this warehouse, any one of which a
naive diff would wave through:

| Trap | What a pure diff sees | Truth |
|---|---|---|
| `json_extract_scalar(doc,'$.instituteId')` — wrong path for an `$oid`-wrapped field | before = `[]`, after = `[]` → **"no change, ship it"** | the dataset is empty and has always been empty |
| `metadata.installmentId` read as plain string only | before = after = 25,140 rows | **4,564 NA rows (15.4%) silently dropped** — they are `$oid`-wrapped |
| `amount` read as a scalar | before = after = all NULL | `amount` is `{"value":{"$numberInt":…},"currency":"…"}` — money never resolved at all |

So the proof has **two independent legs**. Leg A is relative and catches what we change.
Leg B is absolute and catches what was already wrong. **Shipping requires both.**

---

## Leg A — regression diff (relative)

Proves: *the optimisation changed no output.*

### A1. Capture
For each tenant in the matrix (§3), capture the **full desired-state payload** that
`build_desired()` produces, before any change. Capture the *payload*, not the SQL result —
we are proving the contract with GHL is unchanged, not that an intermediate query is unchanged.

Store as newline-delimited JSON, one object per contact, at
`proofs/<run_id>/<region>/<tenant>/desired.ndjson`, alongside a `manifest.json` recording
git SHA, capture start/end UTC, the v3 watermark value at capture time, and row counts per
dataset.

### A2. Canonical serialisation — the part that is usually got wrong
Two payloads that mean the same thing must serialise identically, or the diff drowns in noise
and people start ignoring it. Rules:

- **Object keys sorted** lexicographically, recursively.
- **Arrays:** sort if the field is a set (tags, course names); preserve order if it is a
  sequence. Decide per field and **record the decision in the manifest** — do not sort
  everything reflexively, that hides real ordering regressions.
- **Numbers:** serialise as decimal strings, never floats. `1000` and `1000.0` and `1e3` must
  produce one representation. Money as integer minor units + currency (§B4).
- **Null discipline — three states must stay distinct:** key absent, key present with `null`,
  key present with `""`. Collapsing these is precisely how a broken extraction disguises itself
  as an unchanged one. Encode as `ABSENT` / `NULL` / `EMPTY` sentinels in the canonical form.
- **Timestamps:** UTC, ISO-8601, fixed precision, explicit `Z`.
- **Strings:** no trimming, no case folding, no unicode normalisation. If the pipeline changes
  whitespace we want to see it.

### A3. Identity
Key each contact by a **stable identity that does not depend on the code under change** —
`(region, institute_id, user_id)`. Do **not** key by array position, GHL contact id, or
anything the sync assigns. An unstable key turns a field change into an add+remove pair and
makes the diff unreadable.

### A4. Diff output
Three buckets, reported separately and never summed:
1. **Contacts added** (in after, not before)
2. **Contacts removed** (in before, not after)
3. **Fields changed** — for each, `(identity, field_path, before, after)`

**Pass condition: all three buckets empty.** Any non-empty bucket is a stop, investigated to
root cause, not to a percentage. "Only 0.003% differ" is how you ship the `metadata.classId`
bug — 3 rows in 86,228.

### A5. What Leg A deliberately does not prove
It does not prove the payload is *correct*. Both sides can be equally wrong. That is Leg B.

---

## Leg B — ground-truth assertions (absolute)

Proves: *the payload is right*, independent of before/after. These are invariants that must hold
on the **after** capture and ideally on the before capture too (a failure on before is a
pre-existing bug we have just discovered, and worth its own ticket).

### B1. The extraction census — the single highest-value check
For **every** JSON path the pipeline extracts, over the full source table, count four things:

```sql
SELECT
  count_if(json_extract(doc, <path>) IS NOT NULL)                           AS present,
  count_if(json_extract_scalar(doc, <path>) IS NOT NULL)                    AS plain_ok,
  count_if(json_extract_scalar(doc, <path> || '["$oid"]') IS NOT NULL)      AS oid_ok,
  count_if(json_extract(doc, <path>) IS NOT NULL
           AND json_extract_scalar(doc, <path>) IS NULL
           AND json_extract_scalar(doc, <path> || '["$oid"]') IS NULL)      AS UNRESOLVED
FROM <table> WHERE region = <r>
```

**Hard fail: `UNRESOLVED > 0`.** The value exists in the document and our extraction produces
nothing from it. That is exactly how `amount` hid — present on 2,949,539 rows, resolved by none
of `$.amount`, `$numberDecimal`, `$numberInt`, `$numberLong`, because the real shape was
`{"value":{"$numberInt":…},"currency":…}`.

**Hard fail: `plain_ok > 0 AND oid_ok > 0` for a field the code reads with only one form.**
That is the mixed-encoding trap. Measured incidence, which is why this check is not optional:

| field | region | plain | `$oid`-wrapped | wrapped % |
|---|---|---|---|---|
| `metadata.classId` | in | 2,760,425 | 131 | 0.005% |
| `metadata.classId` | na | 86,225 | 3 | 0.003% |
| `metadata.sessionId` | in | 216,641 | 849 | 0.4% |
| `metadata.sessionId` | na | 33,264 | **2,181** | **6.2%** |
| `metadata.installmentId` | in | 2,086,981 | 26,634 | 1.3% |
| `metadata.installmentId` | na | 25,140 | **4,564** | **15.4%** |

Note the rates differ ~12× between regions. **A census run only on IN would read 1.3% as noise
while NA loses 15.4% of installments.** Run it per region, always.

### B2. Per-field null-rate bounds
For each output field, assert `null_rate <= <threshold>` on the after capture, with thresholds
agreed once and stored in the manifest. A wrong path produces a uniform 100% null rate, which
Leg A cannot see but this catches immediately. Set thresholds from the *current measured* rate
plus a small margin — not from optimism.

### B3. Independent cross-check per dataset
For at least one field per dataset, recompute the number by a **different path** and require
agreement. The point is path independence, not a second opinion from the same code.
- attended / upcoming → recompute from `session_participant_facts_v3` vs `session_facts_v3`
  joined to enrolments; require equality per student.
- participants → count from `processed_na.institute_participants` (daily layer, different
  lineage) and require agreement within the known dump lag, reconciled by `updatedat`.
- credits → `SUM(CREDIT) − SUM(DEBIT)` from the ledger vs the fact's stored balance.
- invoices → per `(user, currency)` totals vs the gateway report `transactions_report`.

### B4. Money invariants — assert these explicitly
`amount` is `{"value": <int|{"$numberInt"|"$numberDouble"}>, "currency": "<ISO>"}`.
Encoding varies by `op`: seed rows are `$numberInt` (8 IN rows are `$numberDouble`),
insert/update rows are plain numbers. Therefore:
- **Coalesce all three forms**; assert `UNRESOLVED = 0` per B1.
- **Values are minor units.** Never render as a major-unit amount without dividing, and never
  store as float. Integer minor units + currency code, end to end.
- **Never sum across currencies.** There are **35 distinct currencies in IN and 16 in NA**.
  Assert that every money aggregate is grouped by currency and that no output field is a
  currency-blind total. This is a correctness failure that looks like a plausible number.

### B5. Encoding-drift canary
The census (B1) is not a one-off. Mongo is schema-free and the app can start writing a new shape
at any time. Run the census **on a schedule** over the fields the pipeline depends on, and alert
on any change in the resolved/unresolved profile. This is the only defence against a future
`amount`-shaped surprise.

---

## 3. The tenant matrix

Minimum **6 tenants: 3 IN + 3 NA**, chosen for coverage, not convenience:

| slot | pick for |
|---|---|
| IN-1, NA-1 | highest volume — worst case for cost and for timeouts |
| IN-2, NA-2 | richest feature use — has credits **and** invoices **and** registration answers **and** parents |
| IN-3, NA-3 | edge shape — tiny or brand-new tenant, few sessions, likely NULLs and empty datasets |

NA is mandatory and not a formality: every mixed-encoding rate measured is materially worse in NA,
and NA tenants are more likely to be multi-currency.

Additionally include **one tenant with zero rows** in at least one dataset. Empty-vs-error is a
distinction that breaks quietly, and a tenant with no registration form is the cheapest way to
test it.

---

## 4. Procedure

1. **Freeze.** Record the v3 watermark and the git SHA. The lake moves underneath you — a diff
   across a moving source proves nothing.
2. **Capture before** (Leg A1) for all 6 tenants.
3. **Run Leg B on the before capture.** Any failure here is a pre-existing bug: file it, decide
   explicitly whether the optimisation is allowed to fix it. **A fix that changes output is not a
   regression — but it must be a declared, reviewed change, never a silent one.**
4. Airflow implements the change.
5. **Capture after**, at a comparable watermark.
6. **Run Leg A.** All three buckets must be empty, modulo rows whose source genuinely changed
   between captures — which is why step 1 matters, and why the diff should exclude contacts whose
   `ingested_at` moved inside the capture window rather than hand-waving them.
7. **Run Leg B on the after capture.** All assertions pass.
8. Record the result in `knowledge/asks/` or a proof log, with both captures' manifests.

### Repeat per change, not once at the end
Each optimisation lands separately — dropping `row_number()`, adding `region`, moving `upcoming()`
to the participant fact, then each new fact. A single diff at the end tells you something broke
but not which change broke it. **One capture-diff cycle per landed change.**

---

## 5. Ordering the changes by risk

Cheapest and safest first, so that a failed diff is easy to attribute:

| # | Change | Output risk | Note |
|---|---|---|---|
| 1 | Delete `row_number() OVER (PARTITION BY _id …)` | **none** — provably a no-op (`count(*) == count(DISTINCT _id)` on 7/7 tables) | pure win; still diff it |
| 2 | Add `region = '<r>'` | **none** if the tenant is single-region | prunes 96–98% |
| 3 | `upcoming()` → `session_participant_facts_v3`, bounded to +90d | **changes output deliberately** | today's counts are ~2.4× inflated by far-future recurrences; this is a **declared correction**, expect a diff and review it |
| 4 | Each new fact, one at a time | rises with each | diff per fact |

Change 3 is the one to watch: it is the first that *should* produce a diff. Agree the expected
shape of that diff **before** running it, or the temptation is to rationalise whatever comes out.

---

## 6. What would make me reject a proof

- A diff summarised as a percentage rather than a row count.
- A pass claimed on IN only.
- Leg B skipped because "Leg A was clean".
- Null, absent and empty collapsed in the canonical form.
- Captures taken at materially different watermarks with no exclusion logic.
- Thresholds in B2 chosen after seeing the result.
