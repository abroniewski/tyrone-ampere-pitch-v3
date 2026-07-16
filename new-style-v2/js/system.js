(() => {
  'use strict';
  // Lightbox + LinkedIn carousel helpers for system proof embeds.
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
  if (carousel) {
    carousel.scrollBy({
      left: direction * 220,
      behavior: window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth',
    });
  }
}
