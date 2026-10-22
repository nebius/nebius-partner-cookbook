export interface CompileOptions {
  slug: string;
  cookbookDir: string;
  repoUrl: string;
  cookbookSlugByDir: Record<string, string>;
  frontmatter?: Record<string, unknown>;
  /**
   * Top-level directory the content lives under. Defaults to "cookbooks";
   * blueprints pass "blueprints". Used to resolve relative links against the
   * canonical GitHub source.
   */
  baseDir?: string;
  /** Catalog route prefix for sibling links (e.g. "recipes" or "blueprints"). */
  siblingRoute?: string;
}

/**
 * Transform a hand-written cookbook README into MDX for the catalog site.
 *
 * Three things happen here:
 *  1. The leading H1 + tagline blockquote are stripped — the page chrome already
 *     renders the title and tagline from recipe.json, and a duplicate H1 hurts
 *     accessibility and SEO.
 *  2. Relative links are rewritten:
 *     - Sibling cookbook directories (e.g. `../02-foo-bar/`) become catalog routes
 *       (`/recipes/foo-bar`). This keeps in-catalog navigation client-side.
 *     - Every other relative target points at the canonical GitHub source.
 *  3. A frontmatter block is prepended (used by next-mdx-remote consumers that
 *     want to parse metadata directly from the .mdx file).
 *
 * The transform is plain string manipulation — fast, no AST roundtrip, and good
 * enough for our authored Markdown. If we ever need richer rewriting (e.g.
 * resolving `<Component>` references) we can swap in a remark plugin here
 * without touching the build script.
 */
export function compileCookbookReadme(markdown: string, options: CompileOptions): string {
  let body = markdown;
  body = stripLeadingTitle(body);
  body = rewriteLinks(body, options);

  const fm = options.frontmatter ?? { slug: options.slug };
  const frontmatterBlock =
    "---\n" +
    Object.entries(fm)
      .map(([k, v]) => `${k}: ${JSON.stringify(v)}`)
      .join("\n") +
    "\n---\n\n";

  return frontmatterBlock + body;
}

/**
 * Drop the first H1 and any blockquote that immediately follows it (used as the
 * tagline in our cookbook README convention).
 */
function stripLeadingTitle(markdown: string): string {
  const lines = markdown.split("\n");
  let i = 0;

  // Skip leading blank lines.
  while (i < lines.length && lines[i]?.trim() === "") i++;

  // Drop a leading H1.
  if (i < lines.length && /^#\s/.test(lines[i] ?? "")) {
    i++;
    // Skip blank lines between H1 and the optional tagline blockquote.
    while (i < lines.length && lines[i]?.trim() === "") i++;
    // Drop a contiguous blockquote (one or more `>`-prefixed lines).
    while (i < lines.length && /^>\s?/.test(lines[i] ?? "")) i++;
  }

  // Re-skip blank lines so the body starts cleanly.
  while (i < lines.length && lines[i]?.trim() === "") i++;

  return lines.slice(i).join("\n");
}

const LINK_RE = /(!?)\[([^\]]+)\]\(([^)\s]+)(\s+"[^"]*")?\)/g;

function rewriteLinks(markdown: string, options: CompileOptions): string {
  const { cookbookDir, repoUrl, cookbookSlugByDir } = options;
  const baseDir = options.baseDir ?? "cookbooks";
  const siblingRoute = options.siblingRoute ?? "recipes";
  return markdown.replace(LINK_RE, (_match, bang, label, target, title) => {
    const rewritten = rewriteTarget(
      target,
      cookbookDir,
      repoUrl,
      cookbookSlugByDir,
      baseDir,
      siblingRoute,
    );
    return `${bang}[${label}](${rewritten}${title ?? ""})`;
  });
}

function rewriteTarget(
  target: string,
  cookbookDir: string,
  repoUrl: string,
  cookbookSlugByDir: Record<string, string>,
  baseDir: string,
  siblingRoute: string,
): string {
  if (target.startsWith("http://") || target.startsWith("https://")) return target;
  if (target.startsWith("#")) return target;
  if (target.startsWith("mailto:")) return target;

  // Split off any fragment so we can normalize the path.
  const hashIdx = target.indexOf("#");
  const path = hashIdx === -1 ? target : target.slice(0, hashIdx);
  const fragment = hashIdx === -1 ? "" : target.slice(hashIdx);

  // Resolve relative to the content directory.
  const resolved = normalizePath(`${baseDir}/${cookbookDir}/${path}`);

  // Sibling in the same tier? Send the reader to its catalog page.
  const siblingMatch = resolved.match(new RegExp(`^${baseDir}/([^/]+)/?$`));
  if (siblingMatch) {
    const dir = siblingMatch[1];
    if (dir && dir !== cookbookDir) {
      const slug = cookbookSlugByDir[dir];
      if (slug) return `/${siblingRoute}/${slug}${fragment}`;
    }
  }

  // Anything else: point at the file in the canonical GitHub repo. We can only
  // *reliably* tell a directory from its trailing slash — files like `LICENSE`
  // or `Makefile` have no extension. Trailing-slash → tree, otherwise blob.
  const isDirectory = resolved.endsWith("/");
  const kind = isDirectory ? "tree" : "blob";
  const trimmed = resolved.replace(/\/$/, "");
  return `${repoUrl.trim().replace(/[./]+$/, "")}/${kind}/main/${trimmed}${fragment}`;
}

/** Resolve `.` and `..` segments in a posix-style path. */
function normalizePath(path: string): string {
  const parts = path.split("/");
  const out: string[] = [];
  for (const part of parts) {
    if (part === "" || part === ".") continue;
    if (part === "..") {
      out.pop();
      continue;
    }
    out.push(part);
  }
  return out.join("/") + (path.endsWith("/") ? "/" : "");
}
