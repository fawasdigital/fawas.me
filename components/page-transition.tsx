"use client";

import { motion, useReducedMotion } from "framer-motion";
import { usePathname } from "next/navigation";
import { useState, type ReactNode } from "react";

export function PageTransition({ children }: { children: ReactNode }) {
  const pathname = usePathname();
  const reduced = useReducedMotion();
  const [displayed, setDisplayed] = useState(pathname);
  const [moves, setMoves] = useState(0);

  if (pathname !== displayed) {
    setDisplayed(pathname);
    setMoves((count) => count + 1);
  }

  const animate = moves > 0 && !reduced;

  return (
    <motion.div
      key={pathname}
      initial={animate ? { opacity: 0, y: 10 } : false}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.45, ease: [0.22, 1, 0.36, 1] }}
    >
      {children}
    </motion.div>
  );
}
