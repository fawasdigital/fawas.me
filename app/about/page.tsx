import { JsonLd } from "@/components/json-ld";
import { Reveal } from "@/components/reveal";
import { RichText } from "@/components/rich-text";
import { Section } from "@/components/section";
import { site } from "@/content/site";
import { breadcrumbJsonLd, pageMeta, profilePageJsonLd } from "@/lib/seo";

export const metadata = pageMeta({
  title: site.seo.about.title,
  description: site.seo.about.description,
  path: "/about",
});

export default function AboutPage() {
  return (
    <>
      <JsonLd data={profilePageJsonLd()} />
      <JsonLd
        data={breadcrumbJsonLd([
          { name: site.nav[0].label, path: "/" },
          { name: site.ui.about, path: "/about" },
        ])}
      />
      <Section className="py-20 md:py-28">
        <h1 className="font-display text-[clamp(3.5rem,8vw,7rem)] leading-[0.9] tracking-[-0.05em]">
          {site.ui.about}
        </h1>
        <div className="mt-12 max-w-3xl space-y-8">
          {site.about.map((paragraph) => (
            <Reveal key={paragraph.map((part) => part.text).join("")}>
              <RichText
                parts={paragraph}
                className="text-xl leading-snug text-pretty text-muted md:text-2xl"
              />
            </Reveal>
          ))}
        </div>
        <p className="mt-28 max-w-5xl font-display text-[clamp(2.75rem,7vw,5.75rem)] leading-[0.95] tracking-[-0.045em]">
          {site.tagline}
        </p>
      </Section>
    </>
  );
}
