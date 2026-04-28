---
collection: "FeedbackForm"
model: "FeedbackForm"
source_file: "src/models/FeedbackForm.js"
field_count: 9
last_synced: "2026-04-28T10:58:23+00:00"
---

# `FeedbackForm` (Mongo collection)

- **Model**: `FeedbackForm`
- **Source**: [`src/models/FeedbackForm.js`](../../../src/models/FeedbackForm.js)
- **Athena counterpart**: try `processed.wise_app_backend__feedback_form` or `processed.wise_app_backend__feedbackform` — verify in `schemas/INDEX.md`.

## Indexes

- `[{ instituteId: 1, profile: 1 }, { unique: true }]`

## Local sub-schemas referenced

`feedbackFormSchema`, `questionSchema`

## Fields

| Path | Type | Ref | Enum | Required | Default | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `instituteId` | `ObjectId` | `Institute` |  | required |  |  |
| `profile` | `String` |  | teacher, student | required |  |  |
| `questions[]` | `<questionSchema>` |  |  |  |  |  |
| `questions[].required` | `Boolean` |  |  |  | false |  |
| `questions[].type` | `String` |  | <VALID_QUESTION_TYPES> | required |  |  |
| `questions[].questionText` | `String` |  |  |  |  |  |
| `questions[].options` | `Object` |  |  |  |  |  |
| `commentText` | `String` |  |  |  |  |  |
| `enabled` | `Boolean` |  |  |  | true |  |

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
