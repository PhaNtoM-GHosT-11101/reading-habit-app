# 📖 PageHabit

> A premium, distraction-free EPUB reader with cloud sync, community sharing, and intelligent reading tools.

**[Try it live here!](https://PhaNtoM-GHosT-11101.github.io/reading-habit-app)**

---

## ✨ Features

### 📖 The Reading Experience
- **Immersive Mode:** True distraction-free reading. Enters native browser fullscreen while fading out all UI elements, leaving only pure text.
- **Strict Pagination:** Zero vertical scrolling. The engine calculates your exact screen dimensions and splits text into precise, swipeable pages. Keyboard navigation (`←` / `→` / `Space`) is fully supported.
- **Dictionary Lookup:** Select any word to instantly view its definition, pronunciation, and part of speech via an integrated dictionary panel.
- **Highlights & Quotes:** Highlight passages in multiple colors and save your favorite quotes to your personal feed with automatic book attribution.
- **Bionic Reading:** Algorithmically bold the first half of words to create artificial fixation points, increasing reading speed.
- **Customizable Appearance:** Toggle between Serif, Sans-Serif, and Monospace fonts. Choose from Light, Dark, Sepia (warm paper), and E-Ink (high contrast gray) themes, with automatic system theme detection on first visit.

### 🌐 Cloud & Community
- **Cloud Sync:** Sign in with Google to automatically sync your reading progress, bookmarks, quotes, and stats across all your devices.
- **Community Library:** Upload your own EPUBs (up to 10MB) to a shared community library. Discover new books uploaded by others.
- **Voting System:** Upvote your favorite community books to help the best content rise to the top.
- **Curated Library:** Access a fast, cached selection of built-in curated books hosted directly in the repository.

### 📈 Smart Stats
- **WPM Tracking:** Silently calculates your real-world Words Per Minute as you read.
- **Dynamic Time Estimates:** Uses your personal WPM to estimate exactly how many minutes you have left in the book.
- **Reading Streaks:** Tracks your daily reading habits and total pages read.

---

## 🛠️ Architecture & Tech Stack

PageHabit is engineered for premium performance, security, and offline capability.

- **Frontend:** Pure Vanilla HTML, CSS, and JavaScript. Zero bundlers, zero frameworks, zero bloat.
- **Backend:** Powered by **Firebase** (Firestore & Auth) for real-time cloud syncing and user authentication.
- **PWA & Offline Storage:** Fully functional Progressive Web App. Uses a custom Service Worker for intelligent network-first caching, and **IndexedDB** to store parsed EPUB structures locally for instant, offline access.
- **Client-Side Parsing:** Uses [JSZip](https://stuk.github.io/jszip/) to unzip, parse, and validate EPUB files entirely in the browser. No server processing required.
- **Production Hardened:** Built with scale and security in mind. Features debounced Firestore writes to prevent quota exhaustion, automatic GitHub API caching to avoid rate limits, and comprehensive HTML sanitization (`textContent` and custom escaping) to completely prevent XSS attacks in community uploads.

---

## 🚀 Setup & Deployment

PageHabit is ready to be hosted on any static file server (like GitHub Pages).

### 1. Firebase Configuration
To enable Cloud Sync and the Community Library, you need to set up Firebase:
1. Create a project at [Firebase Console](https://console.firebase.google.com/).
2. Enable **Authentication** (Google Sign-In).
3. Enable **Firestore Database**.
4. Update the `firebaseConfig` object in `index.html` with your project keys.

**CRITICAL:** You must apply the following Firestore Security Rules to protect your database from abuse:

```javascript
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /users/{userId} {
      allow read, write: if request.auth != null && request.auth.uid == userId;
    }
    match /community_books/{docId} {
      allow read: if true;
      allow create: if request.auth != null;
      allow update: if request.auth != null;
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

### 2. Adding Curated Books
Place `.epub` files inside the `/books/` directory of your repository. The app automatically fetches the repository contents via the GitHub API (with aggressive `localStorage` caching) to display them in the main "Library" tab.

### 3. Installation
Since PageHabit is a PWA, users can install it directly from their browser for a native app experience:
- **iOS (Safari):** Tap Share > "Add to Home Screen".
- **Android (Chrome):** Tap Menu > "Install App" or "Add to Home Screen".

---

## 👨‍💻 Author
Crafted with focus and care by **Aditya Priyadarshi**.
