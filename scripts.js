/* ═══════════════════════════════════════════════════════════
   STELLA — Front-end behavior
   - Mobile nav toggle
   - Scroll reveal (IntersectionObserver)
   - Sticky-nav state on scroll
   - Form submit loading state
   ═══════════════════════════════════════════════════════════ */

(function () {
  'use strict';

  /* ── Mobile nav toggle ─────────────────────────── */
  const toggle = document.querySelector('.nav-toggle');
  const menu   = document.querySelector('.nav-menu');

  if (toggle && menu) {
    const setOpen = (open) => {
      toggle.classList.toggle('open', open);
      menu.classList.toggle('open', open);
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      document.body.style.overflow = open ? 'hidden' : '';
    };
    toggle.addEventListener('click', () => setOpen(!menu.classList.contains('open')));
    menu.querySelectorAll('a').forEach((a) => a.addEventListener('click', () => setOpen(false)));
    document.addEventListener('keydown', (e) => { if (e.key === 'Escape') setOpen(false); });
  }

  /* ── Sticky nav scroll state ───────────────────── */
  const nav = document.querySelector('.nav');
  if (nav) {
    let ticking = false;
    const onScroll = () => {
      nav.classList.toggle('scrolled', window.scrollY > 24);
      ticking = false;
    };
    window.addEventListener('scroll', () => {
      if (!ticking) {
        window.requestAnimationFrame(onScroll);
        ticking = true;
      }
    }, { passive: true });
    onScroll();
  }

  /* ── Scroll reveal ─────────────────────────────── */
  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const targets = document.querySelectorAll('.reveal');

  if (!reduce && 'IntersectionObserver' in window && targets.length) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -8% 0px' });
    targets.forEach((el) => io.observe(el));
  } else {
    targets.forEach((el) => el.classList.add('is-visible'));
  }

  /* ── Form submit: thank-you URL + loading state ── */
  document.querySelectorAll('form[action*="formsubmit.co"]').forEach((form) => {
    const next = form.querySelector('input[name="_next"]');
    if (next) {
      // Resolve relative to the current page so GitHub Pages and a future
      // apex domain (site served from /) both land on this site's thank-you.
      next.value = new URL('thank-you', window.location.href).href;
    }
    form.addEventListener('submit', () => {
      const btn = form.querySelector('button[type="submit"], .btn');
      if (btn) {
        btn.disabled = true;
        btn.dataset.originalText = btn.textContent;
        btn.textContent = 'Sending…';
      }
    });
  });

  /* ── Smooth focus for in-page anchors ──────────── */
  document.querySelectorAll('a[href^="#"]').forEach((a) => {
    a.addEventListener('click', (e) => {
      const id = a.getAttribute('href').slice(1);
      const target = id && document.getElementById(id);
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth', block: 'start' });
        target.setAttribute('tabindex', '-1');
        target.focus({ preventScroll: true });
      }
    });
  });
})();
