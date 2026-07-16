# 03. Color and Material

## Working palette

| Name | Hex | Primary role |
|---|---|---|
| Ink | `#050505` | Hero, footer, dark sections |
| Carbon | `#101216` | Secondary dark surfaces |
| Paper | `#F5F6F7` | Editorial and narrative sections |
| White | `#FFFFFF` | Text and high-contrast actions |
| Mist | `#E3E9F1` | Statistics and light-blue fields |
| Silver | `#B9C4D8` | Gradient end, secondary visual field |
| Steel | `#7D8595` | Metadata and muted structure |
| Electric | `#063CFF` | Action, acceleration, major data |
| Electric bright | `#1358FF` | Gradient highlight |
| Electric deep | `#0029C8` | Gradient shadow |

## Color proportions

A representative page should use approximately:

- 55 to 70 percent black or carbon.
- 15 to 25 percent paper, white, or mist.
- 5 to 15 percent electric blue.
- Less than 5 percent silver and steel accents.

The blue should feel scarce enough to remain charged.

## Core gradients

### Electric shard

```css
linear-gradient(145deg, #0439FF 0%, #2358DD 48%, #C2CADB 100%)
```

### Soft atmospheric field

```css
linear-gradient(135deg, rgba(6,60,255,.98), rgba(77,101,180,.72) 58%, rgba(207,214,228,.94))
```

Do not use the gradient on standard buttons or body text. Reserve it for large shapes and image overlays.

## Lines

- On dark: `rgba(255,255,255,.22)`.
- On light: `rgba(5,5,5,.18)`.
- Use one-pixel rules.
- Allow large structures to be defined by border grids instead of boxed cards.

## Text opacity

- Primary text: 100 percent.
- Secondary dark-mode text: 62 to 72 percent white.
- Secondary light-mode text: 58 to 68 percent black.
- Disabled or tertiary labels: no lower than 45 percent when contrast remains acceptable.

## Grain

A subtle fractal noise layer may be used at 3 to 6 percent opacity with `soft-light`. Grain should be barely visible on standard monitors and should not reduce text clarity.

## Accessibility

Electric blue is strong against white but may not meet contrast requirements for small blue text on black or some blue-gray fields. Use it primarily as a fill, large numeral, or icon. Verify all final combinations with a contrast checker.

## Print and presentation adaptation

For print or pitch decks:

- Use rich black according to the printer's profile, not the web hex value.
- Keep blue as a spot-like accent when possible.
- Preserve the blue-to-silver shard as a large device rather than a small gradient flourish.
- Test thin white type on black at actual output size.
