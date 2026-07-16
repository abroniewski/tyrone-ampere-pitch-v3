# 02. Typography

## Confirmed live-site font

The current public site at [amperealliance.ca](https://amperealliance.ca/) loads **General Sans** from the theme as three WOFF2 cuts:

| Weight | File |
|---:|---|
| 300 | `GeneralSans-Light.woff2` |
| 400 | `GeneralSans-Regular.woff2` |
| 500 | `GeneralSans-Medium.woff2` |

The theme registers the family under the CSS alias `"G"`:

```css
font-family: "G", Helvetica, Arial, sans-serif;
```

Full extraction: `reference/live-site-extraction.json`.

**License note:** General Sans is a commercial family (Indian Type Foundry). Do not bundle or hotlink production font files without a valid license.

## Observed character

General Sans is a clean neo-grotesk. Display sizes use weight 300. Navigation and labels use 500. Body copy uses 400. The earlier pitch-kit assumption of Helvetica Neue / Inter was a fallback only.

## Production font strategy

### Primary (confirmed on live site)

- **General Sans** — Light 300, Regular 400, Medium 500.

### Fallback stack for prototypes without licensed files

- Inter.
- Helvetica Neue.
- Arial or Nimbus Sans L.

This package's CSS still ships fallback stacks in `assets/css/tokens.css` because font files are not bundled.

## Official sizing system

The live site does **not** use the pitch kit's `clamp()` tokens directly. It scales from artboard values:

```css
font-size: calc(N / var(--size) * var(--size-end));
```

| Breakpoint | `--size` | `--size-end` |
|---|---:|---|
| Default | 1440 | `100vw` |
| `min-width: 1800px` | 1440 | `1800px` |
| `max-width: 1199px` | 1200 | `100vw` |
| `max-width: 1023px` | 1024 | `100vw` |
| `max-width: 767px` | 392 | `100vw` |

### Official type classes

At a 1440px viewport, rendered size equals `N`.

| Class | Weight | N (px) | Line height | Notes |
|---|---|---:|---|---|
| `.f--h1` | 300 | 100 | 95% | Mobile N = 60 |
| `.f--h1-small` | 300 | 62 | 110% | Mobile N = 30 |
| `.f--h2` | 400 | 15 | 100% | Uppercase, silver |
| `.f--h3` | 300 | 100 | 120% | Scales to 80 / 60 / 40 |
| `.f--h3-small` | 300 | 48 | 110% | Mobile N = 40 |
| `.f--h4` | 300 | 30 | 110% | Scales to 24 / 22 |
| `.f--navigation` | 500 | 12 | 110% | Uppercase white (desktop inline) |
| `.f--navigation` mobile overlay | 400 | 20 | 110% | Uppercase white; rule applies below 1024px |
| `.f--p` | 400 | 16 | 140% | Silver body |
| `.f--p-small` | 400 | 14 | 140% | Silver |
| `.f--callout` | 300 | 48 | 110% | Mobile N = 28 |
| `.f--testimonial` | 300 | 30 | 110% | Mobile N = 22 |
| `.f--tag` | 400 | 15 | — | Uppercase silver |

### Browser-validated computed sizes

Captured with Playwright Chromium (`reference/manual-capture.json`):

| Viewport | Element | Size | Weight |
|---:|---|---:|---:|
| 1440 | Hero `h1.f--h1` | 100px / 95px lh | 300 |
| 1440 | Nav link | 12px | 500 |
| 1440 | Body `.f--p` | 16px / 22.4px lh | 400 |
| 1024 | Hero `h1.f--h1` | 85.33px | 300 |
| 390 | Hero `h1.f--h1` | 59.69px | 300 |
| 390 | Nav link (menu open) | 19.90px | 400 |

## Navigation selectors

| Mode | Selector | Notes |
|---|---|---|
| Desktop link | `header nav ul.f--navigation a` | Visible at 1024px+ |
| Mobile trigger | `header .menu` | Opens overlay |
| Mobile panel | `header nav.active` | Full-screen black overlay |
| Mobile link | `header nav ul.f--navigation a` | Same selector; menu must be open to measure |

## Pitch-kit working scale

The included prototype still uses rem/clamp tokens for convenience. Map them to the official classes during calibration:

| Pitch token | Approximate official class |
|---|---|
| `--type-hero` | `.f--h1` / `.f--h3` |
| `--type-display` | `.f--h1-small` / `.f--callout` |
| `--type-h1` | `.f--h4` at large interior headlines |
| `--type-h2` | `.f--testimonial` |
| `--type-h3` | `.f--h4` |
| `--type-body-lg` | between `.f--p` and `.f--callout` |
| `--type-body` | `.f--p` |
| `--type-small` | `.f--p-small` |
| `--type-micro` | `.f--navigation` |

| Token | Use | Working value |
|---|---|---|
| `--type-hero` | Homepage hero | `clamp(3.5rem, 7vw, 8.4rem)` |
| `--type-display` | Manifesto statement | `clamp(2.9rem, 5.5vw, 6.5rem)` |
| `--type-h1` | Interior page headline | `clamp(2.6rem, 4.5vw, 5.6rem)` |
| `--type-h2` | Section headline | `clamp(2.15rem, 3.6vw, 4.5rem)` |
| `--type-h3` | Card headline | `clamp(1.45rem, 2.2vw, 2.6rem)` |
| `--type-body-lg` | Strategic introduction | `clamp(1.08rem, 1.35vw, 1.35rem)` |
| `--type-body` | Standard copy | `1rem` |
| `--type-small` | Card copy and metadata | `0.78rem` |
| `--type-micro` | Labels and coordinates | `0.68rem` |

## Weight hierarchy

- Hero and major headlines: 300.
- Section labels (`.f--h2`, `.f--tag`): 400.
- Body: 400.
- Navigation: 500.
- Bold should remain rare outside emphasis inside `.f--h2 strong` or footer metadata.

## Display rules

- Line height: 0.95 to 1.2 on live site display classes.
- The live site relies on line splitting more than negative tracking.
- Sentence case over all caps for headlines.
- Deliberately author line breaks in hero copy.
- Keep the main hero between three and five lines.
- Avoid a last line containing only a short article or preposition.
- Use periods selectively. A final period adds confidence to a major statement.

## Body rules

- Line height: 1.4 on `.f--p` and `.f--p-small`.
- Measure: 45 to 70 characters per line.
- Paragraphs: one to four sentences.
- Keep text blocks narrow inside large compositions.

## Labels

Labels use:

- Uppercase.
- 12 to 15px rendered size on desktop.
- Silver (`#C2C2C2`) on dark fields.
- Optional number prefix, for example `(01)`.
- Optional triangle or dot cue (`#3D6DFF` on live site marquees).

## Numeric typography

Large statistics use General Sans at weight 300. Count-up animation runs over 5 seconds when `.inview` triggers.

## Font calibration checklist

When licensed General Sans files are received:

1. Compare lowercase `a`, `g`, and `t` against live site screenshots.
2. Compare numeral width and the shape of `1`, `3`, and `7`.
3. Recheck hero line breaks at 1800, 1440, 1200, 1024, and 392 pixels.
4. Replace clamp tokens with the official `calc(N / var(--size) * var(--size-end))` system if pixel-matching is required.
5. Check button width and navigation spacing.
6. Recheck all clipping at 200 percent zoom.
