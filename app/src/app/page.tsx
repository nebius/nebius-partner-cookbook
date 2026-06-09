import Link from "next/link";
import { ArrowUpRight } from "lucide-react";
import { getRecipes } from "@/lib/recipes";
import type { RecipeSummary } from "@/lib/recipes";
import { getBlueprints } from "@/lib/blueprints";
import type { BlueprintSummary } from "@/lib/blueprints";
import { Badge, Container, NebiusLogo } from "@/components";
import { GITHUB_REPO_URL } from "@/lib/site";

export default function HomePage() {
  const recipes = getRecipes();
  const blueprints = getBlueprints();

  return (
    <main className="min-h-dvh">
      <Container size="lg" className="pt-24 pb-24 sm:pt-32">
        {/* Masthead */}
        <header className="mb-20 grid gap-8 sm:grid-cols-[auto_1fr] sm:items-end">
          <div className="space-y-6">
            <div className="flex items-center gap-3">
              <NebiusLogo height={28} />
              <span className="font-mono text-[11px] uppercase tracking-[0.22em] text-ink-soft">
                / Agent Blueprint Recipes · v0.1
              </span>
              <span className="ml-1 inline-flex items-center gap-1.5 font-mono text-[10px] uppercase tracking-[0.18em] text-accent">
                <span className="size-1.5 rounded-full bg-accent phosphor-dot" aria-hidden />
                live
              </span>
            </div>
            <h1 className="font-display text-[88px] leading-[0.85] tracking-[0.01em] text-ink sm:text-[128px]">
              Production agents,
              <br />
              <span className="text-accent">unforked.</span>
            </h1>
          </div>

          <p className="max-w-md text-lg italic leading-snug text-ink-soft sm:justify-self-end sm:text-right">
            Runnable, observable, deployable recipes — and complete reference blueprints — for
            building AI agents on Nebius Token Factory + Partners. No magic, no toy code.
          </p>
        </header>

        {/* Stat row */}
        <div className="mb-16 grid grid-cols-2 gap-px border-y border-edge bg-edge sm:grid-cols-4">
          <Stat label="recipes" value={String(recipes.length)} />
          <Stat label="blueprints" value={String(blueprints.length)} />
          <Stat label="runtime" value="python 3.12" />
          <Stat label="provider" value="nebius" />
        </div>

        {/* Recipes index */}
        <section>
          <div className="mb-6 flex items-baseline justify-between">
            <h2 className="font-mono text-[11px] uppercase tracking-[0.22em] text-ink-soft">
              ▸ Recipes
            </h2>
            <span className="font-mono text-[11px] text-ink-dim">
              {String(recipes.length).padStart(2, "0")} ↦ ∞
            </span>
          </div>

          {recipes.length === 0 ? (
            <p className="font-mono text-sm text-ink-dim">No recipes yet.</p>
          ) : (
            <div className="grid gap-5 lg:grid-cols-2">
              {recipes.map((r) => (
                <RecipeCard key={r.slug} recipe={r} />
              ))}
            </div>
          )}
        </section>

        {/* Blueprints index */}
        {blueprints.length > 0 ? (
          <section className="mt-20">
            <div className="mb-6 flex items-baseline justify-between">
              <h2 className="font-mono text-[11px] uppercase tracking-[0.22em] text-ink-soft">
                ▸ Blueprints
              </h2>
              <span className="font-mono text-[11px] text-ink-dim">
                {String(blueprints.length).padStart(2, "0")} ↦ ∞
              </span>
            </div>
            <p className="mb-6 max-w-2xl text-[15px] leading-relaxed text-ink-soft">
              Complete, deployable reference applications. Larger than recipes and not part of the
              sequence — clone and run them end-to-end.
            </p>

            <div className="grid gap-5">
              {blueprints.map((b) => (
                <BlueprintCard key={b.slug} blueprint={b} />
              ))}
            </div>
          </section>
        ) : null}

        {/* Footer */}
        <footer className="mt-24 flex flex-wrap items-center justify-between gap-4 border-t border-edge pt-6 font-mono text-[11px] uppercase tracking-[0.16em] text-ink-dim">
          <span>
            Build with &lt;3 by{" "}
            <a
            href="https://clementsauvage.me/?utm_source=agent_blueprint_recipes&utm_medium=referral&utm_campaign=agent_blueprint_recipes"
              className="transition hover:text-accent"
              target="_blank"
              rel="noreferrer"
            >
              Clément S.
            </a>{" "}
            and the Nebius team
          </span>
          <a
            href={GITHUB_REPO_URL}
            className="transition hover:text-accent"
            target="_blank"
            rel="noreferrer"
          >
            github ↗
          </a>
        </footer>
      </Container>
    </main>
  );
}

function Stat({ label, value }: { label: string; value: string }) {
  return (
    <div className="bg-paper px-5 py-5">
      <div className="font-mono text-[10px] uppercase tracking-[0.18em] text-ink-dim">{label}</div>
      <div className="mt-1 font-display text-4xl leading-none text-ink">{value}</div>
    </div>
  );
}

function RecipeCard({ recipe }: { recipe: RecipeSummary }) {
  const difficultyTone =
    recipe.difficulty === "beginner"
      ? "neutral"
      : recipe.difficulty === "intermediate"
        ? "accent"
        : "warn";

  const stackChips = [...recipe.stack.primary, ...recipe.stack.secondary.slice(0, 2)];

  return (
    <Link href={`/recipes/${recipe.slug}`} className="group block">
      <article
        className={
          "relative flex h-full flex-col overflow-hidden border border-edge bg-surface/30 transition " +
          "group-hover:border-accent/60 group-hover:bg-surface/60 group-hover:shadow-[0_0_48px_-24px_var(--color-accent-glow)] " +
          (recipe.upcoming ? "opacity-50" : "")
        }
      >
        {/* Order watermark — bleeds out of the top-right corner */}
        <span
          aria-hidden
          className="pointer-events-none absolute -right-3 -top-12 select-none font-display text-[180px] leading-none text-edge-strong/70 transition group-hover:text-accent/15"
        >
          {String(recipe.order).padStart(2, "0")}
        </span>

        {/* Header strip */}
        <div className="relative flex items-center justify-between border-b border-edge px-6 py-3 sm:px-7">
          <span className="font-mono text-[11px] uppercase tracking-[0.18em] text-accent">
            recipe · {String(recipe.order).padStart(2, "0")}
          </span>
          <Badge tone={difficultyTone}>{recipe.difficulty}</Badge>
        </div>

        {/* Body */}
        <div className="relative flex-1 space-y-4 px-6 py-7 sm:px-7">
          <div className="flex items-start justify-between gap-4">
            <div className="space-y-1.5">
              <span className="block font-mono text-sm font-bold uppercase tracking-[0.16em] text-accent">
                {recipe.eyebrow}
              </span>
              <h3 className="font-display text-[44px] leading-[0.9] tracking-[0.01em] text-ink transition group-hover:text-accent sm:text-5xl">
                {recipe.title}
              </h3>
            </div>
            <ArrowUpRight className="size-5 shrink-0 text-ink-dim transition group-hover:translate-x-0.5 group-hover:-translate-y-0.5 group-hover:text-accent" />
          </div>
          <p className="text-[15px] leading-relaxed text-ink-soft">{recipe.tagline}</p>
        </div>

        {/* Footer — stack chips + read time */}
        <div className="relative flex items-center justify-between gap-4 border-t border-edge px-6 py-3 sm:px-7">
          <div className="flex min-w-0 flex-wrap items-center gap-x-3 gap-y-1 font-mono text-[10px] uppercase tracking-[0.14em] text-ink-dim">
            {stackChips.map((s, i) => (
              <span key={s} className="inline-flex items-center gap-3">
                {i > 0 ? <span className="text-edge-strong">·</span> : null}
                {s}
              </span>
            ))}
          </div>
          <span className="shrink-0 font-mono text-[10px] uppercase tracking-[0.14em] text-ink-dim">
            {recipe.estimatedReadingTime}
          </span>
        </div>
      </article>
    </Link>
  );
}

function BlueprintCard({ blueprint }: { blueprint: BlueprintSummary }) {
  const stackChips = [...blueprint.stack.primary, ...blueprint.stack.secondary.slice(0, 2)];

  return (
    <Link href={`/blueprints/${blueprint.slug}`} className="group block">
      <article
        className={
          "relative flex h-full flex-col overflow-hidden border border-edge bg-surface/30 transition " +
          "group-hover:border-accent/60 group-hover:bg-surface/60 group-hover:shadow-[0_0_48px_-24px_var(--color-accent-glow)] " +
          (blueprint.upcoming ? "opacity-50" : "")
        }
      >
        {/* Glyph watermark — bleeds out of the top-right corner */}
        <span
          aria-hidden
          className="pointer-events-none absolute -right-4 -top-16 select-none font-display text-[200px] leading-none text-edge-strong/60 transition group-hover:text-accent/15"
        >
          ◈
        </span>

        {/* Header strip */}
        <div className="relative flex items-center justify-between gap-3 border-b border-edge px-6 py-3 sm:px-7">
          <span className="font-mono text-[11px] uppercase tracking-[0.18em] text-accent">
            blueprint
          </span>
          <div className="flex items-center gap-2">
            <Badge tone="warn">reference app</Badge>
            {blueprint.capabilities?.hasUI ? <Badge tone="accent">ui</Badge> : null}
          </div>
        </div>

        {/* Body */}
        <div className="relative flex-1 space-y-4 px-6 py-7 sm:px-7">
          <div className="flex items-start justify-between gap-4">
            <div className="space-y-1.5">
              <span className="block font-mono text-sm font-bold uppercase tracking-[0.16em] text-accent">
                {blueprint.eyebrow}
              </span>
              <h3 className="font-display text-[40px] leading-[0.9] tracking-[0.01em] text-ink transition group-hover:text-accent sm:text-5xl">
                {blueprint.title}
              </h3>
            </div>
            <ArrowUpRight className="size-5 shrink-0 text-ink-dim transition group-hover:translate-x-0.5 group-hover:-translate-y-0.5 group-hover:text-accent" />
          </div>
          <p className="max-w-2xl text-[15px] leading-relaxed text-ink-soft">{blueprint.tagline}</p>
        </div>

        {/* Footer — stack + integrations + run time */}
        <div className="relative flex items-center justify-between gap-4 border-t border-edge px-6 py-3 sm:px-7">
          <div className="flex min-w-0 flex-wrap items-center gap-x-3 gap-y-1 font-mono text-[10px] uppercase tracking-[0.14em] text-ink-dim">
            {stackChips.map((s, i) => (
              <span key={s} className="inline-flex items-center gap-3">
                {i > 0 ? <span className="text-edge-strong">·</span> : null}
                {s}
              </span>
            ))}
          </div>
          <span className="shrink-0 font-mono text-[10px] uppercase tracking-[0.14em] text-ink-dim">
            {blueprint.estimatedRunTime}
          </span>
        </div>
      </article>
    </Link>
  );
}
