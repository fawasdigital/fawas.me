import { site } from "@/content/site";
import { Reveal } from "./reveal";

export function BrandStrip() {
  return (
    <section aria-label={site.ui.brands} className="border-t border-line">
      <Reveal>
        <ul className="mx-auto grid w-full max-w-[1200px] grid-cols-2 md:grid-cols-3 xl:grid-cols-6">
          {site.brands.map((brand) => (
            <li key={brand} className="border-line border-r border-b px-4 py-8 xl:border-b-0">
              <p className="text-center font-display text-sm tracking-tight text-balance text-muted">
                {brand}
              </p>
            </li>
          ))}
        </ul>
      </Reveal>
    </section>
  );
}
