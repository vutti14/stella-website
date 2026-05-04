# STELLA Website — Production-Ready Build

**Domain:** stella.co.th
**Pages:** 9 (Homepage, About, System, Tiers, Process, Projects, Contact, Showroom, Thank-you)
**Framework:** Static HTML + CSS + vanilla JS — no build step

---

## What's in this folder

```
stella_site/
├── index.html          Homepage
├── about.html          Manifesto / philosophy
├── system.html         Anatomy + materials + performance
├── tiers.html          Essential / Signature / Reserve
├── process.html        Five conversations (timeline)
├── projects.html       Project gallery
├── contact.html        Direct lines + inquiry form
├── showroom.html       Sound-chamber appointment form
├── thank-you.html      Form-success page
├── styles.css          Master stylesheet (shared)
├── scripts.js          Mobile menu, scroll reveal, form UX
├── favicon.svg         Brand mark
├── og-image.png        Social-share image
├── og-image.svg        Social-share source
├── netlify.toml        Hosting config (security headers + cache)
├── _redirects          Clean URLs (about → about.html)
├── robots.txt          SEO crawler rules
├── sitemap.xml         SEO sitemap
└── HOW_TO_DEPLOY.md    Step-by-step deployment guide
```

---

## What's working out of the box

- **Premium editorial design** — Cormorant Garamond × Inter × Noto Serif Thai
- **Responsive** — full mobile support including hamburger drawer menu
- **Scroll-reveal animations** — content fades in elegantly as you scroll
- **Sticky navigation** — adds a subtle border + tightens on scroll
- **Working forms** — both Showroom Booking and Contact Inquiry post to Netlify Forms
- **Form spam protection** — built-in honeypot field
- **Clean URLs** — `/about` instead of `/about.html` (via _redirects)
- **SEO** — meta tags, Open Graph, Twitter Card, sitemap, canonical URLs
- **Accessibility** — skip-to-content link, ARIA labels, keyboard navigation, prefers-reduced-motion support
- **Performance** — fonts preconnected, CSS minified-friendly, no heavy frameworks
- **Background grain** — subtle SVG noise for warmth

---

## Deploy in 3 minutes (Netlify)

1. Go to [app.netlify.com/drop](https://app.netlify.com/drop)
2. Drag this **entire folder** into the drop zone
3. Done — your site is live at `random-name.netlify.app`

To use your custom domain `stella.co.th`:
1. Site settings → Domain management → Add custom domain
2. Update DNS to point to Netlify (instructions provided)

Forms will work automatically — submissions appear under **Forms** in your Netlify dashboard, and email notifications can be configured under Site settings → Forms → Notifications.

---

## What still needs real content

1. **Phone number** — replace `+66 (0) 2 ___ ____` everywhere with the real number
2. **Email addresses** — confirm `concierge@`, `design@`, `projects@`, `care@` are set up
3. **Showroom address** — currently blank; add when you want it public (or keep "Thonglor, by appointment")
4. **Project photography** — replace `.placeholder` cards in `projects.html` with real shots when ready
5. **Verify Thai copy** — the existing translations are in the prototype; final copy review by the team is recommended

---

## Updating contact info

Open any `.html` file in any text editor and search for:
- `+66 (0) 2 ___ ____` — replace with the real phone (3 occurrences per page in nav and footer)
- `concierge@stella.co.th` — replace if a different email is preferred
- `Thonglor, Sukhumvit` — update if the showroom address changes

A find-and-replace across all files takes about 5 minutes.

---

## Browser support

Modern evergreen browsers (Chrome, Edge, Safari, Firefox — last 2 years).
The site degrades gracefully on older browsers — animations turn off, layout still works.
