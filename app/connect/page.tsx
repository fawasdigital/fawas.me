import { ContactForm } from "@/components/contact-form";
import { GlobeCanvas } from "@/components/globe-canvas";
import { JsonLd } from "@/components/json-ld";
import { LocationCard } from "@/components/location-card";
import { MagneticButton } from "@/components/magnetic-button";
import { Section } from "@/components/section";
import { mailto, site } from "@/content/site";
import { breadcrumbJsonLd, contactPageJsonLd, pageMeta } from "@/lib/seo";

const channels = [
  { href: mailto(), label: "Email" },
  { href: site.social.whatsapp, label: "WhatsApp" },
  { href: site.social.linkedin, label: "LinkedIn" },
  { href: site.social.x, label: "X" },
];

export const metadata = pageMeta({
  title: site.seo.connect.title,
  description: site.seo.connect.description,
  path: "/connect",
});

export default function ConnectPage() {
  return (
    <>
      <JsonLd data={contactPageJsonLd()} />
      <JsonLd
        data={breadcrumbJsonLd([
          { name: site.nav[0].label, path: "/" },
          { name: site.ui.connect, path: "/connect" },
        ])}
      />
      <Section className="py-20 md:py-28">
        <h1 className="font-display text-[clamp(3.5rem,8vw,7rem)] leading-[0.9] tracking-[-0.05em]">
          {site.ui.connect}
        </h1>
        <p className="mt-8 max-w-xl text-lg leading-relaxed text-pretty text-muted">{site.connect.intro}</p>
        <div className="mt-10 flex flex-wrap gap-3">
          {channels.map((channel) => (
            <MagneticButton key={channel.label} href={channel.href} variant="ghost">
              {channel.label}
            </MagneticButton>
          ))}
        </div>

        <div className="mt-20 grid items-start gap-12 lg:grid-cols-12">
          <div className="lg:col-span-5">
            <div className="flex items-start justify-between gap-4">
              <h2 className="font-display text-[clamp(1.75rem,3vw,2.4rem)] leading-tight tracking-tight">
                {site.connect.location}
              </h2>
              <div className="h-24 w-24 shrink-0 sm:h-28 sm:w-28">
                <GlobeCanvas />
              </div>
            </div>
            <LocationCard />
            <p className="mt-4 text-sm leading-relaxed text-muted">{site.connect.also}</p>
          </div>
          <div className="lg:col-span-7">
            <ContactForm />
          </div>
        </div>
      </Section>
    </>
  );
}
