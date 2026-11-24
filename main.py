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

# Runtime validation: the entry must stay exactly one line of 1-160 chars.
# This guards against accidental edits; it never changes the output bytes.
_EXCUSE_BYTES = EXCUSE.encode("utf-8")
assert 1 <= len(EXCUSE) <= 160, "excuse must be 1-160 characters"
assert "\n" not in EXCUSE and "\r" not in EXCUSE, "excuse must be one line"
assert len(_EXCUSE_BYTES) == len(EXCUSE), "excuse must be pure ASCII"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Deterministic byte write: exact bytes, no newline translation.
    with open(path, "wb") as f:
        f.write(_EXCUSE_BYTES)


if __name__ == "__main__":
    main()
