# Optional project tooling

The README workflow works without installing these helpers. This page describes
the standalone Python foundation, optional command runner and harness self-checks.
Attached applications use their own setup and native commands.

## Project foundation

Uses a `pyproject.toml`, `src/` package layout, Hatchling build backend and a local
virtual environment, adapting the packaging conventions of the existing repositories.
The harness has no runtime dependencies. Development dependencies are pinned in
`requirements-dev.lock`; Python 3.11+ is required. Application dependencies and any
frontend manifest will be chosen when the actual problem is known.

```sh
make setup
make check
.venv/bin/interview doctor
```

`make setup` creates `.venv`, installs the pinned development tools and installs the
package in editable mode. `make check` runs lint/format checks, harness tests, package
build and doctor. On Windows or without Make, use `python -m venv .venv`, the venv's
Python to install `-r requirements-dev.lock`, then `pip install --no-build-isolation
--no-deps -e .`; run the equivalent commands listed in Makefile. The pinned file records
this verified development environment, not a universal cross-platform resolver lock.

## Configure application commands when the task is known

`harness.commands.json` starts empty. The harness never labels that as a passing test.
Add executable argument arrays with a working directory relative to this repository:

```json
{
  "test": [{"argv": [".venv/bin/python", "-m", "pytest", "tests/app"], "cwd": ".", "timeout_seconds": 120}],
  "lint": [],
  "build": [],
  "dev": []
}
```

This standalone Python example explicitly uses the environment created by make setup.
Use the target's actual interpreter/package manager for other stacks. The runner does
not activate an environment or rewrite PATH; bare python3 may resolve to system Python.
On Windows use the actual .venv/Scripts/python.exe path. This example is not a
prescribed application stack. Add multiple
steps for multiple components, using their own working directories. No shell
expansion is performed. `python3 scripts/harness.py run test` executes configured
steps in order, stops on failure and writes a receipt plus logs to ignored
`.harness/evidence/`. Use `run lint`, `run build`, or `run dev` similarly. Interactive
servers are often easier in a dedicated terminal; record their command/port in the
handoff and stop them when done. Never put credentials in command arguments or logs.
Summarize relevant evidence in the session's tracked `validation.md`.

## Verify the harness

```sh
python3 -m unittest discover -s tests/harness -v
python3 scripts/harness.py doctor
```

These checks cover harness tooling, not a future application. See
[setup verification](setup-verification.md) for the actual setup results and
remaining interactive rehearsal steps.
