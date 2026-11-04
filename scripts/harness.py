"""Run the checkout's harness without requiring installation."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from interview_harness.cli import main  # noqa: E402

if __name__ == "__main__":
    raise SystemExit(main())
