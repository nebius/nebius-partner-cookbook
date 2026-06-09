import manifest from "@/content/recipes-manifest.json" with { type: "json" };
import type { Recipe } from "@nebius-cookbook/recipe-schema";

export interface RecipeSummary extends Pick<
  Recipe,
  "slug" | "order" | "eyebrow" | "title" | "upcoming" | "tagline" | "difficulty" | "estimatedReadingTime" | "estimatedRunTime" | "stack" | "tags" | "models" | "publishedAt" | "updatedAt"
> {
  dir: string;
}

const recipes = manifest as RecipeSummary[];

export function getRecipes(): RecipeSummary[] {
  return [...recipes].sort((a, b) => a.order - b.order);
}

export function getRecipe(slug: string): RecipeSummary | undefined {
  return recipes.find((r) => r.slug === slug);
}
