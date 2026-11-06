"""Rebuild homepage layout to follow mynameiskalam.com structure, keep Fawas dark colors."""

from pathlib import Path

DIST = Path(__file__).resolve().parent / "dist"
INDEX = DIST / "index.html"

CSS = r"""
body.home{background:#0b0b0b;overflow-x:hidden}
body.home .dtr-heading,body.home h1,body.home h2,body.home h3{text-transform:none!important}
.km{color:#eee;font-family:"Mona Sans",system-ui,sans-serif}
.km a{color:inherit;text-decoration:none}
.km a.km-btn-fill,.km-btn-fill{background:#fff;color:#111!important}
.km a.km-btn-fill:hover,.km-btn-fill:hover{color:#111!important;background:#f3f3f3}
.km a.km-btn-ghost,.km-btn-ghost{color:#fff!important}
.km em{font-style:italic;font-weight:600;color:#fff}
.km-wrap{max-width:1180px;margin:0 auto;padding:0 28px}
.km-hero{display:grid;grid-template-columns:1.35fr .65fr;gap:40px;align-items:center;padding:128px 28px 56px;max-width:1180px;margin:0 auto}
.km-hero h1{margin:0 0 22px;font-size:clamp(2.8rem,6.4vw,4.8rem);line-height:.98;letter-spacing:-.045em;font-weight:750;color:#fff}
.km-hero p{margin:0 0 28px;max-width:540px;font-size:1.08rem;line-height:1.6;color:#bdbdbd}
.km-hero p strong{color:#fff}
.km-ctas{display:flex;flex-wrap:wrap;gap:12px;margin:0 0 36px}
.km-btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;border-radius:999px;padding:14px 22px;font-size:15px;font-weight:600;line-height:1}
.km-btn-ghost{background:transparent;border:1px solid #333}
.km-trust{display:flex;flex-wrap:wrap;gap:22px;padding-top:22px;border-top:1px solid #222}
.km-trust b{display:block;font-size:1.35rem;color:#fff;letter-spacing:-.03em}
.km-trust span{color:#8d8d8d;font-size:13px}
.km-visual{position:relative;width:100%;max-width:360px;margin-left:auto}
.km-visual-card{height:auto;min-height:0;border-radius:24px;overflow:hidden;background:#111;border:1px solid #222}
.km-visual-card picture{display:block;width:100%;height:auto;min-height:0}
.km-visual-card img{width:100%;height:auto;min-height:0;aspect-ratio:4/5;object-fit:cover;object-position:50% 12%;display:block}
.km-badge{position:absolute;top:18px;right:18px;z-index:2;background:#111;color:#fff;border:1px solid #333;border-radius:999px;padding:8px 14px;font-size:12px;letter-spacing:.04em;text-transform:uppercase}
.km-ticker-shell{max-width:1180px;margin:8px auto 0;padding:0 28px;box-sizing:border-box}
.km-ticker{display:flex;align-items:center;gap:0;background:#0f0f0f;border:1px solid #1c1c1c;border-radius:16px;padding:0 20px 0 24px;overflow:hidden;min-height:72px;width:100%;box-sizing:border-box}
.km-ticker-label{position:relative;z-index:2;flex:0 0 auto;color:#7a7a7a;font-size:11px;letter-spacing:.16em;text-transform:uppercase;padding:18px 22px 18px 0;background:#0f0f0f;box-shadow:18px 0 24px 10px #0f0f0f}
.km-ticker-mask{flex:1;min-width:0;overflow:hidden;mask-image:linear-gradient(90deg,transparent,#000 28px,#000 calc(100% - 36px),transparent);-webkit-mask-image:linear-gradient(90deg,transparent,#000 28px,#000 calc(100% - 36px),transparent)}
.km-ticker-track{display:flex;align-items:center;width:max-content;gap:44px;padding:18px 0;animation:kmscroll 36s linear infinite}
.km-ticker:hover .km-ticker-track{animation-play-state:paused}
.km-ticker-track img{height:26px;width:auto;flex:0 0 auto;display:block;opacity:.95;filter:brightness(0) invert(1)}
.km-ticker-track .km-word{flex:0 0 auto;color:#fff;font-size:15px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;opacity:.9}
@keyframes kmscroll{from{transform:translateX(0)}to{transform:translateX(-50%)}}
.km-section{max-width:1180px;margin:0 auto;padding:88px 28px}
.km-kicker{margin:0 0 14px;color:#9a9a9a;font-size:12px;letter-spacing:.14em;text-transform:uppercase}
.km-kicker:before{content:"";display:inline-block;width:22px;height:1px;background:#666;margin-right:10px;vertical-align:middle}
.km-section h2{margin:0 0 16px;font-size:clamp(2.1rem,5vw,3.6rem);line-height:1.05;letter-spacing:-.04em;color:#fff;max-width:720px}
.km-lede{margin:0 0 36px;max-width:560px;color:#b3b3b3;font-size:1.05rem;line-height:1.6}
.km-work{display:grid;grid-template-columns:1fr 1fr;gap:22px}
.km-work-card{position:relative;display:flex;flex-direction:column;justify-content:flex-end;min-height:340px;border-radius:22px;overflow:hidden;background:#141414;border:1px solid #222}
.km-work-card img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:.38}
.km-work-card:hover img{opacity:.5}
.km-work-card .copy{position:relative;z-index:1;padding:28px}
.km-chip{display:inline-block;background:#111;border:1px solid #333;border-radius:999px;padding:5px 10px;font-size:11px;letter-spacing:.08em;text-transform:uppercase;margin-bottom:12px}
.km-work-card h3{margin:0 0 10px;font-size:1.7rem;line-height:1.15;letter-spacing:-.03em;color:#fff}
.km-work-card p{margin:0;color:#c6c6c6;font-size:.98rem;line-height:1.5}
.km-more{display:inline-block;margin-top:22px;color:#fff;border-bottom:1px solid #444;padding-bottom:2px}
.km-services{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}
.km-svc{background:#141414;border:1px solid #222;border-radius:22px;padding:26px 22px;min-height:280px}
.km-svc-top{display:flex;justify-content:space-between;align-items:center;margin-bottom:28px;color:#888;font-size:12px;letter-spacing:.08em}
.km-ico{width:40px;height:40px;border-radius:12px;background:#1c1c1c;display:grid;place-items:center;color:#fff}
.km-svc h3{margin:0 0 10px;font-size:1.25rem;color:#fff}
.km-svc p{margin:0 0 16px;color:#b0b0b0;font-size:.95rem;line-height:1.55}
.km-svc ul{margin:0;padding:0;list-style:none;color:#9a9a9a;font-size:14px}
.km-svc li{padding:5px 0 5px 14px;position:relative}
.km-svc li:before{content:"–";position:absolute;left:0}
.km a.km-svc-cta,.km-svc-cta{background:#fff;color:#111!important;border:0;display:flex;flex-direction:column;justify-content:space-between}
.km-svc-cta h3,.km-svc-cta strong,.km a.km-svc-cta h3,.km a.km-svc-cta strong{color:#111!important}
.km-svc-cta p,.km a.km-svc-cta p{color:#444!important}
.km-svc-cta .km-svc-top,.km a.km-svc-cta .km-svc-top{color:#666!important}
.km-svc-cta .km-ico{background:#111;color:#fff}
.km-about{display:grid;grid-template-columns:.9fr 1.1fr;gap:48px;align-items:start}
.km-about-visual{border-radius:24px;overflow:hidden;min-height:420px;background:#151515;border:1px solid #222}
.km-about-visual img{width:100%;height:100%;object-fit:cover;min-height:420px}
.km-meta{margin:0 0 10px;color:#8d8d8d;font-size:14px}
.km-stats{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin:28px 0}
.km-stat{border:1px solid #222;border-radius:16px;padding:16px}
.km-stat b{display:block;font-size:1.8rem;color:#fff}
.km-stat span{color:#8d8d8d;font-size:13px}
.km-caps{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.km-cap{border:1px solid #222;border-radius:16px;padding:16px}
.km-cap h4{margin:0 0 6px;color:#fff;font-size:1rem}
.km-cap p{margin:0;color:#9a9a9a;font-size:14px;line-height:1.45}
.km-cta{max-width:1180px;margin:0 auto 96px;padding:56px 36px;border:1px solid #222;border-radius:28px;background:#121212}
.km-cta h2{margin:0 0 12px;font-size:clamp(2rem,4vw,3rem);color:#fff}
.km-cta p{margin:0 0 24px;color:#b3b3b3;max-width:560px}
@media (max-width:980px){
  .km-hero,.km-about,.km-services,.km-work{grid-template-columns:1fr}
  .km-visual{max-width:280px;margin:8px auto 0}
  .km-svc-cta{min-height:220px}
  .km-ticker-shell{padding:0 20px}
  .km-ticker-label{max-width:92px;line-height:1.35}
}
"""

HOME = r"""
<article id="post-9" class="post-9 page type-page">
<div class="entry-content km">
  <section class="km-hero">
    <div>
      <h1>Search-driven growth that <em>actually ranks.</em></h1>
      <p>I'm <strong>Muhammed Fawas</strong>, an SEO Specialist based between Kerala and Dubai. 2.5+ years helping businesses across India and the UAE improve search visibility, attract qualified traffic, and grow.</p>
      <div class="km-ctas">
        <a class="km-btn km-btn-fill" href="https://wa.me/971528481743" target="_blank" rel="noopener">WhatsApp →</a>
        <a class="km-btn km-btn-ghost" href="#works">Explore work</a>
      </div>
      <div class="km-trust">
        <div><b>2.5+</b><span>Years of SEO</span></div>
        <div><b>20+</b><span>Websites managed</span></div>
        <div><b>15+</b><span>Google Business Profiles</span></div>
      </div>
    </div>
    <div class="km-visual">
      <div class="km-visual-card">
        <picture>
          <source type="image/webp" srcset="/wp-content/uploads/fawas-exec-800.webp 800w, /wp-content/uploads/fawas-exec.webp 795w" sizes="(max-width:980px) 92vw, 360px">
          <img src="/wp-content/uploads/fawas-exec.jpg" alt="Muhammed Fawas, SEO Specialist" width="795" height="1105" fetchpriority="high" decoding="async">
        </picture>
      </div>
      <span class="km-badge">Immediate joiner</span>
    </div>
  </section>

  <div class="km-ticker-shell">
  <div class="km-ticker" aria-label="Clients">
    <div class="km-ticker-label">Trusted by teams at</div>
    <div class="km-ticker-mask">
      <div class="km-ticker-track">
        <img src="/wp-content/uploads/logos/dexito.webp?v=w1" alt="dExito Branding" height="26">
        <img src="/wp-content/uploads/logos/greenoasis.webp?v=w1" alt="Green Oasis Travel" height="26">
        <img src="/wp-content/uploads/logos/grandbake.webp?v=w1" alt="Grand Bake" height="26">
        <img src="/wp-content/uploads/logos/salman.webp?v=w1" alt="Brand with Salman" height="26">
        <img src="/wp-content/uploads/logos/crink.webp?v=w1" alt="Crink.app" height="26">
        <img src="/wp-content/uploads/logos/aurevo.webp?v=w1" alt="Aurevo Interiors" height="26">
        <span class="km-word">ZAQRT</span>
        <img src="/wp-content/uploads/logos/tawakkal.webp?v=w1" alt="Al Tawakkal" height="26">
        <img src="/wp-content/uploads/logos/dexito.webp?v=w1" alt="" height="26" aria-hidden="true">
        <img src="/wp-content/uploads/logos/greenoasis.webp?v=w1" alt="" height="26" aria-hidden="true">
        <img src="/wp-content/uploads/logos/grandbake.webp?v=w1" alt="" height="26" aria-hidden="true">
        <img src="/wp-content/uploads/logos/salman.webp?v=w1" alt="" height="26" aria-hidden="true">
        <img src="/wp-content/uploads/logos/crink.webp?v=w1" alt="" height="26" aria-hidden="true">
        <img src="/wp-content/uploads/logos/aurevo.webp?v=w1" alt="" height="26" aria-hidden="true">
        <span class="km-word" aria-hidden="true">ZAQRT</span>
        <img src="/wp-content/uploads/logos/tawakkal.webp?v=w1" alt="" height="26" aria-hidden="true">
      </div>
    </div>
  </div>
  </div>

  <section class="km-section" id="works">
    <p class="km-kicker">Selected work · Case studies</p>
    <h2>SEO work that <em>actually grows.</em></h2>
    <p class="km-lede">Real search programs from India and the UAE. Clicks, leads, and revenue from the portfolio — not vanity metrics.</p>
    <div class="km-work">
      <a class="km-work-card" href="/work/brand-with-salman/">
        <img src="/wp-content/uploads/work/brand-with-salman.jpg" alt="Brand with Salman">
        <div class="copy"><span class="km-chip">Personal branding SEO</span><h3>Brand with Salman</h3><p>201 → 2.57K organic clicks and 303 → 378K impressions over 1.5 years.</p></div>
      </a>
      <a class="km-work-card" href="/work/green-oasis/">
        <img src="/wp-content/uploads/work/green-oasis.jpg" alt="Green Oasis Travel">
        <div class="copy"><span class="km-chip">Travel SEO</span><h3>Green Oasis Travel</h3><p>11.6K organic clicks, 813K impressions, and 500+ qualified leads in 12 months.</p></div>
      </a>
      <a class="km-work-card" href="/work/grand-bake/">
        <img src="/wp-content/uploads/work/grand-bake.jpg" alt="Grand Bake">
        <div class="copy"><span class="km-chip">E-commerce SEO</span><h3>Grand Bake</h3><p>6.86K clicks, 268 organic orders, and AED 47,585+ in revenue.</p></div>
      </a>
      <a class="km-work-card" href="/work/dexito-branding/">
        <img src="/wp-content/uploads/work/dexito.jpg" alt="dExito Branding">
        <div class="copy"><span class="km-chip">Agency SEO</span><h3>dExito Branding</h3><p>145 → 21.7K clicks and 998 → 1.38M impressions in 1.5 years.</p></div>
      </a>
    </div>
    <a class="km-more" href="/work/aurevo-interiors/">More work: Aurevo, ZAQRT, Al Tawakkal, Crink.app, Ameen Ahsan →</a>
  </section>

  <section class="km-section" id="services">
    <p class="km-kicker">Services · What I do</p>
    <h2>Services that move <em>rankings, not slides.</em></h2>
    <p class="km-lede">Three focused areas: search, digital marketing, and websites that are built to rank.</p>
    <div class="km-services">
      <article class="km-svc">
        <div class="km-svc-top"><span>01</span><span class="km-ico">↗</span></div>
        <h3>SEO</h3>
        <p>Technical SEO, on-page, off-page, local SEO, GEO, AEO, and AI search for India and the UAE.</p>
        <ul><li>Search Console growth</li><li>Local &amp; GBP SEO</li><li>Content that ranks</li><li>GEO / AI Overviews</li></ul>
      </article>
      <article class="km-svc">
        <div class="km-svc-top"><span>02</span><span class="km-ico">+</span></div>
        <h3>Digital Marketing</h3>
        <p>Helping businesses build a stronger online presence and grow through effective digital strategies.</p>
        <ul><li>Brand visibility</li><li>India &amp; UAE markets</li><li>Social &amp; ads support</li><li>Lead generation</li></ul>
      </article>
      <article class="km-svc">
        <div class="km-svc-top"><span>03</span><span class="km-ico">◻</span></div>
        <h3>Web Development</h3>
        <p>WordPress and custom sites with SEO-friendly structure, content, and performance.</p>
        <ul><li>WordPress builds</li><li>Wix to Astro migrations</li><li>On-page architecture</li><li>E-commerce structure</li></ul>
      </article>
      <a class="km-svc km-svc-cta" href="/contact/">
        <div>
          <div class="km-svc-top"><span>Next</span><span class="km-ico">→</span></div>
          <h3>Got a project in mind?</h3>
          <p>Tell me what the business needs. WhatsApp or email — I usually reply within a day.</p>
        </div>
        <strong>Start a conversation →</strong>
      </a>
    </div>
  </section>

  <section class="km-section" id="about">
    <p class="km-kicker">About</p>
    <h2>SEO from Kerala and Dubai, focused on measurable growth.</h2>
    <div class="km-about">
      <div class="km-about-visual">
        <img src="/wp-content/uploads/work/aurevo.jpg" alt="Web and SEO work">
      </div>
      <div>
        <p class="km-meta">Muhammed Fawas · SEO Specialist · Al Qusais, Dubai · Immediate joiner</p>
        <p class="km-lede" style="margin-bottom:0">I'm an SEO Specialist with 2.5+ years of experience driving organic growth for businesses across India and the UAE. Technical SEO, on-page and off-page, local SEO, AEO, GEO, AI search, and WordPress development.</p>
        <div class="km-stats">
          <div class="km-stat"><b>2.5+</b><span>Years of SEO</span></div>
          <div class="km-stat"><b>20+</b><span>Websites managed</span></div>
          <div class="km-stat"><b>15+</b><span>GBPs optimized</span></div>
        </div>
        <div class="km-caps">
          <div class="km-cap"><h4>Technical SEO</h4><p>Architecture, indexing, Core Web Vitals, and migrations including Wix to Astro.</p></div>
          <div class="km-cap"><h4>Local SEO</h4><p>Google Business Profiles and location pages across India and the UAE.</p></div>
          <div class="km-cap"><h4>GEO &amp; AI search</h4><p>Visibility in ChatGPT, Google AI Overviews, Claude, and Perplexity.</p></div>
          <div class="km-cap"><h4>Web</h4><p>WordPress, custom builds, and e-commerce structure that supports SEO.</p></div>
        </div>
      </div>
    </div>
  </section>

  <section class="km-wrap km-cta" id="contact">
    <h2>Got a project that needs to rank?</h2>
    <p>Tell me what you're trying to grow. I'll tell you honestly whether I can help. No pitch decks.</p>
    <div class="km-ctas">
      <a class="km-btn km-btn-fill" href="https://wa.me/971528481743" target="_blank" rel="noopener">WhatsApp directly</a>
      <a class="km-btn km-btn-ghost" href="mailto:muhammedfawaas@gmail.com">muhammedfawaas@gmail.com</a>
    </div>
  </section>
</div>
</article>
"""


def main() -> None:
    t = INDEX.read_text(encoding="utf-8")
    a = t.find("<article ")
    b = t.find("</article>")
    if a < 0 or b < 0:
        raise SystemExit("article markers missing")
    t = t[:a] + HOME + t[b + len("</article>") :]

    if 'id="fawas-kalam-home"' in t:
        t = t.replace(
            t[t.find('<style id="fawas-kalam-home">') : t.find("</style>", t.find('id="fawas-kalam-home"')) + 8],
            f'<style id="fawas-kalam-home">{CSS}</style>',
        )
    else:
        t = t.replace("</style>\n</head>", f'</style>\n<style id="fawas-kalam-home">{CSS}</style>\n</head>', 1)
        if 'id="fawas-kalam-home"' not in t:
            t = t.replace('<style id="fawas-content">', f'<style id="fawas-kalam-home">{CSS}</style>\n<style id="fawas-content">', 1)

    INDEX.write_text(t, encoding="utf-8")
    print("homepage rebuilt", INDEX.stat().st_size)


if __name__ == "__main__":
    main()
