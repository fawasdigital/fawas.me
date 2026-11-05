import type { MetadataRoute } from "next";
import { site } from "@/content/site";

export default function sitemap(): MetadataRoute.Sitemap {
  return [
    { url: site.url, lastModified: site.updated, changeFrequency: "monthly", priority: 1 },
    { url: `${site.url}/work`, lastModified: site.updated, changeFrequency: "monthly", priority: 0.8 },
    { url: `${site.url}/about`, lastModified: site.updated, changeFrequency: "monthly", priority: 0.8 },
    { url: `${site.url}/connect`, lastModified: site.updated, changeFrequency: "monthly", priority: 0.7 },
  ];
}
