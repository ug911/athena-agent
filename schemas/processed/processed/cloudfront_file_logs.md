---
database: processed
table: cloudfront_file_logs
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/production/cloudfront-file-logs
format: INPUTFORMAT
partition_keys:
- dt
last_synced: '2026-04-28T07:10:27+00:00'
sampled_rows: 200
---

# `processed.cloudfront_file_logs`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `date` | `date` |  |
| `time` | `string` |  |
| `location` | `string` |  |
| `bytes` | `bigint` |  |
| `request_ip` | `string` |  |
| `method` | `string` |  |
| `host` | `string` |  |
| `uri` | `string` |  |
| `status` | `int` |  |
| `referrer` | `string` |  |
| `user_agent` | `string` |  |
| `query_string` | `string` |  |
| `cookie` | `string` |  |
| `result_type` | `string` |  |
| `request_id` | `string` |  |
| `host_header` | `string` |  |
| `request_protocol` | `string` |  |
| `request_bytes` | `bigint` |  |
| `time_taken` | `float` |  |
| `xforwarded_for` | `string` |  |
| `ssl_protocol` | `string` |  |
| `ssl_cipher` | `string` |  |
| `response_result_type` | `string` |  |
| `http_version` | `string` |  |
| `fle_status` | `string` |  |
| `fle_encrypted_fields` | `int` |  |
| `c_port` | `int` |  |
| `time_to_first_byte` | `float` |  |
| `x_edge_detailed_result_type` | `string` |  |
| `sc_content_type` | `string` |  |
| `sc_content_len` | `bigint` |  |
| `sc_range_start` | `bigint` |  |
| `sc_range_end` | `bigint` |  |
| `dt` | `string` |  |

**Partition keys:** `dt`

## Enum-like columns

_String columns with ≤20 distinct values in 200 sampled rows. Distribution shown as `value (×count)`._

- `location`: `DEL51-P2 (×72)`, `CCU50-P3 (×48)`, `BOM78-P5 (×22)`, `SIN52-P1 (×14)`, `MAA51-C1 (×12)`, `BLR50-P3 (×9)`, `HYD57-P1 (×7)`, `PNQ50-P3 (×7)`, `MRS52-C1 (×4)`, `BAH53-C1 (×3)`, `NRT20-P2 (×2)`
- `method`: `GET (×200)`
- `host`: `d3odzk9kxo0zti.cloudfront.net (×200)`
- `referrer`: `- (×142)`, `https://web.wise.live/ (×10)`, `https://imageclasses.onlineclass.site/ (×8)`, `https://krashicoaching.onlineclass.site/ (×6)`, `https://maariftutorial.onlineclass.site/ (×5)`, `https://files.wiseapp.live/external_assets/pdf.js/generic-legacy/web/viewer.html?file=https://files.wiseapp.live/upload_files/655c50f300350183ba55ca06/upload_1681de94-0513-426a-b020-89b3cf502473.pdf (×4)`, `https://files.wiseapp.live/external_assets/pdf.js/generic-legacy/web/viewer.html?file=https://files.wiseapp.live/upload_files/6177a669e74b7880dd28b8cd/upload_5b8701d8-e564-489d-bb75-19b2dc6dec72.pdf (×4)`, `https://files.wiseapp.live/external_assets/pdf.js/generic-legacy/web/viewer.css (×4)`, `https://files.wiseapp.live/external_assets/pdf.js/generic-legacy/web/viewer.html?file=https://files.wiseapp.live/upload_files/617d1805661a6b8185083ec6/upload_89e138ca-91e3-48eb-9e1a-4a1aac04280c.pdf (×3)`, `https://files.wiseapp.live/external_assets/pdf.js/generic-legacy/web/viewer.html?file=https://files.wiseapp.live/upload_files/64a9262fcc13ad0d2f0f5bd3/upload_e2f4cdaf-f9d1-4cde-9ff8-fcfa5fc3d892.pdf (×3)`, `https://files.wiseapp.live/external_assets/pdf.js/generic-legacy/web/viewer.html?file=https://files.wiseapp.live/upload_files/64a9262fcc13ad0d2f0f5bd3/upload_c6089b61-cd05-495b-a9ec-fb8769c9bb24.pdf (×2)`, `https://prayastutorialabhyas.onlineclass.site/ (×1)`, `https://files.wiseapp.live/external_assets/pdf.js/generic-legacy/web/viewer.html?file=https://files.wiseapp.live/upload_files/6177a669e74b7880dd28b8cd/upload_9714f689-8612-4291-adcb-1234a031ea5a.pdf (×1)`, `https://files.wiseapp.live/external_assets/pdf.js/generic-legacy/web/viewer.html?file=https://files.wiseapp.live/upload_files/6314187d2cdfac7fd631247d/upload_2f67eeff-22b4-4d17-8743-cce103c7e721.pdf (×1)`, `https://files.wiseapp.live/external_assets/pdf.js/generic-legacy/web/viewer.html?file=https://files.wiseapp.live/upload_files/64a9262fcc13ad0d2f0f5bd3/upload_7e196efc-fa26-43c4-b2e1-0cdec2de4406.pdf (×1)`, `https://files.wiseapp.live/external_assets/pdf.js/generic-legacy/web/viewer.html?file=https://files.wiseapp.live/upload_files/64a9262fcc13ad0d2f0f5bd3/upload_4dc60205-7b5b-468a-a13e-0038f0c0084b.pdf (×1)`, `https://files.wiseapp.live/external_assets/pdf.js/generic-legacy/web/viewer.html?file=https://files.wiseapp.live/upload_files/655c50f300350183ba55ca06/upload_c4b58b59-e768-4658-8599-288aec28e2d1.pdf (×1)`, `https://files.wiseapp.live/external_assets/pdf.js/generic-legacy/web/viewer.html?file=https://files.wiseapp.live/upload_files/64a9262fcc13ad0d2f0f5bd3/upload_ebc67549-595a-496c-b358-8b122f835c48.pdf (×1)`, `https://files.wiseapp.live/external_assets/pdf.js/generic-legacy/web/viewer.html?file=https://files.wiseapp.live/upload_files/64a9262fcc13ad0d2f0f5bd3/upload_a851e5fe-c84a-4571-be17-454e0e5c1d3c.pdf (×1)`, `https://files.wiseapp.live/external_assets/pdf.js/generic-legacy/web/viewer.html?file=https://files.wiseapp.live/upload_files/64a9262fcc13ad0d2f0f5bd3/upload_64c9318f-79f1-434f-9f76-7906a7f6e0eb.pdf (×1)`
- `query_string`: `- (×180)`, `thumbnail=true (×10)`, `file=https://files.wiseapp.live/upload_files/617d1805661a6b8185083ec6/upload_89e138ca-91e3-48eb-9e1a-4a1aac04280c.pdf (×1)`, `file=https://files.wiseapp.live/upload_files/6177a669e74b7880dd28b8cd/upload_9714f689-8612-4291-adcb-1234a031ea5a.pdf (×1)`, `file=https://files.wiseapp.live/upload_files/6177a669e74b7880dd28b8cd/upload_5b8701d8-e564-489d-bb75-19b2dc6dec72.pdf (×1)`, `file=https://files.wiseapp.live/upload_files/655c50f300350183ba55ca06/upload_1681de94-0513-426a-b020-89b3cf502473.pdf (×1)`, `file=https://files.wiseapp.live/upload_files/64a9262fcc13ad0d2f0f5bd3/upload_7e196efc-fa26-43c4-b2e1-0cdec2de4406.pdf (×1)`, `file=https://files.wiseapp.live/upload_files/64a9262fcc13ad0d2f0f5bd3/upload_ebc67549-595a-496c-b358-8b122f835c48.pdf (×1)`, `file=https://files.wiseapp.live/upload_files/64a9262fcc13ad0d2f0f5bd3/upload_a851e5fe-c84a-4571-be17-454e0e5c1d3c.pdf (×1)`, `file=https://files.wiseapp.live/upload_files/64a9262fcc13ad0d2f0f5bd3/upload_64c9318f-79f1-434f-9f76-7906a7f6e0eb.pdf (×1)`, `file=https://files.wiseapp.live/upload_files/64a9262fcc13ad0d2f0f5bd3/upload_e2f4cdaf-f9d1-4cde-9ff8-fcfa5fc3d892.pdf (×1)`, `file=https://files.wiseapp.live/upload_files/64a9262fcc13ad0d2f0f5bd3/upload_c6089b61-cd05-495b-a9ec-fb8769c9bb24.pdf (×1)`
- `cookie`: `- (×200)`
- `result_type`: `Hit (×165)`, `Miss (×22)`, `RefreshHit (×10)`, `Error (×3)`
- `host_header`: `files.wiseapp.live (×200)`
- `request_protocol`: `https (×200)`
- `xforwarded_for`: `- (×200)`
- `ssl_protocol`: `TLSv1.3 (×192)`, `TLSv1.2 (×8)`
- `ssl_cipher`: `TLS_AES_128_GCM_SHA256 (×192)`, `ECDHE-RSA-AES128-GCM-SHA256 (×8)`
- `response_result_type`: `Hit (×166)`, `Miss (×22)`, `RefreshHit (×10)`, `Error (×2)`
- `http_version`: `HTTP/2.0 (×199)`, `HTTP/1.1 (×1)`
- `fle_status`: `- (×200)`
- `x_edge_detailed_result_type`: `Hit (×165)`, `Miss (×22)`, `RefreshHit (×10)`, `ClientHungUpRequest (×2)`, `ClientCommError (×1)`
- `sc_content_type`: `image/jpeg (×55)`, `application/pdf (×54)`, `image/png (×30)`, `- (×25)`, `text/html (×10)`, `image (×9)`, `image/avif (×5)`, `image/svg+xml (×4)`, `application/javascript (×3)`, `text/css (×2)`, `binary/octet-stream (×2)`, `application/vnd.openxmlformats-officedocument.presentationml.presentation (×1)`
- `dt`: `2023-11-22 (×185)`, `2023-11-23 (×15)`

## DDL

```sql
CREATE EXTERNAL TABLE `processed.cloudfront_file_logs`(
  `date` date COMMENT '', 
  `time` string COMMENT '', 
  `location` string COMMENT '', 
  `bytes` bigint COMMENT '', 
  `request_ip` string COMMENT '', 
  `method` string COMMENT '', 
  `host` string COMMENT '', 
  `uri` string COMMENT '', 
  `status` int COMMENT '', 
  `referrer` string COMMENT '', 
  `user_agent` string COMMENT '', 
  `query_string` string COMMENT '', 
  `cookie` string COMMENT '', 
  `result_type` string COMMENT '', 
  `request_id` string COMMENT '', 
  `host_header` string COMMENT '', 
  `request_protocol` string COMMENT '', 
  `request_bytes` bigint COMMENT '', 
  `time_taken` float COMMENT '', 
  `xforwarded_for` string COMMENT '', 
  `ssl_protocol` string COMMENT '', 
  `ssl_cipher` string COMMENT '', 
  `response_result_type` string COMMENT '', 
  `http_version` string COMMENT '', 
  `fle_status` string COMMENT '', 
  `fle_encrypted_fields` int COMMENT '', 
  `c_port` int COMMENT '', 
  `time_to_first_byte` float COMMENT '', 
  `x_edge_detailed_result_type` string COMMENT '', 
  `sc_content_type` string COMMENT '', 
  `sc_content_len` bigint COMMENT '', 
  `sc_range_start` bigint COMMENT '', 
  `sc_range_end` bigint COMMENT '')
PARTITIONED BY ( 
  `dt` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/production/cloudfront-file-logs'
TBLPROPERTIES (
  'has_encrypted_data'='false', 
  'parquet.compression'='GZIP', 
  'presto_query_id'='20220116_172839_00068_x7w8r', 
  'transient_lastDdlTime'='1700122893')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
