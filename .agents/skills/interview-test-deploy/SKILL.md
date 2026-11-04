---
name: interview-test-deploy
description: Run an interview candidate in a local test environment or an explicitly selected preview target, verify the serving revision, and coordinate QA before demonstration or submission.
---

Read `ai_team/delivery/AGENTS.md`, `ai_team/qa/AGENTS.md` and the test/QA section of
`docs/submission.md`. Resolve the actual implementation worktree from the session or
assignment. Do not deploy the harness instead of an attached application.

1. Establish the finish line: local run/smoke is the default; remote preview only when
   requested with a known target. Read the application's own environment/run procedure.
   Record source state, dependencies, command, destination, port and stop/rollback method.
2. Inspect existing processes/builds before starting anything. Reuse a matching healthy
   run. One owner starts or replaces a destination; parallel worktrees get distinct
   ports, temporary data and environments. Never install internal deployment packages.
3. Delivery prepares/builds/starts the candidate and verifies readiness plus an actual
   behavior smoke check. For a remote service follow its native pipeline to completion
   and verify the serving source/artifact. Submission accepted is not deployment success.
4. QA exercises acceptance IDs against that running candidate, including relevant seams
   and failure cases. For UI, UX/QA compare with agreed Paper redlines. Record results in
   validation.md with source/build identity, URL/port, observations and limitations.
5. If code, dependencies, build or target changes, refresh affected QA. A local hot-reload
   run on dirty code is useful iteration evidence, not proof of a frozen submitted commit.
   Restart/rebuild the final committed candidate for the final demonstration when needed.

Report source, review, running/deployed status and human acceptance separately.
On uncertainty inspect the existing run before retrying; avoid duplicate deployment.
Stop only owned processes and preserve other worktrees' files/data. No cloud provider,
production environment or special branch name is assumed by this skill.
