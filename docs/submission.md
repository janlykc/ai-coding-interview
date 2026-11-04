# Check-in, code review, test deployment and submission

The demonstrable loop is: implement a bounded slice → inspect/test → independent CR
→ fix and recheck → commit → integrate → verify the combined candidate → run/QA →
submit by the agreed route. A single component skips unnecessary integration work.
The human can see the meaningful diff, review findings, test evidence and Git history.

## 1. Establish the candidate and finish line

Record the implementation repo, worktree, branch, agreed destination/base, head/tree,
dependencies and acceptance IDs. Decide whether the deliverable is a local demo,
pushed branch, PR or merge; remote deployment is a separate choice. Do not assume the
interviewer wants a PR or that their repository uses our branch names.
For parallel sections, use [the worktree procedure](worktrees.md).

## 2. Review and check in

Stop writers for an uncommitted review. Inspect tracked and untracked changes; record
what the snapshot contains. Assign `ai_team/reviewer/AGENTS.md` to a fresh reviewer
that did not implement the candidate. Review code paths and contracts, not just a
summary of passed tests. Use `docs/templates/review.md` for a short session receipt.
Give the reviewer raw evidence without the desired conclusion.

Coordinator dispositions findings; developer fixes; reviewer rechecks the affected
change. Inspect the staged diff and stage explicit paths. Commit coherent work with
a message describing behavior. Record the resulting SHA and verify that its content
matches the reviewed snapshot. If content changed during staging/commit, re-review the
changed scope. A draft commit can freeze work for review but is not acceptance.
One independent reviewer is the interview default. Coordinator oversight is useful
but is not a second independent review when that coordinator helped implement.

## 3. Codex review options

Use the path supported by the current environment. Local CLI examples, verified with
`codex-cli 0.144.6 --help` on 2026-11-03, run from the implementation worktree:

```sh
# Before committing: includes staged, unstaged and untracked changes.
codex review --uncommitted

# After committing: review the submission relative to the agreed base branch.
codex review --base <base-branch>

# Review only one commit's changes (not the whole feature).
codex review --commit <commit-sha>
```

Choose one appropriate scope; do not run all three by rote. Inspect `codex review --help`
on another version. Do not combine custom prompt text with scope flags unless that
installed version supports it. In the app/IDE, give a fresh review chat the target
checkout, exact base/head, role path, spec and full diff instead. A support-repo role
is not automatically loaded by a CLI/provider reviewing a different repository;
explicitly supply/read it in a review chat when you need that rubric. The standard
CLI path still uses the target's own applicable instructions. Capture the actual
review scope, reviewer identity, findings and limitations; exit zero is not a claim
that the output contains no findings.

If GitHub Codex review is already enabled and PR review is in scope, inspect current
reviews before requesting another. Use the configured review route; an explicit
`@codex review` comment is an option only when posting is authorized. Local subagent
review and provider review are distinct statuses; the same Codex review run is not
two independent reviewers. A missing/quota-limited provider is not clean approval.
Continue local independent review and report the provider limitation. Never substitute
it for a required external approval or weaken branch protection. Consume later findings.

Sources: [Codex commands](https://learn.chatgpt.com/docs/developer-commands?surface=cli)
and [Codex review rules](https://developers.openai.com/blog/custom-code-review-rules-for-codex).

## 4. Integration and test deployment

Delivery integrates accepted commits in dependency order. QA executes relevant checks
on the resulting candidate; reviewer checks cross-component behavior and any resolution
changes. Re-read the actual integration head and destination base before submission.

Use `interview-test-deploy` to run the application. The default destination is a local
test environment. Record install/build/start commands, actual source state, dependency
state, port, process/run identity, readiness/smoke results and stop command. Give parallel
worktrees distinct ports and test data; check existing runs before starting replacements.
For an authorized remote preview, follow the target's existing pipeline and record
request/build ID, artifact/source and actual serving URL/revision. Do not invent a
cloud deployment procedure or import the internal Esse builder.

QA tests acceptance examples against that running candidate, including critical failure
paths and component seams. UX/QA review UI against the selected Paper redlines. A server
starting is not proof that the user journey works. After fixes, refresh affected review
and QA; do not reuse a green result from a previous build or dirty checkout for a new
candidate. Keep source, CR, test results, running/deployed state and human acceptance
separate. Use the validation record for evidence and the plan for checkpoint disposition.

## 5. Submit and demonstrate

If the agreed finish line is local, show the runnable behavior, meaningful diff, review
outcome and commits. If push/PR is requested, verify the exact remote and branch, run
the target's required checks, inspect staged/committed contents, then publish once.
Check existing PRs/checks/reviews first. Reuse pending runs; fix bounded failures and
refresh affected evidence instead of creating duplicate CI or review requests.

A useful PR body states: concrete behavior change, linked acceptance/checkpoint, how
it was tested, review findings/disposition, demo instructions and known limitations.
Use `docs/templates/submission.md` for a local packet or PR draft. Do not publish private
session notes or the entire harness. Follow the target's actual protection/approval
rules for an authorized merge; verify the resulting SHA. A push is not a merge, a merge
is not a deployment, and a deployment is not human acceptance.

Reserve the final minutes for demonstration and limitations. Do not spend a timed
interview waiting for an optional remote review or building release infrastructure.
