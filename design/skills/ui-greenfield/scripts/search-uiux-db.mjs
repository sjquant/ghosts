#!/usr/bin/env node
import { readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const root = dirname(here);
const query = process.argv.slice(2).join(" ").toLowerCase().trim();

if (!query) {
  console.error("Usage: node scripts/search-uiux-db.mjs <query>");
  process.exit(2);
}

const files = [
  "references/ui-ux-db/palettes.csv",
  "references/ui-ux-db/font-pairings.csv",
  "references/ui-ux-db/ux-guidelines.csv",
];

function parseCsv(text) {
  const lines = text.trim().split(/\r?\n/);
  const headers = lines.shift().split(",");
  return lines.map((line) => {
    const cells = line.split(",");
    return Object.fromEntries(headers.map((header, i) => [header, cells[i] ?? ""]));
  });
}

const terms = query.split(/\s+/).filter(Boolean);
const results = [];

for (const file of files) {
  const rows = parseCsv(readFileSync(join(root, file), "utf8"));
  for (const row of rows) {
    const haystack = Object.values(row).join(" ").toLowerCase();
    const score = terms.reduce((sum, term) => sum + (haystack.includes(term) ? 1 : 0), 0);
    if (score > 0) results.push({ file, score, row });
  }
}

results.sort((a, b) => b.score - a.score || a.file.localeCompare(b.file));
console.log(JSON.stringify(results.slice(0, 20), null, 2));
