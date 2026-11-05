export function HeroFallback({ variant = "wire" }: { variant?: "wire" | "gradient" }) {
  if (variant === "gradient") {
    return (
      <div
        className="h-full w-full"
        style={{
          background:
            "radial-gradient(circle at 50% 45%, rgba(124,92,255,0.55), rgba(124,92,255,0.08) 42%, transparent 70%)",
        }}
      />
    );
  }

  return (
    <svg viewBox="0 0 200 200" className="h-full w-full" aria-hidden>
      <g fill="none" stroke="#7C5CFF" strokeWidth="1.25">
        <polygon points="100,18 168,56 168,132 100,170 32,132 32,56" opacity="0.9" />
        <polygon points="100,18 168,132 32,132" opacity="0.7" />
        <polygon points="32,56 168,56 100,170" opacity="0.7" />
        <path d="M100 18 L100 170 M32 56 L168 132 M168 56 L32 132" opacity="0.45" />
      </g>
    </svg>
  );
}
