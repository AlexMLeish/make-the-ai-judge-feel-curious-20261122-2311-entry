import os
from pathlib import Path


def main() -> None:
    here = Path(__file__).resolve().parent
    text = (here / "entry.txt").read_bytes()
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(text)


if __name__ == "__main__":
    main()
