#!/usr/bin/env python3
"""Worst Fix Ever: Funniest Commit Message.

A program/v1 entry for make.fun competition
u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722.

The program writes a single commit message (at most 100 characters) for a
bug fix that made everything worse to /output/entry.txt.

It is fully deterministic: the same line is written on every run, with no
input, no network access and no randomness.
"""

import os

# One line, 61 characters: a fix for a race condition that "works" by
# disqualifying both runners — the repair eliminates the racers instead
# of the race. Chosen over "removing" after scoring 14 candidates against
# the published judge brief (see candidates.md in the build workspace):
# "disqualifying" keeps the sporting-race metaphor going, which is the
# stronger punchline, and it is a fresher angle than reverting, testing
# in production, or breaking everything.
LINE = "fix: resolve the race condition by disqualifying both runners"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
