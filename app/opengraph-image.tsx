import { site } from "@/content/site";
import { ogContentType, ogSize, renderOg } from "@/lib/og";

export const alt = `${site.name}, ${site.role}`;
export const size = ogSize;
export const contentType = ogContentType;

export default function Image() {
  return renderOg(site.name, site.role);
}
