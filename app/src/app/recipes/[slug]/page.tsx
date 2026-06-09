import { notFound } from "next/navigation";
import Link from "next/link";
import { MDXRemote } from "next-mdx-remote/rsc";
import remarkGfm from "remark-gfm";
import { ArrowLeft, Play } from "lucide-react";
import { getRecipe, getRecipes } from "@/lib/recipes";
import { loadRecipeMdx } from "@/lib/mdx";
import { Badge, Button, Container, NebiusLogo } from "@/components";
import { mdxComponents } from "@/components/mdx";
import { ghPath } from "@/lib/site";

export function generateStaticParams() {
  return getRecipes().map((r) => ({ slug: r.slug }));
}

export async function generateMetadata({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const recipe = getRecipe(slug);
  if (!recipe) return {};
  return { title: recipe.title, description: recipe.tagline };
}

export default async function RecipePage({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const recipe = getRecipe(slug);
  if (!recipe) notFound();

  const mdx = await loadRecipeMdx(recipe.slug);

  return (
    <main>
      <Container size="md" className="pt-12 pb-24 sm:pt-16">
        <div className="flex flex-wrap items-center justify-between gap-4">
          <Link href="/" className="inline-flex items-center gap-3">
            <NebiusLogo height={20} />
            <span className="font-mono text-[11px] uppercase tracking-[0.18em] text-ink-soft">
              / Agent Blueprint Recipes
            </span>
          </Link>
          <Link
            href="/"
            className="inline-flex items-center gap-1.5 font-mono text-[11px] uppercase tracking-[0.18em] text-ink-soft transition hover:text-accent"
          >
            <ArrowLeft className="size-3" /> all recipes
          </Link>
        </div>

        {/* Hero */}
        <header className="mt-10 mb-12 grid gap-6 sm:mt-14">
          <div className="font-mono text-[11px] uppercase tracking-[0.22em] text-accent">
            recipe · {String(recipe.order).padStart(2, "0")} / {recipe.difficulty}
          </div>
          <h1 className="font-display text-[64px] leading-[0.9] tracking-[0.01em] text-ink sm:text-[88px]">
            {recipe.title}
          </h1>
          <p className="max-w-2xl text-lg italic leading-snug text-ink-soft sm:text-xl">
            {recipe.tagline}
          </p>

          <div className="mt-2">
            <Link href={`/recipes/${recipe.slug}/play`}>
              <Button>
                <Play className="size-3" /> Try it live
              </Button>
            </Link>
          </div>
        </header>

        {/* Spec strip */}
        <dl className="mb-16 grid grid-cols-2 gap-px border-y border-edge bg-edge sm:grid-cols-4">
          <SpecCell label="read" value={recipe.estimatedReadingTime} />
          <SpecCell label="run" value={recipe.estimatedRunTime} />
          <SpecCell label="stack" value={recipe.stack.primary[0] ?? "—"} mono />
          <SpecCell
            label="models"
            value={`${recipe.models.length}`}
            mono
            extra={
              <div className="mt-1 flex flex-wrap gap-1">
                {recipe.models.map((m) => (
                  <Badge key={m.id} tone="accent">
                    {m.role}
                  </Badge>
                ))}
              </div>
            }
          />
        </dl>

        <article>
          {mdx ? (
            <MDXRemote
              source={mdx}
              components={mdxComponents}
              options={{
                mdxOptions: {
                  remarkPlugins: [remarkGfm],
                },
              }}
            />
          ) : (
            <p className="font-mono text-sm text-ink-dim">
              No README yet. See{" "}
              <a
                href={ghPath("tree", "main", "cookbooks", recipe.dir)}
                className="text-accent underline decoration-accent/30 underline-offset-2 hover:decoration-accent"
              >
                cookbooks/{recipe.dir}
              </a>
              .
            </p>
          )}
        </article>
      </Container>
    </main>
  );
}

function SpecCell({
  label,
  value,
  mono = false,
  extra,
}: {
  label: string;
  value: string;
  mono?: boolean;
  extra?: React.ReactNode;
}) {
  return (
    <div className="bg-paper px-5 py-4">
      <div className="font-mono text-[10px] uppercase tracking-[0.18em] text-ink-dim">
        {label}
      </div>
      <div
        className={
          mono
            ? "mt-1.5 font-mono text-sm text-ink"
            : "mt-1 font-display text-4xl leading-none text-ink"
        }
      >
        {value}
      </div>
      {extra}
    </div>
  );
}
