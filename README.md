# Sharpe's Septic — Website Refresh (Splash Omnimedia) · **CLIENT PREVIEW**

A modernized, CMS-ready **refresh** of the Sharpe's Septic Tank & Well Drilling Service website. Keeps the company's existing identity, sitemap, and service hierarchy; improves layout, navigation, mobile, accessibility, and conversion. A refresh — not a redesign, rebuild, or rebrand. Source of truth: https://www.sharpessepticandwelldrilling.com/

---

## Internal QA Before Sending Client Link

Run this checklist on the deployed GitHub Pages URL before sharing:

- [ ] **Open the deployed GitHub Pages URL.**
- [ ] **Confirm images load** (see the bold remote-image note below — this is the #1 risk).
- [ ] Confirm the logo loads in header and footer.
- [ ] Confirm no visible template tokens anywhere.
- [ ] Confirm no broken internal links.
- [ ] Spot-check Homepage, Septic Services, Well Drilling, Grease Interceptors, Contact, and FAQs.
- [ ] Confirm mobile nav opens/closes.
- [ ] Confirm sticky mobile CTA bar shows and doesn't cover content.
- [ ] Confirm contact-form success message appears without navigation.
- [ ] Confirm temporary photography placeholders are acceptable for this review.
- [ ] Confirm ServiceTitan / Customer Portal / Financing / Social Feed / Promo Popup are hidden.
- [ ] Confirm client-facing copy contains no internal uncertainty language.
- [ ] In the note to the client, say current images are temporary until the photo/video shoot assets are ready.

> ### ⚠️ REMOTE IMAGE DEPENDENCY — open the GitHub Pages URL and confirm all remote images load before sending to client.
> Images load **remotely from the live Sharpe's website** (its WordPress CDN). Image binaries are **not** bundled in `assets/images/` (only `manifest.json` + `download-assets.sh`) — they could not be downloaded from the build environment. Every remote image uses `referrerpolicy="no-referrer"` to reduce cross-origin hotlink blocking, but this is not guaranteed. **To make the preview fully self-contained, localize the images (see "Asset handling" below).**

---

## 1. Preview status & client-readiness

**Rating: Client-ready with minor refinements.** Static HTML/CSS/JS — no build step, no server, no Python needed to preview. All client-visible tokens and fabricated testimonials removed; hidden modules carry no live tokens or broken links.

## 2. File structure

```
sharpes-septic-refresh-client-preview/
├── index.html                              Homepage (root — required for GitHub Pages)
├── septic-services.html  + 4 sub-pages
├── well-drilling.html    + 3 sub-pages
├── grease-interceptors.html + 2 sub-pages
├── precast-tanks.html
├── faqs.html  /  associations-licensing.html
├── why-sharpes.html  /  reviews.html  /  review-us.html
├── contact.html
├── .nojekyll                               Serve files as-is on GitHub Pages
├── assets/
│   ├── styles.css                          Shared design system (CSS variables)
│   ├── main.js                             Shared behavior, dependency-free
│   └── images/
│       ├── manifest.json                   Each asset → live-site source URL
│       └── download-assets.sh              Pulls local copies of the real assets
├── build.py / pages.py / service_content.py / other_pages.py   Generators (reference only)
└── README.md
```

## 3. Page inventory (20 pages)

Home · Septic Services · Septic Installation · Septic Repairs & Replacement · Septic Pumping · Septic Inspections · Well Drilling · Well Installation · Well Repair & Maintenance · Well Inspections · Grease Interceptors · Grease Interceptor Installation · Grease Interceptor Pumping & Inspections · Precast Tanks · FAQs · Associations & Licensing · Why Sharpe's · Our Reviews · Review Us · Contact.

Verified: 0 broken internal links · one `<h1>` per page · 20 unique title tags · meta description on every page.

## 4. How to preview

- **Locally:** open `index.html` in any browser (internet required for images).
- **GitHub Pages:** copy this folder's contents to the repo root → Settings → Pages → Deploy from a branch → `/ (root)` → open the URL and run the Internal QA checklist above. Paths are relative and case-correct; `.nojekyll` is included.

## 5. Asset handling — images are REMOTE

Toggle in `build.py` (`USE_REMOTE_ASSETS = True`). To localize:
1. `bash assets/images/download-assets.sh` (saves assets into `assets/images/` with manifest filenames).
2. Set `USE_REMOTE_ASSETS = False` in `build.py`.
3. `python3 pages.py` to regenerate HTML pointing at local files.

Source URLs are preserved in `assets/images/manifest.json`.

**Real assets in use** (temporary current-site imagery; each tagged with a "replace after shoot" comment + alt text):
logo (`sharpes-logo-current.png`, includes LLC) · home hero (`sharpes-home-banner.jpg`) · Lexington's Best badge (`bestoflex-2025.png`) · `sharpes-about-trust.jpg` · `sharpes-septic-team.jpg` · `sharpes-well-frontyard.jpg` · `sharpes-well-tools.jpg` · `sharpes-grease-digging.jpg` · `sharpes-grease-backing-up.jpg` · `sharpes-precast-frontyard.jpg`.

## 6. Tokens & comments

**No `{{...}}` tokens remain anywhere in the HTML** (verified). Hidden conditional modules now use `data-url=""` and `href="#"` instead of tokens, with developer comments explaining what to add. The contact form uses `action=""` (prototype mode). Internal `OPEN ITEM` / `CMS:` / `TODO` notes were removed from HTML and live only in this README.

## 7. Conditional modules — hidden by default

ServiceTitan Book Now · Customer Portal · Financing · Promo Popup · Social Feed — all OFF by default, no dead buttons, no visible tokens, no financing claims, popup never auto-opens. Each shows only when given a real URL/embed (or `data-enabled="true"`). Implementation: `assets/main.js`.

## 8. Contact form (preview behavior)

Fields: Name\*, Phone\*, Email\*, Service Type, Property City/Location, Message/Service Need. Service Type options: Septic Pumping, Septic Inspection, Septic Repair/Replacement, Septic Installation, Well Installation, Well Repair/Maintenance, Well Inspection, Grease Interceptor Installation, Grease Interceptor Pumping/Inspection, Precast Tanks, Other/Not Sure.

Prototype: required-field + email validation with accessible field-tied errors; on valid submit it does **not** navigate and shows *"Thank you for contacting Sharpe's. Our team has received your request and will follow up to help you determine the next step."* URL prefill works: `contact.html?service=septic-inspection`. **Connect a production endpoint before launch** (set the form `action`).

## 9. Testimonials — source status

Testimonials in this preview are pulled from the current live site or confirmed project materials — **no fabricated/representative quotes, no invented cities.** Used: Patrick H., Anonymous, Blair C., Christina M., Katherine D., Stephanie W. Confirm which are approved for reuse before launch.

## 10. Placeholders remaining

After the Final QA pass, visible "Future Photography Placeholder" blocks remain on only **three** pages, each because no suitable real image exists yet:

- **Septic Inspections** — no inspection-specific photo available.
- **Associations & Licensing** — awaiting credential/association logos.
- **Contact** — awaiting the live Google Maps embed.

The homepage has **no visible placeholder** (its hero and "symptom" sections use real current-site photos; the only placeholder is inside the hidden ServiceTitan block, which never displays). Service-detail pages that previously showed placeholders (Septic Installation, Septic Repairs & Replacement, Well Repair & Maintenance, Well Inspections, Grease Interceptor Pumping & Inspections) now use contextually appropriate real current-site images. No raw `[Photo Placeholder]` text appears anywhere.

## 11. Tracking hooks

`data-track` → `window.dataLayer` (GA4/GTM-ready): `phone_click`, `book_now_click`, `customer_portal_click`, `contact_form_start`, `contact_form_submit`, `service_type_selection`, `request_inspection_click`, `request_estimate_click`, `request_commercial_service_click`, `financing_click`, `faq_expand`, `review_click`, `service_card_click`, `promo_popup_open`, `promo_popup_close`, `social_feed_click`.

## 12. Accessibility

One H1/page · logical headings · skip link · keyboard nav + submenus (`aria-expanded`, Esc closes) · labeled mobile nav toggle · native `<details>` FAQ accordions · visible focus states · labeled fields with field-tied errors · alt text on every image · accessible "Future Photography Placeholder" labels · `prefers-reduced-motion` support · 48px+ tap targets · sticky mobile CTA with body bottom-padding so it never covers content.

## 13. SEO / GEO / AI structure

Each page has a unique title, meta description, single H1, clear H2s, service-specific crawlable text, and internal links to related services. **Accurate `LocalBusiness` JSON-LD is embedded on every page** (name, phone, address, areaServed, foundingDate 1966, URL).

**Schema TODOs for production** (add when accurate): `Organization`, `Service` (per service page), `FAQPage` (FAQs + service pages with FAQ blocks), `BreadcrumbList` (service sub-pages). Do not add inaccurate schema.

## 14. Known open items (README only — not on client pages)

- Confirm final legal business name and **LLC** usage.
- Confirm final **logo asset** with LLC (preview uses live-site `Sharpes-add-LLC.png`).
- Confirm **ServiceTitan booking URL** · **Customer Portal URL**.
- Confirm **GreenSky/ServiceTitan financing language** (financing stays hidden until approved copy supplied).
- Confirm whether **DHEC** language should remain or be updated before launch. *(Footer currently reads "Licensed · Bonded · Insured · DHEC", matching the live site. SCDES wording is NOT used on the visible site until confirmed.)*
- Confirm final **service area** list.
- Confirm final **photography/video** assets from the shoot.
- Confirm whether **"Voted Lexington's Best Four Years In A Row"** badge + exact wording should remain visible.
- Confirm **testimonials** approved for reuse.
- Confirm whether **social feed** integration is approved.
- Confirm whether the **promotional popup** should be enabled.
- Confirm whether **current-site photos** are acceptable as temporary imagery.
- Hero image is temporary current-site imagery pending the photography shoot.

## 15. Exact next steps for Splash

1. Internal review of Homepage, service templates, Contact, FAQs.
2. **Localize images** (section 5), then re-confirm rendering.
3. Push to GitHub, enable Pages, run the Internal QA checklist above.
4. Confirm logo/LLC, ServiceTitan + Portal URLs, financing decision, DHEC wording, award badge, approved testimonials.
5. Schedule/complete the photo shoot; swap temporary images.
6. Connect the contact-form endpoint; configure GA4/GTM; add remaining schema.
7. Final mobile/accessibility QA, then send the client preview link with a note that imagery is temporary.

---

## Design direction

Palette and type pulled from Sharpe's current site CSS — brand red `#DB222A`, charcoal `#231F20`, amber accent `#F5A623`, **Lato** throughout. All colors/fonts are CSS variables at the top of `assets/styles.css` (`:root`) — re-theming is a one-file change.

## Real brand alignment (from live site)

Brand colors and type were verified against the live site's computed styles and matched exactly:
- **Type: Lato** sitewide (already in use).
- **Brand red `#DB222A`** for accents, links, buttons, and H1 (matches live).
- **Body text `#231F20`** (matches live).
- **Headings now follow the live site's system:** H1 is uppercase Lato (white on the red hero band; the brand red H1 applies on any light background), and H2 section headings use the live site's exact heading gray **`#58595B`**, uppercase. Eyebrow labels remain brand red, uppercase. Dark sections keep white headings.

## Main navigation redesign

The header was reworked so it no longer wraps or feels cramped:

- **Phone CTA fixed** — the old "Call (803) 755-1615" button wrapped to four lines. It's now a designed phone block (circular phone icon + "Call us today" label + number on one line) that never wraps; `white-space:nowrap` added to all buttons.
- **Nav typography** — tighter, bolder, single-line labels with an active-section indicator (brand-red underline / left bar in the drawer) and a brand-light hover pill.
- **Breakpoint raised to 1200px** — with 8 top-level items plus the phone block and CTA, the inline row only shows when there's genuinely room; below 1200px it collapses to the existing polished slide-in drawer + hamburger (no squeezing). Drawer offset synced to the 80px header height.
- **Header polish** — slightly taller bar, refined shadow, a 2px brand-light bottom hairline, smaller/cleaner logo sizing, and a subtle lift + shadow on the Schedule Service button.
- Sitemap, nav hierarchy, links, and the logo are unchanged.

## Custom icons (no emoji)

All emoji have been removed sitewide and replaced with a **custom inline SVG icon set** (consistent line-art, filled stars). Icons inherit color via `currentColor` and are sized by CSS (`.ico` plus context selectors), so they re-color to match the utility bar, brand service-card chips, trust bar, and footer. The set is generated in `build.py` (`_ICON_PATHS` / `_svg` / `_icons`, applied in `write()`), so re-running `python3 pages.py` keeps the HTML emoji-free. Icons covered: pin, clock, phone, lock, map, home, calendar, shield-check, truck, clarity (clear options), water drop (well), tank (septic), barrel (grease), block (precast), and star (ratings). Verified: 0 emoji remain in any HTML file.

## Final QA pass (Done With Excellence)

- **Placeholders reduced:** real current-site images assigned to five service-detail pages (Septic Installation, Septic Repairs & Replacement, Well Repair & Maintenance, Well Inspections, Grease Interceptor Pumping & Inspections). Visible placeholders now appear on only three pages (Septic Inspections, Associations & Licensing logos, Contact map) — each justified and polished. Homepage has none visible.
- **Image localization retried** — the build environment has no outbound network (`000` to all hosts), so images remain remote (see remote-image note). `download-assets.sh` + `manifest.json` + the `USE_REMOTE_ASSETS` toggle let Splash localize in three steps.
- **Hidden modules verified safe:** all conditional modules use empty `data-url=""`; the reveal logic in `main.js` requires a real (non-token, non-empty) URL or `data-enabled="true"`, so ServiceTitan, Customer Portal, Financing, Social Feed, and Promo Popup cannot display by accident. No dead buttons.
- **Verified clean:** 0 `{{tokens}}`, 0 `OPEN ITEM`/`TODO`/`CMS:` notes in HTML, 0 broken internal links, one H1 per page, alt text on every image, 20 unique titles + meta descriptions, all `tel:` links `+18037551615`, LocalBusiness JSON-LD on all 20 pages, contact form `action=""` (prototype) with the approved success message, service prefill (`?service=`) intact, reduced-motion + focus-visible + sticky-CTA clearance preserved.
- **Testimonials unchanged** — verified live-site/confirmed quotes only.

## Content revision pass (marketing / SEO / GEO / StoryBrand)

This revision improved marketing clarity and conversion without changing the design, sitemap, or page count:

- **Local SEO:** natural references to Columbia, Gaston, Lexington, and the surrounding Midlands added across the homepage and major service pages (not keyword-stuffed).
- **Direct-answer sections** ("Quick answer") added to all 13 service pages for SEO/GEO/AI visibility — each is a plain-text H2 question + concise answer (e.g., "How often should a septic tank be pumped?", "Do I need a septic inspection when buying or selling a home?").
- **Service-specific detail** added so pages read less templated: lift stations/Letts systems (septic), permitting guidance (installation), interceptor sizes 1,000–3,000 gal and business types (grease), product list incl. distribution boxes/lids/pole pads made in Sharpe's own plant (precast).
- **Audience resonance:** clearer language for homeowners, buyers/sellers/realtors, builders/property owners, and commercial-kitchen operators.
- **StoryBrand:** customer-as-hero framing, clearer problems, empathy + authority on Why Sharpe's, simple 3-step plans, success outcomes.
- **CTAs made specific:** "Schedule Well Service" (well repair), "Request Product Information" (precast), "View Septic Pumping / View Well Services" (homepage); removed all "schedule online" wording (booking not confirmed); "Learn more" replaced with "View [service]".
- **Contact:** added a "What happens next?" 3-step section and a "Select Other / Not Sure and we'll help route your request" reassurance line.
- **FAQs** expanded to 13 (added well-service signs, grease pumping/inspections, "what happens after I request service", buying/selling inspection, city-specific service area).
- **Testimonials unchanged** — still only verified live-site/confirmed quotes (Patrick H., Anonymous, Blair C., Christina M., Katherine D., Stephanie W.).
- Verified: 0 `{{tokens}}`, 0 internal notes in HTML, 0 broken links, one H1 per page, LocalBusiness JSON-LD on all 20 pages.

## What changed from the prior preview

1. **All hidden `{{tokens}}` removed** from HTML attributes (Customer Portal, ServiceTitan, contact-form endpoint) → safe `data-url=""` / `href="#"` / `action=""` with developer comments.
2. **Internal `OPEN ITEM` / `CMS:` / `TODO` comments stripped** from HTML (reproducibly, via the generator) and kept in this README only.
3. **Accurate `LocalBusiness` JSON-LD** added to every page; schema TODOs documented.
4. **Testimonial polish:** empty city `<span>` removed when a quote has no location.
5. **`.nojekyll` retained**, full GitHub-readiness + a11y/SEO/link QA (0 broken links, one H1/page, 20 unique titles, all images have alt text).
6. Remote-image dependency made unmistakable with a bold internal QA note.
