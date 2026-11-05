import { NextResponse } from "next/server";

const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

type Payload = {
  name: string;
  email: string;
  message: string;
};

function readPayload(body: unknown): { data?: Payload; error?: string } {
  if (!body || typeof body !== "object") return { error: "Invalid request." };
  const record = body as Record<string, unknown>;

  const name = typeof record.name === "string" ? record.name.trim() : "";
  const email = typeof record.email === "string" ? record.email.trim() : "";
  const message = typeof record.message === "string" ? record.message.trim() : "";

  if (name.length < 2) return { error: "Please enter your name." };
  if (!emailPattern.test(email)) return { error: "Please enter a valid email." };
  if (message.length < 1 || message.length > 5000) return { error: "Please enter a message." };
  if (name.length > 120 || email.length > 200) return { error: "Invalid request." };

  return { data: { name, email, message } };
}

export async function POST(request: Request) {
  let body: unknown;
  try {
    const text = await request.text();
    if (text.length > 20_000) {
      return NextResponse.json({ ok: false, error: "Invalid request." }, { status: 413 });
    }
    body = JSON.parse(text);
  } catch {
    return NextResponse.json({ ok: false, error: "Invalid request." }, { status: 400 });
  }

  const parsed = readPayload(body);
  if (!parsed.data) {
    return NextResponse.json({ ok: false, error: parsed.error }, { status: 400 });
  }

  // TODO: deliver `parsed.data` through an email provider.
  void parsed.data;

  return NextResponse.json({ ok: true });
}
