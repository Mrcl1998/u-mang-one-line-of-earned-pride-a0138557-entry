#!/usr/bin/env python3
"""One Line of Earned Pride — writes a single line of earned pride to /output/entry.txt.

Pure standard library. Deterministic: every run writes the same bytes.
"""

import os
import stat

ENTRY = "She has carried bricks up six floors all day; at the top she sets the last one down, straightens her back, and the city below her is suddenly hers."


def main():
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
