# 07. Motion System

## Motion character

Motion should feel controlled, directional, and mechanical. It should not feel bouncy, playful, or ornamental.

The live site at [amperealliance.ca](https://amperealliance.ca/) confirms this through Lenis smooth scrolling, Splitting.js text reveals, and CSS keyframe utilities triggered by an `inview` class.

Full extraction: `reference/live-site-extraction.json`.

## Official libraries

| Library | Role |
|---|---|
| Lenis | Smooth scroll (`duration: 1.2`) |
| Splitting.js | Per-character and per-line headline reveals |
| Alpine.js | Parallax, marquee, accordion, menu state |
| Splide | Carousels and testimonial sliders |
| InfiniteMarquee | Horizontal and vertical marquees |
| countUp.js | Statistic counters (`duration: 5s`) |

## Core easing

### Live-site reveal primary

```css
cubic-bezier(0.4, 0.5, 0, 1)
```

Use for:

- Character reveals (`down` keyframe, 1.2s).
- Line reveals (`fadedown` keyframe, 1.2s).
- `.t--fadeline` (1.5s).
- Headline accent transitions (1s to 1.5s).

### Live-site reveal secondary

```css
cubic-bezier(0.25, 0.1, 0.25, 1)
```

Use for:

- `.t--fade`, `.t--fadedown`, `.t--fadeup`, `.t--fadeleft`, `.t--faderight`.
- Width animations.
- Delayed headline right-column reveal (`1s` with `0.25s` delay).

### Pitch-kit working reveal easing

```css
cubic-bezier(0.16, 1, 0.3, 1)
```

Retained in the prototype for card fills and large clip reveals where the live CSS uses the curves above.

### Page-state easing

```css
cubic-bezier(0.76, 0, 0.24, 1)
```

Use for:

- Full-screen menu.
- Major state transitions in the pitch prototype.

### UI easing

```css
ease
```

Use for:

- 250ms opacity and background transitions.
- Page enter (`.animate-in`, 0.25s ease-in).
- Page exit (`.animate-out`, 250ms opacity).

## Timing scale

| Token | Official duration | Pitch-kit duration | Use |
|---|---:|---:|---|
| UI | 250 ms | 180 ms | Opacity, hover, page transition |
| Fade utilities | 1000 ms | 420 ms | `.t--fade*` inview reveals |
| Char / line reveal | 1200 ms | 1100 ms | Splitting headlines |
| Fadeline | 1500 ms | — | Line mask reveal |
| Headline rule | 1500 ms | — | Section headline underline |
| Accordion | 500 ms | — | `max-height` transition |
| Count-up | 5000 ms | — | Statistics |
| Card fill (prototype) | — | 650 ms | Cobalt card hover |

## Scroll and in-view behavior

### Lenis

```js
{
  duration: 1.2,
  easing: t => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
  smoothWheel: true,
  smoothTouch: false
}
```

### IntersectionObserver

- Adds `.inview` once.
- `rootMargin: -100px`.
- Child stagger for grouped counters: `index / 8` seconds.

## Text splitting

### Characters (`[data-splitting]`)

- Initial: `translateY(110%)`.
- In view: `down` animation, 1.2s, primary easing.
- Stagger: `calc(var(--char-index) * 0.01s)` — **10ms per character** (browser-validated).

### Lines (`[data-splitting=lines]`)

- Initial: `translateY(102%)`, `opacity: 0`.
- In view: `fadedown` animation, 1.2s, primary easing.
- Stagger: `calc(var(--line-index) * 0.25s)`.

## Utility reveal classes

Initial state classes:

- `.t--fade` — opacity only.
- `.t--fadedown` — `translateY(50px)`, opacity 0.
- `.t--fadeline` — `translateY(105%)`.
- `.t--fadeup` — `translateY(-50px)`, opacity 0.
- `.t--fadeleft` / `.t--faderight` — horizontal 25px offset.

Delay utilities: `.t--delay_250` through `.t--delay_2500` in 250ms steps.

## Page-load sequence

Recommended order (aligned with live site behavior):

1. Black canvas appears immediately.
2. Hero headline characters or lines rise via Splitting.
3. Supporting copy uses `.t--fade` or `.t--fadedown` utilities.
4. Section headlines animate left icon, rule width, and right label on `.inview`.
5. Hero or background media may use parallax.

Do not add a logo spin, percentage counter preloader, or audio.

## Scroll reveal

Default on live site:

- Trigger via `.inview` class.
- Fade/slide distance: 25 to 50px depending on utility.
- Duration: 1000 to 1500ms.
- Observer margin: `-100px`.
- Stop observing after first reveal.

Large headlines use Splitting vertical clip rather than a simple fade.

## Hover states

### Live-site buttons and controls

- 250ms opacity or background transitions.
- Accent hover fill: `#3D6DFF`.
- Slider nav buttons reveal a circular `#3D6DFF` fill on hover (desktop only, `min-width: 1025px`).

### Pitch-kit prototype additions

These remain valid interaction targets but were inferred from the agency case study rather than copied CSS:

- White fill rising from the bottom on primary buttons.
- Cobalt card fill from the bottom over ~650ms.
- Portfolio row cobalt sweep from the left.
- Media scale 3 to 6 percent over 900 to 1200ms.

## Marquee

- Component: `InfiniteMarquee` via Alpine `marquee` data.
- Linear infinite animation using `--_speed`.
- Default `duplicateCount: 2`.
- `pauseOnHover: true`.
- Speed formula in app.js: `1500 * multiplier`.

## Parallax

- Alpine `parallax` component.
- `data-power` attribute controls intensity.
- Scroll-linked `translateY` on large media or background shapes.
- Disable on reduced-motion settings.

## Header behavior (live site)

- Adds `.scroll` after `scrollY > 50`.
- Adds `.off` while scrolling down; removes on scroll up.

## Page transitions (live site)

Internal navigation:

1. Add `.animate-out` to `body`.
2. Wait 250ms.
3. Navigate.

## Mobile motion

Reduce layers and travel distance. Keep:

- Headline line or character reveal.
- Menu transition.
- Simple `.inview` fade utilities.

Remove or minimize:

- Magnetic buttons (prototype only).
- Strong parallax.
- Cursor effects.
- Complex pinned sequences.

Below `1023px`, `fadeleft` keyframes switch to a vertical `translateY(25px)` entrance.

## Reduced motion

The pitch-kit CSS and JavaScript detect `prefers-reduced-motion: reduce` and:

- Remove transition duration.
- Stop parallax.
- Stop marquee movement.
- Reveal content immediately.
- Preserve all content and interaction states.

Confirm live-site reduced-motion behavior separately before claiming pixel parity.

## Animation budget

At any moment, aim for no more than:

- One large continuous background motion.
- One active reveal sequence.
- One user-triggered hover or menu transition.

More simultaneous motion turns precision into visual static.
