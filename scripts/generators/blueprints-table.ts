import { join, resolve } from "node:path";
import { loadBlueprints } from "../lib/blueprints.ts";

interface BlueprintsTableOptions {
  blueprintsDir: string;
  columns?: string[];
  heading?: string;
}

const COLUMN_LABELS: Record<string, string> = {
  title: "Blueprint",
  stack: "Stack",
  integrations: "Integrations",
  difficulty: "Difficulty",
  runTime: "Run",
};

export async function generate(
  options: BlueprintsTableOptions,
  configDir: string,
): Promise<string> {
  const blueprintsDir = resolve(configDir, options.blueprintsDir);
  const blueprints = await loadBlueprints(blueprintsDir);
  const columns = options.columns ?? ["title", "stack", "integrations", "runTime"];
  const heading = options.heading ?? "## Blueprints";
  const headingLines = heading ? [heading, ""] : [];

  if (blueprints.length === 0) {
    return [...headingLines, "_No blueprints yet._", ""].join("\n");
  }

  const header = `| ${columns.map((c) => COLUMN_LABELS[c] ?? c).join(" | ")} |`;
  const separator = `| ${columns.map(() => "---").join(" | ")} |`;

  const rows = blueprints.map(({ dir, blueprint }) => {
    const cells = columns.map((col) => {
      switch (col) {
        case "title": {
          const label = blueprint.eyebrow
            ? `${blueprint.eyebrow} — ${blueprint.title}`
            : blueprint.title;
          return `[${label}](./blueprints/${dir}/)`;
        }
        case "stack": {
          const all = [...blueprint.stack.primary, ...blueprint.stack.secondary];
          return all.map((s) => `\`${s}\``).join(" ");
        }
        case "integrations":
          return blueprint.integrations.map((s) => `\`${s}\``).join(" ");
        case "difficulty":
          return blueprint.difficulty;
        case "runTime":
          return blueprint.estimatedRunTime;
        case "tagline":
          return blueprint.tagline;
        default:
          return "";
      }
    });
    return `| ${cells.join(" | ")} |`;
  });

  return [...headingLines, header, separator, ...rows, ""].join("\n");
}

if (import.meta.main) {
  const blueprintsDir = process.argv[2] ?? join(process.cwd(), "blueprints");
  console.log(await generate({ blueprintsDir: "." }, blueprintsDir));
}
