import { readFile } from "node:fs/promises";
import { join } from "node:path";

const RECIPES_CONTENT_DIR = join(process.cwd(), "src", "content", "recipes");
const BLUEPRINTS_CONTENT_DIR = join(process.cwd(), "src", "content", "blueprints");

/**
 * Read the compiled MDX for a recipe, stripping the leading YAML frontmatter
 * block that `scripts/build-recipes.ts` emits. The metadata it contains is
 * already available via the recipes manifest, so the renderer only needs the
 * body.
 */
export async function loadRecipeMdx(slug: string): Promise<string | null> {
  return loadMdx(join(RECIPES_CONTENT_DIR, `${slug}.mdx`));
}

/** Read the compiled MDX for a blueprint (see `scripts/build-blueprints.ts`). */
export async function loadBlueprintMdx(slug: string): Promise<string | null> {
  return loadMdx(join(BLUEPRINTS_CONTENT_DIR, `${slug}.mdx`));
}

async function loadMdx(path: string): Promise<string | null> {
  try {
    const raw = await readFile(path, "utf8");
    return stripFrontmatter(raw);
  } catch (err) {
    if ((err as NodeJS.ErrnoException).code === "ENOENT") return null;
    throw err;
  }
}

function stripFrontmatter(raw: string): string {
  if (!raw.startsWith("---")) return raw;
  const end = raw.indexOf("\n---", 3);
  if (end === -1) return raw;
  // Skip past the closing "---" and any trailing newlines.
  let i = end + 4;
  while (raw[i] === "\n") i++;
  return raw.slice(i);
}
