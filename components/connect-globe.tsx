"use client";

import { useRef } from "react";
import { Canvas, useFrame } from "@react-three/fiber";
import type { Group } from "three";
import { site } from "@/content/site";

function latLngToVec(lat: number, lng: number, radius: number): [number, number, number] {
  const phi = ((90 - lat) * Math.PI) / 180;
  const theta = ((lng + 180) * Math.PI) / 180;
  return [
    -(radius * Math.sin(phi) * Math.cos(theta)),
    radius * Math.cos(phi),
    radius * Math.sin(phi) * Math.sin(theta),
  ];
}

function Globe() {
  const ref = useRef<Group>(null);
  const dubai = latLngToVec(site.connect.places.dubai.lat, site.connect.places.dubai.lng, 1.04);
  const kerala = latLngToVec(site.connect.places.kerala.lat, site.connect.places.kerala.lng, 1.04);

  useFrame(({ clock }) => {
    if (!ref.current) return;
    ref.current.rotation.y = Math.PI + 0.42 + Math.sin(clock.elapsedTime * 0.35) * 0.28;
  });

  return (
    <group ref={ref} rotation={[0.2, 0, 0]}>
      <mesh>
        <sphereGeometry args={[0.98, 32, 32]} />
        <meshBasicMaterial color="#111114" />
      </mesh>
      <mesh>
        <sphereGeometry args={[1, 24, 24]} />
        <meshBasicMaterial color="#7C5CFF" wireframe transparent opacity={0.45} />
      </mesh>
      <mesh position={dubai}>
        <sphereGeometry args={[0.045, 12, 12]} />
        <meshBasicMaterial color="#EDEDED" />
      </mesh>
      <mesh position={kerala}>
        <sphereGeometry args={[0.045, 12, 12]} />
        <meshBasicMaterial color="#7C5CFF" />
      </mesh>
    </group>
  );
}

export function ConnectGlobe({ active }: { active: boolean }) {
  return (
    <Canvas
      flat
      dpr={[1, 1.5]}
      frameloop={active ? "always" : "never"}
      camera={{ position: [0, 0, 2.7], fov: 40 }}
      gl={{ alpha: true, antialias: true, powerPreference: "high-performance" }}
      onCreated={({ gl }) => gl.setClearColor(0x000000, 0)}
      style={{ width: "100%", height: "100%" }}
    >
      <Globe />
    </Canvas>
  );
}
