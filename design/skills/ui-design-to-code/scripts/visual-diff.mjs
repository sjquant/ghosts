#!/usr/bin/env node
const [reference, actual] = process.argv.slice(2);

if (!reference || !actual) {
  console.error("Usage: node scripts/visual-diff.mjs <reference.png> <actual.png>");
  process.exit(2);
}

let PNG;
let pixelmatch;
try {
  ({ PNG } = await import("pngjs"));
  ({ default: pixelmatch } = await import("pixelmatch"));
} catch {
  console.error("Missing dependencies. Install with: bun add -d pngjs pixelmatch");
  process.exit(2);
}

const { readFileSync } = await import("node:fs");
const ref = PNG.sync.read(readFileSync(reference));
const act = PNG.sync.read(readFileSync(actual));

const dimensionsMatch = ref.width === act.width && ref.height === act.height;
if (!dimensionsMatch) {
  console.log(JSON.stringify({
    dimensionsMatch,
    reference: { width: ref.width, height: ref.height },
    actual: { width: act.width, height: act.height },
    diffPixels: null,
    diffRatio: null,
    similarityScore: null,
  }, null, 2));
  process.exit(1);
}

const diff = new PNG({ width: ref.width, height: ref.height });
const diffPixels = pixelmatch(ref.data, act.data, diff.data, ref.width, ref.height, { threshold: 0.1 });
const total = ref.width * ref.height;
const diffRatio = diffPixels / total;
const similarityScore = Math.max(0, 100 * (1 - diffRatio));

console.log(JSON.stringify({
  dimensionsMatch,
  reference: { width: ref.width, height: ref.height },
  actual: { width: act.width, height: act.height },
  diffPixels,
  diffRatio,
  similarityScore,
}, null, 2));

process.exit(diffRatio > 0.02 ? 1 : 0);
