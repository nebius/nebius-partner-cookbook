import { afterEach, expect, test } from "bun:test";
import { execFileSync } from "node:child_process";
import { mkdtemp, mkdir, rm, writeFile } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join, resolve } from "node:path";
import { checkRepository } from "../check-repository-regressions";
import { loadRecipes } from "../lib/recipes";
import { normalizeBaseUrl } from "../lib/nebius-url";

const directories: string[] = [];
async function fixture(): Promise<string> {
  const dir = await mkdtemp(join(tmpdir(), "cookbook-review-"));
  directories.push(dir);
  return dir;
}
afterEach(async () => {
  await Promise.all(directories.splice(0).map((dir) => rm(dir, { recursive: true, force: true })));
});

// Assemble the old host so the production guard can scan its own regression tests.
const oldHost = ["api", "studio", "nebius", "ai"].join(".");
test("repository guard checks tracked text, ignores private and generated files", async () => {
  const dir = await fixture();
  execFileSync("git", ["init", "-q", dir]);
  await writeFile(join(dir, ".gitignore"), ".env\n.claude/settings.local.json\n");
  await mkdir(join(dir, ".claude"));
  await writeFile(join(dir, ".env"), oldHost);
  await writeFile(join(dir, ".claude/settings.local.json"), oldHost);
  await writeFile(join(dir, "untracked.md"), oldHost);
  await writeFile(join(dir, "tracked.md"), oldHost);
  await mkdir(join(dir, "blueprints/demo/data"), { recursive: true });
  await writeFile(join(dir, "blueprints/demo/data/run.json"), oldHost);
  execFileSync("git", ["add", ".gitignore", "tracked.md", "blueprints"], { cwd: dir });
  expect(await checkRepository(dir)).toEqual(["tracked.md:1: pre-rebrand Token Factory host"]);
  await rm(join(dir, "tracked.md"));
  expect(await checkRepository(dir)).toEqual([]);
});

test("historical SDK warning is allowed only on the exact documented line", async () => {
  const dir = await fixture();
  execFileSync("git", ["init", "-q", dir]);
  const path = "blueprints/sentinel-compliance-auditor/CLAUDE.md";
  await mkdir(join(dir, "blueprints/sentinel-compliance-auditor"), { recursive: true });
  const warning = `langchain_nebius 0.1.3 defaults to \`https://${oldHost}/v1/\`; always override \`base_url\` with \`https://api.tokenfactory.nebius.com/v1/\`.`;
  await writeFile(join(dir, path), warning);
  execFileSync("git", ["add", path], { cwd: dir });
  expect(await checkRepository(dir)).toEqual([]);
  await writeFile(join(dir, path), `${warning}\nUse https://${oldHost}/v1/`);
  expect(await checkRepository(dir)).toHaveLength(1);
});

test("recipe discovery tolerates WIP folders and skips hidden/template folders", async () => {
  const dir = await fixture();
  for (const folder of ["01-ready", "02-wip", ".private", "_template"]) {
    await mkdir(join(dir, folder));
  }
  await writeFile(join(dir, "01-ready/recipe.json"), JSON.stringify({ order: 1, models: [] }));
  await writeFile(join(dir, ".private/recipe.json"), "invalid");
  await writeFile(join(dir, "_template/recipe.json"), "invalid");
  expect((await loadRecipes(dir)).map((item) => item.dir)).toEqual(["01-ready"]);
});

test("host-only model endpoints include v1 while custom API paths are preserved", () => {
  expect(normalizeBaseUrl("https://example.com/")).toBe("https://example.com/v1");
  expect(normalizeBaseUrl("https://example.com/v1/")).toBe("https://example.com/v1");
  expect(normalizeBaseUrl("https://example.com/proxy/v1/")).toBe("https://example.com/proxy/v1");
});

const run = { model: "test-model", workloadVersion: "v1", inputTokens: 10, outputTokens: 5, latencySeconds: 1, costUsd: 0.1 };
async function summarize(value: unknown) {
  const dir = await fixture();
  const input = join(dir, "runs.jsonl");
  await writeFile(input, Array.from({ length: 5 }, () => JSON.stringify(value)).join("\n"));
  const proc = Bun.spawn([process.execPath, resolve(import.meta.dir, "../summarize-benchmark.ts"), input], { stdout: "pipe", stderr: "pipe" });
  const [exitCode, stdout, stderr] = await Promise.all([proc.exited, new Response(proc.stdout).text(), new Response(proc.stderr).text()]);
  return { exitCode, stdout, stderr };
}
test.each([
  ["model", { ...run, model: undefined }],
  ["workloadVersion", { ...run, workloadVersion: " " }],
  ["inputTokens", { ...run, inputTokens: -1 }],
  ["object", null],
])("benchmark rejects invalid %s before printing a summary", async (field, value) => {
  const result = await summarize(value);
  expect(result.exitCode).not.toBe(0);
  expect(result.stdout).toBe("");
  expect(result.stderr).toContain(field as string);
});
test("valid benchmark produces complete metadata and medians", async () => {
  const result = await summarize(run);
  expect(result.exitCode).toBe(0);
  expect(JSON.parse(result.stdout)).toMatchObject({ model: "test-model", workloadVersion: "v1", runCount: 5, median: { inputTokens: 10, outputTokens: 5, latencySeconds: 1, costUsd: 0.1 } });
});
