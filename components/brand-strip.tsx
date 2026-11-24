import { site } from "@/content/site";
import { Reveal } from "./reveal";

export function BrandStrip() {
  return (
    <section aria-label={site.ui.brands} className="border-t border-line">
      <Reveal>
        <ul className="mx-auto grid w-full max-w-[1200px] grid-cols-2 border-line sm:grid-cols-3 lg:grid-cols-5">
          {site.brands.map((brand) => (
            <li key={brand} className="border-r border-b border-line px-4 py-8">
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
