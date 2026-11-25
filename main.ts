import { createHash } from "node:crypto";
import { copyFileSync, mkdirSync, readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

// Copy the checked-in front-page image to the output path, then verify
// the copy byte for byte. No network access. Deterministic.
const here = dirname(fileURLToPath(import.meta.url));
const source = join(here, "assets", "entry.png");
const outputDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
const destination = join(outputDir, "entry.png");

// The gate allows at most 1 MiB and at most 1024x1024 pixels; the
// checked-in image is verified against the size cap here, and its
// dimensions were verified when it was rendered (see render.py).
const data = readFileSync(source);
if (data.length > 1048576) {
  throw new Error(`entry.png is ${data.length} bytes, over the 1 MiB limit`);
}
const sha256 = createHash("sha256").update(data).digest("hex");

mkdirSync(outputDir, { recursive: true });
copyFileSync(source, destination);

const written = readFileSync(destination);
if (written.length !== data.length) {
  throw new Error(
    `post-copy length mismatch: source ${data.length} bytes, output ${written.length} bytes`,
  );
}
const writtenSha256 = createHash("sha256").update(written).digest("hex");
if (writtenSha256 !== sha256) {
  throw new Error(
    `post-copy sha256 mismatch: source ${sha256}, output ${writtenSha256}`,
  );
}

console.log(`wrote ${destination} (${written.length} bytes, sha256 ${sha256})`);
