export type TextPart = { text: string; strong?: boolean };

export const site = {
  name: "Muhammed Fawas",
  role: "Digital Marketer & SEO Specialist",
  url: "https://fawas.me",
  email: "muhammedfawaas@gmail.com",
  status: "Available",
  tagline: "Build. Rank. Grow. Repeat.",
  updated: "2026-11-03",
  home: {
    intro:
      "I'm Muhammed Fawas, an SEO Specialist with 2.5+ years of experience driving organic growth for businesses across India and the UAE.",
    second:
      "My expertise includes Technical SEO, On-Page & Off-Page SEO, Local SEO, AEO, GEO, AI Search Optimization, and WordPress & custom website development. I have managed 20+ websites and optimized 15+ Google Business Profiles.",
    ctas: {
      work: "Explore my work",
      about: "About me",
      connect: "Connect",
    },
  },
  brands: [
    "dExito Branding",
    "Green Oasis Travel",
    "Grand Bake",
    "Brand with Salman",
    "Crink.app",
    "Aurevo Interiors",
  ],
  experience: [
    {
      role: "SEO Specialist",
      org: "Crink.app",
      dates: "Apr 2026 – Jun 2026",
      place: "Kochi, Kerala",
      mode: "On-site",
    },
    {
      role: "SEO Analyst",
      org: "dExito Branding",
      dates: "Jun 2024 – Mar 2026",
      place: "Calicut, Kerala",
      mode: "On-site",
    },
    {
      role: "Digital Marketing Executive",
      org: "Acodez IT Solutions",
      dates: "Mar 2024 – May 2024",
      place: "Calicut, Kerala",
      mode: "Internship",
    },
  ],
  caseStudyTodo: "// TODO: case-study cards",
  about: [
    [
      { text: "I'm " },
      { text: "Muhammed Fawas", strong: true },
      {
        text: ", an SEO Specialist with 2.5+ years of experience driving organic growth for businesses across India and the UAE.",
      },
    ],
    [
      { text: "My expertise includes " },
      {
        text: "Technical SEO, On-Page & Off-Page SEO, Local SEO, AEO, GEO, AI Search Optimization",
        strong: true,
      },
      {
        text: ", and WordPress & custom website development. I have managed 20+ websites and optimized 15+ Google Business Profiles.",
      },
    ],
    [
      { text: "I focus on improving search visibility, attracting qualified traffic, and delivering measurable business growth across traditional and AI-powered search." },
    ],
  ] as readonly (readonly TextPart[])[],
  connect: {
    intro:
      "I'm always open to interesting conversations, new opportunities, and creative collaborations. Don't hesitate to reach out. I'd love to hear from you.",
    location: "Al Qusais, Dubai, United Arab Emirates",
    also: "Also based in Kerala, India · Usually replies within a day.",
    map: {
      lat: 25.278,
      lng: 55.385,
      bbox: "55.34,25.25,55.43,25.31",
    },
    places: {
      dubai: { lat: 25.278, lng: 55.385 },
      kerala: { lat: 10.85, lng: 76.27 },
    },
  },
  social: {
    linkedin: "https://www.linkedin.com/in/muhammed-fawas/",
    x: "https://x.com/muhammed_fawaas",
    whatsapp: "https://wa.me/971528481743",
  },
  nav: [
    { href: "/", label: "Home" },
    { href: "/about", label: "About" },
    { href: "/portfolio", label: "Portfolio" },
    { href: "/contact", label: "Contact" },
  ],
  seo: {
    home: {
      title: "Muhammed Fawas — Digital Marketer & SEO Specialist",
      description:
        "Digital Marketer and SEO Specialist helping businesses build a stronger online presence. Brands in India and clients across the UAE.",
    },
    work: {
      title: "Work",
      description:
        "SEO work with Crink.app, dExito Branding, Green Oasis Travel, Grand Bake, and clients across India and the UAE.",
    },
    about: {
      title: "About",
      description:
        "Muhammed Fawas is an SEO Specialist with 2.5+ years of experience in technical SEO, GEO, and AI search for India and the UAE.",
    },
    connect: {
      title: "Connect",
      description:
        "Open to conversations, opportunities, and collaborations. Al Qusais, Dubai, United Arab Emirates — also based in Kerala, India.",
    },
  },
  form: {
    name: "Name",
    email: "Email",
    message: "Message",
    submit: "Send message",
    sending: "Sending…",
    success: "Thanks. I'll get back to you.",
    another: "Send another",
    error: "Something went wrong. Please use email or WhatsApp instead.",
    nameError: "Please enter your name.",
    emailError: "Please enter a valid email.",
    messageError: "Please enter a message.",
  },
  ui: {
    skip: "Skip to content",
    openMenu: "Open menu",
    closeMenu: "Close menu",
    primaryNav: "Primary",
    socialNav: "Social",
    brands: "Brands",
    experience: "Experience",
    clients: "Selected Clients",
    work: "Work",
    about: "About",
    connect: "Connect",
    contactForm: "Contact form",
    mapTitle: "Map of Al Qusais, Dubai",
    notFoundTitle: "Page not found",
    notFoundBody: "That link doesn't lead anywhere.",
    backHome: "Back home",
  },
} as const;

export type Experience = (typeof site.experience)[number];

export function mailto() {
  return `mailto:${site.email}`;
}

export function mapEmbedSrc() {
  const { bbox, lat, lng } = site.connect.map;
  return `https://www.openstreetmap.org/export/embed.html?bbox=${encodeURIComponent(bbox)}&layer=mapnik&marker=${lat}%2C${lng}`;
}
