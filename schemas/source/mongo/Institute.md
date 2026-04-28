---
collection: "Institute"
model: "Institute"
source_file: "src/models/Institute.js"
field_count: 134
last_synced: "2026-04-28T10:58:23+00:00"
---

# `Institute` (Mongo collection)

- **Model**: `Institute`
- **Source**: [`src/models/Institute.js`](../../../src/models/Institute.js)
- **Athena counterpart**: try `processed.wise_app_backend__institute` — verify in `schemas/INDEX.md`.

## Indexes

- `[{ instituteCode: 1 }, { unique: true }]`
- `[{ ownerId: 1 }]`

## Local sub-schemas referenced

`calendarSettingsSchema`, `chatSettingsSchema`, `classroomDefaultSettingsSchema`, `contractSettingsSchema`, `creditSettingsSchema`, `deviceBindingSettingsSchema`, `feeSettingsSchema`, `instituteSchema`, `localeSettingsSchema`, `magicJoinTokenConfigSchema`, `notificationSettingsSchema`, `recordingDeletionPolicySchema`, `sessionAIConfigSchema`, `sessionSettingsSchema`, `settingsSchema`, `taxSettingsSchema`, `teacherAvailabilitySettingsSchema`, `teacherPermissionsSchema`, `zoomSettingsSchema`

## Fields

| Path | Type | Ref | Enum | Required | Default | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `name` | `String` |  |  | required |  |  |
| `profilePicture` | `String` |  |  |  | getThumbnailImageForInstitute |  |
| `coverPicture` | `String` |  |  |  | 'https://cdn.wiseapp.live/images/inst… |  |
| `instituteType` | `String` |  |  |  | 'OTHER' |  |
| `instituteCode` | `String` |  |  | required | generateInstituteNumber |  |
| `ownerId` | `ObjectId` | `user` |  | required |  |  |
| `namespace` | `String` |  |  | required |  |  |
| `settings` | `<settingsSchema>` |  |  |  | {} |  |
| `settings.autoRecord` | `Boolean` |  |  |  | false |  |
| `settings.classroomDefaultSettings` | `<classroomDefaultSettingsSchema>` |  |  |  | {} |  |
| `settings.classroomDefaultSettings.autoAccept` | `Boolean` |  |  |  | true |  |
| `settings.classroomDefaultSettings.magicJoinTokenConfig` | `<magicJoinTokenConfigSchema>` |  |  |  |  |  |
| `settings.classroomDefaultSettings.magicJoinTokenConfig.loginRequired` | `Boolean` |  |  |  | false |  |
| `settings.classroomDefaultSettings.magicJoinTokenConfig.registrationRequired` | `Boolean` |  |  |  | false |  |
| `settings.disableRecordingResources` | `Boolean` |  |  |  | false |  |
| `settings.disableWaitingRoom` | `Boolean` |  |  |  | false |  |
| `settings.disableAutoAdmit` | `Boolean` |  |  |  |  |  |
| `settings.meetingChatSetting` | `String` |  | <VALID_CHAT_SETTINGS> |  |  |  |
| `settings.disableScreenRecording` | `Boolean` |  |  |  | true |  |
| `settings.disableStopRecording` | `Boolean` |  |  |  |  |  |
| `settings.enableAdhocSession` | `Boolean` |  |  |  | false |  |
| `settings.enableResourceDownload` | `Boolean` |  |  |  |  |  |
| `settings.autoUnshareRecording` | `Boolean` |  |  |  |  |  |
| `settings.disableWebSdk` | `Boolean` |  |  |  | true |  |
| `settings.hideMeetingParticipants` | `Boolean` |  |  |  |  |  |
| `settings.hideSpeakerViewParticipants` | `Boolean` |  |  |  |  |  |
| `settings.disableRecordingProcessing` | `Boolean` |  |  |  |  |  |
| `settings.teacherAvailabilitySettings` | `<teacherAvailabilitySettingsSchema>` |  |  |  | {} |  |
| `settings.teacherAvailabilitySettings.enabled` | `Boolean` |  |  |  | false |  |
| `settings.teacherAvailabilitySettings.disableUpdatingLeaves` | `Boolean` |  |  |  | false |  |
| `settings.teacherAvailabilitySettings.disableUpdatingWorkingHours` | `Boolean` |  |  |  | false |  |
| `settings.defaultCurrency` | `String` |  | <ALLOWED_CURRENCIES> |  | CURRENCY_USD |  |
| `settings.defaultSessionCancellationPolicyNote` | `String` |  |  |  |  |  |
| `settings.welcomeEmailNote` | `String` |  |  |  |  |  |
| `settings.deviceBindingSettings` | `<deviceBindingSettingsSchema>` |  |  |  | {} |  |
| `settings.deviceBindingSettings.enabled` | `Boolean` |  |  |  | false |  |
| `settings.deviceBindingSettings.deviceLimit` | `Number` |  |  |  | 5 |  |
| `settings.recordingDeletionPolicy` | `<recordingDeletionPolicySchema>` |  |  |  | {} |  |
| `settings.recordingDeletionPolicy.deleteAfterDays` | `Number` |  |  |  | 45 |  |
| `settings.recordingDeletionPolicy.classroomsToSkip` | `Array<ObjectId>` | `class` |  |  |  |  |
| `settings.lensFeedbackAnonymous` | `Boolean` |  |  |  |  |  |
| `settings.teacherPermissions` | `<teacherPermissionsSchema>` |  |  |  | {} |  |
| `settings.teacherPermissions.disableSessionManagement` | `Boolean` |  |  |  | false |  |
| `settings.teacherPermissions.disableContentManagement` | `Boolean` |  |  |  | false |  |
| `settings.feeSettings` | `<feeSettingsSchema>` |  |  |  | {} |  |
| `settings.feeSettings.enableFees` | `Boolean` |  |  |  | true |  |
| `settings.feeSettings.autoCharge` | `Boolean` |  |  |  | false |  |
| `settings.feeSettings.autoChargeDaysAfter` | `Number` |  |  |  | DEFAULT_AUTO_CHARGE_DAYS_AFTER |  |
| `settings.feeSettings.showFeesToParentOnly` | `Boolean` |  |  |  | false |  |
| `settings.feeSettings.enableTutorPayout` | `Boolean` |  |  |  | true |  |
| `settings.feeSettings.autoApproveTutorPayouts` | `Boolean` |  |  |  | true |  |
| `settings.feeSettings.enableSplitPayments` | `Boolean` |  |  |  |  |  |
| `settings.feeSettings.allowAccessForPendingConfirmation` | `Boolean` |  |  |  | true |  |
| `settings.feeSettings.enableCoupons` | `Boolean` |  |  |  | true |  |
| `settings.feeSettings.invoiceBillingInformation` | `String` |  |  |  |  |  |
| `settings.feeSettings.invoiceAdditionalNote` | `String` |  |  |  |  |  |
| `settings.feeSettings.disableSuspension` | `Boolean` |  |  |  |  |  |
| `settings.calendarSettings` | `<calendarSettingsSchema>` |  |  |  | {} |  |
| `settings.calendarSettings.inviteAttendees` | `Boolean` |  |  |  | false |  |
| `settings.zoomSettings` | `<zoomSettingsSchema>` |  |  |  | {} |  |
| `settings.zoomSettings.entryExitChime` | `String` |  | <VALID_ENTRY_EXIT_CHIMES> |  | ENTRY_EXIT_CHIME_NONE |  |
| `settings.zoomSettings.enableParticipantScreenSharing` | `Boolean` |  |  |  | false |  |
| `settings.zoomSettings.hostVideoOn` | `Boolean` |  |  |  | false |  |
| `settings.zoomSettings.disableBreakoutRoom` | `Boolean` |  |  |  | false |  |
| `settings.zoomSettings.enableFocusMode` | `Boolean` |  |  |  |  |  |
| `settings.keepRawRecordings` | `Boolean` |  |  |  |  |  |
| `settings.skipRecordingHLSEncryption` | `Boolean` |  |  |  |  |  |
| `settings.sessionSettings` | `<sessionSettingsSchema>` |  |  |  | {} |  |
| `settings.sessionSettings.liveMeetingProvider` | `String` |  | <VALID_LIVE_SESSION_PROVIDER> |  | LIVE_SESSION_PROVIDER_ZOOM |  |
| `settings.sessionSettings.meetingSummaryVisibility` | `String` |  | <VALID_MEETING_SUMMARY_VISIBILITY> |  | MEETING_SUMMARY_VISIBILITY_ALL |  |
| `settings.sessionSettings.disallowConflict` | `Boolean` |  |  |  |  |  |
| `settings.sessionSettings.disableAITitle` | `Boolean` |  |  |  |  |  |
| `settings.sessionSettings.advanceSlotBookingBuffer` | `Number` |  | 0, 60, 180, 360, 540, 720, 1080, 1440, 2880, 4320, 5760, … |  | 60 |  |
| `settings.sessionSettings.blockedAdjacentSlotBuffer` | `Number` |  | 0, 5, 10, 15, 30, 60, 120 |  | 0 |  |
| `settings.sessionSettings.studentSlotCancellationBuffer` | `Number` |  | 60, 180, 360, 720, 1440, 2160, 2880 |  | 60 |  |
| `settings.sessionSettings.unpaidFeesSessionCancellationDays` | `Number` |  | 1, 2, 3 |  |  |  |
| `settings.sessionSettings.allowOnlyConsecutiveSlotBooking` | `Boolean` |  |  |  |  |  |
| `settings.sessionSettings.showScheduledTimeForPastSessionsToStudents` | `Boolean` |  |  |  |  |  |
| `settings.sessionSettings.enableInstituteLevelCredits` | `Boolean` |  |  |  |  |  |
| `settings.sessionSettings.allowTeacherToManageCredits` | `Boolean` |  |  |  |  |  |
| `settings.sessionSettings.enableLiveClassCredits` | `Boolean` |  |  |  |  |  |
| `settings.sessionSettings.doNotOverrideHost` | `Boolean` |  |  |  |  |  |
| `settings.sessionSettings.allowTeacherFeedbackUpdate` | `Boolean` |  |  |  | true |  |
| `settings.sessionSettings.allowStudentToCancelSession` | `Boolean` |  |  |  | true |  |
| `settings.sessionSettings.creditSettings` | `<creditSettingsSchema>` |  |  |  | {} |  |
| `settings.sessionSettings.creditSettings.deductionStrategy` | `String` |  | <VALID_CREDIT_DEDUCTION_STRATEGIES> |  | CREDIT_DEDUCTION_STRATEGY_ON_SCHEDULING |  |
| `settings.sessionSettings.creditSettings.deductionType` | `String` |  | <VALID_DEDUCTION_TYPES> |  | DEDUCTION_TYPE_FIXED |  |
| `settings.sessionSettings.creditSettings.autoDeductForMissedSessions` | `Boolean` |  |  |  | true |  |
| `settings.sessionSettings.enableGoogleMeet` | `Boolean` |  |  |  |  |  |
| `settings.sessionSettings.bookingTimeslotGranularity` | `Number` |  | 5, 15, 30 |  | 15 |  |
| `settings.sessionSettings.maxAdvanceSlotBookingDays` | `Number` |  | <MAX_ADVANCE_SLOT_BOOKING_DAYS_VALUES> |  | DEFAULT_MAX_ADVANCE_SLOT_BOOKING_DAYS |  |
| `settings.sessionSettings.sessionAIConfig` | `<sessionAIConfigSchema>` |  |  |  |  |  |
| `settings.sessionSettings.sessionAIConfig.enabled` | `Boolean` |  |  |  | false |  |
| `settings.sessionSettings.studentFeedbackVisibility` | `String` |  | ADMIN, ADMIN_TEACHER |  |  |  |
| `settings.sessionSettings.updateCreditAccess` | `String` |  | OWNER, ADMIN, ADMIN_TEACHER |  |  |  |
| `settings.sessionSettings.restrictTeacherSessionVisibility` | `Boolean` |  |  |  |  |  |
| `settings.sessionSettings.disableOfflineSessions` | `Boolean` |  |  |  |  |  |
| `settings.taxSettings` | `<taxSettingsSchema>` |  |  |  |  |  |
| `settings.taxSettings.enabled` | `Boolean` |  |  | required |  |  |
| `settings.taxSettings.defaultTaxRuleGroupId` | `ObjectId` | `TaxRuleGroup` |  | required |  |  |
| `settings.showHiddenClassroomData` | `Boolean` |  |  |  |  |  |
| `settings.storeRedirectionURL` | `String` |  |  |  |  |  |
| `settings.sessionRecordingView` | `String` |  | <VALID_SESSION_RECORDING_VIEWS> |  | SESSION_RECORDING_VIEW_SPEAKER |  |
| `settings.sessionAllowStartBeforeMinutes` | `Number` |  | <VALID_SESSION_ALLOW_START_BEFORE_MINUTES_RANGE> |  | DEFAULT_SESSION_ALLOW_START_BEFORE_MI… |  |
| `settings.disableSessionLiveStreaming` | `Boolean` |  |  |  |  |  |
| `settings.sessionNotStartedReminderDelay` | `Number` |  |  |  | DEFAULT_SESSION_NOT_STARTED_REMINDER_… |  |
| `settings.notificationSettings` | `<notificationSettingsSchema>` |  |  |  | {} |  |
| `settings.notificationSettings.replyToEmail` | `String` |  |  |  |  |  |
| `settings.notificationSettings.disableWhatsApp` | `Boolean` |  |  |  |  |  |
| `settings.notificationSettings.disableEmail` | `Boolean` |  |  |  |  |  |
| `settings.notificationSettings.categoryConfig` | `Object` |  |  |  |  |  |
| `settings.notificationSettings.fromEmail` | `String` |  |  |  |  |  |
| `settings.joinLensSecondaryCTA` | `String` |  | BROWSER, ZOOM, ZOOM_ON_MOBILE, HIDE |  | "BROWSER" |  |
| `settings.joinLensPrimaryCTA` | `String` |  | SHOW, HIDE |  |  |  |
| `settings.showWebinarOption` | `Boolean` |  |  |  | false |  |
| `settings.enableMeetingAnnotation` | `Boolean` |  |  |  | true |  |
| `settings.contractSettings` | `<contractSettingsSchema>` |  |  |  | {} |  |
| `settings.contractSettings.enabled` | `Boolean` |  |  |  | false |  |
| `settings.contractSettings.showContractsToParentOnly` | `Boolean` |  |  |  | false |  |
| `settings.allowPublicRegistrations` | `Boolean` |  |  |  | true |  |
| `settings.chatSettings` | `<chatSettingsSchema>` |  |  |  | {} |  |
| `settings.chatSettings.enabled` | `Boolean` |  |  |  | true |  |
| `settings.localeSettings` | `<localeSettingsSchema>` |  |  |  | {} |  |
| `settings.localeSettings.timeFormat` | `String` |  | 12h, 24h |  | '12h' |  |
| `settings.localeSettings.calendarStartDay` | `String` |  | MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, S… |  |  |  |
| `settings.enableGoogleDriveInAssessments` | `Boolean` |  |  |  |  |  |
| `settings.showLearnerContactToTeacher` | `Boolean` |  |  |  |  |  |
| `settings.participantRegistrationFormVisibility` | `String` |  | ADMIN, ADMIN_TEACHER |  |  |  |
| `settings.participantContractVisibility` | `String` |  | ADMIN, ADMIN_TEACHER |  |  |  |
| `settings.participantAdditionalNoteVisibility` | `String` |  | ADMIN, ADMIN_TEACHER |  |  |  |
| `settings.blockedPlatforms` | `Array<String>` |  |  |  | undefined |  |
| `settings.termsOfServiceLink` | `String` |  |  |  |  |  |
| `settings.privacyPolicyLink` | `String` |  |  |  |  |  |
| `metadata` | `Object` |  |  |  |  |  |

## Usage (from backend-api)

_65 call site(s) found across `controllers/`, `services/`, `repositories/`, `workers/`, `helpers/`._

### Query methods

- `.findOne` × 31
- `.find` × 11
- `.aggregate` × 5
- `.updateMany` × 4
- `.updateOne` × 4
- `.exists` × 4
- `.create` × 3
- `.deleteOne` × 1
- `.findOneAndUpdate` × 1
- `.countDocuments` × 1

### Populated fields (join hints)

Fields commonly hydrated via `.populate(...)` — in Athena, these are the joins worth pre-computing or caching.

- `ownerId` × 9

### Top call sites

- `src/controllers/InstituteController.js` × 8
- `src/services/instituteService.js` × 8
- `src/controllers/ParentController.js` × 5
- `src/controllers/UserController.js` × 4
- `src/services/instituteAdmissionService.js` × 4
- `src/controllers/IntegrationTestController.js` × 2
- `src/controllers/PublicController.js` × 2
- `src/services/contractService.js` × 2

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
