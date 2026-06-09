#!/usr/bin/env bun
import { readdir, readFile } from "node:fs/promises";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import Ajv2020 from "ajv/dist/2020";
import addFormats from "ajv-formats";

const here = dirname(fileURLToPath(import.meta.url));
const repoRoot = resolve(here, "..");
const schemaPath = join(repoRoot, "schemas", "blueprint.schema.json");
const blueprintsDir = join(repoRoot, "blueprints");

const schema = JSON.parse(await readFile(schemaPath, "utf8"));
const ajv = new Ajv2020({ allErrors: true, strict: false });
addFormats(ajv);
const validate = ajv.compile(schema);

const errors: string[] = [];
let validated = 0;

let entries: { name: string; isDirectory: () => boolean }[];
try {
  entries = await readdir(blueprintsDir, { withFileTypes: true });
} catch (err) {
  if ((err as NodeJS.ErrnoException).code === "ENOENT") {
    console.log("No blueprints/ directory yet. Nothing to validate.");
    process.exit(0);
  }
  throw err;
}

for (const entry of entries) {
  if (!entry.isDirectory()) continue;
  if (entry.name.startsWith(".")) continue;

  const blueprintPath = join(blueprintsDir, entry.name, "blueprint.json");
  let blueprint: unknown;
  try {
    blueprint = JSON.parse(await readFile(blueprintPath, "utf8"));
  } catch (err) {
    if ((err as NodeJS.ErrnoException).code === "ENOENT") {
      // A directory without blueprint.json is not (yet) a catalog blueprint.
      continue;
    }
    errors.push(`${entry.name}/blueprint.json: invalid JSON — ${(err as Error).message}`);
    continue;
  }

  if (!validate(blueprint)) {
    for (const e of validate.errors ?? []) {
      errors.push(`${entry.name}/blueprint.json ${e.instancePath || "/"}: ${e.message}`);
    }
    continue;
  }

  const b = blueprint as { slug: string };
  if (b.slug !== entry.name) {
    errors.push(
      `${entry.name}/blueprint.json: slug="${b.slug}" but directory is "${entry.name}"`,
    );
  }

  validated++;
}

if (errors.length > 0) {
  console.error(`Blueprint validation failed (${errors.length} error${errors.length > 1 ? "s" : ""}):`);
  for (const e of errors) console.error(`  - ${e}`);
  process.exit(1);
}

console.log(`Validated ${validated} blueprint${validated === 1 ? "" : "s"}.`);
