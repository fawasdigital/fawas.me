"use client";

import dynamic from "next/dynamic";
import { useRef } from "react";
import { useSceneGate } from "./use-scene-gate";

const WorkHeaderScene = dynamic(
  () => import("./work-header-scene").then((mod) => mod.WorkHeaderScene),
  { ssr: false },
);

export function WorkCanvas() {
  const ref = useRef<HTMLDivElement>(null);
  const { reduced, active } = useSceneGate(ref);

  return (
    <div ref={ref} className="h-full w-full" aria-hidden="true">
      {reduced === false ? (
        <WorkHeaderScene active={active} />
      ) : (
        <div className="h-full w-full bg-[radial-gradient(circle_at_70%_40%,rgba(124,92,255,0.2),transparent_62%)]" />
      )}
    </div>
  );
}
