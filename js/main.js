// ==========================================================================
// Café R2 — main.js
// Sticky/shrinking header, mobile nav, carousel autoplay, menu tabs,
// scroll-to-top, and contact form + Cloudflare Turnstile handling.
// ==========================================================================

// ---- CONFIG: update these before going live ----
// See README.md / SETUP-GUIDE.md for the full step-by-step.
const CONFIG = {
  // Cloudflare Turnstile dashboard -> your widget -> "Sitekey"
  TURNSTILE_SITE_KEY: "1x00000000000000000000AA", // <-- REPLACE with your real sitekey

  // Formspree dashboard -> your form -> "Endpoint" (looks like
  // https://formspree.io/f/xxxxabcd). Formspree verifies the Turnstile
  // token server-side automatically once you paste your Turnstile Secret
  // Key into the Formspree form's CAPTCHA settings — no custom backend
  // needed at all.
  FORM_ENDPOINT: "https://formspree.io/f/REPLACE_WITH_YOUR_FORM_ID",
};

document.addEventListener("DOMContentLoaded", () => {
  initHeader();
  initMobileNav();
  initCarousel();
  initMenuTabs();
  initScrollTop();
  initTurnstile();
  initContactForm();
  initYear();
});

/* ---------------- Sticky / shrinking header ---------------- */
function initHeader() {
  const header = document.querySelector(".site-header");
  if (!header) return;
  const onScroll = () => {
    if (window.scrollY > 40) header.classList.add("scrolled");
    else header.classList.remove("scrolled");
  };
  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });
}

/* ---------------- Mobile nav toggle ---------------- */
function initMobileNav() {
  const toggle = document.querySelector(".nav-toggle");
  const nav = document.querySelector(".main-nav");
  if (!toggle || !nav) return;
  toggle.addEventListener("click", () => {
    nav.classList.toggle("open");
    const isOpen = nav.classList.contains("open");
    toggle.setAttribute("aria-expanded", isOpen ? "true" : "false");
  });
  nav.querySelectorAll("a").forEach((link) => {
    link.addEventListener("click", () => nav.classList.remove("open"));
  });
}

/* ---------------- Auto-playing carousel ---------------- */
function initCarousel() {
  const track = document.querySelector(".carousel-track");
  if (!track) return;

  let autoScroll = true;
  let dir = 1;
  const speed = 0.6; // px per frame

  track.addEventListener("mouseenter", () => (autoScroll = false));
  track.addEventListener("mouseleave", () => (autoScroll = true));
  track.addEventListener("touchstart", () => (autoScroll = false), { passive: true });

  function step() {
    if (autoScroll) {
      const maxScroll = track.scrollWidth - track.clientWidth;
      if (maxScroll > 0) {
        track.scrollLeft += speed * dir;
        if (track.scrollLeft >= maxScroll - 1) dir = -1;
        if (track.scrollLeft <= 0) dir = 1;
      }
    }
    requestAnimationFrame(step);
  }
  requestAnimationFrame(step);
}

/* ---------------- Menu category tabs ---------------- */
function initMenuTabs() {
  const tabs = document.querySelectorAll(".menu-tab");
  const panels = document.querySelectorAll(".menu-panel");
  if (!tabs.length) return;

  tabs.forEach((tab) => {
    tab.addEventListener("click", () => {
      const target = tab.getAttribute("data-target");
      tabs.forEach((t) => t.classList.remove("active"));
      panels.forEach((p) => p.classList.remove("active"));
      tab.classList.add("active");
      const panel = document.getElementById(target);
      if (panel) panel.classList.add("active");
      tab.scrollIntoView({ behavior: "smooth", inline: "center", block: "nearest" });
    });
  });
}

/* ---------------- Scroll to top button ---------------- */
function initScrollTop() {
  const btn = document.querySelector(".scroll-top");
  if (!btn) return;
  window.addEventListener(
    "scroll",
    () => {
      if (window.scrollY > 600) btn.classList.add("show");
      else btn.classList.remove("show");
    },
    { passive: true }
  );
  btn.addEventListener("click", () => {
    window.scrollTo({ top: 0, behavior: "smooth" });
  });
}

/* ---------------- Cloudflare Turnstile ---------------- */
function initTurnstile() {
  const wrap = document.querySelector(".turnstile-wrap");
  if (!wrap) return;
  const widget = document.createElement("div");
  widget.className = "cf-turnstile";
  widget.setAttribute("data-sitekey", CONFIG.TURNSTILE_SITE_KEY);
  widget.setAttribute("data-theme", "light");
  widget.setAttribute("data-callback", "onTurnstileVerified");
  widget.setAttribute("data-expired-callback", "onTurnstileExpired");
  wrap.appendChild(widget);
}

window.turnstileToken = null;
window.onTurnstileVerified = function (token) {
  window.turnstileToken = token;
};
window.onTurnstileExpired = function () {
  window.turnstileToken = null;
};

/* ---------------- Contact form ---------------- */
function initContactForm() {
  const form = document.querySelector("#contact-form");
  const status = document.querySelector(".form-status");
  if (!form) return;

  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    status.textContent = "";
    status.className = "form-status";

    if (!form.name.value.trim() || !form.phone.value.trim() || !form.message.value.trim()) {
      status.textContent = "Please fill in your name, phone and message. / කරුණාකර නම, දුරකථන අංකය සහ පණිවිඩය සම්පූර්ණ කරන්න.";
      status.classList.add("err");
      return;
    }

    if (!window.turnstileToken) {
      status.textContent = "Please complete the verification box above before sending. / කරුණාකර ඉහත සත්‍යාපන කොටුව සම්පූර්ණ කරන්න.";
      status.classList.add("err");
      return;
    }

    const submitBtn = form.querySelector("button[type='submit']");
    const originalLabel = submitBtn.textContent;
    submitBtn.disabled = true;
    submitBtn.textContent = "Sending...";

    try {
      // Formspree reads all of the form's fields directly from FormData,
      // including the "cf-turnstile-response" hidden field that the
      // Turnstile widget automatically adds inside this <form>. Formspree
      // verifies that token server-side using the Turnstile Secret Key you
      // paste into your Formspree form's CAPTCHA settings — no custom
      // backend required. See README.md / SETUP-GUIDE.md.
      const res = await fetch(CONFIG.FORM_ENDPOINT, {
        method: "POST",
        headers: { Accept: "application/json" },
        body: new FormData(form),
      });

      const result = await res.json().catch(() => ({}));

      if (!res.ok || result.errors) {
        const msg = (result.errors && result.errors.map((x) => x.message).join(", ")) || "";
        throw new Error(msg || "Request failed");
      }

      status.textContent = "Thank you! Your message has been sent. We'll get back to you soon. / ස්තූතියි! ඔබේ පණිවිඩය යවා ඇත.";
      status.classList.add("ok");
      form.reset();
      window.turnstileToken = null;
      if (window.turnstile) window.turnstile.reset();
    } catch (err) {
      status.textContent =
        "Couldn't send right now — please call/WhatsApp us at +94 70 252 6009, or email cafer2juicebar@gmail.com directly.";
      status.classList.add("err");
    } finally {
      submitBtn.disabled = false;
      submitBtn.textContent = originalLabel;
    }
  });
}

/* ---------------- Footer year ---------------- */
function initYear() {
  const el = document.querySelector("#year");
  if (el) el.textContent = new Date().getFullYear();
}
