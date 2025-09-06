// NeuroFit Website JavaScript - Fixed Version
// Handles navigation, modals, cookies, analytics, and Stripe integration

(function() {
    'use strict';

    // Configuration
    const CONFIG = {
        stripePublishableKey: 'pk_test_51234567890abcdefghijklmnopqrstuvwxyz', // Replace with actual key
        ga4MeasurementId: 'G-XXXXXXXXXX', // Replace with actual measurement ID
        cookieConsentKey: 'neurofit-cookie-consent',
        cookieConsentDuration: 365 // days
    };

    // Initialize Stripe
    let stripe;
    
    // DOM Elements - Initialize after DOM loads
    let elements = {};

    // Utility Functions
    function setCookie(name, value, days) {
        const expires = new Date();
        expires.setTime(expires.getTime() + (days * 24 * 60 * 60 * 1000));
        document.cookie = `${name}=${value};expires=${expires.toUTCString()};path=/;SameSite=Strict`;
    }

    function getCookie(name) {
        const nameEQ = name + "=";
        const ca = document.cookie.split(';');
        for (let i = 0; i < ca.length; i++) {
            let c = ca[i];
            while (c.charAt(0) === ' ') c = c.substring(1, c.length);
            if (c.indexOf(nameEQ) === 0) return c.substring(nameEQ.length, c.length);
        }
        return null;
    }

    function debounce(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    }

    // Initialize DOM Elements
    function initElements() {
        elements = {
            navToggle: document.querySelector('.nav__toggle'),
            navMenu: document.querySelector('.nav__menu'),
            cookieBanner: document.getElementById('cookie-banner'),
            acceptCookies: document.getElementById('accept-cookies'),
            declineCookies: document.getElementById('decline-cookies'),
            stripeButtons: document.querySelectorAll('.stripe-checkout'),
            modals: document.querySelectorAll('.modal'),
            modalTriggers: document.querySelectorAll('.modal-trigger'),
            modalCloses: document.querySelectorAll('.modal__close'),
            leadForm: document.querySelector('.lead-form'),
            navLinks: document.querySelectorAll('a[href^="#"]'),
            heroActions: document.querySelectorAll('.hero__actions a[href^="#"]')
        };
    }

    // Google Analytics 4 Integration
    function initGA4(hasConsent) {
        if (!CONFIG.ga4MeasurementId || CONFIG.ga4MeasurementId === 'G-XXXXXXXXXX') {
            console.warn('GA4 Measurement ID not configured');
            return;
        }

        // Load gtag script
        const script = document.createElement('script');
        script.async = true;
        script.src = `https://www.googletagmanager.com/gtag/js?id=${CONFIG.ga4MeasurementId}`;
        document.head.appendChild(script);

        // Initialize gtag
        window.dataLayer = window.dataLayer || [];
        function gtag() { dataLayer.push(arguments); }
        window.gtag = gtag;

        gtag('js', new Date());
        
        // Configure consent mode
        gtag('consent', 'default', {
            'analytics_storage': hasConsent ? 'granted' : 'denied',
            'ad_storage': hasConsent ? 'granted' : 'denied'
        });

        gtag('config', CONFIG.ga4MeasurementId, {
            anonymize_ip: true,
            cookie_flags: 'SameSite=Strict;Secure'
        });

        // Track key events if consent given
        if (hasConsent) {
            setupGA4Events();
        }
    }

    function setupGA4Events() {
        // Track pricing button clicks
        elements.stripeButtons.forEach(button => {
            button.addEventListener('click', function() {
                const priceId = this.dataset.priceId;
                const tier = priceId.includes('starter') ? 'Starter' : 
                           priceId.includes('complete') ? 'Complete' : 'Premium';
                
                if (window.gtag) {
                    gtag('event', 'begin_checkout', {
                        currency: 'GBP',
                        value: tier === 'Starter' ? 47 : tier === 'Complete' ? 97 : 197,
                        items: [{
                            item_id: priceId,
                            item_name: `NeuroFit ${tier}`,
                            category: 'Training Programme',
                            quantity: 1,
                            price: tier === 'Starter' ? 47 : tier === 'Complete' ? 97 : 197
                        }]
                    });
                }
            });
        });

        // Track lead form submissions
        if (elements.leadForm) {
            elements.leadForm.addEventListener('submit', function() {
                if (window.gtag) {
                    gtag('event', 'generate_lead', {
                        event_category: 'Lead Generation',
                        event_label: 'Free Guide Download'
                    });
                }
            });
        }
    }

    function updateGA4Consent(hasConsent) {
        if (window.gtag) {
            gtag('consent', 'update', {
                'analytics_storage': hasConsent ? 'granted' : 'denied',
                'ad_storage': hasConsent ? 'granted' : 'denied'
            });
            
            if (hasConsent) {
                setupGA4Events();
            }
        }
    }

    // Cookie Consent Management
    function initCookieConsent() {
        const existingConsent = getCookie(CONFIG.cookieConsentKey);
        
        if (existingConsent === null) {
            // Show banner if no previous consent
            if (elements.cookieBanner) {
                elements.cookieBanner.classList.remove('hidden');
            }
        } else {
            // Initialize GA4 based on existing consent
            const hasConsent = existingConsent === 'accepted';
            initGA4(hasConsent);
        }
    }

    function handleCookieConsent(accepted) {
        setCookie(CONFIG.cookieConsentKey, accepted ? 'accepted' : 'declined', CONFIG.cookieConsentDuration);
        if (elements.cookieBanner) {
            elements.cookieBanner.classList.add('hidden');
        }
        
        if (accepted) {
            initGA4(true);
        } else {
            initGA4(false);
        }
        
        // Update existing GA4 if already loaded
        updateGA4Consent(accepted);
    }

    // Mobile Navigation
    function initMobileNav() {
        if (!elements.navToggle || !elements.navMenu) return;

        elements.navToggle.addEventListener('click', function(e) {
            e.preventDefault();
            const isActive = this.classList.contains('active');
            
            this.classList.toggle('active');
            elements.navMenu.classList.toggle('active');
            
            // Update aria-expanded for accessibility
            this.setAttribute('aria-expanded', !isActive);
            
            // Prevent body scroll when menu is open
            if (!isActive) {
                document.body.style.overflow = 'hidden';
            } else {
                document.body.style.overflow = '';
            }
        });

        // Close menu on link click (mobile)
        elements.navMenu.addEventListener('click', function(e) {
            if (e.target.classList.contains('nav__link') || e.target.classList.contains('btn')) {
                elements.navToggle.classList.remove('active');
                elements.navMenu.classList.remove('active');
                elements.navToggle.setAttribute('aria-expanded', 'false');
                document.body.style.overflow = '';
            }
        });

        // Close menu on window resize
        window.addEventListener('resize', debounce(function() {
            if (window.innerWidth > 768) {
                elements.navToggle.classList.remove('active');
                elements.navMenu.classList.remove('active');
                elements.navToggle.setAttribute('aria-expanded', 'false');
                document.body.style.overflow = '';
            }
        }, 250));
    }

    // Modal Management
    function initModals() {
        // Open modals
        elements.modalTriggers.forEach(trigger => {
            trigger.addEventListener('click', function(e) {
                e.preventDefault();
                const modalId = this.dataset.modal;
                const modal = document.getElementById(modalId);
                
                if (modal) {
                    openModal(modal);
                    
                    // Track modal opens
                    if (window.gtag) {
                        gtag('event', 'modal_open', {
                            event_category: 'Engagement',
                            event_label: modalId.replace('-modal', '')
                        });
                    }
                }
            });
        });

        // Close modals
        elements.modalCloses.forEach(closeBtn => {
            closeBtn.addEventListener('click', function(e) {
                e.preventDefault();
                const modal = this.closest('.modal');
                closeModal(modal);
            });
        });

        // Close modal on overlay click
        elements.modals.forEach(modal => {
            modal.addEventListener('click', function(e) {
                if (e.target === this || e.target.classList.contains('modal__overlay')) {
                    closeModal(this);
                }
            });
        });

        // Close modal on Escape key
        document.addEventListener('keydown', function(e) {
            if (e.key === 'Escape') {
                const openModal = document.querySelector('.modal:not(.hidden)');
                if (openModal) {
                    closeModal(openModal);
                }
            }
        });
    }

    function openModal(modal) {
        if (modal) {
            modal.classList.remove('hidden');
            modal.setAttribute('aria-hidden', 'false');
            document.body.style.overflow = 'hidden';
            
            // Focus management for accessibility
            const closeButton = modal.querySelector('.modal__close');
            if (closeButton) {
                setTimeout(() => closeButton.focus(), 100);
            }
        }
    }

    function closeModal(modal) {
        if (modal) {
            modal.classList.add('hidden');
            modal.setAttribute('aria-hidden', 'true');
            document.body.style.overflow = '';
        }
    }

    // Stripe Checkout Integration
    function initStripe() {
        // Initialize Stripe
        if (typeof Stripe !== 'undefined') {
            stripe = Stripe(CONFIG.stripePublishableKey);
        } else {
            console.warn('Stripe not loaded');
            return;
        }
    }

    function initStripeCheckout() {
        if (!stripe) {
            console.warn('Stripe not initialized');
            return;
        }

        elements.stripeButtons.forEach(button => {
            button.addEventListener('click', async function(e) {
                e.preventDefault();
                
                const priceId = this.dataset.priceId;
                if (!priceId) {
                    console.error('No price ID found');
                    return;
                }

                // Show loading state
                const originalText = this.textContent;
                this.textContent = 'Loading...';
                this.classList.add('loading');
                this.disabled = true;

                try {
                    // In production, this would call your backend to create a checkout session
                    // For demo purposes, we'll simulate the process
                    await new Promise(resolve => setTimeout(resolve, 1000));
                    
                    // Show demo message since we can't actually process payments
                    alert(`Demo Mode: Would redirect to Stripe checkout for ${priceId}\n\nIn production, this would redirect to Stripe's secure checkout page.`);
                    
                    // In real implementation, use this:
                    /*
                    const { error } = await stripe.redirectToCheckout({
                        lineItems: [{
                            price: priceId,
                            quantity: 1
                        }],
                        mode: 'payment',
                        successUrl: `${window.location.origin}/success?session_id={CHECKOUT_SESSION_ID}`,
                        cancelUrl: `${window.location.origin}/pricing`,
                        billingAddressCollection: 'required',
                        shippingAddressCollection: {
                            allowedCountries: ['GB', 'IE']
                        }
                    });

                    if (error) {
                        console.error('Stripe error:', error);
                        alert('Payment failed. Please try again.');
                    }
                    */
                } catch (error) {
                    console.error('Checkout error:', error);
                    alert('Unable to process payment. Please try again later.');
                } finally {
                    // Reset button state
                    this.textContent = originalText;
                    this.classList.remove('loading');
                    this.disabled = false;
                }
            });
        });
    }

    // Lead Form Handling
    function initLeadForm() {
        if (!elements.leadForm) return;

        elements.leadForm.addEventListener('submit', function(e) {
            const submitBtn = this.querySelector('button[type="submit"]');
            const originalText = submitBtn.textContent;
            
            // Show loading state
            submitBtn.textContent = 'Sending...';
            submitBtn.disabled = true;
            
            // Form will be handled by Netlify
            // Reset button after form submission
            setTimeout(() => {
                submitBtn.textContent = 'Thank you!';
                setTimeout(() => {
                    submitBtn.textContent = originalText;
                    submitBtn.disabled = false;
                    this.reset();
                }, 2000);
            }, 1000);
        });

        // Email validation enhancement
        const emailInput = elements.leadForm.querySelector('input[type="email"]');
        if (emailInput) {
            emailInput.addEventListener('blur', function() {
                const isValid = this.checkValidity();
                this.classList.toggle('invalid', !isValid);
                
                // Show custom validation message
                if (!isValid && this.value) {
                    this.setCustomValidity('Please enter a valid email address');
                } else {
                    this.setCustomValidity('');
                }
            });
        }
    }

    // Smooth Scrolling for Anchor Links
    function initSmoothScrolling() {
        // Get all links that point to sections on the same page
        const allAnchorLinks = document.querySelectorAll('a[href^="#"]');
        
        allAnchorLinks.forEach(link => {
            link.addEventListener('click', function(e) {
                const href = this.getAttribute('href');
                
                // Skip if it's just "#" or empty
                if (!href || href === '#') return;
                
                const target = document.querySelector(href);
                
                if (target) {
                    e.preventDefault();
                    
                    // Calculate offset for fixed header
                    const header = document.querySelector('.header');
                    const headerHeight = header ? header.offsetHeight : 0;
                    const targetPosition = target.offsetTop - headerHeight - 20;
                    
                    window.scrollTo({
                        top: targetPosition,
                        behavior: 'smooth'
                    });
                    
                    // Update URL hash
                    if (history.pushState) {
                        history.pushState(null, null, href);
                    }
                }
            });
        });
    }

    // FAQ Toggle Enhancement
    function initFAQ() {
        const faqItems = document.querySelectorAll('.faq__item');
        
        faqItems.forEach(item => {
            const question = item.querySelector('.faq__question');
            
            if (question) {
                question.addEventListener('click', function() {
                    // Track FAQ interactions
                    if (window.gtag) {
                        gtag('event', 'faq_interaction', {
                            event_category: 'Engagement',
                            event_label: question.textContent.trim()
                        });
                    }
                });
            }
        });
    }

    // Accessibility Enhancements
    function initAccessibility() {
        // Skip link functionality
        const skipLink = document.querySelector('a[href="#main-content"]');
        if (skipLink) {
            skipLink.addEventListener('click', function(e) {
                e.preventDefault();
                const target = document.getElementById('main-content');
                if (target) {
                    target.focus();
                    target.scrollIntoView();
                }
            });
        }

        // Keyboard navigation for custom elements
        document.addEventListener('keydown', function(e) {
            // Custom handling for FAQ items
            if (e.target.classList.contains('faq__question') && (e.key === 'Enter' || e.key === ' ')) {
                e.preventDefault();
                e.target.click();
            }
        });
    }

    // Error Handling and Fallbacks
    function initErrorHandling() {
        window.addEventListener('error', function(e) {
            console.error('JavaScript error:', e.error);
            
            // Track errors if GA4 is available
            if (window.gtag) {
                gtag('event', 'exception', {
                    description: e.error?.message || 'Unknown error',
                    fatal: false
                });
            }
        });

        // Handle unhandled promise rejections
        window.addEventListener('unhandledrejection', function(e) {
            console.error('Unhandled promise rejection:', e.reason);
            
            if (window.gtag) {
                gtag('event', 'exception', {
                    description: e.reason?.message || 'Promise rejection',
                    fatal: false
                });
            }
        });
    }

    // Main Initialization Function
    function init() {
        // Initialize DOM elements first
        initElements();

        // Core functionality
        initCookieConsent();
        initMobileNav();
        initModals();
        initSmoothScrolling();
        initLeadForm();
        initFAQ();
        initAccessibility();
        initErrorHandling();

        // Initialize Stripe
        initStripe();
        if (stripe) {
            initStripeCheckout();
        }

        // Initialize cookie consent event handlers
        if (elements.acceptCookies) {
            elements.acceptCookies.addEventListener('click', () => handleCookieConsent(true));
        }
        
        if (elements.declineCookies) {
            elements.declineCookies.addEventListener('click', () => handleCookieConsent(false));
        }

        console.log('NeuroFit website initialized successfully');
    }

    // Initialize when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }

    // Expose necessary functions globally for debugging
    window.NeuroFit = {
        closeModal,
        openModal,
        handleCookieConsent,
        updateGA4Consent,
        init
    };

})();