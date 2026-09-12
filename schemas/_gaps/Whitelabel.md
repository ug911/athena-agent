---
collection: "Whitelabel"
athena_table: "wise_app_backend__whitelabel"
mongo_field_count: 99
athena_field_count: 134
matched: 75
coverage_pct: 75.8
last_diffed: "2026-09-08T08:05:41+00:00"
---

# Schema gap: `Whitelabel` ↔ `processed.wise_app_backend__whitelabel`

- **Mongo source**: [`src/models/Whitelabel.js`](../source/mongo/Whitelabel.md)
- **Athena counterpart**: [`schemas/processed/processed/wise_app_backend__whitelabel.md`](../processed/processed/wise_app_backend__whitelabel.md)
- **Coverage**: 75/99 Mongo fields are present in Athena (**75.8%**).

## In Mongo, missing from Athena

These fields are declared in the Mongoose schema but the Athena lake pipeline doesn't expose them. Either widen the extractor or note the field as JSON-only inside an existing varchar column.

| Path | Type | Ref | Required |
| --- | --- | --- | --- |
| `featureConfig.disableRedirectToPrimary` | `Boolean` |  |  |
| `featureConfig.lensDisableAutoAdmit` | `Boolean` |  |  |
| `featureConfig.studentPermissions` | `<inline-schema>` |  |  |
| `featureConfig.teacherPermissions` | `<inline-schema>` |  |  |
| `featureConfig.languageSettings` | `<inline-schema>` |  |  |
| `featureConfig.enableLensSeeScreen` | `Boolean` |  |  |
| `featureConfig.enableIntegrityCheck` | `Boolean` |  |  |
| `featureConfig.enablePortalLoginIntegration` | `Boolean` |  |  |
| `featureConfig.hideSignupOnLoginPage` | `Boolean` |  |  |
| `featureConfig.hideContainerApp` | `Boolean` |  |  |
| `featureConfig.parentDrivenSignups` | `Boolean` |  |  |
| `featureConfig.disableStoreOnIOSApp` | `Boolean` |  |  |
| `featureConfig.disableStoreOnAndroidApp` | `Boolean` |  |  |
| `featureConfig.disableCalendarLinking` | `Boolean` |  |  |
| `featureConfig.enableRTL` | `Boolean` |  |  |
| `featureConfig.tracking` | `<inline-schema>` |  |  |
| `displayConfig.themeConfig` | `<themeConfigSchema>` |  |  |
| `displayConfig.themeConfig.primaryColor` | `String` |  |  |
| `displayConfig.themeConfig.primaryForegroundColor` | `String` |  |  |
| `displayConfig.tncUrl` | `String` |  |  |
| `displayConfig.embeddedClientAppURL` | `String` |  |  |
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
| `featureconfig.enablesociallogin` | `bool` | JSON path |
| `hostnames.[]` | `string` | JSON path |
| `adminuserids.[]` | `string` | JSON path |
| `displayconfig.namevariables.invoice` | `string` | JSON path |
| `displayconfig.namevariables.store` | `string` | JSON path |
| `displayconfig.sociallinks.sociallinks[].link` | `string` | JSON path |
| `displayconfig.sociallinks.sociallinks[].type` | `string` | JSON path |
| `__v.$numberint` | `string` | JSON path |
| `createdat.$date` | `object` | JSON path |
| `createdat.$date.$numberlong` | `string` | JSON path |
| `updatedat.$date` | `object` | JSON path |
| `updatedat.$date.$numberlong` | `string` | JSON path |
| `versionconfig.android.latestbuildnumber` | `object` | JSON path |
| `versionconfig.android.latestbuildnumber.$numberint` | `string` | JSON path |
| `versionconfig.android.latestbuildnumber.$numberlong` | `string` | JSON path |
| `versionconfig.android.latestversionname` | `string` | JSON path |
| `versionconfig.android.minbuildnumber` | `object` | JSON path |
| `versionconfig.android.minbuildnumber.$numberint` | `string` | JSON path |
| `versionconfig.android.minbuildnumber.$numberlong` | `string` | JSON path |
| `versionconfig.ios.latestbuildnumber` | `object` | JSON path |
| `versionconfig.ios.latestbuildnumber.$numberint` | `string` | JSON path |
| `versionconfig.ios.latestversionname` | `string` | JSON path |
| `versionconfig.ios.minbuildnumber` | `object` | JSON path |
| `versionconfig.ios.minbuildnumber.$numberint` | `string` | JSON path |
| `versionconfig.mac.latestbuildnumber` | `object` | JSON path |
| `versionconfig.mac.latestbuildnumber.$numberint` | `string` | JSON path |
| `versionconfig.mac.latestbuildnumber.$numberlong` | `string` | JSON path |
| `versionconfig.mac.minbuildnumber` | `object` | JSON path |
| `versionconfig.mac.minbuildnumber.$numberint` | `string` | JSON path |
| `versionconfig.windows.latestbuildnumber` | `object` | JSON path |
| `versionconfig.windows.latestbuildnumber.$numberint` | `string` | JSON path |
| `versionconfig.windows.latestbuildnumber.$numberlong` | `string` | JSON path |
| `versionconfig.windows.latestversionname` | `string` | JSON path |
| `versionconfig.windows.minbuildnumber` | `object` | JSON path |
| `versionconfig.windows.minbuildnumber.$numberint` | `string` | JSON path |
| `systemconfig.customauthconfig.jwttokensecret` | `string` | JSON path |
| `systemconfig.maxlogins.$numberint` | `string` | JSON path |
| `systemconfig.securevideorestrictions.enforcesecureapp` | `bool` | JSON path |
| `customauthconfig.jwttokensecret` | `string` | JSON path |
| `defaultinstituteid.$oid` | `string` | JSON path |
| `maxlogins.$numberint` | `string` | JSON path |
| `additionalconfig.ytplayer` | `bool` | JSON path |
