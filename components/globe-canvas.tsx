"use client";

import dynamic from "next/dynamic";
import { useRef } from "react";
import { useSceneGate } from "./use-scene-gate";

const ConnectGlobe = dynamic(
  () => import("./connect-globe").then((mod) => mod.ConnectGlobe),
  { ssr: false },
);

function GlobeFallback() {
  return (
    <svg viewBox="0 0 100 100" className="h-full w-full" aria-hidden>
      <circle cx="50" cy="50" r="34" fill="#111114" stroke="#7C5CFF" strokeOpacity="0.8" />
      <ellipse cx="50" cy="50" rx="16" ry="34" fill="none" stroke="#7C5CFF" strokeOpacity="0.45" />
      <ellipse cx="50" cy="50" rx="34" ry="12" fill="none" stroke="#7C5CFF" strokeOpacity="0.45" />
      <circle cx="62" cy="42" r="3" fill="#EDEDED" />
      <circle cx="68" cy="54" r="3" fill="#7C5CFF" />
    </svg>
  );
}

export function GlobeCanvas() {
  const ref = useRef<HTMLDivElement>(null);
  const { reduced, active } = useSceneGate(ref);

  return (
    <div ref={ref} className="h-full w-full" aria-hidden="true">
      {reduced === false ? <ConnectGlobe active={active} /> : <GlobeFallback />}
    </div>
  );
}
