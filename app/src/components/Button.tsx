import { forwardRef } from "react";
import { cn } from "./cn";

type Variant = "primary" | "secondary" | "ghost" | "outline";
type Size = "sm" | "md";

interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: Variant;
  size?: Size;
}

const BASE =
  "inline-flex items-center justify-center gap-2 rounded-sm font-mono uppercase tracking-[0.08em] transition disabled:opacity-40 disabled:cursor-not-allowed focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-accent focus-visible:ring-offset-2 focus-visible:ring-offset-paper";

const VARIANT: Record<Variant, string> = {
  primary:
    "bg-accent text-paper hover:bg-accent-strong shadow-[0_0_24px_-8px_var(--color-accent-glow)]",
  secondary:
    "bg-surface text-ink border border-edge-strong hover:border-accent hover:text-accent",
  outline:
    "border border-edge-strong text-ink-soft hover:border-accent hover:text-accent",
  ghost: "text-ink-soft hover:text-ink hover:bg-surface",
};

const SIZE: Record<Size, string> = {
  sm: "h-8 px-3 text-[11px]",
  md: "h-9 px-4 text-xs",
};

export const Button = forwardRef<HTMLButtonElement, ButtonProps>(function Button(
  { variant = "primary", size = "md", className, ...rest },
  ref,
) {
  return (
    <button
      ref={ref}
      className={cn(BASE, VARIANT[variant], SIZE[size], className)}
      {...rest}
    />
  );
});
