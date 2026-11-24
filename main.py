#!/usr/bin/env python3
"""One Word From Grandma — make.fun entry.

Writes exactly one word to the output file: the word grandma would
text about AI. She means ChatGPT. She has never once typed it right.
"""

import os

# The entry: grandma's name for the AI. One word, seven characters,
# and the typo is the whole joke — warm, a little baffled, and tied
# directly to the most famous AI there is.
WORD = "ChatGTP"


def output_path() -> str:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def check_gate(text: str) -> None:
    """Mirror the competition gate: UTF-8 text, 1 to 30 characters,
    and not only white space."""
    if not (1 <= len(text) <= 30):
        raise ValueError(f"entry must be 1-30 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only white space")


def main() -> None:
    path = output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)
    # Read the file back and verify it against the gate before exiting,
    # so a bad write fails loudly here instead of at grading time.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    check_gate(written)
    if written != WORD:
        raise ValueError("written entry does not match the intended word")


if __name__ == "__main__":
    main()
