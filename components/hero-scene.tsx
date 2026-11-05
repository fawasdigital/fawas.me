"use client";

import { useEffect, useRef } from "react";
import { Canvas, useFrame } from "@react-three/fiber";
import { Float, MeshDistortMaterial } from "@react-three/drei";
import type { Group } from "three";

function Orb({ onLowFps }: { onLowFps: () => void }) {
  const group = useRef<Group>(null);
  const mouse = useRef({ x: 0, y: 0 });
  const stats = useRef({ frames: 0, time: 0, dropped: false });

  useEffect(() => {
    const onMove = (event: PointerEvent) => {
      mouse.current.x = (event.clientX / window.innerWidth) * 2 - 1;
      mouse.current.y = -((event.clientY / window.innerHeight) * 2 - 1);
    };
    window.addEventListener("pointermove", onMove, { passive: true });
    return () => window.removeEventListener("pointermove", onMove);
  }, []);

  useFrame(({ clock }, delta) => {
    const node = group.current;
    if (!node) return;
    node.rotation.y = clock.elapsedTime * 0.18 + mouse.current.x * 0.45;
    node.rotation.x = mouse.current.y * 0.28;

    const sample = stats.current;
    if (sample.dropped) return;
    if (delta > 0.5) {
      sample.frames = 0;
      sample.time = 0;
      return;
    }
    sample.frames += 1;
    sample.time += delta;
    if (sample.time < 1.6) return;
    const fps = sample.frames / sample.time;
    sample.frames = 0;
    sample.time = 0;
    if (window.innerWidth < 768 && fps < 28) {
      sample.dropped = true;
      onLowFps();
    }
  });

  return (
    <Float speed={1.2} rotationIntensity={0.12} floatIntensity={0.35}>
      <group ref={group} scale={0.78}>
        <mesh>
          <icosahedronGeometry args={[1.25, 5]} />
          <MeshDistortMaterial
            color="#7C5CFF"
            emissive="#6a48ff"
            emissiveIntensity={0.4}
            roughness={0.62}
            metalness={0}
            distort={0.28}
            speed={1.2}
          />
        </mesh>
        <mesh>
          <icosahedronGeometry args={[1.58, 1]} />
          <meshBasicMaterial color="#7C5CFF" wireframe transparent opacity={0.38} />
        </mesh>
      </group>
    </Float>
  );
}

export function HeroScene({
  active,
  onLowFps,
}: {
  active: boolean;
  onLowFps: () => void;
}) {
  return (
    <Canvas
      flat
      dpr={[1, 1.5]}
      frameloop={active ? "always" : "never"}
      camera={{ position: [0, 0, 5.8], fov: 34 }}
      gl={{ alpha: true, antialias: true, powerPreference: "high-performance" }}
      onCreated={({ gl }) => gl.setClearColor(0x000000, 0)}
      style={{ width: "100%", height: "100%" }}
    >
      <ambientLight intensity={1.15} />
      <directionalLight position={[2.2, 1.4, 3.2]} intensity={0.45} />
      <Orb onLowFps={onLowFps} />
    </Canvas>
  );
}
