"use client";

import dynamic from "next/dynamic";
import { useRef, useState } from "react";
import { HeroFallback } from "./hero-fallback";
import { useSceneGate } from "./use-scene-gate";

const HeroScene = dynamic(() => import("./hero-scene").then((mod) => mod.HeroScene), {
  ssr: false,
});

export function HeroCanvas() {
  const ref = useRef<HTMLDivElement>(null);
  const { reduced, active } = useSceneGate(ref);
  const [lowFps, setLowFps] = useState(false);
  const webgl = reduced === false && !lowFps;

  return (
    <div ref={ref} className="relative h-full w-full" aria-hidden="true">
      {webgl ? (
        <HeroScene active={active} onLowFps={() => setLowFps(true)} />
      ) : (
        <HeroFallback variant={lowFps ? "gradient" : "wire"} />
      )}
    </div>
  );
}
