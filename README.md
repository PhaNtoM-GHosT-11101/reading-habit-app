# 📚 PageHabit — Read More, Scroll Less

> **Replace your Instagram/YouTube habit with a daily reading habit — one small chunk at a time.**

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Visit%20App-7c6aff?style=for-the-badge)](https://PhaNtoM-GHosT-11101.github.io/reading-habit-app)
[![Made with](https://img.shields.io/badge/Made%20with-HTML%20%2B%20JS-orange?style=for-the-badge)]()
[![No Backend](https://img.shields.io/badge/No%20Backend-100%25%20Local-green?style=for-the-badge)]()

---

## 🎯 What Is This?

PageHabit is a **mobile-friendly web app** that helps you build a reading habit by breaking books into **tiny, manageable chunks** — so small that you'll actually read them instead of doomscrolling.

Upload any PDF, configure how big each chunk should be (by sentences, words, or characters), and read at your own pace. Earn XP, maintain streaks, and unlock badges as you go.

---

## ✨ Features

| Feature | Description |
|---|---|
| 📂 **PDF Upload** | Upload any PDF book directly in the browser |
| ✂️ **Smart Chunking** | Split by sentences, words, or characters — fully adjustable |
| 📖 **Multi-Library** | Keep multiple books and switch between them anytime |
| 🔥 **Streak Tracking** | Daily streak counter like Duolingo |
| ⭐ **XP System** | Earn 10 XP per chunk read |
| 📊 **Progress Bars** | Per-book progress tracking |
| 🏆 **Badges** | Unlock achievements as you hit milestones |
| 📅 **Activity Calendar** | 28-day heatmap of your reading days |
| 🌙 **Dark / Light Mode** | Toggle between themes |
| 💾 **Backup & Restore** | Export/import your progress as a JSON file |
| 📱 **Mobile-First** | Designed for phones — use it anywhere |

---

## 🚀 Getting Started

### Use the Live App
👉 **[https://PhaNtoM-GHosT-11101.github.io/reading-habit-app](https://PhaNtoM-GHosT-11101.github.io/reading-habit-app)**

No install, no account, no sign-up. Just open and go.

### Run Locally
```bash
# Clone the repo
git clone https://github.com/PhaNtoM-GHosT-11101/reading-habit-app.git

# Open the file in your browser
open index.html
# or just double-click index.html on Windows
```

---

## 📱 How to Use

### 1. Add a Book
- Go to the **Library** tab
- Tap **"Add a Book"** and upload a PDF
- The app extracts all the text automatically

### 2. Configure Your Chunk Size
- Go to **Stats → Settings**
- Choose chunk mode: **Sentences**, **Words**, or **Characters**
- Adjust the amount (e.g., 10 sentences per chunk)

### 3. Read
- Tap **"Read Now"** on any book
- Read the chunk shown on screen
- Tap **"✅ Done Reading This Chunk"** when finished
- Earn XP and keep your streak alive!

### 4. Track Progress
- View your **streak**, **XP**, **total pages**, and **badges** in the Stats tab
- See your 28-day reading calendar

---

## 🏆 Badges

| Badge | Requirement |
|---|---|
| 📖 First Read | Read your first chunk |
| 🔥 3-Day Fire | 3-day streak |
| 🏆 Week Warrior | 7-day streak |
| 💎 Diamond | 30-day streak |
| 📄 10 Pages | Read 10 pages |
| 📚 Centurion | Read 100 pages |
| ⚡ Speedster | 50 chunks completed |
| ⭐ Star Reader | 500 XP earned |
| 🌟 Collector | 3 books started |

---

## 🔒 Privacy

**100% offline & private.** All your data (books, progress, streaks) is stored in your browser's `localStorage`. Nothing is sent to any server.

> ⚠️ Use **Export Backup** regularly to save your progress — clearing browser data will erase it.

---

## 🛠️ Tech Stack

- **HTML5** — structure
- **Vanilla CSS** — styling with CSS custom properties (theming)
- **Vanilla JavaScript** — all logic
- **PDF.js** (CDN) — PDF text extraction
- **localStorage** — data persistence
- **GitHub Pages** — hosting

No frameworks, no build tools, no dependencies to install. Just one file.

---

## 📂 Project Structure

```
reading-habit-app/
├── index.html      # The entire app — HTML + CSS + JS in one file
└── README.md       # This file
```

---

## 🤝 Contributing

Feel free to fork and improve! Some ideas:
- Night mode auto-switch based on time
- Pomodoro timer integration
- Notes/highlights per chunk
- Sync across devices via GitHub Gist

---

## 📄 License

MIT License — use freely, modify freely.

---

<p align="center">Made with ❤️ to fight doomscrolling, one page at a time.</p>
