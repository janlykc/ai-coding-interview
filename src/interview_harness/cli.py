"""Session creation and explicit application-command receipts; no AI runtime required."""

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

STARTER_TEMPLATES = ("spec", "plan", "handoff")


def root_from(start: Path) -> Path:
    for path in (start.resolve(), *start.resolve().parents):
        if (path / "harness.commands.json").is_file() and (path / "AGENTS.md").is_file():
            return path
    raise ValueError("Run from a harness checkout, or pass --root PATH.")


def git(root: Path, *args: str) -> str:
    result = subprocess.run(["git", "-C", str(root), *args], capture_output=True, text=True)
    return result.stdout.strip() if result.returncode == 0 else "unavailable"


def code_state(root: Path) -> dict:
    diff = subprocess.run(["git", "-C", str(root), "diff", "HEAD", "--binary"], capture_output=True)
    untracked = subprocess.run(
        ["git", "-C", str(root), "ls-files", "--others", "--exclude-standard", "-z"],
        capture_output=True,
    )
    hashes = {}
    for name in untracked.stdout.split(b"\0"):
        if name:
            relative = os.fsdecode(name)
            path = root / relative
            if path.is_file() and not path.is_symlink():
                hashes[relative] = hashlib.sha256(path.read_bytes()).hexdigest()
    return {
        "head": git(root, "rev-parse", "HEAD"),
        "branch": git(root, "branch", "--show-current"),
        "status": git(root, "status", "--short"),
        "diff_sha256": hashlib.sha256(diff.stdout).hexdigest() if diff.returncode == 0 else None,
        "untracked_sha256": hashes,
    }


def new_session(root: Path, name: str, *, attached: bool = False) -> Path:
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        raise ValueError("Use lowercase letters, digits and single hyphens for the session name.")
    destination = root / (".harness/sessions" if attached else "docs/sessions") / name
    # Read templates before mutation; existing sessions are never overwritten.
    contents = {
        item: (root / "docs" / "templates" / f"{item}.md")
        .read_text()
        .replace("{{SESSION}}", name)
        .replace("{{ROOT}}", str(root))
        for item in STARTER_TEMPLATES
    }
    destination.mkdir(parents=True, exist_ok=False)
    for item, content in contents.items():
        (destination / f"{item}.md").write_text(content)
    (root / "docs" / "ACTIVE_SESSION").write_text(str(destination.relative_to(root)) + "\n")
    return destination


def active_session(root: Path) -> str:
    pointer = root / "docs" / "ACTIVE_SESSION"
    if not pointer.exists():
        return "none (start with new-session <slug>)"
    relative = pointer.read_text().strip()
    target = (root / relative).resolve()
    if (
        not any(
            target.is_relative_to((root / folder).resolve())
            for folder in ("docs/sessions", ".harness/sessions")
        )
        or not target.is_dir()
    ):
        raise ValueError("ACTIVE_SESSION must point to an existing harness session folder.")
    return relative


def attach_repository(root: Path, target: Path, name: str) -> Path:
    root, target = root.resolve(), target.expanduser().resolve()
    if not target.is_dir():
        raise ValueError("Target must be an existing Git checkout; clone it first.")
    top = git(target, "rev-parse", "--show-toplevel")
    if top == "unavailable" or Path(top).resolve() != target:
        raise ValueError("Pass the target Git/worktree root, not a subdirectory.")
    if target.is_relative_to(root) or root.is_relative_to(target):
        raise ValueError("Use separate, non-nested target and harness checkouts.")
    session = new_session(root, name, attached=True)
    context = {
        "mode": "attached",
        "harness_root": str(root),
        "target_root": str(target),
        "session_root": str(session),
        "target_branch_at_attach": git(target, "branch", "--show-current"),
        "target_head_at_attach": git(target, "rev-parse", "HEAD"),
    }
    (session / "context.json").write_text(json.dumps(context, indent=2) + "\n")
    prompt = f"""Work in attached-repository mode. I am the PE/product owner.
Implementation checkout: {target}
Support harness: {root}
Session and planning records: {session}

First read {session / "context.json"} and {session / "handoff.md"}.
Inspect the target's applicable AGENTS.md files and project conventions. Read
{root / "AGENTS.md"} as supporting workflow guidance, and explicitly load
{root / ".agents/skills/engineering-spec/SKILL.md"} for design or
{root / ".agents/skills/engineering-handoff/SKILL.md"} for continuation.
Resolve role/skill paths from the harness and application paths from the target.
Use the target's stack, tests, dependencies, branch and remotes. Do not install the
harness as an application dependency or replace target instructions/configuration.
Run each worker in its explicitly assigned target worktree and give it the absolute harness role and
session paths. Preserve target-specific requirements; raise genuine conflicts.
Begin design with me, or resume the agreed checkpoint. Do not invent the task.
"""
    (session / "start.md").write_text(prompt)
    handoff = session / "handoff.md"
    handoff.write_text(
        handoff.read_text().replace(
            f"Repository/worktree: {root}", f"Repository/worktree: {target}"
        )
        + f"\n## Attached repository\n\n"
        f"Implementation checkout: {target}\nSupport harness: {root}\n"
        f"Planning records: {session}\n"
        "The implementation checkout above is the application worktree. "
        "Verify its Git state before work. Target files have not been changed.\n"
    )
    plan = session / "plan.md"
    plan.write_text(
        plan.read_text().replace(
            "Standalone: optional harness.commands.json. Attached: target-native commands.",
            "Use target-native commands (not the harness runner).",
        )
        + f"\nImplementation Git checkout: {target}\n"
        + f"Initial branch: {context['target_branch_at_attach']}\n"
        + "Confirm target remote and authorization before pushing.\n"
    )
    workspace = session / "interview.code-workspace"
    workspace.write_text(
        json.dumps(
            {
                "folders": [
                    {"name": "implementation", "path": str(target)},
                    {"name": "support-harness", "path": str(root)},
                ],
                "settings": {"workbench.startupEditor": "none"},
            },
            indent=2,
        )
        + "\n"
    )
    return session


def attached_context(root: Path) -> dict | None:
    if not (root / "docs/ACTIVE_SESSION").exists():
        return None
    session = root / active_session(root)
    path = session / "context.json"
    if not path.exists():
        if session.resolve().is_relative_to((root / ".harness/sessions").resolve()):
            raise ValueError(
                "Attached session is missing context.json; establish its target first."
            )
        return None
    context = json.loads(path.read_text())
    keys = ("harness_root", "target_root", "session_root")
    if not isinstance(context, dict) or context.get("mode") != "attached":
        raise ValueError("context.json must describe mode 'attached'.")
    if not all(
        isinstance(context.get(key), str) and Path(context[key]).is_absolute() for key in keys
    ):
        raise ValueError(
            "Attached context requires absolute harness_root, target_root and session_root."
        )
    if Path(context["harness_root"]).resolve() != root.resolve() or (
        Path(context["session_root"]).resolve() != session.resolve()
    ):
        raise ValueError(
            "Attached context paths do not match this harness/session; rebind them first."
        )
    target = Path(context["target_root"]).resolve()
    if not target.is_dir():
        raise ValueError("Attached target is missing; restore the checkout path.")
    top = git(target, "rev-parse", "--show-toplevel")
    if top == "unavailable" or Path(top).resolve() != target:
        raise ValueError("Attached target is no longer a Git/worktree root.")
    if target.is_relative_to(root.resolve()) or root.resolve().is_relative_to(target):
        raise ValueError("Use separate, non-nested target and harness checkouts.")
    return context


def command_config(root: Path) -> dict:
    config = json.loads((root / "harness.commands.json").read_text())
    if not isinstance(config, dict):
        raise ValueError("harness.commands.json must be an object mapping command names to steps.")
    return config


def command_steps(root: Path, name: str) -> list[dict]:
    config = command_config(root)
    steps = config.get(name)
    if not steps:
        raise ValueError(f"Application command {name!r} is NOT CONFIGURED; no check ran.")
    if not isinstance(steps, list):
        raise ValueError("Each command must be a list of steps.")
    for step in steps:
        if not isinstance(step, dict):
            raise ValueError("Each step must be an object.")
        argv = step.get("argv")
        if (
            not isinstance(argv, list)
            or not argv
            or not all(isinstance(x, str) and x for x in argv)
        ):
            raise ValueError("argv must be a nonempty list of strings; shell text is not accepted.")
        directory = step.get("cwd", ".")
        if not isinstance(directory, str):
            raise ValueError("cwd must be a repository-relative directory.")
        cwd = (root / directory).resolve()
        if not cwd.is_relative_to(root.resolve()) or not cwd.is_dir():
            raise ValueError("cwd must be an existing directory inside the repository.")
        timeout = step.get("timeout_seconds", 120)
        if type(timeout) is not int or timeout < 1:
            raise ValueError("timeout_seconds must be a positive integer.")
    return steps


def run_command(root: Path, name: str) -> int:
    if attached_context(root):
        raise ValueError(
            "Attached mode: run application commands in the target checkout, "
            "then record target code state and results in session validation.md."
        )
    steps = command_steps(root, name)  # Validate all steps before executing any.
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ")
    evidence = root / ".harness" / "evidence" / f"{stamp}-{name}"
    evidence.mkdir(parents=True, exist_ok=False)
    receipt = {"command": name, "started_utc": stamp, "before": code_state(root), "steps": []}
    exit_code = 0
    try:
        for number, step in enumerate(steps, 1):
            log_path = evidence / f"{number}.log"
            print(f"Running: {step['argv']} (cwd={step.get('cwd', '.')})", flush=True)
            with log_path.open("w") as log:
                try:
                    result = subprocess.run(
                        step["argv"],
                        cwd=root / step.get("cwd", "."),
                        stdout=log,
                        stderr=subprocess.STDOUT,
                        timeout=step.get("timeout_seconds", 120),
                    )
                    code = result.returncode
                    outcome = "pass" if code == 0 else "fail"
                except subprocess.TimeoutExpired:
                    code, outcome = 124, "timeout"
                    log.write("\nCommand timed out. Check for child services before retrying.\n")
                except OSError as exc:
                    code, outcome = 127, "blocked"
                    log.write(f"{exc}\n")
            print(log_path.read_text(errors="replace"), end="")
            receipt["steps"].append(
                {**step, "exit_code": code, "result": outcome, "log": log_path.name}
            )
            if code:
                exit_code = code if code > 0 else 1
                break
    except KeyboardInterrupt:
        exit_code = 130
        receipt["interrupted"] = True
    finally:
        receipt["exit_code"] = exit_code
        receipt["after"] = code_state(root)
        receipt["code_changed_during_run"] = receipt["before"] != receipt["after"]
        (evidence / "receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
        print(f"Receipt: {evidence / 'receipt.json'}")
    return exit_code


def doctor(root: Path) -> int:
    missing = []
    for relative in [
        "AGENTS.md",
        "pyproject.toml",
        "harness.commands.json",
        "interview.code-workspace",
        *[f"docs/templates/{item}.md" for item in STARTER_TEMPLATES],
        *[
            f"ai_team/{role}/AGENTS.md"
            for role in [
                "coordinator",
                "reviewer",
                "spec_author",
                "developer",
                "qa",
                "ux",
                "delivery",
            ]
        ],
        *[
            f".agents/skills/{skill}/SKILL.md"
            for skill in [
                "engineering-spec",
                "engineering-deliver",
                "engineering-handoff",
                "engineering-ui-design",
                "engineering-review",
                "engineering-test-deploy",
            ]
        ],
    ]:
        if not (root / relative).is_file():
            missing.append(relative)
    print(f"Repository: {root}\nPython: {sys.version.split()[0]}")
    git_available = shutil.which("git") is not None
    print(f"Git: {shutil.which('git') or 'MISSING'}")
    print(f"Codex CLI (optional): {shutil.which('codex') or 'not on PATH; IDE/app can be used'}")
    print(f"Active session: {active_session(root)}")
    context = attached_context(root)
    if context:
        print(
            f"Attached target: {context['target_root']}; run its native application checks there."
        )
        print("Configuration below belongs to the support harness, not the attached application.")
    config = command_config(root)
    for name in ("test", "lint", "build", "dev"):
        if config.get(name):
            command_steps(root, name)
            print(f"Application {name}: configured (not executed)")
        else:
            print(f"Application {name}: NOT CONFIGURED")
    for path in missing:
        print(f"MISSING: {path}")
    print("Manual preflight: sign-in, model/tools, subagents, screen sharing and app/IDE handoff.")
    print("Doctor checks the harness only; it does not validate the application.")
    return int(bool(missing) or not git_available)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, help="Harness checkout (default: discover from cwd)")
    subs = parser.add_subparsers(dest="action", required=True)
    subs.add_parser("doctor")
    subs.add_parser("status")
    session = subs.add_parser("new-session")
    session.add_argument("name")
    attach = subs.add_parser("attach", help="Use this harness alongside an existing checkout")
    attach.add_argument("target", type=Path)
    attach.add_argument("--session", required=True)
    run = subs.add_parser("run")
    run.add_argument("name", choices=["test", "lint", "build", "dev"])
    args = parser.parse_args(argv)
    try:
        root = root_from(args.root or Path.cwd())
        if args.action == "doctor":
            return doctor(root)
        if args.action == "new-session":
            print(new_session(root, args.name))
        elif args.action == "attach":
            session_path = attach_repository(root, args.target, args.session)
            print(f"Workspace: {session_path / 'interview.code-workspace'}")
            print(f"Start/resume prompt: {session_path / 'start.md'}")
        elif args.action == "status":
            print(f"Active session: {active_session(root)}")
            context = attached_context(root)
            if context:
                print(json.dumps(context, indent=2))
                target = Path(context["target_root"])
                if not target.is_dir():
                    raise ValueError("Attached target is missing; restore the checkout path.")
                print("Target Git state:")
                print(json.dumps(code_state(target), indent=2))
            else:
                print(json.dumps(code_state(root), indent=2))
        else:
            return run_command(root, args.name)
        return 0
    except (ValueError, OSError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
