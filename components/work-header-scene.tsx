"use client";

import { useEffect, useMemo, useRef } from "react";
import { Canvas, useFrame } from "@react-three/fiber";
import { BufferAttribute, BufferGeometry, Points } from "three";

function Dust() {
  const ref = useRef<Points>(null);
  const geometry = useMemo(() => {
    const count = 70;
    const positions = new Float32Array(count * 3);
    let seed = 17;
    const random = () => {
      seed = (seed * 16807) % 2147483647;
      return (seed - 1) / 2147483646;
    };
    for (let index = 0; index < count; index += 1) {
      positions[index * 3] = (random() - 0.5) * 9;
      positions[index * 3 + 1] = (random() - 0.5) * 3.2;
      positions[index * 3 + 2] = (random() - 0.5) * 2.4;
    }
    const buffer = new BufferGeometry();
    buffer.setAttribute("position", new BufferAttribute(positions, 3));
    return buffer;
  }, []);

  useEffect(() => () => geometry.dispose(), [geometry]);

  useFrame((_, delta) => {
    if (ref.current) ref.current.rotation.y += delta * 0.04;
  });

  return (
    <points ref={ref} geometry={geometry}>
      <pointsMaterial
        color="#7C5CFF"
        size={0.028}
        transparent
        opacity={0.55}
        sizeAttenuation
        depthWrite={false}
      />
    </points>
  );
}

export function WorkHeaderScene({ active }: { active: boolean }) {
  return (
    <Canvas
      flat
      dpr={[1, 1.5]}
      frameloop={active ? "always" : "never"}
      camera={{ position: [0, 0, 4], fov: 50 }}
      gl={{ alpha: true, antialias: true, powerPreference: "high-performance" }}
      onCreated={({ gl }) => gl.setClearColor(0x000000, 0)}
      style={{ width: "100%", height: "100%" }}
    >
      <Dust />
    </Canvas>
  );
}
