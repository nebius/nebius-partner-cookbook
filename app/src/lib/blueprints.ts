import manifest from "@/content/blueprints-manifest.json" with { type: "json" };

export interface BlueprintSummary {
  slug: string;
  eyebrow: string;
  title: string;
  upcoming: boolean;
  tagline: string;
  summary: string;
  difficulty: "beginner" | "intermediate" | "advanced";
  estimatedRunTime: string;
  stack: { primary: string[]; secondary: string[] };
  tags: string[];
  models: { id: string; provider?: string; role?: string }[];
  integrations: string[];
  capabilities: { hasUI?: boolean; hasEval?: boolean; hasDataset?: boolean };
  dataset: { description?: string; items?: number } | null;
  publishedAt: string;
  updatedAt: string;
  dir: string;
}

const blueprints = manifest as BlueprintSummary[];

export function getBlueprints(): BlueprintSummary[] {
  return [...blueprints].sort((a, b) => a.title.localeCompare(b.title));
}

export function getBlueprint(slug: string): BlueprintSummary | undefined {
  return blueprints.find((b) => b.slug === slug);
}
