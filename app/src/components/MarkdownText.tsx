"use client";

import ReactMarkdown, { type Components } from "react-markdown";
import remarkGfm from "remark-gfm";

const components: Components = {
  p: ({ children }) => <p className="my-2 leading-relaxed">{children}</p>,
  h1: ({ children }) => (
    <h3 className="mt-4 mb-2 font-display text-xl leading-tight text-ink">{children}</h3>
  ),
  h2: ({ children }) => (
    <h4 className="mt-4 mb-2 font-display text-lg leading-tight text-ink">{children}</h4>
  ),
  h3: ({ children }) => (
    <h5 className="mt-3 mb-1.5 font-mono text-[11px] uppercase tracking-[0.16em] text-accent">
      {children}
    </h5>
  ),
  h4: ({ children }) => (
    <h6 className="mt-3 mb-1.5 font-mono text-[11px] uppercase tracking-[0.14em] text-ink-soft">
      {children}
    </h6>
  ),
  ul: ({ children }) => <ul className="my-2 list-disc space-y-1 pl-5">{children}</ul>,
  ol: ({ children }) => <ol className="my-2 list-decimal space-y-1 pl-5">{children}</ol>,
  li: ({ children }) => <li className="leading-relaxed">{children}</li>,
  a: ({ href, children }) => (
    <a
      href={href ?? "#"}
      target={href?.startsWith("http") ? "_blank" : undefined}
      rel={href?.startsWith("http") ? "noreferrer" : undefined}
      className="text-accent underline decoration-accent/40 underline-offset-2 hover:decoration-accent"
    >
      {children}
    </a>
  ),
  blockquote: ({ children }) => (
    <blockquote className="my-3 border-l-2 border-accent/60 pl-3 italic text-ink-soft">
      {children}
    </blockquote>
  ),
  code: ({ className, children }) => {
    // Fenced blocks come wrapped in <pre>; inline code does not.
    if (className) return <code className={className}>{children}</code>;
    return (
      <code className="border border-edge bg-surface px-1 py-0.5 font-mono text-[0.86em] text-accent">
        {children}
      </code>
    );
  },
  pre: ({ children }) => (
    <pre className="thin-scroll my-3 overflow-x-auto border border-edge bg-surface/60 p-3 font-mono text-[12.5px] leading-relaxed text-ink">
      {children}
    </pre>
  ),
  table: ({ children }) => (
    <div className="thin-scroll my-3 overflow-x-auto border border-edge">
      <table className="w-full border-collapse text-sm">{children}</table>
    </div>
  ),
  th: ({ children }) => (
    <th className="border-b border-edge-strong bg-surface/50 px-3 py-1.5 text-left font-mono text-[10px] uppercase tracking-[0.14em] text-ink-soft">
      {children}
    </th>
  ),
  td: ({ children }) => (
    <td className="border-b border-edge px-3 py-1.5 align-top">{children}</td>
  ),
  hr: () => <hr className="my-4 border-edge" />,
  strong: ({ children }) => <strong className="font-medium text-ink">{children}</strong>,
  em: ({ children }) => <em className="italic">{children}</em>,
};

export function MarkdownText({ source }: { source: string }) {
  return (
    <ReactMarkdown remarkPlugins={[remarkGfm]} components={components}>
      {source}
    </ReactMarkdown>
  );
}
