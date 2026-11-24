import type { Experience } from "@/content/site";
import { Reveal } from "./reveal";

export function TimelineItem({ item }: { item: Experience }) {
  return (
    <li className="relative border-l border-line py-8 pl-8">
      <span
        className="absolute top-10 -left-[5px] h-2.5 w-2.5 rounded-full bg-accent shadow-[0_0_16px_rgba(124,92,255,0.75)]"
        aria-hidden
      />
      <Reveal>
      <div className="grid gap-2 md:grid-cols-12 md:gap-6">
        <p className="font-mono text-xs text-muted md:col-span-3">{item.dates}</p>
        <div className="md:col-span-9">
          <h3 className="font-display text-2xl tracking-tight">{item.role}</h3>
          <p className="mt-1 text-lg">{item.org}</p>
          <p className="mt-2 text-sm text-muted">
            {[item.place, item.mode].filter(Boolean).join(" · ")}
          </p>
          {item.points.length > 0 ? (
            <ul className="mt-3 max-w-2xl space-y-1.5 text-sm leading-relaxed text-muted">
              {item.points.map((point) => (
                <li key={point}>{point}</li>
              ))}
            </ul>
          ) : null}
        </div>
      </div>
      </Reveal>
    </li>
  );
}
