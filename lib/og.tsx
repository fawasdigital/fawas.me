import { ImageResponse } from "next/og";

export const ogSize = { width: 1200, height: 630 };
export const ogContentType = "image/png";

export function renderOg(title: string, subtitle: string) {
  return new ImageResponse(
    (
      <div
        style={{
          width: "100%",
          height: "100%",
          display: "flex",
          flexDirection: "column",
          justifyContent: "space-between",
          background: "#0A0A0B",
          color: "#EDEDED",
          padding: "72px",
        }}
      >
        <div style={{ display: "flex", alignItems: "center", fontSize: 24, color: "#8A8A93" }}>
          <div
            style={{
              width: 14,
              height: 14,
              borderRadius: 99,
              background: "#3DDC97",
              marginRight: 12,
            }}
          />
          Available
        </div>
        <div style={{ display: "flex", flexDirection: "column" }}>
          <div style={{ fontSize: 84, letterSpacing: "-0.045em", lineHeight: 0.95 }}>{title}</div>
          <div style={{ marginTop: 24, fontSize: 32, color: "#8A8A93" }}>{subtitle}</div>
        </div>
        <div style={{ display: "flex", justifyContent: "space-between", fontSize: 24 }}>
          <div style={{ color: "#7C5CFF" }}>fawas.me</div>
          <div style={{ color: "#8A8A93" }}>Digital Marketer & SEO Specialist</div>
        </div>
      </div>
    ),
    { ...ogSize },
  );
}
