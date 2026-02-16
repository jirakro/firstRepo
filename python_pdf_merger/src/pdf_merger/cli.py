"""Command-line interface for merging PDF files with PyPDF2."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Iterable

from PyPDF2 import PdfMerger


def merge_pdfs(input_files: Iterable[Path], output_file: Path) -> None:
    """Merge the provided PDF files into a single output PDF."""
    merger = PdfMerger()

    try:
        for input_file in input_files:
            merger.append(str(input_file))

        output_file.parent.mkdir(parents=True, exist_ok=True)
        with output_file.open("wb") as stream:
            merger.write(stream)
    finally:
        merger.close()


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="pdf-merger",
        description="Merge multiple PDF files into one PDF.",
    )
    parser.add_argument(
        "inputs",
        nargs="+",
        type=Path,
        help="Input PDF files in the order they should be merged.",
    )
    parser.add_argument(
        "-o",
        "--output",
        required=True,
        type=Path,
        help="Path to write the merged PDF.",
    )
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    missing_files = [path for path in args.inputs if not path.exists()]
    if missing_files:
        parser.error(
            "The following input files do not exist: "
            + ", ".join(str(path) for path in missing_files)
        )

    merge_pdfs(args.inputs, args.output)
    print(f"Merged {len(args.inputs)} files into {args.output}")


if __name__ == "__main__":
    main()
