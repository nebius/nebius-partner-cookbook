#!/usr/bin/env bun
import { mkdir, readFile, writeFile } from "node:fs/promises";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { compileCookbookReadme } from "@nebius-cookbook/mdx-pipeline";
import { loadBlueprints } from "./lib/blueprints.ts";

const here = dirname(fileURLToPath(import.meta.url));
const repoRoot = resolve(here, "..");
const blueprintsDir = join(repoRoot, "blueprints");
const contentDir = join(repoRoot, "app", "src", "content");
const blueprintsContentDir = join(contentDir, "blueprints");

function cleanRepoUrl(value: string | undefined): string {
  return (value ?? "https://github.com/nebius/nebius-partner-cookbook").trim().replace(/[./]+$/, "");
}

const REPO_URL = cleanRepoUrl(process.env.GITHUB_REPO_URL);

await mkdir(blueprintsContentDir, { recursive: true });

const blueprints = await loadBlueprints(blueprintsDir);

const slugByDir = Object.fromEntries(
  blueprints.map(({ dir, blueprint }) => [dir, blueprint.slug]),
);

const manifest: Array<Record<string, unknown>> = [];

for (const { dir, blueprint } of blueprints) {
  const readmePath = join(blueprintsDir, dir, "README.md");
  let body = "";
  try {
    body = await readFile(readmePath, "utf8");
  } catch (err) {
    if ((err as NodeJS.ErrnoException).code !== "ENOENT") throw err;
    console.warn(`No README for ${dir}, emitting frontmatter-only MDX.`);
  }

  const compiled = compileCookbookReadme(body, {
    slug: blueprint.slug,
    cookbookDir: dir,
    repoUrl: REPO_URL,
    cookbookSlugByDir: slugByDir,
    baseDir: "blueprints",
    siblingRoute: "blueprints",
    frontmatter: {
      slug: blueprint.slug,
      title: blueprint.title,
      tagline: blueprint.tagline,
      publishedAt: blueprint.publishedAt,
      updatedAt: blueprint.updatedAt,
    },
  });

  const mdxPath = join(blueprintsContentDir, `${blueprint.slug}.mdx`);
  await writeFile(mdxPath, compiled, "utf8");

  manifest.push({
    slug: blueprint.slug,
    eyebrow: blueprint.eyebrow,
    title: blueprint.title,
    upcoming: blueprint.upcoming ?? false,
    tagline: blueprint.tagline,
    summary: blueprint.summary,
    difficulty: blueprint.difficulty,
    estimatedRunTime: blueprint.estimatedRunTime,
    stack: blueprint.stack,
    tags: blueprint.tags,
    models: blueprint.models,
    integrations: blueprint.integrations,
    capabilities: blueprint.capabilities ?? {},
    dataset: blueprint.dataset ?? null,
    publishedAt: blueprint.publishedAt,
    updatedAt: blueprint.updatedAt,
    dir,
  });
}

const manifestPath = join(contentDir, "blueprints-manifest.json");
await writeFile(manifestPath, JSON.stringify(manifest, null, 2) + "\n", "utf8");

console.log(
  `Built ${manifest.length} blueprint${manifest.length === 1 ? "" : "s"} into ${contentDir}`,
);
