---
collection: "Whitelabel"
model: "Whitelabel"
source_file: "src/models/Whitelabel.js"
field_count: 99
last_synced: "2026-04-28T10:58:23+00:00"
---

# `Whitelabel` (Mongo collection)

- **Model**: `Whitelabel`
- **Source**: [`src/models/Whitelabel.js`](../../../src/models/Whitelabel.js)
- **Athena counterpart**: try `processed.wise_app_backend__whitelabel` — verify in `schemas/INDEX.md`.

## Local sub-schemas referenced

`displayConfigSchema`, `featureConfigSchema`, `nameVariablesSchema`, `systemConfigSchema`, `themeConfigSchema`, `versionConfigSchema`, `whiteLabelSchema`

## Fields

| Path | Type | Ref | Enum | Required | Default | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `namespace` | `String` |  |  | required, unique |  |  |
| `hostnames` | `Array<String>` |  |  |  |  |  |
| `featureConfig` | `<featureConfigSchema>` |  |  |  | {} |  |
| `featureConfig.canCreateClassrooms` | `Boolean` |  |  |  | true |  |
| `featureConfig.disableEmailLogin` | `Boolean` |  |  |  | false |  |
| `featureConfig.disablePhoneLogin` | `Boolean` |  |  |  | true |  |
| `featureConfig.disableGoogleLogin` | `Boolean` |  |  |  | false |  |
| `featureConfig.disableAppleLogin` | `Boolean` |  |  |  | true |  |
| `featureConfig.enableJWTBasedLogin` | `Boolean` |  |  |  | false |  |
| `featureConfig.adminUserIds` | `Array` |  |  |  | [] |  |
| `featureConfig.enableLens` | `Boolean` |  |  |  |  |  |
| `featureConfig.disableRedirectToPrimary` | `Boolean` |  |  |  |  |  |
| `featureConfig.lensDisableAutoAdmit` | `Boolean` |  |  |  |  |  |
| `featureConfig.studentPermissions` | `<inline-schema>` |  |  |  |  |  |
| `featureConfig.teacherPermissions` | `<inline-schema>` |  |  |  |  |  |
| `featureConfig.languageSettings` | `<inline-schema>` |  |  |  |  |  |
| `featureConfig.enableCustomYTPlayer` | `Boolean` |  |  |  |  |  |
| `featureConfig.enableLensSeeScreen` | `Boolean` |  |  |  |  |  |
| `featureConfig.enableLensTroubleshoot` | `Boolean` |  |  |  |  |  |
| `featureConfig.enableIntegrityCheck` | `Boolean` |  |  |  |  |  |
| `featureConfig.enableParentPortal` | `Boolean` |  |  |  | true |  |
| `featureConfig.enableLoginPin` | `Boolean` |  |  |  |  |  |
| `featureConfig.enablePortalLoginIntegration` | `Boolean` |  |  |  |  |  |
| `featureConfig.hideSignupOnLoginPage` | `Boolean` |  |  |  |  |  |
| `featureConfig.hideContainerApp` | `Boolean` |  |  |  |  |  |
| `featureConfig.disableWiseBranding` | `Boolean` |  |  |  |  |  |
| `featureConfig.disableParticipantUnmute` | `Boolean` |  |  |  |  |  |
| `featureConfig.disableParticipantVideo` | `Boolean` |  |  |  |  |  |
| `featureConfig.parentDrivenSignups` | `Boolean` |  |  |  |  |  |
| `featureConfig.disableStoreOnIOSApp` | `Boolean` |  |  |  |  |  |
| `featureConfig.disableStoreOnAndroidApp` | `Boolean` |  |  |  |  |  |
| `featureConfig.disableCalendarLinking` | `Boolean` |  |  |  |  |  |
| `featureConfig.enableRTL` | `Boolean` |  |  |  | false |  |
| `featureConfig.tracking` | `<inline-schema>` |  |  |  |  |  |
| `displayConfig` | `<displayConfigSchema>` |  |  |  | {} |  |
| `displayConfig.appIconLink` | `String` |  |  |  |  |  |
| `displayConfig.contactEmail` | `String` |  |  |  | 'info@wiseapp.live' |  |
| `displayConfig.contactMobile` | `String` |  |  |  | '+917795206692' |  |
| `displayConfig.androidAppUrl` | `String` |  |  |  |  |  |
| `displayConfig.brandingName` | `String` |  |  |  |  |  |
| `displayConfig.brandingLogo` | `String` |  |  |  |  |  |
| `displayConfig.brandingFavicon` | `String` |  |  |  |  |  |
| `displayConfig.themeConfig` | `<themeConfigSchema>` |  |  |  | {} |  |
| `displayConfig.themeConfig.primaryColor` | `String` |  |  |  |  |  |
| `displayConfig.themeConfig.primaryForegroundColor` | `String` |  |  |  |  |  |
| `displayConfig.siteUrl` | `String` |  |  |  |  |  |
| `displayConfig.portalURL` | `String` |  |  |  |  |  |
| `displayConfig.iosAppUrl` | `String` |  |  |  |  |  |
| `displayConfig.footerString` | `String` |  |  |  | '' |  |
| `displayConfig.tollFreeNumber` | `String` |  |  |  | '' |  |
| `displayConfig.socialLinks` | `Array` |  |  |  | [] |  |
| `displayConfig.faqUrl` | `String` |  |  |  |  |  |
| `displayConfig.tncUrl` | `String` |  |  |  |  |  |
| `displayConfig.privacyPolicyUrl` | `String` |  |  |  |  |  |
| `displayConfig.trialClassId` | `String` |  |  |  | '' |  |
| `displayConfig.defaultCountryCode` | `String` |  |  |  |  |  |
| `displayConfig.homeURL` | `String` |  |  |  |  |  |
| `displayConfig.nameVariables` | `<nameVariablesSchema>` |  |  |  | {} |  |
| `displayConfig.nameVariables.teacher` | `String` |  |  |  |  |  |
| `displayConfig.nameVariables.student` | `String` |  |  |  |  |  |
| `displayConfig.nameVariables.parent` | `String` |  |  |  |  |  |
| `displayConfig.nameVariables.classroom` | `String` |  |  |  |  |  |
| `displayConfig.nameVariables.institute` | `String` |  |  |  |  |  |
| `displayConfig.nameVariables.admin` | `String` |  |  |  |  |  |
| `displayConfig.nameVariables.classroomName` | `String` |  |  |  |  |  |
| `displayConfig.nameVariables.classroomSubject` | `String` |  |  |  |  |  |
| `displayConfig.nameVariables.liveClassroom` | `String` |  |  |  |  |  |
| `displayConfig.nameVariables.oneToOneClassroom` | `String` |  |  |  |  |  |
| `displayConfig.nameVariables.recordedClassroom` | `String` |  |  |  |  |  |
| `displayConfig.nameVariables.session` | `String` |  |  |  |  |  |
| `displayConfig.nameVariables.test` | `String` |  |  |  |  |  |
| `displayConfig.nameVariables.assessment` | `String` |  |  |  |  |  |
| `displayConfig.nameVariables.resource` | `String` |  |  |  |  |  |
| `displayConfig.nameVariables.discussion` | `String` |  |  |  |  |  |
| `displayConfig.nameVariables.content` | `String` |  |  |  |  |  |
| `displayConfig.nameVariables.group` | `String` |  |  |  |  |  |
| `displayConfig.nameVariables.criteria` | `String` |  |  |  |  |  |
| `displayConfig.superAdminHomeURL` | `String` |  |  |  |  |  |
| `displayConfig.lensInMeetingIcon` | `String` |  |  |  |  |  |
| `displayConfig.embeddedClientAppURL` | `String` |  |  |  |  |  |
| `displayConfig.loginBackgroundImage` | `String` |  |  |  |  |  |
| `displayConfig.macAppUrl` | `String` |  |  |  |  |  |
| `displayConfig.windowsAppUrl` | `String` |  |  |  |  |  |
| `systemConfig` | `<systemConfigSchema>` |  |  |  | {} |  |
| `systemConfig.maxLogins` | `Number` |  |  |  |  |  |
| `systemConfig.appHash` | `String` |  |  |  |  |  |
| `systemConfig.customAuthConfig` | `<inline-schema>` |  |  |  |  |  |
| `systemConfig.secureVideoRestrictions` | `<inline-schema>` |  |  |  |  |  |
| `systemConfig.defaultProfilePicture` | `String` |  |  |  |  |  |
| `systemConfig.allowZoomPoolNameOverrideThroughAPI` | `Boolean` |  |  |  |  |  |
| `versionConfig` | `<versionConfigSchema>` |  |  |  | {} |  |
| `versionConfig.android` | `versionSchema` |  |  |  | {} |  |
| `versionConfig.ios` | `versionSchema` |  |  |  | {} |  |
| `versionConfig.mac` | `versionSchema` |  |  |  | {} |  |
| `versionConfig.windows` | `versionSchema` |  |  |  | {} |  |
| `defaultInstituteId` | `ObjectId` | `Institute` |  |  |  |  |
| `metadata` | `Object` |  |  |  |  |  |
| `disabled` | `Boolean` |  |  |  | false |  |
| `disabledAt` | `Date` |  |  |  |  |  |

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
