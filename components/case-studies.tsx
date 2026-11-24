import { site, type CaseStudy } from "@/content/site";
import { Reveal } from "./reveal";

function Study({ study }: { study: CaseStudy }) {
  return (
    <Reveal>
      <article className="rounded-2xl border border-line bg-surface px-6 py-8 md:px-8">
        <div className="flex flex-wrap items-baseline justify-between gap-x-6 gap-y-2">
          <h3 className="font-display text-2xl tracking-tight md:text-3xl">
            {"href" in study ? (
              <a
                href={study.href}
                className="link-sweep"
                target="_blank"
                rel="noopener noreferrer"
              >
                {study.name}
                <span className="sr-only"> (opens in a new tab)</span>
              </a>
            ) : (
              study.name
            )}
          </h3>
          <p className="font-mono text-xs text-muted">{study.duration}</p>
        </div>
        <p className="mt-2 text-sm text-muted">
          {study.industry} · {study.market}
        </p>
        <p className="mt-4 max-w-3xl text-base leading-relaxed text-pretty text-muted">{study.summary}</p>
        {study.metrics.length > 0 ? (
          <dl
            className={`mt-6 grid grid-cols-2 gap-px overflow-hidden rounded-xl border border-line bg-line ${
              study.metrics.length >= 4
                ? "sm:grid-cols-2 lg:grid-cols-4"
                : study.metrics.length === 3
                  ? "sm:grid-cols-3"
                  : "sm:grid-cols-2"
            }`}
          >
            {study.metrics.map((metric) => (
              <div key={metric.label} className="bg-surface px-4 py-4">
                <dt className="font-mono text-[11px] tracking-wide text-muted">{metric.label}</dt>
                <dd className="mt-2 font-display text-xl tracking-tight text-balance md:text-2xl">
                  {metric.value}
                </dd>
              </div>
            ))}
          </dl>
        ) : null}
        {study.highlights.length > 0 ? (
          <ul className="mt-5 max-w-3xl space-y-2 text-sm leading-relaxed text-muted">
            {study.highlights.map((item) => (
              <li key={item}>{item}</li>
            ))}
          </ul>
        ) : null}
        {"rankings" in study ? (
          <div className="mt-6 overflow-x-auto">
            <p className="font-mono text-[11px] tracking-wide text-accent">{study.rankings.label}</p>
            <table className="mt-3 w-full min-w-[28rem] border-collapse text-left text-sm">
              <thead>
                <tr className="border-b border-line">
                  {study.rankings.headers.map((header, index) => (
                    <th
                      key={header}
                      scope="col"
                      className={`px-3 py-2 font-mono text-[11px] font-normal tracking-wide text-muted ${index === 0 ? "text-left" : "text-right"}`}
                    >
                      {header}
                    </th>
                  ))}
                </tr>
              </thead>
              <tbody>
                {study.rankings.rows.map((row) => (
                  <tr key={row.join("|")} className="border-b border-line last:border-b-0">
                    {row.map((cell, index) => (
                      <td
                        key={`${cell}-${index}`}
                        className={`px-3 py-2.5 text-muted ${index === 0 ? "text-text" : "text-right font-mono text-xs"}`}
                      >
                        {cell}
                      </td>
                    ))}
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        ) : null}
      </article>
    </Reveal>
  );
}

export function CaseStudies() {
  return (
    <div className="mt-8 space-y-4">
      {site.caseStudies.map((study) => (
        <Study key={study.name} study={study} />
      ))}
    </div>
  );
}
