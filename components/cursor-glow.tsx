"use client";

import { useEffect, useRef } from "react";

export function CursorGlow() {
  const ref = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const el = ref.current;
    if (!el) return;
    const reduce = window.matchMedia("(prefers-reduced-motion: reduce)");
    const fine = window.matchMedia("(pointer: fine)");
    if (reduce.matches || !fine.matches) return;

    const onMove = (event: PointerEvent) => {
      el.style.opacity = "1";
      el.style.transform = `translate3d(${event.clientX - 220}px, ${event.clientY - 220}px, 0)`;
    };

    window.addEventListener("pointermove", onMove, { passive: true });
    return () => window.removeEventListener("pointermove", onMove);
  }, []);

  return (
    <div
      ref={ref}
      aria-hidden
      className="pointer-events-none fixed top-0 left-0 z-0 h-[440px] w-[440px] opacity-0"
      style={{
        background: "radial-gradient(circle, rgba(124,92,255,0.16), transparent 68%)",
      }}
    />
  );
}
