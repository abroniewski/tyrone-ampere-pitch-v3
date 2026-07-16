# 14. Calibration Protocol

## Purpose

Use this protocol to turn the brand-faithful reconstruction into a tightly calibrated implementation after direct current-site evidence is available.

## Capture set

Capture the official site with browser zoom at 100 percent and extensions disabled.

### Desktop

- 1440 x 900 homepage at top.
- 1440 x 900 homepage after header state changes.
- Full-page homepage capture.
- One interior page at top.
- Portfolio index.
- Contact form.

### Tablet

- 1024 x 768 hero.
- Open navigation.
- One card section.

### Mobile

- 390 x 844 hero.
- Open navigation.
- Portfolio or insight list.
- Contact form.

### Motion

Record 30 to 60 seconds at 60 frames per second showing:

- Initial load.
- Hero reveal.
- Header transition.
- One full scroll through the homepage.
- Button hover.
- Card hover.
- Mobile menu open and close.

## Calibration order

Do not adjust everything at once. Use this sequence:

1. Font family and weight.
2. Hero line breaks.
3. Major font sizes and line heights.
4. Horizontal gutters and grid spans.
5. Vertical section spacing.
6. Color tokens.
7. Polygon geometry and image crop.
8. Header dimensions and nav spacing.
9. Component borders and internal padding.
10. Motion timing and easing.
11. Mobile-specific crop and overlaps.

## Overlay method

For each viewport:

1. Export the implementation at the exact same dimensions.
2. Place the official capture above it at 50 percent opacity.
3. Align the viewport edges.
4. Compare anchor points:
   - Wordmark position.
   - First headline baseline.
   - Hero wedge edge.
   - Supporting-copy baseline.
   - Section starts.
   - CTA dimensions.
5. Change tokens before writing one-off overrides.

## Color calibration

Sample only from flat areas, not antialiased type, compressed photography, or gradients. Average several points. Confirm the result against official brand specifications.

## Type calibration

When the font is correct, adjust in this order:

1. Weight.
2. Tracking.
3. Line height.
4. Size.
5. Width constraint.

Changing font size first often hides the real mismatch.

## Motion calibration

Measure:

- Delay from page load to first hero movement.
- Duration of each headline line.
- Stagger between lines.
- Header transition duration.
- Card-fill duration.
- Image-scale duration.

Match the perceived rhythm rather than copying every millisecond blindly. Browser and device rendering can change the feel.

## Acceptance checklist

- Major desktop anchors differ by less than 8 pixels.
- Major mobile anchors differ by less than 6 pixels.
- Hero line breaks match.
- Color difference is visually negligible on calibrated displays.
- Motion starts and ends at comparable moments.
- No component loses keyboard, reduced-motion, or responsive behavior during calibration.
- Approved official assets are in place.
