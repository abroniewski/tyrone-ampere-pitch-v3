# 11. Accessibility and Performance

## Accessibility target

Aim for WCAG 2.2 AA for all public pages.

## Keyboard behavior

- All links, buttons, menu controls, and form fields must be reachable.
- Focus order must follow reading order.
- The mobile menu button must expose `aria-expanded` and `aria-controls`.
- Escape should close the full-screen menu.
- Focus must remain visible against black, blue, and light backgrounds.
- Do not make hover the only way to reveal essential content.

## Motion

- Respect `prefers-reduced-motion`.
- Do not autoplay audio.
- Keep background video muted with a visible pause control when it conveys more than decoration.
- Avoid large flashing changes.
- Do not tie reading progress to forced scroll or long scroll-jacking sequences.

## Contrast

Check every final token combination. Pay special attention to:

- Small gray text on black.
- White text over blue photography.
- Blue small text on mist.
- Thin type over gradients.
- Footer legal copy.

Add a local dark overlay to photography rather than adding a text shadow.

## Type

- Base text should remain at least 16 CSS pixels.
- Small labels may be smaller only when nonessential and high contrast.
- Content must remain usable at 200 percent zoom.
- Do not lock line height in pixels.
- Avoid long all-caps passages.

## Images

- Meaningful images need concise alt text.
- Decorative SVG fields need empty alt text or `aria-hidden=true`.
- Portrait alt text should identify the role or context, not describe unhelpful physical traits.
- Company logos should include the company name in accessible text nearby.

## Forms

- Every field needs a real label.
- Errors must be specific and linked to fields.
- Do not rely on placeholder text as a label.
- Explain required fields.
- Confirm successful submission in text.
- Provide privacy context near the submit action.

## Performance budgets

Recommended page budgets for initial load:

- HTML: under 80 KB compressed.
- Critical CSS: under 45 KB compressed.
- JavaScript: under 60 KB compressed for this marketing experience.
- Hero image: under 350 KB when practical.
- Total initial image payload: under 900 KB.
- Hero video: under 8 MB and not required for Largest Contentful Paint.
- Font files: only the weights actually used.

## Core Web Vitals goals

- LCP: under 2.5 seconds at the 75th percentile.
- INP: under 200 milliseconds.
- CLS: under 0.1.

## Implementation tactics

- Preload only the primary display font and hero asset.
- Use `font-display: swap` or an approved equivalent.
- Set media dimensions to prevent layout shift.
- Avoid large animation libraries when CSS and Intersection Observer are enough.
- Defer noncritical scripts.
- Use server-side rendering or static generation for editorial pages.
- Cache immutable assets with fingerprinted filenames.

## Testing matrix

Test at minimum:

- Keyboard only.
- VoiceOver on Safari.
- NVDA or JAWS on Chrome or Edge.
- Reduced motion.
- Windows High Contrast Mode.
- 200 percent zoom.
- iPhone-sized Safari.
- Android-sized Chrome.
- Slow 4G with a midrange device profile.
