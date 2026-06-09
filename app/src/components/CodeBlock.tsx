import { cn } from "./cn";

interface CodeBlockProps {
  children: React.ReactNode;
  className?: string;
}

export function CodeBlock({ children, className }: CodeBlockProps) {
  return (
    <pre
      className={cn(
        "thin-scroll overflow-x-auto rounded-md border border-edge bg-paper-warm p-3 font-mono text-xs leading-relaxed text-ink",
        className,
      )}
    >
      {children}
    </pre>
  );
}

interface InlineCodeProps {
  children: React.ReactNode;
}

export function InlineCode({ children }: InlineCodeProps) {
  return (
    <code className="rounded bg-paper-warm px-1.5 py-0.5 font-mono text-[0.85em] text-ink">
      {children}
    </code>
  );
}
