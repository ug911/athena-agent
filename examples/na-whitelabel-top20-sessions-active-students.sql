-- intent: top NA whitelabel tenants by conducted sessions, with monthly sessions, active students
--         (classroom-based AND attendance-based) and sessions/student. Bound every date window.
-- notes:  is_conducted = meetingStatus IN ('ENDED','STARTED') (facts_v3.py:165). Enrolment uses raw
--         classparticipant STUDENT+ACCEPTED, NOT spf_v3.is_enrolled (which counts REMOVED rows).
--         Tenant = whitelabel namespace via processed_na.institute (daily); NULL namespace = new/demo.
WITH sf AS (
  SELECT session_id, institute_id, class_id, session_date,
         CASE WHEN session_date < DATE '2026-09-01' THEN 'aug' ELSE 'sep' END AS m
  FROM lake_cdc.session_facts_v3
  WHERE region = 'na' AND is_conducted
    AND session_date >= DATE '2026-08-01' AND session_date < DATE '2026-09-16'
),
tenant AS (
  SELECT s.institute_id, coalesce(i.namespace, 'inst:' || s.institute_id) AS tenant
  FROM (SELECT DISTINCT institute_id FROM sf) s
  LEFT JOIN processed_na.institute i ON i.instituteid = s.institute_id
),
enrol AS (
  SELECT DISTINCT json_extract_scalar(doc,'$["classId"]["$oid"]') AS class_id,
                  json_extract_scalar(doc,'$["userId"]["$oid"]')  AS student_id
  FROM lake_cdc.wise_app_backend__classparticipant
  WHERE region = 'na' AND json_extract_scalar(doc,'$.relation') = 'STUDENT'
    AND json_extract_scalar(doc,'$.status') = 'ACCEPTED'
),
sess AS (
  SELECT t.tenant,
         count_if(m='aug') AS aug_full,
         count_if(m='aug' AND session_date < DATE '2026-08-16') AS aug_1_15,
         count_if(m='sep') AS sep_1_15
  FROM sf JOIN tenant t ON t.institute_id = sf.institute_id GROUP BY t.tenant
),
cls AS (  -- classroom-based: every ACCEPTED student in any class that held a conducted session that month
  SELECT t.tenant,
         count(DISTINCT CASE WHEN c.m='aug' THEN e.student_id END) AS aug_students_cls,
         count(DISTINCT CASE WHEN c.m='sep' THEN e.student_id END) AS sep_students_cls
  FROM (SELECT DISTINCT institute_id, class_id, m FROM sf) c
  JOIN tenant t ON t.institute_id = c.institute_id
  JOIN enrol e ON e.class_id = c.class_id
  GROUP BY t.tenant
),
att AS (  -- attendance-based: distinct students who actually attended a conducted session that month
  SELECT t.tenant,
         count(DISTINCT CASE WHEN sf.m='aug' THEN p.student_id END) AS aug_students_att,
         count(DISTINCT CASE WHEN sf.m='sep' THEN p.student_id END) AS sep_students_att
  FROM sf JOIN tenant t ON t.institute_id = sf.institute_id
  JOIN lake_cdc.session_participant_facts_v3 p
    ON p.institute_id = sf.institute_id AND p.session_id = sf.session_id AND p.attended
  GROUP BY t.tenant
)
SELECT s.tenant, s.aug_full, s.aug_1_15, s.sep_1_15,
       coalesce(c.aug_students_cls,0) AS aug_students_cls, coalesce(a.aug_students_att,0) AS aug_students_att,
       coalesce(c.sep_students_cls,0) AS sep_students_cls, coalesce(a.sep_students_att,0) AS sep_students_att,
       round(1.0*s.aug_full/nullif(c.aug_students_cls,0),2) AS aug_spc,
       round(1.0*s.aug_full/nullif(a.aug_students_att,0),2) AS aug_spa,
       round(1.0*s.sep_1_15/nullif(c.sep_students_cls,0),2) AS sep_spc,
       round(1.0*s.sep_1_15/nullif(a.sep_students_att,0),2) AS sep_spa
FROM sess s LEFT JOIN cls c ON c.tenant = s.tenant LEFT JOIN att a ON a.tenant = s.tenant
WHERE s.tenant NOT IN ('wise','wise-demo','make-up-testing','makeuptesting','acme')
  AND s.tenant NOT LIKE 'inst:%'
ORDER BY s.sep_1_15 DESC
LIMIT 20
