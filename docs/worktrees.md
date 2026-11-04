# Parallel implementation with Git worktrees

Use worktrees when components have independent boundaries and enough work to justify
parallel agents. A small task may be faster in one checkout. Decompose first: PM/spec
and developer reconnaissance establish interfaces; coordinator names owners and checkpoints.
Worktrees isolate files, not ports, databases, credentials, remote services or dependencies.

## Plan the split

In the active plan, record each task's branch, absolute worktree path, owner, owned
paths, base SHA, dependency, acceptance IDs, test command and port/environment if needed.
Use one writer per worktree and one integration owner. Shared contracts belong to one
owner; either land them first or branch dependents from the agreed contract commit.
Uncommitted edits in the original checkout are not included in a new worktree. Preserve
those edits and explicitly decide whether they belong in the candidate before branching.

## Example using native Git

Run from the **implementation repository**, substituting the example names/paths.
Inspect existing worktrees and select an agreed, committed starting point first:

```sh
git status --short --branch
git worktree list
BASE=$(git rev-parse HEAD)
git worktree add -b interview/integration ../interview-integration "$BASE"
git worktree add -b interview/api ../interview-api "$BASE"
git worktree add -b interview/ui ../interview-ui "$BASE"
```

These commands are examples, not an instruction to invent API/UI work for every task.
Use distinct branch/path names per exercise. If the repository has no commits, agree
and create a legitimate baseline first. Never reset or stash someone else's work to
make the example fit. In an attached session, all these are worktrees of the provided
repo, not the support harness.

The explicit worker worktree assignment takes precedence over the original target_root
for application edits/tests/Git. Verify the checkout shares the target's resolved Git
common directory (`git rev-parse --path-format=absolute --git-common-dir`). Keep shared
context.json stable while workers run; record the current integration path in handoff.md.

Each worker reads target instructions from its own checkout, then explicitly loads its
harness role and the shared session. Keep PM/spec and coordinator/plan writes with their
owners in the session location; do not create competing specs in every worktree. Each
checkout uses its own environment/build outputs; do not symlink a mutable venv or
node_modules across branches with different dependency states.

## Review and integration

Developers report ready-for-review with exact code state and validation. Freeze writes
for a review of uncommitted changes. The independent CR agent reviews; developers fix;
reviewer rechecks affected changes. Delivery commits the agreed snapshot after staged
inspection. A draft/WIP commit can stabilize a review candidate but is not an accepted
checkpoint and should be labeled accordingly.

The integration owner merges accepted branches in dependency order. For example,
from the clean integration checkout, after both contributions are ready:

```sh
git merge --no-ff --no-edit interview/api
git merge --no-ff --no-edit interview/ui
git log --oneline --graph -8
git rev-parse HEAD
git rev-parse 'HEAD^{tree}'
```

If a merge conflicts, stop the sequence and assign resolution to the relevant developer.
The coordinator does not implement the fix. Inspect/review the resolved diff, rerun
affected checks and preserve the prior result until resolution is validated. A clean
merge can still contain semantic conflicts: run combined contract/integration checks,
review the complete submission diff, then test/deploy and QA the integration candidate.
A review of each component alone does not qualify the combined application.

If the destination branch advances, re-evaluate against the current destination and
refresh affected review/test evidence. Do not assume `main` or `dev` is the destination;
record the task's actual target in the plan. Keep an unreviewed moving ref out of a
final submission. See [submission](submission.md).

## Cleanup

After integration and acceptance, ensure the worker is stopped, its checkout is clean,
and its commits are retained in the intended branch/history. Then remove the specific
worktree with `git worktree remove <path>` and use non-forced branch deletion when safe.
Do not force removal, prune unrelated worktrees, or delete the only copy of unfinished
work. Keep unfinished work and record its owner/status in the handoff.
