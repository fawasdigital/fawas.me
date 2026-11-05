import { site } from "@/content/site";

export function StatusPill({ className = "" }: { className?: string }) {
  return (
    <p
      className={`items-center gap-2 rounded-full border border-line bg-surface px-3 py-1.5 font-mono text-[11px] tracking-wide text-text ${className}`}
    >
      <span className="pulse-dot inline-block h-1.5 w-1.5 rounded-full bg-[#3DDC97]" aria-hidden />
      {site.status}
    </p>
  );
}
