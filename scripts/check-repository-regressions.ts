#!/usr/bin/env bun

import { readdir, readFile } from "node:fs/promises";
import { extname, join, relative, resolve } from "node:path";

const repoRoot = resolve(import.meta.dir, "..");
const ignoredDirectories = new Set([".git", ".next", ".venv", "node_modules"]);
const checkedExtensions = new Set([
  "",
  ".example",
  ".json",
  ".md",
  ".py",
  ".ts",
  ".tsx",
  ".yml",
  ".yaml",
]);
const forbidden = [
  { pattern: "api.studio.nebius.ai", reason: "pre-rebrand Token Factory host" },
  { pattern: "cd cookbook/cookbooks", reason: "incorrect clone directory" },
  { pattern: "cd nebius-cookbook/cookbooks", reason: "incorrect clone directory" },
  { pattern: "DeepSeek-R1-0528", reason: "retired quickstart model" },
  { pattern: "NEBIUS_API_KEY=NEBIUS_API_KEY=", reason: "duplicated env assignment" },
] as const;

const failures: string[] = [];

async function walk(directory: string): Promise<void> {
  for (const entry of await readdir(directory, { withFileTypes: true })) {
    if (entry.isDirectory() && ignoredDirectories.has(entry.name)) {
      continue;
    }

    const path = join(directory, entry.name);
    if (entry.name === "check-repository-regressions.ts") {
      continue;
    }
    if (entry.isDirectory()) {
      await walk(path);
      continue;
    }
    if (!entry.isFile() || !checkedExtensions.has(extname(entry.name))) {
      continue;
    }

    const content = await readFile(path, "utf8");
    for (const item of forbidden) {
      if (content.includes(item.pattern)) {
        failures.push(`${relative(repoRoot, path)}: ${item.reason}`);
      }
    }
  }
}

await walk(repoRoot);

if (failures.length > 0) {
  console.error("Repository regression check failed:");
  for (const failure of failures.sort()) {
    console.error(`- ${failure}`);
  }
  process.exit(1);
}

console.log("Repository regression checks passed.");
