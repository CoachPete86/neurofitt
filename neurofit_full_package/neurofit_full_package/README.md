# NeuroFit Launch Package

This package contains everything you need to deploy and operate the NeuroFit programme, including the static website, legal documents and marketing assets. Below is an overview of the contents:

## Directory structure

```
/
├── README.md            # This overview
├── neurofit_site/        # Production-ready static website
│   ├── index.html        # Sales landing page with hero, features and lead form
│   ├── pricing.html      # Pricing tiers with Stripe Checkout buttons and FAQs
│   ├── guide.html        # Canonical guide covering workouts, meal planning and tracking
│   ├── about.html        # About page for Pete Ryan and his credentials
│   ├── corporate.html    # Corporate offering overview and pitch
│   ├── 404.html          # Custom 404 error page
│   ├── assets/           # CSS, JS and image assets
│   └── legal/            # Redirect pages for legal documents
│       ├── terms.html    # Redirect to the Terms & Conditions
│       ├── privacy.html  # Redirect to the Privacy Policy
│       ├── cookies.html  # Redirect to the Cookie Policy
│       ├── medical.html  # Full Medical Disclaimer
│       └── returns.html  # Full Returns & Refunds policy
├── terms.html            # Full Terms & Conditions
├── privacy.html          # Full Privacy Policy
├── cookies.html          # Full Cookie Policy
├── medical.html          # Redirects to the Medical Disclaimer in legal/
├── returns.html          # Redirects to the Returns & Refunds policy in legal/
├── deliverables_step2_and_3.txt
│                          # Step 2: Interactive workbook instructions
│                          # Step 3: Exercise demo library plan
└── deliverables_steps5_to_13.txt
                           # Step 5: Compliance pack summary
                           # Step 6: Analytics & Trust guidelines
                           # Step 7: Sales funnel assets
                           # Step 9: Corporate pack summary
                           # Step 10: Ops & QA docs
                           # Step 11: Final packaging notes
                           # Step 13: Deployment & launch instructions
```

## How to use

1. **Read the legal documents** – The Terms & Conditions (`terms.html`), Privacy Policy (`privacy.html`), and Cookie Policy (`cookies.html`) live at the root.  The Medical Disclaimer and Returns & Refunds Policy are in the `legal/` directory (`legal/medical.html` and `legal/returns.html`); the root‑level `medical.html` and `returns.html` files are simple redirects. All legal pages are linked from the website footer.
2. **Deploy the website** (`neurofit_site/`). You can upload this directory to Netlify or GitHub Pages. Follow the detailed deployment instructions in `deliverables_steps5_to_13.txt` (Step 13).
3. **Consult the guide** (`guide.html`) for the programme content and to embed the workbook and exercise library.
4. **Use the deliverables documents**:
   - `deliverables_step2_and_3.txt` – Provides interactive workbook instructions (Step 2) and the exercise demo library plan (Step 3).
   - `deliverables_steps5_to_13.txt` – Summarises the compliance pack (Step 5), analytics and trust guidelines (Step 6), sales funnel assets (Step 7), corporate pack summary (Step 9), operations & QA docs (Step 10), final packaging instructions (Step 11) and deployment & launch instructions (Step 13).

If you need to modify or extend the site, edit the files in `neurofit_site/`. Remember to update links in the footer if you relocate the legal documents. For marketing, use the sales funnel assets to design your email automation and content calendar.

For any questions or support, contact **support@neurofit.co.uk**.