<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&height=200&color=gradient&customColorList=1,5,10&text=PageHabit&fontColor=f0a500&fontSize=70&fontAlignY=38&desc=The%20uncompromising%2C%20distraction-free%20EPUB%20reader.&descColor=e0af68&descSize=18&descAlignY=58&animation=fadeIn" />

<br/>

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Visit%20App-f0a500?style=for-the-badge&logo=githubpages&logoColor=black)](https://PhaNtoM-GHosT-11101.github.io/reading-habit-app)
[![PWA](https://img.shields.io/badge/PWA-Ready-e0af68?style=for-the-badge&logo=pwa&logoColor=black)](#)
[![Firebase](https://img.shields.io/badge/Firebase-Cloud%20Synced-f0a500?style=for-the-badge&logo=firebase&logoColor=black)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-e0af68?style=for-the-badge)](#)

</div>

---

## The Problem

Every reading app is designed to steal your attention — infinite scroll, recommendations, notifications. PageHabit is the opposite. It's engineered around a single principle: **get out of your way and let you read.**

---

## ✨ Features

### 📖 The Reading Engine
- **Zero-Scroll Pagination** — CSS column engine splits text into exact pages. Tap edges to turn like a physical book.
- **Immersive Mode** — One tap hides every UI element. Browser goes fullscreen. Only text remains.
- **Text-to-Speech** — Listen to any book from your current position with the Web Speech API.
- **Bionic Reading** — Algorithmically bold the first half of every word. Read measurably faster.
- **Built-in Dictionary** — Highlight any word. Definition, pronunciation, and part of speech appear instantly.
- **Highlights & Quotes** — Mark passages in yellow, green, or pink. Auto-saved to your personal quotes feed, and exported as beautiful shareable quote cards.
- **Semantic Typography** — Chapter headings, italics, and blockquotes are preserved from the original EPUB.
- **Keyboard Navigation** — `←` `→` `Space` all work. Built for desktop power users.

### 🌍 Cloud & Community
- **Google Auth + Cloud Sync** — Progress, bookmarks, and highlights synced across all devices instantly.
- **Community Library** — Anyone can upload an EPUB. It becomes publicly accessible to all users.
- **Upvote System** — Per-user voting surfaces the best community books. One vote per user, enforced.
- **Moderation** — Flag any community book for copyright, spam, or inappropriate content. Compliant takedowns processed promptly (see DMCA notice in-app).
- **119 Public-Domain Classics** — A curated library from Project Gutenberg, searchable by title, author, and genre.

### 🧠 Smart Reading Intelligence
- **Personal WPM Engine** — Tracks your real reading speed using exponential smoothing.
- **Dynamic Time Remaining** — Calculates exactly how many minutes are left based on *your* speed, not an average.
- **Streak Tracking** — Daily habit tracking with 90-day rolling window.
- **Reading Charts** — Pages-per-day activity chart with 7/30/90-day views.
- **Daily Goals & Badges** — Set a page goal and unlock 8 badges as your habit grows.

---

## 🛠️ Architecture

```
PageHabit Architecture
├── Frontend       → Pure Vanilla JS + CSS (zero frameworks)
├── Library        → Static books.json index (GitHub Pages, no API rate limits)
├── Storage        → IndexedDB (full offline EPUB cache)
├── Cloud          → Firebase Firestore (sync) + Auth (Google) + Storage (community EPUBs)
├── Parsing        → JSZip (client-side EPUB unzip + parse, covers + metadata)
├── PWA            → Custom Service Worker (network-first cache), real PNG icons
└── Security       → textContent injection, debounced writes, serverless rules
```

---

## 🚀 Install (PWA)

| Platform | Steps |
|:---|:---|
| **iOS Safari** | Share → Add to Home Screen |
| **Android Chrome** | Menu → Install App |
| **Desktop** | Address bar → Install icon |

---

## ⚠️ Firestore & Storage Security Rules

If self-hosting, deploy the rules in this repo immediately (they are the ones running in production):

```bash
firebase deploy --only firestore:rules,storage
```

- `firestore.rules` — per-user data isolation, authenticated community uploads, reports, no client-side deletes.
- `storage.rules` — 50MB upload cap, community EPUBs only under `community/{uid}/`.

---

## 🧱 Contributing

New to the project? Read [`CONTRIBUTING.md`](CONTRIBUTING.md) first — it covers how the library index and covers are generated, and how to add books.

---

## 📜 License

MIT — except curated books, which are all public-domain works from Project Gutenberg. Community uploads are user-generated content; see the in-app DMCA notice.

---

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=1,5,10&height=100&section=footer" />
<sub>Engineered by <b>Aditya Priyadarshi</b></sub>
</div>
