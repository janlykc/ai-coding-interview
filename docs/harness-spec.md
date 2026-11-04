# Harness specification

Historical construction/verification record, not current operating instructions.
Current behavior is defined by root AGENTS.md and the relevant role/skill.
Results below describe the versions checked at the time.

Status: implemented initial baseline, 2026-11-03.
Source: the user's requested workflow and supplied interview preparation guide.
This document specifies the reusable harness; exercise specs live under docs/sessions/.

## Requirements and acceptance

| ID | Requirement | Acceptance |
| --- | --- | --- |
| H1 | Standalone, reusable project | Own Git root; no internal packages, product code or absolute runtime dependencies |
| H2 | Familiar Python project setup | pyproject.toml, src layout, editable install, pinned dev tools and working checks |
| H3 | Spec-driven collaboration | Human PE/product owner; PM/scribe authors spec; developer reconnaissance; explicit implementation agreement |
| H4 | Coordinator-led execution | Role instructions separate coordination/review from implementation and test execution; checkpoints trace to acceptance |
| H5 | Testing and delivery | Evidence records candidate state; unconfigured app checks fail; local demo default; explicit remote/deployment policy |
| H6 | App and IDE continuation | VS Code workspace and tasks; shared files; durable session handoff and single active writer convention |
| H7 | Repeatable practice | Session templates, non-overwriting creation, worktree guidance and retrospective-driven improvements |

## Design decisions

- Keep application language/framework choices open until the task arrives. Python
  tooling supports the harness and provides a familiar starting foundation.
- Use explicit role files plus repository-local skills. Do not hard-code native
  multi-agent configuration, model identifiers or application cloud accounts. The UI
  skill declares the verified local Paper MCP dependency and checks worker access.
- Keep the main agent's design context when it becomes coordinator. Load only relevant
  role instructions and checkpoint context into workers to control token cost.
- Use durable files to continue across interfaces; no dependence on automatic chat sync.
- Keep main as the reusable baseline; use exercise branches/worktrees for implementations.
- Keep validation failures and unavailable checks visible. A green tooling check does
  not certify an unknown application or prove human acceptance.

## Remaining human rehearsal

Sign-in, native skill discovery in each installed interface, actual subagent behavior,
screen-sharing ergonomics and live app-to-IDE-to-app continuation require an interactive
practice session. The files and tools enable these workflows; setup checks alone do not
establish that every installed interface exposes the same capabilities.
