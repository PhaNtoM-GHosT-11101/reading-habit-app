const CACHE_NAME = 'pagehabit-v1';
const ASSETS = [
  './',
  './index.html',
  './manifest.json',
  'https://cdnjs.cloudflare.com/ajax/libs/jszip/3.10.1/jszip.min.js',
  'https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Lora:ital,wght@0,400;0,500;1,400&display=swap'
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => cache.addAll(ASSETS))
  );
  self.skipWaiting();
});

self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(keys =>
      Promise.all(keys.filter(key => key !== CACHE_NAME).map(key => caches.delete(key)))
    )
  );
  self.clients.claim();
});

self.addEventListener('fetch', event => {
  if (event.request.method !== 'GET') return;

  // Never cache API calls — always go to network
  if (event.request.url.includes('api.github.com') ||
      event.request.url.includes('firestore.googleapis.com') ||
      event.request.url.includes('dictionaryapi.dev') ||
      event.request.url.includes('identitytoolkit.googleapis.com')) {
    event.respondWith(
      fetch(event.request).catch(() => new Response(JSON.stringify([]), {
        headers: { 'Content-Type': 'application/json' }
      }))
    );
    return;
  }

  // Network first, fallback to cache for everything else
  event.respondWith(
    fetch(event.request)
      .then(response => {
        if (response && response.status === 200) {
          const resClone = response.clone();
          caches.open(CACHE_NAME).then(cache => cache.put(event.request, resClone));
        }
        return response;
      })
      .catch(() => caches.match(event.request))
  );
});
