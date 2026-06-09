import { join, resolve } from "node:path";
import { loadRecipes } from "../lib/recipes.ts";

interface RecipesTableOptions {
  cookbooksDir: string;
  columns?: string[];
  heading?: string;
}

const COLUMN_LABELS: Record<string, string> = {
  order: "#",
  title: "Recipe",
  stack: "Stack",
  difficulty: "Difficulty",
  readingTime: "Reading",
  runTime: "Run",
};

export async function generate(
  options: RecipesTableOptions,
  configDir: string,
): Promise<string> {
  const cookbooksDir = resolve(configDir, options.cookbooksDir);
  const recipes = await loadRecipes(cookbooksDir);
  const columns = options.columns ?? ["order", "title", "stack", "difficulty", "readingTime"];
  const heading = options.heading ?? "## Recipes";

  if (recipes.length === 0) {
    return `${heading}\n\n_No recipes yet. Bootstrap one with \`bun run new\`._\n`;
  }

  const header = `| ${columns.map((c) => COLUMN_LABELS[c] ?? c).join(" | ")} |`;
  const separator = `| ${columns.map(() => "---").join(" | ")} |`;

  const rows = recipes.map(({ dir, recipe }) => {
    const cells = columns.map((col) => {
      switch (col) {
        case "order":
          return String(recipe.order).padStart(2, "0");
        case "title": {
          const label = recipe.eyebrow
            ? `${recipe.eyebrow} — ${recipe.title}`
            : recipe.title;
          return `[${label}](./cookbooks/${dir}/)`;
        }
        case "stack": {
          const all = [...recipe.stack.primary, ...recipe.stack.secondary];
          return all.map((s) => `\`${s}\``).join(" ");
        }
        case "difficulty":
          return recipe.difficulty;
        case "readingTime":
          return recipe.estimatedReadingTime;
        case "runTime":
          return recipe.estimatedRunTime;
        case "tagline":
          return recipe.tagline;
        default:
          return "";
      }
    });
    return `| ${cells.join(" | ")} |`;
  });

  return [heading, "", header, separator, ...rows, ""].join("\n");
}

if (import.meta.main) {
  const cookbooksDir = process.argv[2] ?? join(process.cwd(), "cookbooks");
  console.log(await generate({ cookbooksDir: "." }, cookbooksDir));
}
