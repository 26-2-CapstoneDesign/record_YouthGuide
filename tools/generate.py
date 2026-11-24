"""Generate Obsidian and GitHub readable notes from two Git histories."""

import argparse
import hashlib
import subprocess
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from urllib.parse import quote
from zoneinfo import ZoneInfo


REPOS = {"FrontEnd": "FE", "BackEnd": "BE"}
ORG = "26-2-CapstoneDesign"
KST = ZoneInfo("Asia/Seoul")


def git(repo, *args):
    return subprocess.run(
        ["git", "-C", str(repo), *args],
        check=True,
        capture_output=True,
        text=True,
    ).stdout


def safe(value):
    return value.replace("\\", "\\\\").replace("[", "\\[").replace("]", "\\]").replace("\n", " ").strip()


def commits(repo):
    log = git(repo, "log", "--reverse", "--format=%H%x1f%an%x1f%ae%x1f%aI%x1f%cn%x1f%cI%x1f%s%x1e", "HEAD")
    for record in log.split("\x1e"):
        fields = record.strip("\n").split("\x1f")
        if len(fields) != 7:
            continue
        sha, author, email, authored, committer, committed, subject = fields
        parents = git(repo, "rev-list", "--parents", "-n", "1", sha).strip().split()[1:]
        if parents:
            changes = git(repo, "diff", "--name-status", "-M", parents[0], sha)
        else:
            changes = git(repo, "diff-tree", "--root", "--no-commit-id", "--name-status", "-r", sha)
        files = []
        for line in changes.splitlines():
            parts = line.split("\t")
            if len(parts) >= 2:
                files.append((parts[0], parts[-1]))
        yield {
            "sha": sha,
            "author": author,
            "email": email,
            "authored": authored,
            "committer": committer,
            "committed": committed,
            "subject": subject,
            "files": files,
            "parents": parents,
        }


def kst(value):
    return parse_date(value).astimezone(KST).strftime("%Y-%m-%d %H:%M KST")


def parse_date(value):
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def person_id(author, email):
    return hashlib.sha256((author or email).strip().casefold().encode()).hexdigest()[:12]


def write(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists() or path.read_text() != content:
        path.write_text(content)


def generate(sources, output):
    output = Path(output)
    all_commits = []
    snapshots = []
    for name, repo in sources.items():
        prefix = REPOS[name]
        head = git(repo, "rev-parse", "HEAD").strip()
        snapshots.append(f"- {name}: [`{head[:12]}`](https://github.com/{ORG}/{name}/commit/{head})")
        for commit in commits(repo):
            commit["repo"] = name
            commit["prefix"] = prefix
            commit["person_id"] = person_id(commit["author"], commit["email"])
            commit["filename"] = f"{prefix}-{commit['sha']}.md"
            all_commits.append(commit)

    all_commits.sort(key=lambda c: (parse_date(c["authored"]), c["repo"], c["sha"]))
    people = defaultdict(list)
    months = defaultdict(list)
    for c in all_commits:
        people[c["person_id"]].append(c)
        month = parse_date(c["authored"]).astimezone(KST).strftime("%Y-%m")
        months[month].append(c)
        file_lines = []
        for status, path in c["files"]:
            file_url = f"https://github.com/{ORG}/{c['repo']}/blob/{c['sha']}/{quote(path, safe='/')}"
            file_lines.append(f"- `{status}` [{safe(path)}]({file_url})")
        note = (
            f"# {safe(c['subject']) or c['sha'][:12]}\n\n"
            f"- 저장소: [{c['repo']}](https://github.com/{ORG}/{c['repo']})\n"
            f"- 작성자: [{safe(c['author'])}](../people/{c['person_id']}.md)\n"
            f"- 작성 시각: {kst(c['authored'])} (`{c['authored']}`)\n"
            f"- 커밋 시각: {kst(c['committed'])} (`{c['committed']}`)\n"
            f"- 커미터: {safe(c['committer'])}\n"
            f"- 원본: [커밋 `{c['sha']}`](https://github.com/{ORG}/{c['repo']}/commit/{c['sha']})\n\n"
            f"## 변경 파일\n\n" + ("\n".join(file_lines) if file_lines else "- 변경 파일 없음 (병합 커밋일 수 있음)") + "\n\n"
            "## 해석\n\n실행 흐름과 변경 이유는 관련 코드·PR·이슈를 확인한 뒤 [작업 문서](../work/README.md)에 기록합니다.\n"
        )
        write(output / "commits" / c["filename"], note)

    for pid, entries in people.items():
        name = safe(entries[-1]["author"])
        lines = [f"# {name}", "", f"기록된 커밋: {len(entries)}개. 공동 작업과 리뷰 기여는 별도 근거가 있을 때 [작업 문서](../work/README.md)에 기록합니다.", "", "## 커밋", ""]
        for c in reversed(entries):
            lines.append(f"- {kst(c['authored'])} · {c['repo']} · [{safe(c['subject']) or c['sha'][:12]}](../commits/{c['filename']})")
        write(output / "people" / f"{pid}.md", "\n".join(lines) + "\n")

    for month, entries in months.items():
        lines = [f"# {month} 작업 기록", ""]
        for c in entries:
            lines.append(f"- {kst(c['authored'])} · [{safe(c['author'])}](../people/{c['person_id']}.md) · {c['repo']} · [{safe(c['subject']) or c['sha'][:12]}](../commits/{c['filename']})")
        write(output / "timeline" / f"{month}.md", "\n".join(lines) + "\n")

    expected = {
        "commits": {c["filename"] for c in all_commits},
        "people": {f"{pid}.md" for pid in people},
        "timeline": {f"{month}.md" for month in months},
    }
    for folder, filenames in expected.items():
        for path in (output / folder).glob("*.md"):
            if path.name not in filenames:
                path.unlink()

    lines = ["# YouthGuide 작업 기록", "", "FrontEnd와 BackEnd의 `develop` 브랜치 커밋을 기준으로 생성한 기록입니다. 시각은 한국 시간으로 표시하고 커밋에는 원본 시간대를 함께 보존합니다.", "", "## 분석 기준", "", *snapshots, "", "## 팀원", ""]
    for pid, entries in sorted(people.items(), key=lambda item: item[1][-1]["author"].casefold()):
        lines.append(f"- [{safe(entries[-1]['author'])}](people/{pid}.md) · 커밋 {len(entries)}개")
    lines.extend(["", "## 월별 기록", ""])
    for month in sorted(months, reverse=True):
        lines.append(f"- [{month}](timeline/{month}.md) · 커밋 {len(months[month])}개")
    lines.extend(["", "## 기능과 작업", "", "- [작업별 분석](work/README.md)", "- [기능별 분석](features/README.md)", ""])
    write(output / "README.md", "\n".join(lines))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--frontend", type=Path, required=True)
    parser.add_argument("--backend", type=Path, required=True)
    parser.add_argument("--output", type=Path, default=Path("analysis"))
    args = parser.parse_args()
    generate({"FrontEnd": args.frontend, "BackEnd": args.backend}, args.output)


if __name__ == "__main__":
    main()
