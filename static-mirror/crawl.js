import axios from "axios";
import * as cheerio from "cheerio";
import crypto from "crypto";
import fs from "fs-extra";
import path from "path";
import { fileURLToPath } from "url";

const args = process.argv.slice(2).filter((arg) => !arg.startsWith("--"));
const rewriteOnly = process.argv.includes("--rewrite");
const START_URL = args[0] || "https://tanshcreative.com/mellow-wp/";
const OUT_DIR = path.resolve(args[1] || path.join(path.dirname(fileURLToPath(import.meta.url)), "dist"));
const DELAY_MS = 400;
const MAX_PAGES = 200;
const MAX_ASSETS = 4000;

const start = new URL(START_URL);
const ORIGIN = start.origin;
const HOST = start.host;
const BASE = start.pathname.replace(/\/+$/, "") || "";

const ASSET_EXT = new Set([
  "css", "js", "mjs", "map", "json", "xml", "txt",
  "png", "jpg", "jpeg", "gif", "webp", "svg", "ico", "avif",
  "woff", "woff2", "ttf", "otf", "eot",
  "mp4", "webm", "mp3", "pdf",
]);

const TEXT_EXT = new Set(["html", "css", "js", "mjs", "svg", "json", "xml", "txt", "map"]);

const pageQueue = [];
const assetQueue = [];
const seenPages = new Set();
const seenAssets = new Set();
const externalRewrites = [];
const failures = [];

function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

function shortHash(value) {
  return crypto.createHash("sha1").update(value).digest("hex").slice(0, 10);
}

function safeDecode(value) {
  try {
    return decodeURIComponent(value);
  } catch {
    return value;
  }
}

function extname(pathname) {
  return path.posix.extname(pathname).toLowerCase().replace(".", "");
}

function isSkippablePage(pathname) {
  const p = pathname.toLowerCase();
  return (
    p.includes("/wp-admin") ||
    p.includes("/wp-login") ||
    p.includes("/wp-json") ||
    p.includes("/xmlrpc.php") ||
    p.includes("/wp-cron") ||
    p.endsWith("/feed") ||
    p.includes("/feed/") ||
    p.endsWith("/comments/feed")
  );
}

function resolveUrl(href, base) {
  if (!href) return null;
  const value = href.trim();
  if (
    !value ||
    value.startsWith("data:") ||
    value.startsWith("mailto:") ||
    value.startsWith("tel:") ||
    value.startsWith("javascript:") ||
    value.startsWith("#")
  ) {
    return null;
  }
  try {
    const url = new URL(value, base);
    if (url.protocol !== "http:" && url.protocol !== "https:") return null;
    url.hash = "";
    return url;
  } catch {
    return null;
  }
}

function isInsideSite(url) {
  return url.host === HOST && (url.pathname === BASE || url.pathname.startsWith(`${BASE}/`));
}

function pageKey(url) {
  const pathname = url.pathname.replace(/\/+$/, "") || "/";
  return `${url.origin}${pathname}`;
}

function enqueuePage(href, base) {
  const url = resolveUrl(href, base);
  if (!url || !isInsideSite(url) || isSkippablePage(url.pathname)) return;
  if (ASSET_EXT.has(extname(url.pathname))) {
    enqueueAsset(url.toString(), "file");
    return;
  }
  const key = pageKey(url);
  if (seenPages.has(key) || seenPages.size >= MAX_PAGES) return;
  seenPages.add(key);
  pageQueue.push(url.toString().replace(/\/+$/, "") === `${ORIGIN}${BASE}` ? `${ORIGIN}${BASE}/` : url.toString());
}

function enqueueAsset(href, kind) {
  const url = typeof href === "string" ? resolveUrl(href, START_URL) : href;
  if (!url) return;
  const ext = extname(url.pathname);
  const known = ASSET_EXT.has(ext) || kind === "style" || kind === "script" || kind === "font";
  if (!known) return;
  if (!isInsideSite(url) && !known) return;
  const id = url.toString();
  if (seenAssets.has(id) || seenAssets.size >= MAX_ASSETS) return;
  seenAssets.add(id);
  assetQueue.push({ url: id, kind });
}

function splitSrcset(value) {
  return value
    .split(",")
    .map((part) => part.trim().split(/\s+/)[0])
    .filter((item) => item && !item.startsWith("data:"));
}

function toLocalPath(assetUrl, kind) {
  const url = new URL(assetUrl);
  const pathname = safeDecode(url.pathname);
  const ext = path.posix.extname(pathname).toLowerCase();
  const sameSite = isInsideSite(url);
  let rel = sameSite
    ? pathname.slice(BASE.length).replace(/^\/+/, "")
    : path.posix.join("_external", url.hostname, pathname.replace(/^\/+/, ""));

  const cacheBustedFile = sameSite && ASSET_EXT.has(ext.replace(".", ""));
  if (cacheBustedFile) return rel;

  if (url.search) {
    const hash = shortHash(url.search);
    if (ext) return `${rel.slice(0, -ext.length)}.${hash}${ext}`;
    const suffix = kind === "style" ? ".css" : kind === "script" ? ".js" : "";
    return `${rel.replace(/\/+$/, "")}/${hash}${suffix}`;
  }
  if (!ext && kind === "style") return `${rel}.css`;
  return rel;
}

function rememberRewrite(assetUrl, localPath) {
  const url = new URL(assetUrl);
  if (isInsideSite(url) && ASSET_EXT.has(extname(url.pathname))) return;
  const target = `/${localPath.replace(/^\/+/, "")}`;
  externalRewrites.push([url.toString(), target]);
  externalRewrites.push([`//${url.host}${url.pathname}${url.search}`, target]);
}

async function request(target) {
  let attempt = 0;
  while (true) {
    await sleep(attempt === 0 ? DELAY_MS : DELAY_MS + attempt * 1200);
    try {
      const response = await axios.get(target, {
        responseType: "arraybuffer",
        timeout: 45000,
        maxRedirects: 5,
        headers: {
          "User-Agent":
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
          Accept: "*/*",
        },
        validateStatus: () => true,
      });
      if ([429, 502, 503, 504].includes(response.status) && attempt < 4) {
        attempt += 1;
        console.warn(`  retry ${response.status} ${target}`);
        continue;
      }
      return response;
    } catch (error) {
      if (attempt < 4) {
        attempt += 1;
        console.warn(`  retry network ${target}`);
        continue;
      }
      throw error;
    }
  }
}

function pageFile(pageUrl) {
  const url = new URL(pageUrl);
  let pathname = safeDecode(url.pathname);
  if (pathname.startsWith(BASE)) pathname = pathname.slice(BASE.length);
  pathname = pathname.replace(/^\/+/, "").replace(/\/+$/, "");
  if (!pathname) return "index.html";
  return path.join(pathname, "index.html");
}

function collectFromHtml(html, pageUrl) {
  const $ = cheerio.load(html);

  $("a[href]").each((_, el) => enqueuePage($(el).attr("href"), pageUrl));

  const assetAttrs = [
    ["img[src], video[src], audio[src], source[src], embed[src]", "src", "file"],
    ["img[data-src], img[data-lazy-src], source[data-src]", "data-src", "file"],
    ["img[data-lazy-src]", "data-lazy-src", "file"],
    ["video[poster]", "poster", "file"],
    ["script[src]", "src", "script"],
    ["link[rel='stylesheet']", "href", "style"],
    ["link[rel='icon'], link[rel='apple-touch-icon'], link[rel='shortcut icon']", "href", "file"],
    ["meta[property='og:image'], meta[name='twitter:image']", "content", "file"],
  ];

  for (const [selector, attr, kind] of assetAttrs) {
    $(selector).each((_, el) => enqueueAsset($(el).attr(attr), kind));
  }

  $("[srcset], [data-srcset]").each((_, el) => {
    for (const attr of ["srcset", "data-srcset"]) {
      const value = $(el).attr(attr);
      if (!value) continue;
      for (const item of splitSrcset(value)) enqueueAsset(item, "file");
    }
  });

  $("link[rel='preload'], link[rel='prefetch']").each((_, el) => {
    const as = ($(el).attr("as") || "").toLowerCase();
    const href = $(el).attr("href");
    const kind = as === "style" ? "style" : as === "script" ? "script" : as === "font" ? "font" : "file";
    if (["style", "script", "font", "image", "video", "audio"].includes(as)) enqueueAsset(href, kind);
    const imagesrcset = $(el).attr("imagesrcset");
    if (imagesrcset) {
      for (const item of splitSrcset(imagesrcset)) enqueueAsset(item, "file");
    }
  });

  $("[style]").each((_, el) => collectCssRefs($(el).attr("style") || "", pageUrl));
  $("style").each((_, el) => collectCssRefs($(el).text() || "", pageUrl));
  collectTextRefs(html, pageUrl);
}

function collectCssRefs(css, baseUrl) {
  const urlRe = /url\(\s*(['"]?)([^'")]+)\1\s*\)/gi;
  const importRe = /@import\s+(?:url\(\s*)?['"]([^'"]+)['"]/gi;
  let match;
  while ((match = urlRe.exec(css))) {
    const raw = match[2].trim();
    if (raw.startsWith("data:")) continue;
    enqueueAsset(resolveUrl(raw, baseUrl)?.toString(), "file");
  }
  while ((match = importRe.exec(css))) {
    enqueueAsset(resolveUrl(match[1], baseUrl)?.toString(), "style");
  }
}

function collectTextRefs(text, baseUrl) {
  const patterns = [
    /https?:\/\/tanshcreative\.com\/mellow-wp\/[^"'\\\s>]+\.(?:css|js|mjs|png|jpe?g|gif|webp|svg|ico|avif|woff2?|ttf|otf|eot|mp4|webm)(?:\?[^"'\\\s>]*)?/gi,
    /https?:\\\/\\\/tanshcreative\.com\\\/mellow-wp\\\/[^"'\\\s>]+\.(?:css|js|mjs|png|jpe?g|gif|webp|svg|ico|avif|woff2?|ttf|otf|eot|mp4|webm)(?:\?[^"'\\\s>]*)?/gi,
  ];
  for (const pattern of patterns) {
    const found = text.match(pattern) || [];
    for (const item of found) {
      const normalized = item.replace(/\\\//g, "/");
      const url = resolveUrl(normalized, baseUrl);
      if (!url) continue;
      const ext = extname(url.pathname);
      enqueueAsset(url.toString(), ext === "css" ? "style" : ext === "js" || ext === "mjs" ? "script" : "file");
    }
  }
}

async function savePage(pageUrl) {
  console.log(`page  ${pageUrl}`);
  const response = await request(pageUrl);
  if (response.status < 200 || response.status >= 300) {
    failures.push(`${response.status} ${pageUrl}`);
    return;
  }
  const type = String(response.headers["content-type"] || "");
  const body = Buffer.from(response.data);
  if (!type.includes("text/html")) {
    enqueueAsset(pageUrl, "file");
    return;
  }
  const html = body.toString("utf8");
  collectFromHtml(html, pageUrl);
  await fs.outputFile(path.join(OUT_DIR, pageFile(pageUrl)), body);
}

async function saveAsset(entry) {
  const localPath = toLocalPath(entry.url, entry.kind);
  const destination = path.join(OUT_DIR, localPath);
  if (await fs.pathExists(destination)) {
    rememberRewrite(entry.url, localPath);
    return;
  }
  console.log(`asset ${entry.url}`);
  let response;
  try {
    response = await request(entry.url);
  } catch (error) {
    failures.push(`network ${entry.url} ${error.message}`);
    return;
  }
  if (response.status < 200 || response.status >= 300) {
    failures.push(`${response.status} ${entry.url}`);
    return;
  }
  const body = Buffer.from(response.data);
  await fs.outputFile(destination, body);
  rememberRewrite(entry.url, localPath);

  const type = String(response.headers["content-type"] || "");
  const looksLikeCss = entry.kind === "style" || type.includes("text/css") || destination.endsWith(".css");
  const looksLikeJs = entry.kind === "script" || destination.endsWith(".js");
  if (looksLikeCss || looksLikeJs) {
    const text = body.toString("utf8");
    if (looksLikeCss) collectCssRefs(text, entry.url);
    collectTextRefs(text, entry.url);
  }
}

function rewriteText(text) {
  const pairs = [
    ["https://tanshcreative.com/mellow-wp/", "/"],
    ["http://tanshcreative.com/mellow-wp/", "/"],
    ["https://tanshcreative.com/mellow-wp", "/"],
    ["http://tanshcreative.com/mellow-wp", "/"],
    ["//tanshcreative.com/mellow-wp/", "/"],
    ["https:\\/\\/tanshcreative.com\\/mellow-wp\\/", "\\/"],
    ["http:\\/\\/tanshcreative.com\\/mellow-wp\\/", "\\/"],
    ["https:\\/\\/tanshcreative.com\\/mellow-wp", "\\/"],
    ["http:\\/\\/tanshcreative.com\\/mellow-wp", "\\/"],
    ["https%3A%2F%2Ftanshcreative.com%2Fmellow-wp%2F", "%2F"],
    ["http%3A%2F%2Ftanshcreative.com%2Fmellow-wp%2F", "%2F"],
    ["https%3a%2f%2ftanshcreative.com%2fmellow-wp%2f", "%2f"],
    ["http%3a%2f%2ftanshcreative.com%2fmellow-wp%2f", "%2f"],
    ["https%3A%2F%2Ftanshcreative.com%2Fmellow-wp", "%2F"],
    ["http%3A%2F%2Ftanshcreative.com%2Fmellow-wp", "%2F"],
  ];
  let out = text;
  for (const [from, to] of pairs) out = out.split(from).join(to);

  const extras = [...externalRewrites].sort((a, b) => b[0].length - a[0].length);
  for (const [from, to] of extras) {
    out = out.split(from).join(to);
    out = out.split(from.replace(/&/g, "&amp;")).join(to);
    out = out.split(from.replace(/&/g, "&#038;")).join(to);
  }
  return out;
}

async function postProcess() {
  const files = [];
  const walk = async (dir) => {
    const entries = await fs.readdir(dir, { withFileTypes: true });
    for (const entry of entries) {
      const full = path.join(dir, entry.name);
      if (entry.isDirectory()) await walk(full);
      else files.push(full);
    }
  };
  await walk(OUT_DIR);

  let changed = 0;
  for (const file of files) {
    const ext = path.extname(file).toLowerCase().replace(".", "");
    if (!TEXT_EXT.has(ext)) continue;
    const original = await fs.readFile(file, "utf8");
    const next = rewriteText(original);
    if (next !== original) {
      await fs.writeFile(file, next);
      changed += 1;
    }
  }
  return changed;
}

async function main() {
  if (rewriteOnly) {
    const rewritten = await postProcess();
    console.log(`Rewritten files: ${rewritten}`);
    return;
  }

  await fs.emptyDir(OUT_DIR);
  enqueuePage(START_URL, START_URL);
  console.log(`Mirroring ${START_URL}`);
  console.log(`Output ${OUT_DIR}`);

  while (pageQueue.length || assetQueue.length) {
    if (pageQueue.length) {
      const pageUrl = pageQueue.shift();
      try {
        await savePage(pageUrl);
      } catch (error) {
        failures.push(`page ${pageUrl} ${error.message}`);
      }
      continue;
    }
    const asset = assetQueue.shift();
    try {
      await saveAsset(asset);
    } catch (error) {
      failures.push(`asset ${asset.url} ${error.message}`);
    }
  }

  const rewritten = await postProcess();
  console.log(`\nPages: ${seenPages.size}`);
  console.log(`Assets: ${seenAssets.size}`);
  console.log(`Rewritten files: ${rewritten}`);
  if (failures.length) {
    console.log(`Failures: ${failures.length}`);
    for (const failure of failures) console.log(`  ${failure}`);
  }
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
