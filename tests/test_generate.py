import subprocess
import tempfile
import unittest
from pathlib import Path

from tools.generate import generate, kst, parse_date, person_id


def git(repo, *args, env=None):
    return subprocess.run(
        ["git", "-C", str(repo), *args],
        check=True,
        capture_output=True,
        text=True,
        env=env,
    ).stdout.strip()


class GenerateTests(unittest.TestCase):
    def test_dates_with_different_offsets_sort_by_actual_time(self):
        self.assertLess(parse_date("2026-11-20T09:00:00+09:00"), parse_date("2026-11-20T01:00:00Z"))

    def test_same_author_with_two_commit_emails_has_one_person_note(self):
        self.assertEqual(person_id("eoyan", "first@example.com"), person_id("eoyan", "second@example.com"))

    def test_utc_z_timestamp_is_converted_to_kst(self):
        self.assertEqual(kst("2026-10-08T19:39:14Z"), "2026-10-09 04:39 KST")

    def test_generates_linked_commit_person_and_timeline_notes_idempotently(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "source"
            source.mkdir()
            git(source, "init", "-q")
            git(source, "config", "user.name", "Test Author")
            git(source, "config", "user.email", "test@example.com")
            (source / "service.py").write_text("print('hello')\n")
            git(source, "add", ".")
            git(source, "commit", "-qm", "Add service", env={
                **__import__("os").environ,
                "GIT_AUTHOR_DATE": "2026-11-20T10:00:00+09:00",
                "GIT_COMMITTER_DATE": "2026-11-20T10:05:00+09:00",
            })
            sha = git(source, "rev-parse", "HEAD")
            output = root / "analysis"
            generate({"FrontEnd": source}, output)

            commit = output / "commits" / f"FE-{sha}.md"
            self.assertTrue(commit.exists())
            self.assertIn("2026-11-20 10:00 KST", commit.read_text())
            self.assertIn("service.py", commit.read_text())
            self.assertIn("../people/", commit.read_text())
            people = list((output / "people").glob("*.md"))
            self.assertEqual(len(people), 1)
            self.assertIn(f"../commits/FE-{sha}.md", people[0].read_text())
            self.assertIn(f"../commits/FE-{sha}.md", (output / "timeline" / "2026-11.md").read_text())

            first = {p.relative_to(output): p.read_bytes() for p in output.rglob("*.md")}
            generate({"FrontEnd": source}, output)
            second = {p.relative_to(output): p.read_bytes() for p in output.rglob("*.md")}
            self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
