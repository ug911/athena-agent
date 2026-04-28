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

## Usage (from backend-api)

_6 call site(s) found across `controllers/`, `services/`, `repositories/`, `workers/`, `helpers/`._

### Query methods

- `.updateMany` × 2
- `.findOneAndUpdate` × 1
- `.find` × 1
- `.findOne` × 1
- `.deleteMany` × 1

### Top call sites

- `src/services/registrationFormService.js` × 5
- `src/workers/dataTransferWorker.js` × 1

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
