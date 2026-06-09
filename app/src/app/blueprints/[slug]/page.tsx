import { notFound } from "next/navigation";
import Link from "next/link";
import { MDXRemote } from "next-mdx-remote/rsc";
import remarkGfm from "remark-gfm";
import { ArrowLeft } from "lucide-react";
import { getBlueprint, getBlueprints } from "@/lib/blueprints";
import { loadBlueprintMdx } from "@/lib/mdx";
import { Badge, Button, Container, NebiusLogo } from "@/components";
import { mdxComponents } from "@/components/mdx";
import { ghPath } from "@/lib/site";

export function generateStaticParams() {
  return getBlueprints().map((b) => ({ slug: b.slug }));
}

export async function generateMetadata({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const blueprint = getBlueprint(slug);
  if (!blueprint) return {};
  return { title: blueprint.title, description: blueprint.tagline };
}

export default async function BlueprintPage({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const blueprint = getBlueprint(slug);
  if (!blueprint) notFound();

  const mdx = await loadBlueprintMdx(blueprint.slug);

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
            blueprint / {blueprint.difficulty}
          </div>
          <h1 className="font-display text-[56px] leading-[0.9] tracking-[0.01em] text-ink sm:text-[80px]">
            {blueprint.title}
          </h1>
          <p className="max-w-2xl text-lg italic leading-snug text-ink-soft sm:text-xl">
            {blueprint.tagline}
          </p>

          <div className="mt-2">
            <a href={ghPath("tree", "main", "blueprints", blueprint.dir)} target="_blank" rel="noreferrer">
              <Button>View source ↗</Button>
            </a>
          </div>
        </header>

        {/* Spec strip */}
        <dl className="mb-10 grid grid-cols-2 gap-px border-y border-edge bg-edge sm:grid-cols-4">
          <SpecCell label="run" value={blueprint.estimatedRunTime} mono />
          <SpecCell label="stack" value={blueprint.stack.primary[0] ?? "—"} mono />
          <SpecCell
            label="models"
            value={`${blueprint.models.length}`}
            mono
          />
          <SpecCell
            label="integrations"
            value={`${blueprint.integrations.length}`}
            mono
            extra={
              <div className="mt-1 flex flex-wrap gap-1">
                {blueprint.integrations.map((i) => (
                  <Badge key={i} tone="accent">
                    {i}
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
                href={ghPath("tree", "main", "blueprints", blueprint.dir)}
                className="text-accent underline decoration-accent/30 underline-offset-2 hover:decoration-accent"
              >
                blueprints/{blueprint.dir}
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
      <div className="font-mono text-[10px] uppercase tracking-[0.18em] text-ink-dim">{label}</div>
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
