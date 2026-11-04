# First test drive — November 4, 2026

Use a real sample question and your normal Esse style. The point is to observe the
workflow under a clock, not to demonstrate every feature of the harness. Keep the
baseline stable during the run except for fixes that unblock work.

## Start

Open a fresh exercise worktree for a blank project, or the supplied repo alongside
this harness. Keep Codex and VS Code on the same implementation checkout. Fill in
prompts/start.md with the actual paths and question. Allow 60–75 minutes, matching
the interview guide. Check sign-in and relevant tools before starting the clock.

You supply the outcome, priorities, questions and architecture judgment. PM/scribe
joins when the spec needs authoring. Request developer feasibility input or a Paper
UX pass only when the task needs it. Keep the same lead when you agree the first implementation checkpoint.

## Run naturally

1. Start with the lead alone and the design discussion. Load skills and spawn
   subagents only as their work becomes necessary. Aim for concrete acceptance examples and a small
   first slice. Let your questions sharpen the redlines; do not manually author the spec.
2. Let the coordinator dispatch implementation. Use separate worktrees if the problem
   has useful independent sections, not merely to exercise the feature.
3. Test/run the first slice, inspect the important code path, and challenge an assumption
   or introduce a realistic requirement adjustment. Record what rework that causes.
4. Bring in independent CR and QA as useful work becomes available; release idle
   design workers rather than exhausting agent slots. For UI, compare against Paper.
5. At a real checkpoint, save the handoff and switch once between Codex and VS Code.
   Verify the target, current checkpoint and stopped writers before continuing.
6. Finish with a meaningful commit and a running demonstration. Push/PR/preview only
   if that is part of the chosen exercise. Keep incomplete checks and limitations visible.

Do not manufacture approval for yourself: the agent asks you to agree the initial spec
and surfaces consequential changes. Routine authorized execution proceeds autonomously.
If tools fail, observe how well the fallback works instead of restarting the exercise.

## Record a few observations

PM/scribe or the coordinator can keep a few timestamped lines; no telemetry system needed.

| Observation | Record |
| --- | --- |
| Design agreement | Time and whether you understood the proposed solution |
| First working slice | Time and the behavior actually demonstrated |
| Coordination overhead | Approximate waiting, repeated context and unnecessary questions |
| Review value | Concrete defects caught, rework, and speculative/noisy findings |
| Code understanding | Can you explain input → main logic → output and modify an important decision? |
| Continuation | Correct repo/worktree/checkpoint resumed; duplicate writers avoided |
| Tools | Paper/subagent access in the actual worker and IDE; any fallback needed |
| Cost | Actual token/cost counters if exposed; otherwise unknown, not estimated as fact |
| Naturalness | Where it felt like your Esse workflow and where the harness got in the way |

End with a five-minute debrief in the session retrospective: keep, change, remove,
and one improvement to try next. A partial solution with useful observations is a
valid first rehearsal; do not score success solely by feature completion or test count.
