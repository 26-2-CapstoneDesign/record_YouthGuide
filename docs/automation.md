# 작업 기록 자동화

이 저장소의 `analysis/` 폴더는 Obsidian vault로 열 수 있습니다. 상대 경로 Markdown 링크는 Obsidian 그래프와 GitHub 양쪽에서 작동합니다.

## 수집 범위

- `26-2-CapstoneDesign/FrontEnd`의 `develop` 브랜치
- `26-2-CapstoneDesign/BackEnd`의 `develop` 브랜치
- 작성자와 커미터, 원본 시간대와 한국 시간, 커밋 메시지, 변경 파일, 원본 커밋 링크

`analysis/commits`, `analysis/people`, `analysis/timeline`, `analysis/README.md`는 자동 생성 파일입니다. 직접 편집하지 마세요. 기능 해설은 `analysis/work`와 `analysis/features`에 작성합니다. 이 두 폴더의 수동 문서는 자동 생성기가 덮어쓰지 않습니다.

작성자 표기는 Git 커밋의 author 필드를 따릅니다. 동일한 이름으로 기록된 커밋은 한 페이지에 묶이며, 공동 작업·리뷰·실제 담당 범위는 커밋만으로 확인할 수 없으므로 작업 문서에 근거와 함께 기록해야 합니다. GitHub 계정명과 표시 이름이 다른 팀원은 작업 문서에서 명시적으로 연결하세요.

## 자동 실행

`.github/workflows/analysis-sync.yml`은 15분마다, 수동 실행 시, 이 저장소의 분석 파일이 `main`에 반영될 때 실행됩니다. GitHub 예약 실행은 정확한 시각보다 늦어질 수 있습니다. 워크플로는 두 비공개 저장소를 **읽기 전용 토큰**으로 체크아웃하고 Markdown을 재생성한 뒤, 변경이 있으면 이 저장소에 커밋합니다.

GitHub Actions 저장소 비밀 값:

| 이름 | 용도 |
| --- | --- |
| `SOURCE_REPOS_TOKEN` | FrontEnd·BackEnd 저장소의 Contents: read 권한을 가진 fine-grained PAT |
| `NOTION_TOKEN` | Notion 연결 토큰. 없으면 Notion 단계만 건너뜀 |

조직 정책상 deploy key가 비활성화되어 있습니다. GitHub의 fine-grained PAT을 만들어 `26-2-CapstoneDesign` 조직의 **FrontEnd와 BackEnd 두 저장소만** 선택하고 `Contents: read` 권한을 부여합니다. 조직의 토큰 승인 정책이 있다면 승인도 완료해야 합니다. 토큰과 Notion 연결 토큰은 GitHub Actions 비밀 값에만 저장하고 파일에는 넣지 않습니다.

`SOURCE_REPOS_TOKEN`이 아직 없으면 워크플로는 경고를 남기고 수집 단계를 건너뜁니다. 비밀 값을 저장한 뒤 다음 예약 실행이나 수동 실행부터 갱신됩니다.

## Notion 연결

대상 상위 페이지: `https://app.notion.com/p/26-2-3db7ea032e9880149835d874bc9fbd48`

1. [Notion 연결 설정](https://www.notion.com/profile/integrations)에서 내부 연결을 만들고 페이지 읽기·삽입·수정 권한을 부여합니다.
2. 대상 상위 페이지에서 그 연결을 추가합니다.
3. 연결 토큰을 이 저장소의 Actions 비밀 값 `NOTION_TOKEN`으로 저장합니다. 토큰을 Markdown이나 채팅에 붙여넣지 않습니다.
4. GitHub Actions의 **Sync project history and Notion** 워크플로를 수동 실행합니다.

Notion에는 팀원·월별 기록·작업·기능 페이지를 미러링합니다. 487개의 개별 커밋 페이지는 Obsidian/GitHub에 두어 Notion을 탐색용으로 유지합니다. Notion 페이지 ID와 내용 해시는 `analysis/.notion-pages.json`에 저장되어 다음 실행 때 같은 페이지를 갱신합니다. Notion에서 동기화 페이지의 본문을 직접 고치면 다음 실행 때 Markdown 내용으로 교체됩니다.

Notion 동기화는 [Notion Markdown API v2](https://developers.notion.com/guides/data-apis/working-with-markdown-content)를 사용합니다. API 제한 응답은 `Retry-After`에 따라 재시도합니다.

## 로컬 실행

```sh
python3 -m unittest discover -s tests -v
python3 tools/generate.py --frontend /path/to/FrontEnd --backend /path/to/BackEnd
```

Notion 동기화는 `NOTION_TOKEN`, `NOTION_PARENT_PAGE_ID`, `GITHUB_REPOSITORY`, `GITHUB_REF_NAME` 환경 변수를 설정한 뒤 `python3 tools/notion_sync.py`로 실행할 수 있습니다.
