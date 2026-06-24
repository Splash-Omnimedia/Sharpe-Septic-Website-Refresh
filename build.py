# -*- coding: utf-8 -*-
"""
Static-site generator for the Sharpe's Septic refresh prototype.
Run:  python3 build.py
Outputs all .html pages into this folder, sharing one header/footer/CSS/JS.

CMS NOTE for Splash's team:
  - Real, confirmed business facts (name, phone, address) are rendered inline.
  - Conditional/configurable URLs use {{placeholder}} tokens so the matching
    module stays hidden until a real value is supplied (see assets/main.js).
  - Editable content regions are wrapped in <!-- CMS: field_name --> comments.
"""
import os, html

OUT = os.path.dirname(os.path.abspath(__file__))

# ---------------- Business constants (CMS-editable) ----------------
SITE = {
    "siteName": "Sharpe's Septic",
    "siteNameFull": "Sharpe's Septic Tank &amp; Well Drilling Service",
    "legalBusinessName": "Sharpe's Septic Tank &amp; Well Drilling Service, LLC",
    "phoneDisplay": "(803) 755-1615",
    "phoneHref": "tel:+18037551615",
    "address": "3660 Fish Hatchery Road, Gaston, SC 29503",
    "serviceArea": "the Midlands of South Carolina",
    "since": "1966",
    # Conditional URLs — left as tokens so modules stay OFF until confirmed
    "serviceTitanBookingUrl": "{{serviceTitanBookingUrl}}",
    "customerPortalUrl": "{{customerPortalUrl}}",
    "financingUrl": "{{financingUrl}}",
    "contactFormEndpoint": "{{contactFormEndpoint}}",
    "socialFeedEmbed": "{{socialFeedEmbed}}",
    # Real logo asset pulled from the current live site (already includes "LLC").
    "logoUrl": "https://www.sharpessepticandwelldrilling.com/wp-content/uploads/2025/08/Sharpes-add-LLC.png",
    "logoLocal": "assets/images/sharpes-logo-current.png",
    "logoAlt": "Sharpe's Septic Tank &amp; Well Drilling Service, LLC",
}

# ---------------- Image asset registry ----------------
# All imagery below is pulled from the CURRENT live Sharpe's site so the prototype
# is grounded in the real company. Each entry has both the live-CDN URL (so the
# prototype renders immediately for review) and a descriptive LOCAL filename for
# when Splash downloads the assets into assets/images/ (see assets/images/manifest.json
# and assets/images/download-assets.sh).
#
# Flip USE_REMOTE_ASSETS to False after running the download script to serve images
# locally instead of from the live CDN.
#
# NOTE: every photo emitted via photo() carries a "Temporary current-site image"
# comment — these are stand-ins until the approved full-day photography shoot.
USE_REMOTE_ASSETS = True

_CDN = "https://www.sharpessepticandwelldrilling.com/wp-content/uploads/2019/07"
ASSETS = {
    "home_banner":      {"url": _CDN + "/banner-home.jpg",      "file": "sharpes-home-banner.jpg",      "alt": "Sharpe's Septic Tank &amp; Well Drilling crew and equipment on a Midlands job site"},
    "about_trust":      {"url": "https://www.sharpessepticandwelldrilling.com/wp-content/themes/splashomnimediatheme/images/img-004.jpg", "file": "sharpes-about-trust.jpg", "alt": "Sharpe's Septic and Well technicians at work in the field"},
    "septic_team":      {"url": _CDN + "/child-header1.jpg",    "file": "sharpes-septic-team.jpg",      "alt": "Sharpe's Septic Tank and Well Drilling service team on site"},
    "well_frontyard":   {"url": _CDN + "/child-header-3.jpg",   "file": "sharpes-well-frontyard.jpg",   "alt": "Front-yard excavation for a Sharpe's well drilling project"},
    "well_tools":       {"url": _CDN + "/tools-closeup.jpg",    "file": "sharpes-well-tools.jpg",       "alt": "Close-up of well drilling and service tools used by the Sharpe's crew"},
    "grease_digging":   {"url": _CDN + "/child-header-2.jpg",   "file": "sharpes-grease-digging.jpg",   "alt": "Excavation work for a septic and grease interceptor installation"},
    "grease_backing":   {"url": _CDN + "/backing-up.jpg",       "file": "sharpes-grease-backing-up.jpg","alt": "Sharpe's service truck positioned for a commercial grease interceptor job"},
    "precast_frontyard":{"url": _CDN + "/child-header-4.jpg",   "file": "sharpes-precast-frontyard.jpg","alt": "Job site where a precast septic tank is being set in the front yard"},
    "bestoflex":        {"url": "https://www.sharpessepticandwelldrilling.com/wp-content/uploads/2025/06/BestofLex_Logo2025-1.png", "file": "bestoflex-2025.png", "alt": "Voted Lexington's Best 2025 award badge"},
}

def asset_src(key):
    a = ASSETS[key]
    return a["url"] if USE_REMOTE_ASSETS else (SITE["logoLocal"].rsplit("/",1)[0] + "/" + a["file"])

def logo_src():
    return SITE["logoUrl"] if USE_REMOTE_ASSETS else SITE["logoLocal"]

# ---------------- Navigation model (current Sharpe's sitemap) ----------------
NAV = [
    ("Home", "index.html", []),
    ("Septic Services", "septic-services.html", [
        ("Septic Installation", "septic-installation.html"),
        ("Septic Repairs &amp; Replacement", "septic-repairs-replacement.html"),
        ("Septic Pumping", "septic-pumping.html"),
        ("Septic Inspections", "septic-inspections.html"),
    ]),
    ("Well Drilling", "well-drilling.html", [
        ("Well Installation", "well-installation.html"),
        ("Well Repair &amp; Maintenance", "well-repair-maintenance.html"),
        ("Well Inspections", "well-inspections.html"),
    ]),
    ("Grease Interceptors", "grease-interceptors.html", [
        ("Grease Interceptor Installation", "grease-interceptor-installation.html"),
        ("Grease Interceptor Pumping &amp; Inspections", "grease-interceptor-pumping-inspections.html"),
    ]),
    ("Precast Tanks", "precast-tanks.html", []),
    ("Resources", "faqs.html", [
        ("FAQs", "faqs.html"),
        ("Associations &amp; Licensing", "associations-licensing.html"),
    ]),
    ("Why Sharpe's", "why-sharpes.html", [
        ("Our Reviews", "reviews.html"),
        ("Review Us", "review-us.html"),
    ]),
    ("Contact", "contact.html", []),
]

# ---------------- Reusable HTML partials ----------------
def head(title, desc):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Lato:wght@400;700;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="assets/styles.css">
  <script type="application/ld+json">
  {{"@context":"https://schema.org","@type":"LocalBusiness","name":"Sharpe's Septic Tank & Well Drilling Service, LLC","telephone":"+1-803-755-1615","address":{{"@type":"PostalAddress","streetAddress":"3660 Fish Hatchery Road","addressLocality":"Gaston","addressRegion":"SC","postalCode":"29503","addressCountry":"US"}},"areaServed":"Midlands of South Carolina","url":"https://www.sharpessepticandwelldrilling.com/","foundingDate":"1966"}}
  </script>
</head>
<body>
  <a class="skip-link" href="#main">Skip to main content</a>
"""

def nav_markup(active):
    items = []
    for label, link, subs in NAV:
        is_active = (link == active) or any(s[1] == active for s in subs)
        if subs:
            sub_html = "".join(
                f'<li><a href="{s[1]}">{s[0]}</a></li>' for s in subs
            )
            btn_cls = ' class="active"' if is_active else ''
            items.append(f"""        <li class="has-sub" aria-expanded="false">
          <button{btn_cls} aria-haspopup="true" aria-expanded="false">{label}</button>
          <ul class="submenu" aria-label="{html.unescape(label)} submenu">
            <li><a href="{link}"><strong>All {html.unescape(label)}</strong></a></li>
            {sub_html}
          </ul>
        </li>""")
        else:
            aria = ' aria-current="page"' if is_active else ""
            items.append(f'        <li><a href="{link}"{aria}>{label}</a></li>')
    return "\n".join(items)

def header(active):
    return f"""  <!-- Utility bar: phone + service area -->
  <div class="utility-bar">
    <div class="container">
      <div class="util-left">
        <span class="util-item">📍 Serving {SITE['serviceArea']}</span>
        <span class="util-item">🕑 Family owned since {SITE['since']}</span>
      </div>
      <div class="util-left">
        <a class="util-item" href="{SITE['phoneHref']}" data-track="phone_click">📞 {SITE['phoneDisplay']}</a>
        <!-- Customer Portal — add the real portal URL to data-url and href when available (see README). -->
        <a class="util-item" data-module data-module-link data-url=""
           href="#" data-track="customer_portal_click" hidden>🔐 Customer Portal</a>
      </div>
    </div>
  </div>

  <!-- ============ HEADER / MAIN NAV ============ -->
  <header class="site-header">
    <div class="container">
      <!-- Sharpe's logo (already includes LLC). -->
      <a class="brand-logo" href="index.html" aria-label="{html.unescape(SITE['siteNameFull'])} home">
        <img class="brand-logo-img" src="{logo_src()}" alt="{SITE['logoAlt']}" width="240" height="60" referrerpolicy="no-referrer">
      </a>

      <nav class="main-nav" aria-label="Primary">
        <ul>
{nav_markup(active)}
        </ul>
      </nav>

      <div class="header-cta">
        <a class="nav-phone" href="{SITE['phoneHref']}" data-track="phone_click">
          <span class="nav-phone-ico">📞</span>
          <span class="nav-phone-text"><small>Call us today</small><strong>{SITE['phoneDisplay']}</strong></span>
        </a>
        <!-- Primary CTA routes to Contact by default; swap href to serviceTitanBookingUrl when ServiceTitan is live -->
        <a class="btn btn--primary" href="contact.html" data-track="request_estimate_click">Schedule Service</a>
      </div>

      <button class="nav-toggle" aria-label="Open menu" aria-expanded="false" aria-controls="primary-nav">
        <span></span>
      </button>
    </div>
  </header>
"""

def footer():
    cols_services = """
        <h4>Services</h4>
        <ul>
          <li><a href="septic-services.html">Septic Services</a></li>
          <li><a href="septic-pumping.html">Septic Pumping</a></li>
          <li><a href="septic-inspections.html">Septic Inspections</a></li>
          <li><a href="well-drilling.html">Well Drilling</a></li>
          <li><a href="grease-interceptors.html">Grease Interceptors</a></li>
          <li><a href="precast-tanks.html">Precast Tanks</a></li>
        </ul>"""
    cols_company = """
        <h4>Company</h4>
        <ul>
          <li><a href="why-sharpes.html">Why Sharpe's</a></li>
          <li><a href="reviews.html">Our Reviews</a></li>
          <li><a href="review-us.html">Review Us</a></li>
          <li><a href="faqs.html">FAQs</a></li>
          <li><a href="associations-licensing.html">Associations &amp; Licensing</a></li>
          <li><a href="contact.html">Contact</a></li>
        </ul>"""
    return f"""  <!-- Footer -->
  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <!-- Sharpe's logo (already includes LLC). -->
          <a class="brand-logo" href="index.html" aria-label="{html.unescape(SITE['siteNameFull'])} home">
            <img class="brand-logo-img" src="{logo_src()}" alt="{SITE['logoAlt']}" width="240" height="60" referrerpolicy="no-referrer">
          </a>
          <p style="margin-top:16px;color:#c4d5e3">Dependable septic and well services for homeowners and businesses across {SITE['serviceArea']} since {SITE['since']}.</p>
          <div class="footer-contact-item">📞 <a href="{SITE['phoneHref']}" data-track="phone_click">{SITE['phoneDisplay']}</a></div>
          <div class="footer-contact-item">📍 <span>{SITE['address']}</span></div>
        </div>
        <div>{cols_services}</div>
        <div>{cols_company}</div>
        <div>
          <h4>Get Service</h4>
          <p style="color:#c4d5e3">Tell us what you need and we'll get back to you quickly.</p>
          <a class="btn btn--primary" href="contact.html" data-track="request_estimate_click" style="margin-bottom:12px">Schedule Service</a>
          <!-- CONDITIONAL: Social feed — placeholder only until embed is provided -->
          <div data-module data-enabled="false" data-track="social_feed_click" hidden>
            <h4 style="margin-top:20px">Follow Sharpe's</h4>
            <div class="social-feed-ph">Sharpe&#39;s social feed will appear here once connected.</div>
          </div>
        </div>
      </div>
      <div class="footer-bottom">
        <span>&copy; <span data-year>2026</span> {SITE['legalBusinessName']}. All rights reserved.</span>
        <span class="licensing-line">Licensed · Bonded · Insured · DHEC</span>
      </div>
    </div>
  </footer>

  <!-- ============ STICKY MOBILE CALL / BOOK BAR ============ -->
  <div class="mobile-callbar" aria-hidden="false">
    <a class="mc-call" href="{SITE['phoneHref']}" data-track="phone_click">📞 Call</a>
    <a class="mc-book" href="contact.html" data-track="request_estimate_click">Schedule Service</a>
  </div>

  <!-- ============ CONDITIONAL: PROMO POPUP (disabled by default) ============ -->
  <div class="promo-popup" data-enabled="false" data-delay="6000" role="dialog" aria-modal="true" aria-label="Promotion">
    <div class="promo-card">
      <button class="promo-close" aria-label="Close" data-track="promo_popup_close">&times;</button>
      <p class="eyebrow">Sharpe&#39;s Septic &amp; Well</p>
      <h3>Need septic or well service?</h3>
      <p>Call our local team and we&#39;ll help you find the right next step.</p>
      <a class="btn btn--primary" href="contact.html">Schedule Service</a>
    </div>
  </div>

  <script src="assets/main.js"></script>
</body>
</html>"""

def cta_band(headline="Need septic or well service in the Midlands?",
             sub="Call now or send a service request and a local Sharpe's team member will help you figure out the right next step."):
    return f"""  <!-- ============ FINAL CTA ============ -->
  <section class="cta-band">
    <div class="container">
      <div>
        <h2>{headline}</h2>
        <p>{sub}</p>
      </div>
      <div class="hero-actions" style="display:flex;gap:16px;flex-wrap:wrap">
        <a class="btn btn--primary btn--lg" href="contact.html" data-track="request_estimate_click">Schedule Service</a>
        <a class="btn btn--ghost btn--lg" href="{SITE['phoneHref']}" data-track="phone_click">Call {SITE['phoneDisplay']}</a>
      </div>
    </div>
  </section>
"""

def faq_block(title, items, intro=""):
    rows = ""
    for q, a in items:
        rows += f"""      <details class="faq-item">
        <summary>{q}</summary>
        <div class="faq-body"><p>{a}</p></div>
      </details>
"""
    intro_html = f'<p class="lead center" style="margin:0 auto 32px">{intro}</p>' if intro else ""
    return f"""  <!-- ============ FAQ ACCORDION ============ -->
  <section class="section section--alt">
    <div class="container">
      <div class="center"><p class="eyebrow">Questions &amp; Answers</p><h2>{title}</h2>{intro_html}</div>
      <div class="faq">
{rows}      </div>
    </div>
  </section>
"""

def related_block(links):
    items = ""
    for label, href in links:
        items += f'        <a href="{href}" data-track="service_card_click">{label}</a>\n'
    return f"""  <!-- ============ RELATED SERVICES ============ -->
  <section class="section section--tight">
    <div class="container">
      <h2 class="center">Related Services</h2>
      <div class="related-grid">
{items}      </div>
    </div>
  </section>
"""

import re as _re
# ---------------- Custom inline SVG icon set ----------------
# Replaces all emoji sitewide with consistent, brand-colored line icons
# (filled for stars). Icons inherit color via currentColor and are sized by CSS
# (.ico and its context selectors in assets/styles.css). Applied in write().
_ICON_PATHS = {
 "pin": '<path d="M12 21s-6-5.3-6-10a6 6 0 1 1 12 0c0 4.7-6 10-6 10Z"/><circle cx="12" cy="11" r="2.1"/>',
 "clock": '<circle cx="12" cy="12" r="8.5"/><path d="M12 7.5V12l3 1.8"/>',
 "phone": '<path d="M6.6 4.2 9.4 4l1.4 3.7-1.9 1.4a10.6 10.6 0 0 0 4.6 4.6l1.4-1.9 3.7 1.4-.2 2.8a1.7 1.7 0 0 1-1.8 1.6A14.5 14.5 0 0 1 5.2 6.1a1.7 1.7 0 0 1 1.4-1.9Z"/>',
 "lock": '<rect x="5" y="10.5" width="14" height="9" rx="2"/><path d="M8 10.5V8a4 4 0 0 1 8 0v2.5"/>',
 "map": '<path d="M9 4 3.5 6.2v13.3L9 17.3l6 2.2 5.5-2.2V4.2L15 6.4 9 4Z"/><path d="M9 4v13.3M15 6.4v13.1"/>',
 "home": '<path d="M4 11.3 12 5l8 6.3"/><path d="M6 10v9.5h12V10"/><path d="M10 19.5V14h4v5.5"/>',
 "calendar": '<rect x="4" y="5.5" width="16" height="14" rx="2"/><path d="M4 9.5h16M8 3.5v4M16 3.5v4"/>',
 "shield": '<path d="M12 3.5 5 6v6c0 4.2 3 7 7 8.5 4-1.5 7-4.3 7-8.5V6l-7-2.5Z"/><path d="m9 12 2 2 4-4"/>',
 "truck": '<path d="M3 7h11v9.5H3z"/><path d="M14 10.5h3.8l3.2 3.2v2.8H14z"/><circle cx="7" cy="17.5" r="1.7"/><circle cx="17.3" cy="17.5" r="1.7"/>',
 "clarity": '<path d="M4 5.5h16v10H9.5L5.5 19v-3.5H4z"/><path d="m8.5 10.3 2 2 3.6-3.6"/>',
 "drop": '<path d="M12 3.4S6 9.8 6 14a6 6 0 0 0 12 0c0-4.2-6-10.6-6-10.6Z"/><path d="M9.6 14.2a2.4 2.4 0 0 0 2.4 2.3"/>',
 "tank": '<rect x="4" y="8" width="16" height="9" rx="2"/><path d="M4 11.5h16"/><path d="M8.5 8V6.4M15.5 8V6.4"/><path d="M7 17v1.8M17 17v1.8"/>',
 "barrel": '<rect x="6.5" y="4" width="11" height="16" rx="3"/><path d="M6.5 9h11M6.5 14.5h11"/>',
 "block": '<path d="m12 4 8 3v8.5l-8 3.5-8-3.5V7Z"/><path d="m4 7 8 3 8-3M12 10v8"/>',
 "star": '<path d="m12 3.6 2.6 5.2 5.8.9-4.2 4.1 1 5.7L12 16.9 6.8 19.5l1-5.7-4.2-4.1 5.8-.9Z"/>',
}
def _svg(name, fill=False):
    fillv = 'currentColor' if fill else 'none'
    return ('<svg class="ico" viewBox="0 0 24 24" fill="%s" stroke="currentColor" '
            'stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" '
            'aria-hidden="true" focusable="false">%s</svg>') % (fillv, _ICON_PATHS[name])

_EMOJI = {
 "\U0001F4CD": ("pin", 0), "\U0001F551": ("clock", 0), "\U0001F4DE": ("phone", 0),
 "\U0001F510": ("lock", 0), "\U0001F5FA": ("map", 0), "\U0001F3E0": ("home", 0),
 "\U0001F4C5": ("calendar", 0), "✅": ("shield", 0), "\U0001F69A": ("truck", 0),
 "\U0001F91D": ("clarity", 0), "\U0001F4A7": ("drop", 0), "\U0001F6BF": ("tank", 0),
 "\U0001F6E2": ("barrel", 0), "\U0001F9F1": ("block", 0),
 "⭐": ("star", 1), "★": ("star", 1),
}
def _icons(s):
    s = s.replace("️", "")   # drop emoji variation selectors
    for e, (name, fill) in _EMOJI.items():
        if e in s:
            s = s.replace(e, _svg(name, bool(fill)))
    return s

def _clean_comments(s):
    """Strip internal-only review language from generated HTML so the client
    preview reads clean. Removes OPEN ITEM/TODO comments, standalone CMS:
    comments, and inline (CMS: ...) annotations inside banner comments.
    Useful developer comments (e.g. the temporary-image note) are preserved."""
    s = _re.sub(r"[ \t]*<!--[^>]*?(OPEN ITEM|TODO)[^>]*?-->\n?", "", s)
    s = _re.sub(r"[ \t]*<!--\s*CMS:[^>]*?-->\n?", "", s)
    s = _re.sub(r"\s*\(CMS:[^)]*\)", "", s)
    return s

def write(filename, body):
    body = _clean_comments(body)
    body = _icons(body)
    with open(os.path.join(OUT, filename), "w", encoding="utf-8") as f:
        f.write(body)
    print("wrote", filename)

# Image placeholder helper — used only where no suitable real asset exists yet.
def img_ph(text):
    return f'<div class="img-ph" role="img" aria-label="Future photography placeholder: {text}"><span>Future Photography Placeholder: {text}</span></div>'

# Real-image helper. Emits a current-site image with descriptive alt text and a
# replace-after-shoot comment. `eager=True` for above-the-fold images (no lazy load).
def photo(key, eager=False, alt=None):
    a = ASSETS[key]
    alt_text = alt if alt is not None else a["alt"]
    loading = "" if eager else ' loading="lazy"'
    return ("<!-- Temporary current-site image. Replace after approved full-day photography shoot. -->\n        "
            f'<img class="media" src="{asset_src(key)}" alt="{alt_text}"{loading} decoding="async" referrerpolicy="no-referrer">')

print("Partials loaded.")
