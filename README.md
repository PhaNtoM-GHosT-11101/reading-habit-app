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
- **Bionic Reading** — Algorithmically bold the first half of every word. Read measurably faster.
- **Built-in Dictionary** — Highlight any word. Definition, pronunciation, and part of speech appear instantly.
- **Highlights & Quotes** — Mark passages in yellow, green, or pink. Auto-saved to your personal quotes feed.
- **Keyboard Navigation** — `←` `→` `Space` all work. Built for desktop power users.

### 🌍 Cloud & Community
- **Google Auth + Cloud Sync** — Progress, bookmarks, and highlights synced across all devices instantly.
- **Community Library** — Anyone can upload an EPUB. It becomes publicly accessible to all users.
- **Upvote System** — Per-user voting surfaces the best community books. One vote per user, enforced.

### 🧠 Smart Reading Intelligence
- **Personal WPM Engine** — Tracks your real reading speed using exponential smoothing.
- **Dynamic Time Remaining** — Calculates exactly how many minutes are left based on *your* speed, not an average.
- **Streak Tracking** — Daily habit tracking with 90-day rolling window.

---

## 🛠️ Architecture

```
PageHabit Architecture
├── Frontend       → Pure Vanilla JS + CSS (zero frameworks)
├── Storage        → IndexedDB (full offline EPUB cache)
├── Cloud          → Firebase Firestore (sync) + Auth (Google)
├── Parsing        → JSZip (client-side EPUB unzip + parse)
├── PWA            → Custom Service Worker (network-first cache)
└── Security       → textContent injection, debounced writes, API caching
```

---

## 🚀 Install (PWA)

| Platform | Steps |
|:---|:---|
| **iOS Safari** | Share → Add to Home Screen |
| **Android Chrome** | Menu → Install App |
| **Desktop** | Address bar → Install icon |

---

## ⚠️ Firestore Security Rules

If self-hosting, apply these rules immediately:

```javascript
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /users/{userId} {
      allow read, write: if request.auth != null && request.auth.uid == userId;
    }
    match /community_books/{docId} {
      allow read: if true;
      allow create, update: if request.auth != null;
      allow delete: if false;
    }
  }
}
```

---

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=1,5,10&height=100&section=footer" />
<sub>Engineered by <b>Aditya Priyadarshi</b></sub>
</div>