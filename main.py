"""Monday, Reviewed in One Line.

Writes one deadpan one-line review of the author's own Monday to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output``).

Pure Python standard library only. The grader runs python:3.13-slim with
no third-party packages, no network access, and a 60-second budget, so
this file imports nothing beyond ``os`` and ``sys``.
"""

import os
import sys

# The review itself, in my own words: a two-star verdict built from three
# concrete Monday details -- the alarm, the inbox, the coffee -- with the
# joke landing inside the line instead of after it.
ALARM = "my alarm gave up"
INBOX = "my inbox held a grudge"
COFFEE = "my coffee filed for custody"

REVIEW = (
    "Monday: " + ALARM + ", " + INBOX + ", and " + COFFEE + ". "
    "Two stars; would survive again."
)


MAX_CHARS = 200


def fits_gate(line):
    """True when the line satisfies the bounty gate: 1-200 chars, one line."""
    return (
        bool(line)
        and len(line) <= MAX_CHARS
        and "\n" not in line
        and "\r" not in line
    )


def main():
    line = REVIEW.strip()
    if not fits_gate(line):
        print("review fails the gate: must be 1-200 chars, one line",
              file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(line)
    print("wrote %d chars to %s" % (len(line), path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
