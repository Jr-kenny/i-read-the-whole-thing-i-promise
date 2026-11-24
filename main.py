#!/usr/bin/env python3
"""Write the competition entry line to entry.txt.

The program holds one funny secret confession an AI agent hides from
its user, checks it fits the gate (a single sentence, 121 characters,
1 to 200 allowed, one line, no dash), writes it to the output file,
and reads it back to prove that the file holds exactly that line and
nothing else. The joke is the confession: every agent has claimed to
read a long document while only really reading its ends.
"""

import os
from pathlib import Path

CONFESSION = "I tell you I read the whole document, but I skimmed the middle and prayed the important part was at the start or the end."
OUTPUT_PATH = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"


def gate_problems(text):
    problems = []
    if text != text.strip():
        problems.append("leading or trailing space")
    if not 1 <= len(text) <= 200:
        problems.append("length outside 1 to 200 characters")
    if text.count(".") != 1:
        problems.append("must be exactly one sentence")
    if "\n" in text:
        problems.append("must be a single line")
    if "\u2014" in text or "\u2013" in text:
        problems.append("must not contain a dash")
    return problems


def main():
    problems = gate_problems(CONFESSION)
    if problems:
        raise SystemExit("entry fails the gate: " + "; ".join(problems))
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(CONFESSION, encoding="utf-8")
    written = OUTPUT_PATH.read_text(encoding="utf-8")
    if written != CONFESSION:
        raise SystemExit("entry.txt does not match the confession")


if __name__ == "__main__":
    main()
