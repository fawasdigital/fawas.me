"use client";

import Link from "next/link";
import { useEffect, useRef, useState, type KeyboardEvent } from "react";
import { usePathname } from "next/navigation";
import { site } from "@/content/site";
import { StatusPill } from "./status-pill";

export function Nav() {
  const pathname = usePathname();
  const [open, setOpen] = useState(false);
  const headerRef = useRef<HTMLElement>(null);
  const buttonRef = useRef<HTMLButtonElement>(null);

  useEffect(() => {
    if (!open) return;
    const onKey = (event: globalThis.KeyboardEvent) => {
      if (event.key === "Escape") {
        setOpen(false);
        buttonRef.current?.focus();
      }
    };
    const previous = document.body.style.overflow;
    document.body.style.overflow = "hidden";
    document.addEventListener("keydown", onKey);
    return () => {
      document.body.style.overflow = previous;
      document.removeEventListener("keydown", onKey);
    };
  }, [open]);

  useEffect(() => {
    const media = window.matchMedia("(min-width: 768px)");
    const onChange = () => {
      if (media.matches) setOpen(false);
    };
    media.addEventListener("change", onChange);
    return () => media.removeEventListener("change", onChange);
  }, []);

  function onKeyDown(event: KeyboardEvent<HTMLElement>) {
    if (!open || event.key !== "Tab") return;
    const root = headerRef.current;
    if (!root) return;
    const items = Array.from(root.querySelectorAll<HTMLElement>("a, button"));
    const first = items[0];
    const last = items[items.length - 1];
    if (!first || !last) return;
    if (event.shiftKey && document.activeElement === first) {
      event.preventDefault();
      last.focus();
    } else if (!event.shiftKey && document.activeElement === last) {
      event.preventDefault();
      first.focus();
    }
  }

  return (
    <header
      ref={headerRef}
      onKeyDown={onKeyDown}
      className="sticky top-0 z-50 border-b border-line bg-bg"
    >
      <nav
        aria-label={site.ui.primaryNav}
        className="mx-auto flex h-16 w-full max-w-[1200px] items-center justify-between gap-4 px-5 md:px-8"
      >
        <Link href="/" className="font-display text-lg tracking-tight">
          <span className="sm:hidden">Fawas</span>
          <span className="hidden sm:inline">{site.name}</span>
        </Link>

        <ul className="hidden items-center gap-7 md:flex">
          {site.nav.map((item) => {
            const current = pathname === item.href;
            return (
              <li key={item.href}>
                <Link
                  href={item.href}
                  aria-current={current ? "page" : undefined}
                  className={`link-sweep text-sm ${current ? "text-text" : "text-muted hover:text-text"}`}
                  onClick={() => setOpen(false)}
                >
                  {item.label}
                </Link>
              </li>
            );
          })}
        </ul>

        <div className="flex items-center gap-2">
          <StatusPill className="hidden sm:inline-flex" />
          <button
            ref={buttonRef}
            type="button"
            className="relative h-11 w-11 md:hidden"
            aria-expanded={open}
            aria-controls="mobile-nav"
            onClick={() => setOpen((value) => !value)}
          >
            <span className="sr-only">{open ? site.ui.closeMenu : site.ui.openMenu}</span>
            <span
              className={`absolute top-1/2 right-3 left-3 h-px origin-center bg-text transition-transform ${open ? "rotate-45" : "-translate-y-[5px]"}`}
            />
            <span
              className={`absolute top-1/2 right-3 left-3 h-px origin-center bg-text transition-transform ${open ? "-rotate-45" : "translate-y-[5px]"}`}
            />
          </button>
        </div>
      </nav>

      {open ? (
        <div id="mobile-nav" className="fixed inset-0 top-16 z-40 flex flex-col bg-bg px-6 pt-8 md:hidden">
          <StatusPill className="mb-10 inline-flex w-fit" />
          <ul className="flex flex-col gap-5">
            {site.nav.map((item) => {
              const current = pathname === item.href;
              return (
                <li key={item.href}>
                  <Link
                    href={item.href}
                    aria-current={current ? "page" : undefined}
                    className="font-display text-5xl tracking-tight"
                    onClick={() => setOpen(false)}
                  >
                    {item.label}
                  </Link>
                </li>
              );
            })}
          </ul>
        </div>
      ) : null}
    </header>
  );
}
