# Glossary

Business term → canonical table / column. Add entries as you encounter ambiguity.

> **IN / NA deployments:** table references below use IN database names. For NA queries, swap `processed` → `processed_na` and `backend` → `backend_na`. See `CLAUDE.md` for details.

| Term | Means | Where to find it |
| --- | --- | --- |
| _example: active user_ | _user with at least one event in trailing 30d_ | _`views.active_users_30d`_ |
| session | One Zoom meeting on Wise's platform. Holds one license from `start_time` to `end_time`. | `processed.wise_app_backend__zoom` (`_id` = session id) |
| host (of a session) | Teacher who ran a specific zoom session. May differ from class owner for co-taught classes. | `wise_app_backend__zoom.userid` → `processed.user.userid` |
| class owner / primary teacher | Owner of the class entity (not necessarily the host of every session). | `processed.class.userid` → `processed.user.userid` |
| participant (live attendance, collapsed) | Person attending a zoom session. Single entry/exit window per (session, participant) — rejoins are collapsed. | UNNEST `wise_app_backend__zoom.participants[]`; `firstentrytime` / `lastexittime` |
| participant (per-segment join/leave) | Source-of-truth for each rejoin event. `zoom.participants[]` is the aggregated single-window view of these segments. | `wise_app_backend__raw_zoom_attendance.participants[]`; `join_time` / `leave_time` are **ISO strings** (parse with `from_iso8601_timestamp`) |
| attendance summary | Per (session, participant) duration + attendance %. Cheapest route for who-attended-what and session-level license concurrency (typed timestamps, no JSON parsing). | `processed.zoom_attendance` |
| missed session | Session that never ran. Lives in a separate table — does **not** appear in `zoom_attendance`. | `processed.zoom_missed_attendance` |
| active student of an institute | `institute_participants` row with `relation = 'STUDENT' AND status = 'ACCEPTED'`. Excludes `REMOVED` (left/kicked) and `REQUESTED` (pending). | `processed.institute_participants` |
| registration form answer | One row per `(institute, user, question)`. Pivot with `MAX(IF(questiontext = 'X', answer))` to get one row per student. | `processed.student_registration_form` |
| POLL answer (gotcha) | Stores the **option id** (e.g. `A`, `B`), not the option label. Resolve via `wise_app_backend__registration_form.fields[].options[]`. | `student_registration_form.questiontype = 'POLL'` |
| namespace | Tenant identifier. Can span multiple institutes within the same customer (e.g. `leadiasacademy` → Lead IAS, Lead Junior, Lead Junior Telugu, Lead IAS Junior Int'l). | `class.namespace`, `user.namespace`, `institute.namespace` |
| institute | A specific brand / branch within a tenant namespace. | `processed.institute` (joined via `class.instituteid`) |
| zoom license in use | 1 license = 1 running session at an instant. Concurrency = sessions whose `[start_time, end_time)` covers that instant. | Sweep-line on `wise_app_backend__zoom` |
| past session | Sessions that actually ran and ended. Filter `meetingstatus = 'ENDED'` — `end_time` is set to the actual end. `end_time IS NULL` means the session **never started** (missed), not "currently live". | `wise_app_backend__zoom.meetingstatus` / `end_time` |
| class (vocabulary warning) | Ambiguous — can mean the **recurring class entity** (`processed.class`) OR a **single live session / occurrence** (`processed.wise_app_backend__zoom`). Always confirm which sense the user wants. Sessions = time/attendance/duration; class entity = enrollment/schedule/ownership. | both tables |
| Wise-pool license vs BYO | Filter `metadata.zoomadminaccountid` against Wise's pool to scope to Wise-owned licenses (vs customers' own Zoom accounts). | `wise_app_backend__zoom.metadata.zoomadminaccountid` |
| license-consuming session | Excludes `type = 'OFFLINE'` and `meetingstatus IN ('CANCELLED','MISSED')` — those don't hold a license. | `wise_app_backend__zoom.type` / `meetingstatus` |
| AI summary (of a session) | LLM-generated meeting summary (title / overview / detail sections). Row may exist with an **empty** array — gate on `summaries <> '[]'`. | `processed.wise_app_backend__rawzoomsummary`; flattened in `processed.zoom_summaries` |
| session transcript | VTT transcript file(s) for a session, one per part/segment. Row may exist with an **empty** array — gate on `files <> '[]'`. | `processed.wise_app_backend__rawsessiontranscript` |
| AI revision notes / quizzes | Post-session AI study artifacts. Distinct from summary and transcript. | `processed.wise_app_backend__session_ai_data` |
| session with AI artifacts | Session having a non-empty summary **or** transcript. The three AI tables are independent; a session can have any subset. Summary coverage consistently exceeds transcript coverage. | join the three tables on `sessionid` (`$oid`) = session id |
| active teacher (of a tenant) | Distinct user who hosted >=1 `ENDED` session in the window. Used to size a setup, e.g. to exclude tenants under N teachers. | `zoomers_v3.userid` (row=1, meetingstatus='ENDED') -> `user.namespace` |
| non-human tutor name (gotcha) | Several large tenants name teacher accounts after the org, a class slot, or a roster id rather than a person: `tutoroot` (`Tutoroot tech faculty`), `toprankers` (`Toprankers_5429232`), `k8school` (`TWO B TEACHER`, `Grade Eight Personalized`). `wise-demo` seeds many accounts sharing one human-looking name. Filter these out of per-teacher metrics. | `processed.user.name`; see `examples/tutors_with_ai_artifacts_wow.sql` |
