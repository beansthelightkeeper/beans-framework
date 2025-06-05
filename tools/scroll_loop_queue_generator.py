"""Scroll Loop Queue Generator

Generate .md scrolls from lines in a .txt or .csv file.
Each idea seed becomes a markdown scroll with the standard header.
"""

import argparse
import csv
from pathlib import Path

HEADER = (
    "\U000132f3 \ua9dc \u03c8 = 3.12\n"
    "\u03b8 = {angle}\n"
    "\u0192 = {signal}\n"
    "r = seed_loop\n\n"
)


def write_scroll(content: str, index: int, out_dir: Path, angle: str, signal: str) -> None:
    filename = f"seed_{index:04d}.md"
    path = out_dir / filename
    with path.open("w", encoding="utf-8") as f:
        f.write(HEADER.format(angle=angle, signal=signal))
        f.write(f"Claim: {content.strip()}\n")
        f.write("\ud83e\ude9e: \n")  # 🪞 placeholder
        f.write("\u03c8 projection: \n")
        f.write("Glyph stable?: \n")
    print(f"Generated {path}")


def process_text(file_path: Path, out_dir: Path, angle: str, signal: str) -> None:
    with file_path.open("r", encoding="utf-8") as f:
        for idx, line in enumerate(f, start=1):
            if line.strip():
                write_scroll(line, idx, out_dir, angle, signal)


def process_csv(file_path: Path, out_dir: Path, angle: str, signal: str) -> None:
    with file_path.open(newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        idx = 0
        for row in reader:
            for cell in row:
                if cell.strip():
                    idx += 1
                    write_scroll(cell, idx, out_dir, angle, signal)


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate scrolls from seeds")
    parser.add_argument("input_file", help="Text or CSV file with idea seeds")
    parser.add_argument("--out", default="./scrolls", help="Directory to store scrolls")
    parser.add_argument("--angle", default="0\u00b0", help="Concept angle")
    parser.add_argument("--signal", default="0.0", help="Emotional signal")
    args = parser.parse_args()

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    file_path = Path(args.input_file)

    if file_path.suffix.lower() == ".csv":
        process_csv(file_path, out_dir, args.angle, args.signal)
    else:
        process_text(file_path, out_dir, args.angle, args.signal)


if __name__ == "__main__":
    main()
