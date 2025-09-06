// Cookie consent logic
// Responsible for displaying a consent banner, storing the user’s choice and
// loading analytics only after acceptance. The banner is hidden on subsequent
// visits for one year by saving the preference in localStorage.

document.addEventListener('DOMContentLoaded', () => {
  const banner = document.querySelector('.cookie-banner');
  if (!banner) return;
  const pref = localStorage.getItem('cookie_consent');
  if (!pref) {
    // Show the banner until the user makes a choice
    banner.style.display = 'block';
  } else if (pref === 'accepted') {
    // Immediately load analytics if previously accepted
    if (typeof loadGA === 'function') loadGA();
  }
});

function acceptCookies() {
  localStorage.setItem('cookie_consent', 'accepted');
  // Hide banner
  const banner = document.querySelector('.cookie-banner');
  if (banner) banner.style.display = 'none';
  // Load GA4
  if (typeof loadGA === 'function') loadGA();
}

function rejectCookies() {
  localStorage.setItem('cookie_consent', 'rejected');
  const banner = document.querySelector('.cookie-banner');
  if (banner) banner.style.display = 'none';
}