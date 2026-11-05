import { site } from "@/content/site";
import { ogContentType, ogSize, renderOg } from "@/lib/og";

export const alt = `About ${site.name}`;
export const size = ogSize;
export const contentType = ogContentType;

export default function Image() {
  return renderOg(site.ui.about, site.tagline);
}
