import Link from "next/link";
import { mailto, site } from "@/content/site";

const links = [
  { href: mailto(), label: "Email", external: false },
  { href: site.social.whatsapp, label: "WhatsApp", external: true },
  { href: site.social.linkedin, label: "LinkedIn", external: true },
  { href: site.social.x, label: "X", external: true },
];

export function Footer() {
  return (
    <footer className="mt-24 border-t border-line">
      <div className="mx-auto flex w-full max-w-[1200px] flex-col gap-6 px-5 py-10 sm:flex-row sm:items-center sm:justify-between md:px-8">
        <Link href="/" className="font-display text-lg tracking-tight">
          {site.name}
        </Link>
        <nav aria-label={site.ui.socialNav}>
          <ul className="flex flex-wrap gap-x-6 gap-y-3">
            {links.map((link) => (
              <li key={link.label}>
                <a
                  href={link.href}
                  className="link-sweep text-sm text-muted hover:text-text"
                  {...(link.external
                    ? { target: "_blank", rel: "noopener noreferrer" }
                    : {})}
                >
                  {link.label}
                  {link.external ? <span className="sr-only"> (opens in a new tab)</span> : null}
                </a>
              </li>
            ))}
          </ul>
        </nav>
      </div>
    </footer>
  );
}
