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
    STARTER_TEMPLATES,
    active_session,
    attach_repository,
    attached_context,
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
        for name in STARTER_TEMPLATES:
            (templates / f"{name}.md").write_text("{{SESSION}} {{ROOT}}")
        subprocess.run(["git", "init", "-q", str(self.root)], check=True)

    def target_repo(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        target = Path(temp.name).resolve()
        subprocess.run(["git", "init", "-q", str(target)], check=True)
        (target / "AGENTS.md").write_text("target instructions")
        return target

    def test_attachment_preserves_target_and_binds_workspace(self):
        target = self.target_repo()
        before = subprocess.check_output(["git", "-C", str(target), "status", "--porcelain"])
        session = attach_repository(self.root, target, "provided-task")
        self.assertEqual((target / "AGENTS.md").read_text(), "target instructions")
        self.assertEqual(
            before, subprocess.check_output(["git", "-C", str(target), "status", "--porcelain"])
        )
        context = attached_context(self.root)
        self.assertEqual(context["target_root"], str(target))
        workspace = json.loads((session / "interview.code-workspace").read_text())
        self.assertEqual(workspace["folders"][0]["path"], str(target))
        self.assertIn(str(target), (session / "start.md").read_text())
        self.assertTrue(session.is_relative_to(self.root.resolve() / ".harness"))
        with self.assertRaises(FileExistsError):
            attach_repository(self.root, target, "provided-task")

    def test_attached_runner_refuses_wrong_repository_and_standalone_resumes(self):
        attach_repository(self.root, self.target_repo(), "provided-task")
        self.configure([{"argv": [sys.executable, "-c", "raise SystemExit(0)"]}])
        with self.assertRaisesRegex(ValueError, "Attached mode"):
            self.run_quiet()
        new_session(self.root, "standalone")
        self.assertIsNone(attached_context(self.root))
        self.assertEqual(self.run_quiet(), 0)

    def test_attachment_rejects_non_repo_subdirectory_and_nested_target(self):
        target = self.target_repo()
        sub = target / "sub"
        sub.mkdir()
        for candidate in (self.root, sub, Path(self.temp.name) / "missing"):
            with self.subTest(candidate=candidate), self.assertRaises(ValueError):
                attach_repository(self.root, candidate, "invalid")
        self.assertFalse((self.root / "docs/ACTIVE_SESSION").exists())

    def test_missing_or_malformed_attached_context_cannot_run_support_checks(self):
        session = attach_repository(self.root, self.target_repo(), "attached")
        context_file = session / "context.json"
        valid = json.loads(context_file.read_text())
        self.configure([{"argv": [sys.executable, "-c", 'open("wrong-root", "w").close()']}])
        for value in (
            {},
            [],
            {**valid, "target_root": "."},
            {**valid, "session_root": str(self.root)},
            {**valid, "target_root": str(self.root / "missing")},
        ):
            context_file.write_text(json.dumps(value))
            with self.subTest(value=value), self.assertRaises(ValueError):
                self.run_quiet()
        context_file.unlink()
        with self.assertRaisesRegex(ValueError, "missing context.json"):
            self.run_quiet()
        self.assertFalse((self.root / "wrong-root").exists())

    def test_replaced_target_checkout_is_rejected(self):
        target = self.target_repo()
        attach_repository(self.root, target, "attached")
        (target / ".git").rename(target / "old-git")
        with self.assertRaisesRegex(ValueError, "no longer a Git/worktree root"):
            attached_context(self.root)

    def test_command_config_requires_mapping(self):
        (self.root / "harness.commands.json").write_text("[]")
        with self.assertRaisesRegex(ValueError, "object mapping"):
            command_steps(self.root, "test")

    def test_attachment_accepts_a_real_linked_worktree(self):
        target = self.target_repo()
        subprocess.run(["git", "-C", str(target), "add", "AGENTS.md"], check=True)
        subprocess.run(
            [
                "git",
                "-C",
                str(target),
                "-c",
                "user.name=Test",
                "-c",
                "user.email=test@example.invalid",
                "commit",
                "-qm",
                "base",
            ],
            check=True,
        )
        extra = tempfile.TemporaryDirectory()
        self.addCleanup(extra.cleanup)
        worktree = Path(extra.name) / "worker"
        subprocess.run(
            ["git", "-C", str(target), "worktree", "add", "-qb", "worker", str(worktree)],
            check=True,
        )
        attach_repository(self.root, worktree, "linked")
        self.assertEqual(attached_context(self.root)["target_root"], str(worktree.resolve()))
        self.assertTrue((worktree / ".git").is_file())

    def configure(self, steps):
        (self.root / "harness.commands.json").write_text(json.dumps({"test": steps}))

    def run_quiet(self):
        with contextlib.redirect_stdout(io.StringIO()):
            return run_command(self.root, "test")

    def receipt(self):
        paths = list((self.root / ".harness/evidence").glob("*/receipt.json"))
        self.assertEqual(len(paths), 1)
        return json.loads(paths[0].read_text())

    def test_new_session_is_lean_and_never_overwrites(self):
        for name in ("decisions", "validation", "retrospective"):
            (self.root / "docs/templates" / f"{name}.md").write_text("optional record")
        path = new_session(self.root, "practice-01")
        self.assertEqual({p.name for p in path.iterdir()}, {"spec.md", "plan.md", "handoff.md"})
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
