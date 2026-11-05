"use client";

import Link from "next/link";
import { useRef, type MouseEvent, type ReactNode, type Ref } from "react";

type Variant = "solid" | "ghost" | "text";

export const buttonClass: Record<Variant, string> = {
  solid:
    "inline-flex min-h-11 items-center justify-center rounded-full bg-accent px-5 text-[15px] font-medium text-bg hover:brightness-110",
  ghost:
    "inline-flex min-h-11 items-center justify-center rounded-full border border-line bg-surface px-5 text-[15px] text-text hover:border-white/20",
  text: "inline-flex min-h-11 items-center text-[15px] text-muted link-sweep hover:text-text",
};

export function useMagnetic<T extends HTMLElement>() {
  const ref = useRef<T>(null);

  function onMouseMove(event: MouseEvent<T>) {
    const el = ref.current;
    if (!el) return;
    if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;
    if (!window.matchMedia("(pointer: fine)").matches) return;

    const rect = el.getBoundingClientRect();
    const x = event.clientX - (rect.left + rect.width / 2);
    const y = event.clientY - (rect.top + rect.height / 2);
    el.style.transition = "transform 80ms linear";
    el.style.transform = `translate3d(${x * 0.22}px, ${y * 0.3}px, 0)`;
  }

  function onMouseLeave() {
    const el = ref.current;
    if (!el) return;
    el.style.transition = "transform 500ms cubic-bezier(0.22, 1, 0.36, 1)";
    el.style.transform = "translate3d(0, 0, 0)";
  }

  return { ref, onMouseMove, onMouseLeave };
}

export function MagneticButton({
  href,
  children,
  variant = "solid",
  className = "",
}: {
  href: string;
  children: ReactNode;
  variant?: Variant;
  className?: string;
}) {
  const { ref, onMouseMove, onMouseLeave } = useMagnetic<HTMLAnchorElement>();
  const classes = `${buttonClass[variant]} ${className}`;
  const external = href.startsWith("http");

  if (external) {
    return (
      <a
        ref={ref}
        href={href}
        className={classes}
        onMouseMove={onMouseMove}
        onMouseLeave={onMouseLeave}
        target="_blank"
        rel="noopener noreferrer"
      >
        {children}
        <span className="sr-only"> (opens in a new tab)</span>
      </a>
    );
  }

  return (
    <Link
      ref={ref as Ref<HTMLAnchorElement>}
      href={href}
      className={classes}
      onMouseMove={onMouseMove}
      onMouseLeave={onMouseLeave}
    >
      {children}
    </Link>
  );
}
