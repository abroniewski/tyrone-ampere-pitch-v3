# 07. Motion System

## Motion character

Motion should feel controlled, directional, and mechanical. It should not feel bouncy, playful, or ornamental.

## Core easing

### Reveal easing

```css
cubic-bezier(0.16, 1, 0.3, 1)
```

Use for:

- Headline reveals.
- Card fills.
- Media scale.
- Menu movement.

### Page-state easing

```css
cubic-bezier(0.76, 0, 0.24, 1)
```

Use for:

- Preloader exit.
- Full-screen menu.
- Major state transitions.

## Timing scale

| Token | Duration | Use |
|---|---:|---|
| Fast | 180 ms | Opacity and small feedback |
| Base | 420 ms | Buttons and link states |
| Slow | 900 ms | Section reveals and image changes |
| Reveal | 1100 ms | Large headline and clip reveals |

## Page-load sequence

Recommended order:

1. Black preloader appears immediately.
2. Cobalt line fills over 900 to 1100 milliseconds.
3. Preloader fades over 500 to 700 milliseconds.
4. Hero headline lines rise in with 90 to 130 milliseconds of stagger.
5. Supporting copy appears after the second headline line.
6. Hero media drifts at a nearly imperceptible speed.

Do not add a logo spin, percentage counter, or audio.

## Scroll reveal

Default:

- Start 40 pixels lower.
- Fade from 0 to 1.
- Duration: 900 to 1100 milliseconds.
- Trigger: 10 to 15 percent visible.
- Stop observing after first reveal.

Large headlines may use a vertical clip instead of a simple fade.

## Hover states

### Buttons

A white fill rises from the bottom. The arrow moves northeast by 2 to 3 pixels.

### System cards

Cobalt fills the entire card from the bottom over approximately 650 milliseconds.

### Portfolio rows

Cobalt sweeps in from the left over approximately 650 milliseconds.

### Media cards

Image scales 3 to 6 percent over 900 to 1200 milliseconds.

### Magnetic movement

Use only on fine pointers. Keep displacement below 12 percent of cursor distance. Never move a button far enough to evade the pointer.

## Parallax

- Use only on large background shapes or media.
- Working speed: 0.04 to 0.08 of scroll delta.
- Never parallax body copy.
- Disable on reduced-motion settings.

## Marquee

- Constant linear movement.
- 18 to 28 seconds per loop.
- Duplicate content for seamless motion.
- Pause may be added on hover for accessibility.

## Mobile motion

Reduce layers and travel distance. Keep:

- Headline line reveal.
- Menu transition.
- Card fill.
- Simple scroll reveal.

Remove or minimize:

- Magnetic buttons.
- Strong parallax.
- Cursor effects.
- Complex pinned sequences.

## Reduced motion

The included CSS and JavaScript detect `prefers-reduced-motion: reduce` and:

- Remove transition duration.
- Stop parallax.
- Stop marquee movement.
- Reveal content immediately.
- Preserve all content and interaction states.

## Animation budget

At any moment, aim for no more than:

- One large continuous background motion.
- One active reveal sequence.
- One user-triggered hover or menu transition.

More simultaneous motion turns precision into visual static.
