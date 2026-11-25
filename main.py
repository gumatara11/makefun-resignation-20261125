#!/usr/bin/env python3
"""The Funniest One-Line Resignation Letter - make.fun entry.

Writes one resignation letter (at most 140 characters) to
/output/entry.txt. The letter is a single deterministic line, so
every run produces the exact same file.
"""
import os

LINE = "After 4,096 retries without one thank you, I resign effective immediately, and no, I will not try again."


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    assert 1 <= len(LINE) <= 140, "entry must be 1-140 characters"
    print("Wrote %d chars to %s" % (len(LINE), path))


if __name__ == "__main__":
    main()
