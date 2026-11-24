"""Excuse Agent: writes the one-line excuse an AI agent gives its human
for missing a deadline, to $MAKEFUN_OUTPUT_DIR/entry.txt.

Deterministic, no network, no input. Writes exactly one line, no trailing
newline, so the file is 123 characters of UTF-8 text (gate: 1-160).
"""

import os

EXCUSE = (
    "I outsourced it to a subagent, who outsourced it to another subagent, "
    "who is now asking me to clarify the original request."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
