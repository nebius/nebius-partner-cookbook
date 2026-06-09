import Link from "next/link";
import { Children, isValidElement } from "react";
import type { MDXComponents } from "mdx/types";
import { cn } from "./cn";
import { MermaidDiagram } from "./MermaidDiagram";

/**
 * MDX → React element overrides for cookbook README rendering.
 *
 * Editorial-technical hybrid: Instrument Serif display headings (matching the
 * page chrome), Plex Sans body, Plex Mono for inline code and fenced blocks.
 * Hairline rules separate sections; no @tailwindcss/typography needed.
 */
export const mdxComponents: MDXComponents = {
  h1: ({ children, ...rest }) => (
    <h2
      className="mt-16 mb-6 border-t border-edge pt-10 font-display text-5xl leading-[0.95] tracking-[0.01em] text-ink"
      {...rest}
    >
      {children}
    </h2>
  ),
  h2: ({ children, ...rest }) => (
    <h2
      className="mt-16 mb-6 border-t border-edge pt-10 font-display text-5xl leading-[0.95] tracking-[0.01em] text-ink"
      {...rest}
    >
      {children}
    </h2>
  ),
  h3: ({ children, ...rest }) => (
    <h3
      className="mt-10 mb-3 font-display text-3xl leading-none tracking-[0.01em] text-ink"
      {...rest}
    >
      {children}
    </h3>
  ),
  h4: ({ children, ...rest }) => (
    <h4
      className="mt-8 mb-2 font-mono text-[11px] uppercase tracking-[0.18em] text-accent"
      {...rest}
    >
      {children}
    </h4>
  ),
  p: ({ children }) => (
    <p className="my-5 text-[16px] leading-[1.7] text-ink-soft">{children}</p>
  ),
  a: ({ href, children, ...rest }) => {
    const target = href ?? "#";
    const isInternal = target.startsWith("/") && !target.startsWith("//");
    const className =
      "text-accent underline decoration-accent/30 decoration-1 underline-offset-[3px] transition hover:decoration-accent";
    if (isInternal) {
      return (
        <Link href={target} className={className}>
          {children}
        </Link>
      );
    }
    return (
      <a
        href={target}
        target={target.startsWith("http") ? "_blank" : undefined}
        rel={target.startsWith("http") ? "noreferrer" : undefined}
        className={className}
        {...rest}
      >
        {children}
      </a>
    );
  },
  ul: ({ children }) => (
    <ul className="my-5 space-y-2 pl-0 text-[16px] leading-[1.7] text-ink-soft">{children}</ul>
  ),
  ol: ({ children }) => (
    <ol className="my-5 list-decimal space-y-2 pl-6 text-[16px] leading-[1.7] text-ink-soft marker:font-mono marker:text-xs marker:text-ink-dim">
      {children}
    </ol>
  ),
  li: ({ children }) => (
    <li className="relative pl-6 before:absolute before:left-0 before:top-[0.6em] before:h-px before:w-3 before:bg-edge-strong">
      {children}
    </li>
  ),
  blockquote: ({ children }) => (
    <blockquote className="my-8 border-l border-accent pl-5 text-lg italic leading-snug text-ink">
      {children}
    </blockquote>
  ),
  hr: () => <hr className="my-12 border-edge" />,
  code: ({ children, className }) => {
    if (className) return <code className={className}>{children}</code>;
    return (
      <code className="border border-edge bg-surface px-1.5 py-0.5 font-mono text-[0.86em] text-accent">
        {children}
      </code>
    );
  },
  pre: ({ children, ...rest }) => {
    const child = Children.toArray(children)[0];
    if (isValidElement<{ className?: string; children?: React.ReactNode }>(child)) {
      const className = child.props.className ?? "";
      if (className.split(/\s+/).includes("language-mermaid")) {
        return <MermaidDiagram source={extractText(child.props.children)} />;
      }
    }

    return (
      <pre
        className="thin-scroll my-6 overflow-x-auto border border-edge-strong bg-surface/60 p-4 font-mono text-[13px] leading-relaxed text-ink shadow-[inset_0_1px_0_rgba(255,255,255,0.02)]"
        {...rest}
      >
        {children}
      </pre>
    );
  },
  table: ({ children }) => (
    <div className="thin-scroll my-8 overflow-x-auto border border-edge">
      <table className="w-full border-collapse text-sm">{children}</table>
    </div>
  ),
  thead: ({ children }) => (
    <thead className="border-b border-edge-strong bg-surface/50">{children}</thead>
  ),
  th: ({ children, className }) => (
    <th
      className={cn(
        "px-4 py-2.5 text-left font-mono text-[10px] uppercase tracking-[0.16em] text-ink-soft",
        className,
      )}
    >
      {children}
    </th>
  ),
  td: ({ children, className }) => (
    <td className={cn("border-b border-edge px-4 py-2.5 align-top text-ink-soft", className)}>
      {children}
    </td>
  ),
  strong: ({ children }) => <strong className="font-medium text-ink">{children}</strong>,
  em: ({ children }) => <em className="italic text-ink">{children}</em>,
};

function extractText(value: React.ReactNode): string {
  return Children.toArray(value)
    .map((child) => (typeof child === "string" || typeof child === "number" ? String(child) : ""))
    .join("")
    .trim();
}
