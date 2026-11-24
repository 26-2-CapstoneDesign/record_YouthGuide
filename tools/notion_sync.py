"""Mirror reviewed Markdown notes to Notion (Markdown remains the source of truth).

Notion Markdown API: https://developers.notion.com/guides/data-apis/working-with-markdown-content
"""

import argparse
import hashlib
import json
import os
import re
import time
from pathlib import Path, PurePosixPath
from urllib.error import HTTPError
from urllib.parse import quote
from urllib.request import Request, urlopen


API_ROOT = "https://api.notion.com/v1"
VERSION = "2026-03-11"
LINK = re.compile(r"(?<!!)\[([^\]]+)\]\(([^)]+\.md)\)")


def convert_links(markdown, path, repository, branch):
    """Replace local Markdown links with public GitHub URLs for Notion readers."""
    def replace(match):
        label, target = match.groups()
        if target.startswith(("https://", "http://")):
            return match.group(0)
        parts = []
        for part in (PurePosixPath(path).parent / target).parts:
            if part == "..":
                if parts:
                    parts.pop()
            elif part != ".":
                parts.append(part)
        absolute = "/".join(parts)
        return f"[{label}](https://github.com/{repository}/blob/{quote(branch, safe='')}/{quote(absolute, safe='/')})"

    return LINK.sub(replace, markdown)


class NotionClient:
    def __init__(self, token):
        self.token = token

    def request(self, method, path, data):
        body = json.dumps(data, ensure_ascii=False).encode("utf-8")
        for attempt in range(6):
            request = Request(
                API_ROOT + path,
                data=body,
                method=method,
                headers={
                    "Authorization": f"Bearer {self.token}",
                    "Notion-Version": VERSION,
                    "Content-Type": "application/json",
                },
            )
            try:
                with urlopen(request, timeout=30) as response:
                    return json.load(response)
            except HTTPError as error:
                if error.code in (429, 529) and attempt < 5:
                    delay = int(error.headers.get("Retry-After", "0")) or min(2 ** attempt, 30)
                    time.sleep(delay)
                    continue
                detail = error.read().decode("utf-8", errors="replace")[:500]
                raise RuntimeError(f"Notion API {method} {path}: HTTP {error.code}: {detail}") from error
        raise RuntimeError("Notion API retry limit reached")

    def create_page(self, parent, title, markdown):
        response = self.request("POST", "/pages", {
            "parent": {"page_id": parent},
            "markdown_version": "v2",
            "markdown": markdown,
        })
        return response["id"]

    def update_page(self, page_id, markdown):
        self.request("PATCH", f"/pages/{page_id}/markdown", {
            "markdown_version": "v2",
            "type": "replace_content",
            "replace_content": {"new_str": markdown},
        })


def notes_to_sync(analysis):
    yield analysis / "README.md"
    for folder in ("people", "timeline", "work", "features"):
        yield from (path for path in sorted((analysis / folder).glob("*.md")) if path.name != "TEMPLATE.md")


def sync_notes(client, analysis, mapping_path, parent, repository, branch):
    analysis = Path(analysis)
    mapping_path = Path(mapping_path)
    mapping = json.loads(mapping_path.read_text()) if mapping_path.exists() else {}
    root = analysis.parent
    for path in notes_to_sync(analysis):
        if not path.exists():
            continue
        key = path.relative_to(root).as_posix()
        markdown = convert_links(path.read_text(), Path(key), repository, branch)
        digest = hashlib.sha256(markdown.encode()).hexdigest()
        existing = mapping.get(key)
        if existing and existing["sha256"] == digest:
            continue
        title = next((line[2:].strip() for line in markdown.splitlines() if line.startswith("# ")), path.stem)
        if existing:
            body = re.sub(r"^# [^\n]*\n\s*", "", markdown, count=1)
            client.update_page(existing["id"], body)
            page_id = existing["id"]
        else:
            page_id = client.create_page(parent, title, markdown)
        mapping[key] = {"id": page_id, "sha256": digest}
        mapping_path.parent.mkdir(parents=True, exist_ok=True)
        mapping_path.write_text(json.dumps(mapping, ensure_ascii=False, indent=2, sort_keys=True) + "\n")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--analysis", type=Path, default=Path("analysis"))
    parser.add_argument("--mapping", type=Path, default=Path("analysis/.notion-pages.json"))
    args = parser.parse_args()
    token = os.environ.get("NOTION_TOKEN")
    parent = os.environ.get("NOTION_PARENT_PAGE_ID")
    repository = os.environ.get("GITHUB_REPOSITORY", "26-2-CapstoneDesign/record_YouthGuide")
    branch = os.environ.get("GITHUB_REF_NAME", "main")
    if not token or not parent:
        raise SystemExit("NOTION_TOKEN and NOTION_PARENT_PAGE_ID are required")
    sync_notes(NotionClient(token), args.analysis, args.mapping, parent, repository, branch)


if __name__ == "__main__":
    main()
