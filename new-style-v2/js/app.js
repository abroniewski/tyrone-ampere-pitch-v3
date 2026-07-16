(() => {
  'use strict';

  const root = document.documentElement;
  const body = document.body;
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  const preloader = document.querySelector('.preloader');
  let loadingFinished = false;
  const finishLoading = () => {
    if (loadingFinished) return;
    loadingFinished = true;
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
  else {
    window.addEventListener('load', finishLoading, { once: true });
    // Don't wait forever on third-party embeds (Loom, etc.)
    window.setTimeout(finishLoading, reducedMotion ? 0 : 1800);
  }

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

  /* ---------- peek-carousel ---------- */
  document.querySelectorAll('[data-peek-carousel]').forEach((carousel) => {
    const track = carousel.querySelector('.peek-carousel__track');
    const prev = carousel.querySelector('[data-peek-prev]');
    const next = carousel.querySelector('[data-peek-next]');
    if (!track) return;

    const cardStep = () => {
      const card = track.querySelector('.peek-carousel__card');
      if (!card) return track.clientWidth * 0.8;
      const style = getComputedStyle(track);
      const gap = parseFloat(style.columnGap || style.gap || '0') || 0;
      return card.getBoundingClientRect().width + gap;
    };

    const scrollByCard = (dir) => {
      track.scrollBy({
        left: dir * cardStep(),
        behavior: reducedMotion ? 'auto' : 'smooth',
      });
    };

    prev?.addEventListener('click', () => scrollByCard(-1));
    next?.addEventListener('click', () => scrollByCard(1));
  });

  /* ---------- metric-accordion ---------- */
  const accordions = document.querySelectorAll('[data-metric-accordion]');

  const setItemOpen = (accordion, item, open) => {
    const toggle = item.querySelector('.metric-accordion__toggle');
    const panel = item.querySelector('.metric-accordion__panel');
    item.classList.toggle('is-open', open);
    if (toggle) {
      toggle.setAttribute('aria-expanded', String(open));
      toggle.textContent = open ? 'Read less −' : 'Read more +';
    }
    if (panel) panel.hidden = !open;
  };

  accordions.forEach((accordion) => {
    const items = Array.from(accordion.querySelectorAll('.metric-accordion__item'));
    items.forEach((item) => {
      const toggle = item.querySelector('.metric-accordion__toggle');
      const panel = item.querySelector('.metric-accordion__panel');
      const openByDefault = item.hasAttribute('data-open');
      if (panel) panel.hidden = !openByDefault;
      setItemOpen(accordion, item, openByDefault);

      const activate = () => {
        const willOpen = !item.classList.contains('is-open');
        items.forEach((other) => setItemOpen(accordion, other, other === item && willOpen));
      };

      toggle?.addEventListener('click', (event) => {
        event.stopPropagation();
        activate();
      });
      item.querySelector('.metric-accordion__row')?.addEventListener('click', (event) => {
        if (event.target.closest('a, button')) return;
        activate();
      });
    });
  });

  window.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') {
      setMenu(false);
      accordions.forEach((accordion) => {
        accordion.querySelectorAll('.metric-accordion__item.is-open').forEach((item) => {
          setItemOpen(accordion, item, false);
        });
      });
    }
  });
})();
