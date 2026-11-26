"""Rename the Planet — make.fun entry.

Writes one line to $MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output):
a funny new name for Saturn plus the why, in a single line under
200 characters, as the gate requires.
"""

import os

LINE = (
    "Rename Saturn 'Buffering' — its rings have been loading for "
    "4.5 billion years and the bar hasn't moved."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
    assert LINE.strip() == LINE, "line must not start or end with whitespace"
    assert "\n" not in LINE, "line must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(f"wrote {path} ({len(LINE)} chars)")


if __name__ == "__main__":
    main()
