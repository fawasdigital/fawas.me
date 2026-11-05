import { ClientGrid } from "@/components/client-grid";
import { JsonLd } from "@/components/json-ld";
import { Section } from "@/components/section";
import { TimelineItem } from "@/components/timeline-item";
import { WorkCanvas } from "@/components/work-canvas";
import { site } from "@/content/site";
import { breadcrumbJsonLd, pageMeta } from "@/lib/seo";

export const metadata = pageMeta({
  title: site.seo.work.title,
  description: site.seo.work.description,
  path: "/work",
});

export default function WorkPage() {
  return (
    <>
      <JsonLd
        data={breadcrumbJsonLd([
          { name: site.nav[0].label, path: "/" },
          { name: site.ui.work, path: "/work" },
        ])}
      />
      <div className="relative overflow-hidden">
        <div className="pointer-events-none absolute inset-x-0 top-0 h-64 [mask-image:linear-gradient(90deg,transparent,black_30%)]">
          <WorkCanvas />
        </div>
        <Section className="relative py-20 md:py-28">
          <h1 className="font-display text-[clamp(3.5rem,8vw,7rem)] leading-[0.9] tracking-[-0.05em]">
            {site.ui.work}
          </h1>
          <h2 className="mt-16 font-display text-3xl tracking-tight md:text-4xl">{site.ui.experience}</h2>
          <ol className="mt-4">
            {site.experience.map((item) => (
              <TimelineItem key={`${item.org}-${item.dates}`} item={item} />
            ))}
          </ol>
          <h2 className="mt-20 font-display text-3xl tracking-tight md:text-4xl">{site.ui.clients}</h2>
          <div className="mt-8">
            <ClientGrid />
          </div>
          {/* TODO: case-study cards. Real projects only — no placeholder metrics, quotes, or logos. */}
          <div className="mt-16 rounded-2xl border border-dashed border-white/15 px-6 py-10">
            <p className="font-mono text-sm text-accent">{site.caseStudyTodo}</p>
          </div>
        </Section>
      </div>
    </>
  );
}
