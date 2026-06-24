# -*- coding: utf-8 -*-
"""Contact, FAQs, Associations & Licensing, Why Sharpe's, Reviews, Review Us."""
from build import (head, header, footer, cta_band, faq_block, related_block,
                   write, img_ph, photo, SITE)

P = SITE["phoneHref"]; PD = SITE["phoneDisplay"]

SERVICE_OPTIONS = [
    ("septic-pumping","Septic Pumping"),
    ("septic-inspection","Septic Inspection"),
    ("septic-repair","Septic Repair / Replacement"),
    ("septic-installation","Septic Installation"),
    ("well-installation","Well Installation"),
    ("well-repair","Well Repair / Maintenance"),
    ("well-inspection","Well Inspection"),
    ("grease-interceptor-installation","Grease Interceptor Installation"),
    ("grease-interceptor-pumping","Grease Interceptor Pumping / Inspection"),
    ("precast-tanks","Precast Tanks"),
    ("other","Other / Not Sure"),
]

def build_contact():
    b = head("Contact Sharpe's Septic | Schedule Service in the Midlands",
             "Contact Sharpe's Septic Tank & Well Drilling Service. Call (803) 755-1615 or send a service request for septic, well, grease interceptor, and precast tank service across the Midlands.")
    b += header("contact.html")
    b += '  <main id="main">\n'

    b += f"""  <!-- ============ HERO ============ -->
  <section class="hero hero--sub">
    <div class="container">
      <nav class="breadcrumb" aria-label="Breadcrumb"><ol><li><a href="index.html">Home</a></li><li>Contact</li></ol></nav>
      <p class="eyebrow">Get in touch</p>
      <h1>Schedule service or ask a question</h1>
      <p>Tell us what you need and a local Sharpe's team member will get back to you. Prefer to talk? Call us directly — we're happy to help you figure out the right service.</p>
      <div class="hero-actions">
        <a class="btn btn--primary btn--lg" href="{P}" data-track="phone_click">Call {PD}</a>
      </div>
    </div>
  </section>
"""

    options_html = '<option value="" selected disabled>Select a service…</option>\n'
    for val, label in SERVICE_OPTIONS:
        options_html += f'            <option value="{val}">{label}</option>\n'

    b += f"""  <!-- ============ CONTACT FORM + DETAILS ============ -->
  <section class="section">
    <div class="container">
      <div class="split">
        <!-- LEFT: form (CMS: routes to contactFormEndpoint) -->
        <div>
          <h2>Request service</h2>
          <p class="lead">Not sure which service to choose? Select &ldquo;Other / Not Sure&rdquo; and we'll help route your request.</p>
          <p class="hint">Fields marked <span style="color:var(--warn)">*</span> are required.</p>
          <div class="form-card">
            <p data-form-success tabindex="-1" hidden role="status" style="font-family:var(--font-head);font-weight:700;color:var(--ok);font-size:1.15rem">
              Thank you for contacting Sharpe&#39;s. Our team has received your request and will follow up to help you determine the next step.
            </p>
            <form data-contact-form action="" method="post" novalidate>
              <div class="form-row">
                <div class="field">
                  <label for="name">Name <span class="req" aria-hidden="true">*</span></label>
                  <input id="name" name="name" type="text" autocomplete="name" required aria-required="true" aria-describedby="name-err">
                  <span class="error-msg" id="name-err">Please enter your name.</span>
                </div>
                <div class="field">
                  <label for="phone">Phone <span class="req" aria-hidden="true">*</span></label>
                  <input id="phone" name="phone" type="tel" autocomplete="tel" required aria-required="true" aria-describedby="phone-err">
                  <span class="error-msg" id="phone-err">Please enter a phone number.</span>
                </div>
              </div>
              <div class="field">
                <label for="email">Email <span class="req" aria-hidden="true">*</span></label>
                <input id="email" name="email" type="email" autocomplete="email" required aria-required="true" aria-describedby="email-err">
                <span class="error-msg" id="email-err">Please enter a valid email address.</span>
              </div>
              <div class="form-row">
                <div class="field">
                  <label for="service-type">Service Type</label>
                  <select id="service-type" name="service" data-track="service_type_selection">
{options_html}          </select>
                  <span class="hint">Not sure? Choose "Other / Not Sure" and we'll help.</span>
                </div>
                <div class="field">
                  <label for="city">Property City / Location</label>
                  <input id="city" name="city" type="text" autocomplete="address-level2" placeholder="e.g. Lexington, SC">
                </div>
              </div>
              <div class="field">
                <label for="message">Message / Service Need</label>
                <textarea id="message" name="message" placeholder="Tell us what's going on — symptoms, timing, property details…"></textarea>
              </div>
              <button class="btn btn--primary btn--lg btn--block" type="submit" data-track="contact_form_submit">Send Service Request</button>
            </form>
          </div>
        </div>

        <!-- RIGHT: contact details + map placeholder -->
        <div>
          <h2>Reach Sharpe's directly</h2>
          <div class="card" style="margin-bottom:24px">
            <div class="footer-contact-item" style="color:var(--ink)">📞 <a href="{P}" data-track="phone_click"><strong>{PD}</strong></a></div>
            <div class="footer-contact-item" style="color:var(--ink)">📍 <span>{SITE['address']}</span></div>
            <div class="footer-contact-item" style="color:var(--ink)">🗺️ <span>Serving {SITE['serviceArea']}</span></div>
            <div class="footer-contact-item" style="color:var(--ink)">🕑 <span>Family owned &amp; operated since {SITE['since']}</span></div>
            <!-- Customer Portal — add the real portal URL to data-url and href when available (see README). -->
            <div data-module data-module-link data-url="" hidden>
              <a class="btn btn--secondary" href="#" data-track="customer_portal_click" style="margin-top:12px">Customer Portal Login</a>
            </div>
          </div>
          <div style="margin-bottom:24px">{photo("septic_team", alt="Sharpe's Septic Tank and Well Drilling team serving the Midlands")}</div>
          <!-- Map embed pending: replace with the live Google Maps embed for the service area / shop location. -->
          {img_ph("Map of Sharpe's service area in the Midlands")}
          <!-- CONDITIONAL: ServiceTitan online booking (hidden until URL provided) -->
          <div class="module-st" data-module data-url="" hidden style="margin-top:24px">
            <h3>Prefer to book online?</h3>
            <p>Pick a time that works for you.</p>
            <a class="btn btn--primary" data-module-link href="#" data-track="book_now_click">Book Now</a>
          </div>
        </div>
      </div>
    </div>
  </section>
  <!-- ============ WHAT HAPPENS NEXT ============ -->
  <section class="section section--alt">
    <div class="container">
      <div class="center"><p class="eyebrow">What happens next?</p><h2>After you send your request</h2></div>
      <div class="grid grid-3" style="margin-top:40px">
        <div class="step"><div class="step-num" aria-hidden="true">1</div><h3>We review your request</h3><p>A local Sharpe's team member reviews the details you send.</p></div>
        <div class="step"><div class="step-num" aria-hidden="true">2</div><h3>We follow up</h3><p>We reach out to confirm the right service for your property.</p></div>
        <div class="step"><div class="step-num" aria-hidden="true">3</div><h3>We help schedule</h3><p>We help you schedule the next step at a time that works for you.</p></div>
      </div>
    </div>
  </section>
"""
    b += "  </main>\n"
    b += footer()
    write("contact.html", b)


def build_faqs():
    b = head("Septic & Well FAQs | Sharpe's Septic",
             "Answers to common questions about septic systems, pumping, inspections, wells, grease interceptors, and precast tanks in the Midlands. Call (803) 755-1615.")
    b += header("faqs.html")
    b += '  <main id="main">\n'
    b += """  <section class="hero hero--sub">
    <div class="container">
      <nav class="breadcrumb" aria-label="Breadcrumb"><ol><li><a href="index.html">Home</a></li><li>Resources</li><li>FAQs</li></ol></nav>
      <p class="eyebrow">Resources</p>
      <h1>Frequently asked questions</h1>
      <p>Straightforward answers to the questions we hear most. Don't see yours? Give us a call.</p>
    </div>
  </section>
"""
    faqs = [
        ("How often should I pump my septic tank?","For most households, every 3–5 years, depending on tank size and usage. We can recommend a schedule for your property."),
        ("What are the signs my septic system needs repair?","Slow drains, sewage odors, gurgling plumbing, backups, and standing water or unusually green grass over the drain field. You don't have to diagnose it yourself — describe what you're seeing and we'll help."),
        ("Do you handle both residential and commercial work?","Yes. We serve homeowners and businesses across the Midlands, including restaurants with grease interceptors."),
        ("Do I need a septic inspection when buying or selling a home?","It's strongly recommended for any property on a septic system. An inspection gives buyers, sellers, and realtors a documented look at the system before closing, so there are no costly surprises."),
        ("Why did my water pressure drop?","It's often a pump or pressure system issue. We diagnose the specific cause and repair it."),
        ("How often should a grease interceptor be pumped?","It depends on your kitchen's volume and local requirements. We'll recommend a schedule that keeps you compliant."),
        ("What areas do you serve?","We serve Columbia, Gaston, Lexington, and the surrounding Midlands of South Carolina. Call us if you're unsure whether you're in our service area."),
        ("How long has Sharpe's been in business?","We've served the Midlands since 1966 as a family-owned septic and well company."),
        ("Do you install precast tanks?","Yes — we supply and install quality precast tanks for new systems and replacements."),
        ("What are the signs my well needs service?","Low or fluctuating water pressure, dirty or discolored water, sputtering faucets, unusual noises, or a pump that runs constantly. Call us and we'll diagnose the cause."),
        ("Do you help with grease interceptor pumping and inspections?","Yes. We install, pump, and inspect grease interceptors for restaurants and other commercial kitchens, and we can provide documentation to support compliance."),
        ("What happens after I request service?","We review your request, follow up to confirm the right service for your property, and help you schedule the next step."),
        ("How do I schedule service?","Call (803) 755-1615 or send a request through our Contact page and we'll get back to you quickly."),
    ]
    b += faq_block("Septic, well &amp; commercial FAQs", faqs)
    b += related_block([("Septic Services","septic-services.html"),("Well Drilling","well-drilling.html"),
                        ("Associations &amp; Licensing","associations-licensing.html"),("Contact Sharpe's","contact.html")])
    b += cta_band("Still have a question?","Call us and a local Sharpe's team member will be glad to help.")
    b += "  </main>\n"
    b += footer()
    write("faqs.html", b)


def build_associations():
    b = head("Associations & Licensing | Sharpe's Septic",
             "Sharpe's Septic Tank & Well Drilling Service is a licensed and insured South Carolina contractor. Learn about our credentials and associations.")
    b += header("associations-licensing.html")
    b += '  <main id="main">\n'
    b += """  <section class="hero hero--sub">
    <div class="container">
      <nav class="breadcrumb" aria-label="Breadcrumb"><ol><li><a href="index.html">Home</a></li><li>Resources</li><li>Associations &amp; Licensing</li></ol></nav>
      <p class="eyebrow">Resources</p>
      <h1>Associations &amp; licensing</h1>
      <p>Sharpe's is a licensed and insured South Carolina septic and well contractor. We hold our work to professional standards you can count on.</p>
    </div>
  </section>
  <section class="section">
    <div class="container">
      <div class="split">
        <div>
          <p class="eyebrow">Credentials</p>
          <h2>Licensed, insured &amp; experienced</h2>
          <p class="lead">Decades of local experience, backed by proper licensing and insurance, mean your project is handled the right way.</p>
          <ul class="checklist">
            <li>Licensed South Carolina septic &amp; well contractor</li>
            <li>Bonded and fully insured for your protection</li>
            <li>Work completed in accordance with South Carolina regulations</li>
            <li>Family owned and operated since 1966</li>
          </ul>
          <!-- CMS: add specific license number(s), bonding details, and association names/logos once confirmed. -->
        </div>
        <div>""" + img_ph("Sharpe's licensing, certifications, or association logos") + """</div>
      </div>
    </div>
  </section>
"""
    b += related_block([("FAQs","faqs.html"),("Why Sharpe's","why-sharpes.html"),("Contact Sharpe's","contact.html")])
    b += cta_band()
    b += "  </main>\n"
    b += footer()
    write("associations-licensing.html", b)


def build_why():
    b = head("Why Sharpe's | Local Septic & Well Experts Since 1966",
             "Why homeowners and businesses across the Midlands trust Sharpe's Septic Tank & Well Drilling Service. Family owned since 1966, licensed, insured, and practical.")
    b += header("why-sharpes.html")
    b += '  <main id="main">\n'
    b += f"""  <section class="hero hero--sub">
    <div class="container">
      <nav class="breadcrumb" aria-label="Breadcrumb"><ol><li><a href="index.html">Home</a></li><li>Why Sharpe's</li></ol></nav>
      <p class="eyebrow">Why Sharpe's</p>
      <h1>A local team the Midlands has trusted since 1966</h1>
      <p>You shouldn't have to guess what's wrong with your septic system or well. We're a local, family-owned company that explains your options in plain terms and has built its reputation, one honest job at a time, since 1966.</p>
    </div>
  </section>
  <section class="section">
    <div class="container">
      <div class="grid grid-3">
        <div class="card"><span class="card-icon" aria-hidden="true">🏠</span><h3>Local &amp; family owned</h3><p>Rooted in the Midlands and invested in our neighbors. When you call, you reach people who know the area.</p></div>
        <div class="card"><span class="card-icon" aria-hidden="true">📅</span><h3>Since 1966</h3><p>Decades of hands-on experience with septic systems and wells across all kinds of properties and conditions.</p></div>
        <div class="card"><span class="card-icon" aria-hidden="true">✅</span><h3>Licensed &amp; insured</h3><p>A properly licensed and insured South Carolina contractor, so your project is in capable hands.</p></div>
        <div class="card"><span class="card-icon" aria-hidden="true">🤝</span><h3>Straightforward</h3><p>We explain your options in plain terms and recommend what actually makes sense for your property.</p></div>
        <div class="card"><span class="card-icon" aria-hidden="true">🚚</span><h3>Septic + well in one</h3><p>From septic to well drilling to grease interceptors, you have one trusted local team for it all.</p></div>
        <div class="card"><span class="card-icon" aria-hidden="true">⭐</span><h3>Locally trusted</h3><p>Homeowners and businesses across the Midlands rely on us — read what they have to say.</p><a class="card-link" href="reviews.html" data-track="review_click">See reviews</a></div>
      </div>
    </div>
  </section>
"""
    b += related_block([("Our Reviews","reviews.html"),("Review Us","review-us.html"),
                        ("Associations &amp; Licensing","associations-licensing.html"),("Contact Sharpe's","contact.html")])
    b += cta_band()
    b += "  </main>\n"
    b += footer()
    write("why-sharpes.html", b)


def build_reviews():
    b = head("Our Reviews | Sharpe's Septic",
             "Read reviews from Midlands homeowners and businesses who trust Sharpe's Septic Tank & Well Drilling Service.")
    b += header("reviews.html")
    b += '  <main id="main">\n'
    b += """  <section class="hero hero--sub">
    <div class="container">
      <nav class="breadcrumb" aria-label="Breadcrumb"><ol><li><a href="index.html">Home</a></li><li>Why Sharpe's</li><li>Our Reviews</li></ol></nav>
      <p class="eyebrow">What customers say</p>
      <h1>Our reviews</h1>
      <p>Real feedback from the homeowners and businesses we serve across the Midlands.</p>
    </div>
  </section>
"""
    # Reviews below are pulled from the current live Sharpe's site / confirmed project materials.
    reviews = [
        ("I have used Sharpe's two times in the last 10 years for septic service. Both times they were on time, did not leave any mess at all, and were very friendly. I thought the price was also reasonable. I would definitely use them again.","Patrick H.",""),
        ("Very nice and friendly office staff. Very helpful.","Anonymous",""),
        ("Great people know their business. They dug a well and cleaned out my tank. Can't say enough good things about them.","Blair C.",""),
        ("Very quick and very helpful.","Christina M.",""),
        ("Great service!","Katherine D.",""),
        ("We needed our septic tank emptied out. They were quick to get us on the books, and very professional and quick in doing their job. Very friendly staff, and they explained everything they were doing.","Stephanie W.",""),
    ]
    cards = ""
    for q, who, where in reviews:
        cards += f"""        <div class="testimonial">
          <div class="stars" aria-label="5 out of 5 stars">★★★★★</div>
          <blockquote>&ldquo;{q}&rdquo;</blockquote>
          <p class="who">{who}{('<span>'+where+'</span>') if where else ''}</p>
        </div>
"""
    b += f"""  <section class="section section--alt">
    <div class="container">
      <div class="grid grid-3">
{cards}      </div>
      <!-- CMS: connect live reviews from Google or your review platform here. -->
      <div class="center"><a class="btn btn--primary" href="review-us.html" data-track="review_click">Leave us a review</a></div>
    </div>
  </section>
"""
    b += cta_band()
    b += "  </main>\n"
    b += footer()
    write("reviews.html", b)


def build_review_us():
    b = head("Review Us | Sharpe's Septic",
             "Had a good experience with Sharpe's Septic Tank & Well Drilling Service? Leave us a review — it helps your Midlands neighbors find dependable service.")
    b += header("review-us.html")
    b += '  <main id="main">\n'
    b += """  <section class="hero hero--sub">
    <div class="container">
      <nav class="breadcrumb" aria-label="Breadcrumb"><ol><li><a href="index.html">Home</a></li><li>Why Sharpe's</li><li>Review Us</li></ol></nav>
      <p class="eyebrow">Thank you</p>
      <h1>Leave Sharpe's a review</h1>
      <p>If we've done good work for you, a quick review helps your neighbors across the Midlands find a team they can trust.</p>
    </div>
  </section>
  <section class="section">
    <div class="container center" style="max-width:680px">
      <div class="card">
        <span class="card-icon" aria-hidden="true" style="margin:0 auto">⭐</span>
        <h2>Share your experience</h2>
        <p class="lead" style="margin:0 auto 24px">Choose where you'd like to leave a review. We appreciate your feedback!</p>
        <!-- CMS: confirm the exact Google review URL before launch; Facebook points to the live Sharpe's page. -->
        <div class="hero-actions" style="justify-content:center">
          <a class="btn btn--primary btn--lg" href="https://www.google.com/search?q=Sharpe%27s+Septic+Tank+%26+Well+Drilling+Service+reviews" data-track="review_click">Review on Google</a>
          <a class="btn btn--secondary btn--lg" href="https://www.facebook.com/sharpessepticwell1966/" data-track="review_click">Review on Facebook</a>
        </div>
      </div>
    </div>
  </section>
"""
    b += cta_band()
    b += "  </main>\n"
    b += footer()
    write("review-us.html", b)


def build_all():
    build_contact()
    build_faqs()
    build_associations()
    build_why()
    build_reviews()
    build_review_us()
