# Implementation plan — {{SESSION}}

Owner: coordinator. Execution source of truth; requirements remain in spec.md.
Status and actual time budget, if relevant:

## Environment and Git policy

- Repository/worktree: record absolute path in handoff.
- Application install/start/test/build commands: discover and record. Standalone: optional harness.commands.json. Attached: target-native commands.
- Local commits: coherent checkpoints after coordinator review.
- Push: record actual session authorization and exact remote/branch; do not assume it.
- Deployment: local demonstration by default; external target/authorization not specified.
- Delegation: preferred when useful; honor requested direct execution or use sequential roles when unavailable.

## Design gaps and readiness

Record only unresolved gaps that affect this plan: missing behavior/contract, required
decision or investigation, owner, affected checkpoint and resolution. Revisit the spec
with agreed answers. Do not dispatch work that depends on an unresolved critical gap;
unaffected authorized checkpoints may proceed.

## Checkpoints

Replace the row below when the actual task is known. Do not dispatch an undefined task.

| ID | Outcome / acceptance IDs | Owner and files | Dependencies | Validation / exit | Status |
| --- | --- | --- | --- | --- | --- |
| C1 | To be agreed | | | | planned |

## Checkpoint review and commits

For each checkpoint: readiness decision, remaining limits and links to relevant
review/validation/submission records. Keep detailed evidence in its owning record.

## Scope changes

Decision reference, affected acceptance IDs/checkpoints, agreed adjustment:

## Parallel work and submission (when relevant)

| Task | Owner / owned files | Worktree / branch / base SHA | Dependencies | Environment / port | Integration order |
| --- | --- | --- | --- | --- | --- |

Integration owner and destination branch:
Independent CR owner and review route (local subagent / Codex local / provider):
Local run/preview and QA owner:
Submission finish line and required checks:
Use review.md and submission.md templates when useful; keep the record brief.
