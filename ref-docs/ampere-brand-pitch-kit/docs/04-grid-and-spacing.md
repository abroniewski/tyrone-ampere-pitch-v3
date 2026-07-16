# 04. Grid and Spacing

## Desktop grid

- 12 columns.
- Maximum content width: 1888 pixels in the working code.
- Fluid horizontal gutter: 20 to 64 pixels.
- Fluid gap: 16 to 40 pixels.
- Major sections may break the container for full-bleed black, blue, or image fields.

## Tablet grid

- 8 columns below 1024 pixels.
- Preserve asymmetric spans rather than forcing every module to 50/50.
- Hide the full navigation and switch to the menu trigger.

## Mobile grid

- 4 columns below 768 pixels.
- Horizontal gutter: 20 pixels.
- Major content usually spans all four columns.
- Preserve the hero wedge, but allow the title to overlap it.

## Vertical rhythm

| Token | Use | Working value |
|---|---|---|
| `--section-space` | Major section padding | `clamp(6rem, 12vw, 13rem)` |
| `--section-space-sm` | Compact or CTA sections | `clamp(4rem, 7vw, 8rem)` |
| `--header-height` | Fixed header | `5.25rem`, mobile `4.5rem` |
| `--grid-gap` | Layout gap | `clamp(1rem, 2vw, 2.5rem)` |

## Spacing principle

Large type needs large silence. Do not solve content pressure by shrinking the type first. Remove copy, increase the section height, or change the line break.

## Alignment rules

- Align labels to the top edge of a headline block.
- Align supporting copy to a headline baseline or the bottom of the section.
- Anchor small metadata near composition edges.
- Allow image shapes to ignore the text grid when creating tension.
- Do not center standard sections by default.

## Borders and card grids

For three-column systems:

- Apply one border to the grid's top and left.
- Apply right and bottom borders to each card.
- This avoids doubled lines.
- Keep corners square.

## Breakpoint guidance

The included breakpoints are implementation defaults, not confirmed official values:

- Large desktop: 1440 and above.
- Desktop: 1024 to 1439.
- Tablet: 768 to 1023.
- Mobile: below 768.

Add a 480-pixel adjustment only when actual content requires it. Do not fragment the system into many micro-breakpoints.
