export type Difficulty = "beginner" | "intermediate" | "advanced";
export type ModelRole = "primary" | "planner" | "writer" | "critic" | "embed" | "rerank";
export type HttpMethod = "GET" | "POST" | "PUT" | "PATCH" | "DELETE";

export interface RecipeStack {
  primary: string[];
  secondary: string[];
}

export interface RecipeStory {
  problem: string;
  solution: string;
  outcome: string;
}

export interface RecipeModel {
  id: string;
  role: ModelRole;
}

export interface RecipeQuickstart {
  clone: string;
  configure: string;
  run: string;
}

export interface RecipeEndpoint {
  method: HttpMethod;
  path: string;
  streaming?: boolean;
  description: string;
}

export interface RecipeDeployment {
  target: string;
  instructions: string;
}

export interface RecipeAuthor {
  name: string;
  url?: string;
}

export interface RecipeAssets {
  hero?: string;
  demo?: string;
  architecture?: string;
}

export interface Recipe {
  $schema?: string;
  slug: string;
  order: number;
  eyebrow: string;
  title: string;
  upcoming?: boolean;
  tagline: string;
  difficulty: Difficulty;
  estimatedReadingTime: string;
  estimatedRunTime: string;
  stack: RecipeStack;
  tags: string[];
  story: RecipeStory;
  prerequisites: string[];
  models: RecipeModel[];
  assets?: RecipeAssets;
  quickstart: RecipeQuickstart;
  endpoints: RecipeEndpoint[];
  deployment: RecipeDeployment;
  nextRecipe?: string;
  authors: RecipeAuthor[];
  publishedAt: string;
  updatedAt: string;
}
