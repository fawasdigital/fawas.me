import { BrandStrip } from "@/components/brand-strip";
import { HeroCanvas } from "@/components/hero-canvas";
import { JsonLd } from "@/components/json-ld";
import { MagneticButton } from "@/components/magnetic-button";
import { site } from "@/content/site";
import { personJsonLd } from "@/lib/seo";

export default function HomePage() {
  const [first, ...rest] = site.name.split(" ");

  return (
    <>
      <JsonLd data={personJsonLd()} />
      <section className="mx-auto grid w-full max-w-[1200px] items-center gap-8 px-5 py-12 md:min-h-[calc(100svh-4rem)] md:grid-cols-12 md:px-8 md:py-16">
        <div className="order-2 md:order-1 md:col-span-7">
          <h1 className="font-display text-[clamp(3.5rem,7.2vw,8rem)] leading-[0.86] tracking-[-0.05em]">
            {first}
            <br />
            {rest.join(" ")}
          </h1>
          <p className="mt-6 max-w-md text-lg text-muted md:text-xl">{site.role}</p>
          <p className="mt-8 max-w-xl text-base leading-relaxed text-pretty md:text-lg">{site.home.intro}</p>
          <p className="mt-4 max-w-xl text-base leading-relaxed text-pretty text-muted md:text-lg">
            {site.home.second}
          </p>
          <div className="mt-10 flex flex-wrap items-center gap-3">
            <MagneticButton href="/work">{site.home.ctas.work}</MagneticButton>
            <MagneticButton href="/about" variant="ghost">
              {site.home.ctas.about}
            </MagneticButton>
            <MagneticButton href="/connect" variant="text">
              {site.home.ctas.connect}
            </MagneticButton>
          </div>
        </div>
        <div className="order-1 h-[220px] sm:h-[280px] md:order-2 md:col-span-5 md:h-[480px]">
          <HeroCanvas />
        </div>
      </section>
      <BrandStrip />
    </>
  );
}
