import tempfile
import unittest
from pathlib import Path

from tools.notion_sync import convert_links, sync_notes


class FakeNotion:
    def __init__(self):
        self.created = []
        self.updated = []

    def create_page(self, parent, title, markdown):
        self.created.append((parent, title, markdown))
        return f"page-{len(self.created)}"

    def update_page(self, page_id, markdown):
        self.updated.append((page_id, markdown))


class NotionSyncTests(unittest.TestCase):
    def test_relative_links_become_github_links(self):
        text = "[member](../people/alice.md) [source](https://example.com)"
        result = convert_links(text, Path("analysis/work/task.md"), "owner/repo", "main")
        self.assertIn("https://github.com/owner/repo/blob/main/analysis/people/alice.md", result)
        self.assertIn("https://example.com", result)

    def test_creates_then_updates_same_page(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            note = root / "analysis" / "people" / "alice.md"
            note.parent.mkdir(parents=True)
            note.write_text("# Alice\n\nFirst version\n")
            mapping = root / ".notion-pages.json"
            client = FakeNotion()
            sync_notes(client, root / "analysis", mapping, "parent", "owner/repo", "main")
            self.assertEqual(len(client.created), 1)
            note.write_text("# Alice\n\nSecond version\n")
            sync_notes(client, root / "analysis", mapping, "parent", "owner/repo", "main")
            self.assertEqual(len(client.created), 1)
            self.assertEqual(len(client.updated), 1)
            self.assertIn("Second version", client.updated[0][1])


if __name__ == "__main__":
    unittest.main()
