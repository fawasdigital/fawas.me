"""Polish the static Fawas site: layout, case studies, URLs, leftover theme junk."""

from __future__ import annotations

import html
import re
import shutil
from pathlib import Path

DIST = Path(__file__).resolve().parent / "dist"

PROJECTS = [
    {
        "slug": "brand-with-salman",
        "title": "Brand with Salman",
        "cat": "Personal Branding SEO",
        "filter": "seo",
        "site": "brandwithsalman.com",
        "url": "https://brandwithsalman.com",
        "cover": "/wp-content/uploads/work/brand-with-salman.jpg",
        "images": [
            "/wp-content/uploads/work/brand-with-salman.jpg",
            "/wp-content/uploads/work/brand-with-salman-2.jpg",
        ],
        "meta": "Personal branding & performance marketing · India, UAE · 1.5 years",
        "summary": "Over 1.5 years, a targeted personal branding SEO strategy delivered consistent organic growth for Salmanul Faris, increasing performance from 201 clicks to 2.57K clicks and 303 to 378K impressions.",
        "body": [
            "High-intent keywords achieved and maintained strong rankings across Kerala, Dubai, and the UAE, driving 100+ qualified inbound leads, including international clients.",
            "The approach combined search-intent mapping, GEO-focused local optimization, authority-building content, and AI search visibility across ChatGPT, Claude, Perplexity, and Google AI Overviews.",
        ],
        "stats": [
            ("201 → 2.57K", "Organic clicks"),
            ("303 → 378K", "Impressions"),
            ("100+", "Inbound leads"),
        ],
    },
    {
        "slug": "green-oasis",
        "title": "Green Oasis Travel",
        "cat": "Travel SEO",
        "filter": "seo",
        "site": "greenoasistravel.com",
        "url": "https://greenoasistravel.com",
        "cover": "/wp-content/uploads/work/green-oasis.jpg",
        "images": [
            "/wp-content/uploads/work/green-oasis.jpg",
            "/wp-content/uploads/work/green-oasis-2.jpg",
        ],
        "meta": "Travel & tourism · Kerala, India · 12 months",
        "summary": "With the launch of an SEO-optimized website and a focused growth strategy, Green Oasis recorded 11.6K organic clicks and 813K organic impressions within one year.",
        "body": [
            "Service pages, travel packages, and informational blogs emerged as key traffic drivers, generating 500+ qualified leads.",
            "Core service queries such as travel agency in Kerala, Turkey packages from Kerala, and international tour packages ranked in the top results.",
        ],
        "stats": [
            ("11.6K", "Organic clicks"),
            ("813K", "Impressions"),
            ("500+", "Qualified leads"),
        ],
    },
    {
        "slug": "grand-bake",
        "title": "Grand Bake",
        "cat": "E-commerce SEO",
        "filter": "ecommerce",
        "site": "grandbake.com",
        "url": "https://grandbake.com",
        "cover": "/wp-content/uploads/work/grand-bake.jpg",
        "images": [
            "/wp-content/uploads/work/grand-bake.jpg",
            "/wp-content/uploads/work/grand-bake-2.jpg",
        ],
        "meta": "E-commerce bakery · Dubai, UAE · 5 months",
        "summary": "A focused e-commerce and local SEO strategy delivered 6.86K organic clicks, 268 organic orders, and AED 47,585+ in revenue.",
        "body": [
            "Category pages including croissants, cakes, Arabic sweets, and frozen foods became top traffic and revenue drivers.",
            "Google Business Profile visibility improved local discovery across Dubai, Abu Dhabi, and Sharjah.",
        ],
        "stats": [
            ("6.86K", "Organic clicks"),
            ("268", "Organic orders"),
            ("AED 47,585+", "Revenue"),
        ],
    },
    {
        "slug": "dexito-branding",
        "title": "dExito Branding",
        "cat": "Agency SEO",
        "filter": "seo",
        "site": "dexitobranding.com",
        "url": "https://dexitobranding.com",
        "cover": "/wp-content/uploads/work/dexito.jpg",
        "images": [
            "/wp-content/uploads/work/dexito.jpg",
            "/wp-content/uploads/work/dexito-2.jpg",
        ],
        "meta": "Digital marketing · Kerala, India · 1.5 years",
        "summary": "The SEO-optimized website scaled from 145 clicks and 998 impressions to 21.7K clicks and 1.38M impressions in 1.5 years.",
        "body": [
            "Core service pages, strategic content, and targeted SEO optimization were the primary traffic drivers.",
            "The work strengthened search rankings, user engagement, and the agency's position in the Kerala market.",
        ],
        "stats": [
            ("145 → 21.7K", "Organic clicks"),
            ("998 → 1.38M", "Impressions"),
            ("1.5 yrs", "SEO program"),
        ],
    },
    {
        "slug": "aurevo-interiors",
        "title": "Aurevo Interiors",
        "cat": "Web Development",
        "filter": "web",
        "site": "aurevointeriors.com",
        "url": "https://aurevointeriors.com",
        "cover": "/wp-content/uploads/work/aurevo.jpg",
        "images": ["/wp-content/uploads/work/aurevo.jpg"],
        "meta": "Interior design · Kerala, India · Ongoing",
        "summary": "Managed and updated the Aurevo Interiors website, focusing on development, page optimization, content updates, and user experience.",
        "body": [
            "Worked on SEO-friendly architecture, on-page optimization, and content structure to strengthen search visibility.",
            "Kept performance, content, and website improvements aligned with SEO best practices and business objectives.",
        ],
        "stats": [],
    },
    {
        "slug": "zaqrt",
        "title": "ZAQRT",
        "cat": "E-commerce Migration",
        "filter": "web",
        "site": "zaqrt.com",
        "url": "https://zaqrt.com",
        "cover": "/wp-content/uploads/work/zaqrt.jpg",
        "images": ["/wp-content/uploads/work/zaqrt.jpg"],
        "meta": "E-commerce & online retail · Saudi Arabia · WordPress to custom-built",
        "summary": "Worked on migrating the ZAQRT e-commerce website from WordPress to a custom-built site, focusing on structure and shopping functionality.",
        "body": [
            "Supported the transition from WordPress to a custom architecture to improve flexibility, usability, and the shopping experience.",
            "Maintained content structure and aligned the new website with e-commerce requirements and digital growth objectives.",
        ],
        "stats": [],
    },
    {
        "slug": "al-tawakkal",
        "title": "Al Tawakkal",
        "cat": "SEO Consulting",
        "filter": "seo",
        "site": "altawakkal.ae",
        "url": "https://altawakkal.ae",
        "cover": "/wp-content/uploads/work/al-tawakkal.jpg",
        "images": ["/wp-content/uploads/work/al-tawakkal.jpg"],
        "meta": "Business setup consultancy · UAE · 3 months",
        "summary": "SEO consulting for a UAE business setup firm. Organic clicks increased from 8.11K to 12.9K (+59.1%) and impressions from 1.12M to 1.35M (+20.5%).",
        "body": [
            "The project covered strategy recommendations, blog optimization, content reviews, on-page improvements, off-page SEO, and outreach.",
            "Visibility improved across business-setup search queries in the UAE.",
        ],
        "stats": [
            ("8.11K → 12.9K", "Organic clicks"),
            ("+59.1%", "Click growth"),
            ("1.12M → 1.35M", "Impressions"),
        ],
    },
    {
        "slug": "crink-app",
        "title": "Crink.app",
        "cat": "Healthcare SEO",
        "filter": "seo",
        "site": "crink.app",
        "url": "https://crink.app",
        "cover": "/wp-content/uploads/work/crink.jpg",
        "images": [
            "/wp-content/uploads/work/crink.jpg",
            "/wp-content/uploads/work/crink-2.jpg",
        ],
        "meta": "Mental health & wellness · Kerala, India · 2 months",
        "summary": "Developed and executed SEO for Crink.app, covering website architecture, technical SEO, content optimization, and organic growth in a YMYL category.",
        "body": [
            "The strategy strengthened topical authority and discoverability across AI-powered search, including ChatGPT, Google AI Overviews, and Perplexity.",
            "Migrated the website from Wix to Astro using AI-assisted development, with a focus on E-E-A-T and technical SEO.",
        ],
        "stats": [],
    },
    {
        "slug": "ameen-ahsan",
        "title": "Ameen Ahsan",
        "cat": "Personal Branding SEO",
        "filter": "seo",
        "site": "ameenahsan.com",
        "url": "https://ameenahsan.com",
        "cover": "/wp-content/uploads/work/ameen-ahsan.jpg",
        "images": ["/wp-content/uploads/work/ameen-ahsan.jpg"],
        "meta": "Family business consulting · Dubai, UAE · 3 months",
        "summary": "In three months, the website grew from 54 to 158 clicks and 1.19K to 2.61K impressions for Dubai's micro-niche audience.",
        "body": [
            "The site ranks on page 3 for key family-business consulting terms, with stronger Google AI Overview and multi-LLM visibility.",
            "Ameen Ahsan is a Dubai-based family business and strategy consultant with 20+ years of experience.",
        ],
        "stats": [
            ("54 → 158", "Organic clicks"),
            ("1.19K → 2.61K", "Impressions"),
            ("3 months", "SEO program"),
        ],
    },
]

CSS = """
.fawas-wordmark{display:inline-block;font-weight:700;font-size:22px;letter-spacing:-.04em;color:#fff;line-height:1;text-decoration:none}
a.dtr-logo{text-decoration:none}
img[src*="me-2.jpg"]{visibility:hidden}
.dtr-feature-highlight__icon:has(img[src*="me-2.jpg"]){position:relative;background:#1a1a1a;border-radius:50%}
.dtr-feature-highlight__icon:has(img[src*="me-2.jpg"])::after{content:"MF";position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font-weight:700;color:#fff}
.elementor-9 .elementor-element.elementor-element-5b410c0:not(.elementor-motion-effects-element-type-background),
.elementor-9 .elementor-element.elementor-element-5b410c0 > .elementor-motion-effects-container > .elementor-motion-effects-layer{background-image:none!important;background-color:#1a1a1a!important}
.elementor-element-5b410c0{position:relative}
.elementor-element-5b410c0::after{content:"MF";position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:28px;letter-spacing:-.04em;color:#fff}
.fawas-brand{display:flex;align-items:center;justify-content:center;min-height:48px;padding:8px 12px;color:#fff;font-weight:600;font-size:15px;letter-spacing:-.02em;text-align:center}
.dtr-testimonial__client-img,.dtr-timeline__icon{display:none!important}
.dtr-timeline__heading{margin:0 0 4px}
.dtr-portfolio-item__wrapper{overflow:hidden}
.dtr-portfolio-item__img{position:relative;aspect-ratio:16/10;min-height:240px;background:#1a1a1a;overflow:hidden}
.dtr-portfolio-item__img img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;display:block;opacity:1!important;visibility:visible!important}
.dtr-portfolio-item__img .dtr-overlay{background:linear-gradient(180deg,rgba(0,0,0,.12) 20%,rgba(0,0,0,.72) 100%)!important;opacity:1!important}
.dtr-portfolio-item:hover .dtr-portfolio-item__img .dtr-overlay{background:linear-gradient(180deg,rgba(0,0,0,.08) 10%,rgba(0,0,0,.82) 100%)!important}
.dtr-filter-nav-wrapper{display:flex!important;justify-content:center;margin:8px 0 28px}
.dtr-filter-nav{display:flex;flex-wrap:wrap;gap:8px;justify-content:center}
img[src*="Figma"],img[src*="Illustrator"],img[src*="framer"],img[src*="html-"],img[src*="Sketch"],img[src*="notion"],img[src*="webflow"],img[src*="Slack"],img[src*="wordpress-"],img[src*="angular"],img[src*="visual-studio"],img[src*="nextjs"],img[src*="premier-pro"],img[src*="capcut"],img[src*="adobe-audition"],img[src*="davinci"],img[alt="Figma"],img[alt="Adobe Illustrator"]{display:none!important}
.fawas-stat{display:block;font-size:clamp(1.5rem,3vw,2.6rem);font-weight:700;line-height:1.1;letter-spacing:-.03em}
.fawas-case{max-width:980px;margin:48px auto 96px;padding:0 24px}
.fawas-case .meta{color:#8a8a8a;font-size:14px;margin:0 0 20px;line-height:1.6}
.fawas-case p{font-size:1.125rem;line-height:1.65;margin:0 0 16px}
.fawas-case img{width:100%;height:auto;border-radius:18px;margin:18px 0;background:#111;display:block}
.fawas-case a{color:#fff}
.fawas-stats{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin:8px 0 28px}
.fawas-stat-card{border:1px solid #222;border-radius:16px;padding:18px 16px;background:#111}
.fawas-stat-card b{display:block;font-size:1.35rem;letter-spacing:-.03em;margin-bottom:4px}
.fawas-stat-card span{color:#8a8a8a;font-size:13px}
.fawas-case-nav{display:flex;justify-content:space-between;gap:16px;margin-top:40px;padding-top:24px;border-top:1px solid #1c1c1c;font-size:15px}
.fawas-case-nav span{color:#555}
@media (max-width:720px){.fawas-stats{grid-template-columns:1fr}}
"""


def patch_css(text: str) -> str:
    return re.sub(
        r'<style id="fawas-content">.*?</style>',
        f'<style id="fawas-content">{CSS}</style>',
        text,
        count=1,
        flags=re.S,
    )


def patch_global(text: str) -> str:
    text = patch_css(text)
    text = text.replace("/about-page/", "/about/")
    text = text.replace("/contact-page/", "/contact/")
    text = text.replace("Mellow &raquo; Feed", "Muhammed Fawas &raquo; Feed")
    text = text.replace("Mellow &raquo; Comments Feed", "Muhammed Fawas &raquo; Comments Feed")
    text = text.replace("title=\"Mellow\"", 'title="Muhammed Fawas"')
    text = text.replace("<p class=\"dtr-timeline__duration\"> Jun 2024 &mdash; Mar 2026 </p>", "<p class=\"dtr-timeline__duration\">Jun 2024 &mdash; Mar 2026</p>")
    text = text.replace("<p class=\"dtr-timeline__designation\">SEO Analyst </p>", "<p class=\"dtr-timeline__designation\">SEO Analyst</p>")
    return text


def add_heading_if_missing(text: str, unique: str, heading: str) -> str:
    if f">{html.escape(heading)}</h6>" in text and unique in text:
        # heading may already exist elsewhere; still add if unique block lacks it
        pass
    needle = unique
    if unique not in text:
        return text
    idx = text.find(unique)
    window = text[idx : idx + 400]
    if f">{heading}</h6>" in window or f">{html.escape(heading)}</h6>" in window:
        return text
    # insert heading after the icon wrapper, before closing .dtr-timeline__head
    head_close = text.find("</div>", idx)
    # find the head close after icon - typically `</div>\t\n\t\t\t\t\t\t\t</div>` after img
    # safer: after unique string, find first `</div>` then next `</div>` of head
    first = text.find("</div>", idx)
    second = text.find("</div>", first + 1)
    insert = f'\n\t\t\t\t\t\t\t\t\t\t\t\t\t<h6 class="dtr-timeline__heading">{html.escape(heading)}</h6>\n'
    return text[:second] + insert + text[second:]


def patch_timeline(text: str) -> str:
    pairs = [
        ("comp-2-r5qklcxr0qaba893o3vxbs2eat4zpcdl8odxz1lyps.png", "Crink.app"),
        ("comp-1-1-r5qkkmm9pdaecgs6t08v3dvhqsfjyzvcbr7wxvzz7k.png", "Acodez IT Solutions"),
        ("comp-3-r5qkxcdo5ooy4pjdntxdrc866f7fp1u16xnbqdauww.png", "WordCamp Kerala"),
        ("alma-3-r5qjw3ztfxq0lu8f4nfzpkegngg33e9i4rpwf5l2bk.png", "Aviv Digital Academy"),
        ("alma-1-r5qido6bmd77tsp3ype92z0sil1pzqwg975jrv83r4.png", "Availability"),
    ]
    for unique, heading in pairs:
        text = add_heading_if_missing(text, unique, heading)
    return text


def portfolio_grid() -> str:
    items = []
    for i, p in enumerate(PROJECTS):
        pri = ' fetchpriority="high"' if i == 0 else ' loading="lazy"'
        href = f"/work/{p['slug']}/"
        items.append(
            f'<div class="dtr-portfolio-item isotope-item {p["filter"]} all">'
            f'<div class="dtr-portfolio-item__wrapper dtr-radius--rounded">'
            f'<a class="dtr-portfolio-item__wrap-link" href="{href}" target="_self" aria-label="{html.escape(p["title"])}"></a>'
            f'<div class="dtr-portfolio-item__img"><div class="dtr-overlay"></div>'
            f'<img decoding="async"{pri} src="{p["cover"]}" class="attachment-full size-full wp-post-image" alt="{html.escape(p["title"])}" />'
            f'<a class="dtr-portfolio-item__link" href="{href}" target="_self" aria-label="{html.escape(p["title"])}">View project</a>'
            f'<div class="dtr-portfolio-item__content"><div class="dtr-portfolio-item__categories">'
            f'<span class="dtr-portfolio-item__category">{html.escape(p["cat"])}</span></div>'
            f'<h4 class="dtr-portfolio-item__heading"><a href="{href}" target="_self">{html.escape(p["title"])}</a></h4>'
            f"</div></div></div></div>"
        )
    nav = (
        '<div class="dtr-filter-nav-wrapper"><ul class="dtr-filter-nav dtr-filter-nav__center clearfix">'
        '<li><a class="dtr-filter-all active" data-filter="*" href="#">All</a></li>'
        '<li><a data-filter=".seo" href="#">SEO</a></li>'
        '<li><a data-filter=".ecommerce" href="#">E-commerce</a></li>'
        '<li><a data-filter=".web" href="#">Web</a></li>'
        "</ul></div>"
    )
    return nav + '<div class="dtr-portfolio-grid portfolio-style1 dtr-portfolio-masonry dtr-portfolio-grid-3col">' + "".join(items) + "</div>"


def patch_home_grid(text: str) -> str:
    start = text.find('<div class="dtr-filter-nav-wrapper">')
    end = text.find('<div class="elementor-element elementor-element-d648979')
    if start < 0:
        return text
    if end < 0:
        # fallback: end of portfolio parent after grid
        marker = '<div class="dtr-portfolio-grid'
        g = text.find(marker, start)
        # find closing after grid - too fragile; skip rebuild if about block missing
        return text
    return text[:start] + portfolio_grid() + text[end:]


def write_project_pages() -> None:
    template = (DIST / "about" / "index.html").read_text(encoding="utf-8")
    header_end = template.find('<div class="dtr-page-title--section')
    footer_start = template.find('<footer id="dtr-footer-section"')
    head = template[:header_end]
    foot = template[footer_start:]

    for i, p in enumerate(PROJECTS):
        prev_p = PROJECTS[i - 1] if i else None
        next_p = PROJECTS[i + 1] if i + 1 < len(PROJECTS) else None
        imgs = "".join(
            f'<img src="{src}" alt="{html.escape(p["title"])}" />' for src in p["images"]
        )
        paras = "".join(f"<p>{html.escape(b)}</p>" for b in p["body"])
        stats = ""
        if p["stats"]:
            cards = "".join(
                f'<div class="fawas-stat-card"><b>{html.escape(v)}</b><span>{html.escape(l)}</span></div>'
                for v, l in p["stats"]
            )
            stats = f'<div class="fawas-stats">{cards}</div>'
        prev_html = (
            f'<a href="/work/{prev_p["slug"]}/">← {html.escape(prev_p["title"])}</a>'
            if prev_p
            else "<span></span>"
        )
        next_html = (
            f'<a href="/work/{next_p["slug"]}/">{html.escape(next_p["title"])} →</a>'
            if next_p
            else "<span></span>"
        )
        body = f"""<div class="dtr-page-title--section text-center">
    <div class="dtr-page-title__overlay"></div>
    <div class="container">
        <div class="dtr-page-title__content">
            <h1 class="dtr-page-title">{html.escape(p["title"])}</h1>
        </div>
        <div class="dtr-breadcrumb-wrapper">
            <ul class="breadcrumbs">
                <li class="home"><a href="/" title="Home">Home</a></li>
                <li><a href="/#works">Work</a></li>
                <li>{html.escape(p["title"])}</li>
            </ul>
        </div>
    </div>
</div>
<div id="dtr-main-wrapper" class="clearfix dtr-fullwidth">
<main id="dtr-primary-section" class="dtr-content-area">
<article class="fawas-case">
<p class="meta">{html.escape(p["cat"])} · <a href="{html.escape(p["url"])}" target="_blank" rel="noopener">{html.escape(p["site"])}</a><br>{html.escape(p["meta"])}</p>
<p>{html.escape(p["summary"])}</p>
{stats}
{paras}
{imgs}
<div class="fawas-case-nav">{prev_html}{next_html}</div>
<p><a href="/#works">Back to work</a> · <a href="/contact/">Connect</a> · <a href="/muhammed-fawas-seo-specialist-resume.pdf">Download resume</a></p>
</article>
</main>
</div>
"""
        page = re.sub(
            r"<title>.*?</title>",
            f"<title>{html.escape(p['title'])} &#8211; Muhammed Fawas</title>",
            head,
            count=1,
        )
        page = page.replace(
            '<link rel="canonical" href="/about/" />',
            f'<link rel="canonical" href="/work/{p["slug"]}/" />',
        )
        out = DIST / "work" / p["slug"] / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(page + body + foot, encoding="utf-8")
        print("wrote", out.relative_to(DIST))


def copy_pretty_urls() -> None:
    for src, dest in (("about-page", "about"), ("contact-page", "contact")):
        s = DIST / src
        d = DIST / dest
        if not s.exists():
            continue
        src_index = (s / "index.html").read_text(encoding="utf-8") if (s / "index.html").exists() else ""
        if "Redirecting" in src_index and d.exists():
            continue
        if d.exists():
            shutil.rmtree(d)
        shutil.copytree(s, d)


def write_redirect(path: Path, target: str) -> None:
    path.mkdir(parents=True, exist_ok=True)
    (path / "index.html").write_text(
        f"""<!DOCTYPE html><html lang="en"><head>
<meta charset="utf-8"><meta http-equiv="refresh" content="0;url={target}">
<link rel="canonical" href="{target}">
<title>Redirecting</title>
<script>location.replace({target!r})</script>
</head><body><p><a href="{target}">Continue</a></p></body></html>
""",
        encoding="utf-8",
    )


def stub_demo_pages() -> None:
    write_redirect(DIST / "about-page", "/about/")
    write_redirect(DIST / "contact-page", "/contact/")
    for folder in (
        "blog",
        "portfolio",
        "services",
        "seo-services",
        "product-design",
        "ui-ux-design",
        "brand-strategy",
        "author",
        "tag",
        "category",
        "dtr_portfoliotags",
    ):
        root = DIST / folder
        if not root.exists():
            continue
        for html_file in root.rglob("index.html"):
            html_file.write_text(
                """<!DOCTYPE html><html lang="en"><head>
<meta charset="utf-8"><meta http-equiv="refresh" content="0;url=/">
<meta name="robots" content="noindex,nofollow">
<title>Redirecting</title>
<script>location.replace("/")</script>
</head><body><p><a href="/">Home</a></p></body></html>
""",
                encoding="utf-8",
            )
    for html_file in DIST.glob("style-*/index.html"):
        html_file.write_text(
            """<!DOCTYPE html><html lang="en"><head>
<meta charset="utf-8"><meta http-equiv="refresh" content="0;url=/">
<meta name="robots" content="noindex,nofollow"><title>Redirecting</title>
<script>location.replace("/")</script></head><body><p><a href="/">Home</a></p></body></html>
""",
            encoding="utf-8",
        )
    (DIST / "robots.txt").write_text(
        "User-agent: *\nAllow: /\nDisallow: /blog/\nDisallow: /portfolio/\nDisallow: /tag/\nDisallow: /category/\nDisallow: /author/\n",
        encoding="utf-8",
    )


def main() -> None:
    copy_pretty_urls()
    for path in DIST.rglob("*.html"):
        rel = path.relative_to(DIST).as_posix()
        if rel.startswith(("blog/", "portfolio/", "tag/", "category/", "author/", "dtr_portfoliotags/", "style-")):
            continue
        if rel in {"about-page/index.html", "contact-page/index.html"}:
            continue
        text = path.read_text(encoding="utf-8")
        updated = patch_global(text)
        if path == DIST / "index.html" or path == DIST / "about" / "index.html":
            updated = patch_timeline(updated)
        if updated != text:
            path.write_text(updated, encoding="utf-8")
    write_project_pages()
    stub_demo_pages()
    print("polish complete")


if __name__ == "__main__":
    main()
