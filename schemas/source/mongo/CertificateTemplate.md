---
collection: "CertificateTemplate"
model: "CertificateTemplate"
source_file: "src/models/CertificateTemplate.js"
field_count: 15
last_synced: "2026-04-28T10:58:23+00:00"
---

# `CertificateTemplate` (Mongo collection)

- **Model**: `CertificateTemplate`
- **Source**: [`src/models/CertificateTemplate.js`](../../../src/models/CertificateTemplate.js)
- **Athena counterpart**: try `processed.wise_app_backend__certificate_template` or `processed.wise_app_backend__certificatetemplate` — verify in `schemas/INDEX.md`.

## Local sub-schemas referenced

`CertificateTemplateSchema`, `TemplateVariableSchema`

## Fields

| Path | Type | Ref | Enum | Required | Default | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `htmlTemplate` | `String` |  |  | required |  |  |
| `previewImage` | `String` |  |  | required |  |  |
| `imageHeight` | `Number` |  |  | required |  |  |
| `imageWidth` | `Number` |  |  | required |  |  |
| `archived` | `Boolean` |  |  |  | false |  |
| `variables[]` | `<TemplateVariableSchema>` |  |  |  |  |  |
| `variables[].name` | `String` |  |  | required |  |  |
| `variables[].displayName` | `String` |  |  | required |  |  |
| `variables[].type` | `String` |  | TEMPLATE_VARIABLE_TYPE_IMAGE, TEMPLATE_VARIABLE_TYPE_TEXT | required |  |  |
| `variables[].charLimit` | `Number` |  |  |  | DEFAULT_CHAR_LIMIT |  |
| `variables[].defaultValue` | `String` |  |  | required |  |  |
| `variables[].value` | `String` |  |  |  | '' |  |
| `variables[].editable` | `Boolean` |  |  |  | true |  |
| `variables[].style` | `String` |  |  |  |  |  |
| `variables[].stylable` | `Boolean` |  |  |  |  |  |

## Usage (from backend-api)

_2 call site(s) found across `controllers/`, `services/`, `repositories/`, `workers/`, `helpers/`._

### Query methods

- `.find` × 1
- `.findOne` × 1

### Top call sites

- `src/controllers/TeacherController.js` × 1
- `src/services/classroomCertificateService.js` × 1

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
