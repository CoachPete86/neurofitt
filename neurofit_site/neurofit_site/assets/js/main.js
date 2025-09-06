// NeuroFit Main JavaScript
// This file initialises interactive behaviour such as the mobile navigation
// toggle and simple event handlers. It delegates analytics and consent
// responsibilities to ga4.js and consent.js.

document.addEventListener('DOMContentLoaded', () => {
  // Mobile navigation toggle
  const navToggle = document.querySelector('.mobile-nav-toggle');
  const navMenu = document.querySelector('header nav ul');
  if (navToggle && navMenu) {
    navToggle.addEventListener('click', () => {
      navMenu.classList.toggle('open');
    });
  }

  // Lead magnet form submission
  const leadForm = document.querySelector('.lead-form');
  if (leadForm) {
    leadForm.addEventListener('submit', (e) => {
      // Prevent default submission to show a thank you message; Netlify will
      // still process the form because of the hidden input [name='form-name']
      e.preventDefault();
      const formData = new FormData(leadForm);
      const name = formData.get('name');
      const email = formData.get('email');
      // You could send this data to a CRM or trigger further actions here
      alert('Thank you for signing up, ' + name + '! We\'ll be in touch soon.');
      // Track event via GA4 if available
      if (typeof trackEvent === 'function') {
        trackEvent('lead_form_submission', { email: email });
      }
      // Reset the form
      leadForm.reset();
    });
  }
});