# Backend-API usage patterns

_Static-extracted from `wise/backend-api/src/{controllers,services,repositories,workers,helpers}/**/*.js`._

Scanned 171 JS files. Per-collection details live in `schemas/source/mongo/<collection>.md` under `## Usage`.

## Models ranked by call-site count

Higher = the model is touched more often by application code, so its Athena table is more likely to be a hot query target.

| Collection | Total calls | Distinct files | Top method | Top populate field |
| --- | ---: | ---: | --- | --- |
| `class` | 224 | 60 | `.findOne` ×101 | `userId` ×12 |
| `user` | 213 | 57 | `.findOne` ×109 | `parentIds` ×1 |
| `zoom` | 174 | 45 | `.findOne` ×56 | `classId` ×9 |
| `transaction` | 133 | 22 | `.findOne` ×35 | `senderId` ×2 |
| `InstituteParticipant` | 91 | 26 | `.findOne` ×27 | `userId` ×17 |
| `ClassParticipant` | 77 | 31 | `.find` ×27 | `userId` ×17 |
| `Institute` | 65 | 29 | `.findOne` ×31 | `ownerId` ×9 |
| `assignments` | 49 | 17 | `.findOne` ×12 | `userId` ×1 |
| `announcements` | 47 | 16 | `.aggregate` ×12 | `classId` ×2 |
| `PremiumOrder` | 44 | 10 | `.findOne` ×18 |  |
| `LiveClassInsight` | 41 | 9 | `.findOne` ×19 | `sessionId` ×1 |
| `ClassroomSection` | 40 | 9 | `.find` ×8 | `classId` ×1 |
| `ClassroomFee` | 37 | 14 | `.findOne` ×22 | `classId` ×1 |
| `study materials` | 34 | 13 | `.findOne` ×8 | `userId` ×1 |
| `Entity` | 25 | 8 | `.findOneAndUpdate` ×8 |  |
| `LinkedGoogleCalendar` | 21 | 6 | `.findOne` ×7 |  |
| `SessionFeedbackSubmission` | 21 | 10 | `.find` ×7 | `sessionId` ×2 |
| `Whitelabel` | 20 | 5 | `.updateOne` ×7 |  |
| `UserStreamingInfo` | 18 | 7 | `.findOne` ×6 | `userId` ×1 |
| `InstitutePublicProfile` | 17 | 6 | `.findOne` ×4 |  |
| `Chat` | 17 | 4 | `.find` ×4 |  |
| `RegistrationForm` | 16 | 9 | `.findOne` ×15 |  |
| `VendorIntegration` | 15 | 9 | `.findOne` ×5 |  |
| `VendorConfiguration` | 15 | 5 | `.findOne` ×7 |  |
| `WorkingHoursSchedule` | 14 | 4 | `.findOne` ×4 |  |
| `LiveClassPoll` | 14 | 1 | `.updateMany` ×4 |  |
| `LensRoomConfig` | 13 | 6 | `.findOne` ×7 | `agendaIds` ×2 |
| `InstituteGroupMember` | 13 | 5 | `.find` ×5 |  |
| `GoogleCalendarEvent` | 13 | 4 | `.find` ×8 | `sessionId` ×2 |
| `ManualAttendance` | 12 | 3 | `.findOne` ×7 | `sessionId` ×1 |
| `LiveClassDiscussion` | 12 | 2 | `.findOneAndUpdate` ×5 |  |
| `Coupon` | 12 | 2 | `.findOne` ×6 |  |
| `Contract` | 11 | 5 | `.findOne` ×5 |  |
| `FeedbackForm` | 11 | 6 | `.findOne` ×4 |  |
| `liveclassagendas` | 11 | 3 | `.findOne` ×5 |  |
| `ChessGame` | 11 | 1 | `.findOne` ×5 |  |
| `SessionCredit` | 10 | 5 | `.updateOne` ×2 |  |
| `InstituteGroup` | 10 | 3 | `.findOne` ×5 |  |
| `PollVote` | 9 | 7 | `.deleteMany` ×3 | `userId` ×1 |
| `ClassroomCertificate` | 9 | 6 | `.find` ×3 | `certificateConfigId` ×1 |
| `LiveClassTest` | 9 | 1 | `.findOne` ×3 | `questions` ×1 |
| `ContractSubmission` | 8 | 4 | `.find` ×4 |  |
| `ClassroomPublicProfile` | 8 | 5 | `.findOne` ×3 |  |
| `ClassroomCertificateConfig` | 8 | 4 | `.find` ×2 | `templateId` ×2 |
| `LiveClassLeaderboard` | 8 | 2 | `.findOneAndUpdate` ×3 |  |
| `EntityInteraction` | 8 | 4 | `.insertMany` ×3 |  |
| `userPreference` | 7 | 2 | `.findOne` ×4 |  |
| `InstituteLeaderboardConfig` | 7 | 5 | `.findOne` ×3 | `instituteId` ×1 |
| `TeacherLeave` | 7 | 3 | `.find` ×5 |  |
| `TaxRuleGroup` | 7 | 2 | `.exists` ×3 |  |
| `verification` | 7 | 1 | `.updateOne` ×3 |  |
| `PencilSpaceEntity` | 7 | 2 | `.create` ×3 |  |
| `Leaderboard` | 7 | 3 | `.aggregate` ×2 | `classId` ×1 |
| `ChatMessage` | 7 | 4 | `.deleteMany` ×3 |  |
| `SessionAIData` | 7 | 1 | `.updateOne` ×3 |  |
| `SavedCommunication` | 6 | 3 | `.aggregate` ×2 | `classId` ×1 |
| `EmailSupression` | 6 | 5 | `.updateOne` ×2 |  |
| `RawRecording` | 6 | 4 | `.findOne` ×3 |  |
| `VideoKeyRecord` | 6 | 4 | `.findOne` ×2 |  |
| `TempData` | 6 | 2 | `.findOne` ×2 |  |
| `RegistrationFormSubmission` | 6 | 2 | `.updateMany` ×2 |  |
| `Lead` | 5 | 5 | `.findOne` ×3 |  |
| `InstituteTags` | 5 | 2 | `.findOne` ×2 |  |
| `InstituteLocations` | 5 | 2 | `.findOne` ×2 |  |
| `DeletedFile` | 5 | 3 | `.updateOne` ×3 |  |
| `RawZoomAttendance` | 4 | 2 | `.findOne` ×3 |  |
| `temp_user` | 4 | 1 | `.findOne` ×2 |  |
| `RawZoomSummary` | 3 | 3 | `.findOne` ×1 |  |
| `TeacherPublicProfile` | 3 | 2 | `.findOne` ×1 |  |
| `RawSessionTranscript` | 2 | 2 | `.findOne` ×2 |  |
| `CertificateTemplate` | 2 | 2 | `.find` ×1 |  |
| `Event` | 2 | 1 | `.findOneAndUpdate` ×1 |  |
| `RawChat` | 1 | 1 | `.findOne` ×1 |  |
| `Sequence` | 1 | 1 | `.findOneAndUpdate` ×1 |  |

## Most-populated fields globally

Tells you which `populate(...)` paths are hot across the codebase — these are the joins Claude should know to write proactively in Athena SQL.

- `userId` × 56
- `classId` × 17
- `instituteId` × 15
- `ownerId` × 9
- `sessionId` × 6
- `senderId` × 2
- `coTeachers` × 2
- `agendaIds` × 2
- `templateId` × 2
- `receiverId` × 1
- `joinedRequest` × 1
- `zoomLink.sessionId` × 1
- `certificateConfigId` × 1
- `parentIds` × 1
- `questions` × 1
