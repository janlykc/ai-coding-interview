import contextlib
import io
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))
from interview_harness.cli import (  # noqa: E402
    TEMPLATES,
    active_session,
    command_steps,
    new_session,
    root_from,
    run_command,
)


class HarnessTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "AGENTS.md").write_text("test fixture")
        (self.root / ".gitignore").write_text(".harness/\n")
        self.configure([])
        templates = self.root / "docs/templates"
        templates.mkdir(parents=True)
        for name in TEMPLATES:
            (templates / f"{name}.md").write_text("{{SESSION}} {{ROOT}}")
        subprocess.run(["git", "init", "-q", str(self.root)], check=True)

    def configure(self, steps):
        (self.root / "harness.commands.json").write_text(json.dumps({"test": steps}))

    def run_quiet(self):
        with contextlib.redirect_stdout(io.StringIO()):
            return run_command(self.root, "test")

    def receipt(self):
        paths = list((self.root / ".harness/evidence").glob("*/receipt.json"))
        self.assertEqual(len(paths), 1)
        return json.loads(paths[0].read_text())

    def test_new_session_is_complete_and_never_overwrites(self):
        path = new_session(self.root, "practice-01")
        self.assertEqual(len(list(path.glob("*.md"))), len(TEMPLATES))
        self.assertIn(str(self.root), (path / "handoff.md").read_text())
        (path / "spec.md").write_text("human decision")
        with self.assertRaises(FileExistsError):
            new_session(self.root, "practice-01")
        self.assertEqual((path / "spec.md").read_text(), "human decision")
        self.assertEqual(active_session(self.root), "docs/sessions/practice-01")

    def test_invalid_slug_cannot_escape_session_directory(self):
        for slug in ("../escape", "/absolute", "", "a/b", "A", "a--b"):
            with self.subTest(slug=slug), self.assertRaises(ValueError):
                new_session(self.root, slug)

    def test_missing_template_does_not_create_partial_session(self):
        (self.root / "docs/templates/spec.md").unlink()
        with self.assertRaises(FileNotFoundError):
            new_session(self.root, "missing")
        self.assertFalse((self.root / "docs/sessions/missing").exists())

    def test_unconfigured_test_does_not_report_success_or_create_receipt(self):
        with self.assertRaisesRegex(ValueError, "NOT CONFIGURED"):
            self.run_quiet()
        self.assertFalse((self.root / ".harness").exists())

    def test_command_failure_stops_following_step_and_records_result(self):
        self.configure(
            [
                {"argv": [sys.executable, "-c", "raise SystemExit(7)"]},
                {"argv": [sys.executable, "-c", 'open("should-not-exist", "w").close()']},
            ]
        )
        self.assertEqual(self.run_quiet(), 7)
        self.assertFalse((self.root / "should-not-exist").exists())
        self.assertEqual(self.receipt()["steps"][0]["result"], "fail")
        self.assertEqual(len(self.receipt()["steps"]), 1)

    def test_success_and_code_change_are_recorded_separately(self):
        self.configure([{"argv": [sys.executable, "-c", 'open("changed.txt", "w").write("new")']}])
        self.assertEqual(self.run_quiet(), 0)
        result = self.receipt()
        self.assertEqual(result["steps"][0]["result"], "pass")
        self.assertTrue(result["code_changed_during_run"])
        self.assertIn("changed.txt", result["after"]["untracked_sha256"])

    def test_missing_executable_is_blocked(self):
        self.configure([{"argv": ["interview-nonexistent-executable-xyz"]}])
        self.assertEqual(self.run_quiet(), 127)
        self.assertEqual(self.receipt()["steps"][0]["result"], "blocked")

    def test_timeout_is_not_a_pass(self):
        self.configure(
            [{"argv": [sys.executable, "-c", "import time; time.sleep(3)"], "timeout_seconds": 1}]
        )
        self.assertEqual(self.run_quiet(), 124)
        self.assertEqual(self.receipt()["steps"][0]["result"], "timeout")

    def test_all_steps_validated_before_execution(self):
        self.configure(
            [
                {"argv": [sys.executable, "-c", 'open("should-not-exist", "w").close()']},
                {"argv": ["echo", "outside"], "cwd": ".."},
            ]
        )
        with self.assertRaises(ValueError):
            self.run_quiet()
        self.assertFalse((self.root / "should-not-exist").exists())

    def test_shell_string_is_rejected(self):
        self.configure([{"argv": "echo hello; echo no"}])
        with self.assertRaises(ValueError):
            command_steps(self.root, "test")

    def test_discovery_from_subfolder_and_invalid_pointer(self):
        self.assertEqual(root_from(self.root / "docs"), self.root.resolve())
        (self.root / "docs/ACTIVE_SESSION").write_text("../../")
        with self.assertRaises(ValueError):
            active_session(self.root)


if __name__ == "__main__":
    unittest.main()
