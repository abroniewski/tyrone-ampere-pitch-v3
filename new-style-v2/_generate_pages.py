#!/usr/bin/env python3
"""Generate all new-style-v2 HTML pages with shared Ampere chrome."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT.parent

STEPS = [
    ("index.html", "1", "The Miss"),
    ("strategy.html", "2", "Strategy"),
    ("problem.html", "3", "Problem"),
    ("control.html", "4", "Control"),
    ("risks.html", "5", "Risks"),
    ("why-adam.html", "6", "Why Adam"),
    ("system.html", "7", "The System"),
    ("next.html", "8", "Next"),
]

ARROW = (
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
    'stroke-width="1.5" aria-hidden="true"><path d="M5 19 19 5M8 5h11v11"/></svg>'
)
MARK = (
    '<svg class="brand__mark" viewBox="0 0 64 64" aria-hidden="true">'
    '<path d="M30 7 11 55l18-12.8L32 20z" fill="currentColor"/>'
    '<path d="m35 9 18 46-16.7-11.8L33 21z" fill="currentColor"/></svg>'
)


def journey_nav(active_file: str) -> str:
    links = []
    for href, num, label in STEPS:
        current = ' aria-current="page"' if href == active_file else ""
        links.append(f'<a href="{href}"{current}><span class="n">{num}</span>{label}</a>')
    return "\n          ".join(links)


def mobile_nav(active_file: str) -> str:
    links = []
    for href, num, label in STEPS:
        current = ' aria-current="page"' if href == active_file else ""
        links.append(f'<a class="mobile-menu__link" href="{href}"{current}>{num} · {label}</a>')
    return "\n      ".join(links)


def wrap(
    active_file: str,
    title: str,
    main_html: str,
    *,
    footer_extra: str = "",
    extra_scripts: str = "",
) -> str:
    footer = (
        "Built by Adam Broniewski from the 2026-07-15 call transcript. "
        "Private: contains quotes from that call, not for redistribution."
        + footer_extra
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="robots" content="noindex, nofollow">
<meta name="theme-color" content="#000000">
<link rel="icon" href="assets/svg/concept-mark.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/pitch.css">
</head>
<body class="is-loading">
<a class="skip-link" href="#main">Skip to content</a>
<div class="preloader" aria-hidden="true">
  <div class="preloader__inner">
    <div class="preloader__brand">{MARK}<span>ADAM × AMPERE</span></div>
    <div class="preloader__track"><div class="preloader__bar"></div></div>
  </div>
</div>
<header class="site-header">
  <div class="site-header__inner">
    <a class="brand" href="index.html" aria-label="Adam × Ampere pitch home">{MARK}<span>ADAM × AMPERE</span></a>
    <nav class="journey-nav" aria-label="Pitch journey">
          {journey_nav(active_file)}
    </nav>
    <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="mobile-menu" aria-label="Open menu" data-menu-toggle>
      <span class="menu-toggle__lines"></span>
    </button>
  </div>
</header>
<aside class="mobile-menu" id="mobile-menu" aria-hidden="true" data-mobile-menu>
  <nav class="mobile-menu__links" aria-label="Mobile journey">
      {mobile_nav(active_file)}
  </nav>
  <div class="mobile-menu__meta">The Living GTM System · Private pitch</div>
</aside>
<main id="main">
{main_html}
</main>
<footer class="site-footer">{footer}</footer>
<script src="js/app.js"></script>
{extra_scripts}
</body>
</html>
"""


def page_hero(kicker: str, title_html: str, *ledes: str, media: bool = False) -> str:
    media_html = '<div class="page-hero__media" aria-hidden="true"></div>' if media else ""
    lede_html = ""
    for i, lede in enumerate(ledes):
        delay = f' style="--reveal-delay:{80 * (i + 1)}ms"' if i else ""
        lede_html += f'\n      <p class="lede" data-reveal{delay}>{lede}</p>'
    return f"""  <section class="page-hero">
    <div class="noise"></div>
    {media_html}
    <div class="page-hero__inner">
      <div class="kicker">{kicker}</div>
      <h1 data-reveal>{title_html}</h1>{lede_html}
    </div>
  </section>"""


def cta(href: str, label: str, ghost: bool = False) -> str:
    cls = "button button--outline" if ghost else "button"
    return f'<a class="{cls}" href="{href}"><span>{label}</span>{ARROW}</a>'


# ---------------------------------------------------------------------------
# Page bodies
# ---------------------------------------------------------------------------

index_body = f"""
{page_hero(
    "(01) The Miss",
    "One missed fact<br>changed this<br>whole pitch.",
    "I built this pitch for you once already. Then I went back through our call, because something important was missing.",
    "You are not only fixing sales and marketing for the companies Ampere owns today. <strong>You are building the commercial system for the companies Ampere has not bought yet.</strong>",
    media=True,
)}

  <div class="marquee" aria-hidden="true">
    <div class="marquee__track">
      <span class="marquee__item">Acquire</span><span class="marquee__item">Integrate</span>
      <span class="marquee__item">Govern</span><span class="marquee__item">Publish</span>
      <span class="marquee__item">Acquire</span><span class="marquee__item">Integrate</span>
      <span class="marquee__item">Govern</span><span class="marquee__item">Publish</span>
    </div>
  </div>

  <div class="pitch-main">
    <section class="pitch-section" data-reveal>
      <h2 class="section-title">What you actually said</h2>
      <div class="cards">
        <div class="card">
          <div class="tag">23:46</div>
          <blockquote>"Eventually we want to buy some more companies."</blockquote>
        </div>
        <div class="card">
          <div class="tag">36:54</div>
          <blockquote>"If you keep buying companies and you become more vertically integrated... you basically become like an Amazon."</blockquote>
        </div>
        <div class="card">
          <div class="tag">36:54</div>
          <blockquote>"I want to keep adding all these different capabilities... and keep bolting things together and create this amazing end-to-end solution."</blockquote>
        </div>
      </div>
      <p class="prose" style="margin-top:1.5rem">That changes the job. A website can solve today's credibility problem. A deck can help the next meeting. A value proposition gives the sales team something to say. <span class="punch">But if those are built as stand-alone assets, the next acquisition makes them stale.</span></p>
    </section>

    <section class="pitch-section" data-reveal>
      <div class="quote-block">We just watched that happen here. One strategic insight entered the source material, and every downstream file in this pitch had to be rebuilt. What you're reading now IS the demo of the system Ampere needs.</div>
      <p class="prose">You never saw version one, and that's fine... it's more useful as evidence than it ever was as a pitch. It still exists, preserved exactly as it was before the insight landed. It was good. It's now stale. That's the whole point.</p>
      <a class="exhibit-link" href="exhibit-a/index.html"><b>EXHIBIT A</b> Open the previous pitch, preserved as evidence →</a>
    </section>

    <div class="cta-row">{cta("strategy.html", "See what that does to the GTM problem")}</div>

    <div class="meta-note">
      <span class="label">How this page was made</span>
      This page exists because the source understanding changed. The old pitch is now an example of what happens when downstream assets aren't tied to a living strategic model. At Ampere, every acquisition will do to your website, decks, and sales training exactly what this insight did to my pitch.
    </div>
  </div>
"""

strategy_body = f"""
{page_hero(
    "(02) Strategy",
    "Ampere's strategy<br>makes change the<br>permanent state.",
    "You're not optimizing a stable portfolio. You're building a group that keeps adding capabilities until it can solve a larger part of the customer's problem end to end.",
)}
  <div class="pitch-main">
    <section class="pitch-section" data-reveal>
      <h2 class="section-title">It's already happening, in three moves</h2>
      <div class="step-card"><div class="step-num">1</div><div>
        <h3>The group intends to keep buying</h3>
        <p><span class="said">"Eventually we want to buy some more companies... that's like a core part of what we want to do."</span></p>
        <p>And you already said you can't run that recurring commercial workload alone: "I just don't think I can do it all myself. It's going to be too crazy."</p>
      </div></div>
      <div class="step-card"><div class="step-num">2</div><div>
        <h3>The value is in the combination</h3>
        <p>Two of the companies were serving the same customers and passing work between each other without a shared commercial plan. You aligned them under one go-to-market, and it immediately made sense. That was integration work, and it will repeat with every acquisition.</p>
        <p>The Amazon opportunity needs TWO companies because neither can deliver it alone. The combined capability of the portfolio is itself part of the offer.</p>
      </div></div>
      <div class="step-card"><div class="step-num">3</div><div>
        <h3>The customer promise is becoming the portfolio</h3>
        <p>The future differentiation isn't one company's fabrication skill. It's Ampere's ability to combine engineering, manufacturing, installation, commissioning, and lifecycle service into one accountable partner that owns the entire outcome... instead of the customer managing handoffs between vendors.</p>
      </div></div>
    </section>
    <section class="pitch-section" data-reveal>
      <div class="quote-block">The portfolio is not only what Ampere owns. It is what Ampere sells.</div>
    </section>
    <section class="pitch-section" data-reveal>
      <h2 class="section-title">What one acquisition can change</h2>
      <p class="prose">Every deal that closes can move any of these, and usually moves several at once:</p>
      <div class="chain" style="margin-top:1.25rem">
        <div class="link">Capability set</div><div class="link">ICP</div><div class="link">Vertical priority</div>
        <div class="link">Solution architecture</div><div class="link">Value propositions</div><div class="link">Available proof</div>
        <div class="link">Website structure</div><div class="link">Sales story</div><div class="link">Opportunity routing</div>
        <div class="link">Rep training</div>
      </div>
      <p class="prose" style="margin-top:1.25rem">Ten commercial objects, all downstream of one signature on one share purchase agreement. Nobody is planning to update them. They just all quietly become less true.</p>
    </section>
    <div class="cta-row">{cta("problem.html", "That makes the real problem bigger than bad assets")}</div>
    <div class="meta-note">
      <span class="label">How this page was made</span>
      Every claim traces to a timestamp: the buying intent [23:46, 30:31], the burgers-and-fries consolidation [24:46], the two-company Amazon deal [29:35], the end-to-end ambition [36:54]. The dossier system that powers this pitch stores each one with its provenance.
    </div>
  </div>
"""

problem_body = f"""
{page_hero(
    "(03) Problem",
    "The real problem<br>is commercial<br>entropy.",
    "Bad websites and decks are the visible symptoms. The deeper problem: Ampere's commercial truth will keep changing while the assets, the systems, and the people struggle to keep up.",
    "<strong>Every acquisition adds capability. Without a living system underneath, it also adds stale pages, conflicting decks, duplicated claims, and another set of things you have to remember personally.</strong>",
)}
  <div class="pitch-main">
    <section class="pitch-section" data-reveal>
      <h2 class="section-title">Five ways it shows up, in your own words</h2>
      <div class="cards">
        <div class="card"><div class="tag">The offer keeps moving</div>
          <blockquote>"We won't be fast soon. And then everyone's going to forget about us for a year."</blockquote>
          <p>"Small and fast" is already expiring. The future story is still being designed: pre-built assemblies? stock? technical features? service? the combined group? Positioning isn't a decision you'll make once. It's a variable.</p></div>
        <div class="card"><div class="tag">Assets detached from the truth</div>
          <blockquote>"We look like we just crawled out of your basement."</blockquote>
          <p>A deck gets rebuilt by hand. A website gets fixed separately. A proposal gets written for one account. None of them knows when the capability model changes underneath it.</p></div>
        <div class="card"><div class="tag">Sales gets snapshots, not a system</div>
          <blockquote>"I need to retrain them on what we even need to be selling and why and how."</blockquote>
          <p>That retraining will go stale again the moment the portfolio changes, unless there's a release process that keeps reps current.</p></div>
        <div class="card"><div class="tag">The group can't see its combined capability</div>
          <blockquote>"Maybe there's opportunities to collaborate... maybe we're calling on similar customers."</blockquote>
          <p>You want one high-level view because opportunities already require multiple companies. Today that map lives nowhere except in your head.</p></div>
        <div class="card"><div class="tag">You are the database AND the update mechanism</div>
          <blockquote>"I basically am just going to have to create everything."</blockquote>
          <p>You're already the person correcting websites, decks, positioning, and cross-company alignment. The acquisition strategy makes that dependency compound with every deal.</p></div>
      </div>
    </section>
    <section class="pitch-section" data-reveal>
      <div class="quote-block">Today's problem is that Ampere lacks content. Tomorrow's problem is that Ampere lacks a controlled way to change what the content is true about.</div>
    </section>
    <div class="cta-row">{cta("control.html", "And the answer can't be pure centralization either")}</div>
    <div class="meta-note">
      <span class="label">How this page was made</span>
      The first version of this pitch diagnosed an asset shortage: 29 extracted pains, mostly about production. The revised extraction found the layer underneath: ten strategic requirements created by the acquisition model. The full map is on the System page. The old diagnosis is in Exhibit A.
    </div>
  </div>
"""

control_body = f"""
{page_hero(
    "(04) Control",
    "One front door.<br>Many owners.",
    "The future system has to respect a tension you described precisely: the market should see one professional Ampere, the operating companies stay legally and commercially distinct, the presidents own their P&amp;Ls and want control... and you still need consistency, routing, and group-level advantage.",
)}
  <div class="pitch-main">
    <section class="pitch-section" data-reveal>
      <div class="quote-block">The presidents own their P&amp;Ls. That's not an obstacle. It's a design requirement, and any commercial system that ignores it is dead on arrival.</div>
      <p class="prose">The presidents carry real accountability: their results, their technical claims, their customer relationships. A system that asks them to give that up deserves to fail. You already saw the shape of the answer yourself: one unified Ampere front, with customers and opportunities routed to the right company under the hood. The system just needs to make that instinct operational.</p>
    </section>
    <section class="pitch-section" data-reveal>
      <h2 class="section-title">The design principle</h2>
      <div class="quote-block" style="margin-top:0.5rem">Centralize the truth, not every decision.</div>
      <div class="cards owns-grid">
        <div class="card"><h3>Ampere group owns</h3><ul>
          <li>The group narrative and master brand standards</li>
          <li>The portfolio capability map</li>
          <li>Shared ICP and solution definitions</li>
          <li>Common proof and claim rules</li>
          <li>The unified customer entry point</li>
        </ul></div>
        <div class="card"><h3>Presidents own or approve</h3><ul>
          <li>Company-specific technical claims</li>
          <li>Local proof and references</li>
          <li>Capacity and delivery constraints</li>
          <li>Vertical-specific nuance</li>
          <li>Company-level commercial exceptions</li>
        </ul></div>
        <div class="card"><h3>You own</h3><ul>
          <li>Cross-company GTM architecture</li>
          <li>Final group coherence</li>
          <li>Priority and release decisions</li>
          <li>Conflict resolution</li>
          <li>The sales enablement standard</li>
        </ul></div>
        <div class="card"><h3>The system owns</h3><ul>
          <li>Traceability and versioning</li>
          <li>Impact lists when something changes</li>
          <li>Routing and status</li>
          <li>Deprecation of stale versions</li>
          <li>Notification, so nobody sells old truth</li>
        </ul></div>
      </div>
    </section>
    <section class="pitch-section" data-reveal>
      <div class="quote-block">Presidents don't need to surrender control for Ampere to present a unified front. They need a system that makes local control compatible with group coherence.</div>
      <p class="prose">And it has to work FOR the presidents, not around them. Each one gets stronger assets, more qualified leads, and access to larger multi-company projects, while keeping approval over every claim made about their company. If the system doesn't create visible local value, it doesn't deserve adoption.</p>
    </section>
    <div class="cta-row">{cta("risks.html", "Without that system, the strategy creates predictable risks")}</div>
    <div class="meta-note">
      <span class="label">How this page was made</span>
      The governance split comes from mapping your constraints [33:27 to 38:49] against how my current system already tags every claim: owner, publication status, approval state. Federated approval is one of the modules that must be BUILT for Ampere. It's named honestly on the System page.
    </div>
  </div>
"""

risks_body = f"""
{page_hero(
    "(05) Risks",
    "Every acquisition can<br>add value and disorder<br>at the same time.",
    "Nothing on this page is invented. Every risk is something you said, taken one step forward using your own numbers.",
)}
  <div class="pitch-main">
    <section class="pitch-section" data-reveal>
      <h2 class="section-title">Six predictable risks</h2>
      <div class="step-card"><div class="step-num">1</div><div>
        <h3>The speed story expires on schedule</h3>
        <p><span class="said">"We're about to fill our entire pipeline for the next year. So we won't be fast soon. And then everyone's going to forget about us for a year."</span></p>
        <p>Once the pipeline fills, Ampere enters a positioning gap: "fast" stops being true, and the replacement value proposition doesn't exist yet. According to your own forecast, that's <strong>12 months</strong> before the current sales story stops working.</p>
      </div></div>
      <div class="step-card"><div class="step-num">2</div><div>
        <h3>The synergy stays invisible</h3>
        <p>Ampere may own an end-to-end capability while the market still sees unrelated companies with disconnected websites. The Amazon-style deals that need two companies don't happen by accident. Someone, or something, has to know the combinations exist.</p>
      </div></div>
      <div class="step-card"><div class="step-num">3</div><div>
        <h3>Reps sell yesterday's Ampere</h3>
        <p>A rep uses an old deck, misses a newly acquired capability, makes an outdated claim, or routes the opportunity to one company when the group could solve more. Nobody did anything wrong. The truth just changed and no release process told them.</p>
      </div></div>
      <div class="step-card"><div class="step-num">4</div><div>
        <h3>The US team ramps against a moving target</h3>
        <p>The plan is to replace the agent channel with an internal team. That team needs to understand the portfolio, present it professionally, and have approved assets from day one. Weak enablement doesn't cost the savings directly. It delays the strategy that creates them.</p>
        <p>Your own example from the call: <strong>$12M to one agent, on one project</strong>. Every month the internal team isn't ready to take over is another month the agent channel keeps earning its percentage.</p>
        <p><strong>The internal team doesn't need to be cheap. It only needs to cost less than that.</strong></p>
      </div></div>
      <div class="step-card"><div class="step-num">5</div><div>
        <h3>Perception compounds against you</h3>
        <p><span class="said">"Perception is everything. You need to look like an established company. Otherwise why the hell am I going to trust you to take on this multi-million-dollar project?"</span></p>
        <p>Your words. At this deal size, materials don't need to lose a whole deal to be expensive. They only need to introduce a little doubt at the wrong moment, in front of exactly the buyers the group needs. And if the fix arrives as scattered one-off efforts, every company keeps presenting a different Ampere.</p>
      </div></div>
      <div class="step-card"><div class="step-num">6</div><div>
        <h3>You become the permanent integration layer</h3>
        <p>Each acquisition adds websites, decks, approval chains, value propositions, and sales questions. Your last-mile bottleneck stops being a bad month and becomes structural. And a website rebuilt today WITHOUT modular content and source links is just the next expensive migration waiting for the next acquisition.</p>
        <p>You have already spent roughly <strong>two weeks</strong> on websites, deck layouts, recolored images, and an AI design system that made output worse. Before the wider group system has even been built.</p>
        <p>The question isn't what two weeks of your time cost. It's what those two weeks would have been worth on a $120M deal, with a president, or on the next acquisition.</p>
      </div></div>
    </section>
    <section class="pitch-section" data-reveal>
      <div class="stats">
        <div class="stat"><div class="stat-num">$12M</div><div class="stat-label">to one agent, one project</div></div>
        <div class="stat"><div class="stat-num">12 mo</div><div class="stat-label">until "fast" stops working</div></div>
        <div class="stat"><div class="stat-num">2 wks</div><div class="stat-label">already spent on one-offs</div></div>
        <div class="stat"><div class="stat-num">5%</div><div class="stat-label">agent take of revenue</div></div>
      </div>
      <div class="quote-block" style="margin-top:2rem">The risk is not only that the marketing stays bad. The risk is that every acquisition makes the commercial layer harder to change.</div>
    </section>
    <div class="cta-row">{cta("why-adam.html", "This is where my experience matters, not only my tooling")}</div>
    <div class="meta-note">
      <span class="label">How this page was made</span>
      Each thing you said gets asked "and then what?". The only numbers on this page are ones you gave me yourself: the one-year pipeline, the $12M agent example, and the two weeks already spent.
    </div>
  </div>
"""

why_adam_body = f"""
{page_hero(
    "(06) Why Adam",
    "I've lived both<br>sides of this<br>change.",
    "Konekti hired me for a commercial motion built around a BMW deal. The deal didn't land. The company pivoted: agentic AI went into the platform, the ICP moved from process-mining and IT buyers to the business side, and the whole product story changed before the commercial infrastructure did.",
    "<strong>Sound like anything you're about to do on purpose, repeatedly, with every acquisition?</strong>",
)}
  <div class="pitch-main">
    <section class="pitch-section" data-reveal>
      <h2 class="section-title">I was inside all three problems at once</h2>
      <div class="cards">
        <div class="card"><div class="tag">Sales</div>
          <p>I know the pressure of being told to go create revenue, reaching the point where the prospect says "can you send something over"... and having nothing credible to send. You lived it too. We compared scars on the call.</p></div>
        <div class="card"><div class="tag">Marketing</div>
          <p>I know the pressure of producing the deck, the page, the proposal, and the follow-up while every output risks becoming a one-off, because the strategy is still moving underneath it.</p></div>
        <div class="card"><div class="tag">Executive GTM</div>
          <p>I know what it's like when the ICP and positioning aren't resolved but the company needs a commercial answer NOW. The CEO told me "don't worry about that, Adam." So I wrote the value proposition myself, as an anchor, and let recorded conversations strengthen it every week.</p></div>
      </div>
    </section>
    <section class="pitch-section" data-reveal>
      <h2 class="section-title">What the pivot taught me, concretely</h2>
      <p class="prose">The old ICP's proof points didn't just become useless. They became DANGEROUS: quoting the wrong era's evidence to the new buyer undermines the new story. So the system tags every proof point with its era, and old-era claims are filtered before reuse. That's not a feature you think of until a pivot burns you.</p>
      <p class="prose">The anchor value proposition worked the same way: version one was wrong in places, and that was fine, because it existed, it was versioned, and every call either confirmed a claim or killed it. <span class="punch">You don't need the right answer to start. You need a system that makes the answer converge.</span></p>
      <p class="prose">And yes: my Konekti contract wasn't renewed, because the pivot's traction hasn't turned into recurring revenue fast enough to keep me. I'm telling you that plainly for two reasons. You should hear it from me first. And it's why the timing of this conversation is almost stupid.</p>
    </section>
    <section class="pitch-section" data-reveal>
      <div class="quote-block">I'm not a content producer who needs a finished strategy handed to me. I build the commercial scaffolding while the strategy is still becoming clear.</div>
    </section>
    <div class="cta-row">{cta("system.html", "Here's the system I built because the assets didn't exist")}</div>
    <div class="meta-note">
      <span class="label">How this page was made</span>
      The pivot story is in our transcript [3:27 to 5:38, 20:38 to 21:39]. The era-tagging and versioned value proposition aren't claims. They're visible in the working system on the next page.
    </div>
  </div>
"""

next_body = f"""
{page_hero(
    "(08) Next",
    "Solve today.<br>Prove tomorrow.",
    "Ninety days. The urgent website, core deck, and value-proposition foundation get built... and built in a way that proves Ampere can absorb the next capability change without starting over.",
)}
  <div class="pitch-main">
    <section class="pitch-section" data-reveal>
      <h2 class="section-title">The 90-day build</h2>
      <div class="timeline">
        <div class="tl-item"><div class="when">Weeks 1-2 · Inventory and operating model</div>
          <p>Recording and intake standard. Audit of every current asset. The commercial object taxonomy. Decision-rights interviews with you, the presidents, and your systems owner. Pilot company or solution selected. <strong>Output:</strong> current-state map, asset registry v0, ownership matrix, capture workflow.</p></div>
        <div class="tl-item"><div class="when">Weeks 3-4 · Company and capability model</div>
          <p>Internal dossiers for the pilot companies from your discovery-trip recordings. Capabilities, overlaps, proof, constraints, and cross-company combinations mapped. First group-to-company positioning hierarchy. <strong>Output:</strong> portfolio capability map v1 and solution map v1.</p></div>
        <div class="tl-item"><div class="when">Weeks 5-8 · Urgent assets as governed views</div>
          <p>The Ampere brand becomes tokens and components. Group and pilot-company value propositions built from evidence. The website you can't send to customers gets rebuilt. The core sales deck and an approved sales play ship. Every output registered against its source objects and owners. <strong>Output:</strong> customer-ready assets that already belong to the system.</p></div>
        <div class="tl-item"><div class="when">Weeks 9-12 · The change-cascade proof</div>
          <p>We introduce a controlled change: a new capability, a company combination, a positioning decision. The system identifies every affected asset, routes updates to the right approvers, regenerates the views, notifies sales, and retires old versions. <strong>Output:</strong> proof that the architecture can evolve without a rebuild. Success isn't a prettier website. Success is that one change moves through the group without a manual scavenger hunt.</p></div>
      </div>
    </section>
    <section class="pitch-section" data-reveal>
      <h2 class="section-title">What this buys Ampere</h2>
      <p class="prose">Two things, both from your own numbers. No consulting math needed.</p>
      <div class="upside-grid">
        <article class="upside-card">
          <div class="eyebrow">1 · The agent money stays in the group</div>
          <h3>The internal team takes over sooner</h3>
          <p>Agents take 5% of revenue. On one $120M project, one agent stands to make $12M... your example, from our call. The internal team that replaces that channel costs a fraction of it, but only starts earning its keep once it has value propositions, credible materials, and account knowledge to work with.</p>
          <p><strong>This system is how the new team walks in ready instead of ramping for a year.</strong></p>
        </article>
        <article class="upside-card">
          <div class="eyebrow">2 · Your calendar goes back to the CRO job</div>
          <h3>You stop being the production bottleneck</h3>
          <p>Mega deals, presidents, acquisitions, value-proposition design. That's the work you said should be on your desk, and you've already lost two weeks of it to websites and slide layouts.</p>
          <p><strong>The system does the last-mile production. You do the work only the group's commercial leader can do.</strong></p>
        </article>
      </div>
    </section>
    <section class="pitch-section" data-reveal>
      <h2 class="section-title">How we start</h2>
      <div class="doors">
        <div class="door"><div class="num">THE ASK</div><h3>The 90-day build</h3>
          <p>Give me one company, one cross-company solution, the assets you hate, and access to the people who own the truth. I'll build the first version so the next acquisition makes the system stronger instead of making the marketing messier. Lowest-risk proof there is.</p></div>
        <div class="door"><div class="num">WHERE IT GOES</div><h3>The role you already described</h3>
          <p>You said you need a marketing generalist who works directly for you, that you trust, across companies. If the 90 days proves out, it converts: embedded role or operating retainer, your call. The timing is honestly a little stupid.</p></div>
        <div class="door"><div class="num">TODAY</div><h3>One email</h3>
          <p>Send me the design system and website you already promised on the call. I'll run them through the machine and show you what comes back. Costs you nothing and starts the clock on nothing.</p></div>
      </div>
    </section>
    <section class="pitch-section" data-reveal>
      <div class="quote-block">This is no longer a pitch about making assets faster. It's about giving Ampere a commercial memory, a controlled way to change, and a repeatable method for turning acquisitions into one coherent market story.</div>
    </section>
    <div class="cta-row">
      <a class="button" href="mailto:adam@getkonekti.io?subject=Ampere%20design%20system%20(as%20promised)"><span>Send me that design system</span>{ARROW}</a>
      {cta("index.html", "Read it again", ghost=True)}
      {cta("exhibit-a/index.html", "Compare with Exhibit A", ghost=True)}
    </div>
    <div class="meta-note">
      <span class="label">One last thing</span>
      This pitch went stale once and rebuilt itself in a day. Your commercial story will go stale with every acquisition, on purpose, forever. One of us has already solved that problem.
    </div>
  </div>
"""


def build_system_page() -> str:
    raw = (SRC / "system.html").read_text(encoding="utf-8")
    main = re.search(r"<main>(.*)</main>", raw, re.S).group(1)

    # Replace old hero with Ampere page-hero
    hero = page_hero(
        "(07) The System",
        "Build the urgent assets<br>as views of a<br>living system.",
        "The website is a view. The deck is a view. The value proposition is a versioned model. The source of truth lives underneath.",
        "<strong>Seven layers. The first six create current, governed commercial output and are proven below, in production. The seventh is what Ampere's acquisition strategy demands, and it must be built. I'll show you both honestly.</strong>",
    )
    main = re.sub(
        r'<section class="hero">.*?</section>\s*',
        "",
        main,
        count=1,
        flags=re.S,
    )

    # Wrap remaining content in pitch-main and prepend hero
    # Remove trailing CTA/meta from being orphaned — keep as-is inside pitch-main
    body = f"""
{hero}
  <div class="pitch-main">
{main}
  </div>
"""
    # Fix inline styles that assumed amber theme (harmless if left)
    lightbox = """
<div class="lightbox-overlay" id="lightbox" onclick="closeLightbox(event)">
  <button class="lightbox-close" type="button" aria-label="Close" onclick="closeLightbox(event)">&times;</button>
  <img id="lightboxImg" src="" alt="">
</div>
<script src="js/system.js"></script>
"""
    return wrap(
        "system.html",
        "The Living GTM System | 7. The System",
        body,
        extra_scripts=lightbox,
    )


PAGES = {
    "index.html": ("The Living GTM System | 1. The Miss", index_body, ""),
    "strategy.html": ("The Living GTM System | 2. Strategy", strategy_body, ""),
    "problem.html": ("The Living GTM System | 3. Problem", problem_body, ""),
    "control.html": ("The Living GTM System | 4. Control", control_body, ""),
    "risks.html": (
        "The Living GTM System | 5. Risks",
        risks_body,
        " Private: contains quotes and commercial figures from that call, not for redistribution.",
    ),
    "why-adam.html": ("The Living GTM System | 6. Why Adam", why_adam_body, ""),
    "next.html": (
        "The Living GTM System | 8. Next",
        next_body,
        " Private: contains quotes and commercial figures from that call, not for redistribution.",
    ),
}


def main() -> None:
    for filename, (title, body, footer_extra) in PAGES.items():
        html = wrap(filename, title, body, footer_extra=footer_extra)
        # Fix double footer note on risks/next
        if footer_extra:
            html = html.replace(
                "Private: contains quotes from that call, not for redistribution." + footer_extra,
                footer_extra.strip(),
            )
        (ROOT / filename).write_text(html, encoding="utf-8")
        print(f"Wrote {filename}")

    system_html = build_system_page()
    (ROOT / "system.html").write_text(system_html, encoding="utf-8")
    print("Wrote system.html")


if __name__ == "__main__":
    main()
