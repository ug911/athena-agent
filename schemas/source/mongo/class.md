---
collection: "class"
model: "class"
source_file: "src/models/Classroom.js"
field_count: 96
last_synced: "2026-04-28T10:58:23+00:00"
---

# `class` (Mongo collection)

- **Model**: `class`
- **Source**: [`src/models/Classroom.js`](../../../src/models/Classroom.js)
- **Athena counterpart**: try `processed.wise_app_backend__class` — verify in `schemas/INDEX.md`.

## Indexes

- `[{ classNumber: 1 }, { unique: true }]`
- `[{ namespace: 1, slug: 1 }, { unique: true, partialFilterExpression: { slug: { $exists: true } } }]`
- `[{ joinedRequest: 1, createdAt: 1 }]`
- `[{ pendingRequest: 1, createdAt: 1 }]`
- `[{ userId: 1 }, {}]`
- `[{ coTeachers: 1 }, { sparse: true }]`
- `[{ coTeacherRequests: 1 }, {}]`
- `[{ namespace: 1 }, { partialFilterExpression: { namespace: "wise_upsc" } }]`

## Local sub-schemas referenced

`autoBookSessionsSchema`, `classSchema`, `deletedStudentsSchema`, `magicJoinTokenConfigSchema`, `metadataSchema`, `notificationSettingsSchema`, `settingsSchema`, `studentSlotBookingSchema`, `suspendedStudentsSchema`, `zoomLinkSchema`

## Fields

| Path | Type | Ref | Enum | Required | Default | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `name` | `String` |  |  |  |  |  |
| `subject` | `String` |  |  |  |  |  |
| `description` | `String` |  |  |  |  |  |
| `slug` | `String` |  |  |  |  |  |
| `namespace` | `String` |  |  |  | 'wise' |  |
| `classCovers` | `Array<coverSchema>` |  |  |  | () => [{         link: `https://cdn.w… |  |
| `schedule` | `Object` |  |  |  | () => ({ occurrences: [] }) |  |
| `oldSchedules` | `Object` |  |  |  | () => [] |  |
| `zoomLink` | `<zoomLinkSchema>` |  |  |  | {} |  |
| `zoomLink.start_url` | `String` |  |  |  |  |  |
| `zoomLink.join_url` | `String` |  |  |  | '' |  |
| `zoomLink.password` | `String` |  |  |  |  |  |
| `zoomLink.timezone` | `String` |  |  |  |  |  |
| `zoomLink.sessionId` | `String` |  |  |  |  |  |
| `zoomLink.mettingId` | `String` |  |  |  |  |  |
| `zoomLink.meetingStarted` | `Boolean` |  |  |  |  |  |
| `zoomLink.provider` | `String` |  | <VALID_SESSION_PROVIDERS> |  |  |  |
| `zoomLink.mettingEnded` | `Boolean` |  |  |  | false |  |
| `zoomLink.meetingUUID` | `String` |  |  |  |  |  |
| `zoomLink.startTime` | `Date` |  |  |  | Date.now |  |
| `zoomLink.registrationEnabled` | `Boolean` |  |  |  |  |  |
| `zoomLink.metadata` | `Object` |  |  |  |  |  |
| `userId` | `ObjectId` | `user` |  | required |  |  |
| `classNumber` | `Number` |  |  | required | generateClassNumber |  |
| `pendingRequest` | `Array<ObjectId>` | `user` |  |  |  |  |
| `joinedRequest` | `Array<ObjectId>` | `user` |  |  |  |  |
| `coTeacherRequests` | `Array<ObjectId>` | `user` |  |  |  |  |
| `coTeachers` | `Array<ObjectId>` | `user` |  |  |  |  |
| `hidden` | `Boolean` |  |  |  | false |  |
| `archived` | `Boolean` |  |  |  | false |  |
| `archivedAt` | `Date` |  |  |  |  |  |
| `dataDeleted` | `Boolean` |  |  |  |  |  |
| `disableReminder` | `Boolean` |  |  |  | false |  |
| `thumbnail` | `String` |  |  |  |  |  |
| `deletedStudents[]` | `<deletedStudentsSchema>` |  |  |  |  |  |
| `deletedStudents[].userId` | `ObjectId` | `user` |  | required |  |  |
| `deletedStudents[].type` | `String` |  | REMOVED, LEFT |  |  |  |
| `deletedStudents[].deletedOn` | `Date` |  |  |  | Date.now |  |
| `suspendedStudents[]` | `<suspendedStudentsSchema>` |  |  |  |  |  |
| `suspendedStudents[].userId` | `ObjectId` | `user` |  | required |  |  |
| `suspendedStudents[].reason` | `String` |  | FEE_DELAY, SUSPEND |  |  |  |
| `settings` | `<settingsSchema>` |  |  |  | {} |  |
| `settings.disableStudentDiscussions` | `Boolean` |  |  |  | false |  |
| `settings.disableStudentComments` | `Boolean` |  |  |  | false |  |
| `settings.lockClassroom` | `Boolean` |  |  |  | false |  |
| `settings.lockAfter` | `Number` |  |  |  | 0 |  |
| `settings.openClassroom` | `Boolean` |  |  |  | false |  |
| `settings.admissionsDisabled` | `Boolean` |  |  |  | false |  |
| `settings.autoAccept` | `Boolean` |  |  |  | true |  |
| `settings.magicJoinTokenConfig` | `<magicJoinTokenConfigSchema>` |  |  |  |  |  |
| `settings.magicJoinTokenConfig.enabledOn` | `Date` |  |  |  | moment.utc() |  |
| `settings.magicJoinTokenConfig.token` | `String` |  |  |  |  |  |
| `settings.magicJoinTokenConfig.loginRequired` | `Boolean` |  |  |  | false |  |
| `settings.magicJoinTokenConfig.registrationRequired` | `Boolean` |  |  |  | false |  |
| `settings.studentSlotBooking` | `<studentSlotBookingSchema>` |  |  |  | {} |  |
| `settings.studentSlotBooking.enabled` | `Boolean` |  |  |  | false |  |
| `settings.studentSlotBooking.cancellationPolicyNote` | `String` |  |  |  |  |  |
| `settings.studentSlotBooking.slotDurations` | `Array<Number>` |  | <SESSION_DURATION_MINS> |  |  |  |
| `settings.notificationSettings` | `<notificationSettingsSchema>` |  |  |  |  |  |
| `settings.notificationSettings.DemoSessionReminder_10` | `Boolean` |  |  |  |  |  |
| `settings.notificationSettings.DemoSessionReminder_60` | `Boolean` |  |  |  |  |  |
| `settings.notificationSettings.DemoSessionReminder_1440` | `Boolean` |  |  |  |  |  |
| `settings.notificationSettings.DemoSessionUpdated` | `Boolean` |  |  |  |  |  |
| `settings.autoBookSessions` | `<autoBookSessionsSchema>` |  |  |  |  |  |
| `settings.autoBookSessions.slots` | `Array<<inline-schema>>` |  |  |  |  |  |
| `settings.autoBookSessions.recurrenceUnit` | `String` |  | W |  |  |  |
| `settings.autoBookSessions.lastSessionCreatedAt` | `Date` |  |  |  |  |  |
| `settings.validityInDays` | `Number` |  |  |  | -1 |  |
| `settings.provideCertification` | `Boolean` |  |  |  | false |  |
| `settings.videoPlayRestriction` | `Number` |  |  |  | -1 |  |
| `settings.requireCreditsForSession` | `Boolean` |  |  |  |  |  |
| `settings.allowBookingWithoutCredits` | `String` |  | NONE, ADMIN_TEACHER, ALL |  | 'ADMIN_TEACHER' |  |
| `settings.postSessionRedirectionURL` | `String` |  |  |  |  |  |
| `settings.enableSplitPayments` | `Boolean` |  |  |  |  |  |
| `settings.googleMeetLink` | `String` |  |  |  |  |  |
| `settings.disableCreditDeduction` | `Boolean` |  |  |  |  |  |
| `settings.zoomPoolNameOverride` | `String` |  |  |  |  |  |
| `settings.maxAdvanceSlotBookingDays` | `Number` |  | <MAX_ADVANCE_SLOT_BOOKING_DAYS_VALUES> |  |  |  |
| `settings.maxAllowedParticipants` | `Number` |  |  |  |  |  |
| `instituteId` | `ObjectId` | `Institute` |  |  |  |  |
| `instituteRequest` | `ObjectId` | `Institute` |  |  |  |  |
| `metadata` | `<metadataSchema>` |  |  |  |  |  |
| `metadata.tags` | `Array<String>` |  |  |  |  |  |
| `metadata.demo` | `Boolean` |  |  |  |  |  |
| `metadata.instituteId` | `ObjectId` | `Institute` |  |  |  |  |
| `metadata.isLensDefaultMeetingRoom` | `Boolean` |  |  |  |  |  |
| `metadata.duplicateClassroomId` | `String` |  |  |  |  |  |
| `metadata.appApprovalClassroom` | `Boolean` |  |  |  |  |  |
| `metadata.learnerManagedFlow` | `Boolean` |  |  |  |  |  |
| `metadata.ageRestriction` | `String` |  |  |  |  |  |
| `metadata.templateClassId` | `String` |  |  |  |  |  |
| `hiddenAt` | `Date` |  |  |  |  |  |
| `classType` | `String` |  | <ALL_CLASS_TYPES> |  | CLASS_TYPE_LIVE |  |
| `published` | `Boolean` |  |  |  | (doc) => doc?.classType === CLASS_TYP… |  |
| `showTests` | `Boolean` |  |  |  |  |  |
| `billingUnit` | `String` |  | <BILLING_UNITS> |  |  |  |

## Usage (from backend-api)

_224 call site(s) found across `controllers/`, `services/`, `repositories/`, `workers/`, `helpers/`._

### Query methods

- `.findOne` × 101
- `.find` × 64
- `.updateOne` × 28
- `.aggregate` × 16
- `.updateMany` × 4
- `.findOneAndUpdate` × 3
- `.create` × 2
- `.populate` × 2
- `.deleteMany` × 1
- `.exists` × 1
- `.deleteOne` × 1
- `.countDocuments` × 1

### Populated fields (join hints)

Fields commonly hydrated via `.populate(...)` — in Athena, these are the joins worth pre-computing or caching.

- `userId` × 12
- `instituteId` × 11
- `coTeachers` × 2
- `joinedRequest` × 1
- `zoomLink.sessionId` × 1

### Top call sites

- `src/controllers/InstituteController.js` × 28
- `src/controllers/TeacherController.js` × 19
- `src/services/classroomService.js` × 16
- `src/services/feeService.js` × 15
- `src/services/instituteService.js` × 12
- `src/controllers/FeeCollectionV2Controller.js` × 10
- `src/services/meetingService.js` × 8
- `src/workers/dataTransferWorker.js` × 8

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
