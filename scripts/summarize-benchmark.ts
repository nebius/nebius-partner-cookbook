#!/usr/bin/env bun

import { readFile } from "node:fs/promises";
import { resolve } from "node:path";

interface BenchmarkRun {
  model: string;
  workloadVersion: string;
  inputTokens: number;
  outputTokens: number;
  latencySeconds: number;
  costUsd: number;
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
    return JSON.parse(line) as BenchmarkRun;
  } catch (error) {
    throw new Error(`Invalid JSON on line ${index + 1}: ${(error as Error).message}`);
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

for (const [index, run] of runs.entries()) {
  for (const field of ["inputTokens", "outputTokens", "latencySeconds", "costUsd"] as const) {
    if (!Number.isFinite(run[field]) || run[field] < 0) {
      throw new Error(`Line ${index + 1} has an invalid ${field}.`);
    }
  }
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

const result = {
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
