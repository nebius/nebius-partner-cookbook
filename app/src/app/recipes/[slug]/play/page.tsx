import { notFound } from "next/navigation";
import { getRecipe, getRecipes } from "@/lib/recipes";
import { PlayClient } from "./PlayClient";

export function generateStaticParams() {
  return getRecipes().map((r) => ({ slug: r.slug }));
}

export async function generateMetadata({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const recipe = getRecipe(slug);
  if (!recipe) return {};
  return {
    title: `Try: ${recipe.title}`,
    description: `Interactive client for ${recipe.title} — stream the agent live.`,
  };
}

export default async function PlayPage({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const recipe = getRecipe(slug);
  if (!recipe) notFound();

  return (
    <PlayClient
      slug={recipe.slug}
      title={recipe.title}
      tagline={recipe.tagline}
    />
  );
}
