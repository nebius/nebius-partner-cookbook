#!/usr/bin/env bun
import { readFile, writeFile } from "node:fs/promises";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { compile } from "json-schema-to-typescript";

const here = dirname(fileURLToPath(import.meta.url));
const schemaPath = resolve(here, "..", "..", "..", "schemas", "recipe.schema.json");
const outPath = resolve(here, "..", "src", "types.ts");

const schema = JSON.parse(await readFile(schemaPath, "utf8"));
const ts = await compile(schema, "Recipe", { bannerComment: "// Auto-generated. Run `bun run generate`." });
await writeFile(outPath, ts, "utf8");
console.log(`Wrote ${outPath}`);
