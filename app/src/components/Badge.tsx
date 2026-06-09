import { cn } from "./cn";

type Tone = "neutral" | "accent" | "warn" | "success" | "critical";

const TONE: Record<Tone, string> = {
  neutral: "border-edge-strong text-ink-soft bg-surface",
  accent: "border-accent/40 text-accent bg-accent-soft",
  warn: "border-amber-400/40 text-amber-300 bg-amber-400/10",
  success: "border-emerald-400/40 text-emerald-300 bg-emerald-400/10",
  critical: "border-red-400/40 text-red-300 bg-red-400/10",
};

interface BadgeProps {
  children: React.ReactNode;
  tone?: Tone;
  className?: string;
  /** Render as a thin terminal-style bracket pill, e.g. [STREAMING]. */
  bracket?: boolean;
}

export function Badge({ children, tone = "neutral", className, bracket = false }: BadgeProps) {
  return (
    <span
      className={cn(
        "inline-flex items-center gap-1 border px-1.5 py-0.5 font-mono text-[10px] uppercase leading-[1.4] tracking-[0.12em]",
        TONE[tone],
        className,
      )}
    >
      {bracket ? <span aria-hidden>[</span> : null}
      {children}
      {bracket ? <span aria-hidden>]</span> : null}
    </span>
  );
}
