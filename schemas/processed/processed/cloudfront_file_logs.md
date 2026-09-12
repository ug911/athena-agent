---
canonical: processed
table: cloudfront_file_logs
type: table
layer: processed
regions:
  in: processed
location: s3://[REDACTED-BUCKET]/production/cloudfront-file-logs
format: INPUTFORMAT
partition_keys:
- dt
schema_parity: identical
last_synced: '2026-08-11T13:14:50+00:00'
sampled_rows: 200
sampled_region: in
---

# `processed.cloudfront_file_logs`

## Region availability

| Region | Athena database |
| --- | --- |
| `IN` | `processed` |

_Only present in **IN**._

## Columns (IN)

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

_String columns with ≤20 distinct values in 200 sampled rows from `IN`. Distribution shown as `value (×count)`._

- `location`: `DEL51-P2 (×84)`, `BOM78-P5 (×30)`, `CCU50-P3 (×29)`, `MAA51-C1 (×26)`, `PNQ50-P3 (×10)`, `HYD57-P1 (×8)`, `MCI50-P2 (×6)`, `BLR50-P3 (×3)`, `PHL51-P1 (×2)`, `DFW55-C3 (×1)`, `DXB53-P2 (×1)`
- `method`: `GET (×200)`
- `host`: `d3odzk9kxo0zti.cloudfront.net (×200)`
- `referrer`: `- (×144)`, `https://web.wise.live/ (×11)`, `https://imageclasses.onlineclass.site/ (×9)`, `https://files.wiseapp.live/external_assets/pdf.js/generic-legacy/web/viewer.html?file=https://files.wiseapp.live/upload_files/64a9262fcc13ad0d2f0f5bd3/upload_a278201f-0f7e-4b94-bcd0-9a171aec3f9f.pdf (×7)`, `https://files.wiseapp.live/external_assets/pdf.js/generic-legacy/web/viewer.html?file=https://files.wiseapp.live/upload_files/64a9262fcc13ad0d2f0f5bd3/upload_1ff23115-887a-42e6-99a5-12f8c640e579.pdf (×7)`, `https://files.wiseapp.live/external_assets/pdf.js/generic-legacy/web/viewer.html?file=https://files.wiseapp.live/upload_files/64a9262fcc13ad0d2f0f5bd3/upload_60937be9-ea3c-485f-b541-729be3a14f70.pdf (×4)`, `https://maariftutorial.onlineclass.site/ (×3)`, `https://files.wiseapp.live/external_assets/pdf.js/generic-legacy/web/viewer.html?file=https://files.wiseapp.live/upload_files/64a9262fcc13ad0d2f0f5bd3/upload_c8750671-3650-4510-b7da-2884a8405170.pdf (×3)`, `https://files.wiseapp.live/external_assets/pdf.js/generic-legacy/web/viewer.html?file=https://files.wiseapp.live/upload_files/64a9262fcc13ad0d2f0f5bd3/upload_378d1064-b745-48b0-a85a-abb994457802.pdf (×2)`, `https://files.wiseapp.live/external_assets/pdf.js/generic-legacy/web/viewer.html?file=https://files.wiseapp.live/upload_files/64ba7fdd4a55061556db9d38/upload_354435a7-83d4-459e-a55d-81bb6e94331f.pdf (×2)`, `https://files.wiseapp.live/external_assets/pdf.js/generic-legacy/web/viewer.html?file=https://files.wiseapp.live/upload_files/64a9262fcc13ad0d2f0f5bd3/upload_2800facb-ecd8-449d-a149-476df8390e8b.pdf (×1)`, `https://files.wiseapp.live/external_assets/pdf.js/generic-legacy/web/viewer.html?file=https://files.wiseapp.live/upload_files/650d6d70e8efbea4d50610e3/upload_76563d27-f4ee-4931-9209-f00f6d6a1c7e.pdf (×1)`, `https://files.wiseapp.live/external_assets/pdf.js/generic-legacy/web/viewer.html?file=https://files.wiseapp.live/upload_files/64ec4db7fdaaf87e20c60239/upload_46f8bdae-1e18-43c2-bac2-f8755754fd2e.pdf (×1)`, `https://files.wiseapp.live/external_assets/pdf.js/generic-legacy/web/viewer.html?file=https://files.wiseapp.live/upload_files/64a9262fcc13ad0d2f0f5bd3/upload_f0d9314a-293b-42ba-8ad9-87a89cd5a25b.pdf (×1)`, `https://files.wiseapp.live/external_assets/pdf.js/generic-legacy/web/viewer.html?file=https://files.wiseapp.live/upload_files/64a9262fcc13ad0d2f0f5bd3/upload_c93b7fa0-3223-4c52-8c19-11a1bedfc063.pdf (×1)`, `https://files.wiseapp.live/external_assets/pdf.js/generic-legacy/web/viewer.html?file=https://files.wiseapp.live/upload_files/60d022f3b5c4302429b72265/upload_aad047da-4d3b-46bc-8af7-f362141990c7.pdf (×1)`, `https://files.wiseapp.live/external_assets/pdf.js/generic-legacy/web/viewer.html?file=https://files.wiseapp.live/upload_files/642a46ccd12e9c7bad1a76ce/upload_e80b020b-2c7d-4d7e-a8fc-e91ad20c26f6.pdf (×1)`, `https://files.wiseapp.live/external_assets/pdf.js/generic-legacy/web/viewer.html?file=https://files.wiseapp.live/upload_files/617d1805661a6b8185083ec6/upload_a79c7f2d-3c8f-44f2-99c7-432a3b2943ba.pdf (×1)`
- `query_string`: `- (×180)`, `thumbnail=true (×8)`, `file=https://files.wiseapp.live/upload_files/64a9262fcc13ad0d2f0f5bd3/upload_1ff23115-887a-42e6-99a5-12f8c640e579.pdf (×2)`, `file=https://files.wiseapp.live/upload_files/64a9262fcc13ad0d2f0f5bd3/upload_378d1064-b745-48b0-a85a-abb994457802.pdf (×1)`, `file=https://files.wiseapp.live/upload_files/64a9262fcc13ad0d2f0f5bd3/upload_2800facb-ecd8-449d-a149-476df8390e8b.pdf (×1)`, `file=https://files.wiseapp.live/upload_files/652f9db628b196f11b35814a/upload_d35705ad-b3ef-4806-a9e0-ece533658948.pdf (×1)`, `file=https://files.wiseapp.live/upload_files/650d6d70e8efbea4d50610e3/upload_76563d27-f4ee-4931-9209-f00f6d6a1c7e.pdf (×1)`, `file=https://files.wiseapp.live/upload_files/64a9262fcc13ad0d2f0f5bd3/upload_f0d9314a-293b-42ba-8ad9-87a89cd5a25b.pdf (×1)`, `file=https://files.wiseapp.live/upload_files/64a9262fcc13ad0d2f0f5bd3/upload_c93b7fa0-3223-4c52-8c19-11a1bedfc063.pdf (×1)`, `file=https://files.wiseapp.live/upload_files/64a9262fcc13ad0d2f0f5bd3/upload_c8750671-3650-4510-b7da-2884a8405170.pdf (×1)`, `file=https://files.wiseapp.live/upload_files/64ba7fdd4a55061556db9d38/upload_354435a7-83d4-459e-a55d-81bb6e94331f.pdf (×1)`, `file=https://files.wiseapp.live/upload_files/64a9262fcc13ad0d2f0f5bd3/upload_a278201f-0f7e-4b94-bcd0-9a171aec3f9f.pdf (×1)`, `file=https://files.wiseapp.live/upload_files/617d1805661a6b8185083ec6/upload_a79c7f2d-3c8f-44f2-99c7-432a3b2943ba.pdf (×1)`
- `cookie`: `- (×200)`
- `result_type`: `Hit (×154)`, `Miss (×33)`, `RefreshHit (×12)`, `Error (×1)`
- `host_header`: `files.wiseapp.live (×200)`
- `request_protocol`: `https (×200)`
- `xforwarded_for`: `- (×200)`
- `ssl_protocol`: `TLSv1.3 (×194)`, `TLSv1.2 (×6)`
- `ssl_cipher`: `TLS_AES_128_GCM_SHA256 (×194)`, `ECDHE-RSA-AES128-GCM-SHA256 (×6)`
- `response_result_type`: `Hit (×155)`, `Miss (×33)`, `RefreshHit (×12)`
- `http_version`: `HTTP/2.0 (×190)`, `HTTP/1.1 (×10)`
- `fle_status`: `- (×200)`
- `x_edge_detailed_result_type`: `Hit (×154)`, `Miss (×33)`, `RefreshHit (×12)`, `ClientCommError (×1)`
- `sc_content_type`: `image/jpeg (×46)`, `image/png (×44)`, `- (×41)`, `application/pdf (×40)`, `text/html (×12)`, `image (×8)`, `image/svg+xml (×3)`, `application/vnd.openxmlformats-officedocument.wordprocessingml.document (×2)`, `image/avif (×1)`, `unknown (×1)`, `application/javascript (×1)`, `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet (×1)`
- `dt`: `2023-11-22 (×153)`, `2023-10-27 (×47)`

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
