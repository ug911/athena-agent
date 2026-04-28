---
collection: "assignments"
model: "assignments"
source_file: "src/models/Assessment.js"
field_count: 45
last_synced: "2026-04-28T10:58:23+00:00"
---

# `assignments` (Mongo collection)

- **Model**: `assignments`
- **Source**: [`src/models/Assessment.js`](../../../src/models/Assessment.js)
- **Athena counterpart**: try `processed.wise_app_backend__assignments` — verify in `schemas/INDEX.md`.

## Local sub-schemas referenced

`assignmentsSchema`, `criteriaFeedbackSchema`, `criteriaSchema`, `googleDocFileSchema`, `solutionsSchema`, `submissionSchema`

## Fields

| Path | Type | Ref | Enum | Required | Default | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `topic` | `String` |  |  | required |  |  |
| `submissionDate` | `String` |  |  |  |  |  |
| `submissionTime` | `String` |  |  |  |  |  |
| `startTime` | `Date` |  |  |  |  |  |
| `submitBy` | `Date` |  |  |  |  |  |
| `description` | `String` |  |  |  |  |  |
| `maxMarks` | `Number` |  |  |  |  |  |
| `criteria[]` | `<criteriaSchema>` |  |  |  | undefined |  |
| `criteria[].title` | `String` |  |  | required |  |  |
| `criteria[].maxMarks` | `Number` |  |  | required |  |  |
| `solutions[]` | `<solutionsSchema>` |  |  |  |  |  |
| `solutions[].studentId` | `ObjectId` | `user` |  | required |  |  |
| `solutions[].attachments` | `Array<attachmentSchema>` |  |  |  |  |  |
| `submission[]` | `<submissionSchema>` |  |  |  |  |  |
| `submission[].studentId` | `ObjectId` | `user` |  | required |  |  |
| `submission[].attachments` | `Array<attachmentSchema>` |  |  |  |  |  |
| `submission[].textAnswer` | `String` |  |  |  |  |  |
| `submission[].getMark` | `Number` |  |  |  |  |  |
| `submission[].feedBack` | `String` |  |  |  |  |  |
| `submission[].feedbackRecordings` | `Array<attachmentSchema>` |  |  |  |  |  |
| `submission[].submissionStatus` | `String` |  | pending, submitted, graded |  | 'submitted' |  |
| `submission[].gradedAt` | `Date` |  |  |  |  |  |
| `submission[].answer` | `String` |  |  |  |  |  |
| `submission[].createdAt` | `Date` |  |  |  | Date.now |  |
| `submission[].markedAsSolution` | `Boolean` |  |  |  | false |  |
| `submission[].criteriaFeedback[]` | `<criteriaFeedbackSchema>` |  |  |  | undefined |  |
| `submission[].criteriaFeedback[].criteriaId` | `ObjectId` |  |  | required |  |  |
| `submission[].criteriaFeedback[].marks` | `Number` |  |  | required |  |  |
| `submission[].criteriaFeedback[].feedback` | `String` |  |  |  |  |  |
| `submission[].feedbackFiles` | `Array<attachmentSchema>` |  |  |  |  |  |
| `submission[].submissionFile` | `<googleDocFileSchema>` |  |  |  |  |  |
| `submission[].submissionFile.fileId` | `String` |  |  | required |  |  |
| `submission[].submissionFile.name` | `String` |  |  | required |  |  |
| `userId` | `ObjectId` | `user` |  | required |  |  |
| `classId` | `ObjectId` | `class` |  | required |  |  |
| `lastCommentedAt` | `Date` |  |  |  |  |  |
| `disableCommenting` | `Boolean` |  |  |  | false |  |
| `attachments` | `Array<attachmentSchema>` |  |  |  |  |  |
| `comments` | `Array<commentsSchema>` |  |  |  |  |  |
| `public` | `Boolean` |  |  |  |  |  |
| `thumbnail` | `String` |  |  |  |  |  |
| `pending` | `Boolean` |  |  |  |  |  |
| `googleDocFile` | `<googleDocFileSchema>` |  |  |  |  |  |
| `googleDocFile.fileId` | `String` |  |  | required |  |  |
| `googleDocFile.name` | `String` |  |  | required |  |  |

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
