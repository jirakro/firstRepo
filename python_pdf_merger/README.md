# Python PDF Merger

A small Python project that merges PDF files using the `PyPDF2` library.

## Setup

```bash
cd python_pdf_merger
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

## Usage

```bash
pdf-merger -o merged.pdf file1.pdf file2.pdf file3.pdf
```

You can also run it as a module:

```bash
python -m pdf_merger.cli -o merged.pdf file1.pdf file2.pdf
```
