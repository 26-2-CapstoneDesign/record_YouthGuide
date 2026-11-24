# 13.15 : 이용 제한 중 게시글·댓글·대댓글 작성 차단 (CommunityWriteGuard)

- 저장소: [BackEnd](https://github.com/26-2-CapstoneDesign/BackEnd)
- 작성자: [upbit123](../people/e18eadd07160.md)
- 작성 시각: 2026-11-07 03:20 KST (`2026-11-07T03:20:02+09:00`)
- 커밋 시각: 2026-11-07 03:20 KST (`2026-11-07T03:20:02+09:00`)
- 커미터: upbit123
- 원본: [커밋 `3dce56c9ecfdd1adba8b18eed6e65405a63f12d4`](https://github.com/26-2-CapstoneDesign/BackEnd/commit/3dce56c9ecfdd1adba8b18eed6e65405a63f12d4)

## 변경 파일

- `A` [youth-guide-api/src/main/java/com/youthguide/api/admin/service/CommunityWriteGuard.java](https://github.com/26-2-CapstoneDesign/BackEnd/blob/3dce56c9ecfdd1adba8b18eed6e65405a63f12d4/youth-guide-api/src/main/java/com/youthguide/api/admin/service/CommunityWriteGuard.java)
- `M` [youth-guide-api/src/main/java/com/youthguide/api/review/service/CommunityPostCommandService.java](https://github.com/26-2-CapstoneDesign/BackEnd/blob/3dce56c9ecfdd1adba8b18eed6e65405a63f12d4/youth-guide-api/src/main/java/com/youthguide/api/review/service/CommunityPostCommandService.java)
- `M` [youth-guide-api/src/main/java/com/youthguide/api/review/service/CommunityPostCommentCommandService.java](https://github.com/26-2-CapstoneDesign/BackEnd/blob/3dce56c9ecfdd1adba8b18eed6e65405a63f12d4/youth-guide-api/src/main/java/com/youthguide/api/review/service/CommunityPostCommentCommandService.java)
- `A` [youth-guide-api/src/test/java/com/youthguide/api/admin/service/CommunityWriteGuardTest.java](https://github.com/26-2-CapstoneDesign/BackEnd/blob/3dce56c9ecfdd1adba8b18eed6e65405a63f12d4/youth-guide-api/src/test/java/com/youthguide/api/admin/service/CommunityWriteGuardTest.java)
- `M` [youth-guide-api/src/test/java/com/youthguide/api/review/service/CommunityPostCommandServiceTest.java](https://github.com/26-2-CapstoneDesign/BackEnd/blob/3dce56c9ecfdd1adba8b18eed6e65405a63f12d4/youth-guide-api/src/test/java/com/youthguide/api/review/service/CommunityPostCommandServiceTest.java)
- `M` [youth-guide-api/src/test/java/com/youthguide/api/review/service/CommunityPostCommentCommandServiceTest.java](https://github.com/26-2-CapstoneDesign/BackEnd/blob/3dce56c9ecfdd1adba8b18eed6e65405a63f12d4/youth-guide-api/src/test/java/com/youthguide/api/review/service/CommunityPostCommentCommandServiceTest.java)
- `M` [youth-guide-api/tasks/todo.md](https://github.com/26-2-CapstoneDesign/BackEnd/blob/3dce56c9ecfdd1adba8b18eed6e65405a63f12d4/youth-guide-api/tasks/todo.md)

## 해석

실행 흐름과 변경 이유는 관련 코드·PR·이슈를 확인한 뒤 [작업 문서](../work/README.md)에 기록합니다.
