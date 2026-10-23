#!/usr/bin/env bun

import { execFileSync } from "node:child_process";
import { readFile } from "node:fs/promises";
import { extname, join, resolve } from "node:path";

const repoRoot = resolve(import.meta.dir, "..");
const checkedExtensions = new Set([
  "", ".example", ".json", ".md", ".py", ".ts", ".tsx", ".yml", ".yaml",
]);
const forbidden = [
  { pattern: "api.studio.nebius.ai", reason: "pre-rebrand Token Factory host" },
  { pattern: "cd cookbook/cookbooks", reason: "incorrect clone directory" },
  { pattern: "cd nebius-cookbook/cookbooks", reason: "incorrect clone directory" },
  { pattern: "DeepSeek-R1-0528", reason: "retired quickstart model" },
  { pattern: "NEBIUS_API_KEY=NEBIUS_API_KEY=", reason: "duplicated env assignment" },
] as const;

// Exact, reviewed documentation exceptions; never exempt an entire file or host.
const allowedLines = new Set([
  "blueprints/sentinel-compliance-auditor/CLAUDE.md:langchain_nebius 0.1.3 defaults to `https://api.studio.nebius.ai/v1/`; always override `base_url` with `https://api.tokenfactory.nebius.com/v1/`.",
]);

export async function checkRepository(root: string): Promise<string[]> {
  const tracked = execFileSync("git", ["ls-files", "-z"], { cwd: root, encoding: "utf8" });
  const failures: string[] = [];
  for (const path of tracked.split("\0").filter(Boolean)) {
    if (path === "scripts/check-repository-regressions.ts") continue;
    if (!checkedExtensions.has(extname(path))) continue;
    // Corpora and captured evaluation output are data, not runnable configuration.
    if (/^blueprints\/[^/]+\/data\//.test(path)) continue;
    let content: string;
    try {
      content = await readFile(join(root, path), "utf8");
    } catch (error) {
      if ((error as NodeJS.ErrnoException).code === "ENOENT") continue;
      throw error;
    }
    for (const [index, line] of content.split(/\r?\n/).entries()) {
      if (allowedLines.has(`${path}:${line}`)) continue;
      for (const item of forbidden) {
        if (line.includes(item.pattern)) failures.push(`${path}:${index + 1}: ${item.reason}`);
      }
    }
  }
  return failures.sort();
}

if (import.meta.main) {
  const failures = await checkRepository(repoRoot);
  if (failures.length > 0) {
    console.error("Repository regression check failed:\n- " + failures.join("\n- "));
    process.exit(1);
  }
  console.log("Repository regression checks passed.");
}
