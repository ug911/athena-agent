---
collection: "TaxRuleGroup"
model: "TaxRuleGroup"
source_file: "src/models/TaxRuleGroup.js"
field_count: 12
last_synced: "2026-04-28T10:58:23+00:00"
---

# `TaxRuleGroup` (Mongo collection)

- **Model**: `TaxRuleGroup`
- **Source**: [`src/models/TaxRuleGroup.js`](../../../src/models/TaxRuleGroup.js)
- **Athena counterpart**: try `processed.wise_app_backend__tax_rule_group` or `processed.wise_app_backend__taxrulegroup` — verify in `schemas/INDEX.md`.

## Indexes

- `[{ instituteId: 1 }, {}]`

## Local sub-schemas referenced

`conditionSchema`, `taxRuleGroupSchema`, `taxRuleSchema`

## Fields

| Path | Type | Ref | Enum | Required | Default | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `instituteId` | `ObjectId` | `institute` |  | required |  |  |
| `name` | `String` |  |  | required |  |  |
| `rules[]` | `<taxRuleSchema>` |  |  |  |  |  |
| `rules[].description` | `String` |  |  | required |  |  |
| `rules[].value` | `Number` |  |  | required |  |  |
| `rules[].currency` | `String` |  |  |  |  |  |
| `rules[].type` | `String` |  | <VALID_TAX_RULE_TYPES> | required |  |  |
| `rules[].preTax` | `Boolean` |  |  |  | false |  |
| `rules[].conditions[]` | `<conditionSchema>` |  |  |  |  |  |
| `rules[].conditions[].field` | `String` |  |  | required |  |  |
| `rules[].conditions[].operator` | `String` |  | <VALID_OPERATORS> | required |  |  |
| `rules[].conditions[].value` | `Number` |  |  | required |  |  |

## Usage (from backend-api)

_7 call site(s) found across `controllers/`, `services/`, `repositories/`, `workers/`, `helpers/`._

### Query methods

- `.exists` × 3
- `.findOne` × 2
- `.deleteOne` × 1
- `.findOneAndUpdate` × 1

### Top call sites

- `src/controllers/InstituteController.js` × 5
- `src/services/taxService.js` × 2

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
