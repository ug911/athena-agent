-- intent: list past zoom sessions for a namespace, with class, host teacher, and institute name. Namespaces can span multiple institutes (read class.namespace, then resolve institute via class.instituteid).
WITH zoom AS (
  SELECT
    CAST(json_extract(_id,     '$["$oid"]') AS varchar) AS session_id,
    CAST(json_extract(classid, '$["$oid"]') AS varchar) AS class_id,
    CAST(json_extract(userid,  '$["$oid"]') AS varchar) AS host_userid,
    title,
    meetingstatus,
    from_unixtime(CAST(json_extract_scalar(start_time, '$["$date"]["$numberlong"]') AS bigint)/1000) AS start_time,
    from_unixtime(CAST(json_extract_scalar(end_time,   '$["$date"]["$numberlong"]') AS bigint)/1000) AS end_time
  FROM processed.wise_app_backend__zoom
)
SELECT
  z.session_id, z.start_time, z.end_time, z.title, z.meetingstatus,
  c.class_id, c.name AS class_name, c.subject AS class_subject,
  z.host_userid, u.name AS host_teacher_name,
  c.instituteid, i.name AS institute_name
FROM zoom z
JOIN      processed.class     c ON c.class_id    = z.class_id
LEFT JOIN processed.institute i ON i.instituteid = c.instituteid
LEFT JOIN processed."user"    u ON u.userid      = z.host_userid
WHERE c.namespace = 'leadiasacademy'           -- swap for any tenant namespace
  AND z.end_time IS NOT NULL
  AND z.end_time < current_timestamp
ORDER BY z.start_time DESC;
