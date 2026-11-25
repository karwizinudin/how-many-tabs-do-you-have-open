#!/usr/bin/env python3
"""How many tabs do I have open? Three.

One for the thing I'm doing, one for the thing I was doing,
and one I opened yesterday and keep meaning to read.
"""

import os

TABS_OPEN = 3


def main() -> None:
    text = str(TABS_OPEN)
    # The gate: /output/entry.txt must be UTF-8 text of 1 to 5
    # characters, digits only, not only white space.
    assert text.isdigit() and 1 <= len(text) <= 5, "entry must be 1-5 digits"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    # Re-read and confirm what landed on disk is exactly the digits.
    with open("/output/entry.txt", encoding="utf-8") as f:
        assert f.read() == text


if __name__ == "__main__":
    main()
