#!/usr/bin/env bun

import { readFile } from "node:fs/promises";
import { resolve } from "node:path";

import type { Recipe } from "../packages/recipe-schema/src/types";

type Benchmark = NonNullable<Recipe["benchmark"]>;
type BenchmarkRun = Pick<Benchmark, "model" | "workloadVersion"> & Benchmark["median"];

function parseRun(value: unknown, line: number): BenchmarkRun {
  if (typeof value !== "object" || value === null || Array.isArray(value)) {
    throw new Error(`Line ${line} must be a benchmark object.`);
  }
  const run = value as Record<string, unknown>;
  for (const field of ["model", "workloadVersion"] as const) {
    if (typeof run[field] !== "string" || !run[field].trim()) {
      throw new Error(`Line ${line} has an invalid ${field}; expected a non-empty string.`);
    }
  }
  for (const field of ["inputTokens", "outputTokens", "latencySeconds", "costUsd"] as const) {
    const metric = run[field];
    if (typeof metric !== "number" || !Number.isFinite(metric) || metric < 0) {
      throw new Error(`Line ${line} has an invalid ${field}.`);
    }
  }
  return run as BenchmarkRun;
}

const inputPath = process.argv[2];
if (!inputPath) {
  console.error("Usage: bun run benchmark:summarize <runs.jsonl>");
  process.exit(2);
}

const lines = (await readFile(resolve(inputPath), "utf8"))
  .split(/\r?\n/)
  .map((line) => line.trim())
  .filter(Boolean);
const runs = lines.map((line, index) => {
  try {
    return parseRun(JSON.parse(line), index + 1);
  } catch (error) {
    throw new Error(`Invalid benchmark on line ${index + 1}: ${(error as Error).message}`);
  }
});

if (runs.length < 5) {
  throw new Error(`At least five runs are required; received ${runs.length}.`);
}

const first = runs[0];
if (!first) {
  throw new Error("Benchmark input is empty.");
}
if (runs.some((run) => run.model !== first.model || run.workloadVersion !== first.workloadVersion)) {
  throw new Error("Every run must use the same model and workloadVersion.");
}

function median(values: number[]): number {
  const sorted = [...values].sort((a, b) => a - b);
  const middle = Math.floor(sorted.length / 2);
  const upper = sorted[middle];
  if (upper === undefined) {
    throw new Error("Cannot calculate a median from an empty list.");
  }
  if (sorted.length % 2 === 1) {
    return upper;
  }
  const lower = sorted[middle - 1];
  if (lower === undefined) {
    throw new Error("Cannot calculate an even-sized median.");
  }
  return (lower + upper) / 2;
}

const result: Benchmark = {
  model: first.model,
  workloadVersion: first.workloadVersion,
  runCount: runs.length,
  measuredAt: new Date().toISOString().slice(0, 10),
  median: {
    inputTokens: median(runs.map((run) => run.inputTokens)),
    outputTokens: median(runs.map((run) => run.outputTokens)),
    latencySeconds: median(runs.map((run) => run.latencySeconds)),
    costUsd: median(runs.map((run) => run.costUsd)),
  },
};

console.log(JSON.stringify(result, null, 2));
