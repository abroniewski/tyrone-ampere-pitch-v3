# 10. Implementation Specification

## Architecture

This starter is dependency-free and uses:

- Semantic HTML.
- CSS custom properties.
- CSS Grid and Flexbox.
- SVG concept art.
- Small vanilla JavaScript modules inside one file.

It can be migrated into Webflow, WordPress, Next.js, Astro, Nuxt, or another component framework without changing the core design logic.

## File structure

```text
ampere-brand-pitch-kit/
  index.html
  style-guide.html
  build_site.py
  pages/
  assets/
    css/
    js/
    svg/
  data/
  docs/
  preview/
  reference/
```

## CSS layer

### `tokens.css`

Controls:

- Color.
- Type scale.
- Font stacks.
- Layout dimensions.
- Motion timing.
- Z-index.

### `base.css`

Controls:

- Reset.
- Global type.
- Grid utilities.
- Themes.
- Reveal primitives.
- Reduced-motion fallback.

### `components.css`

Controls:

- Header and mobile menu.
- Heroes.
- Buttons and links.
- Section headers.
- Cards, rows, stats, forms, CTA, and footer.
- Responsive behavior.

## JavaScript layer

`assets/js/app.js` provides:

- Preloader exit.
- Sticky-header state.
- Full-screen mobile menu.
- Intersection Observer reveals.
- Lightweight parallax.
- Fine-pointer magnetic buttons.
- Number counters.
- Prototype form feedback.

No third-party animation library is required. A production team may replace the motion layer with GSAP or Motion only when a complex pinned narrative is justified.

## Content generation

`build_site.py` contains the current prototype copy and shared header/footer functions. After editing the content:

```bash
python3 build_site.py
```

This regenerates the homepage, style guide, and page shells.

## CMS content models

Use these core types:

1. Page.
2. Portfolio company.
3. Case study.
4. Insight article.
5. Person.
6. Job opening.
7. Testimonial.
8. Statistic.
9. Reusable CTA.

See `data/content-model.json`.

## Recommended component mapping

| Starter component | Framework component |
|---|---|
| `.site-header` | `SiteHeader` |
| `.hero` | `HomeHero` |
| `.page-hero` | `PageHero` |
| `.system-card` | `PillarCard` |
| `.work-card` | `FeatureCard` |
| `.portfolio-row` | `PortfolioIndexRow` |
| `.insight-card` | `InsightRow` |
| `.stat` | `StatCard` |
| `.timeline__item` | `TimelineRow` |
| `.quote-block` | `QuoteFeature` |
| `.cta-panel` | `PrimaryCTA` |

## Image implementation

- Use `<picture>` with AVIF and WebP sources.
- Add explicit width and height.
- Use `object-fit: cover` inside polygon masks.
- Load the hero image eagerly and mark it high priority.
- Lazy-load below-the-fold media.
- Use a separate mobile crop when the subject cannot survive the desktop crop.

## SEO

Every page needs:

- Unique title and description.
- Canonical URL.
- Open Graph image.
- Organization, Article, JobPosting, or Breadcrumb structured data where appropriate.
- Descriptive headings with one logical H1.
- Internal links to related portfolio and insight content.

## Analytics events

Track at minimum:

- Primary CTA clicks.
- Contact form starts and completions.
- Portfolio-company opens.
- Article opens.
- Job opens and applications.
- Video plays.
- Scroll depth at 25, 50, 75, and 90 percent.

Use event names tied to intent, not visual labels.

## Production checklist

1. Replace concept identity assets.
2. Confirm current navigation and page inventory.
3. Load approved font files through the client's hosting or licensed provider.
4. Replace prototype copy.
5. Connect CMS collections.
6. Connect form handling and spam protection.
7. Add metadata and structured data.
8. Optimize images and video.
9. Run accessibility and performance audits.
10. Complete visual calibration.
11. Complete legal and brand approval.
12. Remove every `Pitch concept` label before launch.
