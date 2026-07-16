# 02. Typography

## Observed character

The public case-study work uses a clean neo-grotesk with a very light display weight. Letterforms are neutral, open, and modern. The exact licensed typeface could not be confirmed.

## Production font strategy

### Best fidelity candidates

Use only with a valid license:

- Neue Haas Grotesk Display.
- Helvetica Neue.
- Suisse Int'l.
- Neue Montreal.
- Aktiv Grotesk.

### Free or system-safe working candidates

- Inter Tight.
- Inter.
- Archivo.
- Arial or Nimbus Sans L as a final fallback.

This package uses:

```css
--font-display: "Helvetica Neue", "Nimbus Sans L", Helvetica, Arial, sans-serif;
--font-body: Inter, "Helvetica Neue", Helvetica, Arial, sans-serif;
```

No font files are bundled.

## Weight hierarchy

- Hero and major headlines: 200 to 300.
- Section headlines: 300.
- Body: 400.
- Labels and navigation: 500.
- Bold should be rare and reserved for a compact wordmark, proof label, or urgent data point.

## Type scale

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

## Display rules

- Line height: 0.90 to 1.02.
- Tracking: negative 0.025em to negative 0.055em.
- Sentence case over all caps.
- Deliberately author line breaks in hero copy.
- Keep the main hero between three and five lines.
- Avoid a last line containing only a short article or preposition.
- Use periods selectively. A final period adds confidence to a major statement.

## Body rules

- Line height: 1.45 to 1.60.
- Measure: 45 to 70 characters per line.
- Paragraphs: one to four sentences.
- Keep text blocks narrow inside large compositions.

## Labels

Labels use:

- Uppercase.
- 0.06em to 0.10em letter spacing.
- 10 to 12 pixel visual size.
- Optional number prefix, for example `03 / CAMPAIGN DIRECTIONS`.
- Optional triangle cue.

## Numeric typography

Large statistics use the display face at the lightest practical weight. Use tight tracking and no decorative containers. Numbers may occupy 30 to 60 percent of a card.

## Font calibration checklist

When the approved font is received:

1. Compare lowercase `a`, `g`, and `t`.
2. Compare numeral width and the shape of `1`, `3`, and `7`.
3. Recheck hero line breaks at 1440, 1280, 1024, 768, and 390 pixels.
4. Adjust `--tracking-tight` before changing font size.
5. Check button width and navigation spacing.
6. Recheck all clipping at 200 percent zoom.
