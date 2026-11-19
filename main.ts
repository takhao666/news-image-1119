// news-image-20261119 entry (Node 22, standard library only).
//
// The front page is drawn at build time by render.py into entry.png
// in this directory. At grading time this program copies that exact
// file to the output path, so both runs write byte-identical output:
// no network, no randomness, no timestamps in the bytes.
//
// Run outside the grader with:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { createHash } from "node:crypto";
import { mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
const target = join(outDir, "entry.png");

const bytes = readFileSync(join(here, "entry.png"));
const digest = createHash("sha256").update(bytes).digest("hex");

// The entry must be a whole PNG: check its 8-byte signature before copying.
const PNG_MAGIC = Buffer.from([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a]);
if (!bytes.subarray(0, 8).equals(PNG_MAGIC)) {
  throw new Error("entry.png is not a PNG file");
}

mkdirSync(outDir, { recursive: true });
writeFileSync(target, bytes);

// Read back what we wrote and confirm it is the same file, byte for byte.
const written = readFileSync(target);
if (written.length !== bytes.length) {
  throw new Error(
    `entry.png copy is short: ${written.length} of ${bytes.length} bytes`,
  );
}
if (createHash("sha256").update(written).digest("hex") !== digest) {
  throw new Error("entry.png copy failed its sha256 check");
}

console.log(`wrote ${target} (${written.length} bytes, sha256 ${digest})`);
