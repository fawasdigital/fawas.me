import { site } from "@/content/site";
import { ogContentType, ogSize, renderOg } from "@/lib/og";

export const alt = `Work and experience of ${site.name}`;
export const size = ogSize;
export const contentType = ogContentType;

export default function Image() {
  return renderOg(site.ui.work, site.ui.experience);
}
