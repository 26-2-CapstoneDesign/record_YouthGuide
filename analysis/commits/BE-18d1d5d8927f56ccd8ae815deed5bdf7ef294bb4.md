# 13.20 : 관리자 운영 이력 목록·상세 조회 API 구현

- 저장소: [BackEnd](https://github.com/26-2-CapstoneDesign/BackEnd)
- 작성자: [upbit123](../people/e18eadd07160.md)
- 작성 시각: 2026-11-06 14:28 KST (`2026-11-06T14:28:24+09:00`)
- 커밋 시각: 2026-11-06 14:28 KST (`2026-11-06T14:28:24+09:00`)
- 커미터: upbit123
- 원본: [커밋 `18d1d5d8927f56ccd8ae815deed5bdf7ef294bb4`](https://github.com/26-2-CapstoneDesign/BackEnd/commit/18d1d5d8927f56ccd8ae815deed5bdf7ef294bb4)

## 변경 파일

- `M` [youth-guide-api/docs/CURRENT_STATE.md](https://github.com/26-2-CapstoneDesign/BackEnd/blob/18d1d5d8927f56ccd8ae815deed5bdf7ef294bb4/youth-guide-api/docs/CURRENT_STATE.md)
- `M` [youth-guide-api/docs/FEATURE_STATUS.md](https://github.com/26-2-CapstoneDesign/BackEnd/blob/18d1d5d8927f56ccd8ae815deed5bdf7ef294bb4/youth-guide-api/docs/FEATURE_STATUS.md)
- `A` [youth-guide-api/docs/PRD-ADMIN.md](https://github.com/26-2-CapstoneDesign/BackEnd/blob/18d1d5d8927f56ccd8ae815deed5bdf7ef294bb4/youth-guide-api/docs/PRD-ADMIN.md)
- `A` [youth-guide-api/docs/features/WBS-13-20-AUDIT-READ.md](https://github.com/26-2-CapstoneDesign/BackEnd/blob/18d1d5d8927f56ccd8ae815deed5bdf7ef294bb4/youth-guide-api/docs/features/WBS-13-20-AUDIT-READ.md)
- `A` [youth-guide-api/docs/worklogs/WBS-13-20-AUDIT-READ__claude-code__20261106T044211Z.md](https://github.com/26-2-CapstoneDesign/BackEnd/blob/18d1d5d8927f56ccd8ae815deed5bdf7ef294bb4/youth-guide-api/docs/worklogs/WBS-13-20-AUDIT-READ__claude-code__20261106T044211Z.md)
- `A` [youth-guide-api/src/main/java/com/youthguide/api/admin/controller/AdminAuditQueryController.java](https://github.com/26-2-CapstoneDesign/BackEnd/blob/18d1d5d8927f56ccd8ae815deed5bdf7ef294bb4/youth-guide-api/src/main/java/com/youthguide/api/admin/controller/AdminAuditQueryController.java)
- `A` [youth-guide-api/src/main/java/com/youthguide/api/admin/dto/AdminAuditLogDetailResponse.java](https://github.com/26-2-CapstoneDesign/BackEnd/blob/18d1d5d8927f56ccd8ae815deed5bdf7ef294bb4/youth-guide-api/src/main/java/com/youthguide/api/admin/dto/AdminAuditLogDetailResponse.java)
- `A` [youth-guide-api/src/main/java/com/youthguide/api/admin/dto/AdminAuditLogResponse.java](https://github.com/26-2-CapstoneDesign/BackEnd/blob/18d1d5d8927f56ccd8ae815deed5bdf7ef294bb4/youth-guide-api/src/main/java/com/youthguide/api/admin/dto/AdminAuditLogResponse.java)
- `A` [youth-guide-api/src/main/java/com/youthguide/api/admin/dto/AdminAuditLogSearch.java](https://github.com/26-2-CapstoneDesign/BackEnd/blob/18d1d5d8927f56ccd8ae815deed5bdf7ef294bb4/youth-guide-api/src/main/java/com/youthguide/api/admin/dto/AdminAuditLogSearch.java)
- `A` [youth-guide-api/src/main/java/com/youthguide/api/admin/repository/AdminAuditQueryRepository.java](https://github.com/26-2-CapstoneDesign/BackEnd/blob/18d1d5d8927f56ccd8ae815deed5bdf7ef294bb4/youth-guide-api/src/main/java/com/youthguide/api/admin/repository/AdminAuditQueryRepository.java)
- `A` [youth-guide-api/src/main/java/com/youthguide/api/admin/service/AdminAuditQueryService.java](https://github.com/26-2-CapstoneDesign/BackEnd/blob/18d1d5d8927f56ccd8ae815deed5bdf7ef294bb4/youth-guide-api/src/main/java/com/youthguide/api/admin/service/AdminAuditQueryService.java)
- `M` [youth-guide-api/src/main/java/com/youthguide/api/global/exception/ErrorCode.java](https://github.com/26-2-CapstoneDesign/BackEnd/blob/18d1d5d8927f56ccd8ae815deed5bdf7ef294bb4/youth-guide-api/src/main/java/com/youthguide/api/global/exception/ErrorCode.java)
- `A` [youth-guide-api/src/main/resources/db/migration/V9__add_admin_audit_log_created_index.sql](https://github.com/26-2-CapstoneDesign/BackEnd/blob/18d1d5d8927f56ccd8ae815deed5bdf7ef294bb4/youth-guide-api/src/main/resources/db/migration/V9__add_admin_audit_log_created_index.sql)
- `A` [youth-guide-api/src/test/java/com/youthguide/api/admin/controller/AdminAuditQueryControllerTest.java](https://github.com/26-2-CapstoneDesign/BackEnd/blob/18d1d5d8927f56ccd8ae815deed5bdf7ef294bb4/youth-guide-api/src/test/java/com/youthguide/api/admin/controller/AdminAuditQueryControllerTest.java)
- `A` [youth-guide-api/src/test/java/com/youthguide/api/admin/repository/AdminAuditQueryMySqlTest.java](https://github.com/26-2-CapstoneDesign/BackEnd/blob/18d1d5d8927f56ccd8ae815deed5bdf7ef294bb4/youth-guide-api/src/test/java/com/youthguide/api/admin/repository/AdminAuditQueryMySqlTest.java)
- `M` [youth-guide-api/src/test/java/com/youthguide/api/admin/repository/AdminReportCommandMySqlTest.java](https://github.com/26-2-CapstoneDesign/BackEnd/blob/18d1d5d8927f56ccd8ae815deed5bdf7ef294bb4/youth-guide-api/src/test/java/com/youthguide/api/admin/repository/AdminReportCommandMySqlTest.java)
- `M` [youth-guide-api/src/test/java/com/youthguide/api/admin/repository/AdminReportQueryMySqlTest.java](https://github.com/26-2-CapstoneDesign/BackEnd/blob/18d1d5d8927f56ccd8ae815deed5bdf7ef294bb4/youth-guide-api/src/test/java/com/youthguide/api/admin/repository/AdminReportQueryMySqlTest.java)
- `M` [youth-guide-api/src/test/java/com/youthguide/api/admin/repository/RestoredSchemaFlywayTest.java](https://github.com/26-2-CapstoneDesign/BackEnd/blob/18d1d5d8927f56ccd8ae815deed5bdf7ef294bb4/youth-guide-api/src/test/java/com/youthguide/api/admin/repository/RestoredSchemaFlywayTest.java)
- `A` [youth-guide-api/src/test/java/com/youthguide/api/admin/service/AdminAuditQueryServiceTest.java](https://github.com/26-2-CapstoneDesign/BackEnd/blob/18d1d5d8927f56ccd8ae815deed5bdf7ef294bb4/youth-guide-api/src/test/java/com/youthguide/api/admin/service/AdminAuditQueryServiceTest.java)

## 해석

실행 흐름과 변경 이유는 관련 코드·PR·이슈를 확인한 뒤 [작업 문서](../work/README.md)에 기록합니다.
