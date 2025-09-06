// Google Analytics 4 loader
// This module exposes a function to inject the GA4 tag into the page once
// consent has been granted. A placeholder MEASUREMENT_ID is used and must be
// replaced with your real GA4 ID at deployment time.

/**
 * Loads the gtag.js library and initialises Google Analytics 4.
 * Call this only after the user has accepted analytics cookies.
 */
function loadGA() {
  // Avoid loading GA multiple times
  if (window.gtag) return;
  const tagId = 'G-XXXXXXX'; // Replace with real GA4 measurement ID
  // Inject the script asynchronously into the document head
  const gtagScript = document.createElement('script');
  gtagScript.async = true;
  gtagScript.src = `https://www.googletagmanager.com/gtag/js?id=${tagId}`;
  document.head.appendChild(gtagScript);
  // Define the gtag function and initial configuration
  window.dataLayer = window.dataLayer || [];
  function gtag() { dataLayer.push(arguments); }
  window.gtag = gtag;
  gtag('js', new Date());
  gtag('config', tagId);
}

/**
 * Wrapper to send custom events to GA4. If GA4 has not loaded yet, the event
 * call will be ignored. This allows you to call trackEvent safely anywhere
 * after ga4.js has been imported.
 *
 * @param {string} name Name of the event
 * @param {object} params Additional parameters for the event
 */
function trackEvent(name, params = {}) {
  if (typeof window.gtag === 'function') {
    window.gtag('event', name, params);
  }
}