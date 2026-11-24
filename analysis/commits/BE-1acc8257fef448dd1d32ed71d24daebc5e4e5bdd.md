# Merge pull request #4 from 26-2-CapstoneDesign/feature-09-01-review-query

- 저장소: [BackEnd](https://github.com/26-2-CapstoneDesign/BackEnd)
- 작성자: [hyewon](../people/e2d38c3d199d.md)
- 작성 시각: 2026-10-11 12:03 KST (`2026-10-11T12:03:28+09:00`)
- 커밋 시각: 2026-10-11 12:03 KST (`2026-10-11T12:03:28+09:00`)
- 커미터: GitHub
- 원본: [커밋 `1acc8257fef448dd1d32ed71d24daebc5e4e5bdd`](https://github.com/26-2-CapstoneDesign/BackEnd/commit/1acc8257fef448dd1d32ed71d24daebc5e4e5bdd)

## 변경 파일

- `M` [youth-guide-api/docs/CURRENT_STATE.md](https://github.com/26-2-CapstoneDesign/BackEnd/blob/1acc8257fef448dd1d32ed71d24daebc5e4e5bdd/youth-guide-api/docs/CURRENT_STATE.md)
- `M` [youth-guide-api/docs/FEATURE_STATUS.md](https://github.com/26-2-CapstoneDesign/BackEnd/blob/1acc8257fef448dd1d32ed71d24daebc5e4e5bdd/youth-guide-api/docs/FEATURE_STATUS.md)
- `A` [youth-guide-api/docs/features/WBS-09-01-REVIEW-QUERY.md](https://github.com/26-2-CapstoneDesign/BackEnd/blob/1acc8257fef448dd1d32ed71d24daebc5e4e5bdd/youth-guide-api/docs/features/WBS-09-01-REVIEW-QUERY.md)
- `A` [youth-guide-api/docs/worklogs/WBS-09-01-PR-REVIEW__codex__20261010T145026Z.md](https://github.com/26-2-CapstoneDesign/BackEnd/blob/1acc8257fef448dd1d32ed71d24daebc5e4e5bdd/youth-guide-api/docs/worklogs/WBS-09-01-PR-REVIEW__codex__20261010T145026Z.md)
- `A` [youth-guide-api/docs/worklogs/WBS-09-01-PUBLIC-QUERY__codex__20261010T160825Z.md](https://github.com/26-2-CapstoneDesign/BackEnd/blob/1acc8257fef448dd1d32ed71d24daebc5e4e5bdd/youth-guide-api/docs/worklogs/WBS-09-01-PUBLIC-QUERY__codex__20261010T160825Z.md)
- `A` [youth-guide-api/docs/worklogs/WBS-09-01-REVIEW-QUERY__codex__20261010T101546Z.md](https://github.com/26-2-CapstoneDesign/BackEnd/blob/1acc8257fef448dd1d32ed71d24daebc5e4e5bdd/youth-guide-api/docs/worklogs/WBS-09-01-REVIEW-QUERY__codex__20261010T101546Z.md)
- `M` [youth-guide-api/src/main/java/com/youthguide/api/global/config/SecurityConfig.java](https://github.com/26-2-CapstoneDesign/BackEnd/blob/1acc8257fef448dd1d32ed71d24daebc5e4e5bdd/youth-guide-api/src/main/java/com/youthguide/api/global/config/SecurityConfig.java)
- `M` [youth-guide-api/src/main/java/com/youthguide/api/global/exception/ErrorCode.java](https://github.com/26-2-CapstoneDesign/BackEnd/blob/1acc8257fef448dd1d32ed71d24daebc5e4e5bdd/youth-guide-api/src/main/java/com/youthguide/api/global/exception/ErrorCode.java)
- `M` [youth-guide-api/src/main/java/com/youthguide/api/global/exception/GlobalExceptionHandler.java](https://github.com/26-2-CapstoneDesign/BackEnd/blob/1acc8257fef448dd1d32ed71d24daebc5e4e5bdd/youth-guide-api/src/main/java/com/youthguide/api/global/exception/GlobalExceptionHandler.java)
- `A` [youth-guide-api/src/main/java/com/youthguide/api/review/controller/CommunityPostQueryController.java](https://github.com/26-2-CapstoneDesign/BackEnd/blob/1acc8257fef448dd1d32ed71d24daebc5e4e5bdd/youth-guide-api/src/main/java/com/youthguide/api/review/controller/CommunityPostQueryController.java)
- `A` [youth-guide-api/src/main/java/com/youthguide/api/review/domain/CommunityPost.java](https://github.com/26-2-CapstoneDesign/BackEnd/blob/1acc8257fef448dd1d32ed71d24daebc5e4e5bdd/youth-guide-api/src/main/java/com/youthguide/api/review/domain/CommunityPost.java)
- `A` [youth-guide-api/src/main/java/com/youthguide/api/review/domain/CommunityPostKind.java](https://github.com/26-2-CapstoneDesign/BackEnd/blob/1acc8257fef448dd1d32ed71d24daebc5e4e5bdd/youth-guide-api/src/main/java/com/youthguide/api/review/domain/CommunityPostKind.java)
- `A` [youth-guide-api/src/main/java/com/youthguide/api/review/dto/CommunityPostAuthorResponse.java](https://github.com/26-2-CapstoneDesign/BackEnd/blob/1acc8257fef448dd1d32ed71d24daebc5e4e5bdd/youth-guide-api/src/main/java/com/youthguide/api/review/dto/CommunityPostAuthorResponse.java)
- `A` [youth-guide-api/src/main/java/com/youthguide/api/review/dto/CommunityPostDetailResponse.java](https://github.com/26-2-CapstoneDesign/BackEnd/blob/1acc8257fef448dd1d32ed71d24daebc5e4e5bdd/youth-guide-api/src/main/java/com/youthguide/api/review/dto/CommunityPostDetailResponse.java)
- `A` [youth-guide-api/src/main/java/com/youthguide/api/review/dto/CommunityPostPageResponse.java](https://github.com/26-2-CapstoneDesign/BackEnd/blob/1acc8257fef448dd1d32ed71d24daebc5e4e5bdd/youth-guide-api/src/main/java/com/youthguide/api/review/dto/CommunityPostPageResponse.java)
- `A` [youth-guide-api/src/main/java/com/youthguide/api/review/dto/CommunityPostSummaryResponse.java](https://github.com/26-2-CapstoneDesign/BackEnd/blob/1acc8257fef448dd1d32ed71d24daebc5e4e5bdd/youth-guide-api/src/main/java/com/youthguide/api/review/dto/CommunityPostSummaryResponse.java)
- `A` [youth-guide-api/src/main/java/com/youthguide/api/review/repository/CommunityPostQueryRepository.java](https://github.com/26-2-CapstoneDesign/BackEnd/blob/1acc8257fef448dd1d32ed71d24daebc5e4e5bdd/youth-guide-api/src/main/java/com/youthguide/api/review/repository/CommunityPostQueryRepository.java)
- `A` [youth-guide-api/src/main/java/com/youthguide/api/review/repository/projection/CommunityPostDetailProjection.java](https://github.com/26-2-CapstoneDesign/BackEnd/blob/1acc8257fef448dd1d32ed71d24daebc5e4e5bdd/youth-guide-api/src/main/java/com/youthguide/api/review/repository/projection/CommunityPostDetailProjection.java)
- `A` [youth-guide-api/src/main/java/com/youthguide/api/review/repository/projection/CommunityPostSummaryProjection.java](https://github.com/26-2-CapstoneDesign/BackEnd/blob/1acc8257fef448dd1d32ed71d24daebc5e4e5bdd/youth-guide-api/src/main/java/com/youthguide/api/review/repository/projection/CommunityPostSummaryProjection.java)
- `A` [youth-guide-api/src/main/java/com/youthguide/api/review/service/CommunityPostQueryService.java](https://github.com/26-2-CapstoneDesign/BackEnd/blob/1acc8257fef448dd1d32ed71d24daebc5e4e5bdd/youth-guide-api/src/main/java/com/youthguide/api/review/service/CommunityPostQueryService.java)
- `A` [youth-guide-api/src/main/java/com/youthguide/api/review/support/LikePatternEscaper.java](https://github.com/26-2-CapstoneDesign/BackEnd/blob/1acc8257fef448dd1d32ed71d24daebc5e4e5bdd/youth-guide-api/src/main/java/com/youthguide/api/review/support/LikePatternEscaper.java)
- `A` [youth-guide-api/src/test/java/com/youthguide/api/review/controller/CommunityPostQueryControllerTest.java](https://github.com/26-2-CapstoneDesign/BackEnd/blob/1acc8257fef448dd1d32ed71d24daebc5e4e5bdd/youth-guide-api/src/test/java/com/youthguide/api/review/controller/CommunityPostQueryControllerTest.java)
- `A` [youth-guide-api/src/test/java/com/youthguide/api/review/controller/CommunityPostQuerySecurityTest.java](https://github.com/26-2-CapstoneDesign/BackEnd/blob/1acc8257fef448dd1d32ed71d24daebc5e4e5bdd/youth-guide-api/src/test/java/com/youthguide/api/review/controller/CommunityPostQuerySecurityTest.java)
- `A` [youth-guide-api/src/test/java/com/youthguide/api/review/repository/CommunityPostQueryRepositoryMySqlIntegrationTest.java](https://github.com/26-2-CapstoneDesign/BackEnd/blob/1acc8257fef448dd1d32ed71d24daebc5e4e5bdd/youth-guide-api/src/test/java/com/youthguide/api/review/repository/CommunityPostQueryRepositoryMySqlIntegrationTest.java)
- `A` [youth-guide-api/src/test/java/com/youthguide/api/review/repository/CommunityPostQueryRepositoryTest.java](https://github.com/26-2-CapstoneDesign/BackEnd/blob/1acc8257fef448dd1d32ed71d24daebc5e4e5bdd/youth-guide-api/src/test/java/com/youthguide/api/review/repository/CommunityPostQueryRepositoryTest.java)
- `A` [youth-guide-api/src/test/java/com/youthguide/api/review/service/CommunityPostQueryServiceTest.java](https://github.com/26-2-CapstoneDesign/BackEnd/blob/1acc8257fef448dd1d32ed71d24daebc5e4e5bdd/youth-guide-api/src/test/java/com/youthguide/api/review/service/CommunityPostQueryServiceTest.java)
- `A` [youth-guide-api/src/test/java/com/youthguide/api/review/support/LikePatternEscaperTest.java](https://github.com/26-2-CapstoneDesign/BackEnd/blob/1acc8257fef448dd1d32ed71d24daebc5e4e5bdd/youth-guide-api/src/test/java/com/youthguide/api/review/support/LikePatternEscaperTest.java)

## 해석

실행 흐름과 변경 이유는 관련 코드·PR·이슈를 확인한 뒤 [작업 문서](../work/README.md)에 기록합니다.
