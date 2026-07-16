(() => {
  'use strict';

  const root = document.documentElement;
  const body = document.body;
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  const preloader = document.querySelector('.preloader');
  const finishLoading = () => {
    if (!preloader) {
      body.classList.remove('is-loading');
      return;
    }
    window.setTimeout(() => {
      preloader.classList.add('is-complete');
      body.classList.remove('is-loading');
    }, reducedMotion ? 0 : 900);
  };

  if (document.readyState === 'complete') finishLoading();
  else window.addEventListener('load', finishLoading, { once: true });

  const header = document.querySelector('.site-header');
  let lastY = window.scrollY;
  const onScroll = () => {
    if (!header) return;
    const y = window.scrollY;
    header.classList.toggle('is-scrolled', y > 50);
    if (!reducedMotion) {
      if (y > 80 && y > lastY) header.classList.add('is-off');
      else header.classList.remove('is-off');
    }
    lastY = y;
    root.style.setProperty('--scroll-y', `${y}px`);
  };
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  const menuToggle = document.querySelector('[data-menu-toggle]');
  const mobileMenu = document.querySelector('[data-mobile-menu]');
  const setMenu = (open) => {
    if (!menuToggle || !mobileMenu) return;
    body.classList.toggle('menu-open', open);
    mobileMenu.classList.toggle('is-open', open);
    menuToggle.setAttribute('aria-expanded', String(open));
    mobileMenu.setAttribute('aria-hidden', String(!open));
  };

  menuToggle?.addEventListener('click', () => setMenu(!body.classList.contains('menu-open')));
  mobileMenu?.querySelectorAll('a').forEach((link) => link.addEventListener('click', () => setMenu(false)));
  window.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') setMenu(false);
  });

  const revealItems = document.querySelectorAll('[data-reveal], [data-clip-reveal]');
  if (reducedMotion || !('IntersectionObserver' in window)) {
    revealItems.forEach((item) => item.classList.add('is-visible'));
  } else {
    const revealObserver = new IntersectionObserver((entries, observer) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add('is-visible');
        observer.unobserve(entry.target);
      });
    }, { threshold: 0.12, rootMargin: '-100px 0px 0px 0px' });
    revealItems.forEach((item) => revealObserver.observe(item));
  }
})();
