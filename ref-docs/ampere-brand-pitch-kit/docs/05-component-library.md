# 05. Component Library

## Global header

### Anatomy

- Angular symbol plus light wordmark.
- Optional `Pitch concept` qualifier during review.
- Compact primary navigation.
- Rectangular cobalt CTA.
- Mobile menu trigger composed of two thin horizontal lines.

### Behavior

- Transparent over the hero.
- Becomes near-black with subtle blur and a one-pixel lower rule after 24 pixels of scroll.
- Remains fixed.
- Mobile menu opens as a full cobalt field.

### Content limits

- Five primary navigation items plus one CTA.
- Navigation labels should remain one word when practical.

## Hero

### Anatomy

- Full viewport black canvas.
- Left-aligned, hand-broken display headline.
- Small supporting copy low on the left.
- Triangle text link.
- Large right-side polygon image mask.
- Optional coordinates or project marker.
- Optional rotated scroll prompt.

### Rules

- Headline should occupy roughly 35 to 50 percent of viewport width.
- Media wedge should occupy 50 to 65 percent.
- The wedge may sit behind the headline on mobile.
- Use one core message, not a headline, subheadline, badge, and four CTAs.

## Interior page hero

- 72 to 80 percent viewport height.
- Oversized headline on a 12-column grid.
- Short strategic introduction anchored low and right.
- One large gradient shard partially outside the viewport.

## Kicker

- Filled cobalt triangle.
- Uppercase micro-label.
- Optional section number.
- Keep to one line.

## Buttons

### Primary

- Cobalt fill.
- White label.
- Northeast arrow.
- White fill rises from below on hover, changing text to black.

### Outline

- One-pixel border.
- Transparent background.
- Uses the same rising-fill motion.

### Rules

- Square corners.
- Minimum height: 52 pixels.
- One decisive verb phrase.
- Avoid more than two buttons in one view.

## Text links

- Small solid triangle on the left.
- Triangle shifts slightly right on hover.
- Best for secondary navigation or low-emphasis hero actions.

## Section header

Desktop structure:

- Columns 1 to 3: kicker.
- Columns 4 to 10: headline.
- Columns 10 to 12: compact explanation.

On mobile all elements stack, with the headline leading.

## System card

- Black surface.
- One-pixel grid borders.
- Small index at top.
- Large title and compact copy at bottom.
- Cobalt fill rises from the bottom on hover.
- Minimum desktop height: 496 pixels.

Best for:

- Strategic pillars.
- Benefits.
- Capabilities.
- Process phases.

## Campaign or work card

- Large image field.
- Asymmetric polygon crop.
- Bottom gradient overlay.
- Compact category metadata.
- Large title.
- Northeast arrow.
- Media scales 3 to 6 percent on hover.

Use a varied editorial grid rather than equal card tiles.

## Stat card

- Mist background.
- One-pixel dark border grid.
- Oversized thin cobalt numeral.
- Compact label anchored low.
- No icon and no dashboard chrome.

## Timeline row

- Index.
- Large one-word phase title.
- Compact explanatory copy.
- Cobalt fill rises on hover.
- Desktop grid ratio: approximately 1 / 3 / 2.

## Portfolio row

- Index.
- Very large company name.
- Compact sector, location, or year metadata.
- Arrow at the far edge.
- Full cobalt sweep from left on hover.

## Insight row

- Category and reading time.
- Large article title.
- Arrow.
- Slight horizontal inset on hover.
- Text shifts to cobalt on light backgrounds.

## Quote block

- Black field.
- Large gradient shard outside the lower-right edge.
- Oversized quote on the left.
- Small attribution on the right.
- Avoid quotation-mark graphics unless they are essential.

## Person card

- 4:5 or 0.78 portrait crop.
- Grayscale by default.
- Color reveals on hover.
- Name in large light type.
- Role in compact muted text.

## Form

- Labels above fields.
- Transparent inputs with only a bottom rule.
- Large light input text.
- Cobalt focus line.
- Two columns on desktop, one on mobile.
- One primary submit action.

## Footer

- Near-black field.
- Brand at left.
- Three compact link groups.
- Legal and prototype note below a one-pixel rule.
- Avoid oversized social icons.

## States to implement

Every interactive component needs:

- Default.
- Hover for fine pointers.
- Keyboard focus.
- Active or pressed.
- Disabled where applicable.
- Reduced-motion behavior.
- High-contrast fallback where applicable.
