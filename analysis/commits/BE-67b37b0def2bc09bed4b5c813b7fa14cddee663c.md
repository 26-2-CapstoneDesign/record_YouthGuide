# merge: 13.16 관리자 자격증 조회 (#40, 후속 #44)

- 저장소: [BackEnd](https://github.com/26-2-CapstoneDesign/BackEnd)
- 작성자: [upbit123](../people/e18eadd07160.md)
- 작성 시각: 2026-11-07 06:56 KST (`2026-11-07T06:56:21+09:00`)
- 커밋 시각: 2026-11-07 06:56 KST (`2026-11-07T06:56:21+09:00`)
- 커미터: upbit123
- 원본: [커밋 `67b37b0def2bc09bed4b5c813b7fa14cddee663c`](https://github.com/26-2-CapstoneDesign/BackEnd/commit/67b37b0def2bc09bed4b5c813b7fa14cddee663c)

## 변경 파일

- `M` [youth-guide-api/docs/CURRENT_STATE.md](https://github.com/26-2-CapstoneDesign/BackEnd/blob/67b37b0def2bc09bed4b5c813b7fa14cddee663c/youth-guide-api/docs/CURRENT_STATE.md)
- `M` [youth-guide-api/docs/FEATURE_STATUS.md](https://github.com/26-2-CapstoneDesign/BackEnd/blob/67b37b0def2bc09bed4b5c813b7fa14cddee663c/youth-guide-api/docs/FEATURE_STATUS.md)
- `A` [youth-guide-api/docs/SPEC-13-16-CERTIFICATES-READ.md](https://github.com/26-2-CapstoneDesign/BackEnd/blob/67b37b0def2bc09bed4b5c813b7fa14cddee663c/youth-guide-api/docs/SPEC-13-16-CERTIFICATES-READ.md)
- `M` [youth-guide-api/docs/SPEC-ADMIN.md](https://github.com/26-2-CapstoneDesign/BackEnd/blob/67b37b0def2bc09bed4b5c813b7fa14cddee663c/youth-guide-api/docs/SPEC-ADMIN.md)
- `M` [youth-guide-api/docs/TERMS.md](https://github.com/26-2-CapstoneDesign/BackEnd/blob/67b37b0def2bc09bed4b5c813b7fa14cddee663c/youth-guide-api/docs/TERMS.md)
- `A` [youth-guide-api/docs/features/WBS-13-16-CERTIFICATES-READ.md](https://github.com/26-2-CapstoneDesign/BackEnd/blob/67b37b0def2bc09bed4b5c813b7fa14cddee663c/youth-guide-api/docs/features/WBS-13-16-CERTIFICATES-READ.md)
- `A` [youth-guide-api/docs/worklogs/WBS-13-16-CERTIFICATES-READ__claude-code__20261106T210121Z.md](https://github.com/26-2-CapstoneDesign/BackEnd/blob/67b37b0def2bc09bed4b5c813b7fa14cddee663c/youth-guide-api/docs/worklogs/WBS-13-16-CERTIFICATES-READ__claude-code__20261106T210121Z.md)
- `A` [youth-guide-api/src/main/java/com/youthguide/api/admin/controller/AdminCertificateQueryController.java](https://github.com/26-2-CapstoneDesign/BackEnd/blob/67b37b0def2bc09bed4b5c813b7fa14cddee663c/youth-guide-api/src/main/java/com/youthguide/api/admin/controller/AdminCertificateQueryController.java)
- `A` [youth-guide-api/src/main/java/com/youthguide/api/admin/dto/AdminCertificateDetailResponse.java](https://github.com/26-2-CapstoneDesign/BackEnd/blob/67b37b0def2bc09bed4b5c813b7fa14cddee663c/youth-guide-api/src/main/java/com/youthguide/api/admin/dto/AdminCertificateDetailResponse.java)
- `A` [youth-guide-api/src/main/java/com/youthguide/api/admin/dto/AdminCertificateResponse.java](https://github.com/26-2-CapstoneDesign/BackEnd/blob/67b37b0def2bc09bed4b5c813b7fa14cddee663c/youth-guide-api/src/main/java/com/youthguide/api/admin/dto/AdminCertificateResponse.java)
- `A` [youth-guide-api/src/main/java/com/youthguide/api/admin/dto/AdminCertificateSourceKeyResponse.java](https://github.com/26-2-CapstoneDesign/BackEnd/blob/67b37b0def2bc09bed4b5c813b7fa14cddee663c/youth-guide-api/src/main/java/com/youthguide/api/admin/dto/AdminCertificateSourceKeyResponse.java)
- `A` [youth-guide-api/src/main/java/com/youthguide/api/admin/dto/AdminExamEventResponse.java](https://github.com/26-2-CapstoneDesign/BackEnd/blob/67b37b0def2bc09bed4b5c813b7fa14cddee663c/youth-guide-api/src/main/java/com/youthguide/api/admin/dto/AdminExamEventResponse.java)
- `A` [youth-guide-api/src/main/java/com/youthguide/api/admin/dto/AdminExamSessionResponse.java](https://github.com/26-2-CapstoneDesign/BackEnd/blob/67b37b0def2bc09bed4b5c813b7fa14cddee663c/youth-guide-api/src/main/java/com/youthguide/api/admin/dto/AdminExamSessionResponse.java)
- `A` [youth-guide-api/src/main/java/com/youthguide/api/admin/dto/AdminScheduleChangeResponse.java](https://github.com/26-2-CapstoneDesign/BackEnd/blob/67b37b0def2bc09bed4b5c813b7fa14cddee663c/youth-guide-api/src/main/java/com/youthguide/api/admin/dto/AdminScheduleChangeResponse.java)
- `A` [youth-guide-api/src/main/java/com/youthguide/api/admin/dto/AdminScheduleChangesResponse.java](https://github.com/26-2-CapstoneDesign/BackEnd/blob/67b37b0def2bc09bed4b5c813b7fa14cddee663c/youth-guide-api/src/main/java/com/youthguide/api/admin/dto/AdminScheduleChangesResponse.java)
- `A` [youth-guide-api/src/main/java/com/youthguide/api/admin/dto/AdminSourceKeyChangeResponse.java](https://github.com/26-2-CapstoneDesign/BackEnd/blob/67b37b0def2bc09bed4b5c813b7fa14cddee663c/youth-guide-api/src/main/java/com/youthguide/api/admin/dto/AdminSourceKeyChangeResponse.java)
- `A` [youth-guide-api/src/main/java/com/youthguide/api/admin/repository/AdminCertificateHeaderRow.java](https://github.com/26-2-CapstoneDesign/BackEnd/blob/67b37b0def2bc09bed4b5c813b7fa14cddee663c/youth-guide-api/src/main/java/com/youthguide/api/admin/repository/AdminCertificateHeaderRow.java)
- `A` [youth-guide-api/src/main/java/com/youthguide/api/admin/repository/AdminCertificateQueryRepository.java](https://github.com/26-2-CapstoneDesign/BackEnd/blob/67b37b0def2bc09bed4b5c813b7fa14cddee663c/youth-guide-api/src/main/java/com/youthguide/api/admin/repository/AdminCertificateQueryRepository.java)
- `A` [youth-guide-api/src/main/java/com/youthguide/api/admin/repository/AdminSessionEventRow.java](https://github.com/26-2-CapstoneDesign/BackEnd/blob/67b37b0def2bc09bed4b5c813b7fa14cddee663c/youth-guide-api/src/main/java/com/youthguide/api/admin/repository/AdminSessionEventRow.java)
- `A` [youth-guide-api/src/main/java/com/youthguide/api/admin/service/AdminCertificateQueryService.java](https://github.com/26-2-CapstoneDesign/BackEnd/blob/67b37b0def2bc09bed4b5c813b7fa14cddee663c/youth-guide-api/src/main/java/com/youthguide/api/admin/service/AdminCertificateQueryService.java)
- `A` [youth-guide-api/src/test/java/com/youthguide/api/admin/controller/AdminCertificateQueryControllerTest.java](https://github.com/26-2-CapstoneDesign/BackEnd/blob/67b37b0def2bc09bed4b5c813b7fa14cddee663c/youth-guide-api/src/test/java/com/youthguide/api/admin/controller/AdminCertificateQueryControllerTest.java)
- `A` [youth-guide-api/src/test/java/com/youthguide/api/admin/repository/AdminCertificateQueryMySqlTest.java](https://github.com/26-2-CapstoneDesign/BackEnd/blob/67b37b0def2bc09bed4b5c813b7fa14cddee663c/youth-guide-api/src/test/java/com/youthguide/api/admin/repository/AdminCertificateQueryMySqlTest.java)
- `A` [youth-guide-api/src/test/java/com/youthguide/api/admin/service/AdminCertificateQueryServiceTest.java](https://github.com/26-2-CapstoneDesign/BackEnd/blob/67b37b0def2bc09bed4b5c813b7fa14cddee663c/youth-guide-api/src/test/java/com/youthguide/api/admin/service/AdminCertificateQueryServiceTest.java)
- `A` [youth-guide-api/src/test/resources/admin-certificates/baseline.sql](https://github.com/26-2-CapstoneDesign/BackEnd/blob/67b37b0def2bc09bed4b5c813b7fa14cddee663c/youth-guide-api/src/test/resources/admin-certificates/baseline.sql)

## 해석

실행 흐름과 변경 이유는 관련 코드·PR·이슈를 확인한 뒤 [작업 문서](../work/README.md)에 기록합니다.
