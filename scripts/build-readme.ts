#!/usr/bin/env bun
import { readFile, writeFile } from "node:fs/promises";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { generate as generateRecipesTable } from "./generators/recipes-table.ts";
import { generate as generateBlueprintsTable } from "./generators/blueprints-table.ts";

interface Section {
  id: string;
  source: "human" | "generated";
  file?: string;
  generator?: string;
  options?: Record<string, unknown>;
}

interface Config {
  output: string;
  separator?: string;
  header?: { comment?: string };
  sections: Section[];
}

const here = dirname(fileURLToPath(import.meta.url));
const configPath = resolve(here, "..", "README", "_config.json");

const config = JSON.parse(await readFile(configPath, "utf8")) as Config;
const configDir = dirname(configPath);
const separator = config.separator ?? "\n\n";

const parts: string[] = [];

if (config.header?.comment) {
  parts.push(`<!-- ${config.header.comment} -->`);
}

for (const section of config.sections) {
  if (section.source === "human") {
    if (!section.file) throw new Error(`Section ${section.id} missing 'file'`);
    const filePath = resolve(configDir, section.file);
    const body = (await readFile(filePath, "utf8")).trimEnd();
    parts.push(body);
  } else if (section.source === "generated") {
    if (section.generator === "recipes-table") {
      const body = (await generateRecipesTable(
        (section.options ?? {}) as Parameters<typeof generateRecipesTable>[0],
        configDir,
      )).trimEnd();
      parts.push(body);
    } else if (section.generator === "blueprints-table") {
      const body = (await generateBlueprintsTable(
        (section.options ?? {}) as Parameters<typeof generateBlueprintsTable>[0],
        configDir,
      )).trimEnd();
      parts.push(body);
    } else {
      throw new Error(`Unknown generator: ${section.generator}`);
    }
  }
}

const composed = parts.join(separator) + "\n";
const outputPath = resolve(configDir, config.output);

const checkMode = process.argv.includes("--check");

if (checkMode) {
  let existing = "";
  try {
    existing = await readFile(outputPath, "utf8");
  } catch (err) {
    if ((err as NodeJS.ErrnoException).code !== "ENOENT") throw err;
  }
  if (existing !== composed) {
    console.error("README.md is out of sync. Run `bun run build:readme`.");
    process.exit(1);
  }
  console.log("README.md is in sync.");
} else {
  await writeFile(outputPath, composed, "utf8");
  console.log(`Wrote ${outputPath}`);
}
