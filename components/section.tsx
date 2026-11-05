import type { ReactNode } from "react";

export function Section({
  children,
  className = "",
  id,
  label,
}: {
  children: ReactNode;
  className?: string;
  id?: string;
  label?: string;
}) {
  return (
    <section
      id={id}
      aria-label={label}
      className={`mx-auto w-full max-w-[1200px] px-5 md:px-8 ${className}`}
    >
      {children}
    </section>
  );
}
