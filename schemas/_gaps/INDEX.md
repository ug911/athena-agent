# Schema gaps — Mongo ↔ Athena

_Last diffed: 2026-09-08T08:05:41+00:00_

Coverage = fraction of Mongoose fields that have a counterpart in the Athena table for that collection. Lower = more extraction debt.

| Collection | Athena table | Coverage | Missing in Athena | Extra in Athena | Missing field paths |
| --- | --- | ---: | ---: | ---: | --- |
| [`class`](class.md) | `wise_app_backend__class` | 50% (48/96) | 48 | 42 | `description`, `slug`, `classCovers`, `zoomLink.sessionId`, `zoomLink.meetingStarted`, `zoomLink.provider`, `zoomLink.metadata`, `hidden`, `archivedAt`, `dataDeleted`, `thumbnail`, `settings.studentSlotBooking`, _+36 more_ |
| [`LiveClassInsight`](LiveClassInsight.md) | `wise_app_backend__liveclassinsight` | 36% (24/66) | 42 | 22 | `meetingStartedWebhookReceivedAt`, `hostLensRegisteredAt`, `classId`, `participants[].firstEntryTime`, `participants[].lastExitTime`, `agendas[]`, `agendas[].title`, `agendas[].description`, `agendas[].tags`, `agendas[].visibleTags`, `agendas[].agendaItems`, `tempData`, _+30 more_ |
| [`Whitelabel`](Whitelabel.md) | `wise_app_backend__whitelabel` | 76% (75/99) | 24 | 45 | `featureConfig.disableRedirectToPrimary`, `featureConfig.lensDisableAutoAdmit`, `featureConfig.studentPermissions`, `featureConfig.teacherPermissions`, `featureConfig.languageSettings`, `featureConfig.enableLensSeeScreen`, `featureConfig.enableIntegrityCheck`, `featureConfig.enablePortalLoginIntegration`, `featureConfig.hideSignupOnLoginPage`, `featureConfig.hideContainerApp`, `featureConfig.parentDrivenSignups`, `featureConfig.disableStoreOnIOSApp`, _+12 more_ |
| [`user`](user.md) | `wise_app_backend__user` | 68% (41/60) | 19 | 43 | `activated`, `integrations`, `parentIds`, `permissions`, `deleted`, `publicProfile.subdomain`, `publicProfile.publishedAt`, `publicProfile.bio`, `publicProfile.title`, `publicProfile.logoURL`, `publicProfile.introVideo`, `publicProfile.experience`, _+7 more_ |
| [`assignments`](assignments.md) | `wise_app_backend__assignments` | 71% (32/45) | 13 | 61 | `criteria[].title`, `submission[].textAnswer`, `submission[].criteriaFeedback[]`, `submission[].criteriaFeedback[].criteriaId`, `submission[].criteriaFeedback[].marks`, `submission[].submissionFile`, `submission[].submissionFile.fileId`, `submission[].submissionFile.name`, `lastCommentedAt`, `pending`, `googleDocFile`, `googleDocFile.fileId`, _+1 more_ |
| [`zoom`](zoom.md) | `wise_app_backend__zoom` | 85% (73/86) | 13 | 67 | `provider`, `attendees`, `lastCommentedAt`, `public`, `recordingsCaptured`, `recordingUnsharedAt`, `thumbnail`, `description`, `privateNote`, `streamingData`, `streamingData.streamingKey`, `streamingData.streamingURL`, _+1 more_ |
| [`announcements`](announcements.md) | `wise_app_backend__announcements` | 54% (14/26) | 12 | 30 | `canEdit`, `canDelete`, `pollData.question`, `pollData.options`, `pollData.correctAnswer`, `pollData.endsAt`, `pollData.showResults`, `pollData.stats`, `pollData.voteCount`, `public`, `thumbnail`, `metadata` |
| [`Institute`](Institute.md) | `wise_app_backend__institute` | 91% (122/134) | 12 | 99 | `profilePicture`, `coverPicture`, `instituteCode`, `settings.disableRecordingProcessing`, `settings.lensFeedbackAnonymous`, `settings.feeSettings.enableSplitPayments`, `settings.feeSettings.disableSuspension`, `settings.skipRecordingHLSEncryption`, `settings.sessionSettings.unpaidFeesSessionCancellationDays`, `settings.localeSettings.calendarStartDay`, `settings.showLearnerContactToTeacher`, `settings.participantContractVisibility` |
| [`VendorConfiguration`](VendorConfiguration.md) | `wise_app_backend__vendor_configuration` | 53% (10/19) | 9 | 10 | `apiAccess`, `apiAccess.apiKeys`, `s3Configuration`, `s3Configuration.accessKeyId`, `s3Configuration.secretAccessKey`, `s3Configuration.region`, `s3Configuration.bucketName`, `s3Configuration.pathPrefix`, `s3Configuration.aclConfig` |
| [`PremiumOrder`](PremiumOrder.md) | `wise_app_backend__premium_order` | 57% (12/21) | 9 | 25 | `planDescription`, `metadata`, `streamingGBs`, `storageGBs`, `commsCredits`, `planMetadata.baseAmount`, `planMetadata.domesticTransactionFee`, `planMetadata.internationalTransactionFee`, `planMetadata.storageGBs` |
| [`UserStreamingInfo`](UserStreamingInfo.md) | `wise_app_backend__user_streaming_info` | 58% (11/19) | 8 | 17 | `storageUsage[]`, `storageUsage[].consumedGBs`, `communicationUsage[]`, `communicationUsage[].whatsapp`, `communicationUsage[].email`, `communicationUsage[].creditsUsed`, `communicationUsage[].creditsRemaining`, `totalCreditsUsed` |
| [`DeletedFile`](DeletedFile.md) | `wise_app_backend__deleted_file` | 30% (3/10) | 7 | 15 | `failed`, `error`, `skippedDeletion`, `classId`, `entityId`, `deletedAt`, `skipValidation` |
| [`study materials`](study_materials.md) | `wise_app_backend__study_materials` | 72% (18/25) | 7 | 40 | `resources[].link`, `resources[].metadata`, `link`, `disableCommenting`, `public`, `thumbnail`, `metadata` |
| [`SavedCommunication`](SavedCommunication.md) | `wise_app_backend__saved_communication` | 45% (5/11) | 6 | 9 | `instituteId`, `classId`, `notificationId`, `customIntegration`, `title`, `statusMetadata` |
| [`ClassroomSection`](ClassroomSection.md) | `wise_app_backend__classroom_section` | 50% (6/12) | 6 | 10 | `entities[].public`, `dripSettings`, `dripSettings.enableDaysAfter`, `dripSettings.enableOn`, `sequentialLearning`, `other` |
| [`ClassParticipant`](ClassParticipant.md) | `wise_app_backend__classparticipant` | 50% (5/10) | 5 | 10 | `metadata`, `metadata.paymentOptionId`, `metadata.settleDues`, `metadata.feesWaived`, `metadata.payoutSettings` |
| [`SessionFeedbackSubmission`](SessionFeedbackSubmission.md) | `wise_app_backend__session_feedback_submission` | 69% (11/16) | 5 | 11 | `unauthUserId`, `answers[].questionText`, `answers[].type`, `answers[].options`, `answers[].answer` |
| [`RawChat`](RawChat.md) | `wise_app_backend__raw_chat` | 43% (3/7) | 4 | 12 | `files[]`, `files[].sessionIndex`, `files[].meetingUUID`, `files[].file` |
| [`ClassroomPublicProfile`](ClassroomPublicProfile.md) | `wise_app_backend__classroom_public_profile` | 56% (5/9) | 4 | 11 | `highlights`, `highlights.points`, `public`, `reviews` |
| [`transaction`](transaction.md) | `wise_app_backend__transaction` | 76% (13/17) | 4 | 45 | `lineItems[]`, `preTaxAmount`, `taxLineItems[]`, `taxLineItems[].description` |
| [`temp_user`](temp_user.md) | `wise_app_backend__temp_user` | 0% (0/3) | 3 | 3 | `identifier`, `idType`, `metadata` |
| [`userPreference`](userPreference.md) | `wise_app_backend__userpreference` | 40% (2/5) | 3 | 8 | `posts[]`, `posts[].entityId`, `posts[].entityType` |
| [`verification`](verification.md) | `wise_app_backend__verification` | 67% (6/9) | 3 | 11 | `identifier`, `idType`, `ip` |
| [`RegistrationFormSubmission`](RegistrationFormSubmission.md) | `wise_app_backend__registration_form_submission` | 67% (4/6) | 2 | 11 | `classId`, `sessionId` |
| [`SessionCredit`](SessionCredit.md) | `wise_app_backend__session_credit` | 75% (6/8) | 2 | 11 | `instituteId`, `metadata` |
| [`EntityInteraction`](EntityInteraction.md) | `wise_app_backend__entity_interaction` | 78% (7/9) | 2 | 12 | `markedCovered`, `metadata` |
| [`ChessGame`](ChessGame.md) | `wise_app_backend__chess_game` | 93% (26/28) | 2 | 15 | `startFEN`, `duration` |
| [`Event`](Event.md) | `wise_app_backend__event` | 80% (4/5) | 1 | 151 | `expiresAt` |
| [`VendorIntegration`](VendorIntegration.md) | `wise_app_backend__vendorintegration` | 80% (4/5) | 1 | 47 | `whitelabelNamespace` |
| [`RegistrationForm`](RegistrationForm.md) | `wise_app_backend__registration_form` | 86% (6/7) | 1 | 26 | `classId` |
| [`GoogleCalendarEvent`](GoogleCalendarEvent.md) | `wise_app_backend__googlecalendarevent` | 88% (7/8) | 1 | 11 | `linkedGoogleCalendarId` |
| [`RawRecording`](RawRecording.md) | `wise_app_backend__raw_recording` | 88% (7/8) | 1 | 13 | `expiresIn` |
| [`WorkingHoursSchedule`](WorkingHoursSchedule.md) | `wise_app_backend__working_hours_schedule` | 88% (7/8) | 1 | 9 | `classId` |
| [`Entity`](Entity.md) | `wise_app_backend__entity` | 89% (8/9) | 1 | 9 | `entitySecondaryId` |
| [`LiveClassTest`](LiveClassTest.md) | `wise_app_backend__liveclasstest` | 92% (11/12) | 1 | 16 | `duration` |
| [`LiveClassPoll`](LiveClassPoll.md) | `wise_app_backend__live_class_poll` | 96% (24/25) | 1 | 28 | `duration` |
| [`InstituteGroup`](InstituteGroup.md) | `wise_app_backend__institutegroup` | 100% (3/3) | 0 | 6 |  |
| [`InstituteGroupMember`](InstituteGroupMember.md) | `wise_app_backend__institutegroupmember` | 100% (3/3) | 0 | 7 |  |
| [`PollVote`](PollVote.md) | `wise_app_backend__pollvote` | 100% (3/3) | 0 | 8 |  |
| [`tags`](tags.md) | `wise_app_backend__tags` | 100% (3/3) | 0 | 1 |  |
| [`ChatMessage`](ChatMessage.md) | `wise_app_backend__chatmessage` | 100% (4/4) | 0 | 17 |  |
| [`LensEvent`](LensEvent.md) | `wise_app_backend__lens_event` | 100% (4/4) | 0 | 11 |  |
| [`LiveClassLeaderboard`](LiveClassLeaderboard.md) | `wise_app_backend__live_class_leaderboard` | 100% (4/4) | 0 | 18 |  |
| [`ClassroomCertificate`](ClassroomCertificate.md) | `wise_app_backend__classroom_certificate` | 100% (5/5) | 0 | 9 |  |
| [`Lead`](Lead.md) | `wise_app_backend__lead` | 100% (5/5) | 0 | 7 |  |
| [`RawZoomAttendance`](RawZoomAttendance.md) | `wise_app_backend__raw_zoom_attendance` | 100% (6/6) | 0 | 26 |  |
| [`RawZoomSummary`](RawZoomSummary.md) | `wise_app_backend__rawzoomsummary` | 100% (6/6) | 0 | 11 |  |
| [`TeacherLeave`](TeacherLeave.md) | `wise_app_backend__teacher_leave` | 100% (6/6) | 0 | 12 |  |
| [`Chat`](Chat.md) | `wise_app_backend__chat` | 100% (7/7) | 0 | 12 |  |
| [`ClassroomCertificateConfig`](ClassroomCertificateConfig.md) | `wise_app_backend__classroom_certificate_config` | 100% (7/7) | 0 | 9 |  |
| [`RawSessionTranscript`](RawSessionTranscript.md) | `wise_app_backend__rawsessiontranscript` | 100% (7/7) | 0 | 18 |  |
| [`feeStructure`](feeStructure.md) | `wise_app_backend__feestructure` | 100% (7/7) | 0 | 15 |  |
| [`FeedbackForm`](FeedbackForm.md) | `wise_app_backend__feedback_form` | 100% (9/9) | 0 | 11 |  |
| [`InstituteLeaderboardConfig`](InstituteLeaderboardConfig.md) | `wise_app_backend__institute_leaderboard_config` | 100% (9/9) | 0 | 12 |  |
| [`ManualAttendance`](ManualAttendance.md) | `wise_app_backend__manualattendance` | 100% (11/11) | 0 | 12 |  |
| [`LiveClassDiscussion`](LiveClassDiscussion.md) | `wise_app_backend__live_class_discussion` | 100% (14/14) | 0 | 17 |  |
| [`CertificateTemplate`](CertificateTemplate.md) | `wise_app_backend__certificate_template` | 100% (15/15) | 0 | 10 |  |
| [`InstitutePublicProfile`](InstitutePublicProfile.md) | `wise_app_backend__institute_public_profile` | 100% (17/17) | 0 | 28 |  |
| [`Leaderboard`](Leaderboard.md) | `wise_app_backend__leaderboard` | 100% (18/18) | 0 | 77 |  |
| [`LensRoomConfig`](LensRoomConfig.md) | `wise_app_backend__lens_room_config` | 100% (19/19) | 0 | 30 |  |

## Mongo collections with no Athena counterpart

- `ClassroomFee`
- `Contract`
- `ContractSubmission`
- `Coupon`
- `EmailSupression`
- `InstituteLocations`
- `InstituteParticipant`
- `InstituteTags`
- `LinkedGoogleCalendar`
- `PencilSpaceEntity`
- `Sequence`
- `SessionAIData`
- `TaxRuleGroup`
- `TeacherPublicProfile`
- `TempData`
- `VideoKeyRecord`

These collections exist in code but aren't (yet?) flowing to Athena. Confirm with the data-lake owners whether they should be ingested.