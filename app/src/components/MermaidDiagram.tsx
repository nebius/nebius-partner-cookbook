interface MermaidDiagramProps {
  source: string;
}

interface FlowNode {
  id: string;
  label: string;
}

interface FlowEdge {
  from: string;
  to: string;
}

const EDGE_RE = /^\s*([A-Za-z0-9_]+)(?:\[([^\]]+)])?\s*-->\s*([A-Za-z0-9_]+)(?:\[([^\]]+)])?\s*$/;

export function MermaidDiagram({ source }: MermaidDiagramProps) {
  const diagram = parseFlowchart(source);
  if (!diagram) {
    return (
      <pre className="thin-scroll my-6 overflow-x-auto border border-edge-strong bg-surface/60 p-4 font-mono text-[13px] leading-relaxed text-ink">
        <code>{source}</code>
      </pre>
    );
  }

  const path = orderNodes(diagram.nodes, diagram.edges);

  return (
    <figure className="my-8 overflow-x-auto border border-edge bg-surface/40 p-5">
      <div className="flex min-w-[920px] items-center gap-4">
        {path.map((node, index) => (
          <div key={node.id} className="flex items-center gap-4">
            <div className="min-w-36 border border-accent bg-paper-warm px-4 py-3 text-center text-[22px] leading-tight text-ink shadow-[inset_0_1px_0_rgba(255,255,255,0.05)]">
              {node.label}
            </div>
            {index < path.length - 1 ? (
              <div aria-hidden="true" className="flex items-center text-accent">
                <span className="h-px w-8 bg-accent" />
                <span className="-ml-1 text-2xl leading-none">{">"}</span>
              </div>
            ) : null}
          </div>
        ))}
      </div>
    </figure>
  );
}

function parseFlowchart(source: string): { nodes: FlowNode[]; edges: FlowEdge[] } | null {
  const lines = source
    .split("\n")
    .map((line) => line.trim())
    .filter(Boolean);

  if (!/^flowchart\s+LR$/i.test(lines[0] ?? "")) return null;

  const nodes = new Map<string, FlowNode>();
  const edges: FlowEdge[] = [];

  for (const line of lines.slice(1)) {
    const match = line.match(EDGE_RE);
    if (!match) return null;

    const [, from, fromLabel, to, toLabel] = match;
    if (!from || !to) return null;

    nodes.set(from, { id: from, label: fromLabel ?? nodes.get(from)?.label ?? from });
    nodes.set(to, { id: to, label: toLabel ?? nodes.get(to)?.label ?? to });
    edges.push({ from, to });
  }

  return { nodes: [...nodes.values()], edges };
}

function orderNodes(nodes: FlowNode[], edges: FlowEdge[]): FlowNode[] {
  const byId = new Map(nodes.map((node) => [node.id, node]));
  const targets = new Set(edges.map((edge) => edge.to));
  const start = nodes.find((node) => !targets.has(node.id)) ?? nodes[0];
  if (!start) return [];

  const ordered: FlowNode[] = [];
  const seen = new Set<string>();
  let current: FlowNode | undefined = start;

  while (current && !seen.has(current.id)) {
    ordered.push(current);
    seen.add(current.id);
    const next = edges.find((edge) => edge.from === current?.id);
    current = next ? byId.get(next.to) : undefined;
  }

  for (const node of nodes) {
    if (!seen.has(node.id)) ordered.push(node);
  }

  return ordered;
}
