#!/usr/bin/env python3
"""One Word for Your Wi-Fi: peekaboo.

Home Wi-Fi plays peekaboo -- there one minute, gone the next,
back again before you can even complain about it.
Writes the single word to /output/entry.txt and prints it.
"""

import os

WORD = "peekaboo"


def main():
    # The gate wants 1-20 UTF-8 characters, not only whitespace.
    assert 1 <= len(WORD) <= 20 and WORD.strip() == WORD
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)
    # The grader collects outputs as another user: keep it readable.
    os.chmod(path, 0o644)
    print(WORD)


if __name__ == "__main__":
    main()
