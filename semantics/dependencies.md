# View dependency graph

_Auto-generated from view DDLs in `schemas/`. 45 views parsed._

## Forward (view → tables it reads)

### `processed.announcements`
- `processed.wise_app_backend__announcements`

### `processed.assignments`
- `processed.wise_app_backend__assignments`

### `processed.class`
- `processed.wise_app_backend__class`

### `processed.class_participants`
- `processed.wise_app_backend__classparticipant`

### `processed.classroom_fees`
- `processed.wise_app_backend__classroom_fees`

### `processed.features_user_teacher`
- `processed.ft_teacher_announcements`
- `processed.ft_teacher_assignments`
- `processed.ft_teacher_class`
- `processed.ft_teacher_study_materials`
- `processed.ft_teacher_tests`
- `processed.ft_teacher_zooms`
- `processed.user`

### `processed.ft_student_class`
- `processed.class`

### `processed.ft_teacher_announcements`
- `processed.announcements`
- `processed.user`

### `processed.ft_teacher_assignments`
- `processed.assignments`
- `processed.user`

### `processed.ft_teacher_class`
- `processed.class`
- `processed.user`

### `processed.ft_teacher_study_materials`
- `processed.study_materials_flat_v2`
- `processed.user`

### `processed.ft_teacher_tests`
- `processed.tests`
- `processed.user`

### `processed.ft_teacher_zooms`
- `processed.user`
- `processed.zoomers`

### `processed.institute`
- `processed.wise_app_backend__institute`

### `processed.institute_participants`
- `processed.wise_app_backend__institute_participants`

### `processed.liveclassinsight`
- `processed.wise_app_backend__liveclassinsight`

### `processed.liveclassinsight_details`
- `processed.liveclassinsight`

### `processed.mixpanel_detailed_partitions`
- `processed.mixpanel__events`

### `processed.mixpanel_detailed_partitions_by_month`
- `processed.mixpanel__events`

### `processed.mixpanel_partitions`
- `processed.mixpanel__events`

### `processed.registration_form`
- `processed.wise_app_backend__registration_form`

### `processed.registration_form_submission`
- `processed.wise_app_backend__registration_form`
- `processed.wise_app_backend__registration_form_submission`

### `processed.saved_communications`
- `processed.wise_app_backend__saved_communication`

### `processed.session_feedback_submission_student`
- `processed.wise_app_backend__session_feedback_submission`

### `processed.session_feedback_submission_teacher`
- `processed.wise_app_backend__session_feedback_submission`

### `processed.student_registration_form`
- `processed.wise_app_backend__registration_form`
- `processed.wise_app_backend__registration_form_submission`

### `processed.study_materials`
- `processed.wise_app_backend__study_materials`

### `processed.study_materials_flat_v2`
- `processed.data`
- `processed.wise_app_backend__study_materials`

### `processed.study_materials_flat_v3`
- `processed.data`
- `processed.wise_app_backend__study_materials`

### `processed.tests`
- `processed.exam_service__submissions`
- `processed.exam_service__tests`

### `processed.transaction`
- `processed.wise_app_backend__transaction`

### `processed.upsc_live_classrooms`
- `processed.class`
- `processed.user`

### `processed.upsc_live_teacher_private_class_stats`
- `processed.announcements`
- `processed.assignments`
- `processed.class`
- `processed.tests`
- `processed.user`
- `processed.zoomers`

### `processed.upsc_live_teacher_public_class_stats`
- `processed.announcements`
- `processed.assignments`
- `processed.class`
- `processed.tests`
- `processed.user`
- `processed.zoomers`

### `processed.user`
- `processed.wise_app_backend__user`

### `processed.user_features`
- `processed.ft_student_announcements`
- `processed.ft_student_assignments`
- `processed.ft_student_class`
- `processed.ft_student_tests`
- `processed.ft_student_zooms`
- `processed.ft_teacher_announcements`
- `processed.ft_teacher_assignments`
- `processed.ft_teacher_class`
- `processed.ft_teacher_study_materials`
- `processed.ft_teacher_tests`
- `processed.ft_teacher_zooms`
- `processed.user`

### `processed.wise_premium_order`
- `processed.wise_app_backend__premium_order`

### `processed.zoom_summaries`
- `processed.wise_app_backend__rawzoomsummary`

### `processed.zoomers`
- `processed.wise_app_backend__zoom`

### `processed.zoomers_v2`
- `processed.wise_app_backend__zoom`

### `processed.zoomers_v3`
- `processed.wise_app_backend__zoom`

## Reverse (table → views that read it)

### `processed.announcements`
- `processed.ft_teacher_announcements`
- `processed.upsc_live_teacher_private_class_stats`
- `processed.upsc_live_teacher_public_class_stats`

### `processed.assignments`
- `processed.ft_teacher_assignments`
- `processed.upsc_live_teacher_private_class_stats`
- `processed.upsc_live_teacher_public_class_stats`

### `processed.class`
- `processed.ft_student_class`
- `processed.ft_teacher_class`
- `processed.upsc_live_classrooms`
- `processed.upsc_live_teacher_private_class_stats`
- `processed.upsc_live_teacher_public_class_stats`

### `processed.data`
- `processed.study_materials_flat_v2`
- `processed.study_materials_flat_v3`

### `processed.exam_service__submissions`
- `processed.tests`

### `processed.exam_service__tests`
- `processed.tests`

### `processed.ft_student_announcements`
- `processed.user_features`

### `processed.ft_student_assignments`
- `processed.user_features`

### `processed.ft_student_class`
- `processed.user_features`

### `processed.ft_student_tests`
- `processed.user_features`

### `processed.ft_student_zooms`
- `processed.user_features`

### `processed.ft_teacher_announcements`
- `processed.features_user_teacher`
- `processed.user_features`

### `processed.ft_teacher_assignments`
- `processed.features_user_teacher`
- `processed.user_features`

### `processed.ft_teacher_class`
- `processed.features_user_teacher`
- `processed.user_features`

### `processed.ft_teacher_study_materials`
- `processed.features_user_teacher`
- `processed.user_features`

### `processed.ft_teacher_tests`
- `processed.features_user_teacher`
- `processed.user_features`

### `processed.ft_teacher_zooms`
- `processed.features_user_teacher`
- `processed.user_features`

### `processed.liveclassinsight`
- `processed.liveclassinsight_details`

### `processed.mixpanel__events`
- `processed.mixpanel_detailed_partitions`
- `processed.mixpanel_detailed_partitions_by_month`
- `processed.mixpanel_partitions`

### `processed.study_materials_flat_v2`
- `processed.ft_teacher_study_materials`

### `processed.tests`
- `processed.ft_teacher_tests`
- `processed.upsc_live_teacher_private_class_stats`
- `processed.upsc_live_teacher_public_class_stats`

### `processed.user`
- `processed.features_user_teacher`
- `processed.ft_teacher_announcements`
- `processed.ft_teacher_assignments`
- `processed.ft_teacher_class`
- `processed.ft_teacher_study_materials`
- `processed.ft_teacher_tests`
- `processed.ft_teacher_zooms`
- `processed.upsc_live_classrooms`
- `processed.upsc_live_teacher_private_class_stats`
- `processed.upsc_live_teacher_public_class_stats`
- `processed.user_features`

### `processed.wise_app_backend__announcements`
- `processed.announcements`

### `processed.wise_app_backend__assignments`
- `processed.assignments`

### `processed.wise_app_backend__class`
- `processed.class`

### `processed.wise_app_backend__classparticipant`
- `processed.class_participants`

### `processed.wise_app_backend__classroom_fees`
- `processed.classroom_fees`

### `processed.wise_app_backend__institute`
- `processed.institute`

### `processed.wise_app_backend__institute_participants`
- `processed.institute_participants`

### `processed.wise_app_backend__liveclassinsight`
- `processed.liveclassinsight`

### `processed.wise_app_backend__premium_order`
- `processed.wise_premium_order`

### `processed.wise_app_backend__rawzoomsummary`
- `processed.zoom_summaries`

### `processed.wise_app_backend__registration_form`
- `processed.registration_form`
- `processed.registration_form_submission`
- `processed.student_registration_form`

### `processed.wise_app_backend__registration_form_submission`
- `processed.registration_form_submission`
- `processed.student_registration_form`

### `processed.wise_app_backend__saved_communication`
- `processed.saved_communications`

### `processed.wise_app_backend__session_feedback_submission`
- `processed.session_feedback_submission_student`
- `processed.session_feedback_submission_teacher`

### `processed.wise_app_backend__study_materials`
- `processed.study_materials`
- `processed.study_materials_flat_v2`
- `processed.study_materials_flat_v3`

### `processed.wise_app_backend__transaction`
- `processed.transaction`

### `processed.wise_app_backend__user`
- `processed.user`

### `processed.wise_app_backend__zoom`
- `processed.zoomers`
- `processed.zoomers_v2`
- `processed.zoomers_v3`

### `processed.zoomers`
- `processed.ft_teacher_zooms`
- `processed.upsc_live_teacher_private_class_stats`
- `processed.upsc_live_teacher_public_class_stats`
