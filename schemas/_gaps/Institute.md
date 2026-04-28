---
collection: "Institute"
athena_table: "wise_app_backend__institute"
mongo_field_count: 134
athena_field_count: 140
matched: 106
coverage_pct: 79.1
last_diffed: "2026-04-28T11:07:30+00:00"
---

# Schema gap: `Institute` ↔ `processed.wise_app_backend__institute`

- **Mongo source**: [`src/models/Institute.js`](../source/mongo/Institute.md)
- **Athena counterpart**: [`schemas/processed/processed/wise_app_backend__institute.md`](../processed/processed/wise_app_backend__institute.md)
- **Coverage**: 106/134 Mongo fields are present in Athena (**79.1%**).

## In Mongo, missing from Athena

These fields are declared in the Mongoose schema but the Athena lake pipeline doesn't expose them. Either widen the extractor or note the field as JSON-only inside an existing varchar column.

| Path | Type | Ref | Required |
| --- | --- | --- | --- |
| `profilePicture` | `String` |  |  |
| `coverPicture` | `String` |  |  |
| `instituteCode` | `String` |  | required |
| `settings.classroomDefaultSettings.magicJoinTokenConfig` | `<magicJoinTokenConfigSchema>` |  |  |
| `settings.classroomDefaultSettings.magicJoinTokenConfig.loginRequired` | `Boolean` |  |  |
| `settings.classroomDefaultSettings.magicJoinTokenConfig.registrationRequired` | `Boolean` |  |  |
| `settings.disableAutoAdmit` | `Boolean` |  |  |
| `settings.hideSpeakerViewParticipants` | `Boolean` |  |  |
| `settings.disableRecordingProcessing` | `Boolean` |  |  |
| `settings.lensFeedbackAnonymous` | `Boolean` |  |  |
| `settings.feeSettings.enableSplitPayments` | `Boolean` |  |  |
| `settings.feeSettings.disableSuspension` | `Boolean` |  |  |
| `settings.zoomSettings.enableFocusMode` | `Boolean` |  |  |
| `settings.keepRawRecordings` | `Boolean` |  |  |
| `settings.skipRecordingHLSEncryption` | `Boolean` |  |  |
| `settings.sessionSettings.unpaidFeesSessionCancellationDays` | `Number` |  |  |
| `settings.sessionSettings.enableGoogleMeet` | `Boolean` |  |  |
| `settings.showHiddenClassroomData` | `Boolean` |  |  |
| `settings.disableSessionLiveStreaming` | `Boolean` |  |  |
| `settings.notificationSettings.replyToEmail` | `String` |  |  |
| `settings.notificationSettings.fromEmail` | `String` |  |  |
| `settings.joinLensPrimaryCTA` | `String` |  |  |
| `settings.localeSettings.calendarStartDay` | `String` |  |  |
| `settings.showLearnerContactToTeacher` | `Boolean` |  |  |
| `settings.participantContractVisibility` | `String` |  |  |
| `settings.blockedPlatforms` | `Array<String>` |  |  |
| `settings.termsOfServiceLink` | `String` |  |  |
| `settings.privacyPolicyLink` | `String` |  |  |

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
| `settings.devicebindingsettings.devicelimit.$numberint` | `string` | JSON path |
| `settings.feesettings.autochargedaysafter.$numberint` | `string` | JSON path |
| `settings.notificationsettings.categoryconfig.sessionreminder_1440` | `object` | JSON path |
| `settings.notificationsettings.categoryconfig.sessionreminder_60` | `object` | JSON path |
| `settings.notificationsettings.categoryconfig.wisestudentinvite` | `object` | JSON path |
| `settings.notificationsettings.enableemail` | `bool` | JSON path |
| `settings.notificationsettings.enablewhatsapp` | `bool` | JSON path |
| `settings.recordingdeletionpolicy.classroomstoskip.recordingdeletionpolicy.classroomstoskip[].$oid` | `string` | JSON path |
| `settings.recordingdeletionpolicy.deleteafterdays.$numberint` | `string` | JSON path |
| `settings.sessionallowstartbeforeminutes.$numberint` | `string` | JSON path |
| `settings.sessionnotstartedreminderdelay.$numberint` | `string` | JSON path |
| `settings.sessionsettings.advanceslotbookingbuffer.$numberint` | `string` | JSON path |
| `settings.sessionsettings.autosubmitsessionfeedback` | `bool` | JSON path |
| `settings.sessionsettings.blockedadjacentslotbuffer.$numberint` | `string` | JSON path |
| `settings.sessionsettings.bookingtimeslotgranularity.$numberint` | `string` | JSON path |
| `settings.sessionsettings.creditsettings.autodeduct` | `bool` | JSON path |
| `settings.sessionsettings.maxadvanceslotbookingdays.$numberint` | `string` | JSON path |
| `settings.sessionsettings.studentslotcancellationbuffer.$numberint` | `string` | JSON path |
| `settings.taxsettings.defaulttaxrulegroupid.$oid` | `string` | JSON path |
| `settings.uploadresourcestoyoutube` | `bool` | JSON path |
| `metadata.institutesize` | `string` | JSON path |
