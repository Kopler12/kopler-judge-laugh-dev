#!/usr/bin/env python3
"""Make the AI Judge Laugh: Developer Excuses — make.fun entry.

Writes one original single-line developer excuse to /output/entry.txt.
Standard library only, no network.
"""

import os

EXCUSE = "The bug's been there since day one \u2014 production just waited until demo day to introduce itself."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def main() -> None:
    text = EXCUSE.strip()
    if not text:
        raise SystemExit("entry is empty")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise SystemExit(f"entry is {len(text)} chars, over the {MAX_CHARS} limit")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # No trailing newline: the file holds exactly one line, 1-200 chars.
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
