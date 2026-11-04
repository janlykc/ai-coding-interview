# Debugging/pairing trial — 2026-11-04

Original synthetic fixture, not NeetCode starter code or a recreation of the user's
transcript. The task contract is in README.md. Harness guidance was read explicitly
from the sibling debugging worktree during this trial.

## Staged interaction

1. A fresh agent received only the skill/root guidance, fixture and a request to discuss
   the USER SKETCH comments without implementing. It ran the supplied checks, identified
   reversed edges rather than blaming cycle detection, and traced the two queue roles.
   Parent verified no tracked or untracked file changes before advancing.
2. A simulated user turn accepted the discussed design and explicitly requested the fix
   and implementation. The agent proceeded without a redundant approval request,
   preserved the unrelated caller note and added useful tests.
3. Parent inspected the implementation and tested it against an independently written,
   simple time-step scheduler. No original assessment solution was used.

The initial suite had 2 graph passes, 1 graph failure and 7 unimplemented-scheduler
errors. The final suite passes all 18 tests. Additional differential checks cover
300 seeded random DAGs, repeatability/input preservation, chains of 1,000 and 10,000
tasks and 10,000 independent tasks. The event-driven algorithm handles each dependency
once and each task in the heaps once: O(E + V log V) time, O(E + V) space.

## Reproduce

From this worktree:

    python3 -B -m unittest discover -s exercise -v
    python3 -B exercise/verify_reference.py .

## Limits and next useful trial

This supports feasibility, not a measured improvement over the prior harness. The
staged human replies were synthetic. It did not test a live editor's unsaved buffers,
human explanation quality, interview timing, host skill auto-discovery or a weaker model.
Scale checks validate the final design; there was no separately measured optimization
before/after. The contract asks for lexical scheduling, not globally minimal makespan.
A real next trial should let the human edit sketches and steer the discussion naturally.
