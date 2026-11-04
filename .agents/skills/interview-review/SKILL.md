---
name: interview-review
description: Perform independent subagent code review or Codex review of an interview checkpoint, bind findings to the actual candidate, and recheck fixes before submission.
---

Read `ai_team/reviewer/AGENTS.md` and `docs/submission.md` from the harness, plus the
active session and target instructions. In attached mode use the implementation
checkout/worktree from the assignment, not the harness Git root.

1. Capture repository/worktree, base SHA, current head/tree, changed paths and any
   dirty/untracked snapshot. Stop writers while reviewing a dirty snapshot, or use a
   clean committed candidate. Never call a dirty review evidence for a different commit.
2. Coordinator assigns a fresh reviewer that did not implement the change. Pass the
   complete candidate diff, spec/acceptance IDs, applicable instructions, prior findings
   and raw validation. Do not prescribe a desired verdict. One reviewer is the normal
   interview default; use another only when risk, policy or the human requires it.
3. Reviewer inspects code/callers and returns findings, validation, limitations and
   candidate identity. Use session `review.md` based on `docs/templates/review.md`.
   Coordinator routes fixes to developers, records disposition and obtains affected
   re-review. Do not erase earlier findings because a later summary says "clean".
4. If Codex review is available, use the selected local app/CLI review or configured
   PR review path described in submission.md. Record which path actually ran. A local
   Codex reviewer may itself be the independent review; do not double-count one run.
5. Re-read candidate and integration base before accepting. A changed head/base,
   conflict resolution or dependency invalidates affected evidence. Review new changes
   and run the relevant checks on the combined candidate before submission.

Unavailable or quota-limited review is not "no findings". Keep evidence from a local
independent reviewer distinct from provider review status. Do not duplicate a pending
request, wait out an interview on quota, or bypass the target's required checks. Surface
any required-but-unavailable review; continue useful authorized preparation.
