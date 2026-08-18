# Contributing to PageHabit

Thanks for helping build the distraction-free EPUB reader. This guide covers how the library works and how to add books.

## How the library works

- `books/` — the raw EPUB files (public-domain works only, e.g. from Project Gutenberg).
- `scripts/generate_books_index.py` — regenerates `books.json` (title, author, language, genres, cover path, size) and extracts cover images into `covers/`.
- `books.json` — consumed by the app at runtime; no GitHub API involved, so there are no rate limits.

> Whenever you add, remove, or rename files in `books/`, run the generator and commit the result. CI (`.github/workflows/update-index.yml`) does this automatically on push to `main` when `books/` changes.

```bash
python3 scripts/generate_books_index.py
```

## Adding a book

1. Download a **public-domain** EPUB (Project Gutenberg or equivalent).
2. Place it in `books/` following the existing naming convention (e.g. `author_Author-Name/title_Title-Grouped-Words.epub`). The script parses author/title from the path and fills in anything missing from the EPUB's own metadata.
3. Run the generator, verify the new entry in `books.json` and the cover in `covers/`.
4. Commit with a message like `Add <Title> to the library`.

## Code conventions

- Vanilla JS + CSS only — no frameworks, no build step.
- All UI and logic lives in `index.html` (single-file app). Keep it that way unless there's a strong reason not to.
- Use `textContent` when injecting user-provided text — never `innerHTML` with untrusted data.
- UI strings: no emoji; unicode symbols like ♡ and ✦ are fine.
- Verify your JS after editing `index.html`:

```bash
python3 - <<'EOF'
import re
html = open('index.html').read()
m = re.search(r'<script type="module">(.*?)</script>', html, re.S)
open('/tmp/check.js', 'w').write(m.group(1))
EOF
node --check /tmp/check.js
```

## Community content & copyright

- The curated library must stay public-domain only.
- Community uploads are user-generated. If you moderate, remove files that receive valid copyright or abuse reports.
- Don't upload copyrighted works to the community library yourself — it gets the whole app in trouble.

## Getting started

1. Fork the repo.
2. Create a feature branch.
3. Make your change, verify the JS syntax check above.
4. Open a pull request with a clear description.
