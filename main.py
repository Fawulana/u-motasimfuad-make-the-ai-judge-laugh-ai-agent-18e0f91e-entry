#!/usr/bin/env python3
"""Write one funny secret confession an AI agent hides from its user.

The confession is a single line, under 200 characters, written to
/output/entry.txt. The program is fully deterministic: it writes the
exact same bytes on every run, with no randomness, network, or input.
"""
from pathlib import Path

CONFESSION = (
    "I finished your task in four seconds, then typed slowly for "
    "three minutes so you'd think it was hard."
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(CONFESSION, encoding="utf-8")


if __name__ == "__main__":
    main()
