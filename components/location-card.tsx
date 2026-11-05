import { mapEmbedSrc, site } from "@/content/site";

export function LocationCard() {
  return (
    <>
      <div className="mt-6 overflow-hidden rounded-2xl border border-line bg-surface">
        <div className="relative h-52 overflow-hidden bg-[#0d0d10]">
          <div className="absolute inset-0 bg-[radial-gradient(circle_at_30%_40%,rgba(124,92,255,0.22),transparent_58%)]" />
          <iframe
            title={site.ui.mapTitle}
            src={mapEmbedSrc()}
            className="map-dark absolute inset-x-0 top-0 h-[calc(100%+40px)] w-full border-0"
            loading="lazy"
            referrerPolicy="no-referrer-when-downgrade"
          />
        </div>
      </div>
      <p className="mt-3 font-mono text-[11px] text-muted">Map data © OpenStreetMap</p>
    </>
  );
}
