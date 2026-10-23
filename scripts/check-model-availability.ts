#!/usr/bin/env bun

import { join, resolve } from "node:path";
import { loadRecipes } from "./lib/recipes";
import { normalizeBaseUrl } from "./lib/nebius-url";

interface ModelsResponse {
  data?: Array<{ id?: string }>;
}

const repoRoot = resolve(import.meta.dir, "..");
const cookbooksDir = join(repoRoot, "cookbooks");
const baseUrl = normalizeBaseUrl(process.env.NEBIUS_BASE_URL);
const apiKey = process.env.NEBIUS_API_KEY?.trim();

if (!apiKey) {
  console.error("NEBIUS_API_KEY is required to check live model availability.");
  process.exit(2);
}

const recipes = await loadRecipes(cookbooksDir);
const references = new Map<string, string[]>();

for (const { dir, recipe } of recipes) {
  for (const model of recipe.models) {
    const usages = references.get(model.id) ?? [];
    usages.push(`${dir} (${model.role})`);
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
