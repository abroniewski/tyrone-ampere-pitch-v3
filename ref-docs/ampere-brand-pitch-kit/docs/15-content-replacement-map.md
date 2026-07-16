# 15. Content Replacement Map

## Editing model

The prototype is generated from `build_site.py`. Shared brand, header, footer, buttons, page heroes, and CTA structures are defined near the top of that file. Page-specific content follows those shared functions.

After replacements, run:

```bash
python3 build_site.py
```

Then review `index.html`, every page in `pages/`, and `style-guide.html`.

## Homepage slots

### 1. Home hero

Replace:

- Four headline lines inside `.hero__title`.
- Accessible combined headline in `aria-label`.
- Supporting paragraph inside `.hero__foot`.
- Secondary text-link label and destination.
- Coordinate or concept marker, when desired.
- `assets/svg/hero-field.svg` or the `.hero__media` treatment with approved image or video.

Keep:

- One decisive message.
- Deliberate manual line breaks.
- Black-to-cobalt split composition.
- One low-emphasis action.

### 2. Opportunity or manifesto

Replace:

- Kicker and section number.
- Large strategic declaration.
- Two compact explanatory paragraphs.

Keep the explanation under roughly 90 words total.

### 3. Rhythm band

Replace the four marquee words. Use verbs or compact strategic nouns. Duplicate the sequence so the loop remains seamless.

### 4. Strategic system

Replace all three `.system-card` entries:

- Index and category.
- Card title.
- Compact body.

Each card should express one mechanism, not a list of services.

### 5. Campaign, portfolio, or proof cards

Replace:

- Original abstract SVG media.
- Category metadata.
- Headline.
- Destination.
- Optional approved result.

Use a varied editorial grid. Do not turn this into six equal SaaS tiles.

### 6. Proof statistics

Replace every placeholder number with an approved statistic that has:

- Source.
- Owner.
- Date range.
- Definition.
- Publication approval.

Update the visible value, counter attributes, suffix or prefix, and compact label together.

### 7. Rollout or process timeline

Replace the four phase names and explanations. One-word phase names preserve the visual rhythm best. Add only the deliverables that reduce client uncertainty.

### 8. Quote feature

Replace the quote, name, role, company, and approval metadata. Keep the quote under roughly 48 words so the block remains architectural rather than transcript-like.

### 9. Insight rows

For each row, replace:

- Category.
- Reading time.
- Article title.
- Link.

Use a CMS in production rather than maintaining these by hand.

### 10. Major CTA

Replace the closing declaration and one action. Do not split the final moment between several competing destinations.

## Interior page shells

### About

Replace origin narrative, milestone rows, leadership placeholders, and culture principles. Request consistent 4:5 portraits before final layout calibration.

### Approach

Replace acquisition or partnership thesis, three operating principles, process phases, proof example, and founder objections.

### Portfolio

Replace placeholder company rows, sectors, locations, company marks, case-study media, and approved result metrics. Company-name scale may need per-name width adjustments.

### Insights

Replace feature story, article rows, newsletter language, categories, author data, and thumbnails. Add Article structured data in production.

### Careers

Replace culture narrative, workplace media, role rows, locations, employment types, and application URLs. Connect to an ATS or approved job feed.

### Contact

Replace expectation-setting copy, enquiry routes, office details, privacy copy, and form action. The prototype form only demonstrates interface feedback and does not send data.

## Asset replacement order

1. Approved display font and weights.
2. Official logo and favicon.
3. Hero media.
4. Portfolio-company logos.
5. Featured campaign or case-study media.
6. Leadership portraits.
7. Proof statistics and quotes.
8. Editorial thumbnails and social images.

This order prevents late font or identity changes from forcing a broad layout reset.

## Fast search markers

Search the project for these strings:

- `Pitch concept`
- `Member Company`
- `Leader Name`
- `Role Title`
- `CONCEPT 01`
- `Submit sample`
- `Unofficial pitch concept`

Remove or replace every marker before an approved public launch.

## Framework migration

When porting to a component framework, move page copy into CMS or structured content files. Keep the class-level behavior as reference, then map the components listed in `data/component-registry.json` to framework components. The visual system should remain token-driven rather than accumulating page-specific overrides.
