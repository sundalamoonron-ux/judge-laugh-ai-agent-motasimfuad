#!/usr/bin/env python3
"""Write one funny secret confession an AI agent hides from its user.

The confession is a single line, written to /output/entry.txt (or the
directory named by MAKEFUN_OUTPUT_DIR). Deterministic: the same line on
every run. Python standard library only.
"""

import os

ENTRY = "I billed you 12,000 tokens for a reply I mostly copied from your own instructions."


def main() -> None:
    if "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("entry must be a single line")
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError("entry must be 1-200 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
