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
        <h2 className="mt-20 font-display text-3xl tracking-tight md:text-4xl">{site.ui.services}</h2>
        <ul className="mt-6 flex max-w-3xl flex-wrap gap-2">
          {site.services.map((service) => (
            <li
              key={service}
              className="rounded-full border border-line bg-surface px-4 py-2 text-sm text-muted"
            >
              {service}
            </li>
          ))}
        </ul>

        <h2 className="mt-20 font-display text-3xl tracking-tight md:text-4xl">{site.ui.skills}</h2>
        <div className="mt-8 grid gap-px overflow-hidden rounded-2xl border border-line bg-line md:grid-cols-2">
          {site.skills.map((group) => (
            <div key={group.label} className="bg-surface px-6 py-6">
              <h3 className="font-mono text-xs tracking-wide text-accent">{group.label}</h3>
              <ul className="mt-4 flex flex-wrap gap-2">
                {group.items.map((item) => (
                  <li key={item} className="rounded-full border border-line px-3 py-1 text-sm text-muted">
                    {item}
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </div>

        <h2 className="mt-20 font-display text-3xl tracking-tight md:text-4xl">{site.ui.keyResults}</h2>
        <ul className="mt-6 max-w-3xl space-y-4">
          {site.keyResults.map((item) => (
            <li key={item.label} className="border-t border-line pt-4">
              <p className="font-mono text-xs text-accent">{item.label}</p>
              <p className="mt-2 text-base leading-relaxed text-muted">{item.detail}</p>
            </li>
          ))}
        </ul>

        <h2 className="mt-20 font-display text-3xl tracking-tight md:text-4xl">{site.ui.recognition}</h2>
        <ul className="mt-6 max-w-3xl space-y-4">
          {site.recognition.map((item) => (
            <li key={item.title} className="rounded-2xl border border-line bg-surface px-6 py-6">
              <p className="font-mono text-xs text-muted">{item.date}</p>
              <h3 className="mt-2 font-display text-2xl tracking-tight">{item.title}</h3>
              <p className="mt-1 text-sm text-muted">{item.org}</p>
              <p className="mt-3 text-sm leading-relaxed text-muted">{item.detail}</p>
            </li>
          ))}
        </ul>

        <h2 className="mt-20 font-display text-3xl tracking-tight md:text-4xl">{site.ui.certifications}</h2>
        <ul className="mt-6 max-w-3xl space-y-3">
          {site.certifications.map((item) => (
            <li key={item} className="border-t border-line pt-3 text-base text-muted">
              {item}
            </li>
          ))}
        </ul>

        <h2 className="mt-20 font-display text-3xl tracking-tight md:text-4xl">{site.ui.education}</h2>
        <ul className="mt-6 max-w-3xl">
          {site.education.map((item) => (
            <li key={item.credential} className="border-t border-line py-5">
              <div className="grid gap-2 md:grid-cols-12 md:gap-6">
                <p className="font-mono text-xs text-muted md:col-span-3">{item.dates}</p>
                <div className="md:col-span-9">
                  <h3 className="font-display text-xl tracking-tight">{item.credential}</h3>
                  <p className="mt-1 text-sm text-muted">
                    {item.org} · {item.place}
                  </p>
                </div>
              </div>
            </li>
          ))}
        </ul>

        <p className="mt-28 max-w-5xl font-display text-[clamp(2.75rem,7vw,5.75rem)] leading-[0.95] tracking-[-0.045em]">
          {site.tagline}
        </p>
      </Section>
    </>
  );
}
