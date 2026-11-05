import type { Metadata } from "next";
import Link from "next/link";
import { site } from "@/content/site";

export const metadata: Metadata = {
  title: site.ui.notFoundTitle,
  description: site.ui.notFoundBody,
  robots: { index: false, follow: false },
};

export default function NotFound() {
  return (
    <section className="mx-auto flex min-h-[60vh] w-full max-w-[1200px] flex-col justify-center px-5 md:px-8">
      <h1 className="font-display text-[clamp(3rem,8vw,6rem)] leading-[0.9] tracking-[-0.05em]">
        {site.ui.notFoundTitle}
      </h1>
      <p className="mt-4 text-muted">{site.ui.notFoundBody}</p>
      <Link href="/" className="link-sweep mt-8 w-fit text-text">
        {site.ui.backHome}
      </Link>
    </section>
  );
}
