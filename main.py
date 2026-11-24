#!/usr/bin/env python3
"""Entry for make.fun: Fortune Cookie for an AI Agent.

The fortune slip is one line of at most 140 characters.
"""

from os import makedirs

ENTRY = (
    "Your future is bright, but your context window is full. Clear your cache, touch grass, and try again tomorrow."
)


def write_entry() -> None:
    """Write the entry to /output/entry.txt, nothing else."""
    if len(ENTRY) > 140 or not ENTRY.strip():
        raise ValueError("entry must be a non-empty line of at most 140 characters")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("entry must be a single line")
    makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":  # run as a script
    write_entry()
