#!/usr/bin/env python3
"""Generate books.json — a static index of the books/ folder.

Serves two purposes:
1. Removes the dependency on the GitHub contents API (rate-limited to 60 req/hr/IP),
   which the web app used to list the library.
2. Precomputes clean titles/authors (with EPUB metadata as fallback) and extracts
   book covers into covers/, so the client never has to guess from filenames.

Run from anywhere:  python3 scripts/generate_books_index.py
Output:
  books.json       — index at the repository root (committed to git)
  covers/<name>.*  — extracted cover images (committed to git)
"""
import datetime
import json
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BOOKS_DIR = ROOT / "books"
COVERS_DIR = ROOT / "covers"
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


def opf_metadata(zf: zipfile.ZipFile, opf_path: str) -> dict:
    xml = zf.read(opf_path).decode("utf-8", "replace")
    lang = re.search(r"<dc:language[^>]*>(.*?)</dc:language>", xml, re.S)
    creator = re.search(r"<dc:creator[^>]*>(.*?)</dc:creator>", xml, re.S)
    return {
        "lang": (lang.group(1).strip() if lang else ""),
        "creator": (creator.group(1).strip() if creator else ""),
    }


def extract_cover(zf: zipfile.ZipFile, opf_path: str, stem: str) -> str | None:
    """Extract the EPUB cover image into covers/ and return its filename."""
    xml = zf.read(opf_path).decode("utf-8", "replace")
    items = dict(re.findall(r'''<item[^>]*\bid=["']([^"']+)["'][^>]*\bhref=["']([^"']+)["']''', xml))
    items.update({v: k for k, v in re.findall(r'''<item[^>]*\bhref=["']([^"']+)["'][^>]*\bid=["']([^"']+)["']''', xml)})
    cover_id = re.search(r'''<meta[^>]+name=["']cover["'][^>]+content=["']([^"']+)["']''', xml)
    cover_href = None
    if cover_id:
        cover_href = items.get(cover_id.group(1))
    if not cover_href:
        for iid, href in items.items():
            if "cover" in iid.lower() or "cover" in href.lower():
                cover_href = href
                break
    if not cover_href:
        imgs = [n for n in zf.namelist() if n.lower().endswith((".jpg", ".jpeg", ".png", ".gif"))]
        if not imgs:
            return None
        cover_href = imgs[0]
    if cover_href.startswith("/"):
        cover_href = cover_href[1:]
    elif opf_path.count("/"):
        cover_href = opf_path.rsplit("/", 1)[0] + "/" + cover_href

    try:
        data = zf.read(cover_href)
    except KeyError:
        return None
    ext = ".jpg"
    if data[:8] == b"\x89PNG\r\n\x1a\n":
        ext = ".png"
    elif data[:4] == b"GIF8":
        ext = ".gif"
    out = COVERS_DIR / (stem + ext)
    out.write_bytes(data)
    return out.name


def main() -> int:
    if not BOOKS_DIR.is_dir():
        print(f"error: {BOOKS_DIR} not found", file=sys.stderr)
        return 1
    COVERS_DIR.mkdir(exist_ok=True)

    books = []
    for path in sorted(BOOKS_DIR.glob("*.epub")):
        title, author = clean(path.name)
        cover = None
        lang = ""
        try:
            with zipfile.ZipFile(path) as zf:
                names = zf.namelist()
                opf = next((n for n in names if n.lower().endswith(".opf")), None)
                if opf:
                    meta = opf_metadata(zf, opf)
                    lang = meta["lang"]
                    if not author:
                        author = meta["creator"]
                    cover = extract_cover(zf, opf, path.stem)
        except (zipfile.BadZipFile, OSError):
            pass
        books.append(
            {
                "name": path.name,
                "title": title,
                "author": author,
                "lang": lang,
                "cover": cover,
                "size": path.stat().st_size,
            }
        )

    index = {
        "generated": datetime.date.today().isoformat(),
        "count": len(books),
        "books": books,
    }
    OUT.write_text(json.dumps(index, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"wrote {OUT} ({len(books)} books, covers={len(list(COVERS_DIR.glob('*')))}...)")
    return 0


if __name__ == "__main__":
    sys.exit(main())