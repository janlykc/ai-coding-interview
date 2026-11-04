# First holistic assessment

Date: November 3, 2026. Reviewed baseline: 9721f4c and the corrections in this pass.

## Judgment

Ready for a first supervised sample-question rehearsal, not yet proven as an interview
workflow. The harness now reflects the user's Esse style: human PE/product ownership,
PM-authored specs, Paper UX with developer feasibility, continuity of the lead into
coordination, independent review and meaningful Git checkpoints. The main remaining
question is whether those responsibilities fit naturally within 60–75 minutes.

The risk is coordination overhead rather than a missing role. Preserve the familiar
workflow tomorrow and measure where it helps; do not add more agents, automation or
forms before the first real exercise.

## Scope and method

Reviewed the tracked repository across root instructions, all roles and six skills,
prompts, workflow/setup documentation, session templates, Python package and tests,
VS Code configuration, dependency/build setup and Git hygiene. Inspected the untracked
VS Code settings for setup context and left them unchanged. A separate reviewer assessed
the baseline for contradictions and usability. This was a repository review and scenario
walkthrough, plus executable harness checks—not a simulated human interview or live UI build.

## Findings and corrections

| Finding | Effect | Correction |
| --- | --- | --- |
| Attached resume assumed harness files lived in the supplied repo | A fresh IDE chat could not find the session | Start/implement/resume prompts identify harness, session and implementation paths explicitly |
| Delivery skill unconditionally selected the harness runner | Attached agents were told to use a runner that deliberately rejects that mode | Standalone tooling and target-native commands are now distinguished |
| target_root instructions conflicted with worker worktree assignments | A worker could operate in the original checkout | Explicit assigned worktree takes precedence after repository identity verification; shared session stays stable |
| Python command example used system python3 | Installed venv dependencies could be missed | Standalone example uses .venv/bin/python; environment selection is explicit |
| Missing/empty/malformed attachment context was insufficiently validated | Empty metadata could bypass attached-mode protection or cause a traceback | Validate mode, absolute roots, session binding and target Git root before use; regression tests added |
| Construction counts and UX routing lagged behind later changes | Earlier guidance contradicted the current feature set | Updated counts/references and made the Paper UI path consistent |
| Many defined roles lacked an active-team schedule | Plausible slot exhaustion and unnecessary handoffs | Added phase scheduling, PM/scribe combination and appropriate QA/CR or delivery reuse |
| Learning instructions could interrupt a timed exercise | Harness maintenance could consume implementation time | Apply behavior corrections immediately; make durable edits at a checkpoint or afterward unless blocking |

The first six are concrete consistency/tooling findings. Coordination and maintenance
cost are hypotheses mitigated by instructions; the live rehearsal must test them.

## What works in the design

- The human remains responsible for product and architecture decisions without writing
  every spec or reviewing every line. Important execution paths and evidence stay visible.
- The PM–UX–developer loop is explicit, and UX reviews the implemented interface after
  handoff. Paper page names do not manufacture agreement.
- Coordinator and implementer responsibilities are clear. Independent CR is not confused
  with self-review, provider approval or tests passing.
- Provided repositories retain their own instructions, stack and Git destination. The
  harness is usable through README guidance without installing its helper package.
- Worktree integration checks the combined candidate. A pushed commit, running service,
  passed QA and human acceptance remain separate claims.

## Evidence and limits

Current verification: 18 harness tests pass, including malformed attachment handling and
attachment to a real linked worktree; lint/format, package build, doctor and all six skill
validators pass. Earlier disposable Git integration and clean-install checks are recorded
in setup-verification.md. Those results establish tooling behavior, not agent effectiveness.

Still unproven: Paper access in the actual UX worker, model/tool behavior inside the IDE,
live app↔IDE continuation, effective delegation under the clock, useful CR signal and
whether the human feels connected to the code. The local VS Code Python environment
setting is user-owned and mentions system Python; verify the selected interpreter in the
actual exercise rather than treating the workspace default as proof.

## Tomorrow's decision

Follow test-drive.md on November 4 with a real question. Measure time to the first working
slice, coordination waits, review-driven rework, continuation reliability and the human's
ability to explain the main code path. Ask which parts felt natural relative to Esse.
Keep useful behavior, remove friction and try one next improvement based on observations.
Do not infer interview readiness merely from a completed checklist or a green test suite.

Independent follow-up review of these corrections found no actionable residual findings.
The reviewer read the working diff and new assessment/test-drive/tooling documents,
and independently ran all 18 harness tests successfully. It did not claim live Paper,
IDE continuation or interview-performance verification.
