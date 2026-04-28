---
collection: "Whitelabel"
athena_table: "wise_app_backend__whitelabel"
mongo_field_count: 99
athena_field_count: 94
matched: 56
coverage_pct: 56.6
last_diffed: "2026-04-28T11:07:30+00:00"
---

# Schema gap: `Whitelabel` ↔ `processed.wise_app_backend__whitelabel`

- **Mongo source**: [`src/models/Whitelabel.js`](../source/mongo/Whitelabel.md)
- **Athena counterpart**: [`schemas/processed/processed/wise_app_backend__whitelabel.md`](../processed/processed/wise_app_backend__whitelabel.md)
- **Coverage**: 56/99 Mongo fields are present in Athena (**56.6%**).

## In Mongo, missing from Athena

These fields are declared in the Mongoose schema but the Athena lake pipeline doesn't expose them. Either widen the extractor or note the field as JSON-only inside an existing varchar column.

| Path | Type | Ref | Required |
| --- | --- | --- | --- |
| `featureConfig.disableAppleLogin` | `Boolean` |  |  |
| `featureConfig.enableLens` | `Boolean` |  |  |
| `featureConfig.disableRedirectToPrimary` | `Boolean` |  |  |
| `featureConfig.lensDisableAutoAdmit` | `Boolean` |  |  |
| `featureConfig.studentPermissions` | `<inline-schema>` |  |  |
| `featureConfig.teacherPermissions` | `<inline-schema>` |  |  |
| `featureConfig.languageSettings` | `<inline-schema>` |  |  |
| `featureConfig.enableCustomYTPlayer` | `Boolean` |  |  |
| `featureConfig.enableLensSeeScreen` | `Boolean` |  |  |
| `featureConfig.enableLensTroubleshoot` | `Boolean` |  |  |
| `featureConfig.enableIntegrityCheck` | `Boolean` |  |  |
| `featureConfig.enableLoginPin` | `Boolean` |  |  |
| `featureConfig.enablePortalLoginIntegration` | `Boolean` |  |  |
| `featureConfig.hideSignupOnLoginPage` | `Boolean` |  |  |
| `featureConfig.hideContainerApp` | `Boolean` |  |  |
| `featureConfig.disableWiseBranding` | `Boolean` |  |  |
| `featureConfig.disableParticipantUnmute` | `Boolean` |  |  |
| `featureConfig.disableParticipantVideo` | `Boolean` |  |  |
| `featureConfig.parentDrivenSignups` | `Boolean` |  |  |
| `featureConfig.disableStoreOnIOSApp` | `Boolean` |  |  |
| `featureConfig.disableStoreOnAndroidApp` | `Boolean` |  |  |
| `featureConfig.disableCalendarLinking` | `Boolean` |  |  |
| `featureConfig.enableRTL` | `Boolean` |  |  |
| `featureConfig.tracking` | `<inline-schema>` |  |  |
| `displayConfig.themeConfig` | `<themeConfigSchema>` |  |  |
| `displayConfig.themeConfig.primaryColor` | `String` |  |  |
| `displayConfig.themeConfig.primaryForegroundColor` | `String` |  |  |
| `displayConfig.portalURL` | `String` |  |  |
| `displayConfig.iosAppUrl` | `String` |  |  |
| `displayConfig.tncUrl` | `String` |  |  |
| `displayConfig.defaultCountryCode` | `String` |  |  |
| `displayConfig.homeURL` | `String` |  |  |
| `displayConfig.superAdminHomeURL` | `String` |  |  |
| `displayConfig.lensInMeetingIcon` | `String` |  |  |
| `displayConfig.embeddedClientAppURL` | `String` |  |  |
| `displayConfig.loginBackgroundImage` | `String` |  |  |
| `displayConfig.macAppUrl` | `String` |  |  |
| `displayConfig.windowsAppUrl` | `String` |  |  |
| `systemConfig.secureVideoRestrictions` | `<inline-schema>` |  |  |
| `systemConfig.defaultProfilePicture` | `String` |  |  |
| `systemConfig.allowZoomPoolNameOverrideThroughAPI` | `Boolean` |  |  |
| `metadata` | `Object` |  |  |
| `disabledAt` | `Date` |  |  |

## In Athena, missing from Mongo

These fields exist in the Athena table but aren't declared in the current Mongoose schema. Likely renamed / deprecated, or added by the lake pipeline (timestamps, flattened helpers).

| Path | Type | Source |
| --- | --- | --- |
| `additionalconfig` | `string` | column |
| `_id.$oid` | `string` | JSON path |
| `featureconfig.disablefees` | `bool` | JSON path |
| `hostnames.[]` | `string` | JSON path |
| `displayconfig.sociallinks.sociallinks[].link` | `string` | JSON path |
| `displayconfig.sociallinks.sociallinks[].type` | `string` | JSON path |
| `__v.$numberint` | `string` | JSON path |
| `createdat.$date` | `object` | JSON path |
| `createdat.$date.$numberlong` | `string` | JSON path |
| `updatedat.$date` | `object` | JSON path |
| `updatedat.$date.$numberlong` | `string` | JSON path |
| `versionconfig.android.latestbuildnumber` | `object` | JSON path |
| `versionconfig.android.latestbuildnumber.$numberint` | `string` | JSON path |
| `versionconfig.android.minbuildnumber` | `object` | JSON path |
| `versionconfig.android.minbuildnumber.$numberint` | `string` | JSON path |
| `versionconfig.ios.latestbuildnumber` | `object` | JSON path |
| `versionconfig.ios.latestbuildnumber.$numberint` | `string` | JSON path |
| `versionconfig.ios.minbuildnumber` | `object` | JSON path |
| `versionconfig.ios.minbuildnumber.$numberint` | `string` | JSON path |
| `versionconfig.mac.latestbuildnumber` | `object` | JSON path |
| `versionconfig.mac.latestbuildnumber.$numberint` | `string` | JSON path |
| `versionconfig.mac.minbuildnumber` | `object` | JSON path |
| `versionconfig.mac.minbuildnumber.$numberint` | `string` | JSON path |
| `versionconfig.windows.latestbuildnumber` | `object` | JSON path |
| `versionconfig.windows.latestbuildnumber.$numberint` | `string` | JSON path |
| `versionconfig.windows.minbuildnumber` | `object` | JSON path |
| `versionconfig.windows.minbuildnumber.$numberint` | `string` | JSON path |
| `defaultinstituteid.$oid` | `string` | JSON path |
