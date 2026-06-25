/* ============================================================
   Sharpe's Septic — shared front-end behavior
   ------------------------------------------------------------
   Vanilla JS, no dependencies. Progressive enhancement only:
   the site is fully usable with JS disabled.

   Handles: mobile nav, accessible submenu toggles, FAQ a11y,
   conditional modules, contact-form service prefill + validation,
   promo popup, and lightweight analytics hooks (data-track).
   ============================================================ */
(function () {
  "use strict";

  /* ---- Analytics hooks --------------------------------------
     Every element with [data-track="event_name"] fires a push to
     window.dataLayer (GA4 / GTM friendly). Swap pushTrack() for
     your own tracker if needed. */
  window.dataLayer = window.dataLayer || [];
  function pushTrack(name, detail) {
    window.dataLayer.push(Object.assign({ event: name }, detail || {}));
  }
  document.addEventListener("click", function (e) {
    var el = e.target.closest("[data-track]");
    if (el) pushTrack(el.getAttribute("data-track"), { label: (el.textContent || "").trim().slice(0, 60) });
  });

  /* ---- Mobile nav toggle ------------------------------------ */
  var navToggle = document.querySelector(".nav-toggle");
  var nav = document.querySelector(".main-nav");
  if (navToggle && nav) {
    navToggle.addEventListener("click", function () {
      var open = nav.getAttribute("data-open") === "true";
      nav.setAttribute("data-open", String(!open));
      navToggle.setAttribute("aria-expanded", String(!open));
    });
  }

  /* ---- Submenu toggles (keyboard + mobile) ------------------ */
  document.querySelectorAll(".has-sub > button").forEach(function (btn) {
    btn.addEventListener("click", function (e) {
      var li = btn.parentElement;
      var expanded = li.getAttribute("aria-expanded") === "true";
      // close siblings
      document.querySelectorAll(".has-sub[aria-expanded='true']").forEach(function (o) {
        if (o !== li) o.setAttribute("aria-expanded", "false");
      });
      li.setAttribute("aria-expanded", String(!expanded));
      e.stopPropagation();
    });
  });
  document.addEventListener("click", function () {
    document.querySelectorAll(".has-sub[aria-expanded='true']").forEach(function (o) {
      o.setAttribute("aria-expanded", "false");
    });
  });
  // Esc closes nav + submenus
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") {
      if (nav) { nav.setAttribute("data-open", "false"); if (navToggle) navToggle.setAttribute("aria-expanded", "false"); }
      document.querySelectorAll(".has-sub[aria-expanded='true']").forEach(function (o) { o.setAttribute("aria-expanded", "false"); });
      closePromo();
    }
  });

  /* ---- FAQ analytics (native <details> handles open/close) -- */
  document.querySelectorAll(".faq-item").forEach(function (item) {
    item.addEventListener("toggle", function () {
      if (item.open) pushTrack("faq_expand", { question: (item.querySelector("summary") || {}).textContent });
    });
  });

  /* ---- Conditional modules ----------------------------------
     A module is shown only when configured. Two ways to enable:
       1. Set data-url to a real URL (replaces {{...}} placeholder)
       2. Set data-enabled="true"
     Otherwise it stays hidden. This keeps ServiceTitan, Customer
     Portal, Financing, Social Feed, and Popup OFF until confirmed. */
  document.querySelectorAll("[data-module]").forEach(function (mod) {
    var url = mod.getAttribute("data-url") || "";
    var enabled = mod.getAttribute("data-enabled") === "true";
    var configured = enabled || (url && url.indexOf("{{") === -1 && url.trim() !== "");
    if (configured) {
      mod.hidden = false;
      // wire any link inside to the provided URL
      if (url) mod.querySelectorAll("[data-module-link]").forEach(function (a) { a.setAttribute("href", url); });
    } else {
      mod.hidden = true;
    }
  });

  /* ---- Service-type prefill from URL (supports ?service=septic-inspection)
     Works across every service <select> on the page (hero form, landing
     page, contact page) so PPC links can deep-link a service. */
  var params = new URLSearchParams(window.location.search);
  var svc = params.get("service");
  document.querySelectorAll('select[name="service"]').forEach(function (sel) {
    if (svc) {
      var match = Array.prototype.find.call(sel.options, function (o) { return o.value === svc; });
      if (match) { sel.value = svc; pushTrack("service_type_selection", { service: svc, source: "url" }); }
    }
    sel.addEventListener("change", function () {
      pushTrack("service_type_selection", { service: sel.value, source: "manual" });
    });
  });

  /* ---- Accessible validation for every [data-contact-form] -------
     Handles the contact page, the homepage hero form, and the PPC
     landing-page form independently. */
  document.querySelectorAll("form[data-contact-form]").forEach(function (form) {
    var started = false;
    form.addEventListener("input", function () {
      if (!started) { started = true; pushTrack("contact_form_start", { form: form.getAttribute("data-form-name") || "contact" }); }
    });
    form.addEventListener("submit", function (e) {
      var valid = true;
      form.querySelectorAll("[required]").forEach(function (input) {
        var field = input.closest(".field");
        var ok = input.value.trim() !== "" && (input.type !== "email" || /\S+@\S+\.\S+/.test(input.value));
        if (!ok) { valid = false; if (field) field.classList.add("has-error"); input.setAttribute("aria-invalid", "true"); }
        else { if (field) field.classList.remove("has-error"); input.removeAttribute("aria-invalid"); }
      });
      if (!valid) {
        e.preventDefault();
        var firstErr = form.querySelector(".has-error input, .has-error select, .has-error textarea");
        if (firstErr) firstErr.focus();
      } else {
        var sel = form.querySelector('select[name="service"]');
        pushTrack("contact_form_submit", { service: sel ? sel.value : "", form: form.getAttribute("data-form-name") || "contact" });
        // Demo only: prevent navigation in static prototype.
        if (form.getAttribute("action") === "{{contactFormEndpoint}}" || !form.getAttribute("action")) {
          e.preventDefault();
          var note = form.querySelector("[data-form-success]");
          if (note) { note.hidden = false; note.focus(); form.querySelectorAll(".field").forEach(function(f){f.style.display="none";}); }
          var submitRow = form.querySelector("[data-form-submit]");
          if (submitRow) submitRow.style.display = "none";
        }
      }
    });
  });

  /* ---- Promo popup (DISABLED by default) --------------------
     Enable by setting data-enabled="true" on .promo-popup and
     optionally data-delay="6000". Respects a session dismiss. */
  var popup = document.querySelector(".promo-popup");
  function closePromo() {
    if (popup) { popup.setAttribute("data-open", "false"); pushTrack("promo_popup_close"); }
  }
  if (popup && popup.getAttribute("data-enabled") === "true") {
    var dismissed = window.sessionStorage && sessionStorage.getItem("sharpes_promo_dismissed");
    if (!dismissed) {
      var delay = parseInt(popup.getAttribute("data-delay") || "6000", 10);
      setTimeout(function () {
        popup.setAttribute("data-open", "true");
        pushTrack("promo_popup_open");
        // a11y: move focus into the dialog so keyboard/screen-reader users land on it
        var closeBtn = popup.querySelector(".promo-close");
        if (closeBtn) closeBtn.focus();
      }, delay);
    }
    popup.addEventListener("click", function (e) {
      if (e.target === popup || e.target.closest(".promo-close")) {
        closePromo();
        try { sessionStorage.setItem("sharpes_promo_dismissed", "1"); } catch (err) {}
      }
    });
  }

  /* ---- Footer year ------------------------------------------ */
  var yr = document.querySelector("[data-year]");
  if (yr) yr.textContent = new Date().getFullYear();

  /* ---- Header: add depth once the page is scrolled ---------- */
  var header = document.querySelector(".site-header");
  if (header) {
    var onScroll = function () {
      if (window.pageYOffset > 8) header.classList.add("is-scrolled");
      else header.classList.remove("is-scrolled");
    };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  /* ---- Scroll reveal (progressive enhancement) --------------
     Only runs when motion is allowed and IntersectionObserver is
     available; otherwise content stays fully visible (no .reveal
     class is ever added). Elements above the fold reveal at once. */
  var reduceMotion = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (!reduceMotion && "IntersectionObserver" in window) {
    // gate the CSS hidden-states so no-JS users always see content
    document.documentElement.classList.add("js-anim");
    var selectors = [
      ".section .card", ".section .testimonial", ".section .step",
      ".split > *", ".trust-item", ".faq-item", ".related-grid a",
      ".section > .container > .center", ".symptom-card", ".sign-card", ".qa-card"
    ];
    var auto = document.querySelectorAll(selectors.join(","));
    auto.forEach(function (el) {
      el.classList.add("reveal");
      var sibs = el.parentElement ? Array.prototype.indexOf.call(el.parentElement.children, el) : 0;
      if (sibs > 0 && sibs < 4) el.setAttribute("data-reveal-i", String(sibs));
    });
    // combine auto-reveal elements with explicit [data-anim] (directional) elements
    var directional = document.querySelectorAll("[data-anim]");
    var nodes = [];
    auto.forEach(function (el) { nodes.push(el); });
    directional.forEach(function (el) { nodes.push(el); });
    // connector-line containers: get .is-visible to trigger the scroll-drawn lines
    document.querySelectorAll(".feature-grid, .steps-flow").forEach(function (el) { nodes.push(el); });
    if (nodes.length) {
      var io = new IntersectionObserver(function (entries, obs) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
            obs.unobserve(entry.target);
          }
        });
      }, { rootMargin: "0px 0px -8% 0px", threshold: 0.08 });
      nodes.forEach(function (el) { io.observe(el); });
      // Safety net: reveal everything shortly after load in case anything is missed.
      window.addEventListener("load", function () {
        setTimeout(function () {
          nodes.forEach(function (el) { el.classList.add("is-visible"); });
        }, 1400);
      });
    }
  }

  /* ---- Animated stat counters --------------------------------- */
  var statNums = document.querySelectorAll(".stat-num[data-count]");
  if (statNums.length && "IntersectionObserver" in window) {
    var statIO = new IntersectionObserver(function (entries, obs) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        var el = e.target, target = parseFloat(el.getAttribute("data-count")), suf = el.getAttribute("data-suffix") || "";
        obs.unobserve(el);
        if (reduceMotion) { el.textContent = target + suf; return; }
        var dur = 1400, start = null;
        function tick(ts) {
          if (!start) start = ts;
          var p = Math.min((ts - start) / dur, 1);
          var eased = 0.5 - Math.cos(p * Math.PI) / 2; // easeInOut
          el.textContent = Math.round(target * eased) + suf;
          if (p < 1) requestAnimationFrame(tick);
        }
        requestAnimationFrame(tick);
      });
    }, { threshold: 0.4 });
    statNums.forEach(function (el) { statIO.observe(el); });
  }

  /* ---- Back-to-top button ------------------------------------- */
  var toTop = document.createElement("button");
  toTop.className = "to-top";
  toTop.type = "button";
  toTop.setAttribute("aria-label", "Back to top");
  toTop.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 19V5M6 11l6-6 6 6"/></svg>';
  document.body.appendChild(toTop);
  toTop.addEventListener("click", function () {
    window.scrollTo({ top: 0, behavior: (window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches) ? "auto" : "smooth" });
  });
  window.addEventListener("scroll", function () {
    if (window.pageYOffset > 600) toTop.classList.add("show");
    else toTop.classList.remove("show");
  }, { passive: true });
})();
