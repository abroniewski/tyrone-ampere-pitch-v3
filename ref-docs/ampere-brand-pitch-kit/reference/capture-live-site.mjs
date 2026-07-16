import { chromium } from 'playwright';
import { writeFileSync } from 'fs';
import { dirname, join } from 'path';
import { fileURLToPath } from 'url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const URL = 'https://amperealliance.ca/';
const VIEWPORTS = [1440, 1024, 390];

const SELECTORS = {
  heroHeadline: 'h1.f--h1',
  desktopNavLink: 'header nav ul.f--navigation a',
  mobileMenuTrigger: 'header .menu',
  mobileNavPanel: 'header nav',
  mobileNavLink: 'header nav ul.f--navigation a',
  bodyCopy: 'main .f--p, section .f--p',
};

function readStyles(el) {
  if (!el) return null;
  const s = getComputedStyle(el);
  return {
    selectorHint: `${el.tagName.toLowerCase()}${el.className ? '.' + String(el.className).trim().split(/\s+/).join('.') : ''}`,
    text: el.textContent?.trim() || '',
    fontFamily: s.fontFamily,
    fontWeight: s.fontWeight,
    fontSize: s.fontSize,
    lineHeight: s.lineHeight,
    letterSpacing: s.letterSpacing,
    color: s.color,
    textTransform: s.textTransform,
    backgroundColor: s.backgroundColor,
    display: s.display,
    visibility: s.visibility,
    animationName: s.animationName,
    animationDuration: s.animationDuration,
    animationDelay: s.animationDelay,
    animationTimingFunction: s.animationTimingFunction,
    transitionProperty: s.transitionProperty,
    transitionDuration: s.transitionDuration,
  };
}

async function dismissCookies(page) {
  await page.evaluate(() => {
    const buttons = [...document.querySelectorAll('button, a')];
    const accept = buttons.find((b) => /accept/i.test(b.textContent || ''));
    if (accept) accept.click();
  }).catch(() => {});
}

async function captureNav(page, viewportWidth) {
  const isMobileNav = viewportWidth <= 1023;

  if (isMobileNav) {
    await page.click(SELECTORS.mobileMenuTrigger, { timeout: 5000 });
    await page.waitForSelector('header nav.active', { timeout: 5000 });
    await page.waitForTimeout(400);
  }

  return page.evaluate(({ SELECTORS, isMobileNav, readStylesSource }) => {
    const readStyles = eval(`(${readStylesSource})`);
    const navLink = document.querySelector(SELECTORS.mobileNavLink);
    const menuTrigger = document.querySelector(SELECTORS.mobileMenuTrigger);
    const navPanel = document.querySelector(SELECTORS.mobileNavPanel);

    return {
      mode: isMobileNav ? 'mobile-overlay' : 'desktop-inline',
      confirmedSelector: 'header nav ul.f--navigation a',
      menuTriggerSelector: 'header .menu',
      menuTriggerVisible: menuTrigger ? readStyles(menuTrigger) : null,
      navPanel: navPanel
        ? {
            selectorHint: 'header nav' + (navPanel.classList.contains('active') ? '.active' : ''),
            display: getComputedStyle(navPanel).display,
            classList: [...navPanel.classList],
          }
        : null,
      navLink: readStyles(navLink),
      allNavLinks: [...document.querySelectorAll(SELECTORS.mobileNavLink)].map((el) => ({
        text: el.textContent?.trim(),
        fontSize: getComputedStyle(el).fontSize,
        fontWeight: getComputedStyle(el).fontWeight,
      })),
    };
  }, {
    SELECTORS,
    isMobileNav,
    readStylesSource: readStyles.toString(),
  });
}

async function captureAtViewport(page, width) {
  await page.setViewportSize({ width, height: 900 });
  await page.goto(URL, { waitUntil: 'networkidle', timeout: 60000 });
  await page.waitForTimeout(2500);
  await dismissCookies(page);
  await page.waitForTimeout(500);

  const data = await page.evaluate(({ SELECTORS, readStylesSource }) => {
    const readStyles = eval(`(${readStylesSource})`);
    const hero = document.querySelector(SELECTORS.heroHeadline);
    const body = document.querySelector(SELECTORS.bodyCopy);

    return {
      viewportWidth: window.innerWidth,
      documentTitle: document.title,
      backgrounds: {
        body: getComputedStyle(document.body).backgroundColor,
        html: getComputedStyle(document.documentElement).backgroundColor,
      },
      heroHeadline: readStyles(hero),
      bodyCopy: readStyles(body),
      fontPreloads: [...document.querySelectorAll('link[rel="preload"][as="font"]')].map((l) => l.href),
      stylesheets: [...document.querySelectorAll('link[rel="stylesheet"]')].map((l) => l.href),
      heroText: hero?.textContent?.trim().slice(0, 120) || null,
    };
  }, {
    SELECTORS,
    readStylesSource: readStyles.toString(),
  });

  data.navigation = await captureNav(page, width);

  const animated = await page.evaluate(({ readStylesSource }) => {
    const readStyles = eval(`(${readStylesSource})`);
    return [...document.querySelectorAll('h1 .char, [data-splitting] .char')]
      .slice(0, 8)
      .map((el) => readStyles(el))
      .filter((x) => x && x.animationName && x.animationName !== 'none');
  }, { readStylesSource: readStyles.toString() });
  data.activeAnimationsSample = animated;

  await page.evaluate(() => window.scrollTo(0, window.innerHeight * 0.5));
  await page.waitForTimeout(1500);

  data.afterScroll = await page.evaluate(({ readStylesSource }) => {
    const readStyles = eval(`(${readStylesSource})`);
    return {
      scrollY: window.scrollY,
      inviewCount: document.querySelectorAll('.inview').length,
      inviewSamples: [...document.querySelectorAll('.inview [data-splitting] .char, .inview .t--fade, .inview .t--fadedown')]
        .slice(0, 5)
        .map((el) => readStyles(el)),
    };
  }, { readStylesSource: readStyles.toString() });

  if (width <= 1023) {
    await page.click('header nav .close').catch(() => {});
  }

  return data;
}

function toMarkdown(captures) {
  const lines = [
    '# Automated browser capture',
    '',
    `- Date: ${new Date().toISOString().slice(0, 10)}`,
    `- Page URL: ${URL}`,
    `- Capture method: Playwright Chromium (headless)`,
    `- Tool: reference/capture-live-site.mjs`,
    '',
    '## Navigation selectors (confirmed)',
    '',
    '- Desktop inline nav link: `header nav ul.f--navigation a`',
    '- Mobile menu trigger: `header .menu`',
    '- Mobile nav panel: `header nav.active` (full-screen overlay)',
    '- Mobile nav link: `header nav ul.f--navigation a` (same selector, menu must be open)',
    '- Breakpoint: mobile overlay below 1024px; desktop inline at 1024px and above',
    '',
  ];

  for (const c of captures) {
    lines.push(`## Viewport ${c.viewportWidth}px`, '');
    if (c.heroText) lines.push(`- Hero text: "${c.heroText}"`, '');

    lines.push('### Hero headline', '');
    for (const [k, v] of Object.entries(c.heroHeadline || {})) lines.push(`- ${k}: ${v}`);

    lines.push('', `### Navigation (${c.navigation?.mode})`, '');
    lines.push(`- confirmedSelector: ${c.navigation?.confirmedSelector}`);
    if (c.navigation?.navPanel) {
      lines.push(`- navPanel display: ${c.navigation.navPanel.display}`);
      lines.push(`- navPanel classes: ${c.navigation.navPanel.classList?.join(' ')}`);
    }
    lines.push('', '#### First nav link', '');
    for (const [k, v] of Object.entries(c.navigation?.navLink || {})) lines.push(`- ${k}: ${v}`);
    if (c.navigation?.allNavLinks?.length) {
      lines.push('', '#### All nav links', '');
      c.navigation.allNavLinks.forEach((link) => {
        lines.push(`- ${link.text}: ${link.fontSize}, weight ${link.fontWeight}`);
      });
    }
    if (c.navigation?.menuTriggerVisible && c.viewportWidth <= 1023) {
      lines.push('', '#### Menu trigger', '');
      lines.push(`- selector: header .menu`);
      lines.push(`- display: ${c.navigation.menuTriggerVisible.display}`);
    }

    lines.push('', '### Body copy', '');
    for (const [k, v] of Object.entries(c.bodyCopy || {})) lines.push(`- ${k}: ${v}`);

    lines.push('', '### Backgrounds', '');
    lines.push(`- body: ${c.backgrounds?.body}`);
    lines.push(`- html: ${c.backgrounds?.html}`);

    lines.push('', '### After scroll', '');
    lines.push(`- scrollY: ${c.afterScroll?.scrollY}`);
    lines.push(`- inview sections: ${c.afterScroll?.inviewCount}`);
    if (c.afterScroll?.inviewSamples?.length) {
      lines.push('', '#### In-view animation samples', '');
      c.afterScroll.inviewSamples.forEach((s, i) => {
        lines.push(`**Sample ${i + 1}** (\`${s.selectorHint}\`)`);
        lines.push(`- animationName: ${s.animationName}`);
        lines.push(`- animationDuration: ${s.animationDuration}`);
        lines.push(`- animationDelay: ${s.animationDelay}`);
        lines.push(`- animationTimingFunction: ${s.animationTimingFunction}`);
        lines.push('');
      });
    }
    if (c.activeAnimationsSample?.length) {
      lines.push('### Active animations on load', '');
      c.activeAnimationsSample.forEach((s, i) => {
        lines.push(`- [${i + 1}] ${s.selectorHint}: ${s.animationName} ${s.animationDuration} ${s.animationTimingFunction}`);
      });
    }
    lines.push('', '---', '');
  }

  const first = captures[0];
  if (first?.fontPreloads?.length) {
    lines.push('## Font preloads', '');
    first.fontPreloads.forEach((f) => lines.push(`- ${f}`));
    lines.push('');
  }
  if (first?.stylesheets?.length) {
    lines.push('## Stylesheets', '');
    first.stylesheets.forEach((f) => lines.push(`- ${f}`));
    lines.push('');
  }

  return lines.join('\n');
}

const browser = await chromium.launch({ headless: true });
const page = await browser.newPage();
const captures = [];

try {
  for (const width of VIEWPORTS) {
    console.log(`Capturing at ${width}px...`);
    captures.push(await captureAtViewport(page, width));
  }
} finally {
  await browser.close();
}

const jsonPath = join(__dirname, 'manual-capture.json');
const mdPath = join(__dirname, 'manual-capture.md');

writeFileSync(jsonPath, JSON.stringify({ capturedAt: new Date().toISOString(), url: URL, captures }, null, 2));
writeFileSync(mdPath, toMarkdown(captures));

console.log(`Wrote ${jsonPath}`);
console.log(`Wrote ${mdPath}`);
