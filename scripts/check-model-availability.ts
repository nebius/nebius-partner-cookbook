#!/usr/bin/env bun

import { readdir, readFile } from "node:fs/promises";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

interface RecipeModel {
  id: string;
  role: string;
}

interface RecipeMetadata {
  title: string;
  models: RecipeModel[];
}

interface ModelsResponse {
  data?: Array<{ id?: string }>;
}

const here = dirname(fileURLToPath(import.meta.url));
const repoRoot = resolve(here, "..");
const cookbooksDir = join(repoRoot, "cookbooks");
const baseUrl = (process.env.NEBIUS_BASE_URL ?? "https://api.tokenfactory.nebius.com/v1/")
  .replace(/\/+$/, "");
const apiKey = process.env.NEBIUS_API_KEY?.trim();

if (!apiKey) {
  console.error("NEBIUS_API_KEY is required to check live model availability.");
  process.exit(2);
}

const recipeEntries = await readdir(cookbooksDir, { withFileTypes: true });
const references = new Map<string, string[]>();

for (const entry of recipeEntries) {
  if (!entry.isDirectory() || entry.name.startsWith("_")) {
    continue;
  }

  const recipePath = join(cookbooksDir, entry.name, "recipe.json");
  const recipe = JSON.parse(await readFile(recipePath, "utf8")) as RecipeMetadata;
  for (const model of recipe.models) {
    const usages = references.get(model.id) ?? [];
    usages.push(`${entry.name} (${model.role})`);
    references.set(model.id, usages);
  }
}

const controller = new AbortController();
const timeout = setTimeout(() => controller.abort(), 15_000);
let response: Response;

try {
  response = await fetch(`${baseUrl}/models`, {
    headers: { authorization: `Bearer ${apiKey}` },
    signal: controller.signal,
  });
} catch (error) {
  const message = error instanceof Error ? error.message : String(error);
  console.error(`Unable to query ${baseUrl}/models: ${message}`);
  process.exit(1);
} finally {
  clearTimeout(timeout);
}

if (!response.ok) {
  console.error(`Model lookup failed with HTTP ${response.status}.`);
  process.exit(1);
}

const body = (await response.json()) as ModelsResponse;
const available = new Set(
  (body.data ?? [])
    .map((model) => model.id?.trim())
    .filter((id): id is string => Boolean(id)),
);
const missing = [...references.keys()].filter((id) => !available.has(id)).sort();

if (missing.length > 0) {
  console.error("Referenced cookbook models missing from Token Factory:");
  for (const id of missing) {
    console.error(`- ${id}: ${references.get(id)?.join(", ")}`);
  }
  process.exit(1);
}

console.log(
  `All ${references.size} cookbook model${references.size === 1 ? "" : "s"} are available.`,
);
