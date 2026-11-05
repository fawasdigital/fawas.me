import { site } from "@/content/site";
import { ogContentType, ogSize, renderOg } from "@/lib/og";

export const alt = `Connect with ${site.name} in Dubai and Kerala`;
export const size = ogSize;
export const contentType = ogContentType;

export default function Image() {
  return renderOg(site.ui.connect, site.connect.location);
}
