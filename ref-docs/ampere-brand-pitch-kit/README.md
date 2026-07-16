# Ampere Brand Pitch Kit

An unofficial, brand-faithful website system for pitching Ampere Alliance with new content while preserving the recognizable visual language found in public Ampere materials.

## Start here

1. Open `index.html` directly, or run a local server from this folder:

   ```bash
   python3 -m http.server 8000
   ```

2. Visit `http://localhost:8000`.
3. Open `style-guide.html` for the component gallery.
4. Read `docs/00-research-summary.md` before changing tokens.
5. Replace the concept mark and abstract imagery only after receiving approved brand assets.

## What is included

- Responsive one-page pitch homepage.
- Page shells for About, Approach, Portfolio, Insights, Careers, and Contact.
- Reusable CSS token, layout, component, and motion system.
- Dependency-free JavaScript for navigation, reveals, parallax, magnetic actions, and counters.
- Original abstract SVG artwork and a clearly labeled concept mark.
- Desktop, mobile, and style-guide previews.
- Detailed brand, component, motion, content, implementation, accessibility, and rights documentation.
- JSON registries for design tokens, components, content models, and required assets.

## Important fidelity note

The official site presented an automated-access challenge during research. The package therefore combines:

- High-confidence current information architecture and messaging patterns from indexed official pages.
- High-confidence identity details from the original design agency's public Ampere case study.
- Original implementation and artwork built from those observations.
- Clearly marked calibration items for exact current font files, logo masters, color specifications, and motion timings.

This is not a source-code copy and does not contain the official website's proprietary code.

## Rights boundary

The package does not bundle official Ampere logo masters, portfolio-company logos, leadership portraits, website photography, videos, or copied page copy. Those items should be supplied or approved by Ampere before public use. See `docs/12-rights-and-usage.md`.

## Key files

- `index.html`: pitch homepage.
- `style-guide.html`: live component and token gallery.
- `assets/css/tokens.css`: primary design controls.
- `assets/css/components.css`: component implementation.
- `assets/js/app.js`: interaction layer.
- `data/design-tokens.json`: machine-readable token map.
- `data/asset-manifest.json`: full production asset checklist.
- `data/fidelity-matrix.json`: machine-readable confidence and calibration map.
- `docs/13-fidelity-matrix.md`: what is observed, inferred, or still needs approval.
- `docs/14-calibration-protocol.md`: final pixel-calibration process.
- `PACKAGE-INDEX.md`: guided map of the full handoff.
- `NOTICE.md`: concise rights and prototype notice.

## Content replacement

All prototype copy is original pitch copy. Search for `Pitch concept`, `Member Company`, `Leader Name`, and `Role Title` to find the main replacement points.
