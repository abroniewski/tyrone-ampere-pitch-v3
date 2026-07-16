(() => {
  'use strict';

  const loop = document.getElementById('interactiveLoop');
  if (!loop) return;

  const tabs = Array.prototype.slice.call(loop.querySelectorAll('.loop-node'));
  const panels = Array.prototype.slice.call(loop.querySelectorAll('.stage-panel'));

  function updateConnector(tab) {
    const loopRect = loop.getBoundingClientRect();
    const tabRect = tab.getBoundingClientRect();
    const center = tabRect.left - loopRect.left + (tabRect.width / 2);
    loop.style.setProperty('--active-x', `${center}px`);
  }

  function selectStage(tab, moveFocus) {
    const stage = tab.getAttribute('data-stage');

    tabs.forEach((item) => {
      const selected = item === tab;
      item.classList.toggle('active', selected);
      item.setAttribute('aria-selected', selected ? 'true' : 'false');
      item.setAttribute('tabindex', selected ? '0' : '-1');
      const action = item.querySelector('.node-action');
      if (action) action.textContent = selected ? 'Open now' : 'Open stage';
    });

    panels.forEach((panel) => {
      const selected = panel.getAttribute('data-panel') === stage;
      panel.hidden = !selected;
      panel.classList.toggle('active', selected);
    });

    updateConnector(tab);
    if (moveFocus) tab.focus();
  }

  tabs.forEach((tab, index) => {
    tab.addEventListener('click', () => selectStage(tab, false));
    tab.addEventListener('keydown', (event) => {
      let nextIndex = index;
      if (event.key === 'ArrowRight' || event.key === 'ArrowDown') nextIndex = (index + 1) % tabs.length;
      if (event.key === 'ArrowLeft' || event.key === 'ArrowUp') nextIndex = (index - 1 + tabs.length) % tabs.length;
      if (event.key === 'Home') nextIndex = 0;
      if (event.key === 'End') nextIndex = tabs.length - 1;
      if (nextIndex !== index) {
        event.preventDefault();
        selectStage(tabs[nextIndex], true);
      }
    });
  });

  function placeConnector() {
    const active = loop.querySelector('.loop-node.active');
    if (active) updateConnector(active);
  }

  window.addEventListener('resize', placeConnector);
  window.addEventListener('load', placeConnector);
  placeConnector();
})();

function openLightbox(src, alt) {
  const overlay = document.getElementById('lightbox');
  const img = document.getElementById('lightboxImg');
  if (!overlay || !img) return;
  img.src = src;
  img.alt = alt || '';
  overlay.classList.add('open');
}

function closeLightbox(event) {
  if (event && event.target && event.target.id === 'lightboxImg') return;
  const overlay = document.getElementById('lightbox');
  const img = document.getElementById('lightboxImg');
  if (!overlay || !img) return;
  overlay.classList.remove('open');
  img.src = '';
}

document.addEventListener('keydown', (event) => {
  if (event.key === 'Escape') {
    const overlay = document.getElementById('lightbox');
    if (overlay) overlay.classList.remove('open');
  }
});

function scrollCarousel(direction) {
  const carousel = document.getElementById('liCarousel');
  if (carousel) carousel.scrollBy({ left: direction * 220, behavior: 'smooth' });
}
