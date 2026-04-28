---
collection: "RegistrationForm"
model: "RegistrationForm"
source_file: "src/models/RegistrationForm.js"
field_count: 7
last_synced: "2026-04-28T10:58:23+00:00"
---

# `RegistrationForm` (Mongo collection)

- **Model**: `RegistrationForm`
- **Source**: [`src/models/RegistrationForm.js`](../../../src/models/RegistrationForm.js)
- **Athena counterpart**: try `processed.wise_app_backend__registration_form` or `processed.wise_app_backend__registrationform` — verify in `schemas/INDEX.md`.

## Indexes

- `[{ instituteId: 1, classId: 1 }, { unique: true }]`

## Local sub-schemas referenced

`RegistrationFormSchema`, `settingsSchema`

## Fields

| Path | Type | Ref | Enum | Required | Default | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `instituteId` | `ObjectId` | `Institute` |  | required |  |  |
| `classId` | `ObjectId` | `class` |  |  |  |  |
| `enabled` | `Boolean` |  |  | required | false |  |
| `settings` | `<settingsSchema>` |  |  |  | {} |  |
| `settings.requiredForStudents` | `Boolean` |  |  |  | false |  |
| `settings.disableUpdatingSubmission` | `Boolean` |  |  |  | false |  |
| `fields` | `Array<registrationFormQuestionSchema>` |  |  |  |  |  |

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
