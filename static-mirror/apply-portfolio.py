"""Inject resume + portfolio PDF content and images into the static site."""

from pathlib import Path
import html
import re
import shutil

DIST = Path(__file__).resolve().parent / "dist"
ROOT = DIST.parent.parent

PROJECTS = [
    {
        "slug": "brand-with-salman",
        "title": "Brand with Salman",
        "cat": "Personal Branding SEO",
        "filter": "seo",
        "site": "brandwithsalman.com",
        "cover": "/wp-content/uploads/work/brand-with-salman.jpg",
        "images": [
            "/wp-content/uploads/work/brand-with-salman.jpg",
            "/wp-content/uploads/work/brand-with-salman-2.jpg",
        ],
        "meta": "Industry: Personal branding & performance marketing · Market: India, UAE · Duration: 1.5 years",
        "summary": "Over 1.5 years, a targeted personal branding SEO strategy delivered consistent organic growth for Salmanul Faris, increasing performance from 201 clicks to 2.57K clicks and 303 to 378K impressions.",
        "body": [
            "High-intent keywords achieved and maintained strong rankings across Kerala, Dubai, and the UAE, driving 100+ qualified inbound leads, including international clients.",
            "The approach combined search-intent mapping, GEO-focused local optimization, authority-building content, and AI search visibility across ChatGPT, Claude, Perplexity, and Google AI Overviews.",
        ],
    },
    {
        "slug": "green-oasis",
        "title": "Green Oasis Travel",
        "cat": "Travel SEO",
        "filter": "seo",
        "site": "greenoasistravel.com",
        "cover": "/wp-content/uploads/work/green-oasis.jpg",
        "images": [
            "/wp-content/uploads/work/green-oasis.jpg",
            "/wp-content/uploads/work/green-oasis-2.jpg",
        ],
        "meta": "Industry: Travel & tourism · Market: Kerala, India · Duration: 12 months",
        "summary": "With the launch of an SEO-optimized website and a focused growth strategy, Green Oasis recorded 11.6K organic clicks and 813K organic impressions within one year.",
        "body": [
            "Service pages, travel packages, and informational blogs emerged as key traffic drivers, generating 500+ qualified leads.",
            "Core service queries such as travel agency in Kerala, Turkey packages from Kerala, and international tour packages ranked in the top results.",
        ],
    },
    {
        "slug": "grand-bake",
        "title": "Grand Bake",
        "cat": "E-commerce SEO",
        "filter": "ecommerce",
        "site": "grandbake.com",
        "cover": "/wp-content/uploads/work/grand-bake.jpg",
        "images": [
            "/wp-content/uploads/work/grand-bake.jpg",
            "/wp-content/uploads/work/grand-bake-2.jpg",
        ],
        "meta": "Industry: E-commerce bakery · Market: Dubai, UAE · Duration: 5 months",
        "summary": "A focused e-commerce and local SEO strategy delivered 6.86K organic clicks, 268 organic orders, and AED 47,585+ in revenue.",
        "body": [
            "Category pages including croissants, cakes, Arabic sweets, and frozen foods became top traffic and revenue drivers.",
            "Google Business Profile visibility improved local discovery across Dubai, Abu Dhabi, and Sharjah.",
        ],
    },
    {
        "slug": "dexito-branding",
        "title": "dExito Branding",
        "cat": "Agency SEO",
        "filter": "seo",
        "site": "dexitobranding.com",
        "cover": "/wp-content/uploads/work/dexito.jpg",
        "images": [
            "/wp-content/uploads/work/dexito.jpg",
            "/wp-content/uploads/work/dexito-2.jpg",
        ],
        "meta": "Industry: Digital marketing · Market: Kerala, India · Duration: 1.5 years",
        "summary": "The SEO-optimized website scaled from 145 clicks and 998 impressions to 21.7K clicks and 1.38M impressions in 1.5 years.",
        "body": [
            "Core service pages, strategic content, and targeted SEO optimization were the primary traffic drivers.",
            "The work strengthened search rankings, user engagement, and the agency's position in the Kerala market.",
        ],
    },
    {
        "slug": "aurevo-interiors",
        "title": "Aurevo Interiors",
        "cat": "Web Development",
        "filter": "web",
        "site": "aurevointeriors.com",
        "cover": "/wp-content/uploads/work/aurevo.jpg",
        "images": ["/wp-content/uploads/work/aurevo.jpg"],
        "meta": "Industry: Interior design · Market: Kerala, India · Duration: Ongoing",
        "summary": "Managed and updated the Aurevo Interiors website, focusing on development, page optimization, content updates, and user experience.",
        "body": [
            "Worked on SEO-friendly architecture, on-page optimization, and content structure to strengthen search visibility.",
            "Kept performance, content, and website improvements aligned with SEO best practices and business objectives.",
        ],
    },
    {
        "slug": "zaqrt",
        "title": "ZAQRT",
        "cat": "E-commerce Migration",
        "filter": "web",
        "site": "zaqrt.com",
        "cover": "/wp-content/uploads/work/zaqrt.jpg",
        "images": ["/wp-content/uploads/work/zaqrt.jpg"],
        "meta": "Industry: E-commerce & online retail · Market: Saudi Arabia · Platform: WordPress to custom-built",
        "summary": "Worked on migrating the ZAQRT e-commerce website from WordPress to a custom-built site, focusing on structure and shopping functionality.",
        "body": [
            "Supported the transition from WordPress to a custom architecture to improve flexibility, usability, and the shopping experience.",
            "Maintained content structure and aligned the new website with e-commerce requirements and digital growth objectives.",
        ],
    },
    {
        "slug": "al-tawakkal",
        "title": "Al Tawakkal",
        "cat": "SEO Consulting",
        "filter": "seo",
        "site": "altawakkal.ae",
        "cover": "/wp-content/uploads/work/al-tawakkal.jpg",
        "images": ["/wp-content/uploads/work/al-tawakkal.jpg"],
        "meta": "Industry: Business setup consultancy · Market: UAE · Duration: 3 months",
        "summary": "SEO consulting for a UAE business setup firm. Organic clicks increased from 8.11K to 12.9K (+59.1%) and impressions from 1.12M to 1.35M (+20.5%).",
        "body": [
            "The project covered strategy recommendations, blog optimization, content reviews, on-page improvements, off-page SEO, and outreach.",
            "Visibility improved across business-setup search queries in the UAE.",
        ],
    },
    {
        "slug": "crink-app",
        "title": "Crink.app",
        "cat": "Healthcare SEO",
        "filter": "seo",
        "site": "crink.app",
        "cover": "/wp-content/uploads/work/crink.jpg",
        "images": [
            "/wp-content/uploads/work/crink.jpg",
            "/wp-content/uploads/work/crink-2.jpg",
        ],
        "meta": "Industry: Mental health & wellness · Market: Kerala, India · Duration: 2 months",
        "summary": "Developed and executed SEO for Crink.app, covering website architecture, technical SEO, content optimization, and organic growth in a YMYL category.",
        "body": [
            "The strategy strengthened topical authority and discoverability across AI-powered search, including ChatGPT, Google AI Overviews, and Perplexity.",
            "Migrated the website from Wix to Astro using AI-assisted development, with a focus on E-E-A-T and technical SEO.",
        ],
    },
    {
        "slug": "ameen-ahsan",
        "title": "Ameen Ahsan",
        "cat": "Personal Branding SEO",
        "filter": "seo",
        "site": "ameenahsan.com",
        "cover": "/wp-content/uploads/work/ameen-ahsan.jpg",
        "images": ["/wp-content/uploads/work/ameen-ahsan.jpg"],
        "meta": "Industry: Family business consulting · Market: Dubai, UAE · Duration: 3 months",
        "summary": "In three months, the website grew from 54 to 158 clicks and 1.19K to 2.61K impressions for Dubai's micro-niche audience.",
        "body": [
            "The site ranks on page 3 for key family-business consulting terms, with stronger Google AI Overview and multi-LLM visibility.",
            "Ameen Ahsan is a Dubai-based family business and strategy consultant with 20+ years of experience.",
        ],
    },
]


CSS_OLD = """.dtr-portfolio-item__img img,.dtr-testimonial__client-img,.dtr-post-block__img-wrapper img,.dtr-timeline__icon img{opacity:0}
.dtr-portfolio-item__img,.dtr-post-block__img-wrapper{background:#1a1a1a;min-height:180px}"""

CSS_NEW = """.dtr-testimonial__client-img,.dtr-timeline__icon img{opacity:0}
.dtr-portfolio-item__img{background:#111;min-height:220px;overflow:hidden}
.dtr-portfolio-item__img img{width:100%;height:100%;object-fit:cover;display:block;opacity:1}
.dtr-filter-nav-wrapper{display:flex!important;justify-content:center}
.fawas-case{max-width:980px;margin:48px auto 96px;padding:0 24px}
.fawas-case .meta{color:#8a8a8a;font-size:14px;margin:0 0 20px}
.fawas-case p{font-size:1.125rem;line-height:1.6}
.fawas-case img{width:100%;height:auto;border-radius:18px;margin:18px 0;background:#111}
.fawas-case a{color:#fff}"""


def replace_between(html_text, start, end, new):
    i = html_text.find(start)
    j = html_text.find(end, i)
    if i < 0 or j < 0:
        raise SystemExit(f"markers missing: {start!r}")
    return html_text[:i] + new + html_text[j:]


def portfolio_grid():
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
            f'<h4 class="dtr-portfolio-item__heading"><a href="{href}" target="_self" aria-label="{html.escape(p["title"])}">{html.escape(p["title"])}</a></h4>'
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


def patch_css(text):
    if CSS_OLD in text:
        text = text.replace(CSS_OLD, CSS_NEW)
    elif ".fawas-case{" not in text and "style id=\"fawas-content\"" in text:
        text = text.replace(".dtr-recentposts-carousel .dtr-post-block__meta{display:none}", ".dtr-recentposts-carousel .dtr-post-block__meta{display:none}\n" + CSS_NEW)
    return text


def patch_experience(text):
    text = text.replace("Jan 2026 &mdash; Present", "Apr 2026 &mdash; Jun 2026")
    text = text.replace(
        '<div class="dtr-timeline__content">Aurevo Interiors · Kakkad, Kerala · Hybrid</div>',
        '<div class="dtr-timeline__content">Crink.app · Kochi · Technical SEO, E-E-A-T, Wix to Astro migration</div>',
    )
    text = text.replace(
        '<h6 class="dtr-timeline__heading">Crink.app</h6>',
        '<h6 class="dtr-timeline__heading">dExito Branding</h6>',
    )
    text = text.replace(" Apr 2026 &mdash; Jun 2026 ", " Jun 2024 &mdash; Mar 2026 ")
    text = text.replace(
        "<p class=\"dtr-timeline__designation\">SEO Specialist </p>\n\t\t\t\n\t\t\t\t\t\t\t\t<div class=\"dtr-timeline__content\">Kochi, Kerala · On-site</div>",
        "<p class=\"dtr-timeline__designation\">SEO Analyst </p>\n\t\t\t\n\t\t\t\t\t\t\t\t<div class=\"dtr-timeline__content\">Calicut · eCommerce and travel clients across India and the UAE</div>",
    )
    text = text.replace("Jun 2024 &mdash; Dec 2025", "Mar 2024 &mdash; May 2024")
    text = text.replace(
        "<p class=\"dtr-timeline__designation\">SEO Analyst</p>\n\t\t\t<div class=\"dtr-timeline__content\">dExito Branding · Calicut, Kerala · On-site</div>",
        "<p class=\"dtr-timeline__designation\">Digital Marketing Executive</p>\n\t\t\t<div class=\"dtr-timeline__content\">Acodez IT Solutions · Internship · SEO, social, Google Ads, Meta Ads</div>",
    )
    # fourth item was intern - change to volunteer
    text = text.replace("Mar 2024 &mdash; May 2024", "2024")
    text = text.replace(
        "<p class=\"dtr-timeline__designation\">Intern</p>\n\t\t\t\n\t\t\t\t\t\t\t\t<div class=\"dtr-timeline__content\">Acodez IT Solutions · Calicut, Kerala · On-site</div>",
        "<p class=\"dtr-timeline__designation\">Volunteer</p>\n\t\t\t\n\t\t\t\t\t\t\t\t<div class=\"dtr-timeline__content\">WordCamp Kerala 2024 · Community projects and local initiatives</div>",
    )

    text = text.replace("<p class=\"dtr-subheading\">Based in</p>", "<p class=\"dtr-subheading\">Education</p>")
    text = text.replace(
        "<p class=\"dtr-timeline__duration\">Dubai</p>\n\t\t\t\n\t\t\t\t\t\t\t<p class=\"dtr-timeline__designation\">Al Qusais, United Arab Emirates</p>\n\t\t\t\n\t\t\t\t\t\t\t\t<div class=\"dtr-timeline__content\">Al Qusais, Dubai, United Arab Emirates</div>",
        "<p class=\"dtr-timeline__duration\">Aug 2023 &mdash; Feb 2024</p>\n\t\t\t\n\t\t\t\t\t\t\t<p class=\"dtr-timeline__designation\">Diploma in Digital Marketing</p>\n\t\t\t\n\t\t\t\t\t\t\t\t<div class=\"dtr-timeline__content\">Aviv Digital Academy</div>",
    )
    text = text.replace('<h6 class="dtr-timeline__heading">Kerala, India</h6>', '<h6 class="dtr-timeline__heading">GMHSS CU Campus</h6>')
    text = text.replace(
        "<p class=\"dtr-timeline__duration\">India</p>\n\t\t\t\n\t\t\t\t\t\t\t<p class=\"dtr-timeline__designation\">Also based in Kerala, India</p>\n\t\t\t\n\t\t\t\t\t\t\t\t<div class=\"dtr-timeline__content\">Usually replies within a day.</div>",
        "<p class=\"dtr-timeline__duration\">Jun 2018 &mdash; Apr 2020</p>\n\t\t\t\n\t\t\t\t\t\t\t<p class=\"dtr-timeline__designation\">Higher Secondary, Humanities</p>\n\t\t\t\n\t\t\t\t\t\t\t\t<div class=\"dtr-timeline__content\">GMHSS CU Campus School</div>",
    )
    text = text.replace(
        "<p class=\"dtr-timeline__duration\">Available</p>\n\t\t\t\n\t\t\t\t\t\t\t<p class=\"dtr-timeline__designation\">Usually replies within a day</p>\n\t\t\t\n\t\t\t\t\t\t\t\t<div class=\"dtr-timeline__content\">Open to conversations, opportunities, and collaborations.</div>",
        "<p class=\"dtr-timeline__duration\">Al Qusais, Dubai</p>\n\t\t\t\n\t\t\t\t\t\t\t<p class=\"dtr-timeline__designation\">Visit Visa · Immediate joiner</p>\n\t\t\t\n\t\t\t\t\t\t\t\t<div class=\"dtr-timeline__content\">English, Malayalam</div>",
    )

    text = text.replace("<p class=\"dtr-subheading\">Now</p>", "<p class=\"dtr-subheading\">The numbers</p>")
    text = text.replace('<span class="fawas-stat">Available</span>', '<span class="fawas-stat">2.5+</span>')
    text = text.replace("<p>Status</p>", "<p>Years of SEO</p>")
    text = text.replace('<span class="fawas-stat">Dubai</span>', '<span class="fawas-stat">20+</span>')
    text = text.replace("<p>United Arab Emirates</p>", "<p>Websites managed</p>")
    text = text.replace('<span class="fawas-stat">Kerala</span>', '<span class="fawas-stat">15+</span>')
    text = text.replace("<p>India</p>", "<p>Google Business Profiles</p>")
    text = text.replace('<span class="fawas-stat">SEO</span>', '<span class="fawas-stat">Now</span>')
    text = text.replace("<p>Specialist</p>", "<p>Immediate joiner</p>")

    about = (
        "<p>I'm <strong>Muhammed Fawas</strong>, an SEO Specialist with 2.5+ years of experience driving organic growth for businesses across India and the UAE.</p>"
        "<p>My expertise includes Technical SEO, On-Page &amp; Off-Page SEO, Local SEO, AEO, GEO, AI Search Optimization, and WordPress &amp; custom website development. I have managed 20+ websites and optimized 15+ Google Business Profiles.</p>"
        "<p>I focus on improving search visibility, attracting qualified traffic, and delivering measurable business growth across traditional and AI-powered search.</p>"
    )
    text = re.sub(
        r"<p>I'm <strong>Muhammed Fawas</strong>, an SEO Specialist and digital marketer\.</p><p>I'm obsessed with.*?</p><p>I enjoy the intersection.*?</p>",
        about,
        text,
        count=1,
        flags=re.S,
    )
    return text


def patch_home(text):
    text = text.replace(
        "Digital Marketer &amp; SEO Specialist. I help businesses build a stronger online presence and grow.",
        "SEO Specialist with 2.5+ years of experience driving organic growth for businesses across India and the UAE. Technical SEO, on-page and off-page, GEO, and AI search.",
    )
    text = text.replace(
        '<a class="dtr-btn   dtr-radius--round " href="/about-page/" role="button">\n                            <span class="dtr-btn__text">About me</span>',
        '<a class="dtr-btn   dtr-radius--round " href="/muhammed-fawas-seo-specialist-resume.pdf" role="button">\n                            <span class="dtr-btn__text">Download Resume</span>',
    )
    for old, new in zip(
        [
            "dExito Branding",
            "Green Oasis Tours &amp; Travels",
            "Folk &amp; Fab",
            "GrandBakes",
            "Crink.app",
            "Aurevo Interiors",
        ],
        [
            "dExito Branding",
            "Green Oasis Travel",
            "Grand Bake",
            "Brand with Salman",
            "Crink.app",
            "Aurevo Interiors",
        ],
    ):
        text = text.replace(f'<span class="fawas-brand">{old}</span>', f'<span class="fawas-brand">{new}</span>')

    text = text.replace(
        "<h2 class=\"dtr-heading\">SEO, digital marketing, and web development</h2>",
        "<h2 class=\"dtr-heading\">Search-driven digital strategies</h2>",
    )
    text = text.replace("<p class=\"dtr-subheading\">Clients</p>", "<p class=\"dtr-subheading\">Portfolio</p>")
    text = text.replace("<h2 class=\"dtr-heading\">Selected Clients</h2>", "<h2 class=\"dtr-heading\">Selected work</h2>")

    i = text.find('<div class="dtr-filter-nav-wrapper">')
    j = text.find("</div>                </div>", i)
    if i < 0 or j < 0:
        raise SystemExit("portfolio markers missing")
    text = text[:i] + portfolio_grid() + text[j:]
    return patch_experience(text)


def patch_about(text):
    about = (
        "<p>I'm <strong>Muhammed Fawas</strong>, an SEO Specialist with 2.5+ years of experience driving organic growth for businesses across India and the UAE.</p>"
        "<p>My expertise includes Technical SEO, On-Page &amp; Off-Page SEO, Local SEO, AEO, GEO, AI Search Optimization, and WordPress &amp; custom website development. I have managed 20+ websites and optimized 15+ Google Business Profiles.</p>"
        "<p>I focus on improving search visibility, attracting qualified traffic, and delivering measurable business growth across traditional and AI-powered search.</p>"
    )
    text = re.sub(
        r"<p>I'm <strong>Muhammed Fawas</strong>, an SEO Specialist and digital marketer\.</p><p>I'm obsessed with.*?</p><p>I enjoy the intersection.*?</p>",
        about,
        text,
        count=1,
        flags=re.S,
    )
    # reuse the same experience/education replacements as home if those strings exist
    return patch_experience(text)


def write_project_pages():
    template = (DIST / "about-page" / "index.html").read_text(encoding="utf-8")
    header_end = template.find('<div class="dtr-page-title--section')
    footer_start = template.find('<footer id="dtr-footer-section"')
    head = template[:header_end]
    foot = template[footer_start:]

    for p in PROJECTS:
        imgs = "".join(
            f'<img src="{src}" alt="{html.escape(p["title"])}" />' for src in p["images"]
        )
        paras = "".join(f"<p>{html.escape(b)}</p>" for b in p["body"])
        body = f"""</header>
<div id="dtr-main-wrapper" class="clearfix dtr-fullwidth">
<main id="dtr-primary-section" class="dtr-content-area">
<article class="fawas-case">
<p class="meta">{html.escape(p["cat"])} · {html.escape(p["site"])}<br>{html.escape(p["meta"])}</p>
<p>{html.escape(p["summary"])}</p>
{paras}
{imgs}
<p><a href="/#works">Back to work</a> · <a href="/contact-page/">Connect</a> · <a href="/muhammed-fawas-seo-specialist-resume.pdf">Download resume</a></p>
</article>
</main>
</div>
"""
        page = head
        page = re.sub(r"<title>.*?</title>", f"<title>{html.escape(p['title'])} &#8211; Muhammed Fawas</title>", page, count=1)
        page = page.replace("<link rel=\"canonical\" href=\"/about-page/\" />", f'<link rel="canonical" href="/work/{p["slug"]}/" />')
        out = DIST / "work" / p["slug"] / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(page + body + foot, encoding="utf-8")
        print("wrote", out.relative_to(DIST))


def main():
    for path in DIST.rglob("*.html"):
        text = path.read_text(encoding="utf-8")
        updated = patch_css(text)
        if path == DIST / "index.html":
            updated = patch_home(updated)
        elif path == DIST / "about-page" / "index.html":
            updated = patch_about(updated)
        if updated != text:
            path.write_text(updated, encoding="utf-8")
    write_project_pages()


if __name__ == "__main__":
    main()
