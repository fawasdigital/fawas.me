"use client";

import { FormEvent, useState } from "react";
import { site } from "@/content/site";
import { buttonClass, useMagnetic } from "./magnetic-button";

type Errors = {
  name?: string;
  email?: string;
  message?: string;
  form?: string;
};

const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

export function ContactForm() {
  const [errors, setErrors] = useState<Errors>({});
  const [pending, setPending] = useState(false);
  const [done, setDone] = useState(false);
  const { ref, onMouseMove, onMouseLeave } = useMagnetic<HTMLButtonElement>();

  async function onSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    const form = event.currentTarget;
    const data = new FormData(form);
    const name = String(data.get("name") ?? "").trim();
    const email = String(data.get("email") ?? "").trim();
    const message = String(data.get("message") ?? "").trim();
    const next: Errors = {};

    if (name.length < 2) next.name = site.form.nameError;
    if (!emailPattern.test(email)) next.email = site.form.emailError;
    if (message.length < 1) next.message = site.form.messageError;
    setErrors(next);
    if (Object.keys(next).length > 0) return;

    setPending(true);
    try {
      const response = await fetch("/api/contact", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, email, message }),
      });
      const payload = (await response.json()) as { ok?: boolean; error?: string };
      if (!response.ok || !payload.ok) {
        setErrors({ form: payload.error ?? site.form.error });
        return;
      }
      setDone(true);
      setErrors({});
    } catch {
      setErrors({ form: site.form.error });
    } finally {
      setPending(false);
    }
  }

  if (done) {
    return (
      <div className="rounded-2xl border border-line bg-surface p-6 md:p-8" role="status">
        <p className="font-display text-2xl tracking-tight">{site.form.success}</p>
        <button
          type="button"
          className={`${buttonClass.ghost} mt-6`}
          onClick={() => setDone(false)}
        >
          {site.form.another}
        </button>
      </div>
    );
  }

  return (
    <form
      noValidate
      onSubmit={onSubmit}
      aria-label={site.ui.contactForm}
      className="rounded-2xl border border-line bg-surface p-6 md:p-8"
    >
      <div className="grid gap-5">
        <Field
          id="name"
          name="name"
          label={site.form.name}
          autoComplete="name"
          error={errors.name}
        />
        <Field
          id="email"
          name="email"
          type="email"
          label={site.form.email}
          autoComplete="email"
          error={errors.email}
        />
        <div>
          <label htmlFor="message" className="font-mono text-xs text-muted">
            {site.form.message}
          </label>
          <textarea
            id="message"
            name="message"
            rows={6}
            autoComplete="off"
            aria-invalid={errors.message ? true : undefined}
            aria-describedby={errors.message ? "message-error" : undefined}
            className="mt-2 w-full resize-y rounded-xl border border-line bg-bg px-4 py-3 text-base text-text"
          />
          {errors.message ? (
            <p id="message-error" className="mt-2 text-sm text-accent">
              {errors.message}
            </p>
          ) : null}
        </div>
      </div>

      {errors.form ? (
        <p className="mt-4 text-sm text-accent" role="alert">
          {errors.form}
        </p>
      ) : null}

      <button
        ref={ref}
        type="submit"
        disabled={pending}
        aria-busy={pending}
        onMouseMove={onMouseMove}
        onMouseLeave={onMouseLeave}
        className={`${buttonClass.solid} mt-6 disabled:pointer-events-none disabled:opacity-60`}
      >
        {pending ? site.form.sending : site.form.submit}
      </button>
    </form>
  );
}

function Field({
  id,
  name,
  label,
  error,
  type = "text",
  autoComplete,
}: {
  id: string;
  name: string;
  label: string;
  error?: string;
  type?: string;
  autoComplete: string;
}) {
  return (
    <div>
      <label htmlFor={id} className="font-mono text-xs text-muted">
        {label}
      </label>
      <input
        id={id}
        name={name}
        type={type}
        autoComplete={autoComplete}
        aria-invalid={error ? true : undefined}
        aria-describedby={error ? `${id}-error` : undefined}
        className="mt-2 w-full rounded-xl border border-line bg-bg px-4 py-3 text-base text-text"
      />
      {error ? (
        <p id={`${id}-error`} className="mt-2 text-sm text-accent">
          {error}
        </p>
      ) : null}
    </div>
  );
}
