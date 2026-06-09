#!/usr/bin/env bun
import { cp, readdir, readFile, writeFile } from "node:fs/promises";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const repoRoot = resolve(here, "..");
const cookbooksDir = join(repoRoot, "cookbooks");
const templateDir = join(cookbooksDir, "_template");

function prompt(label: string): Promise<string> {
  process.stdout.write(`${label}: `);
  return new Promise((resolveP) => {
    process.stdin.once("data", (data) => resolveP(data.toString().trim()));
  });
}

function slugify(s: string): string {
  return s
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "");
}

const title = await prompt("Title (e.g. 'Streaming RAG with Pinecone Nexus')");
if (!title) {
  console.error("Title is required.");
  process.exit(1);
}

const eyebrow = await prompt("Eyebrow / arc label (e.g. 'Foundation')");
if (!eyebrow) {
  console.error("Eyebrow is required.");
  process.exit(1);
}

const suggestedSlug = slugify(title);
const slugAnswer = await prompt(`Slug [${suggestedSlug}]`);
const slug = slugify(slugAnswer || suggestedSlug);

const difficulty = (await prompt("Difficulty (beginner|intermediate|advanced) [beginner]")) || "beginner";

const existing = await readdir(cookbooksDir, { withFileTypes: true });
const orders = existing
  .filter((e) => e.isDirectory() && /^\d{2}-/.test(e.name))
  .map((e) => parseInt(e.name.slice(0, 2), 10))
  .filter((n) => !Number.isNaN(n));
const nextOrder = (orders.length === 0 ? 0 : Math.max(...orders)) + 1;
const orderPrefix = String(nextOrder).padStart(2, "0");
const target = join(cookbooksDir, `${orderPrefix}-${slug}`);

console.log(`\nCreating ${target}...`);
await cp(templateDir, target, { recursive: true });

const recipePath = join(target, "recipe.json");
const recipeRaw = await readFile(recipePath, "utf8");
const recipe = JSON.parse(recipeRaw);
recipe.slug = slug;
recipe.order = nextOrder;
recipe.eyebrow = eyebrow;
recipe.title = title;
recipe.difficulty = difficulty;
recipe.publishedAt = new Date().toISOString().slice(0, 10);
recipe.updatedAt = recipe.publishedAt;
await writeFile(recipePath, JSON.stringify(recipe, null, 2) + "\n", "utf8");

console.log(`\nBootstrapped ${target}`);
console.log("\nNext steps:");
console.log(`  1. Edit ${target}/recipe.json`);
console.log("  2. Run `bun run validate` to confirm metadata");
console.log("  3. Run `bun run build:readme` to refresh the root README");
console.log(`  4. cd ${target} && uv sync && make dev`);

process.exit(0);
