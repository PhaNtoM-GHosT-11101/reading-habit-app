#!/usr/bin/env python3
"""Generate books.json — a static index of the books/ folder.

Serves two purposes:
1. Removes the dependency on the GitHub contents API (rate-limited to 60 req/hr/IP),
   which the web app used to list the library.
2. Precomputes clean titles/authors so the client never has to guess from filenames.

Run from anywhere:  python3 scripts/generate_books_index.py
Output: books.json at the repository root (committed to git).
"""
import datetime
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BOOKS_DIR = ROOT / "books"
OUT = ROOT / "books.json"


def clean(filename: str) -> tuple[str, str]:
    name = filename[:-5] if filename.lower().endswith(".epub") else filename
    name = re.sub(r"^\d+\s+-\s+", "", name)  # legacy "<gutenberg-id> - " prefix
    title, author = name, ""

    m = re.search(r"\s+by\s+(.+)$", name)
    if m:
        author = m.group(1).strip()
        title = name[: m.start()].strip()
    elif " - " in name:
        parts = name.rsplit(" - ", 1)
        title, author = parts[0].strip(), parts[1].strip()

    # legacy trailing download-count suffix: "Title (3222)"
    title = re.sub(r"\s+\(\d+\)\s*$", "", title)
    author = re.sub(r"\s+\(\d+\)\s*$", "", author)
    title = re.sub(r"_", ": ", title)
    title = re.sub(r"\s+", " ", title).strip()
    title = re.sub(r":\s*$", "", title)
    return title, author


def main() -> int:
    if not BOOKS_DIR.is_dir():
        print(f"error: {BOOKS_DIR} not found", file=sys.stderr)
        return 1

    books = []
    for path in sorted(BOOKS_DIR.glob("*.epub")):
        title, author = clean(path.name)
        books.append(
            {
                "name": path.name,
                "title": title,
                "author": author,
                "size": path.stat().st_size,
            }
        )

    index = {
        "generated": datetime.date.today().isoformat(),
        "count": len(books),
        "books": books,
    }
    OUT.write_text(json.dumps(index, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"wrote {OUT} ({len(books)} books)")
    return 0


if __name__ == "__main__":
    sys.exit(main())