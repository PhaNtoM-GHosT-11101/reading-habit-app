# 📖 PageHabit (Zen Edition)

PageHabit is a gorgeous, ultra-minimalist, distraction-free EPUB reader. Built entirely as a single-file Progressive Web App (PWA), it runs entirely in your browser and functions offline.

**[Try it live here!](https://PhaNtoM-GHosT-11101.github.io/reading-habit-app)**

---

## ✨ Features

- 🧘 **Zen UI:** A museum-quality aesthetic with massive whitespace and gorgeous typography. Zero borders, zero distractions.
- 📱 **Progressive Web App (PWA):** Install it directly to your phone's home screen. Download your books once, and read them on an airplane with zero internet connection.
- 📖 **Strict Pagination:** Unlike most web readers, there is **zero vertical scrolling**. The engine dynamically calculates the exact dimensions of your screen and splits the text into precise pages. Tap the edges of your screen to turn the page just like a real physical Kindle.
- ⚡ **Bionic Reading:** Toggle Bionic Reading in the settings to algorithmically bold the first half of every word, creating artificial fixation points that help you skim and read significantly faster.
- ⏱️ **Smart WPM Tracking:** The app silently tracks how fast you read and calculates an exponential moving average of your real-world Words Per Minute. Your "Estimated Time Left" dynamically adjusts to your personal speed!
- 🎨 **Themes & Typography:** Switch between gorgeous Serif, Sans-Serif, and Monospace fonts. Read comfortably with Light, Dark, Sepia (warm paper), and E-Ink (high contrast gray) themes.
- ✍️ **Highlights & Quotes:** Highlight your favorite passages while reading to save them directly to a beautiful feed in your Stats tab.

## 📚 How to Add New Books

PageHabit fetches `.epub` files directly from this repository's `/books/` folder. 

1. Find any `.epub` file you want to read (e.g., from Project Gutenberg).
2. Upload it to the `/books/` folder in this repository.
3. Open the app and tap **Sync** in the Stats tab. Your new book will instantly appear in the library!

## 🛠️ Tech Stack

- **Architecture:** Zero-build, pure vanilla HTML/CSS/JS. No bundlers, no frameworks, no backend.
- **Parsing:** Powered by [JSZip](https://stuk.github.io/jszip/) to unzip and parse EPUBs entirely on the client side.
- **State:** Uses `localStorage` to save your streaks, saved quotes, settings, and reading progress.

## 🚀 Installation

Because PageHabit is a PWA, you don't need the App Store.

1. Open the [Live Link](https://PhaNtoM-GHosT-11101.github.io/reading-habit-app) in Safari (iOS) or Chrome (Android).
2. Tap the **Share** button (iOS) or **Menu** button (Android).
3. Select **"Add to Home Screen"**.
4. You now have a native-feeling, fully-offline e-reader on your phone!
