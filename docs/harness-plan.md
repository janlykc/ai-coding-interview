# Harness implementation plan

Historical construction/verification record, not current operating instructions.
Current behavior is defined by root AGENTS.md and the relevant role/skill.
Results below describe the versions checked at the time.

This tracks harness construction. It is separate from any future interview task plan.

| Checkpoint | Scope | Acceptance | Status |
| --- | --- | --- | --- |
| H-C1 | Guide review and project conventions | H1, H2 | Complete |
| H-C2 | Root instructions, roles, skills and session templates | H3, H4, H7 | Complete; six skills structurally validated |
| H-C3 | Python package, command runner and failure-path tests | H2, H5 | Complete; current test results in setup-verification.md |
| H-C4 | VS Code workspace, prompts and durable handoff | H6 | Files complete; interactive rehearsal pending |
| H-C5 | Clean setup, lint, build, initial commit and remote | H1, H2, H7 | See setup-verification.md and Git history |

Testing strategy: exercise non-overwrite behavior, invalid session paths, missing
commands, command failure/timeout, evidence identity, and blocked executables; run
lint/format and build the package. Verify a fresh setup separately from the existing venv.

Delivery: local repository selected by the user, with its preconfigured origin.
Initial baseline may be committed and pushed under the user's setup request. Future
exercise sessions record their own destination and Git policy. No application or external
service is deployed as part of creating the harness.
