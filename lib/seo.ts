import type { Metadata } from "next";
import { site } from "@/content/site";

export function pageMeta({
  title,
  description,
  path,
}: {
  title: string;
  description: string;
  path: string;
}): Metadata {
  const fullTitle = `${title} — ${site.name}`;

  return {
    title,
    description,
    alternates: { canonical: path },
    openGraph: {
      type: "website",
      locale: "en_US",
      url: path,
      siteName: site.name,
      title: fullTitle,
      description,
    },
    twitter: {
      card: "summary_large_image",
      title: fullTitle,
      description,
    },
  };
}

export function personJsonLd() {
  return {
    "@context": "https://schema.org",
    "@type": "Person",
    "@id": `${site.url}/#person`,
    name: site.name,
    jobTitle: site.role,
    url: site.url,
    email: site.email,
    description: site.home.intro,
    sameAs: [site.social.linkedin, site.social.x],
    workLocation: [
      {
        "@type": "Place",
        name: "Kerala, India",
        address: {
          "@type": "PostalAddress",
          addressRegion: "Kerala",
          addressCountry: "IN",
        },
      },
      {
        "@type": "Place",
        name: "Dubai, United Arab Emirates",
        address: {
          "@type": "PostalAddress",
          addressLocality: "Dubai",
          addressCountry: "AE",
        },
      },
    ],
  };
}

export function profilePageJsonLd() {
  return {
    "@context": "https://schema.org",
    "@type": "ProfilePage",
    name: `About ${site.name}`,
    url: `${site.url}/about`,
    mainEntity: { "@id": `${site.url}/#person` },
  };
}

export function contactPageJsonLd() {
  return {
    "@context": "https://schema.org",
    "@type": "ContactPage",
    name: `Connect with ${site.name}`,
    url: `${site.url}/connect`,
    mainEntity: {
      "@type": "Person",
      name: site.name,
      url: site.url,
      email: site.email,
      address: {
        "@type": "PostalAddress",
        addressLocality: "Al Qusais, Dubai",
        addressCountry: "AE",
      },
    },
  };
}

export function breadcrumbJsonLd(items: readonly { name: string; path: string }[]) {
  return {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    itemListElement: items.map((item, index) => ({
      "@type": "ListItem",
      position: index + 1,
      name: item.name,
      item: new URL(item.path, site.url).href,
    })),
  };
}
