from pathlib import Path
from textwrap import dedent

ROOT = Path(__file__).resolve().parent

MARK = '''<svg class="brand__mark" viewBox="0 0 64 64" aria-hidden="true"><path d="M30 7 11 55l18-12.8L32 20z" fill="currentColor"/><path d="m35 9 18 46-16.7-11.8L33 21z" fill="currentColor"/></svg>'''
ARROW = '''<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M5 19 19 5M8 5h11v11"/></svg>'''

NAV = [
    ("about", "About", "about.html"),
    ("approach", "Approach", "approach.html"),
    ("portfolio", "Portfolio", "portfolio.html"),
    ("insights", "Insights", "insights.html"),
    ("careers", "Careers", "careers.html"),
]


def head(title: str, description: str, prefix: str = "") -> str:
    return dedent(f'''\
    <!doctype html>
    <html lang="en">
    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <meta name="description" content="{description}">
      <meta name="theme-color" content="#050505">
      <title>{title}</title>
      <link rel="icon" href="{prefix}assets/svg/concept-mark.svg" type="image/svg+xml">
      <link rel="stylesheet" href="{prefix}assets/css/components.css">
    </head>
    ''')


def header(current: str, prefix: str = "") -> str:
    links = []
    mobile = []
    for key, label, href in NAV:
        current_attr = ' aria-current="page"' if key == current else ''
        links.append(f'<a class="site-nav__link" href="{prefix}pages/{href}"{current_attr}>{label}</a>')
        mobile.append(f'<a class="mobile-menu__link" href="{prefix}pages/{href}">{label}</a>')
    return dedent(f'''\
      <a class="skip-link" href="#main">Skip to content</a>
      <div class="preloader" aria-hidden="true">
        <div class="preloader__inner">
          <div class="preloader__brand">{MARK}<span>Ampere Alliance</span><span class="brand__concept">Pitch concept</span></div>
          <div class="preloader__track"><div class="preloader__bar"></div></div>
        </div>
      </div>
      <header class="site-header">
        <div class="site-header__inner">
          <a class="brand" href="{prefix}index.html" aria-label="Ampere Alliance pitch concept home">
            {MARK}<span>Ampere Alliance</span><span class="brand__concept">Pitch concept</span>
          </a>
          <nav class="site-nav" aria-label="Primary navigation">
            <div class="site-nav__links">{''.join(links)}</div>
            <a class="button" href="{prefix}pages/contact.html" data-magnetic><span>Start a conversation</span>{ARROW}</a>
            <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="mobile-menu" aria-label="Open menu" data-menu-toggle><span class="menu-toggle__lines"></span></button>
          </nav>
        </div>
      </header>
      <aside class="mobile-menu" id="mobile-menu" aria-hidden="true" data-mobile-menu>
        <nav class="mobile-menu__links" aria-label="Mobile navigation">{''.join(mobile)}<a class="mobile-menu__link" href="{prefix}pages/contact.html">Contact</a></nav>
        <div class="mobile-menu__meta"><span>Brand-faithful prototype</span><span>2026 / Concept</span></div>
      </aside>
    ''')


def footer(prefix: str = "") -> str:
    return dedent(f'''\
      <footer class="site-footer">
        <div class="site-footer__top">
          <div><a class="brand" href="{prefix}index.html">{MARK}<span>Ampere Alliance</span><span class="brand__concept">Pitch concept</span></a></div>
          <div><h2 class="site-footer__heading">Explore</h2><ul class="site-footer__list"><li><a href="{prefix}pages/about.html">About</a></li><li><a href="{prefix}pages/approach.html">Approach</a></li><li><a href="{prefix}pages/portfolio.html">Portfolio</a></li></ul></div>
          <div><h2 class="site-footer__heading">Connect</h2><ul class="site-footer__list"><li><a href="{prefix}pages/insights.html">Insights</a></li><li><a href="{prefix}pages/careers.html">Careers</a></li><li><a href="{prefix}pages/contact.html">Contact</a></li></ul></div>
          <div><h2 class="site-footer__heading">Prototype</h2><ul class="site-footer__list"><li><a href="{prefix}style-guide.html">Style guide</a></li><li><a href="{prefix}docs/00-research-summary.md">Research notes</a></li><li><a href="{prefix}docs/12-rights-and-usage.md">Rights note</a></li></ul></div>
        </div>
        <div class="site-footer__bottom"><span>&copy; 2026 Unofficial pitch concept. Replace with approved legal copy.</span><span>Original code and concept visuals. Official marks and photography not bundled.</span></div>
      </footer>
      <script src="{prefix}assets/js/app.js"></script>
    </body>
    </html>
    ''')


def button(label: str, href: str, outline: bool = False) -> str:
    cls = 'button button--outline' if outline else 'button'
    return f'<a class="{cls}" href="{href}" data-magnetic><span>{label}</span>{ARROW}</a>'


def page_hero(title: str, intro: str, kicker: str) -> str:
    return dedent(f'''\
    <section class="page-hero">
      <div class="noise"></div><div class="page-hero__shape" data-parallax="0.04"></div>
      <div class="page-hero__grid">
        <div class="page-hero__title-wrap"><span class="kicker">{kicker}</span></div>
        <h1 class="page-hero__title" data-clip-reveal>{title}</h1>
        <p class="page-hero__intro" data-reveal>{intro}</p>
      </div>
    </section>
    ''')


def cta(prefix: str, title: str = "Build the next generation of attention.") -> str:
    return dedent(f'''\
    <section class="cta-panel">
      <div class="cta-panel__shape" data-parallax="0.06"></div>
      <div class="cta-panel__inner">
        <h2 class="cta-panel__title" data-clip-reveal>{title}</h2>
        <div class="cta-panel__action" data-reveal>{button('Start the conversation', prefix + 'pages/contact.html', True)}</div>
      </div>
    </section>
    ''')


def write(name: str, content: str):
    path = ROOT / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding='utf-8')


home = head(
    'Ampere Alliance Pitch Concept',
    'An unofficial, brand-faithful pitch website prototype inspired by Ampere Alliance public materials.'
) + '<body class="is-loading">' + header('home') + dedent(f'''\
<main id="main">
  <section class="hero">
    <div class="noise"></div>
    <div class="hero__media" aria-hidden="true"></div>
    <div class="hero__inner">
      <div class="hero__copy">
        <h1 class="hero__title" aria-label="Make the signal impossible to miss">
          <span class="hero__title-line"><span style="--line-index:0">Make the</span></span>
          <span class="hero__title-line"><span style="--line-index:1">signal</span></span>
          <span class="hero__title-line"><span style="--line-index:2">impossible</span></span>
          <span class="hero__title-line"><span style="--line-index:3">to miss.</span></span>
        </h1>
        <div class="hero__foot"><p>A brand-led marketing system designed to turn industrial scale, founder ambition, and operating proof into market gravity.</p><a class="text-link" href="#opportunity">View the opportunity</a></div>
      </div>
    </div>
    <div class="hero__coordinate">51.0447 N / 114.0719 W / CONCEPT 01</div>
    <div class="hero__scroll">Scroll</div>
  </section>

  <section class="section theme-light" id="opportunity">
    <div class="container">
      <div class="manifesto">
        <h2 class="manifesto__title" data-clip-reveal>Industrial scale deserves market gravity.</h2>
        <div class="manifesto__copy" data-reveal><span class="kicker">01 / The opportunity</span><p>The strongest industrial brands do more than look credible. They create a repeatable signal that attracts founders, talent, partners, and attention at the same time.</p><p>This concept turns the existing Ampere visual language into a flexible content and campaign engine.</p></div>
      </div>
    </div>
  </section>

  <div class="marquee theme-dark" aria-hidden="true"><div class="marquee__track">
    <div class="marquee__item">Position</div><div class="marquee__item">Prove</div><div class="marquee__item">Publish</div><div class="marquee__item">Convert</div>
    <div class="marquee__item">Position</div><div class="marquee__item">Prove</div><div class="marquee__item">Publish</div><div class="marquee__item">Convert</div>
  </div></div>

  <section class="section theme-dark" id="system">
    <div class="container">
      <div class="section-head"><div class="section-head__kicker"><span class="kicker">02 / The system</span></div><h2 class="section-head__title heading-xl" data-clip-reveal>One brand. Three compounding engines.</h2><p class="section-head__aside copy-muted" data-reveal>Each component is modular enough for weekly marketing and disciplined enough to feel unmistakably Ampere.</p></div>
      <div class="system-grid space-top">
        <article class="system-card" data-reveal><div class="system-card__inner"><span class="system-card__index">01 / POSITION</span><div class="system-card__bottom"><h3 class="system-card__title">Own the category.</h3><p class="system-card__copy">A sharper narrative for the alliance, the acquisition thesis, and the advantage of building together.</p></div></div></article>
        <article class="system-card" data-reveal style="--reveal-delay:100ms"><div class="system-card__inner"><span class="system-card__index">02 / PROVE</span><div class="system-card__bottom"><h3 class="system-card__title">Make growth visible.</h3><p class="system-card__copy">Case studies, operator stories, and portfolio evidence built around numbers, decisions, and outcomes.</p></div></div></article>
        <article class="system-card" data-reveal style="--reveal-delay:200ms"><div class="system-card__inner"><span class="system-card__index">03 / PUBLISH</span><div class="system-card__bottom"><h3 class="system-card__title">Create momentum.</h3><p class="system-card__copy">A repeatable content rhythm that turns every milestone into signal, not a one-off announcement.</p></div></div></article>
      </div>
    </div>
  </section>

  <section class="section theme-dark" id="work">
    <div class="container">
      <div class="section-head"><div class="section-head__kicker"><span class="kicker">03 / Campaign directions</span></div><h2 class="section-head__title heading-xl" data-clip-reveal>Proof with a pulse.</h2><p class="section-head__aside copy-muted" data-reveal>Three visual territories, all using the same core system.</p></div>
      <div class="work-grid space-top">
        <article class="work-card" data-reveal><div class="work-card__media"></div><div class="work-card__overlay"><div><div class="work-card__meta">Portfolio proof</div><h3 class="work-card__title">Built to compound.</h3></div>{ARROW}</div></article>
        <article class="work-card" data-reveal><div class="work-card__media"></div><div class="work-card__overlay"><div><div class="work-card__meta">Founder stories</div><h3 class="work-card__title">The people behind power.</h3></div>{ARROW}</div></article>
        <article class="work-card" data-reveal><div class="work-card__media"></div><div class="work-card__overlay"><div><div class="work-card__meta">Market intelligence</div><h3 class="work-card__title">Signal over noise.</h3></div>{ARROW}</div></article>
      </div>
    </div>
  </section>

  <section class="section theme-mist">
    <div class="container">
      <div class="section-head"><div class="section-head__kicker"><span class="kicker">04 / Operating model</span></div><h2 class="section-head__title heading-lg" data-clip-reveal>A system sized for momentum.</h2></div>
      <div class="stats-grid space-top">
        <article class="stat"><div class="stat__number" data-counter="90">0</div><p class="stat__label">Days to establish the narrative, content system, and first campaign cycle.</p></article>
        <article class="stat"><div class="stat__number" data-counter="4">0</div><p class="stat__label">Core content pillars covering acquisition, operations, leadership, and market insight.</p></article>
        <article class="stat"><div class="stat__number" data-counter="1" data-suffix="x">0</div><p class="stat__label">Unified visual and verbal system across web, social, sales, recruitment, and press.</p></article>
      </div>
    </div>
  </section>

  <section class="section theme-dark" id="rollout">
    <div class="container">
      <div class="section-head"><div class="section-head__kicker"><span class="kicker">05 / 90-day rollout</span></div><h2 class="section-head__title heading-xl" data-clip-reveal>Fast enough to feel electric. Structured enough to last.</h2></div>
      <div class="timeline space-top">
        <article class="timeline__item"><span class="timeline__index">01 / WEEKS 1-2</span><h3 class="timeline__title">Decode</h3><p class="timeline__copy">Interviews, message hierarchy, audience map, asset audit, and success criteria.</p></article>
        <article class="timeline__item"><span class="timeline__index">02 / WEEKS 3-5</span><h3 class="timeline__title">Build</h3><p class="timeline__copy">Campaign architecture, content templates, page modules, and production workflow.</p></article>
        <article class="timeline__item"><span class="timeline__index">03 / WEEKS 6-9</span><h3 class="timeline__title">Launch</h3><p class="timeline__copy">Flagship stories, founder content, portfolio proof, and coordinated distribution.</p></article>
        <article class="timeline__item"><span class="timeline__index">04 / WEEKS 10-13</span><h3 class="timeline__title">Compound</h3><p class="timeline__copy">Measure signal, tune the system, and build the next editorial cycle from live data.</p></article>
      </div>
    </div>
  </section>

  <section class="quote-block"><div class="noise"></div><div class="quote-block__shape" data-parallax="0.05"></div><div class="quote-block__content"><blockquote data-clip-reveal>Make every acquisition feel like the beginning of something bigger.</blockquote><p class="quote-block__credit copy-muted" data-reveal>Strategic thesis for a portfolio-wide marketing system.</p></div></section>

  <section class="section theme-light">
    <div class="container"><div class="section-head"><div class="section-head__kicker"><span class="kicker">06 / Thought leadership</span></div><h2 class="section-head__title heading-lg" data-clip-reveal>Ideas built to travel.</h2></div>
      <div class="insight-list space-top">
        <a class="insight-card" href="pages/insights.html"><span class="insight-card__meta">Strategy / 6 min</span><h3 class="insight-card__title">Why industrial brands need a stronger signal</h3><span class="insight-card__arrow">{ARROW}</span></a>
        <a class="insight-card" href="pages/insights.html"><span class="insight-card__meta">Growth / 8 min</span><h3 class="insight-card__title">Turning acquisition milestones into market momentum</h3><span class="insight-card__arrow">{ARROW}</span></a>
        <a class="insight-card" href="pages/insights.html"><span class="insight-card__meta">Talent / 5 min</span><h3 class="insight-card__title">The recruiting advantage of a visible operating vision</h3><span class="insight-card__arrow">{ARROW}</span></a>
      </div>
    </div>
  </section>
  {cta('', 'Build the next generation of attention.')}
</main>
''') + footer()
write('index.html', home)

about = head('About Concept | Ampere Alliance', 'A sample About page using the reconstructed Ampere design system.', '../') + '<body class="is-loading">' + header('about', '../') + '<main id="main">' + page_hero('Built for ambition.', 'A sample narrative page showing how founder story, operating philosophy, and leadership can live inside the same sharp visual system.', 'About / Concept') + dedent('''
<section class="section theme-light"><div class="container"><div class="manifesto"><h2 class="manifesto__title" data-clip-reveal>Start with conviction. Build with proof.</h2><div class="manifesto__copy" data-reveal><p>The story should move from founder energy to operating discipline, then outward to the collective advantage.</p><p>Keep paragraphs compact. Let one strong sentence carry each screen.</p></div></div><hr class="rule"><div class="copy-columns"><p class="body-lg" data-reveal>Use the left column for origin, pivotal decisions, and the human reason the company exists.</p><p class="body-lg" data-reveal>Use the right column for what has been built, who benefits, and what the next chapter demands.</p></div></div></section>
<section class="section theme-dark"><div class="container"><div class="section-head"><div class="section-head__kicker"><span class="kicker">Leadership pattern</span></div><h2 class="section-head__title heading-lg" data-clip-reveal>Operators, not ornaments.</h2></div><div class="people-grid space-top">
<article class="person-card" data-reveal><div class="person-card__media"><img src="../assets/svg/people-field.svg" alt="Abstract placeholder for a leadership portrait"></div><div><h3 class="person-card__name">Leader Name</h3><p class="person-card__role">Chief Executive Officer</p></div></article>
<article class="person-card" data-reveal style="--reveal-delay:100ms"><div class="person-card__media"><img src="../assets/svg/people-field.svg" alt="Abstract placeholder for a leadership portrait"></div><div><h3 class="person-card__name">Leader Name</h3><p class="person-card__role">Chief Operating Officer</p></div></article>
<article class="person-card" data-reveal style="--reveal-delay:200ms"><div class="person-card__media"><img src="../assets/svg/people-field.svg" alt="Abstract placeholder for a leadership portrait"></div><div><h3 class="person-card__name">Leader Name</h3><p class="person-card__role">Chief Growth Officer</p></div></article>
</div></div></section>
''') + cta('../', 'Ambition deserves a system.') + '</main>' + footer('../')
write('pages/about.html', about)

approach = head('Approach Concept | Ampere Alliance', 'A sample Approach page using the reconstructed Ampere design system.', '../') + '<body class="is-loading">' + header('approach', '../') + '<main id="main">' + page_hero('Scale without losing the spark.', 'A sample operating model page built around short declarations, numbered pillars, and proof-oriented detail.', 'Approach / Concept') + dedent('''
<section class="section theme-dark"><div class="container"><div class="system-grid">
<article class="system-card"><div class="system-card__inner"><span class="system-card__index">01 / ALIGN</span><div class="system-card__bottom"><h2 class="system-card__title">Protect the edge.</h2><p class="system-card__copy">Keep the local reputation, specialist knowledge, and operating instincts that made the company valuable.</p></div></div></article>
<article class="system-card"><div class="system-card__inner"><span class="system-card__index">02 / ENABLE</span><div class="system-card__bottom"><h2 class="system-card__title">Add leverage.</h2><p class="system-card__copy">Introduce shared resources, stronger systems, and cross-portfolio capability without adding noise.</p></div></div></article>
<article class="system-card"><div class="system-card__inner"><span class="system-card__index">03 / COMPOUND</span><div class="system-card__bottom"><h2 class="system-card__title">Build together.</h2><p class="system-card__copy">Turn every operational gain into a broader advantage for the collective.</p></div></div></article>
</div></div></section>
<section class="section theme-mist"><div class="container"><div class="section-head"><div class="section-head__kicker"><span class="kicker">Process pattern</span></div><h2 class="section-head__title heading-lg" data-clip-reveal>Simple language. Serious machinery.</h2></div><div class="timeline space-top" style="border-color:var(--color-line-dark)">
<article class="timeline__item" style="border-color:var(--color-line-dark)"><span class="timeline__index">01</span><h3 class="timeline__title">Listen</h3><p class="timeline__copy" style="color:var(--color-text-muted-dark)">Understand the company, its people, and the operating truth.</p></article>
<article class="timeline__item" style="border-color:var(--color-line-dark)"><span class="timeline__index">02</span><h3 class="timeline__title">Design</h3><p class="timeline__copy" style="color:var(--color-text-muted-dark)">Build the integration plan around real constraints and advantages.</p></article>
<article class="timeline__item" style="border-color:var(--color-line-dark)"><span class="timeline__index">03</span><h3 class="timeline__title">Accelerate</h3><p class="timeline__copy" style="color:var(--color-text-muted-dark)">Deploy shared capability and measure what changes.</p></article>
</div></div></section>
''') + cta('../', 'Build stronger. Stay distinct.') + '</main>' + footer('../')
write('pages/approach.html', approach)

portfolio_rows = ''.join([
    f'''<a class="portfolio-row" href="#"><span class="portfolio-row__index">0{i}</span><h2 class="portfolio-row__name">Member Company {i}</h2><p class="portfolio-row__meta">Specialism / Region / Since 20XX</p><span class="portfolio-row__arrow">{ARROW}</span></a>'''
    for i in range(1, 5)
])
portfolio = head('Portfolio Concept | Ampere Alliance', 'A sample Portfolio page using the reconstructed Ampere design system.', '../') + '<body class="is-loading">' + header('portfolio', '../') + '<main id="main">' + page_hero('A collective built to compound.', 'A sample portfolio index showing the high-contrast row treatment, compact metadata, and electric hover state.', 'Portfolio / Concept') + dedent(f'''
<section class="section theme-dark"><div class="container"><div class="portfolio-list">{portfolio_rows}</div></div></section>
<section class="section theme-light"><div class="container"><div class="manifesto"><h2 class="manifesto__title" data-clip-reveal>Case studies should show the mechanism, not just the milestone.</h2><div class="manifesto__copy"><span class="kicker">Recommended anatomy</span><p>Context. Constraint. Intervention. Operational result. Shared advantage. Next horizon.</p><p>Lead with one decisive number and one human quote. Everything else earns its place.</p></div></div></div></section>
''') + cta('../', 'Make the portfolio visible.') + '</main>' + footer('../')
write('pages/portfolio.html', portfolio)

insight_items = [
    ('Category / 7 min', 'A stronger signal for the next generation of power'),
    ('Acquisitions / 9 min', 'What founders need to see before the first conversation'),
    ('Operations / 6 min', 'The hidden value of shared industrial capability'),
    ('Leadership / 5 min', 'Building a founder voice without founder theatre'),
    ('Talent / 8 min', 'Why ambitious operators follow visible ambition'),
    ('Markets / 10 min', 'Turning sector intelligence into commercial trust'),
]
insight_html = ''.join([f'<a class="insight-card" href="#"><span class="insight-card__meta">{meta}</span><h2 class="insight-card__title">{title}</h2><span class="insight-card__arrow">{ARROW}</span></a>' for meta, title in insight_items])
insights = head('Insights Concept | Ampere Alliance', 'A sample Insights page using the reconstructed Ampere design system.', '../') + '<body class="is-loading">' + header('insights', '../') + '<main id="main">' + page_hero('Signal over noise.', 'A compact editorial index for market intelligence, founder perspective, portfolio proof, and operating ideas.', 'Insights / Concept') + f'<section class="section theme-light"><div class="container"><div class="insight-list">{insight_html}</div></div></section>' + cta('../', 'Publish with a point of view.') + '</main>' + footer('../')
write('pages/insights.html', insights)

careers = head('Careers Concept | Ampere Alliance', 'A sample Careers page using the reconstructed Ampere design system.', '../') + '<body class="is-loading">' + header('careers', '../') + '<main id="main">' + page_hero('Build what power becomes next.', 'A recruiting page that leads with ambition and operating reality, then makes roles easy to scan.', 'Careers / Concept') + dedent(f'''
<section class="section theme-light"><div class="container"><div class="manifesto"><h2 class="manifesto__title" data-clip-reveal>For people who prefer building to watching.</h2><div class="manifesto__copy"><p>Use direct, specific language about the work, the standards, and the opportunity to shape a growing collective.</p><p>Avoid generic culture claims. Show decisions, environments, tools, and people in motion.</p></div></div></div></section>
<section class="section theme-dark"><div class="container"><div class="section-head"><div class="section-head__kicker"><span class="kicker">Open roles pattern</span></div><h2 class="section-head__title heading-lg">Find your next role.</h2></div><div class="portfolio-list space-top">
<a class="portfolio-row" href="#"><span class="portfolio-row__index">01</span><h3 class="portfolio-row__name">Role Title</h3><p class="portfolio-row__meta">Calgary / Full time</p><span class="portfolio-row__arrow">{ARROW}</span></a>
<a class="portfolio-row" href="#"><span class="portfolio-row__index">02</span><h3 class="portfolio-row__name">Role Title</h3><p class="portfolio-row__meta">British Columbia / Full time</p><span class="portfolio-row__arrow">{ARROW}</span></a>
<a class="portfolio-row" href="#"><span class="portfolio-row__index">03</span><h3 class="portfolio-row__name">Role Title</h3><p class="portfolio-row__meta">United States / Full time</p><span class="portfolio-row__arrow">{ARROW}</span></a>
</div></div></section>
''') + cta('../', 'Bring your ambition.') + '</main>' + footer('../')
write('pages/careers.html', careers)

contact = head('Contact Concept | Ampere Alliance', 'A sample Contact page using the reconstructed Ampere design system.', '../') + '<body class="is-loading">' + header('contact', '../') + '<main id="main">' + page_hero('Start the next chapter.', 'The form treatment is intentionally spare: strong type, one-pixel rules, no rounded containers, and a single decisive action.', 'Contact / Concept') + dedent(f'''
<section class="section theme-dark"><div class="container"><div class="section-head"><div class="section-head__kicker"><span class="kicker">Project enquiry</span></div><h2 class="section-head__title heading-lg">Share the shape of the opportunity.</h2></div>
<form class="form-grid space-top" data-demo-form>
<div class="field"><label for="name">Name</label><input id="name" name="name" autocomplete="name" placeholder="Your name" required></div>
<div class="field"><label for="email">Email</label><input id="email" name="email" type="email" autocomplete="email" placeholder="name@company.com" required></div>
<div class="field"><label for="company">Company</label><input id="company" name="company" autocomplete="organization" placeholder="Company name"></div>
<div class="field"><label for="topic">Topic</label><select id="topic" name="topic"><option>Partnership</option><option>Portfolio company</option><option>Career</option><option>Media</option><option>Other</option></select></div>
<div class="field field--full"><label for="message">Message</label><textarea id="message" name="message" placeholder="What should we know?"></textarea></div>
<div class="field field--full"><button class="button" type="submit" data-magnetic><span>Send enquiry</span>{ARROW}</button></div>
</form></div></section>
''') + '</main>' + footer('../')
write('pages/contact.html', contact)

style_guide = head('Style Guide | Ampere Pitch Kit', 'Component and token gallery for the reconstructed Ampere-inspired design system.') + '<body class="is-loading">' + header('guide') + dedent(f'''
<main id="main">
<section class="style-guide-header"><span class="kicker">Design system / v1.0</span><h1>Electric precision. Industrial gravity.</h1></section>
<section class="guide-section"><span class="guide-label">01 / COLOR</span><div class="swatch-grid">
<div class="swatch" style="--swatch:#050505"><strong>Ink</strong><code>#050505</code></div>
<div class="swatch" style="--swatch:#063cff"><strong>Electric</strong><code>#063CFF</code></div>
<div class="swatch" style="--swatch:#e3e9f1;--swatch-text:#050505"><strong>Mist</strong><code>#E3E9F1</code></div>
<div class="swatch" style="--swatch:#b9c4d8;--swatch-text:#050505"><strong>Silver</strong><code>#B9C4D8</code></div>
</div></section>
<section class="guide-section"><span class="guide-label">02 / TYPE</span>
<div class="type-sample"><span class="type-sample__token">--type-hero</span><div style="font:200 var(--type-hero)/.9 var(--font-display);letter-spacing:-.055em">Next power</div></div>
<div class="type-sample"><span class="type-sample__token">--type-h1</span><div class="heading-xl">Build with purpose.</div></div>
<div class="type-sample"><span class="type-sample__token">--type-body-lg</span><p class="body-lg">A large body style for strategic statements and section introductions.</p></div>
<div class="type-sample"><span class="type-sample__token">--type-small</span><span style="font-size:var(--type-small)">Compact metadata, navigation, captions, and proof notes.</span></div>
</section>
<section class="guide-section"><span class="guide-label">03 / ACTIONS</span><div class="component-row">{button('Primary action', '#')}{button('Outline action', '#', True)}<a class="text-link" href="#">Text action</a></div></section>
<section class="guide-section"><span class="guide-label">04 / CARDS</span><div class="system-grid"><article class="system-card"><div class="system-card__inner"><span class="system-card__index">01 / CARD</span><div class="system-card__bottom"><h2 class="system-card__title">Sharp by default.</h2><p class="system-card__copy">The blue fill arrives on hover from the bottom edge.</p></div></div></article><article class="system-card"><div class="system-card__inner"><span class="system-card__index">02 / CARD</span><div class="system-card__bottom"><h2 class="system-card__title">No soft corners.</h2><p class="system-card__copy">Structure comes from lines, scale, and clipped geometry.</p></div></div></article><article class="system-card"><div class="system-card__inner"><span class="system-card__index">03 / CARD</span><div class="system-card__bottom"><h2 class="system-card__title">Proof first.</h2><p class="system-card__copy">Every surface should carry an idea, number, or action.</p></div></div></article></div></section>
<section class="guide-section theme-mist"><span class="guide-label">05 / STAT</span><div class="stats-grid"><article class="stat"><div class="stat__number">33+</div><p class="stat__label">Use thin blue numerals against icy fields.</p></article><article class="stat"><div class="stat__number">90</div><p class="stat__label">Keep labels compact and anchored low.</p></article><article class="stat"><div class="stat__number">1x</div><p class="stat__label">Avoid decorative dashboard chrome.</p></article></div></section>
<section class="guide-section"><span class="guide-label">06 / FORM</span><form class="form-grid" data-demo-form><div class="field"><label for="guide-name">Name</label><input id="guide-name" placeholder="Your name"></div><div class="field"><label for="guide-email">Email</label><input id="guide-email" type="email" placeholder="name@company.com"></div><div class="field field--full"><label for="guide-message">Message</label><textarea id="guide-message" placeholder="What should we know?"></textarea></div><div class="field field--full"><button class="button" type="submit"><span>Submit sample</span>{ARROW}</button></div></form></section>
</main>
''') + footer()
write('style-guide.html', style_guide)

print('Generated site pages.')
