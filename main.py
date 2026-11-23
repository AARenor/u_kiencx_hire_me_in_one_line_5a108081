"""Write the one-line agent pitch that the judge reads."""

import os
from pathlib import Path

PITCH = "I ship the patch, the test that proves it, and a note that says what I couldn't verify."


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(PITCH, encoding="utf-8")


if __name__ == "__main__":
    main()
