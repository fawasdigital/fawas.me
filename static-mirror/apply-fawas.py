"""Replace the Mellow demo copy in dist/ with Muhammed Fawas's content."""

import re
from pathlib import Path

DIST = Path(__file__).resolve().parent / "dist"
CORE = {
    DIST / "index.html",
    DIST / "about-page" / "index.html",
    DIST / "contact-page" / "index.html",
}

STYLE = """
<style id="fawas-content">
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
.dtr-portfolio-item__img img,.dtr-testimonial__client-img,.dtr-post-block__img-wrapper img,.dtr-timeline__icon img{opacity:0}
.dtr-portfolio-item__img,.dtr-post-block__img-wrapper{background:#1a1a1a;min-height:180px}
.dtr-filter-nav-wrapper{display:none}
img[src*="Figma"],img[src*="Illustrator"],img[src*="framer"],img[src*="html-"],img[src*="Sketch"],img[src*="notion"],img[src*="webflow"],img[src*="Slack"],img[src*="wordpress-"],img[src*="angular"],img[src*="visual-studio"],img[src*="nextjs"],img[src*="premier-pro"],img[src*="capcut"],img[src*="adobe-audition"],img[src*="davinci"],img[alt="Figma"],img[alt="Adobe Illustrator"]{display:none!important}
.fawas-stat{display:block;font-size:clamp(1.5rem,3vw,2.6rem);font-weight:700;line-height:1.1;letter-spacing:-.03em}
.fawas-stub{max-width:760px;margin:72px auto 96px;padding:0 24px}
.fawas-stub h1{font-size:clamp(2.6rem,7vw,5rem);line-height:.92;letter-spacing:-.04em;margin:0 0 16px}
.fawas-stub p{font-size:1.125rem;line-height:1.55}
.fawas-stub a{color:#fff}
.fawas-stub-page .dtr-breadcrumb-wrapper{display:none}
.dtr-recentposts-carousel .dtr-post-block__meta{display:none}
</style>
"""

NAV = (
    '<ul id="menu-primary-menu" class="dtr-nav sf-menu dtr-main-nav">'
    '<li class="menu-item"><a href="/">Home</a></li>'
    '<li class="menu-item"><a href="/about/">About</a></li>'
    '<li class="menu-item"><a href="/portfolio/">Portfolio</a></li>'
    '<li class="menu-item"><a href="/contact/">Contact</a></li>'
    "</ul>"
)
FOOTER_NAV = (
    '<ul id="menu-copyright-menu" class="menu">'
    '<li class="menu-item"><a href="/">Home</a></li>'
    '<li class="menu-item"><a href="/about/">About</a></li>'
    '<li class="menu-item"><a href="/portfolio/">Portfolio</a></li>'
    '<li class="menu-item"><a href="/contact/">Contact</a></li>'
    "</ul>"
)
STUB = """
<article class="fawas-stub">
<h1>Muhammed Fawas</h1>
<p>Digital Marketer &amp; SEO Specialist.</p>
<p>I'm a Digital Marketer and SEO Specialist passionate about helping businesses build a stronger online presence and grow through effective digital strategies. Over the years, I've worked with brands including dExito Branding, Green Oasis Tours &amp; Travels, Folk &amp; Fab, GrandBakes, Crink.app, and Aurevo Interiors, along with clients across the UAE.</p>
<p><a href="/">Home</a> · <a href="/about-page/">About</a> · <a href="/contact-page/">Connect</a></p>
</article>
"""

LOREM = (
    "There are many variations of passages of Lorem Ipsum available, but the majority have suffered "
    "alteration in some form, by injected humour, or randomised words which don&#8217;t look even slightly "
    "believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn&#8217;t "
    "anything embarrassing hidden in the middle of text."
)
FAQ_ANSWERS = [
    "Al Qusais, Dubai, United Arab Emirates. Also based in Kerala, India.",
    "Email muhammedfawaas@gmail.com, WhatsApp, LinkedIn, or X. Usually replies within a day.",
    "SEO, digital marketing, web development, and the intersection of SEO, development, and AI.",
    "Available for conversations, new opportunities, and creative collaborations.",
    "dExito Branding, Green Oasis Tours &amp; Travels, Folk &amp; Fab, GrandBakes, Crink.app, and Aurevo Interiors, along with clients across the UAE.",
]


def replace_balanced(html, start_marker, new_html):
    start = html.find(start_marker)
    if start < 0:
        return html
    open_tag = start_marker.split()[0].lstrip("<")
    depth = 0
    i = start
    token = re.compile(rf"</?{open_tag}\b")
    while i < len(html):
        match = token.search(html, i)
        if not match:
            return html
        depth += -1 if html.startswith("</", match.start()) else 1
        close = html.find(">", match.end())
        i = close + 1
        if depth == 0:
            return html[:start] + new_html + html[i:]
    return html


def link_feature_cards(html):
    pattern = re.compile(
        r'<a href="#" class="dtr-wrapping-link" role="button"></a>.{0,700}?dtr-feature-highlight__text">[^<]+',
        re.S,
    )

    def repl(match):
        block = match.group(0)
        if "+91" in block or "WhatsApp" in block:
            return block.replace(
                'href="#"',
                'href="https://wa.me/971528481743" target="_blank" rel="noopener"',
                1,
            )
        if "muhammedfawaas@gmail.com" in block:
            return block.replace('href="#"', 'href="mailto:muhammedfawaas@gmail.com"', 1)
        return block

    return pattern.sub(repl, html)


def apply_shared(html, path):
    html = html.replace("/mellow-wp/", "/")
    html = re.sub(
        r'<a class="dtr-logo logo-(default|alt)" href="/" title="Mellow"><img src="/wp-content/uploads/logo.png" alt="Mellow" width="188" height="30"></a>',
        lambda m: f'<a class="dtr-logo logo-{m.group(1)}" href="/" title="Muhammed Fawas"><span class="fawas-wordmark">Fawas</span></a>',
        html,
    )
    html = replace_balanced(html, '<ul id="menu-primary-menu"', NAV)
    html = replace_balanced(html, '<ul id="menu-copyright-menu"', FOOTER_NAV)
    html = re.sub(
        r'<a href="#contact" class="dtr-btn dtr-header-btn" target="_self">\s*<span class="dtr-btn__text">\s*Book a Call\s*</span>\s*</a>',
        '<a href="https://wa.me/971528481743" class="dtr-btn dtr-header-btn" target="_blank" rel="noopener"><span class="dtr-btn__text">WhatsApp</span></a>',
        html,
    )
    html = re.sub(
        r'<figure class="wp-block-image size-full is-resized"><img[^>]*logo-symbol\.png[^>]*></figure>',
        '<p class="fawas-wordmark">Fawas</p>',
        html,
    )
    html = html.replace("© 2025. Mellow", "© 2026. Muhammed Fawas")
    html = html.replace("WordPress Theme by Tansh", "Digital Marketer &amp; SEO Specialist")
    html = html.replace('title="Go to Mellow."', 'title="Go to Muhammed Fawas."')
    html = html.replace('<span property="name">Mellow</span>', '<span property="name">Home</span>')
    html = html.replace("hello@example.com", "muhammedfawaas@gmail.com")
    html = html.replace('placeholder="muhammedfawaas@gmail.com"', 'placeholder="Email"')
    html = html.replace('placeholder="John Doe"', 'placeholder="Name"')
    html = html.replace('placeholder="Message in brief..."', 'placeholder="Message"')
    html = html.replace("+ 1 800 23 456 789", "+91 90727 18780")
    html = html.replace(
        '<a class="dtr-twitter / x" href="#" title="Twitter / X"  target="_blank" rel="nofollow" aria-label="Twitter / X">',
        '<a class="dtr-twitter / x" href="https://x.com/muhammed_fawaas" title="X" target="_blank" rel="noopener" aria-label="X">',
    )
    html = html.replace('<span class="dtr-social-title">Twitter / X</span>', '<span class="dtr-social-title">X</span>')
    html = html.replace(
        '<a class="dtr-whatsapp" href="#" title="Whatsapp"  target="_blank" rel="nofollow" aria-label="Whatsapp">',
        '<a class="dtr-whatsapp" href="https://wa.me/971528481743" title="WhatsApp" target="_blank" rel="noopener" aria-label="WhatsApp">',
    )
    html = html.replace('<span class="dtr-social-title">Whatsapp</span>', '<span class="dtr-social-title">WhatsApp</span></a></li><li><a href="https://www.linkedin.com/in/muhammed-fawas/" title="LinkedIn" target="_blank" rel="noopener" aria-label="LinkedIn"><span class="dtr-social-title">LinkedIn</span>')
    if 'id="fawas-content"' not in html:
        html = html.replace("</head>", STYLE + "</head>", 1)

    if path == DIST / "index.html":
        html = re.sub(
            r"<title>.*?</title>",
            "<title>Muhammed Fawas — Digital Marketer &amp; SEO Specialist</title>",
            html,
            count=1,
        )
    elif path == DIST / "about-page" / "index.html":
        html = html.replace("<title>About Page &#8211; Mellow</title>", "<title>About &#8211; Muhammed Fawas</title>")
        html = html.replace('<h1 class="dtr-page-title">About Page</h1>', '<h1 class="dtr-page-title">About</h1>')
    elif path == DIST / "contact-page" / "index.html":
        html = html.replace("<title>Contact Page &#8211; Mellow</title>", "<title>Connect &#8211; Muhammed Fawas</title>")
        html = html.replace('<h1 class="dtr-page-title">Contact Page</h1>', '<h1 class="dtr-page-title">Connect</h1>')
    else:
        html = html.replace(" &#8211; Mellow", " &#8211; Muhammed Fawas")
    return html


def apply_profile(html):
    """Copy shared by the homepage and the about page."""
    pairs = [
        (
            "<h2 class=\"dtr-heading\">A product designer with a knack for turning problems and challenges into user-driven strategic solutions.</h2>",
            "<h2 class=\"dtr-heading\">Build. Rank. Grow. Repeat.</h2>",
        ),
        (
            "<p>I specialize in creating unique visual identities for digital products. I believe that a stunning design starts with common values, open communication, technical knowledge and respect for your audience.</p>",
            "<p>I'm <strong>Muhammed Fawas</strong>, an SEO Specialist and digital marketer.</p>"
            "<p>I'm obsessed with <strong>SEO, growth, and building things on the internet</strong>, from taking new pages from zero to ranking, to turning traffic into real business value.</p>"
            "<p>I enjoy the intersection of <strong>SEO × Development × AI</strong>, constantly experimenting, learning, and finding new ways to build, grow, and improve.</p>",
        ),
        ("Aug 2023 &mdash; Present", "Jan 2026 &mdash; Present"),
        ("<p class=\"dtr-timeline__designation\">Associate Creative Director</p>", "<p class=\"dtr-timeline__designation\">SEO Specialist</p>"),
        (
            '<div class="dtr-timeline__content">Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod.</div>',
            '<div class="dtr-timeline__content">Aurevo Interiors · Kakkad, Kerala · Hybrid</div>',
        ),
        ("&#x269E; ACME Digital.", "Crink.app"),
        ("May 2021 &mdash; Jun 2023", "Apr 2026 &mdash; Jun 2026"),
        ("Senior Product Designer", "SEO Specialist"),
        (
            '<div class="dtr-timeline__content">Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</div>',
            '<div class="dtr-timeline__content">Kochi, Kerala · On-site</div>',
        ),
        ("Mar 2020 &mdash; Apr 2021", "Jun 2024 &mdash; Dec 2025"),
        (
            "<p class=\"dtr-timeline__designation\">Creative Head @Provev Innovations</p>",
            "<p class=\"dtr-timeline__designation\">SEO Analyst</p>\n\t\t\t<div class=\"dtr-timeline__content\">dExito Branding · Calicut, Kerala · On-site</div>",
        ),
        ("Jan 2019 &mdash; Feb 2020", "Mar 2024 &mdash; May 2024"),
        ("<p class=\"dtr-timeline__designation\">Design Intern</p>", "<p class=\"dtr-timeline__designation\">Intern</p>"),
        (
            '<div class="dtr-timeline__content">Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum.</div>',
            '<div class="dtr-timeline__content">Acodez IT Solutions · Calicut, Kerala · On-site</div>',
        ),
        ("<p class=\"dtr-subheading\">Education</p>", "<p class=\"dtr-subheading\">Based in</p>"),
        ("Nov 2017 &mdash; Dec 2019", "Dubai"),
        ("Cranfield University, UK", "Al Qusais, United Arab Emirates"),
        ("DSGN School, UK", "Kerala, India"),
        ("Aug 2013 &mdash; Oct 2016", "India"),
        ("Msc in Innovation Design", "Also based in Kerala, India"),
        ("Sep 2010 &mdash; Jun 2012", "Available"),
        ("Bsc in IT @ACME Institute, UK", "Usually replies within a day"),
        ("<p class=\"dtr-subheading\">The Numbers</p>", "<p class=\"dtr-subheading\">Now</p>"),
        ("<p>Years of experience</p>", "<p>Status</p>"),
        ("<p>Awards won</p>", "<p>United Arab Emirates</p>"),
        ("<p>Projects completed</p>", "<p>India</p>"),
        ("<p>Happy clients</p>", "<p>Specialist</p>"),
        ("<p class=\"dtr-subheading\">Tools</p>", "<p class=\"dtr-subheading\">Focus</p>"),
        (
            "<h2 class=\"dtr-heading\">The key design and development tools I use</h2>",
            "<h2 class=\"dtr-heading\">SEO × Development × AI</h2>",
        ),
        ("<p>Figma</p>", "<p>SEO</p>"),
        ("<p>Illustrator</p>", "<p>Marketing</p>"),
        ("<p>Framer</p>", "<p>Development</p>"),
        ("<p>HTML5</p>", "<p>AI</p>"),
        ("<p>Sketch</p>", "<p>Creative</p>"),
        ("<p>Notion</p>", "<p>Growth</p>"),
        ("<p>Webflow</p>", "<p>Rankings</p>"),
        ("<p>Slack</p>", "<p>Brands</p>"),
        ("<p>Development</p>", "<p>Build</p>"),
        ("<p>Motion</p>", "<p>Repeat</p>"),
        ("Let's talk about your project", "Don't hesitate to reach out"),
        (
            "Let’s embark on creative journey together by shaping a visual narrative of your brand in the crowded digital space.",
            "I'm always open to interesting conversations, new opportunities, and creative collaborations. Al Qusais, Dubai, United Arab Emirates. Also based in Kerala, India. Usually replies within a day.",
        ),
        ("<p class=\"dtr-feature-highlight__heading\">Book a Call</p>", "<p class=\"dtr-feature-highlight__heading\">WhatsApp</p>"),
        ("<p class=\"dtr-feature-highlight__heading\">Prefer Email Communication</p>", "<p class=\"dtr-feature-highlight__heading\">Email</p>"),
        ("<p class=\"dtr-subheading\">Contact Me</p>", "<p class=\"dtr-subheading\">Connect</p>"),
    ]
    for old, new in pairs:
        html = html.replace(old, new)

    html = re.sub(
        r'<div class="elementor-counter-number-wrapper">\s*<span class="elementor-counter-number-prefix"></span>\s*<span class="elementor-counter-number" data-duration="2000" data-to-value="(\d+)" data-from-value="0" data-delimiter=",">0</span>\s*<span class="elementor-counter-number-suffix">[^<]*</span>\s*</div>',
        lambda m: {
            "12": '<div class="elementor-counter-number-wrapper"><span class="fawas-stat">Available</span></div>',
            "6": '<div class="elementor-counter-number-wrapper"><span class="fawas-stat">Dubai</span></div>',
            "30": '<div class="elementor-counter-number-wrapper"><span class="fawas-stat">Kerala</span></div>',
            "4": '<div class="elementor-counter-number-wrapper"><span class="fawas-stat">SEO</span></div>',
        }.get(m.group(1), m.group(0)),
        html,
    )
    # The second experience item uses the same lorem as the first education item.
    # After the first pass, leftover education lorem still matches the medium string if it was already replaced.
    # Rewrite the education descriptions that now share the Kochi line by their surrounding dates.
    html = html.replace(
        "<p class=\"dtr-timeline__duration\">Dubai</p>\n\t\t\t\n\t\t\t\t\t\t\t<p class=\"dtr-timeline__designation\">Al Qusais, United Arab Emirates</p>\n\t\t\t\n\t\t\t\t\t\t\t\t<div class=\"dtr-timeline__content\">Kochi, Kerala · On-site</div>",
        "<p class=\"dtr-timeline__duration\">Dubai</p>\n\t\t\t\n\t\t\t\t\t\t\t<p class=\"dtr-timeline__designation\">Al Qusais, United Arab Emirates</p>\n\t\t\t\n\t\t\t\t\t\t\t\t<div class=\"dtr-timeline__content\">Al Qusais, Dubai, United Arab Emirates</div>",
    )
    html = html.replace(
        "<p class=\"dtr-timeline__duration\">India</p>",
        "<p class=\"dtr-timeline__duration\">India</p>",
    )
    html = html.replace(
        '<div class="dtr-timeline__content">Acodez IT Solutions · Calicut, Kerala · On-site</div>',
        '<div class="dtr-timeline__content">Usually replies within a day.</div>',
        1,
    ) if False else html
    return html


def fix_education_bodies(html):
    """Education items reused the same lorem as experience, so retarget by nearby headings."""
    html = html.replace(
        "<p class=\"dtr-timeline__designation\">Al Qusais, United Arab Emirates</p>\n\t\t\t\n\t\t\t\t\t\t\t\t<div class=\"dtr-timeline__content\">Kochi, Kerala · On-site</div>",
        "<p class=\"dtr-timeline__designation\">Al Qusais, United Arab Emirates</p>\n\t\t\t\n\t\t\t\t\t\t\t\t<div class=\"dtr-timeline__content\">Al Qusais, Dubai, United Arab Emirates</div>",
    )
    html = html.replace(
        "<p class=\"dtr-timeline__designation\">Also based in Kerala, India</p>\n\t\t\t\n\t\t\t\t\t\t\t\t<div class=\"dtr-timeline__content\">Acodez IT Solutions · Calicut, Kerala · On-site</div>",
        "<p class=\"dtr-timeline__designation\">Also based in Kerala, India</p>\n\t\t\t\n\t\t\t\t\t\t\t\t<div class=\"dtr-timeline__content\">Usually replies within a day.</div>",
    )
    html = html.replace(
        "<p class=\"dtr-timeline__designation\">Usually replies within a day</p>\n\t\t\t\n\t\t\t\t\t\t\t\t<div class=\"dtr-timeline__content\">Aurevo Interiors · Kakkad, Kerala · Hybrid</div>",
        "<p class=\"dtr-timeline__designation\">Usually replies within a day</p>\n\t\t\t\n\t\t\t\t\t\t\t\t<div class=\"dtr-timeline__content\">Open to conversations, opportunities, and collaborations.</div>",
    )
    return html


def apply_home(html):
    html = html.replace("<h1 class=\"dtr-heading\">Mellow</h1>", "<h1 class=\"dtr-heading\">Muhammed</h1>")
    html = html.replace("<h1 class=\"dtr-heading\">White</h1>", "<h1 class=\"dtr-heading\">Fawas</h1>")
    html = html.replace(
        "A product designer, specialize in creating magical visual identities for digital products.",
        "Digital Marketer &amp; SEO Specialist. I help businesses build a stronger online presence and grow.",
    )
    html = html.replace(
        '<a class="dtr-btn   dtr-radius--round dtr-scroll-btn" href="#works" role="button">\n                            <span class="dtr-btn__text">View Portfolio</span>',
        '<a class="dtr-btn   dtr-radius--round dtr-scroll-btn" href="#works" role="button">\n                            <span class="dtr-btn__text">Explore my work</span>',
    )
    html = html.replace(
        '<a class="dtr-btn   dtr-radius--round " href="#" role="button">\n                            <span class="dtr-btn__text">Download Resume</span>',
        '<a class="dtr-btn   dtr-radius--round " href="/about-page/" role="button">\n                            <span class="dtr-btn__text">About me</span>',
    )
    html = html.replace(
        "<h2 class=\"dtr-heading\">Digital Product Design Services I Offer</h2>",
        "<h2 class=\"dtr-heading\">SEO, digital marketing, and web development</h2>",
    )
    services = [
        (
            "Brand Strategy",
            "SEO",
            "/brand-strategy/",
            "A strong brand strategy defines what a brand stands for, promises to its customers, and how it communicates those promises through product development.",
            "Taking new pages from zero to ranking, and turning traffic into real business value.",
            "Brand Posture",
            "Rankings",
        ),
        (
            "Product Design",
            "Digital Marketing",
            "/product-design/",
            "The process of creating and developing a product with the goal of solving a specific problem or fulfilling a user need involves a  functionality, aesthetics and usability.",
            "Helping businesses build a stronger online presence and grow through effective digital strategies.",
            "Web Platform",
            "Brands",
        ),
        (
            "UI UX Design",
            "Web Development",
            "/ui-ux-design/",
            "Creating digital products that are both visually appealing and easy to use having focuse on different aspects of the user’s interaction with a product.",
            "Building digital experiences that not only look good but also help businesses grow.",
            "Visual Design",
            "Build",
        ),
        (
            "SEO Services",
            "AI",
            "/seo-services/",
            "Aim to increase organic (non-paid) traffic by optimizing various elements of a website, making it more attractive to both users and search engines.",
            "The intersection of SEO, development, and AI. Experimenting, learning, and finding new ways to build, grow, and improve.",
            "PPC Advertising",
            "SEO",
        ),
    ]
    for old_name, new_name, href, old_copy, new_copy, old_key, new_key in services:
        html = html.replace(f"<h3 class=\"dtr-servicebox__heading\">{old_name}</h3>", f"<h3 class=\"dtr-servicebox__heading\">{new_name}</h3>")
        html = html.replace(f'href="{href}"', 'href="#contact"')
        html = html.replace(old_copy, new_copy)
        html = html.replace(f">{old_key}<", f">{new_key}<", 1)
    for old, new in [
        (">Consumer Behaviours<", ">Content<"),
        (">Narrative Strategy<", ">Search<"),
        (">Offer Framework<", ">Growth<"),
        (">Mobile Application<", ">UAE<"),
        (">Creative Design Solutions<", ">India<"),
        (">AI Consulting<", ">Strategy<"),
        (">Customer Experience<", ">Web<"),
        (">Prototyping<", ">Experience<"),
        (">Wireframes<", ">Grow<"),
        (">Web Design<", ">Development<"),
        (">SEO Audits<", ">Development<"),
        (">Off-page seo<", ">AI<"),
        (">Keyword Research<", ">Experiment<"),
        (">Link building<", ">Growth<"),
    ]:
        html = html.replace(old, new, 1)

    brands = [
        ("client-1", "dExito Branding"),
        ("client-2", "Green Oasis Tours &amp; Travels"),
        ("client-3", "Folk &amp; Fab"),
        ("client-4", "GrandBakes"),
        ("logoipsum-280", "Crink.app"),
        ("client-5", "Aurevo Interiors"),
    ]
    for alt, name in brands:
        html = re.sub(
            rf'<img[^>]*alt="{alt}"[^>]*>',
            f'<span class="fawas-brand">{name}</span>',
            html,
            count=1,
        )
    html = html.replace("<p class=\"dtr-subheading\">Works</p>", "<p class=\"dtr-subheading\">Clients</p>")
    html = html.replace("<h2 class=\"dtr-heading\">Featured projects</h2>", "<h2 class=\"dtr-heading\">Selected Clients</h2>")
    for old, new, href in [
        ("Pressed Juicery", "dExito Branding", "/portfolio/pressed-juicery/"),
        ("Nouri Probiotic", "Green Oasis Tours &amp; Travels", "/portfolio/nouri-probiotic/"),
        ("Joborba", "Folk &amp; Fab", "/portfolio/joborba/"),
        ("Sound On", "GrandBakes", "/portfolio/sound-on/"),
        ("Onne Skin Care", "Crink.app", "/portfolio/onne-skin-care/"),
        ("Boxed Water", "Aurevo Interiors", "/portfolio/boxed-water/"),
    ]:
        html = html.replace(href, "/#works")
        html = html.replace(old, new)
    html = html.replace(">View Case Study<", ">Client<")

    html = html.replace("<h2 class=\"dtr-heading\">Product Design Process</h2>", "<h2 class=\"dtr-heading\">Build. Rank. Grow. Repeat.</h2>")
    html = html.replace(
        "<p>Structured series of steps that guide the development of a new product—from identifying a problem or opportunity, to delivering a final, market-ready solution.</p>",
        "<p>Build. Rank. Grow. Repeat.</p>",
    )
    html = html.replace(">\n\t\t\t\t\t\t\t\tDiscover</h5>", ">\n\t\t\t\t\t\t\t\tBuild</h5>")
    html = html.replace(
        "The goal is to define clear objectives and requirements for the product and gathering insights.",
        "Building digital experiences that help businesses grow.",
    )
    html = html.replace(">\n\t\t\t\t\t\t\t\tDesign</h5>", ">\n\t\t\t\t\t\t\t\tRank</h5>")
    html = html.replace(
        "In this stage, ideas are translated into tangible concepts to align product with business goals.",
        "Taking new pages from zero to ranking.",
    )
    html = html.replace(">\n\t\t\t\t\t\t\t\tDeliver</h5>", ">\n\t\t\t\t\t\t\t\tGrow</h5>")
    html = html.replace(
        "The final phase involves collaborating with developers to build and launch the product.",
        "Turning traffic into real business value.",
    )
    for old, new in [
        (">Stakeholder Interview<", ">Build<"),
        (">Problem Finding<", ">Web<"),
        (">Market Research<", ">Experience<"),
        (">Product Positioning<", ">Grow<"),
        (">UX Research<", ">SEO<"),
        (">Wireframe<", ">Rankings<"),
        (">Visual Design<", ">Search<"),
        (">User Testing<", ">Content<"),
        (">Validation<", ">Growth<"),
        (">Project Handover<", ">Traffic<"),
        (">Developerr Collaboration<", ">Value<"),
        (">LOng TIme Support<", ">Repeat<"),
    ]:
        html = html.replace(old, new, 1)

    html = html.replace("<p class=\"dtr-subheading\">Testimonials</p>", "<p class=\"dtr-subheading\">Clients</p>")
    html = html.replace("<h2 class=\"dtr-heading\">What clients say</h2>", "<h2 class=\"dtr-heading\">Brands I've worked with</h2>")
    quotes = [
        "dExito Branding. Green Oasis Tours &amp; Travels.",
        "Folk &amp; Fab. GrandBakes.",
        "Crink.app. Aurevo Interiors.",
    ]
    quote = "“Extremely professional, unique and enjoyable. The effort taken to ensure sed quia non numquam eius modi tempora incidunt ut labore voluptat relevance to our requirements ensured the optimum outcome.”"
    for text in quotes:
        html = html.replace(quote, text, 1)
    html = html.replace("Mark Robinson", "dExito Branding")
    html = html.replace("Project Manager, ACME Works", "Client")
    html = html.replace("Thomas Luze", "Folk &amp; Fab")
    html = html.replace("Senior Product Developer @ ThisOne", "Client")
    html = html.replace("Andrea De Santis", "Crink.app")
    html = html.replace("CEO, Agresar Soft Inc.", "Client")

    html = html.replace("<p class=\"dtr-subheading\">Latest Posts</p>", "<p class=\"dtr-subheading\">Connect</p>")
    html = html.replace(
        "<h2 class=\"dtr-heading\">Explore Recent Insights and articles</h2>",
        "<h2 class=\"dtr-heading\">Open to conversations, opportunities, and collaborations.</h2>",
    )
    channels = [
        ("/importance-of-search-engine-optimization-best-practices/", "mailto:muhammedfawaas@gmail.com", "Importance of search engine optimization best practices", "Email"),
        ("/15-design-tips-that-always-deliver-growth/", "https://wa.me/971528481743", "15 design tips that always deliver growth", "WhatsApp"),
        ("/the-value-proposition-business-branding/", "https://www.linkedin.com/in/muhammed-fawas/", "The value proposition business branding", "LinkedIn"),
        ("/essential-social-media-tips-for-small-business/", "https://x.com/muhammed_fawaas", "Essential social media tips for small business", "X"),
    ]
    for href, new_href, title, label in channels:
        html = html.replace(href, new_href)
        html = html.replace(title, label)
    html = html.replace(">Read More<", ">Open<")
    return html


def apply_faq(html):
    questions = [
        ("How many years of experience do you have?", "Where are you based?"),
        ("What is the average timeframe for branding work?", "How can I reach you?"),
        ("Which softwares &amp; tools do you use?", "What do you focus on?"),
        ("How long does a typical web development project take?", "Are you available?"),
        ("How do you establish your design fees?", "Who have you worked with?"),
    ]
    for old, new in questions:
        html = html.replace(old, new)
    for answer in FAQ_ANSWERS:
        html = html.replace(LOREM, answer, 1)
    return html


def stub_page(html):
    html = re.sub(
        r'(<main id="dtr-primary-section" class="dtr-content-area">).*?(</main>)',
        lambda m: m.group(1) + STUB + m.group(2),
        html,
        count=1,
        flags=re.S,
    )
    html = re.sub(
        r'<h1 class="dtr-page-title">.*?</h1>',
        '<h1 class="dtr-page-title">Muhammed Fawas</h1>',
        html,
        count=1,
    )
    if "fawas-stub-page" not in html:
        html = html.replace('<body class="', '<body class="fawas-stub-page ', 1)
    return html


def main():
    files = list(DIST.rglob("index.html"))
    for path in files:
        html = path.read_text(encoding="utf-8", errors="replace")
        html = apply_shared(html, path)
        if path in (DIST / "index.html", DIST / "about-page" / "index.html"):
            html = apply_profile(html)
            html = fix_education_bodies(html)
        if path == DIST / "index.html":
            html = apply_home(html)
        if path == DIST / "contact-page" / "index.html":
            html = apply_profile(html)
            html = apply_faq(html)
        if path not in CORE:
            html = stub_page(html)
        html = link_feature_cards(html)
        path.write_text(html, encoding="utf-8")
    print(f"updated {len(files)} pages")


if __name__ == "__main__":
    main()
