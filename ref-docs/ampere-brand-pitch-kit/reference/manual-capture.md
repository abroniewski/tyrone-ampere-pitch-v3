# Automated browser capture

- Date: 2026-07-16
- Page URL: https://amperealliance.ca/
- Capture method: Playwright Chromium (headless)
- Tool: reference/capture-live-site.mjs

## Navigation selectors (confirmed)

- Desktop inline nav link: `header nav ul.f--navigation a`
- Mobile menu trigger: `header .menu`
- Mobile nav panel: `header nav.active` (full-screen overlay)
- Mobile nav link: `header nav ul.f--navigation a` (same selector, menu must be open)
- Breakpoint: mobile overlay below 1024px; desktop inline at 1024px and above

## Viewport 1440px

- Hero text: "The Next  Generation  of Power"

### Hero headline

- selectorHint: h1.f--h1.words.chars.splitting
- text: The Next  Generation  of Power
- fontFamily: G, Helvetica, Arial, sans-serif
- fontWeight: 300
- fontSize: 100px
- lineHeight: 95px
- letterSpacing: normal
- color: rgb(255, 255, 255)
- textTransform: none
- backgroundColor: rgba(0, 0, 0, 0)
- display: block
- visibility: visible
- animationName: none
- animationDuration: 0s
- animationDelay: 0s
- animationTimingFunction: ease
- transitionProperty: all
- transitionDuration: 0s

### Navigation (desktop-inline)

- confirmedSelector: header nav ul.f--navigation a
- navPanel display: block
- navPanel classes: 

#### First nav link

- selectorHint: a
- text: About
- fontFamily: G, Helvetica, Arial, sans-serif
- fontWeight: 500
- fontSize: 12px
- lineHeight: 13.2px
- letterSpacing: normal
- color: rgb(255, 255, 255)
- textTransform: uppercase
- backgroundColor: rgba(0, 0, 0, 0)
- display: block
- visibility: visible
- animationName: none
- animationDuration: 0s
- animationDelay: 0s
- animationTimingFunction: ease
- transitionProperty: all
- transitionDuration: 0.25s

#### All nav links

- About: 12px, weight 500
- Portfolio: 12px, weight 500
- Approach: 12px, weight 500
- Insights: 12px, weight 500
- Contact: 12px, weight 500

### Body copy

- selectorHint: div.f--p
- text: An elite collective of North America’s most ambitious electrical and instrumentation companies bound by a desire for exponential growth.
- fontFamily: G, Helvetica, Arial, sans-serif
- fontWeight: 400
- fontSize: 16px
- lineHeight: 22.4px
- letterSpacing: normal
- color: rgb(194, 194, 194)
- textTransform: none
- backgroundColor: rgba(0, 0, 0, 0)
- display: block
- visibility: visible
- animationName: none
- animationDuration: 0s
- animationDelay: 0s
- animationTimingFunction: ease
- transitionProperty: all
- transitionDuration: 0s

### Backgrounds

- body: rgba(0, 0, 0, 0)
- html: rgb(0, 0, 0)

### After scroll

- scrollY: 450
- inview sections: 2

#### In-view animation samples

**Sample 1** (`span.char`)
- animationName: down
- animationDuration: 1.2s
- animationDelay: 0s
- animationTimingFunction: cubic-bezier(0.4, 0.5, 0, 1)

**Sample 2** (`span.char`)
- animationName: down
- animationDuration: 1.2s
- animationDelay: 0.01s
- animationTimingFunction: cubic-bezier(0.4, 0.5, 0, 1)

**Sample 3** (`span.char`)
- animationName: down
- animationDuration: 1.2s
- animationDelay: 0.02s
- animationTimingFunction: cubic-bezier(0.4, 0.5, 0, 1)

**Sample 4** (`span.char`)
- animationName: down
- animationDuration: 1.2s
- animationDelay: 0.03s
- animationTimingFunction: cubic-bezier(0.4, 0.5, 0, 1)

**Sample 5** (`span.char`)
- animationName: down
- animationDuration: 1.2s
- animationDelay: 0.04s
- animationTimingFunction: cubic-bezier(0.4, 0.5, 0, 1)

### Active animations on load

- [1] span.char: down 1.2s cubic-bezier(0.4, 0.5, 0, 1)
- [2] span.char: down 1.2s cubic-bezier(0.4, 0.5, 0, 1)
- [3] span.char: down 1.2s cubic-bezier(0.4, 0.5, 0, 1)
- [4] span.char: down 1.2s cubic-bezier(0.4, 0.5, 0, 1)
- [5] span.char: down 1.2s cubic-bezier(0.4, 0.5, 0, 1)
- [6] span.char: down 1.2s cubic-bezier(0.4, 0.5, 0, 1)
- [7] span.char: down 1.2s cubic-bezier(0.4, 0.5, 0, 1)
- [8] span.char: down 1.2s cubic-bezier(0.4, 0.5, 0, 1)

---

## Viewport 1024px

- Hero text: "The Next  Generation  of Power"

### Hero headline

- selectorHint: h1.f--h1.words.chars.splitting
- text: The Next  Generation  of Power
- fontFamily: G, Helvetica, Arial, sans-serif
- fontWeight: 300
- fontSize: 85.3333px
- lineHeight: 81.0667px
- letterSpacing: normal
- color: rgb(255, 255, 255)
- textTransform: none
- backgroundColor: rgba(0, 0, 0, 0)
- display: block
- visibility: visible
- animationName: none
- animationDuration: 0s
- animationDelay: 0s
- animationTimingFunction: ease
- transitionProperty: all
- transitionDuration: 0s

### Navigation (desktop-inline)

- confirmedSelector: header nav ul.f--navigation a
- navPanel display: block
- navPanel classes: 

#### First nav link

- selectorHint: a
- text: About
- fontFamily: G, Helvetica, Arial, sans-serif
- fontWeight: 500
- fontSize: 10.24px
- lineHeight: 11.264px
- letterSpacing: normal
- color: rgb(255, 255, 255)
- textTransform: uppercase
- backgroundColor: rgba(0, 0, 0, 0)
- display: block
- visibility: visible
- animationName: none
- animationDuration: 0s
- animationDelay: 0s
- animationTimingFunction: ease
- transitionProperty: all
- transitionDuration: 0.25s

#### All nav links

- About: 10.24px, weight 500
- Portfolio: 10.24px, weight 500
- Approach: 10.24px, weight 500
- Insights: 10.24px, weight 500
- Contact: 10.24px, weight 500

### Body copy

- selectorHint: div.f--p
- text: An elite collective of North America’s most ambitious electrical and instrumentation companies bound by a desire for exponential growth.
- fontFamily: G, Helvetica, Arial, sans-serif
- fontWeight: 400
- fontSize: 13.6533px
- lineHeight: 19.1147px
- letterSpacing: normal
- color: rgb(194, 194, 194)
- textTransform: none
- backgroundColor: rgba(0, 0, 0, 0)
- display: block
- visibility: visible
- animationName: none
- animationDuration: 0s
- animationDelay: 0s
- animationTimingFunction: ease
- transitionProperty: all
- transitionDuration: 0s

### Backgrounds

- body: rgba(0, 0, 0, 0)
- html: rgb(0, 0, 0)

### After scroll

- scrollY: 450
- inview sections: 2

#### In-view animation samples

**Sample 1** (`span.char`)
- animationName: down
- animationDuration: 1.2s
- animationDelay: 0s
- animationTimingFunction: cubic-bezier(0.4, 0.5, 0, 1)

**Sample 2** (`span.char`)
- animationName: down
- animationDuration: 1.2s
- animationDelay: 0.01s
- animationTimingFunction: cubic-bezier(0.4, 0.5, 0, 1)

**Sample 3** (`span.char`)
- animationName: down
- animationDuration: 1.2s
- animationDelay: 0.02s
- animationTimingFunction: cubic-bezier(0.4, 0.5, 0, 1)

**Sample 4** (`span.char`)
- animationName: down
- animationDuration: 1.2s
- animationDelay: 0.03s
- animationTimingFunction: cubic-bezier(0.4, 0.5, 0, 1)

**Sample 5** (`span.char`)
- animationName: down
- animationDuration: 1.2s
- animationDelay: 0.04s
- animationTimingFunction: cubic-bezier(0.4, 0.5, 0, 1)

### Active animations on load

- [1] span.char: down 1.2s cubic-bezier(0.4, 0.5, 0, 1)
- [2] span.char: down 1.2s cubic-bezier(0.4, 0.5, 0, 1)
- [3] span.char: down 1.2s cubic-bezier(0.4, 0.5, 0, 1)
- [4] span.char: down 1.2s cubic-bezier(0.4, 0.5, 0, 1)
- [5] span.char: down 1.2s cubic-bezier(0.4, 0.5, 0, 1)
- [6] span.char: down 1.2s cubic-bezier(0.4, 0.5, 0, 1)
- [7] span.char: down 1.2s cubic-bezier(0.4, 0.5, 0, 1)
- [8] span.char: down 1.2s cubic-bezier(0.4, 0.5, 0, 1)

---

## Viewport 390px

- Hero text: "The Next  Generation  of Power"

### Hero headline

- selectorHint: h1.f--h1.words.chars.splitting
- text: The Next  Generation  of Power
- fontFamily: G, Helvetica, Arial, sans-serif
- fontWeight: 300
- fontSize: 59.6939px
- lineHeight: 56.7092px
- letterSpacing: normal
- color: rgb(255, 255, 255)
- textTransform: none
- backgroundColor: rgba(0, 0, 0, 0)
- display: block
- visibility: visible
- animationName: none
- animationDuration: 0s
- animationDelay: 0s
- animationTimingFunction: ease
- transitionProperty: all
- transitionDuration: 0s

### Navigation (mobile-overlay)

- confirmedSelector: header nav ul.f--navigation a
- navPanel display: flex
- navPanel classes: active

#### First nav link

- selectorHint: a
- text: About
- fontFamily: G, Helvetica, Arial, sans-serif
- fontWeight: 400
- fontSize: 19.898px
- lineHeight: 13.1327px
- letterSpacing: normal
- color: rgb(255, 255, 255)
- textTransform: uppercase
- backgroundColor: rgba(0, 0, 0, 0)
- display: flex
- visibility: visible
- animationName: none
- animationDuration: 0s
- animationDelay: 0s
- animationTimingFunction: ease
- transitionProperty: all
- transitionDuration: 0.25s

#### All nav links

- About: 19.898px, weight 400
- Portfolio: 19.898px, weight 400
- Approach: 19.898px, weight 400
- Insights: 19.898px, weight 400
- Contact: 19.898px, weight 400

#### Menu trigger

- selector: header .menu
- display: block

### Body copy

- selectorHint: div.f--p
- text: An elite collective of North America’s most ambitious electrical and instrumentation companies bound by a desire for exponential growth.
- fontFamily: G, Helvetica, Arial, sans-serif
- fontWeight: 400
- fontSize: 14.9235px
- lineHeight: 20.8929px
- letterSpacing: normal
- color: rgb(194, 194, 194)
- textTransform: none
- backgroundColor: rgba(0, 0, 0, 0)
- display: block
- visibility: visible
- animationName: none
- animationDuration: 0s
- animationDelay: 0s
- animationTimingFunction: ease
- transitionProperty: all
- transitionDuration: 0s

### Backgrounds

- body: rgba(0, 0, 0, 0)
- html: rgb(0, 0, 0)

### After scroll

- scrollY: 450
- inview sections: 2

#### In-view animation samples

**Sample 1** (`span.char`)
- animationName: down
- animationDuration: 1.2s
- animationDelay: 0s
- animationTimingFunction: cubic-bezier(0.4, 0.5, 0, 1)

**Sample 2** (`span.char`)
- animationName: down
- animationDuration: 1.2s
- animationDelay: 0.01s
- animationTimingFunction: cubic-bezier(0.4, 0.5, 0, 1)

**Sample 3** (`span.char`)
- animationName: down
- animationDuration: 1.2s
- animationDelay: 0.02s
- animationTimingFunction: cubic-bezier(0.4, 0.5, 0, 1)

**Sample 4** (`span.char`)
- animationName: down
- animationDuration: 1.2s
- animationDelay: 0.03s
- animationTimingFunction: cubic-bezier(0.4, 0.5, 0, 1)

**Sample 5** (`span.char`)
- animationName: down
- animationDuration: 1.2s
- animationDelay: 0.04s
- animationTimingFunction: cubic-bezier(0.4, 0.5, 0, 1)

### Active animations on load

- [1] span.char: down 1.2s cubic-bezier(0.4, 0.5, 0, 1)
- [2] span.char: down 1.2s cubic-bezier(0.4, 0.5, 0, 1)
- [3] span.char: down 1.2s cubic-bezier(0.4, 0.5, 0, 1)
- [4] span.char: down 1.2s cubic-bezier(0.4, 0.5, 0, 1)
- [5] span.char: down 1.2s cubic-bezier(0.4, 0.5, 0, 1)
- [6] span.char: down 1.2s cubic-bezier(0.4, 0.5, 0, 1)
- [7] span.char: down 1.2s cubic-bezier(0.4, 0.5, 0, 1)
- [8] span.char: down 1.2s cubic-bezier(0.4, 0.5, 0, 1)

---

## Font preloads

- https://amperealliance.ca/wp-content/themes/theme/assets/fonts/GeneralSans-Light.woff2
- https://amperealliance.ca/wp-content/themes/theme/assets/fonts/GeneralSans-Medium.woff2
- https://amperealliance.ca/wp-content/themes/theme/assets/fonts/GeneralSans-Regular.woff2

## Stylesheets

- https://amperealliance.ca/wp-content/themes/theme/assets/css/global.css?ver=1.0.35
- https://amperealliance.ca/wp-content/themes/theme/assets/css/main.css?ver=1.0.35
- https://amperealliance.ca/wp-content/themes/theme/assets/css/text.css?ver=1.0.35
- https://amperealliance.ca/wp-content/themes/theme/assets/css/diff.css?ver=1.0.35
- https://amperealliance.ca/wp-content/themes/theme/assets/css/partners.css?ver=1.0.35
- https://amperealliance.ca/wp-content/themes/theme/assets/css/testimonials.css?ver=1.0.35
- https://amperealliance.ca/wp-content/themes/theme/assets/css/team.css?ver=1.0.35
- https://amperealliance.ca/wp-content/themes/theme/assets/css/news.css?ver=1.0.35
- https://amperealliance.ca/wp-content/themes/theme/assets/css/growth.css?ver=1.0.35
