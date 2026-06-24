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

  /* ---- Contact form: prefill service type from URL ----------
     Supports /contact/?service=septic-inspection */
  var params = new URLSearchParams(window.location.search);
  var svc = params.get("service");
  var svcSelect = document.querySelector("#service-type");
  if (svc && svcSelect) {
    var match = Array.prototype.find.call(svcSelect.options, function (o) { return o.value === svc; });
    if (match) { svcSelect.value = svc; pushTrack("service_type_selection", { service: svc, source: "url" }); }
  }
  if (svcSelect) {
    svcSelect.addEventListener("change", function () {
      pushTrack("service_type_selection", { service: svcSelect.value, source: "manual" });
    });
  }

  /* ---- Contact form: accessible validation ------------------ */
  var form = document.querySelector("form[data-contact-form]");
  if (form) {
    var started = false;
    form.addEventListener("input", function () {
      if (!started) { started = true; pushTrack("contact_form_start"); }
    });
    form.addEventListener("submit", function (e) {
      var valid = true;
      form.querySelectorAll("[required]").forEach(function (input) {
        var field = input.closest(".field");
        var ok = input.value.trim() !== "" && (input.type !== "email" || /\S+@\S+\.\S+/.test(input.value));
        if (!ok) { valid = false; field.classList.add("has-error"); input.setAttribute("aria-invalid", "true"); }
        else { field.classList.remove("has-error"); input.removeAttribute("aria-invalid"); }
      });
      if (!valid) {
        e.preventDefault();
        var firstErr = form.querySelector(".has-error input, .has-error select, .has-error textarea");
        if (firstErr) firstErr.focus();
      } else {
        pushTrack("contact_form_submit", { service: svcSelect ? svcSelect.value : "" });
        // Demo only: prevent navigation in static prototype.
        if (form.getAttribute("action") === "{{contactFormEndpoint}}" || !form.getAttribute("action")) {
          e.preventDefault();
          var note = form.querySelector("[data-form-success]");
          if (note) { note.hidden = false; note.focus(); form.querySelectorAll(".field").forEach(function(f){f.style.display="none";}); }
        }
      }
    });
  }

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
})();
