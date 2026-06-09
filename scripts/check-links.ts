#!/usr/bin/env bun
import { readdir, readFile, stat } from "node:fs/promises";
import { dirname, isAbsolute, join, relative, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const repoRoot = resolve(here, "..");

const SKIP_DIRS = new Set(["node_modules", ".git", ".next", "dist", "build", ".venv", "__pycache__"]);
const LINK_RE = /\[([^\]]+)\]\(([^)\s]+)(?:\s+"[^"]*")?\)/g;

async function walk(dir: string, files: string[] = []): Promise<string[]> {
  const entries = await readdir(dir, { withFileTypes: true });
  for (const e of entries) {
    if (e.isDirectory()) {
      if (SKIP_DIRS.has(e.name)) continue;
      await walk(join(dir, e.name), files);
    } else if (e.isFile() && e.name.endsWith(".md")) {
      files.push(join(dir, e.name));
    }
  }
  return files;
}

const files = await walk(repoRoot);
const errors: string[] = [];
const externalCache = new Map<string, boolean>();

for (const file of files) {
  const content = await readFile(file, "utf8");
  let match: RegExpExecArray | null;
  while ((match = LINK_RE.exec(content)) !== null) {
    const target = match[2];
    if (!target) continue;
    if (target.startsWith("#")) continue;
    if (target.startsWith("mailto:")) continue;

    if (target.startsWith("http://") || target.startsWith("https://")) {
      if (process.env.CHECK_EXTERNAL !== "1") continue;
      if (externalCache.has(target)) {
        if (!externalCache.get(target)) {
          errors.push(`${relative(repoRoot, file)}: broken external ${target}`);
        }
        continue;
      }
      try {
        const res = await fetch(target, { method: "HEAD", redirect: "follow" });
        const ok = res.ok || res.status === 405;
        externalCache.set(target, ok);
        if (!ok) errors.push(`${relative(repoRoot, file)}: ${res.status} ${target}`);
      } catch (err) {
        externalCache.set(target, false);
        errors.push(`${relative(repoRoot, file)}: fetch failed ${target} — ${(err as Error).message}`);
      }
      continue;
    }

    const cleanTarget = target.split("#")[0]!;
    if (!cleanTarget) continue;
    // README/ sources are composed into the root README.md, so relative links
    // in them are resolved against the repo root, not their own directory.
    const isReadmeSource = relative(repoRoot, file).startsWith("README/");
    const base = isReadmeSource ? repoRoot : dirname(file);
    const linkPath = isAbsolute(cleanTarget)
      ? join(repoRoot, cleanTarget)
      : resolve(base, cleanTarget);
    try {
      await stat(linkPath);
    } catch {
      errors.push(`${relative(repoRoot, file)}: missing ${cleanTarget}`);
    }
  }
}

if (errors.length > 0) {
  console.error(`Found ${errors.length} broken link${errors.length === 1 ? "" : "s"}:`);
  for (const e of errors) console.error(`  - ${e}`);
  process.exit(1);
}

console.log(`Checked ${files.length} markdown file${files.length === 1 ? "" : "s"}. All links resolve.`);
