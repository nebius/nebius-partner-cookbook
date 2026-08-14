// Auto-generated. Run `bun run generate`.

/**
 * Metadata for a single cookbook recipe. Source of truth for the recipes table and the web app catalog.
 */
export interface Recipe {
  $schema?: string;
  /**
   * Kebab-case identifier. Must match the cookbook directory slug.
   */
  slug: string;
  /**
   * Position in the cookbook sequence. Must match the directory prefix NN.
   */
  order: number;
  /**
   * Short narrative-arc label shown above the title on recipe cards (e.g. "Foundation").
   */
  eyebrow: string;
  title: string;
  /**
   * If true, the recipe is planned but not yet built; the web card renders at reduced opacity.
   */
  upcoming?: boolean;
  tagline: string;
  difficulty: "beginner" | "intermediate" | "advanced";
  estimatedReadingTime: string;
  estimatedRunTime: string;
  stack: {
    /**
     * @minItems 1
     */
    primary: [string, ...string[]];
    secondary: string[];
  };
  /**
   * @minItems 1
   */
  tags: [string, ...string[]];
  story: {
    problem: string;
    solution: string;
    outcome: string;
  };
  prerequisites: string[];
  /**
   * @minItems 1
   */
  models: [
    {
      id: string;
      role: "primary" | "planner" | "writer" | "critic" | "embed" | "rerank";
    },
    ...{
      id: string;
      role: "primary" | "planner" | "writer" | "critic" | "embed" | "rerank";
    }[]
  ];
  benchmark?: {
    model: string;
    workloadVersion: string;
    runCount: number;
    measuredAt: string;
    median: {
      inputTokens: number;
      outputTokens: number;
      latencySeconds: number;
      costUsd: number;
    };
  };
  assets?: {
    hero?: string;
    demo?: string;
    architecture?: string;
  };
  quickstart: {
    clone: string;
    configure: string;
    run: string;
  };
  endpoints: {
    method: "GET" | "POST" | "PUT" | "PATCH" | "DELETE";
    path: string;
    streaming?: boolean;
    description: string;
  }[];
  deployment: {
    target: string;
    instructions: string;
  };
  nextRecipe?: string;
  /**
   * @minItems 1
   */
  authors: [
    {
      name: string;
      url?: string;
    },
    ...{
      name: string;
      url?: string;
    }[]
  ];
  publishedAt: string;
  updatedAt: string;
}
