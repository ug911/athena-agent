---
collection: "RegistrationFormSubmission"
model: "RegistrationFormSubmission"
source_file: "src/models/RegistrationFormSubmission.js"
field_count: 6
last_synced: "2026-04-28T10:58:23+00:00"
---

# `RegistrationFormSubmission` (Mongo collection)

- **Model**: `RegistrationFormSubmission`
- **Source**: [`src/models/RegistrationFormSubmission.js`](../../../src/models/RegistrationFormSubmission.js)
- **Athena counterpart**: try `processed.wise_app_backend__registration_form_submission` or `processed.wise_app_backend__registrationformsubmission` — verify in `schemas/INDEX.md`.

## Indexes

- `[{ instituteId: 1, userId: 1, classId: 1, sessionId: 1 }, { unique: true }]`

## Local sub-schemas referenced

`RegistrationFormSubmissionSchema`

## Fields

| Path | Type | Ref | Enum | Required | Default | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `instituteId` | `ObjectId` | `Institute` |  | required |  |  |
| `userId` | `ObjectId` | `user` |  | required |  |  |
| `classId` | `ObjectId` | `class` |  |  |  |  |
| `sessionId` | `ObjectId` | `zoom` |  |  |  |  |
| `answers` | `Array<answerSchema>` |  |  |  |  |  |
| `status` | `String` |  | STATUS_PENDING, STATUS_PARTIALLY_SUBMITTED, STATUS_SUBMITTED | required |  |  |

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
