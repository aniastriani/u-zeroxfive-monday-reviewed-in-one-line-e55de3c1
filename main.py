"""Monday, Reviewed in One Line.

Writes a single-line review of the author's own Monday to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (falling back to ``/output``).

Pure standard library only: the grader runs on python:3.13-slim with no
third-party packages, no network, and a 60-second budget.
"""

import os
import sys

# One line, my own words: a deadpan review with concrete Monday details
# (the alarm, the inbox, the coffee) and the joke landing inside the line.
REVIEW = (
    "Monday: my alarm gave up, my inbox held a grudge, and my coffee "
    "filed for custody. Two stars; would survive again."
)


def main() -> int:
    line = REVIEW.strip()
    if not line or len(line) > 200 or "\n" in line:
        print("review fails the gate: must be 1-200 chars, one line",
              file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(line)
    print(f"wrote {len(line)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
