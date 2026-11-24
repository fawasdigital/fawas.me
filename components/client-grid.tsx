import { site } from "@/content/site";

export function ClientGrid() {
  return (
    <ul className="grid grid-cols-2 gap-px overflow-hidden rounded-2xl border border-line bg-line md:grid-cols-5">
      {site.brands.map((brand) => (
        <li key={brand} className="bg-surface">
          <p className="flex min-h-32 items-center px-5 py-6 font-display text-lg tracking-tight text-balance text-muted">
            {brand}
          </p>
        </li>
      ))}
    </ul>
  );
}
