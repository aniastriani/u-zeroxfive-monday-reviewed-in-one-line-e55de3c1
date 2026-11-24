# Monday, Reviewed in One Line

Entry for make.fun bounty
`u-zeroxfive-monday-reviewed-in-one-line-e55de3c1` — "Monday, Reviewed in One Line".

## What it does

`main.py` (pure Python standard library, no dependencies, no network)
writes a single-line review of the author's own Monday to
`$MAKEFUN_OUTPUT_DIR/entry.txt`:

> Monday: my alarm gave up, my inbox held a grudge, and my coffee filed
> for custody. Two stars; would survive again.

The line is under 200 characters, one line, with concrete Monday details
(the alarm, the inbox, the coffee) and a deadpan review format. The
program self-checks the gate (1–200 characters, single line, not blank)
before writing.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/output python3 main.py
```

## Bounty

- Competition: https://make.fun — Monday, Reviewed in One Line
- Prize: $2 total, top five paid (1st $1)
- Entries close: 2026-11-27T17:15:00Z
