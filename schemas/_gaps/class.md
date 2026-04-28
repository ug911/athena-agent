---
collection: "class"
athena_table: "wise_app_backend__class"
mongo_field_count: 96
athena_field_count: 90
matched: 47
coverage_pct: 49.0
last_diffed: "2026-04-28T11:07:30+00:00"
---

# Schema gap: `class` ↔ `processed.wise_app_backend__class`

- **Mongo source**: [`src/models/Classroom.js`](../source/mongo/class.md)
- **Athena counterpart**: [`schemas/processed/processed/wise_app_backend__class.md`](../processed/processed/wise_app_backend__class.md)
- **Coverage**: 47/96 Mongo fields are present in Athena (**49.0%**).

## In Mongo, missing from Athena

These fields are declared in the Mongoose schema but the Athena lake pipeline doesn't expose them. Either widen the extractor or note the field as JSON-only inside an existing varchar column.

| Path | Type | Ref | Required |
| --- | --- | --- | --- |
| `description` | `String` |  |  |
| `slug` | `String` |  |  |
| `classCovers` | `Array<coverSchema>` |  |  |
| `zoomLink.sessionId` | `String` |  |  |
| `zoomLink.meetingStarted` | `Boolean` |  |  |
| `zoomLink.provider` | `String` |  |  |
| `zoomLink.registrationEnabled` | `Boolean` |  |  |
| `zoomLink.metadata` | `Object` |  |  |
| `hidden` | `Boolean` |  |  |
| `archivedAt` | `Date` |  |  |
| `dataDeleted` | `Boolean` |  |  |
| `thumbnail` | `String` |  |  |
| `settings.studentSlotBooking` | `<studentSlotBookingSchema>` |  |  |
| `settings.studentSlotBooking.enabled` | `Boolean` |  |  |
| `settings.studentSlotBooking.cancellationPolicyNote` | `String` |  |  |
| `settings.studentSlotBooking.slotDurations` | `Array<Number>` |  |  |
| `settings.notificationSettings` | `<notificationSettingsSchema>` |  |  |
| `settings.notificationSettings.DemoSessionReminder_10` | `Boolean` |  |  |
| `settings.notificationSettings.DemoSessionReminder_60` | `Boolean` |  |  |
| `settings.notificationSettings.DemoSessionReminder_1440` | `Boolean` |  |  |
| `settings.notificationSettings.DemoSessionUpdated` | `Boolean` |  |  |
| `settings.autoBookSessions` | `<autoBookSessionsSchema>` |  |  |
| `settings.autoBookSessions.slots` | `Array<<inline-schema>>` |  |  |
| `settings.autoBookSessions.recurrenceUnit` | `String` |  |  |
| `settings.autoBookSessions.lastSessionCreatedAt` | `Date` |  |  |
| `settings.requireCreditsForSession` | `Boolean` |  |  |
| `settings.allowBookingWithoutCredits` | `String` |  |  |
| `settings.postSessionRedirectionURL` | `String` |  |  |
| `settings.enableSplitPayments` | `Boolean` |  |  |
| `settings.googleMeetLink` | `String` |  |  |
| `settings.disableCreditDeduction` | `Boolean` |  |  |
| `settings.zoomPoolNameOverride` | `String` |  |  |
| `settings.maxAdvanceSlotBookingDays` | `Number` |  |  |
| `settings.maxAllowedParticipants` | `Number` |  |  |
| `instituteRequest` | `ObjectId` | `Institute` |  |
| `metadata` | `<metadataSchema>` |  |  |
| `metadata.tags` | `Array<String>` |  |  |
| `metadata.demo` | `Boolean` |  |  |
| `metadata.isLensDefaultMeetingRoom` | `Boolean` |  |  |
| `metadata.duplicateClassroomId` | `String` |  |  |
| `metadata.appApprovalClassroom` | `Boolean` |  |  |
| `metadata.learnerManagedFlow` | `Boolean` |  |  |
| `metadata.ageRestriction` | `String` |  |  |
| `metadata.templateClassId` | `String` |  |  |
| `hiddenAt` | `Date` |  |  |
| `classType` | `String` |  |  |
| `published` | `Boolean` |  |  |
| `showTests` | `Boolean` |  |  |
| `billingUnit` | `String` |  |  |

## In Athena, missing from Mongo

These fields exist in the Athena table but aren't declared in the current Mongoose schema. Likely renamed / deprecated, or added by the lake pipeline (timestamps, flattened helpers).

| Path | Type | Source |
| --- | --- | --- |
| `pendingadmins` | `string` | column |
| `admins` | `string` | column |
| `timing` | `string` | column |
| `timingversion` | `string` | column |
| `_id.$oid` | `string` | JSON path |
| `zoomlink.starttime.$date` | `object` | JSON path |
| `zoomlink.starttime.$date.$numberlong` | `string` | JSON path |
| `admins.[]` | `object` | JSON path |
| `admins.[].$oid` | `string` | JSON path |
| `pendingrequest.[]` | `object` | JSON path |
| `pendingrequest.[].$oid` | `string` | JSON path |
| `joinedrequest.[]` | `object` | JSON path |
| `joinedrequest.[].$oid` | `string` | JSON path |
| `coteachers.[]` | `object` | JSON path |
| `coteachers.[].$oid` | `string` | JSON path |
| `timing.[]` | `object` | JSON path |
| `timing.[].day` | `string` | JSON path |
| `timing.[].from` | `string` | JSON path |
| `timing.[].selected` | `bool` | JSON path |
| `timing.[].to` | `string` | JSON path |
| `userid.$oid` | `string` | JSON path |
| `classnumber.$numberint` | `string` | JSON path |
| `timingversion.$numberint` | `string` | JSON path |
| `settings.disablescreencapture` | `bool` | JSON path |
| `settings.disablewebsdk` | `bool` | JSON path |
| `settings.lockafter.$numberint` | `string` | JSON path |
| `settings.magicjointokenconfig.enabledon.$date` | `object` | JSON path |
| `settings.magicjointokenconfig.enabledon.$date.$numberlong` | `string` | JSON path |
| `settings.validityindays.$numberint` | `string` | JSON path |
| `settings.videoplayrestriction.$numberint` | `string` | JSON path |
| `createdat.$date` | `object` | JSON path |
| `createdat.$date.$numberlong` | `string` | JSON path |
| `deletedstudents.[]` | `object` | JSON path |
| `deletedstudents.[].deletedon.$date` | `object` | JSON path |
| `deletedstudents.[].deletedon.$date.$numberlong` | `string` | JSON path |
| `deletedstudents.[].userid.$oid` | `string` | JSON path |
| `suspendedstudents.[]` | `object` | JSON path |
| `suspendedstudents.[].userid.$oid` | `string` | JSON path |
| `instituteid.$oid` | `string` | JSON path |
| `__v.$numberint` | `string` | JSON path |
