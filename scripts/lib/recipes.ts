import { readdir, readFile } from "node:fs/promises";
import { join } from "node:path";

export interface Recipe {
  $schema?: string;
  slug: string;
  order: number;
  eyebrow: string;
  title: string;
  upcoming?: boolean;
  tagline: string;
  difficulty: "beginner" | "intermediate" | "advanced";
  estimatedReadingTime: string;
  estimatedRunTime: string;
  stack: { primary: string[]; secondary: string[] };
  tags: string[];
  story: { problem: string; solution: string; outcome: string };
  prerequisites: string[];
  models: { id: string; role: string }[];
  assets?: { hero?: string; demo?: string; architecture?: string };
  quickstart: { clone: string; configure: string; run: string };
  endpoints: { method: string; path: string; streaming?: boolean; description: string }[];
  deployment: { target: string; instructions: string };
  nextRecipe?: string;
  authors: { name: string; url?: string }[];
  publishedAt: string;
  updatedAt: string;
}

export interface LoadedRecipe {
  dir: string;
  recipe: Recipe;
}

const TEMPLATE_DIRS = new Set(["_template"]);

export async function loadRecipes(cookbooksDir: string): Promise<LoadedRecipe[]> {
  const entries = await readdir(cookbooksDir, { withFileTypes: true });
  const recipes: LoadedRecipe[] = [];

  for (const entry of entries) {
    if (!entry.isDirectory()) continue;
    if (TEMPLATE_DIRS.has(entry.name)) continue;
    if (entry.name.startsWith(".")) continue;

    const recipePath = join(cookbooksDir, entry.name, "recipe.json");
    try {
      const raw = await readFile(recipePath, "utf8");
      const recipe = JSON.parse(raw) as Recipe;
      recipes.push({ dir: entry.name, recipe });
    } catch (err) {
      if ((err as NodeJS.ErrnoException).code === "ENOENT") continue;
      throw new Error(`Failed to parse ${recipePath}: ${(err as Error).message}`);
    }
  }

  recipes.sort((a, b) => a.recipe.order - b.recipe.order);
  return recipes;
}
