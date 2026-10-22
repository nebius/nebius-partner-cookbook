import { readdir, readFile } from "node:fs/promises";
import { join } from "node:path";

import type { Recipe } from "../../packages/recipe-schema/src/types";
export type { Recipe };

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
