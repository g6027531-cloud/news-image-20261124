// News-image entry: place the checked-in front page at /output/entry.png.
//
// The picture itself is rendered ahead of time (see render.py) and shipped
// in this repository. This program only moves those exact bytes into the
// output directory and proves the move with a hash comparison. It uses
// only the Node standard library, touches no network, and yields identical
// output on every run because the input bytes never change.

import { createHash as hash } from "node:crypto";
import { mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { join } from "node:path";

const IMAGE = new URL("./assets/entry.png", import.meta.url);
const LIMIT = 1024 * 1024;

const bytes = readFileSync(IMAGE);
if (bytes.length > LIMIT) {
  throw new Error(
    `checked-in entry.png is ${bytes.length} bytes, over the ${LIMIT} byte limit`,
  );
}

const digest = hash("sha256").update(bytes).digest("hex");
const targetDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
const target = join(targetDir, "entry.png");

mkdirSync(targetDir, { recursive: true });
writeFileSync(target, bytes);

const back = readFileSync(target);
if (!back.equals(bytes)) {
  throw new Error("output bytes differ from the checked-in image");
}
if (hash("sha256").update(back).digest("hex") !== digest) {
  throw new Error("output hash differs from the checked-in image");
}

console.log(
  `entry.png written to ${target}: ${bytes.length} bytes, sha256 ${digest}`,
);
