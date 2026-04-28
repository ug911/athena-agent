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

## Usage (from backend-api)

_49 call site(s) found across `controllers/`, `services/`, `repositories/`, `workers/`, `helpers/`._

### Query methods

- `.findOne` × 12
- `.aggregate` × 11
- `.updateOne` × 10
- `.find` × 6
- `.create` × 4
- `.deleteMany` × 2
- `.deleteOne` × 1
- `.exists` × 1
- `.updateMany` × 1
- `.insertMany` × 1

### Populated fields (join hints)

Fields commonly hydrated via `.populate(...)` — in Athena, these are the joins worth pre-computing or caching.

- `userId` × 1

### Top call sites

- `src/controllers/TeacherController.js` × 14
- `src/controllers/StudentController.js` × 5
- `src/services/classroomService.js` × 5
- `src/workers/dataTransferWorker.js` × 5
- `src/controllers/UserController.js` × 4
- `src/services/assessmentService.js` × 3
- `src/services/DemoAccountService.js` × 2
- `src/services/classroomCleanupService.js` × 2

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
