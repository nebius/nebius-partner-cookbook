import { forwardRef } from "react";
import { cn } from "./cn";

const FIELD_BASE =
  "w-full border border-edge-strong bg-paper px-3 py-2 font-mono text-sm text-ink placeholder:text-ink-dim focus-visible:outline-none focus-visible:border-accent focus-visible:ring-1 focus-visible:ring-accent/30";

export const Input = forwardRef<HTMLInputElement, React.InputHTMLAttributes<HTMLInputElement>>(
  function Input({ className, ...rest }, ref) {
    return <input ref={ref} className={cn(FIELD_BASE, className)} {...rest} />;
  },
);

export const Textarea = forwardRef<HTMLTextAreaElement, React.TextareaHTMLAttributes<HTMLTextAreaElement>>(
  function Textarea({ className, ...rest }, ref) {
    return (
      <textarea
        ref={ref}
        className={cn(FIELD_BASE, "min-h-[80px] resize-y leading-relaxed", className)}
        {...rest}
      />
    );
  },
);

interface FieldProps {
  label: string;
  hint?: string;
  htmlFor?: string;
  children: React.ReactNode;
}

export function Field({ label, hint, htmlFor, children }: FieldProps) {
  return (
    <label htmlFor={htmlFor} className="block space-y-2">
      <span className="block font-mono text-[10px] uppercase tracking-[0.16em] text-ink-soft">
        {label}
      </span>
      {children}
      {hint ? (
        <span className="block font-mono text-[11px] text-ink-dim">{hint}</span>
      ) : null}
    </label>
  );
}
