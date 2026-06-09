#!/usr/bin/env bun
import { access } from "node:fs/promises";
import { dirname, join, resolve } from "node:path";
import { createInterface } from "node:readline/promises";
import { fileURLToPath } from "node:url";
import { spawn } from "node:child_process";

import { loadRecipes, type LoadedRecipe } from "./lib/recipes";

const here = dirname(fileURLToPath(import.meta.url));
const repoRoot = resolve(here, "..");
const cookbooksDir = join(repoRoot, "cookbooks");

interface Options {
  selector?: string;
  host: string;
  port: string;
  reload: boolean;
}

function usage(exitCode = 0): never {
  const stream = exitCode === 0 ? process.stdout : process.stderr;
  stream.write(`Usage: bun run backend [cookbook] [--port 8080] [--host 0.0.0.0] [--no-reload]

Examples:
  bun run backend
  bun run backend 03 --port 8080
  bun run backend real-time-data-tavily
  bun run start:backend 01 --host 0.0.0.0 --port 8000

When provided, <cookbook> may be an order number, full directory name, or recipe slug.
When omitted, an interactive cookbook menu is shown.
`);
  process.exit(exitCode);
}

function parseArgs(argv: string[]): Options {
  const options: Options = {
    host: "0.0.0.0",
    port: "8000",
    reload: true,
  };

  for (let index = 0; index < argv.length; index += 1) {
    const arg = argv[index];
    if (!arg) continue;

    if (arg === "--help" || arg === "-h") usage(0);

    if (arg === "--port" || arg === "-p") {
      const value = argv[index + 1];
      if (!value) throw new Error(`${arg} requires a value.`);
      options.port = value;
      index += 1;
      continue;
    }

    if (arg.startsWith("--port=")) {
      options.port = arg.slice("--port=".length);
      continue;
    }

    if (arg === "--host") {
      const value = argv[index + 1];
      if (!value) throw new Error("--host requires a value.");
      options.host = value;
      index += 1;
      continue;
    }

    if (arg.startsWith("--host=")) {
      options.host = arg.slice("--host=".length);
      continue;
    }

    if (arg === "--no-reload") {
      options.reload = false;
      continue;
    }

    if (arg.startsWith("-")) {
      throw new Error(`Unknown option: ${arg}`);
    }

    if (options.selector) {
      throw new Error(`Unexpected extra argument: ${arg}`);
    }
    options.selector = arg;
  }

  if (!/^\d+$/.test(options.port) || Number(options.port) <= 0) {
    throw new Error(`Invalid port: ${options.port}`);
  }

  return options;
}

function selectorMatches(selector: string, loaded: LoadedRecipe): boolean {
  const normalized = selector.toLowerCase();
  const order = String(loaded.recipe.order);
  const paddedOrder = order.padStart(2, "0");

  return (
    normalized === order ||
    normalized === paddedOrder ||
    normalized === loaded.dir.toLowerCase() ||
    normalized === loaded.recipe.slug.toLowerCase()
  );
}

async function ensureBackendExists(cookbookDir: string): Promise<void> {
  try {
    await access(join(cookbookDir, "pyproject.toml"));
    await access(join(cookbookDir, "app", "main.py"));
  } catch (err) {
    const message = (err as NodeJS.ErrnoException).message;
    throw new Error(`Selected cookbook is not a runnable backend: ${message}`);
  }
}

async function isRunnableBackend(loaded: LoadedRecipe): Promise<boolean> {
  try {
    await access(join(cookbooksDir, loaded.dir, "pyproject.toml"));
    await access(join(cookbooksDir, loaded.dir, "app", "main.py"));
    return true;
  } catch {
    return false;
  }
}

async function selectFromMenu(recipes: LoadedRecipe[]): Promise<LoadedRecipe> {
  const runnableRecipes: LoadedRecipe[] = [];
  for (const recipe of recipes) {
    if (await isRunnableBackend(recipe)) runnableRecipes.push(recipe);
  }

  if (runnableRecipes.length === 0) {
    throw new Error("No runnable cookbook backends found.");
  }

  if (!process.stdin.isTTY) {
    console.error("No cookbook provided and stdin is not interactive.");
    usage(1);
  }

  console.log("Select a cookbook backend to run:\n");
  runnableRecipes.forEach((loaded, index) => {
    const order = String(loaded.recipe.order).padStart(2, "0");
    console.log(`${index + 1}. ${order} ${loaded.recipe.title}`);
    console.log(`   ${loaded.dir}`);
  });

  const rl = createInterface({
    input: process.stdin,
    output: process.stdout,
  });

  const abort = (): never => {
    rl.close();
    process.exit(130);
  };

  rl.once("SIGINT", abort);
  process.once("SIGINT", abort);

  try {
    while (true) {
      const answer = (await rl.question("\nCookbook number: ")).trim();
      const selectedIndex = Number(answer) - 1;
      const selected = runnableRecipes[selectedIndex];
      if (Number.isInteger(selectedIndex) && selected) return selected;

      const matches = runnableRecipes.filter((recipe) => selectorMatches(answer, recipe));
      if (matches.length === 1) return matches[0] as LoadedRecipe;

      console.error("Choose one of the listed numbers, or enter a cookbook order/slug.");
    }
  } finally {
    rl.removeListener("SIGINT", abort);
    process.removeListener("SIGINT", abort);
    rl.close();
  }
}

async function main(): Promise<void> {
  let options: Options;
  try {
    options = parseArgs(process.argv.slice(2));
  } catch (err) {
    console.error((err as Error).message);
    usage(1);
  }

  const recipes = await loadRecipes(cookbooksDir);
  let selected: LoadedRecipe;

  if (!options.selector) {
    selected = await selectFromMenu(recipes);
  } else {
    const matches = recipes.filter((recipe) => selectorMatches(options.selector as string, recipe));

    if (matches.length === 0) {
      const available = recipes.map(({ dir, recipe }) => `${recipe.order}: ${dir}`).join("\n  ");
      console.error(`No cookbook matched "${options.selector}".`);
      console.error(`\nAvailable cookbooks:\n  ${available}`);
      process.exit(1);
    }

    if (matches.length > 1) {
      console.error(`Selector "${options.selector}" is ambiguous.`);
      for (const match of matches) console.error(`- ${match.dir}`);
      process.exit(1);
    }

    const matched = matches[0];
    if (!matched) {
      throw new Error("Failed to resolve cookbook.");
    }
    selected = matched;
  }

  const cwd = join(cookbooksDir, selected.dir);
  await ensureBackendExists(cwd);

  const args = ["run", "uvicorn", "app.main:app", "--host", options.host, "--port", options.port];
  if (options.reload) args.push("--reload");

  console.log(`Starting ${selected.dir} on http://${options.host}:${options.port}`);
  const child = spawn("uv", args, {
    cwd,
    env: {
      ...process.env,
      HOST: options.host,
      PORT: options.port,
    },
    stdio: "inherit",
  });

  for (const signal of ["SIGINT", "SIGTERM"] as const) {
    process.on(signal, () => {
      child.kill(signal);
    });
  }

  child.on("error", (err) => {
    console.error(`Failed to start uv: ${err.message}`);
    process.exit(1);
  });

  child.on("exit", (code, signal) => {
    if (signal === "SIGINT") process.exit(130);
    if (signal === "SIGTERM") process.exit(143);
    process.exit(code ?? 1);
  });
}

await main();
