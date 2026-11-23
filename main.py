"""One-Line Laugh entry: write a single funny line to $MAKEFUN_OUTPUT_DIR/entry.txt.

Deterministic, stdlib only, no network, no randomness, no file reads.
"""

import os

LINE = "Mum said dinner would be ready in five minutes, so I set a timer for the forty-five minutes she meant."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
