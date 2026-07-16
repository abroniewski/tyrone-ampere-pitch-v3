# Live Site Extraction — Ampere Alliance

Captured **2026-07-16** from public theme assets at [amperealliance.ca](https://amperealliance.ca/).

Machine-readable version: `live-site-extraction.json`. Browser validation: `manual-capture.json`.

## Navigation selectors (confirmed)

| Mode | Selector | Breakpoint |
|---|---|---|
| Desktop nav link | `header nav ul.f--navigation a` | 1024px and above |
| Mobile menu trigger | `header .menu` | below 1024px |
| Mobile nav panel | `header nav.active` | full-screen overlay when open |
| Mobile nav link | `header nav ul.f--navigation a` | 20px / weight 400 (menu must be open) |

Desktop nav: **12px**, weight **500**, uppercase. Mobile nav: **~20px**, weight **400**, uppercase, centered with arrow cue, `#737373` item borders.

## Fonts

| Item | Value |
|---|---|
| Family | **General Sans** (Indian Type Foundry) |
| CSS alias | `"G"` |
| Weights in use | 300 Light, 400 Regular, 500 Medium |
| Files | `GeneralSans-Light.woff2`, `GeneralSans-Regular.woff2`, `GeneralSans-Medium.woff2` |
| Stack | `"G", Helvetica, Arial, sans-serif` |

Font files are preloaded from:

`https://amperealliance.ca/wp-content/themes/theme/assets/fonts/`

**License note:** Do not copy these files into the pitch kit without a valid license. Request approved webfont files from Ampere or the font licensor.

## Type sizing system

The live site does **not** use rem/clamp tokens. It uses a fluid artboard formula:

```css
font-size: calc(N / var(--size) * var(--size-end));
```

| Breakpoint | `--size` | `--size-end` |
|---|---:|---|
| Default desktop | 1440 | `100vw` |
| `min-width: 1800px` | 1440 | `1800px` |
| `max-width: 1199px` | 1200 | `100vw` |
| `max-width: 1023px` | 1024 | `100vw` |
| `max-width: 767px` | 392 | `100vw` |

### Official type classes

`N` is the design-pixel value at the active `--size` artboard.

| Class | Weight | N (px) | Line height | Notes |
|---|---|---:|---|---|
| `.f--h1` | 300 | 100 | 95% | Mobile N = 60 |
| `.f--h1-small` | 300 | 62 | 110% | Mobile N = 30 |
| `.f--h2` | 400 | 15 | 100% | Uppercase, silver |
| `.f--h3` | 300 | 100 | 120% | Scales to 80 / 60 / 40 |
| `.f--h3-small` | 300 | 48 | 110% | Mobile N = 40 |
| `.f--h4` | 300 | 30 | 110% | Scales to 24 / 22 |
| `.f--navigation` | 500 | 12 | 110% | Uppercase white |
| `.f--p` | 400 | 16 | 140% | Silver body |
| `.f--p-small` | 400 | 14 | 140% | Silver |
| `.f--callout` | 300 | 48 | 110% | Mobile N = 28 |
| `.f--testimonial` | 300 | 30 | 110% | Mobile N = 22 |
| `.f--tag` | 400 | 15 | — | Uppercase silver |
| `body` | 400 | 16 | — | White on black |

At a **1440px** viewport, N equals rendered px (for example `.f--h1` = 100px). At **1800px**, sizes cap through `--size-end: 1800px` (for example `.f--h1` ≈ 125px).

## Colors observed in theme CSS

| Token / use | Hex |
|---|---|
| Page background | `#000000` |
| Body text | `#FFFFFF` |
| Secondary text (`--silver`) | `#C2C2C2` |
| Accent blue (buttons, borders, bullets) | `#3D6DFF` |
| Meta theme-color | `#0340F8` |
| Muted gray | `#737373` |
| Light border | `#EEEEEE` |

## Motion and animation

### Libraries

- **Lenis** — smooth scroll (`duration: 1.2`)
- **Splitting.js** — per-character and per-line text reveals
- **Alpine.js** — parallax, marquee, accordion, global state
- **Splide** — carousels
- **InfiniteMarquee** — horizontal/vertical marquees
- **countUp.js** — statistic counters (`duration: 5s`)

### Scroll reveal pattern

1. Elements start with utility classes such as `.t--fade`, `.t--fadedown`, `.t--fadeline`.
2. `IntersectionObserver` adds `.inview` when the element crosses the viewport (`rootMargin: -100px`).
3. CSS keyframes run once.

### Key easing curves

| Name | Value | Typical use |
|---|---|---|
| Reveal primary | `cubic-bezier(0.4, 0.5, 0, 1)` | Char/line reveals, headline accents |
| Reveal secondary | `cubic-bezier(0.25, 0.1, 0.25, 1)` | Fade/slide utilities |
| UI | `ease` / `0.25s` | Buttons, nav, opacity |

### Key durations

| Duration | Use |
|---:|---|
| 250ms | Hover, page transition, UI opacity |
| 500ms | Accordion max-height |
| 1000ms | Fade/slide utilities, headline accents |
| 1200ms | Splitting char and line reveals |
| 1500ms | `.t--fadeline`, headline rule width |
| 5000ms | Count-up statistics |

### Text splitting stagger

- **Characters:** `animation-delay: calc(var(--char-index) * 0.01s)`
- **Lines:** `animation-delay: calc(var(--line-index) * 0.25s)`

### Marquee

Alpine `marquee` component wraps `InfiniteMarquee` with:

- `duplicateCount: 2`
- `pauseOnHover: true`
- `speed: 1500 * multiplier`

### Parallax

`data-power` on parallax elements controls scroll-linked `translateY`.

### Header behavior

- Adds `.scroll` after `scrollY > 50`
- Adds `.off` while scrolling down, removes on scroll up

### Page transitions

Internal links add `.animate-out` (250ms opacity fade) before navigation.

## Manual capture template

If you need to refresh or extend this extraction, drop a file named `manual-capture.md` in this folder using the template below. An agent can parse it and merge updates.

```markdown
# Manual capture

- Date:
- Page URL:
- Viewport width:
- Capture method: DevTools computed styles / screen recording / Figma inspect

## Fonts
- Computed font-family:
- Computed font-weight:
- Computed font-size:
- Computed line-height:
- Computed letter-spacing:

## Element notes
### Hero headline
- Selector or screenshot ref:
- font-size:
- line-height:
- animation observed:

### Navigation
- font-size:
- hover behavior:

## Motion recording notes
- Scroll reveal delay:
- Stagger estimate:
- Easing feel: mechanical / soft / bouncy
- Reduced-motion behavior:

## Colors (eyedropper)
- Background:
- Primary text:
- Accent:
```

### Fast browser workflow

1. Open the page in Chrome.
2. DevTools → **Sources** → search for `global.css` or `GeneralSans`.
3. **Computed** tab on hero `h1`, nav links, and body copy.
4. **Animations** panel while scrolling to confirm trigger timing.
5. Optional: use [WhatFont](https://chrome.google.com/webstore) or DevTools **Rendering → Emulate prefers-reduced-motion** for accessibility checks.
6. Save screenshots at 1440, 1024, and 390 widths into a private working folder (not this repo unless approved).
