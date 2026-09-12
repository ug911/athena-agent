---
collection: "Institute"
athena_table: "wise_app_backend__institute"
mongo_field_count: 134
athena_field_count: 290
matched: 122
coverage_pct: 91.0
last_diffed: "2026-09-08T08:05:41+00:00"
---

# Schema gap: `Institute` ↔ `processed.wise_app_backend__institute`

- **Mongo source**: [`src/models/Institute.js`](../source/mongo/Institute.md)
- **Athena counterpart**: [`schemas/processed/processed/wise_app_backend__institute.md`](../processed/processed/wise_app_backend__institute.md)
- **Coverage**: 122/134 Mongo fields are present in Athena (**91.0%**).

## In Mongo, missing from Athena

These fields are declared in the Mongoose schema but the Athena lake pipeline doesn't expose them. Either widen the extractor or note the field as JSON-only inside an existing varchar column.

| Path | Type | Ref | Required |
| --- | --- | --- | --- |
| `profilePicture` | `String` |  |  |
| `coverPicture` | `String` |  |  |
| `instituteCode` | `String` |  | required |
| `settings.disableRecordingProcessing` | `Boolean` |  |  |
| `settings.lensFeedbackAnonymous` | `Boolean` |  |  |
| `settings.feeSettings.enableSplitPayments` | `Boolean` |  |  |
| `settings.feeSettings.disableSuspension` | `Boolean` |  |  |
| `settings.skipRecordingHLSEncryption` | `Boolean` |  |  |
| `settings.sessionSettings.unpaidFeesSessionCancellationDays` | `Number` |  |  |
| `settings.localeSettings.calendarStartDay` | `String` |  |  |
| `settings.showLearnerContactToTeacher` | `Boolean` |  |  |
| `settings.participantContractVisibility` | `String` |  |  |

## In Athena, missing from Mongo

These fields exist in the Athena table but aren't declared in the current Mongoose schema. Likely renamed / deprecated, or added by the lake pipeline (timestamps, flattened helpers).

| Path | Type | Source |
| --- | --- | --- |
| `_id.$oid` | `string` | JSON path |
| `ownerid.$oid` | `string` | JSON path |
| `createdat.$date` | `object` | JSON path |
| `createdat.$date.$numberlong` | `string` | JSON path |
| `updatedat.$date` | `object` | JSON path |
| `updatedat.$date.$numberlong` | `string` | JSON path |
| `settings.accesscontrol` | `object` | JSON path |
| `settings.accesscontrol.classroomlevel` | `object` | JSON path |
| `settings.accesscontrol.classroomlevel.delete_class` | `object` | JSON path |
| `settings.accesscontrol.classroomlevel.delete_class.admin` | `bool` | JSON path |
| `settings.aireportsettings` | `object` | JSON path |
| `settings.aireportsettings.preview` | `bool` | JSON path |
| `settings.calendarsettings.inviteattendeeparents` | `bool` | JSON path |
| `settings.calendarsettings.invitedemoattendees` | `bool` | JSON path |
| `settings.calendarsettings.sendupdates` | `bool` | JSON path |
| `settings.chatsettings.chatpermissions` | `object` | JSON path |
| `settings.chatsettings.chatpermissions.parent` | `object` | JSON path |
| `settings.chatsettings.chatpermissions.parent.classadmin` | `bool` | JSON path |
| `settings.chatsettings.chatpermissions.parent.teacher` | `bool` | JSON path |
| `settings.chatsettings.chatpermissions.student` | `object` | JSON path |
| `settings.chatsettings.chatpermissions.student.classadmin` | `bool` | JSON path |
| `settings.chatsettings.chatpermissions.student.teacher` | `bool` | JSON path |
| `settings.chatsettings.chatpermissions.teacher` | `object` | JSON path |
| `settings.chatsettings.chatpermissions.teacher.classadmin` | `bool` | JSON path |
| `settings.chatsettings.chatpermissions.teacher.parent` | `bool` | JSON path |
| `settings.chatsettings.chatpermissions.teacher.student` | `bool` | JSON path |
| `settings.chatsettings.chatpermissions.teacher.teacher` | `bool` | JSON path |
| `settings.chatsettings.reactionsenabled` | `bool` | JSON path |
| `settings.devicebindingsettings.devicelimit.$numberint` | `string` | JSON path |
| `settings.feesettings.autochargedaysafter.$numberint` | `string` | JSON path |
| `settings.notificationsettings.categoryconfig.certificatecreation` | `object` | JSON path |
| `settings.notificationsettings.categoryconfig.contractcreated` | `object` | JSON path |
| `settings.notificationsettings.categoryconfig.contractsigned` | `object` | JSON path |
| `settings.notificationsettings.categoryconfig.dailysessionreminder` | `object` | JSON path |
| `settings.notificationsettings.categoryconfig.demosessionreminder_2160` | `object` | JSON path |
| `settings.notificationsettings.categoryconfig.demosessionupdated` | `object` | JSON path |
| `settings.notificationsettings.categoryconfig.discussioncreated` | `object` | JSON path |
| `settings.notificationsettings.categoryconfig.feeadded` | `object` | JSON path |
| `settings.notificationsettings.categoryconfig.feeaddedautocharge` | `object` | JSON path |
| `settings.notificationsettings.categoryconfig.feedue` | `object` | JSON path |
| `settings.notificationsettings.categoryconfig.feeoverdue` | `object` | JSON path |
| `settings.notificationsettings.categoryconfig.feepaid` | `object` | JSON path |
| `settings.notificationsettings.categoryconfig.instructoraddedtoclassroom` | `object` | JSON path |
| `settings.notificationsettings.categoryconfig.learneraddedtoclassroom` | `object` | JSON path |
| `settings.notificationsettings.categoryconfig.paymentfailed` | `object` | JSON path |
| `settings.notificationsettings.categoryconfig.phoneotp` | `object` | JSON path |
| `settings.notificationsettings.categoryconfig.sessioncreditupdates` | `object` | JSON path |
| `settings.notificationsettings.categoryconfig.sessionfeedback` | `object` | JSON path |
| `settings.notificationsettings.categoryconfig.sessionfeedbackwithquiz` | `object` | JSON path |
| `settings.notificationsettings.categoryconfig.sessionnotstartedadminreminder` | `object` | JSON path |
| `settings.notificationsettings.categoryconfig.sessionnotstartedteacherreminder` | `object` | JSON path |
| `settings.notificationsettings.categoryconfig.sessionreminder_10` | `object` | JSON path |
| `settings.notificationsettings.categoryconfig.sessionreminder_1440` | `object` | JSON path |
| `settings.notificationsettings.categoryconfig.sessionreminder_2160` | `object` | JSON path |
| `settings.notificationsettings.categoryconfig.sessionreminder_60` | `object` | JSON path |
| `settings.notificationsettings.categoryconfig.sessionstarted` | `object` | JSON path |
| `settings.notificationsettings.categoryconfig.sessionupdated` | `object` | JSON path |
| `settings.notificationsettings.categoryconfig.unreadchatreminder` | `object` | JSON path |
| `settings.notificationsettings.categoryconfig.wisestudentinvite` | `object` | JSON path |
| `settings.notificationsettings.categoryconfig.wiseteacherinvite` | `object` | JSON path |
| `settings.notificationsettings.emailbannerimageurl` | `string` | JSON path |
| `settings.notificationsettings.enableemail` | `bool` | JSON path |
| `settings.notificationsettings.enablewhatsapp` | `bool` | JSON path |
| `settings.notificationsettings.imagesinemailsenabled` | `bool` | JSON path |
| `settings.notificationsettings.registrationformreminderenabled` | `bool` | JSON path |
| `settings.onboardinginstructions` | `object` | JSON path |
| `settings.onboardinginstructions.admin` | `bool` | JSON path |
| `settings.onboardinginstructions.parent` | `bool` | JSON path |
| `settings.onboardinginstructions.student` | `bool` | JSON path |
| `settings.onboardinginstructions.teacher` | `bool` | JSON path |
| `settings.recordingdeletionpolicy.classroomstoskip.recordingdeletionpolicy.classroomstoskip[].$oid` | `string` | JSON path |
| `settings.recordingdeletionpolicy.deleteafterdays.$numberint` | `string` | JSON path |
| `settings.recordsessiongalleryview` | `bool` | JSON path |
| `settings.sessionallowstartbeforeminutes.$numberint` | `string` | JSON path |
| `settings.sessionnotstartedreminderdelay.$numberint` | `string` | JSON path |
| `settings.sessionsettings.advanceslotbookingbuffer.$numberint` | `string` | JSON path |
| `settings.sessionsettings.allowunpaidcreditsforbooking` | `bool` | JSON path |
| `settings.sessionsettings.autosubmitsessionfeedback` | `bool` | JSON path |
| `settings.sessionsettings.blockedadjacentslotbuffer.$numberint` | `string` | JSON path |
| `settings.sessionsettings.bookingtimeslotgranularity.$numberint` | `string` | JSON path |
| `settings.sessionsettings.creditsettings.allowteachercreditupdateonautosubmit` | `bool` | JSON path |
| `settings.sessionsettings.creditsettings.autodeduct` | `bool` | JSON path |
| `settings.sessionsettings.creditsettings.creditsperhour` | `object` | JSON path |
| `settings.sessionsettings.creditsettings.creditsperhour.$numberint` | `string` | JSON path |
| `settings.sessionsettings.creditsettings.lowcreditthreshold` | `object` | JSON path |
| `settings.sessionsettings.creditsettings.lowcreditthreshold.$numberint` | `string` | JSON path |
| `settings.sessionsettings.defaultsessiondurationselection` | `object` | JSON path |
| `settings.sessionsettings.defaultsessiondurationselection.$numberint` | `string` | JSON path |
| `settings.sessionsettings.enablerecurringsessionbooking` | `bool` | JSON path |
| `settings.sessionsettings.maxadvanceslotbookingdays.$numberint` | `string` | JSON path |
| `settings.sessionsettings.sessionaiconfig.aidataenabled` | `bool` | JSON path |
| `settings.sessionsettings.sessionaiconfig.aisummaryenabled` | `bool` | JSON path |
| `settings.sessionsettings.sessionaiconfig.summaryprompt` | `string` | JSON path |
| `settings.sessionsettings.studentslotcancellationbuffer.$numberint` | `string` | JSON path |
| `settings.showtagstoparticipants` | `bool` | JSON path |
| `settings.taxsettings.defaulttaxrulegroupid.$oid` | `string` | JSON path |
| `settings.uploadresourcestoyoutube` | `bool` | JSON path |
| `metadata.institutesize` | `string` | JSON path |
| `metadata.systemgenerated` | `bool` | JSON path |
