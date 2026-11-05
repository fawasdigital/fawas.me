import type { TextPart } from "@/content/site";

export function RichText({
  parts,
  className = "",
}: {
  parts: readonly TextPart[];
  className?: string;
}) {
  return (
    <p className={className}>
      {parts.map((part, index) =>
        part.strong ? (
          <strong key={index} className="font-medium text-text">
            {part.text}
          </strong>
        ) : (
          <span key={index}>{part.text}</span>
        ),
      )}
    </p>
  );
}
