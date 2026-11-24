"""Funniest time machine warning label (120 characters or fewer).

Prints the label to stdout and writes the exact same label, with no
trailing newline, to /output/entry.txt. Standard library only, no
network access, no files read — the label is a constant in this file.

The gate for this bounty is 1 to 120 characters of UTF-8 text, so the
program refuses to write anything outside that range.
"""

import os
import sys

LINE = (
    "WARNING: Do not wave at your past self. He waves back, "
    "follows you home, and now two of you are paying rent."
)


def main() -> int:
    if not 1 <= len(LINE) <= 120:
        print(f"error: line is {len(LINE)} chars, must be 1-120",
              file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
