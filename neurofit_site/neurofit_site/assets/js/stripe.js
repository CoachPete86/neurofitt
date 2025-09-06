// Stripe Checkout integration
// This script initialises Stripe with a publishable key and exposes a helper
// function for redirecting to Checkout. Replace the publishable key and price
// identifiers with your own values.

// Lazy load Stripe only when needed to reduce initial load times
let stripeInstance = null;

/**
 * Ensure Stripe.js is loaded and return the Stripe instance. You must
 * replace the PUBLISHABLE_KEY placeholder with your real key.
 * @returns {Promise<Stripe>} A promise resolving with the Stripe instance.
 */
async function getStripe() {
  if (stripeInstance) return stripeInstance;
  const publishableKey = 'pk_test_placeholder'; // Replace with your publishable key
  // Load Stripe script if not present
  if (!window.Stripe) {
    await new Promise((resolve, reject) => {
      const script = document.createElement('script');
      script.src = 'https://js.stripe.com/v3/';
      script.onload = resolve;
      script.onerror = reject;
      document.head.appendChild(script);
    });
  }
  stripeInstance = window.Stripe(publishableKey);
  return stripeInstance;
}

/**
 * Redirects the user to a Stripe Checkout session for a given price ID.
 * The success and cancel URLs should point back to your deployed site. The
 * quantity is fixed at 1.
 *
 * @param {string} priceId The Stripe price identifier
 */
async function checkout(priceId) {
  const stripe = await getStripe();
  stripe.redirectToCheckout({
    lineItems: [{ price: priceId, quantity: 1 }],
    mode: 'payment',
    successUrl: window.location.origin + '/pricing.html?success=true',
    cancelUrl: window.location.origin + '/pricing.html?canceled=true'
  }).then((result) => {
    if (result.error) {
      alert(result.error.message);
    }
  });
}