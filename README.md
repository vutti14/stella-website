# STELLA Website

Static marketing site for STELLA architectural glazing. Nine pages, no build step.

**Live site:** https://vutti14.github.io/stella-website/

`stella.co.th` is **not** this site today. Apex DNS currently points elsewhere (and does not serve these pages). `www.stella.co.th` is an unrelated Google Sites property. Keep the `stella.co.th` addresses in on-page copy (for example `concierge@stella.co.th`) as the intended brand domain; attach it later using the steps in `HOW_TO_DEPLOY.md`.

---

## What's in this folder

```
stella-website/
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
├── netlify.toml        Optional Netlify hosting config
├── _redirects          Netlify clean-URL rewrites
├── robots.txt          SEO crawler rules
├── sitemap.xml         SEO sitemap
└── HOW_TO_DEPLOY.md    GitHub Pages (current) + custom domain + Netlify
```

---

## How paths work

Internal links, the favicon, CSS, and JS are **same-directory relative** (`href="about"`, `href="favicon.svg"`, not `href="/about"`).

That is required for a GitHub Pages *project* site (`https://user.github.io/stella-website/`). Root-absolute paths like `/about` resolve to `https://user.github.io/about` and 404.

The same relative URLs also work if the site is later served from a custom domain at the site root (`https://stella.co.th/about`).

Clean URLs (`/about`, not only `/about.html`) already work on GitHub Pages. Do not add a trailing slash (`/about/` is a 404 there). On Netlify, `_redirects` rewrites `/about` → `about.html`.

---

## Forms

Contact and showroom forms POST to [FormSubmit](https://formsubmit.co) at `concierge@stella.co.th` (no API key). After a successful submit, FormSubmit redirects to this site's `thank-you` page. JavaScript sets `_next` from the current page URL so the redirect stays on GitHub Pages or a future apex domain.

**First submission:** FormSubmit emails `concierge@stella.co.th` a one-time confirmation link. Confirm that once, then submissions arrive as normal.

**Netlify Forms:** not used. `data-netlify` was removed so a later Netlify deploy does not intercept the POST and send visitors to formsubmit.co as a GET. FormSubmit still works if you drop the folder on Netlify. To switch back to Netlify Forms, see `HOW_TO_DEPLOY.md`.

---

## What's working out of the box

- **Premium editorial design** — Cormorant Garamond × Inter × Noto Serif Thai
- **Responsive** — full mobile support including hamburger drawer menu
- **Scroll-reveal animations** — content fades in as you scroll
- **Sticky navigation** — adds a subtle border + tightens on scroll
- **Working forms** — Showroom Booking and Contact Inquiry post via FormSubmit
- **Form spam protection** — FormSubmit `_honey` honeypot
- **Clean URLs** — `/about` instead of `/about.html`
- **SEO** — meta tags, Open Graph, Twitter Card, sitemap, canonical URLs (pointing at the live GitHub Pages origin until a custom domain is attached)
- **Accessibility** — skip-to-content link, ARIA labels, keyboard navigation, prefers-reduced-motion support
- **Performance** — fonts preconnected, no heavy frameworks
- **Background grain** — subtle SVG noise for warmth

---

## Local preview

Serve the folder (opening `file://` pages is fine for a quick look; a local server matches production more closely):

```bash
python3 -m http.server 8080
```

Then open http://127.0.0.1:8080/

---

## What still needs real content

1. **Phone number** — replace `+66 (0) 2 ___ ____` everywhere with the real number
2. **Email addresses** — confirm `concierge@`, `design@`, `projects@`, `care@` are set up
3. **Showroom address** — currently general; add when you want it public (or keep "Thonglor, by appointment")
4. **Project photography** — replace `.placeholder` cards in `projects.html` with real shots when ready
5. **Verify Thai copy** — the existing translations are in the prototype; final copy review by the team is recommended
6. **Canonical / OG / sitemap origin** — currently `https://vutti14.github.io/stella-website/`. After attaching a custom domain, update those absolute URLs (see `HOW_TO_DEPLOY.md`)

---

## Updating contact info

Open any `.html` file in any text editor and search for:
- `+66 (0) 2 ___ ____` — replace with the real phone
- `concierge@stella.co.th` — replace if a different email is preferred (also update the FormSubmit `action` on `contact.html` and `showroom.html`)
- `Thonglor, Sukhumvit` — update if the showroom address changes

---

## Browser support

Modern evergreen browsers (Chrome, Edge, Safari, Firefox — last 2 years).
The site degrades gracefully on older browsers — animations turn off, layout still works.
