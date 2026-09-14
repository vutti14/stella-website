# How to Deploy STELLA

The production site is **GitHub Pages**: https://vutti14.github.io/stella-website/

`stella.co.th` is not this site yet. Do not change apex DNS until you control that domain and are ready to point it at this repo. `www.stella.co.th` currently belongs to a different company (STELLA TECH, testing instruments).

There is no build step. GitHub Pages is already enabled on `main` (`/` as the publishing folder). Merging to `main` republishes the site.

---

## Option 1 — GitHub Pages (current production)

1. Push or merge to `main`.
2. Wait for the Pages build (Settings → Pages, or the `pages build and deployment` Action).
3. Visit https://vutti14.github.io/stella-website/

### Attaching a custom domain later

When you own a domain you want to use for *this* site (for example `stella.co.th`):

1. In the repo: Settings → Pages → Custom domain. Enter the domain and save. GitHub will add or ask for a `CNAME` file in `main`.
2. At the DNS host, follow GitHub’s records for an apex (`A` / `ALIAS`) or `www` (`CNAME` to `vutti14.github.io`).
3. Enable “Enforce HTTPS” once the certificate is ready.
4. Update absolute SEO URLs so crawlers and social previews match the new origin:
   - `canonical`, `og:url`, `og:image`, `twitter:image` in every `.html` page
   - `robots.txt` sitemap line
   - every `<loc>` in `sitemap.xml`
   - the fallback `_next` values in `contact.html` and `showroom.html` (JavaScript already rewrites `_next` from the current host, so forms keep working before this edit)
5. Internal navigation does **not** need to change. Relative links work at a project URL (`/stella-website/`) and at a domain apex (`/`).

---

## Option 2 — Netlify Drop (optional)

1. Open https://app.netlify.com/drop in a browser
2. Drag this entire folder onto the page
3. Wait ~30 seconds
4. The site is live at a random `*.netlify.app` URL

Forms still work (they post to FormSubmit, not Netlify Forms). Clean URLs work via `_redirects`.

`netlify.toml` remains for headers and caching if you use this host.

---

## Option 3 — Netlify Git Deploy (optional)

1. Netlify dashboard → “Add new site” → “Import from Git”
2. Select this repo, accept defaults (`publish = "."`)
3. Every push to `main` auto-deploys

---

## How forms work

Both `showroom.html` and `contact.html` POST to **FormSubmit** (`https://formsubmit.co/concierge@stella.co.th`):

- The visitor submits the form
- FormSubmit emails `concierge@stella.co.th`
- The browser is redirected to this site’s `thank-you` page (`_next`)

No API key is required. The first submission sends a confirmation message to that inbox — open the link once to activate.

Honeypot field: `_honey` (hidden). Captcha is disabled (`_captcha=false`) so the flow can reach thank-you without a third-party widget.

### Switching back to Netlify Forms

FormSubmit was chosen so GitHub Pages has a working backend. If you deploy on Netlify and prefer Netlify Forms instead:

1. Remove `action="https://formsubmit.co/..."`.
2. Set `action="thank-you"` (relative).
3. Add `data-netlify="true"` and `netlify-honeypot="bot-field"`.
4. Restore a `form-name` hidden input and a `bot-field` honeypot.
5. Do **not** keep the FormSubmit action together with `data-netlify` — Netlify will intercept the POST and then redirect to formsubmit.co as a GET.

---

## Before going live — checklist

- [ ] Confirm the FormSubmit activation email at `concierge@stella.co.th`
- [ ] Test the contact form end-to-end (submit a test → check email → land on thank-you)
- [ ] Test the showroom form end-to-end
- [ ] Open the site on a phone — check the hamburger menu
- [ ] After a custom domain: rewrite canonical / OG / sitemap URLs to that origin
