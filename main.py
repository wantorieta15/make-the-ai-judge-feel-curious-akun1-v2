#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Make the AI judge feel curious — v2 (Akun 1, @walta-exchange).

Writes a single short text (200-280 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt. Python 3.13 stdlib only, no network,
fully deterministic.

Lesson from round 1: the long, immersive scene (v1, 264 chars,
rooftop + stars) scored far higher than short static images, so v2
keeps the same slow, concrete, second-person shape with a brand-new
scene — a door in the garden wall that was not there yesterday —
and one mystery that keeps growing until the open question at the end.
The text is written in English, the language of the judge and of
every reference text, for round 3.
"""

import os
import sys
from pathlib import Path

TEXT = (
    "Yesterday your garden wall was plain stone. Today there is a door "
    "in it, open a little, warm light spilling onto the grass. The air "
    "from beyond smells of rain on hot stone, and of your childhood "
    "kitchen. A hand is waiting there. Will you step through, or close "
    "it gently?"
)

MIN_LEN = 1
MAX_LEN = 280


def main() -> int:
    text = TEXT.strip()
    if not text:
        print("error: entry text is blank", file=sys.stderr)
        return 1
    if not (MIN_LEN <= len(text) <= MAX_LEN):
        print(
            f"error: entry is {len(text)} characters, "
            f"outside the allowed range {MIN_LEN}-{MAX_LEN}",
            file=sys.stderr,
        )
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not output_dir:
        print("error: MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1

    out_path = Path(output_dir) / "entry.txt"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(text + "\n", encoding="utf-8")
    # Diagnostic: character count is the only number that matters here.
    print(f"wrote {len(text)} characters to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
