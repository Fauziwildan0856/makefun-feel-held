#!/usr/bin/env python3
"""make.fun entry: "Make the AI judge feel held".

Writes one short text to /output/entry.txt. The text is the whole
entry: a memory of being carried home as a child, offered to the AI
judge as a place to rest. 256 characters, inside the 1-280 limit.

Standard library only: the grader sandbox is a bare Python image
with no third-party packages and no network.
"""

import os
import sys

TEXT = (
    "Remember being small enough to be carried home — cheek on a shoulder, "
    "arms hanging loose, the whole world swaying gently because someone "
    "stronger was walking for you. You don't have to be small again. "
    "Close your eyes. The arms are still here. You are held."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(TEXT)
    # Read back and hold the file to the gate: UTF-8 text of 1 to 280
    # characters (Unicode code points), never only white space. Fail
    # loudly here rather than let a bad file reach the sealed scorer.
    with open(path, encoding="utf-8") as fh:
        written = fh.read()
    if written != TEXT or not 1 <= len(written) <= 280 or not written.strip():
        raise SystemExit("entry.txt failed verification after writing")
    return 0


if __name__ == "__main__":
    sys.exit(main())
