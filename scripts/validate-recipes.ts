#!/usr/bin/env bun
import { readdir, readFile } from "node:fs/promises";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import Ajv2020 from "ajv/dist/2020";
import addFormats from "ajv-formats";

const here = dirname(fileURLToPath(import.meta.url));
const repoRoot = resolve(here, "..");
const schemaPath = join(repoRoot, "schemas", "recipe.schema.json");
const cookbooksDir = join(repoRoot, "cookbooks");

const schema = JSON.parse(await readFile(schemaPath, "utf8"));
const ajv = new Ajv2020({ allErrors: true, strict: false });
addFormats(ajv);
const validate = ajv.compile(schema);

const errors: string[] = [];
let validated = 0;

let entries: { name: string; isDirectory: () => boolean }[];
try {
  entries = await readdir(cookbooksDir, { withFileTypes: true });
} catch (err) {
  if ((err as NodeJS.ErrnoException).code === "ENOENT") {
    console.log("No cookbooks/ directory yet. Nothing to validate.");
    process.exit(0);
  }
  throw err;
}

for (const entry of entries) {
  if (!entry.isDirectory()) continue;
  if (entry.name === "_template" || entry.name.startsWith(".")) continue;

  const recipePath = join(cookbooksDir, entry.name, "recipe.json");
  let recipe: unknown;
  try {
    recipe = JSON.parse(await readFile(recipePath, "utf8"));
  } catch (err) {
    if ((err as NodeJS.ErrnoException).code === "ENOENT") {
      errors.push(`${entry.name}/: missing recipe.json`);
      continue;
    }
    errors.push(`${entry.name}/recipe.json: invalid JSON — ${(err as Error).message}`);
    continue;
  }

  if (!validate(recipe)) {
    for (const e of validate.errors ?? []) {
      errors.push(`${entry.name}/recipe.json ${e.instancePath || "/"}: ${e.message}`);
    }
    continue;
  }

  const r = recipe as { slug: string; order: number };
  const expectedPrefix = String(r.order).padStart(2, "0") + "-";
  if (!entry.name.startsWith(expectedPrefix)) {
    errors.push(
      `${entry.name}/recipe.json: order=${r.order} but directory does not start with "${expectedPrefix}"`,
    );
  }
  const expectedSlug = entry.name.slice(expectedPrefix.length);
  if (r.slug !== expectedSlug) {
    errors.push(
      `${entry.name}/recipe.json: slug="${r.slug}" but directory implies "${expectedSlug}"`,
    );
  }

  validated++;
}

if (errors.length > 0) {
  console.error(`Validation failed (${errors.length} error${errors.length > 1 ? "s" : ""}):`);
  for (const e of errors) console.error(`  - ${e}`);
  process.exit(1);
}

console.log(`Validated ${validated} recipe${validated === 1 ? "" : "s"}.`);
