#!/usr/bin/env bun
import { mkdir, readFile, writeFile } from "node:fs/promises";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { compileCookbookReadme } from "@nebius-cookbook/mdx-pipeline";
import { loadRecipes } from "./lib/recipes.ts";

const here = dirname(fileURLToPath(import.meta.url));
const repoRoot = resolve(here, "..");
const cookbooksDir = join(repoRoot, "cookbooks");
const contentDir = join(repoRoot, "app", "src", "content");
const recipesContentDir = join(contentDir, "recipes");

const REPO_URL = process.env.GITHUB_REPO_URL ?? "https://github.com/nebius/nebius-partner-cookbook";

await mkdir(recipesContentDir, { recursive: true });

const recipes = await loadRecipes(cookbooksDir);

const cookbookSlugByDir = Object.fromEntries(recipes.map(({ dir, recipe }) => [dir, recipe.slug]));

const manifest: Array<Record<string, unknown>> = [];

for (const { dir, recipe } of recipes) {
  const readmePath = join(cookbooksDir, dir, "README.md");
  let body = "";
  try {
    body = await readFile(readmePath, "utf8");
  } catch (err) {
    if ((err as NodeJS.ErrnoException).code !== "ENOENT") throw err;
    console.warn(`No README for ${dir}, emitting frontmatter-only MDX.`);
  }

  const compiled = compileCookbookReadme(body, {
    slug: recipe.slug,
    cookbookDir: dir,
    repoUrl: REPO_URL,
    cookbookSlugByDir,
    frontmatter: {
      slug: recipe.slug,
      title: recipe.title,
      tagline: recipe.tagline,
      order: recipe.order,
      difficulty: recipe.difficulty,
      publishedAt: recipe.publishedAt,
      updatedAt: recipe.updatedAt,
    },
  });

  const mdxPath = join(recipesContentDir, `${recipe.slug}.mdx`);
  await writeFile(mdxPath, compiled, "utf8");

  manifest.push({
    slug: recipe.slug,
    order: recipe.order,
    eyebrow: recipe.eyebrow,
    title: recipe.title,
    upcoming: recipe.upcoming ?? false,
    tagline: recipe.tagline,
    difficulty: recipe.difficulty,
    estimatedReadingTime: recipe.estimatedReadingTime,
    estimatedRunTime: recipe.estimatedRunTime,
    stack: recipe.stack,
    tags: recipe.tags,
    models: recipe.models,
    publishedAt: recipe.publishedAt,
    updatedAt: recipe.updatedAt,
    dir,
  });
}

const manifestPath = join(contentDir, "recipes-manifest.json");
await writeFile(manifestPath, JSON.stringify(manifest, null, 2) + "\n", "utf8");

console.log(`Built ${manifest.length} recipe${manifest.length === 1 ? "" : "s"} into ${contentDir}`);
