# feat: 홈 캘린더 특정 회차 숨김 API

- 저장소: [BackEnd](https://github.com/26-2-CapstoneDesign/BackEnd)
- 작성자: [ta4oozlp719](../people/8603e823fffc.md)
- 작성 시각: 2026-10-28 01:03 KST (`2026-10-28T01:03:01+09:00`)
- 커밋 시각: 2026-10-28 01:03 KST (`2026-10-28T01:03:01+09:00`)
- 커미터: ta4oozlp719
- 원본: [커밋 `8b07585df31ecb8b902bcfa4aea0abb514c3a49f`](https://github.com/26-2-CapstoneDesign/BackEnd/commit/8b07585df31ecb8b902bcfa4aea0abb514c3a49f)

## 변경 파일

- `M` [youth-guide-api/src/main/java/com/youthguide/api/global/exception/ErrorCode.java](https://github.com/26-2-CapstoneDesign/BackEnd/blob/8b07585df31ecb8b902bcfa4aea0abb514c3a49f/youth-guide-api/src/main/java/com/youthguide/api/global/exception/ErrorCode.java)
- `M` [youth-guide-api/src/main/java/com/youthguide/api/home/controller/CalendarController.java](https://github.com/26-2-CapstoneDesign/BackEnd/blob/8b07585df31ecb8b902bcfa4aea0abb514c3a49f/youth-guide-api/src/main/java/com/youthguide/api/home/controller/CalendarController.java)
- `A` [youth-guide-api/src/main/java/com/youthguide/api/home/domain/MemberExamSessionExclusion.java](https://github.com/26-2-CapstoneDesign/BackEnd/blob/8b07585df31ecb8b902bcfa4aea0abb514c3a49f/youth-guide-api/src/main/java/com/youthguide/api/home/domain/MemberExamSessionExclusion.java)
- `A` [youth-guide-api/src/main/java/com/youthguide/api/home/domain/MemberExamSessionExclusionId.java](https://github.com/26-2-CapstoneDesign/BackEnd/blob/8b07585df31ecb8b902bcfa4aea0abb514c3a49f/youth-guide-api/src/main/java/com/youthguide/api/home/domain/MemberExamSessionExclusionId.java)
- `M` [youth-guide-api/src/main/java/com/youthguide/api/home/dto/CalendarResponse.java](https://github.com/26-2-CapstoneDesign/BackEnd/blob/8b07585df31ecb8b902bcfa4aea0abb514c3a49f/youth-guide-api/src/main/java/com/youthguide/api/home/dto/CalendarResponse.java)
- `M` [youth-guide-api/src/main/java/com/youthguide/api/home/repository/CalendarQueryRepository.java](https://github.com/26-2-CapstoneDesign/BackEnd/blob/8b07585df31ecb8b902bcfa4aea0abb514c3a49f/youth-guide-api/src/main/java/com/youthguide/api/home/repository/CalendarQueryRepository.java)
- `A` [youth-guide-api/src/main/java/com/youthguide/api/home/repository/MemberExamSessionExclusionRepository.java](https://github.com/26-2-CapstoneDesign/BackEnd/blob/8b07585df31ecb8b902bcfa4aea0abb514c3a49f/youth-guide-api/src/main/java/com/youthguide/api/home/repository/MemberExamSessionExclusionRepository.java)
- `M` [youth-guide-api/src/main/java/com/youthguide/api/home/repository/projection/CalendarEventProjection.java](https://github.com/26-2-CapstoneDesign/BackEnd/blob/8b07585df31ecb8b902bcfa4aea0abb514c3a49f/youth-guide-api/src/main/java/com/youthguide/api/home/repository/projection/CalendarEventProjection.java)
- `A` [youth-guide-api/src/main/java/com/youthguide/api/home/service/CalendarExclusionService.java](https://github.com/26-2-CapstoneDesign/BackEnd/blob/8b07585df31ecb8b902bcfa4aea0abb514c3a49f/youth-guide-api/src/main/java/com/youthguide/api/home/service/CalendarExclusionService.java)
- `M` [youth-guide-api/src/main/java/com/youthguide/api/home/service/CalendarService.java](https://github.com/26-2-CapstoneDesign/BackEnd/blob/8b07585df31ecb8b902bcfa4aea0abb514c3a49f/youth-guide-api/src/main/java/com/youthguide/api/home/service/CalendarService.java)
- `A` [youth-guide-api/src/test/java/com/youthguide/api/home/service/CalendarExclusionServiceTest.java](https://github.com/26-2-CapstoneDesign/BackEnd/blob/8b07585df31ecb8b902bcfa4aea0abb514c3a49f/youth-guide-api/src/test/java/com/youthguide/api/home/service/CalendarExclusionServiceTest.java)
- `M` [youth-guide-api/src/test/java/com/youthguide/api/home/service/CalendarServiceTest.java](https://github.com/26-2-CapstoneDesign/BackEnd/blob/8b07585df31ecb8b902bcfa4aea0abb514c3a49f/youth-guide-api/src/test/java/com/youthguide/api/home/service/CalendarServiceTest.java)

## 해석

실행 흐름과 변경 이유는 관련 코드·PR·이슈를 확인한 뒤 [작업 문서](../work/README.md)에 기록합니다.
