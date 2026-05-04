# How to Deploy STELLA — 3-Minute Guide

## Option 1 — Netlify Drop (fastest, recommended)

1. Open https://app.netlify.com/drop in a browser
2. Drag the entire **stella_site** folder onto the page
3. Wait ~30 seconds while Netlify uploads + indexes the forms
4. Your site is live at a random URL like `loving-newton-abc123.netlify.app`
5. Click "Site settings" → "Change site name" to pick something nicer

### Connecting your domain `stella.co.th`

1. In your Netlify dashboard → "Domain management" → "Add a domain"
2. Enter `stella.co.th` and `www.stella.co.th`
3. Netlify gives you DNS records — paste them into your domain registrar
4. SSL is automatic (Let's Encrypt) within 24 hours

---

## Option 2 — Netlify Git Deploy (best for ongoing edits)

1. Create a new GitHub repo and push these files
2. Netlify dashboard → "Add new site" → "Import from Git"
3. Select your repo, accept defaults (`publish = "."`)
4. Every push to `main` auto-deploys — instant updates

---

## Option 3 — Vercel (alternative)

1. Open https://vercel.com/new
2. Drag the folder, or import a Git repo
3. Forms won't work natively — see notes below

---

## How forms work

Both `showroom.html` and `contact.html` use **Netlify Forms** (free for up to 100 submissions/month):

- The submitter fills the form and clicks Submit
- Netlify intercepts the POST, stores it in your dashboard
- The user is redirected to `/thank-you`
- You get an email notification (configure in Site settings → Forms → Notifications)

To customize the email:
- Site settings → Forms → Notifications → Email notifications
- Add `concierge@stella.co.th`

If you switch to a different host (Vercel, Cloudflare Pages, etc.), you'll need to swap the form action — see e.g. Formspree or Web3Forms for drop-in replacements.

---

## Before going live — checklist

- [ ] Real phone number in nav + footer (search `+66 (0) 2 ___ ____`)
- [ ] Real email addresses set up at the host
- [ ] Real showroom address (or keep general "Thonglor")
- [ ] Test the contact form end-to-end (submit a test → check email)
- [ ] Test the showroom form end-to-end
- [ ] Open the site on a phone — check the hamburger menu
- [ ] Verify SEO: search for "STELLA architectural glazing" once indexed
