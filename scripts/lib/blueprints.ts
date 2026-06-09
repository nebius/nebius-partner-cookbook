import { readdir, readFile } from "node:fs/promises";
import { join } from "node:path";

export interface Blueprint {
  $schema?: string;
  slug: string;
  eyebrow: string;
  title: string;
  upcoming?: boolean;
  tagline: string;
  summary: string;
  difficulty: "beginner" | "intermediate" | "advanced";
  estimatedRunTime: string;
  stack: { primary: string[]; secondary: string[] };
  tags: string[];
  models: { id: string; provider?: string; role?: string }[];
  integrations: string[];
  capabilities?: { hasUI?: boolean; hasEval?: boolean; hasDataset?: boolean };
  dataset?: { description?: string; items?: number };
  assets?: { hero?: string; demo?: string; architecture?: string };
  quickstart: { clone: string; configure: string; run: string };
  deployment: { target: string; instructions: string };
  authors: { name: string; url?: string }[];
  publishedAt: string;
  updatedAt: string;
}

export interface LoadedBlueprint {
  dir: string;
  blueprint: Blueprint;
}

export async function loadBlueprints(blueprintsDir: string): Promise<LoadedBlueprint[]> {
  let entries: { name: string; isDirectory: () => boolean }[];
  try {
    entries = await readdir(blueprintsDir, { withFileTypes: true });
  } catch (err) {
    if ((err as NodeJS.ErrnoException).code === "ENOENT") return [];
    throw err;
  }

  const blueprints: LoadedBlueprint[] = [];

  for (const entry of entries) {
    if (!entry.isDirectory()) continue;
    if (entry.name.startsWith(".")) continue;

    const blueprintPath = join(blueprintsDir, entry.name, "blueprint.json");
    try {
      const raw = await readFile(blueprintPath, "utf8");
      const blueprint = JSON.parse(raw) as Blueprint;
      blueprints.push({ dir: entry.name, blueprint });
    } catch (err) {
      if ((err as NodeJS.ErrnoException).code === "ENOENT") continue;
      throw new Error(`Failed to parse ${blueprintPath}: ${(err as Error).message}`);
    }
  }

  blueprints.sort((a, b) => a.blueprint.title.localeCompare(b.blueprint.title));
  return blueprints;
}
