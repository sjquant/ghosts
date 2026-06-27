#!/usr/bin/env node
import { mkdirSync } from "node:fs";
import { dirname } from "node:path";

const [url, output = "./capture.png", width = "1280", height = "900"] = process.argv.slice(2);

if (!url) {
  console.error("Usage: node scripts/capture-browser.mjs <url> [output.png] [width] [height]");
  process.exit(2);
}

let chromium;
try {
  ({ chromium } = await import("playwright"));
} catch {
  console.error("Missing dependency: playwright. Install with: bun add -d playwright && bunx playwright install chromium");
  process.exit(2);
}

mkdirSync(dirname(output), { recursive: true });
const browser = await chromium.launch();
try {
  const page = await browser.newPage({ viewport: { width: Number(width), height: Number(height) } });
  await page.goto(url, { waitUntil: "networkidle" });
  await page.screenshot({ path: output, fullPage: true });
  console.log(JSON.stringify({ url, output, width: Number(width), height: Number(height) }, null, 2));
} finally {
  await browser.close();
}
