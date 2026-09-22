# Café R2 — Website (v1 draft)

A mobile-first, bilingual (English + Sinhala) website for Café R2, Urubokka.

## What's inside

```
index.html          Main page (all sections: hero, menu, gallery, contact, etc.)
css/style.css        All styling
js/main.js           Header shrink/sticky, mobile nav, auto-carousel, menu tabs,
                      scroll-to-top, Turnstile + contact form handling
images/              Logo, favicons, and 8 product photos
robots.txt           Tells search engines they can crawl the whole site
sitemap.xml          Basic sitemap for search engines
build_menu.py        OPTIONAL: the script used to generate the menu HTML from a
                      simple Python list — only needed if you want to regenerate
                      the whole menu section later. For small edits (a price, a
                      name), just edit index.html directly — search for the item
                      name and change it in place.
SETUP-GUIDE.md        Step-by-step: GitHub -> Cloudflare Pages (free hosting) ->
                      Turnstile -> Formspree. Start here when you're ready to
                      go live.
```

## How to preview it right now

No install needed — just double-click `index.html` and it opens in your browser.
For the best test (mobile view, sticky header, etc.), open it in Chrome, press
F12, and toggle "device toolbar" to see the mobile layout.

## ⚠️ Things to fix before this goes live

1. **Domain name** — I used a placeholder domain `caferz2.lk` in the SEO tags
   (`<link rel="canonical">`, Open Graph tags, and the JSON-LD schema at the top
   of `index.html`). Once you register a real domain, find-and-replace
   `caferz2.lk` with your actual domain throughout `index.html`.
2. **Menu prices** — I don't have your real prices, so I filled in reasonable
   placeholder prices (Rs. 60–420) for every item so the layout looks complete.
   **Please review and correct every price** before publishing — search
   `Rs. ` in `index.html` to find them all quickly.
3. **TikTok link** — you mentioned you want a TikTok handle included; I've left
   the TikTok buttons in place (footer + contact section) but pointed them at
   `#` (a placeholder) since I don't have the real handle/link yet. Search for
   `data-tiktok-placeholder` in `index.html` and update the `href`.
4. **Email address** — currently using `cafer2juicebar@gmail.com` as you gave
   me. You mentioned switching to a domain email later (e.g.
   `hello@caferz2.lk`) — just find-and-replace once that's set up.
5. **Reviews section** — currently shows 6 real Google reviews (real names,
   real quotes) that you provided via screenshots. If you'd rather feature
   different ones, or new reviews come in later, search `review-card` in
   `index.html` to find/edit/add them.
6. **Google Maps embed** — I've wired the embed and the "Open in Google Maps"
   button using your café name/address. Once you're happy, you can also grab
   the exact embed code from Google Maps (Share → Embed a map) using your
   Business Profile pin for pixel-perfect accuracy.

## Making the contact form actually send messages

Good news: **Formspree has native Cloudflare Turnstile support**, so no
custom backend code is needed at all. Formspree verifies the Turnstile token
server-side automatically once you paste your Turnstile **Secret Key** into
your Formspree form's CAPTCHA settings.

Full click-by-click steps (GitHub → Cloudflare Pages → Turnstile → Formspree,
all free tiers) are in **`SETUP-GUIDE.md`** in this same folder — start there.

The short version, once you have your keys:
```js
// js/main.js
const CONFIG = {
  TURNSTILE_SITE_KEY: "your-real-turnstile-site-key",
  FORM_ENDPOINT: "https://formspree.io/f/your-form-id",
};
```
...and the matching `action="https://formspree.io/f/your-form-id"` on the
`<form>` tag in `index.html` (contact section).

## Next steps (once you've reviewed this draft)

Once you're happy with the content, open **`SETUP-GUIDE.md`** and follow it
step by step — it covers GitHub, Cloudflare Pages (free hosting), Turnstile
and Formspree in order, using only free tiers. I'm happy to walk through any
step with you live, one at a time.
