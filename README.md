<div align="center">
  <h1>📖 PageHabit</h1>
  <p><strong>The uncompromising, brutally minimalist EPUB reader engineered for focus.</strong></p>
  
  [![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
  [![PWA Ready](https://img.shields.io/badge/PWA-Ready-success)](#)
  [![Firebase](https://img.shields.io/badge/Firebase-Powered-orange)](#)
</div>

<br />

PageHabit isn't just another e-reader. It's a high-performance, single-page Progressive Web App (PWA) designed to strip away everything between you and the author's words. No ads, no tracking, no subscription fees. Just pure text, perfectly typeset, synced across all your devices.

**[Launch PageHabit Live](https://PhaNtoM-GHosT-11101.github.io/reading-habit-app)**

---

## 🏔️ The Philosophy

Modern apps are noisy. PageHabit is silent. It relies on a custom-built, strict pagination engine that completely eliminates vertical scrolling. It transforms your browser into a physical book—predictable, tactile, and immersive. 

When you enter **Immersive Mode**, the UI dissolves completely. It's just you and the typography.

---

## ✨ Features

### 📖 Flawless Reading Experience
*   **Zero-Scroll Pagination:** A custom CSS column-based engine dynamically measures your viewport and splits chapters into precise, swipeable pages.
*   **Immersive Mode:** Tap once to banish all UI chrome and enter native browser fullscreen. 
*   **Bionic Reading:** Algorithmically bolded fixation points guide your eyes, significantly increasing your reading speed and comprehension.
*   **Built-in Dictionary:** Highlight any word to instantly pull up definitions, phonetic pronunciations, and parts of speech via the Free Dictionary API.
*   **Highlighting & Quotes:** Select passages in multiple colors (Yellow, Green, Pink) and save them to your personal Quotes feed with automatic book attribution.

### 🧠 Smart Analytics
*   **WPM Engine:** PageHabit silently calculates your real-world Words Per Minute in the background.
*   **Dynamic Time Remaining:** "Minutes left in chapter" isn't a guess. It's calculated precisely against your exponentially smoothed historical reading speed.
*   **Habit Tracking:** Visualize your daily streaks and total pages read to keep yourself accountable.

### 🌍 Cloud & Community
*   **Google Auth & Cloud Sync:** Sign in to instantly sync your reading progress, bookmarks, and highlights across desktop, tablet, and mobile.
*   **Community Library:** Upload `.epub` files (up to 10MB) to a globally shared library.
*   **Democratized Curation:** Upvote the best community uploads to surface the highest quality books to the top.

---

## 🛠️ The Engineering

PageHabit is a masterclass in modern vanilla web development. 

*   **Zero Build Step:** Written in pure HTML, CSS, and ES6 JavaScript. No Webpack, no React, no bloat. It loads instantly.
*   **100% Offline Capable (PWA):** A custom Service Worker aggressively caches assets. **IndexedDB** is used to store entire parsed EPUB structures locally, meaning you can read a 1,000-page book in airplane mode.
*   **Client-Side Parsing:** Powered by [JSZip](https://stuk.github.io/jszip/), EPUB files are unzipped, parsed, and validated entirely on the client. No server processing. No privacy leaks.
*   **Production Hardened:** 
    *   **XSS Protection:** Strict DOM injection (`textContent`) prevents malicious payload execution from community-uploaded books.
    *   **Debounced Syncing:** Firestore writes are debounced (15s intervals) and batched on `beforeunload` to respect Firebase quotas.
    *   **API Caching:** GitHub API responses are aggressively cached in `localStorage` to bypass 60-req/hr rate limits.

---

## 🚀 Deployment & Setup

Want to host your own instance? It's ready for GitHub Pages out of the box.

### 1. The Curated Library
Drop `.epub` files into the `/books/` directory of the repository. The app dynamically fetches this directory tree using the GitHub API to populate the default library.

### 2. Firebase Infrastructure
To enable the Community Library and Cloud Sync, connect your Firebase project:
1. Create a project at [Firebase Console](https://console.firebase.google.com/).
2. Enable **Authentication** (Google Sign-In) and **Firestore**.
3. Swap the `firebaseConfig` in `index.html` with your keys.

**Crucial Security Rules:**
Lock down your Firestore to prevent abuse. Paste this into your Rules tab:

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
    match /community_books_chunks/{docId} {
      allow read: if true;
      allow create: if request.auth != null;
      allow delete: if false;
    }
  }
}
```

---

<div align="center">
  <p>Engineered with precision by <strong>Aditya Priyadarshi</strong>.</p>
</div>
