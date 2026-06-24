# -*- coding: utf-8 -*-
"""Page content + assembly. Run: python3 pages.py"""
from build import (head, header, footer, cta_band, faq_block, related_block,
                   write, img_ph, photo, asset_src, SITE)

P = SITE["phoneHref"]; PD = SITE["phoneDisplay"]

# ================= HOMEPAGE =================
def build_home():
    b = head("Sharpe's Septic Tank & Well Drilling Service | Septic & Well Services in the Midlands Since 1966",
             "Sharpe's Septic Tank & Well Drilling Service has served the Midlands since 1966 with septic pumping, repairs, installation, inspections, well drilling, grease interceptors, and precast tanks. Call (803) 755-1615.")
    b += header("index.html")
    b += '  <main id="main">\n'

    # 1. HERO
    b += f"""  <!-- ============ HERO (CMS: hero_headline, hero_copy, hero_image, CTAs) ============ -->
  <section class="hero">
    <div class="container">
      <div>
        <p class="eyebrow">Family owned &amp; operated since {SITE['since']}</p>
        <h1>Trusted Septic &amp; Well Services for the Midlands</h1>
        <p>From routine septic pumping and repairs to well drilling, inspections, grease interceptors, and precast tanks, Sharpe's helps homeowners and businesses across Columbia, Gaston, Lexington, and the surrounding Midlands get dependable service from a local team that has served the area since {SITE['since']}.</p>
        <div class="hero-actions">
          <a class="btn btn--primary btn--lg" href="contact.html" data-track="request_estimate_click">Schedule Service</a>
          <a class="btn btn--ghost btn--lg" href="{P}" data-track="phone_click">Call Sharpe's</a>
        </div>
        <div class="hero-badges">
          <div><strong>50+ yrs</strong>serving the Midlands</div>
          <div><strong>Licensed</strong>&amp; insured SC contractor</div>
          <div><strong>Septic + Well</strong>under one local team</div>
        </div>
        <!-- OPEN ITEM: "Voted Lexington's Best" badge + text are from the current live site. Confirm award badge and exact award wording before launch. If unsupported, keep the text trust signal and remove the badge image from prominent placement until confirmed. -->
        <p class="hero-award"><img src="{asset_src('bestoflex')}" alt="Voted Lexington's Best 2025 award badge" loading="lazy" decoding="async" referrerpolicy="no-referrer"><span>Voted Lexington's Best four years in a row</span></p>
      </div>
      <div class="hero-media">{photo("home_banner", eager=True)}</div>
    </div>
  </section>
"""

    # 2. SERVICE PATHWAY CARDS
    cards = [
        ("🚿", "Septic Services", "Pumping, repairs, replacement, installation, and inspections for residential and commercial systems.", "septic-services.html"),
        ("💧", "Well Drilling", "New well installation, repair and maintenance, and well inspections across the Midlands.", "well-drilling.html"),
        ("🛢️", "Grease Interceptors", "Installation, pumping, and inspections for restaurants and commercial kitchens.", "grease-interceptors.html"),
        ("🧱", "Precast Tanks", "Quality precast septic and water tanks for new installs and replacements.", "precast-tanks.html"),
    ]
    cards_html = ""
    for ico, title, desc, href in cards:
        cards_html += f"""        <a class="card card--link" href="{href}" data-track="service_card_click">
          <span class="card-icon" aria-hidden="true">{ico}</span>
          <h3>{title}</h3>
          <p>{desc}</p>
          <span class="card-link">Explore {title}</span>
        </a>
"""
    b += f"""  <!-- ============ SERVICE PATHWAY CARDS ============ -->
  <section class="section">
    <div class="container">
      <div class="center"><p class="eyebrow">What we do</p><h2>Pick the service that fits your property</h2></div>
      <div class="grid grid-4" style="margin-top:40px">
{cards_html}      </div>
    </div>
  </section>
"""

    # 3. NOT SURE WHAT SERVICE
    b += f"""  <!-- ============ "NOT SURE WHAT SERVICE" CONTEXT ============ -->
  <section class="section section--alt">
    <div class="container">
      <div class="split">
        <div>
          <p class="eyebrow">Not sure what you need?</p>
          <h2>Tell us the symptom — we'll point you to the fix</h2>
          <p class="lead">Slow drains, soggy spots in the yard, sewage odor, a gurgling toilet, or low water pressure can all trace back to your septic system or well. You don't have to diagnose it yourself — tell us what you're noticing and we'll point you to the right service, no pressure and no guesswork.</p>
          <ul class="checklist">
            <li>Slow drains or backups in the house</li>
            <li>Standing water or odor near the drain field</li>
            <li>Low water pressure or dirty water from a well</li>
            <li>Buying or selling a property and need an inspection</li>
            <li>Opening a kitchen and need a grease interceptor</li>
          </ul>
          <div class="hero-actions">
            <a class="btn btn--primary" href="contact.html" data-track="contact_form_start">Get help choosing</a>
            <a class="btn btn--secondary" href="{P}" data-track="phone_click">Call {PD}</a>
          </div>
        </div>
        <div>{photo("about_trust", alt="A Sharpe's technician working on septic service equipment in the field")}</div>
      </div>
    </div>
  </section>
"""

    # 4. TRUST BAR
    b += """  <!-- ============ TRUST BAR (CMS: trust items) ============ -->
  <section class="trust-bar">
    <div class="container">
      <div class="trust-item"><span class="ti-ico" aria-hidden="true">🏠</span><div><strong>Locally owned</strong><span>Rooted in the Midlands</span></div></div>
      <div class="trust-item"><span class="ti-ico" aria-hidden="true">📅</span><div><strong>Since 1966</strong><span>Decades of experience</span></div></div>
      <div class="trust-item"><span class="ti-ico" aria-hidden="true">✅</span><div><strong>Licensed &amp; insured</strong><span>SC septic &amp; well contractor</span></div></div>
      <div class="trust-item"><span class="ti-ico" aria-hidden="true">🚚</span><div><strong>Septic + well</strong><span>One trusted local team</span></div></div>
    </div>
  </section>
"""

    # 5. FEATURED SERVICES
    feat = [
        ("Septic Pumping", "Regular pumping keeps your system healthy and prevents costly backups. We handle residential and commercial tanks.", "septic-pumping.html", "View Septic Pumping"),
        ("Septic Inspections", "Buying, selling, or maintaining a property? Get a clear, documented inspection of your system.", "septic-inspections.html", "View Septic Inspections"),
        ("Well Drilling & Service", "New well installation, repairs, and inspections to keep your water flowing clean and steady.", "well-drilling.html", "View Well Services"),
    ]
    feat_html = ""
    for title, desc, href, label in feat:
        feat_html += f"""        <div class="card">
          <h3>{title}</h3>
          <p>{desc}</p>
          <a class="card-link" href="{href}" data-track="service_card_click">{label}</a>
        </div>
"""
    b += f"""  <!-- ============ FEATURED SERVICES ============ -->
  <section class="section">
    <div class="container">
      <div class="center"><p class="eyebrow">Most requested</p><h2>Featured services</h2></div>
      <div class="grid grid-3" style="margin-top:40px">
{feat_html}      </div>
    </div>
  </section>
"""

    # 6. CONDITIONAL SERVICETITAN BLOCK
    b += f"""  <!-- ============ CONDITIONAL: SERVICETITAN CONVENIENCE BLOCK ============
       Hidden until serviceTitanBookingUrl is supplied (see assets/main.js). -->
  <section class="section section--tight" data-module data-url="" hidden>
    <div class="container">
      <div class="module-st split">
        <div>
          <p class="eyebrow">Book online</p>
          <h2>Schedule your service in a few taps</h2>
          <p class="lead">Pick a time that works for you and we'll confirm your appointment. Manage your service right from your phone.</p>
          <a class="btn btn--primary btn--lg" data-module-link href="#" data-track="book_now_click">Book Now</a>
        </div>
        <div>{img_ph("Customer booking service on a phone")}</div>
      </div>
    </div>
  </section>
"""

    # 7. TESTIMONIALS
    # Testimonials below are pulled from the current live Sharpe's site / confirmed project materials.
    tess = [
        ("I have used Sharpe's two times in the last 10 years for septic service. Both times they were on time, did not leave any mess at all, and were very friendly. I thought the price was also reasonable. I would definitely use them again.", "Patrick H.", ""),
        ("Great people know their business. They dug a well and cleaned out my tank. Can't say enough good things about them.", "Blair C.", ""),
        ("Very quick and very helpful.", "Christina M.", ""),
    ]
    tess_html = ""
    for quote, who, where in tess:
        tess_html += f"""        <div class="testimonial">
          <div class="stars" aria-label="5 out of 5 stars">★★★★★</div>
          <blockquote>&ldquo;{quote}&rdquo;</blockquote>
          <p class="who">{who}{('<span>'+where+'</span>') if where else ''}</p>
        </div>
"""
    b += f"""  <!-- ============ TESTIMONIALS (CMS: testimonials) ============ -->
  <section class="section section--alt">
    <div class="container">
      <div class="center"><p class="eyebrow">What customers say</p><h2>Trusted by Midlands homeowners &amp; businesses</h2></div>
      <div class="grid grid-3" style="margin-top:40px">
{tess_html}      </div>
      <div class="center" style="margin-top:32px">
        <a class="btn btn--secondary" href="reviews.html" data-track="review_click">Read more reviews</a>
      </div>
    </div>
  </section>
"""

    # 8. THREE-STEP PROCESS
    steps = [
        ("Reach out", "Call us or send a service request. Tell us what's going on and where you're located."),
        ("We assess", "A Sharpe's technician evaluates your septic system or well and explains your options clearly."),
        ("We get it done", "We complete the work professionally and leave you with a system you can count on."),
    ]
    steps_html = ""
    for i, (t, d) in enumerate(steps, 1):
        steps_html += f"""        <div class="step">
          <div class="step-num" aria-hidden="true">{i}</div>
          <h3>{t}</h3>
          <p>{d}</p>
        </div>
"""
    b += f"""  <!-- ============ THREE-STEP PROCESS ============ -->
  <section class="section">
    <div class="container">
      <div class="center"><p class="eyebrow">How it works</p><h2>Service in three simple steps</h2></div>
      <div class="grid grid-3" style="margin-top:40px">
{steps_html}      </div>
    </div>
  </section>
"""

    # 9. OPTIONAL SOCIAL FEED PLACEHOLDER
    b += """  <!-- ============ CONDITIONAL: SOCIAL FEED (placeholder, hidden by default) ============ -->
  <section class="section section--tight" data-module data-enabled="false" hidden>
    <div class="container center">
      <p class="eyebrow">Follow along</p>
      <h2>From our social feed</h2>
      <div class="social-feed-ph" style="margin-top:24px" data-track="social_feed_click">Sharpe&#39;s social feed will appear here once connected.</div>
    </div>
  </section>
"""

    b += cta_band()
    b += "  </main>\n"
    b += footer()
    write("index.html", b)

# ================= REUSABLE SERVICE PAGE TEMPLATE =================
def build_service(page):
    """page is a dict describing one service page."""
    b = head(page["title"], page["desc"])
    b += header(page["active"])
    b += '  <main id="main">\n'

    # breadcrumb + hero
    crumbs = "".join(f'<li><a href="{href}">{lbl}</a></li>' for lbl, href in page["crumbs"])
    crumbs += f"<li>{page['h1']}</li>"
    b += f"""  <!-- ============ HERO ============ -->
  <section class="hero hero--sub">
    <div class="container">
      <nav class="breadcrumb" aria-label="Breadcrumb"><ol><li><a href="index.html">Home</a></li>{crumbs}</ol></nav>
      <p class="eyebrow">{page['eyebrow']}</p>
      <h1>{page['h1']}</h1>
      <p>{page['hero_copy']}</p>
      <div class="hero-actions">
        <a class="btn btn--primary btn--lg" href="contact.html?service={page['service_param']}" data-track="{page['cta_track']}">{page['cta_label']}</a>
        <a class="btn btn--ghost btn--lg" href="{P}" data-track="phone_click">Call {PD}</a>
      </div>
    </div>
  </section>
"""

    # context / problem section
    ctx = page["context"]
    list_html = "".join(f"<li>{x}</li>" for x in ctx["points"])
    # Use a real current-site image when this page has a matching asset key; otherwise
    # fall back to a clearly-labeled placeholder for the upcoming photography shoot.
    media_html = photo(page["photo_key"], alt=page.get("photo_alt")) if page.get("photo_key") else img_ph(page["photo"])
    b += f"""  <!-- ============ PROBLEM / CONTEXT ============ -->
  <section class="section">
    <div class="container">
      <div class="split">
        <div>
          <p class="eyebrow">{ctx['eyebrow']}</p>
          <h2>{ctx['title']}</h2>
          <p class="lead">{ctx['body']}</p>
          <ul class="checklist">{list_html}</ul>
        </div>
        <div>{media_html}</div>
      </div>
    </div>
  </section>
"""

    # direct-answer section (SEO / GEO / AI visibility) — concise Q&A in plain text
    if page.get("direct_answer"):
        da_html = ""
        for q, a in page["direct_answer"]:
            da_html += f'        <div style="margin-top:18px"><h2 style="font-size:1.3rem;margin-bottom:8px">{q}</h2><p class="lead" style="margin:0">{a}</p></div>\n'
        b += f"""  <!-- ============ DIRECT ANSWER ============ -->
  <section class="section section--tight">
    <div class="container" style="max-width:840px">
      <p class="eyebrow">Quick answer</p>
{da_html}    </div>
  </section>
"""

    # cards / details
    if page.get("cards"):
        cards_html = ""
        for c in page["cards"]:
            link = f'<a class="card-link" href="{c[2]}" data-track="service_card_click">View {c[0]}</a>' if len(c) > 2 and c[2] else ""
            cards_html += f"""        <div class="card"><h3>{c[0]}</h3><p>{c[1]}</p>{link}</div>
"""
        b += f"""  <!-- ============ SERVICE CARDS / DETAILS ============ -->
  <section class="section section--alt">
    <div class="container">
      <div class="center"><p class="eyebrow">{page.get('cards_eyebrow','What we offer')}</p><h2>{page.get('cards_title','Our services')}</h2></div>
      <div class="grid grid-{page.get('cards_cols',3)}" style="margin-top:40px">
{cards_html}      </div>
    </div>
  </section>
"""

    # signs / use cases
    if page.get("signs"):
        signs_html = "".join(f"<li>{s}</li>" for s in page["signs"]["items"])
        b += f"""  <!-- ============ SIGNS / USE CASES ============ -->
  <section class="section">
    <div class="container">
      <div class="center" style="max-width:760px;margin:0 auto"><p class="eyebrow">When to call</p><h2>{page['signs']['title']}</h2></div>
      <ul class="checklist" style="max-width:760px;margin:32px auto 0;columns:2;column-gap:48px">{signs_html}</ul>
    </div>
  </section>
"""

    # process steps
    if page.get("steps"):
        steps_html = ""
        for i, (t, d) in enumerate(page["steps"], 1):
            steps_html += f"""        <div class="step"><div class="step-num" aria-hidden="true">{i}</div><h3>{t}</h3><p>{d}</p></div>
"""
        b += f"""  <!-- ============ PROCESS STEPS ============ -->
  <section class="section section--alt">
    <div class="container">
      <div class="center"><p class="eyebrow">How it works</p><h2>What to expect</h2></div>
      <div class="grid grid-{len(page['steps'])}" style="margin-top:40px">
{steps_html}      </div>
    </div>
  </section>
"""

    # trust / proof strip
    b += """  <!-- ============ TRUST / PROOF ============ -->
  <section class="trust-bar">
    <div class="container">
      <div class="trust-item"><span class="ti-ico" aria-hidden="true">📅</span><div><strong>Since 1966</strong><span>Decades of local experience</span></div></div>
      <div class="trust-item"><span class="ti-ico" aria-hidden="true">✅</span><div><strong>Licensed &amp; insured</strong><span>SC contractor</span></div></div>
      <div class="trust-item"><span class="ti-ico" aria-hidden="true">🤝</span><div><strong>Straightforward</strong><span>Clear options, no surprises</span></div></div>
      <div class="trust-item"><span class="ti-ico" aria-hidden="true">⭐</span><div><strong>Locally trusted</strong><span>Homeowners &amp; businesses</span></div></div>
    </div>
  </section>
"""

    # FAQ
    if page.get("faqs"):
        b += faq_block(page.get("faq_title", "Frequently asked questions"), page["faqs"])

    # related
    if page.get("related"):
        b += related_block(page["related"])

    b += cta_band(page.get("cta_headline", "Ready to get started?"),
                  page.get("cta_sub", "Call now or send a service request and a local Sharpe's team member will help."))
    b += "  </main>\n"
    b += footer()
    write(page["file"], b)


if __name__ == "__main__":
    build_home()
    import service_content
    for pg in service_content.PAGES:
        build_service(pg)
    import other_pages
    other_pages.build_all()
    print("DONE")
