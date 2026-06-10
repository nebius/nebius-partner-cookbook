// Parse every JSX file with the same @babel/standalone build the browser
// uses (index.html loads babel.min.js and compiles JSX at page load, so a
// syntax error only surfaces when someone opens the UI). Run via:
//   npm install --no-save @babel/standalone && node scripts/check_jsx.mjs
import { readFileSync, readdirSync } from "node:fs";
import { dirname, join, relative } from "node:path";
import { fileURLToPath } from "node:url";
import { createRequire } from "node:module";

const require = createRequire(import.meta.url);
const Babel = require("@babel/standalone");

const staticDir = join(dirname(fileURLToPath(import.meta.url)), "..", "ui", "static");
const files = readdirSync(staticDir, { recursive: true })
  .filter((f) => f.toString().endsWith(".jsx"))
  .map((f) => join(staticDir, f.toString()));

if (files.length === 0) {
  console.error("No .jsx files found — wrong directory?");
  process.exit(1);
}

let failed = false;
for (const file of files) {
  const name = relative(staticDir, file);
  try {
    Babel.transform(readFileSync(file, "utf8"), { presets: ["react"], filename: name });
    console.log(`OK   ${name}`);
  } catch (err) {
    failed = true;
    console.error(`FAIL ${name}: ${err.message.split("\n")[0]}`);
  }
}
process.exit(failed ? 1 : 0);
