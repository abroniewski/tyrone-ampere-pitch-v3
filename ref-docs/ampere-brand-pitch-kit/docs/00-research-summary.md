# 00. Research Summary

## Objective

Reconstruct the Ampere Alliance design language closely enough to create new, on-brand marketing pages without copying the official site's source code or reusing protected assets without approval.

## Research inputs

### Official current site

- Homepage: https://amperealliance.ca/
- About: https://amperealliance.ca/about-us/
- Approach: https://amperealliance.ca/approach/
- Portfolio: https://amperealliance.ca/portfolio/
- Insights: https://amperealliance.ca/insights/
- Careers: https://amperealliance.ca/careers/
- Contact: https://amperealliance.ca/contact/

The current public architecture is therefore treated as:

1. Home
2. About Us
3. Approach
4. Portfolio
5. Insights
6. Careers
7. Contact

The official site title and indexed positioning establish a next-generation power, elite-collective, and exponential-growth frame.

### Original design agency case study

- Agency: AT THE LAB
- Case study: https://www.atthelab.ca/project/amp
- Project year shown by agency: 2023
- Scope shown by agency: brand and website

The agency case study provides high-value visual evidence for:

- Near-black foundation.
- Electric cobalt accent.
- White and icy blue-gray support fields.
- Thin neo-grotesk display typography.
- Compact navigation and metadata.
- Triangular bullets and directional cues.
- Sharp, asymmetrical polygon masks.
- Blue monochrome imagery.
- Large, thin statistics.
- Minimal wordmark treatment.

## Research constraint

The official site previously served an automated verification loader to some research environments. On **2026-07-16**, public theme assets (`global.css`, `app.js`, font preloads) were successfully retrieved from [amperealliance.ca](https://amperealliance.ca/) without copying licensed font files.

Confirmed from live theme assets and Playwright browser validation:

- **Font family:** General Sans (300, 400, 500).
- **Sizing system:** `calc(N / var(--size) * var(--size-end))` with artboard references at 1440, 1200, 1024, and 392.
- **Navigation:** desktop `header nav ul.f--navigation a` (12px/500); mobile overlay via `header .menu` → `header nav.active` (20px/400).
- **Motion stack:** Lenis, Splitting.js, Alpine.js, Splide, InfiniteMarquee, countUp.js.
- **Primary accent in CSS:** `#3D6DFF` (meta theme-color `#0340F8`).
- **Secondary text:** `#C2C2C2` (browser-validated on body copy).

Still requiring approval or direct visual comparison:

- Licensed General Sans files for redistribution.
- Official logo masters and clear-space rules.
- Whether `#0340F8` or `#3D6DFF` is the canonical brand cobalt.
- Exact homepage section order and photography treatment.
- Reduced-motion behavior on the production site.

See `reference/live-site-extraction.json` and `reference/manual-capture.json` for the full machine-readable capture.

## Reconstruction method

This kit combines three layers:

1. **Observed**: elements clearly visible in public agency case-study imagery or indexed official page structure.
2. **Inferred**: implementation values derived from proportions, pixel sampling, and repeated visual patterns.
3. **Original**: new code, pitch copy, SVG artwork, responsive behavior, and accessibility improvements.

## Measured visual findings

Public case-study imagery was sampled for representative colors. The working palette is:

- Ink: `#050505`
- Electric cobalt: `#063CFF`
- Mist: `#E3E9F1`
- Silver: `#B9C4D8`

The case imagery also contains a gradient range from deep cobalt through muted blue into cool silver.

## Strategic page logic

A useful Ampere-style page behaves like a current moving through a circuit:

1. A decisive, oversized opening statement.
2. A compact strategic explanation.
3. Numbered proof or process blocks.
4. A high-contrast image or case-study interruption.
5. A large statistic or quote.
6. A single strong conversion action.

## What not to claim as exact

Until approved source assets or direct screenshots are available, do not describe these as official values:

- Licensed font files for redistribution (family name is confirmed; files are not bundled).
- Exact logo clear-space rules.
- Canonical cobalt hex between `#0340F8` and `#3D6DFF`.
- Exact homepage section order inside the current homepage.
- Reduced-motion behavior on the production site.

See `13-fidelity-matrix.md` for confidence levels and `14-calibration-protocol.md` for the final adjustment process.
