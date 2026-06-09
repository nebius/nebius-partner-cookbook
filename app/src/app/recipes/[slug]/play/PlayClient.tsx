"use client";

import Link from "next/link";
import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import {
  ArrowLeft,
  ChevronDown,
  ChevronUp,
  PanelRight,
  PanelRightClose,
  Send,
  Settings,
  Square,
} from "lucide-react";
import { Badge, Button, Field, Input, NebiusLogo, Textarea, cn } from "@/components";
import { MarkdownText } from "@/components/MarkdownText";
import { streamAgent, type SseEvent } from "@/lib/sse";

interface Props {
  slug: string;
  title: string;
  tagline: string;
}

interface ChatTurn {
  id: string;
  role: "user" | "assistant";
  text: string;
  events: SseEvent[];
  status: "streaming" | "done" | "error" | "cancelled";
  startedAt: number;
}

interface RunStats {
  route?: string;
  contextNeed?: string;
  elapsedSeconds?: number;
  inputTokens: number;
  outputTokens: number;
  costUsd?: number;
  estimated: boolean;
}

const DEFAULT_AGENT_URL = "http://localhost:8000";
const DEFAULT_AGENT_URL_BY_SLUG: Partial<Record<string, string>> = {
  "first-agent-on-nebius": "https://nebius-partners-cookbook-one.cleverapps.io",
  "domain-knowledge-pinecone-nexus": "https://nebius-partners-cookbook-two.cleverapps.io",
  "real-time-data-tavily": "https://nebius-partners-cookbook-three.cleverapps.io",
  "stronger-agents-langchain-langgraph": "https://nebius-partners-cookbook-four.cleverapps.io",
};
const STORAGE_KEY = (slug: string) => `nebius-cookbook:agent-url:${slug}`;
const THREAD_STORAGE_KEY = (slug: string) => `nebius-cookbook:thread-id:${slug}`;
const USER_STORAGE_KEY = (slug: string) => `nebius-cookbook:user-id:${slug}`;

function isLocalFrontend(): boolean {
  if (typeof window === "undefined") return false;
  return ["localhost", "127.0.0.1", "::1"].includes(window.location.hostname);
}

function defaultAgentUrl(slug: string): string {
  if (isLocalFrontend()) return DEFAULT_AGENT_URL;
  return DEFAULT_AGENT_URL_BY_SLUG[slug] ?? DEFAULT_AGENT_URL;
}

function newId(): string {
  return crypto.randomUUID();
}

function fmtTime(ts: number): string {
  const d = new Date(ts);
  return d.toLocaleTimeString("en-US", { hour12: false, hour: "2-digit", minute: "2-digit", second: "2-digit" });
}

const SAMPLE_PROMPTS = [
  "What is Nebius AgentKit in one paragraph?",
  "Explain Server-Sent Events to me like I write API clients.",
  "Compare async streaming and polling for LLM responses.",
];

const BOOK_RECOMMENDER_PROMPTS = [
  "Recommend books about found family and high-stakes adventure for someone who liked Dune.",
  "I just read The Left Hand of Darkness. What should I read next?",
  "Find thoughtful books about climate, power, and social collapse.",
];

const TAVILY_BOOK_PROMPTS = [
  "Find cozy fantasy books launched after 2021 with recent review context.",
  "Recommend recent climate fiction and cite current reviews or awards context.",
  "Find recent editions or formats for books about space exploration.",
];

const ORCHESTRATION_PROMPTS = [
  "I loved Station Eleven and Sea of Tranquility. What should I read next if I want recent literary sci-fi with a hopeful tone?",
  "What is the latest book written by Michel Houellebecq?",
  "Recommend recent climate fiction with enough context to explain why each book is worth reading now.",
];

const ACTION_PROMPTS = [
  "Recommend one short science-fiction book, then create a checkout link for it.",
  "I want to buy The Nebius Cloud Atlas.",
  "Create a payment link for Pinecones in the Vector Garden.",
];

export function PlayClient({ slug, title, tagline }: Props) {
  const [agentUrl, setAgentUrl] = useState(() => defaultAgentUrl(slug));
  const [threadId, setThreadId] = useState("demo-thread");
  const [userId, setUserId] = useState("demo-user");
  const [draft, setDraft] = useState("");
  const [turns, setTurns] = useState<ChatTurn[]>([]);
  const [isStreaming, setIsStreaming] = useState(false);
  const [settingsOpen, setSettingsOpen] = useState(false);
  const [sidebarOpen, setSidebarOpen] = useState(true);
  const [headerExpanded, setHeaderExpanded] = useState(true);
  const abortRef = useRef<AbortController | null>(null);
  const transcriptRef = useRef<HTMLDivElement | null>(null);
  const textareaRef = useRef<HTMLTextAreaElement | null>(null);

  useEffect(() => {
    const stored = window.localStorage.getItem(STORAGE_KEY(slug));
    setAgentUrl(stored || defaultAgentUrl(slug));
    const storedThreadId = window.localStorage.getItem(THREAD_STORAGE_KEY(slug));
    if (storedThreadId) setThreadId(storedThreadId);
    const storedUserId = window.localStorage.getItem(USER_STORAGE_KEY(slug));
    if (storedUserId) setUserId(storedUserId);
  }, [slug]);

  const persistAgentUrl = useCallback(
    (next: string) => {
      setAgentUrl(next);
      window.localStorage.setItem(STORAGE_KEY(slug), next);
    },
    [slug],
  );

  const persistThreadId = useCallback(
    (next: string) => {
      setThreadId(next);
      window.localStorage.setItem(THREAD_STORAGE_KEY(slug), next);
    },
    [slug],
  );

  const persistUserId = useCallback(
    (next: string) => {
      setUserId(next);
      window.localStorage.setItem(USER_STORAGE_KEY(slug), next);
    },
    [slug],
  );

  useEffect(() => {
    if (transcriptRef.current) {
      transcriptRef.current.scrollTop = transcriptRef.current.scrollHeight;
    }
  }, [turns]);

  // Collapse the header chrome the moment the conversation begins.
  useEffect(() => {
    if (turns.length > 0 && headerExpanded) setHeaderExpanded(false);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [turns.length === 0]);

  const runStats = useMemo(() => latestRunStats(turns), [turns]);

  const cancel = useCallback(() => {
    abortRef.current?.abort();
  }, []);

  const decideApproval = useCallback(
    async (turnId: string, approvalId: string, decision: "approve" | "reject") => {
      const target = `${agentUrl.replace(/\/$/, "")}/approvals/${encodeURIComponent(approvalId)}`;
      try {
        const res = await fetch(target, {
          method: "POST",
          headers: { "content-type": "application/json" },
          body: JSON.stringify({ decision }),
        });
        const body = (await res.json().catch(() => ({}))) as Record<string, unknown>;
        const event: SseEvent = {
          name: "approval_result",
          data: {
            approvalId,
            decision,
            ok: res.ok,
            ...body,
          },
        };
        setTurns((items) =>
          items.map((turn) =>
            turn.id === turnId ? { ...turn, events: [...turn.events, event] } : turn,
          ),
        );
      } catch (err) {
        const message =
          err instanceof Error ? err.message : typeof err === "string" ? err : "approval failed";
        const event: SseEvent = {
          name: "approval_result",
          data: { approvalId, decision, ok: false, message },
        };
        setTurns((items) =>
          items.map((turn) =>
            turn.id === turnId ? { ...turn, events: [...turn.events, event] } : turn,
          ),
        );
      }
    },
    [agentUrl],
  );

  const send = useCallback(
    async (overridePrompt?: string) => {
      const prompt = (overridePrompt ?? draft).trim();
      if (!prompt || isStreaming) return;
      if (!overridePrompt) setDraft("");

      const now = Date.now();
      const userTurn: ChatTurn = {
        id: newId(),
        role: "user",
        text: prompt,
        events: [],
        status: "done",
        startedAt: now,
      };
      const assistantTurn: ChatTurn = {
        id: newId(),
        role: "assistant",
        text: "",
        events: [],
        status: "streaming",
        startedAt: now,
      };
      setTurns((t) => [...t, userTurn, assistantTurn]);
      setIsStreaming(true);

      const controller = new AbortController();
      abortRef.current = controller;
      const target = `${agentUrl.replace(/\/$/, "")}/agent/run`;

      const history = turns
        .filter((t) => t.status === "done" && t.text)
        .map((t) => ({ role: t.role, content: t.text }));

      try {
        for await (const event of streamAgent({
          url: target,
          body: { prompt, history, thread_id: threadId, user_id: userId },
          signal: controller.signal,
        })) {
          setTurns((t) => {
            const copy = [...t];
            const last = copy[copy.length - 1];
            if (!last || last.id !== assistantTurn.id) return t;
            const next: ChatTurn = { ...last, events: [...last.events, event] };
            if (event.name === "token" || event.name === "answer") {
              const piece = typeof event.data.text === "string" ? event.data.text : "";
              next.text = event.name === "answer" ? piece : last.text + piece;
            }
            if (event.name === "done") next.status = "done";
            if (event.name === "error") next.status = "error";
            copy[copy.length - 1] = next;
            return copy;
          });
        }
        setTurns((t) => {
          const copy = [...t];
          const last = copy[copy.length - 1];
          if (last && last.status === "streaming") {
            copy[copy.length - 1] = { ...last, status: "done" };
          }
          return copy;
        });
      } catch (err) {
        const cancelled = controller.signal.aborted;
        const message =
          err instanceof Error ? err.message : typeof err === "string" ? err : "unknown error";
        setTurns((t) => {
          const copy = [...t];
          const last = copy[copy.length - 1];
          if (!last) return t;
          copy[copy.length - 1] = {
            ...last,
            status: cancelled ? "cancelled" : "error",
            text: last.text || (cancelled ? "(cancelled)" : `(error) ${message}`),
          };
          return copy;
        });
      } finally {
        abortRef.current = null;
        setIsStreaming(false);
        textareaRef.current?.focus();
      }
    },
    [agentUrl, draft, isStreaming, threadId, turns, userId],
  );

  return (
    <div className="fixed inset-0 flex h-dvh w-screen overflow-hidden bg-paper">
      <FloatingHeader
        slug={slug}
        title={title}
        tagline={tagline}
        expanded={headerExpanded}
        onToggle={() => setHeaderExpanded((v) => !v)}
        sidebarOpen={sidebarOpen}
        onToggleSidebar={() => setSidebarOpen((v) => !v)}
        agentUrl={agentUrl}
        isStreaming={isStreaming}
        onOpenSettings={() => {
          setSidebarOpen(true);
          setSettingsOpen(true);
        }}
      />

      {/* Transcript column */}
      <section className="flex min-w-0 flex-1 flex-col">
        <div ref={transcriptRef} className="thin-scroll flex-1 overflow-y-auto" aria-live="polite">
          <div className="mx-auto max-w-3xl space-y-8 px-6 pt-36 pb-8">
            {turns.length === 0 ? (
              <EmptyState slug={slug} onPick={(prompt) => send(prompt)} />
            ) : (
              turns.map((t) => (
                <Turn
                  key={t.id}
                  turn={t}
                  slug={slug}
                  onApprovalDecision={decideApproval}
                />
              ))
            )}
          </div>
        </div>

        <div className="border-t border-edge bg-paper/80 backdrop-blur-md">
          <div className="mx-auto max-w-3xl px-6 py-4">
            <Composer
              value={draft}
              onChange={setDraft}
              onSend={() => send()}
              onCancel={cancel}
              isStreaming={isStreaming}
              textareaRef={textareaRef}
            />
            <div className="mt-2 flex items-center justify-between font-mono text-[10px] uppercase tracking-[0.14em] text-ink-dim">
              <span>↵ send · shift+↵ newline</span>
              <BottomRunStats stats={runStats} isStreaming={isStreaming} />
            </div>
          </div>
        </div>
      </section>

      {sidebarOpen ? (
        <Sidebar
          turns={turns}
          settingsOpen={settingsOpen}
          onToggleSettings={() => setSettingsOpen((v) => !v)}
          agentUrl={agentUrl}
          onAgentUrlChange={persistAgentUrl}
          slug={slug}
          threadId={threadId}
          onThreadIdChange={persistThreadId}
          userId={userId}
          onUserIdChange={persistUserId}
        />
      ) : null}
    </div>
  );
}

function BottomRunStats({
  stats,
  isStreaming,
}: {
  stats: RunStats | null;
  isStreaming: boolean;
}) {
  if (!stats) return <span>{isStreaming ? "▸ stream open" : "○ idle"}</span>;

  const route = stats.contextNeed ?? stats.route ?? "route pending";
  const time = typeof stats.elapsedSeconds === "number" ? `${stats.elapsedSeconds.toFixed(2)}s` : "…";
  const cost =
    typeof stats.costUsd === "number" ? `$${stats.costUsd.toFixed(6)}` : stats.estimated ? "est. n/a" : "n/a";
  const prefix = isStreaming || stats.estimated ? "est." : "run";

  return (
    <span className="min-w-0 truncate text-right">
      {prefix} {route} · {time} · {stats.inputTokens} in / {stats.outputTokens} out · {cost}
    </span>
  );
}

/* ── header ──────────────────────────────────────────────────────────────── */

function FloatingHeader({
  slug,
  title,
  tagline,
  expanded,
  onToggle,
  sidebarOpen,
  onToggleSidebar,
  agentUrl,
  isStreaming,
  onOpenSettings,
}: {
  slug: string;
  title: string;
  tagline: string;
  expanded: boolean;
  onToggle: () => void;
  sidebarOpen: boolean;
  onToggleSidebar: () => void;
  agentUrl: string;
  isStreaming: boolean;
  onOpenSettings: () => void;
}) {
  const host = useMemo(() => {
    try {
      return new URL(agentUrl).host;
    } catch {
      return agentUrl;
    }
  }, [agentUrl]);

  return (
    <header className="pointer-events-none absolute inset-x-0 top-0 z-20 flex justify-center px-4 pt-4">
      <div
        className={cn(
          "pointer-events-auto w-full max-w-5xl border border-edge-strong bg-paper/80 backdrop-blur-xl",
          "shadow-[0_24px_48px_-24px_rgba(0,0,0,0.6)]",
        )}
      >
        {/* Command bar */}
        <div className="flex items-center gap-2 px-3 py-2.5">
          <Link
            href="/"
            className="inline-flex items-center pr-1"
            title="Agent Blueprint Recipes"
          >
            <NebiusLogo height={18} />
          </Link>

          <span className="font-mono text-[11px] text-ink-dim">/</span>

          <Link
            href={`/recipes/${slug}`}
            className="inline-flex items-center gap-1.5 px-1 py-1 font-mono text-[11px] uppercase tracking-[0.12em] text-ink-soft transition hover:text-accent"
          >
            <ArrowLeft className="size-3" />
            recipes
          </Link>

          <span className="font-mono text-[11px] text-ink-dim">/</span>

          <span className="font-mono text-[11px] uppercase tracking-[0.12em] text-ink truncate">
            {slug}
          </span>

          <div className="ml-auto flex items-center gap-1">
            <button
              type="button"
              onClick={onOpenSettings}
              className="group inline-flex items-center gap-2 border border-edge px-2 py-1 font-mono text-[10px] uppercase tracking-[0.14em] text-ink-soft transition hover:border-accent hover:text-accent"
              title="Configure agent endpoint"
            >
              <span
                className={cn(
                  "size-1.5 rounded-full",
                  isStreaming ? "bg-accent phosphor-dot" : "bg-ink-dim",
                )}
                aria-hidden
              />
              {host}
            </button>

            <button
              type="button"
              onClick={onToggleSidebar}
              aria-label={sidebarOpen ? "Hide event log" : "Show event log"}
              className="ml-1 inline-flex size-8 items-center justify-center border border-transparent text-ink-soft transition hover:border-edge hover:text-ink"
            >
              {sidebarOpen ? (
                <PanelRightClose className="size-4" />
              ) : (
                <PanelRight className="size-4" />
              )}
            </button>

            <button
              type="button"
              onClick={onToggle}
              aria-label={expanded ? "Collapse header" : "Expand header"}
              className="inline-flex size-8 items-center justify-center border border-transparent text-ink-soft transition hover:border-edge hover:text-ink"
            >
              {expanded ? <ChevronUp className="size-4" /> : <ChevronDown className="size-4" />}
            </button>
          </div>
        </div>

        {/* Expanded body — title + tagline */}
        <div
          className={cn(
            "grid overflow-hidden border-t border-edge/0 transition-all duration-300 ease-out",
            expanded ? "grid-rows-[1fr] border-t-edge" : "grid-rows-[0fr]",
          )}
        >
          <div className="min-h-0 overflow-hidden">
            <div className="px-5 py-5">
              <h1 className="font-display text-5xl leading-[0.9] tracking-[0.01em] text-ink sm:text-6xl">
                {title}
              </h1>
              <p className="mt-2 max-w-2xl text-base italic leading-snug text-ink-soft sm:text-lg">
                {tagline}
              </p>
            </div>
          </div>
        </div>
      </div>
    </header>
  );
}

/* ── transcript ──────────────────────────────────────────────────────────── */

function Turn({
  turn,
  slug,
  onApprovalDecision,
}: {
  turn: ChatTurn;
  slug: string;
  onApprovalDecision: (turnId: string, approvalId: string, decision: "approve" | "reject") => void;
}) {
  if (turn.role === "user") {
    return (
      <div className="flex flex-col items-end gap-1.5">
        <span className="font-mono text-[10px] uppercase tracking-[0.16em] text-ink-dim">
          you · {fmtTime(turn.startedAt)}
        </span>
        <div className="max-w-[85%] border border-accent/40 bg-accent-soft px-4 py-2.5 text-[15px] leading-relaxed text-ink">
          {turn.text}
        </div>
      </div>
    );
  }

  const phase = latestStatusPhase(turn.events);
  const statusLabel =
    turn.status === "streaming" ? (phase ?? "thinking") : turn.status === "done" ? "ready" : turn.status;
  const tone: "accent" | "warn" | "critical" =
    turn.status === "error"
      ? "critical"
      : turn.status === "cancelled"
        ? "warn"
        : "accent";
  const rendered = splitMetricsFooter(turn.text);
  const reasoningMessages = agentMessages(turn.events);
  const approval = slug === "actions-with-mcp-stripe" ? latestApproval(turn.events) : null;
  const approvalResult = approval ? latestApprovalResult(turn.events, approval.approvalId) : null;

  return (
    <div className="space-y-1.5">
      <div className="flex items-center gap-2">
        <span className="font-mono text-[10px] uppercase tracking-[0.16em] text-ink-dim">
          agent · {fmtTime(turn.startedAt)}
        </span>
        <Badge tone={tone} bracket>
          {statusLabel}
        </Badge>
        {turn.status === "streaming" ? (
          <span className="size-1.5 rounded-full bg-accent phosphor-dot" aria-hidden />
        ) : null}
      </div>
      <div className="relative">
        <div
          className="absolute left-0 top-0 h-full w-px bg-edge-strong"
          aria-hidden
        />
        <div className="pl-5 text-[15px] leading-relaxed text-ink">
          {reasoningMessages.length > 0 ? (
            <ReasoningTrace messages={reasoningMessages} active={turn.status === "streaming"} />
          ) : null}
          {turn.text ? (
            <>
              <MarkdownText source={rendered.body} />
              {approval ? (
                <ApprovalCard
                  turnId={turn.id}
                  approval={approval}
                  result={approvalResult}
                  onDecision={onApprovalDecision}
                />
              ) : null}
              {rendered.metrics ? (
                <div className="mt-4 border-t border-edge/70 pt-2 font-mono text-[11px] leading-relaxed text-ink-dim">
                  {rendered.metrics}
                </div>
              ) : null}
            </>
          ) : (
            <span className="font-mono text-sm text-ink-dim">
              {turn.status === "streaming" ? "▌" : "(no response)"}
            </span>
          )}
        </div>
      </div>
    </div>
  );
}

function ReasoningTrace({ messages, active }: { messages: string[]; active: boolean }) {
  return (
    <div className="mb-4 border border-edge bg-surface/30 px-3 py-2.5">
      <div className="mb-1.5 flex items-center gap-2 font-mono text-[10px] uppercase tracking-[0.16em] text-ink-dim">
        <span
          className={cn("size-1.5 rounded-full", active ? "bg-accent phosphor-dot" : "bg-ink-dim")}
          aria-hidden
        />
        reasoning
      </div>
      <div className="space-y-1 font-mono text-[11px] leading-relaxed text-ink-soft">
        {messages.map((message, index) => (
          <div
            key={`${index}-${message}`}
            className={cn(
              "flex gap-2",
              active && index === messages.length - 1 ? "text-accent token-fade" : null,
            )}
          >
            <span className="text-ink-dim">{index + 1}</span>
            <span>{message}</span>
          </div>
        ))}
      </div>
    </div>
  );
}

function splitMetricsFooter(text: string): { body: string; metrics: string | null } {
  const match = text.match(/\n\n---\n(Time: .*)$/s);
  if (!match) return { body: text, metrics: null };
  return {
    body: text.slice(0, match.index).trimEnd(),
    metrics: match[1] ?? null,
  };
}

function agentMessages(events: SseEvent[]): string[] {
  return events
    .filter((event) => event.name === "agent_message")
    .map((event) => (typeof event.data.text === "string" ? event.data.text : ""))
    .filter(Boolean);
}

/* ── composer ────────────────────────────────────────────────────────────── */

function Composer({
  value,
  onChange,
  onSend,
  onCancel,
  isStreaming,
  textareaRef,
}: {
  value: string;
  onChange: (v: string) => void;
  onSend: () => void;
  onCancel: () => void;
  isStreaming: boolean;
  textareaRef: React.MutableRefObject<HTMLTextAreaElement | null>;
}) {
  return (
    <form
      onSubmit={(e) => {
        e.preventDefault();
        onSend();
      }}
      className="relative"
    >
      <div className="group relative border border-edge-strong bg-surface/70 focus-within:border-accent focus-within:shadow-[0_0_0_1px_var(--color-accent),0_0_32px_-8px_var(--color-accent-glow)]">
        <span
          aria-hidden
          className="pointer-events-none absolute left-3 top-3 select-none font-mono text-xs text-accent"
        >
          ▸
        </span>
        <Textarea
          ref={textareaRef}
          value={value}
          onChange={(e) => onChange(e.target.value)}
          placeholder="prompt the agent…"
          rows={2}
          onKeyDown={(e) => {
            if (e.key === "Enter" && !e.shiftKey) {
              e.preventDefault();
              onSend();
            }
          }}
          disabled={isStreaming}
          className="min-h-[64px] resize-none border-0 bg-transparent pl-9 pr-32 focus-visible:ring-0"
        />
        <div className="absolute bottom-2 right-2 flex items-center gap-2">
          {isStreaming ? (
            <Button type="button" variant="secondary" size="sm" onClick={onCancel}>
              <Square className="size-3" /> stop
            </Button>
          ) : (
            <Button type="submit" size="sm" disabled={!value.trim()}>
              send <Send className="size-3" />
            </Button>
          )}
        </div>
      </div>
    </form>
  );
}

/* ── empty state ─────────────────────────────────────────────────────────── */

function EmptyState({ slug, onPick }: { slug: string; onPick: (prompt: string) => void }) {
  const isStaticBookRecommender = slug === "domain-knowledge-pinecone-nexus";
  const isFreshBookRecommender = slug === "real-time-data-tavily";
  const isOrchestrationAgent = slug === "stronger-agents-langchain-langgraph";
  const isActionAgent = slug === "actions-with-mcp-stripe";
  const isBookRecommender = isStaticBookRecommender || isFreshBookRecommender;
  const prompts = isFreshBookRecommender
    ? TAVILY_BOOK_PROMPTS
    : isStaticBookRecommender
      ? BOOK_RECOMMENDER_PROMPTS
      : isOrchestrationAgent
        ? ORCHESTRATION_PROMPTS
        : isActionAgent
          ? ACTION_PROMPTS
          : SAMPLE_PROMPTS;

  return (
    <div className="flex min-h-[44dvh] flex-col items-center justify-center text-center">
      <div className="max-w-md space-y-4">
        <Badge bracket>session ready</Badge>
        <h2 className="font-display text-5xl leading-none tracking-[0.01em] text-ink">
          {isBookRecommender
            ? "📚 A book recommender for your agent."
            : isOrchestrationAgent
              ? "A book-agent routing console."
              : isActionAgent
                ? "A book-action approval console."
              : "A console for your agent."}
        </h2>
        <p className="font-mono text-[12px] leading-relaxed text-ink-soft">
          {isBookRecommender ? (
            <>
              Ask for books by topic, author, year, or after a recent read.
              <br />
              {isFreshBookRecommender
                ? "Pinecone supplies knowledge candidates; Tavily adds fresh web context."
                : "Pinecone supplies knowledge candidates; Nebius synthesizes the shortlist."}
            </>
          ) : isOrchestrationAgent ? (
            <>
              Watch LangGraph choose a route before Nebius streams tokens.
              <br />
              Try recommendations, latest-book questions, or prompts that need both taste and freshness.
            </>
          ) : isActionAgent ? (
            <>
              Ask for a fictional book checkout link.
              <br />
              The agent must wait for approval before Stripe MCP is called.
            </>
          ) : (
            <>
              POST <span className="text-accent">/agent/run</span> on your local cookbook.
              <br />
              Every SSE event arrives here — token, status, sources, errors.
            </>
          )}
        </p>
      </div>

      <div className="mt-10 w-full max-w-md space-y-2">
        <span className="block font-mono text-[10px] uppercase tracking-[0.18em] text-ink-dim">
          try
        </span>
        <div className="space-y-1.5">
          {prompts.map((p) => (
            <button
              key={p}
              type="button"
              onClick={() => onPick(p)}
              className="group flex w-full items-center gap-3 border border-edge bg-surface/40 px-3 py-2.5 text-left transition hover:border-accent/60 hover:bg-surface"
            >
              <span className="font-mono text-[10px] uppercase tracking-[0.16em] text-ink-dim group-hover:text-accent">
                ▸
              </span>
              <span className="text-sm text-ink-soft group-hover:text-ink">{p}</span>
            </button>
          ))}
        </div>
      </div>
    </div>
  );
}

/* ── sidebar ─────────────────────────────────────────────────────────────── */

function Sidebar({
  slug,
  turns,
  settingsOpen,
  onToggleSettings,
  agentUrl,
  onAgentUrlChange,
  threadId,
  onThreadIdChange,
  userId,
  onUserIdChange,
}: {
  slug: string;
  turns: ChatTurn[];
  settingsOpen: boolean;
  onToggleSettings: () => void;
  agentUrl: string;
  onAgentUrlChange: (v: string) => void;
  threadId: string;
  onThreadIdChange: (v: string) => void;
  userId: string;
  onUserIdChange: (v: string) => void;
}) {
  // Build a chronological log of every event across every assistant turn,
  // with turn separators inserted between them. Tokens stay out (they're
  // rendered as message text). Heartbeats stay in — they're useful evidence
  // that the SSE channel is alive when no other events fire.
  const logEntries = useMemo<LogEntry[]>(() => {
    const out: LogEntry[] = [];
    let turnIdx = 0;
    for (const turn of turns) {
      if (turn.role !== "assistant") continue;
      turnIdx++;
      out.push({
        kind: "separator",
        turnIdx,
        ts: turn.startedAt,
        key: `sep-${turn.id}`,
      });
      for (let i = 0; i < turn.events.length; i++) {
        const ev = turn.events[i]!;
        if (ev.name === "token") continue;
        out.push({ kind: "event", event: ev, key: `ev-${turn.id}-${i}` });
      }
    }
    return out;
  }, [turns]);

  const visibleEventCount = logEntries.filter((e) => e.kind === "event").length;

  // Sources: take from the latest assistant turn that produced any.
  const sources = useMemo<Source[]>(() => {
    for (let i = turns.length - 1; i >= 0; i--) {
      const t = turns[i];
      if (!t || t.role !== "assistant") continue;
      const s = extractSources(t.events);
      if (s.length > 0) return s;
    }
    return [];
  }, [turns]);

  // Autoscroll the event log to the bottom on new entries.
  const logRef = useRef<HTMLDivElement | null>(null);
  useEffect(() => {
    if (logRef.current) {
      logRef.current.scrollTop = logRef.current.scrollHeight;
    }
  }, [logEntries.length]);

  return (
    <aside className="hidden w-[380px] shrink-0 flex-col border-l border-edge bg-paper-warm/60 md:flex">
      <div className="thin-scroll flex-1 overflow-y-auto pt-36">
        <div className="space-y-6 px-5 pb-8">
          <SidebarSection
            title="settings"
            badge={settingsOpen ? "open" : undefined}
            action={
              <button
                type="button"
                onClick={onToggleSettings}
                className="font-mono text-[10px] uppercase tracking-[0.14em] text-ink-soft transition hover:text-accent"
              >
                <Settings className="inline size-3" />
              </button>
            }
          >
            {settingsOpen ? (
              <div className="space-y-3 pt-2">
                <Field label="agent url" hint="Stored per recipe in localStorage.">
                  <Input
                    value={agentUrl}
                    onChange={(e) => onAgentUrlChange(e.target.value)}
                    spellCheck={false}
                    autoComplete="off"
                  />
                </Field>
                <Field label="thread id" hint="Sent as thread_id for memory recipes.">
                  <Input
                    value={threadId}
                    onChange={(e) => onThreadIdChange(e.target.value)}
                    spellCheck={false}
                    autoComplete="off"
                  />
                </Field>
                <Field label="user id" hint="Sent as user_id for long-term memory recipes.">
                  <Input
                    value={userId}
                    onChange={(e) => onUserIdChange(e.target.value)}
                    spellCheck={false}
                    autoComplete="off"
                  />
                </Field>
              </div>
            ) : (
              <p className="font-mono text-[11px] text-ink-dim">
                {agentUrl}
                <br />
                thread {threadId} · user {userId}
              </p>
            )}
          </SidebarSection>

          <Diagnostics agentUrl={agentUrl} />

          {slug === "long-term-memory-langchain-postgres" ? (
            <MemorySummary agentUrl={agentUrl} userId={userId} />
          ) : null}

          <SidebarSection
            title="event log"
            badge={visibleEventCount > 0 ? `${visibleEventCount}` : undefined}
          >
            <div
              ref={logRef}
              className="thin-scroll max-h-[44dvh] space-y-1.5 overflow-y-auto pt-2"
            >
              {logEntries.length === 0 ? (
                <p className="font-mono text-[11px] text-ink-dim">awaiting first event…</p>
              ) : (
                logEntries.map((entry) =>
                  entry.kind === "separator" ? (
                    <TurnSeparator key={entry.key} idx={entry.turnIdx} ts={entry.ts} />
                  ) : (
                    <EventRow key={entry.key} event={entry.event} />
                  ),
                )
              )}
            </div>
          </SidebarSection>

          {sources.length > 0 ? (
            <SidebarSection title="sources" badge={`${sources.length}`}>
              <ol className="space-y-2 pt-2">
                {sources.map((s) => (
                  <li key={`${s.index}-${s.url || s.title}`} className="flex gap-2 font-mono text-[11px]">
                    <span className="text-accent">[{s.index}]</span>
                    <a
                      href={s.url}
                      target="_blank"
                      rel="noreferrer"
                      className="min-w-0 flex-1 truncate text-ink-soft underline decoration-edge-strong underline-offset-2 hover:text-accent hover:decoration-accent"
                    >
                      {s.title || s.url}
                    </a>
                  </li>
                ))}
              </ol>
            </SidebarSection>
          ) : null}
        </div>
      </div>
    </aside>
  );
}

/* ── diagnostics ─────────────────────────────────────────────────────────── */

type HealthStatus = "ok" | "down" | "unknown";

const DIAGNOSTIC_ENDPOINTS = [
  { method: "GET", path: "/healthz", desc: "liveness" },
  { method: "GET", path: "/readyz", desc: "readiness" },
  { method: "GET", path: "/metrics", desc: "prometheus" },
  { method: "GET", path: "/docs", desc: "openapi" },
] as const;

const HEALTH_POLL_INTERVAL_MS = 5_000;

function Diagnostics({ agentUrl }: { agentUrl: string }) {
  const base = useMemo(() => agentUrl.replace(/\/$/, ""), [agentUrl]);
  const [status, setStatus] = useState<HealthStatus>("unknown");
  const [version, setVersion] = useState<string | null>(null);
  const [checkedAt, setCheckedAt] = useState<number | null>(null);

  useEffect(() => {
    let cancelled = false;
    const tick = async () => {
      try {
        const res = await fetch(`${base}/healthz`, { cache: "no-store" });
        if (cancelled) return;
        if (res.ok) {
          const body = (await res.json().catch(() => ({}))) as {
            status?: string;
            version?: string;
          };
          setStatus(body.status === "ok" ? "ok" : "down");
          setVersion(typeof body.version === "string" ? body.version : null);
        } else {
          setStatus("down");
        }
      } catch {
        if (!cancelled) setStatus("down");
      } finally {
        if (!cancelled) setCheckedAt(Date.now());
      }
    };
    tick();
    const id = setInterval(tick, HEALTH_POLL_INTERVAL_MS);
    return () => {
      cancelled = true;
      clearInterval(id);
    };
  }, [base]);

  const badge =
    status === "ok" ? "live" : status === "down" ? "down" : "checking…";

  return (
    <SidebarSection title="diagnostics" badge={badge}>
      <ul className="space-y-1.5 pt-2 font-mono text-[11px]">
        {DIAGNOSTIC_ENDPOINTS.map((e) => (
          <li key={e.path} className="flex items-center gap-2">
            <span className="shrink-0 text-accent">{e.method}</span>
            <a
              href={`${base}${e.path}`}
              target="_blank"
              rel="noreferrer"
              className="min-w-0 flex-1 truncate text-ink-soft underline decoration-edge-strong underline-offset-2 hover:text-accent hover:decoration-accent"
            >
              {e.path}
            </a>
            <span className="shrink-0 text-ink-dim">{e.desc}</span>
          </li>
        ))}
      </ul>
      <div className="mt-2 flex items-center justify-between border-t border-edge pt-2 font-mono text-[10px] uppercase tracking-[0.14em] text-ink-dim">
        <span>{version ? `v${version}` : "—"}</span>
        <span>{checkedAt ? `polled ${fmtTime(checkedAt)}` : "polling…"}</span>
      </div>
    </SidebarSection>
  );
}

function MemorySummary({ agentUrl, userId }: { agentUrl: string; userId: string }) {
  const base = useMemo(() => agentUrl.replace(/\/$/, ""), [agentUrl]);
  const encodedUserId = encodeURIComponent(userId || "demo-user");
  const href = `${base}/memory/${encodedUserId}/summary`;
  const [summary, setSummary] = useState<string | null>(null);
  const [state, setState] = useState<"idle" | "loading" | "error">("idle");

  const loadSummary = useCallback(async () => {
    setState("loading");
    try {
      const res = await fetch(href, { cache: "no-store" });
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      const body = (await res.json()) as { summary?: unknown };
      setSummary(typeof body.summary === "string" ? body.summary : "(empty summary)");
      setState("idle");
    } catch {
      setSummary(null);
      setState("error");
    }
  }, [href]);

  return (
    <SidebarSection
      title="user memory"
      badge={state === "loading" ? "loading" : summary ? "loaded" : undefined}
      action={
        <button
          type="button"
          onClick={loadSummary}
          className="font-mono text-[10px] uppercase tracking-[0.14em] text-ink-soft transition hover:text-accent"
        >
          refresh
        </button>
      }
    >
      <div className="space-y-2 pt-2 font-mono text-[11px] leading-relaxed">
        <a
          href={href}
          target="_blank"
          rel="noreferrer"
          className="block truncate text-ink-soft underline decoration-edge-strong underline-offset-2 hover:text-accent hover:decoration-accent"
        >
          /memory/{userId || "demo-user"}/summary
        </a>
        {state === "error" ? (
          <p className="text-red-300">summary unavailable</p>
        ) : summary ? (
          <pre className="thin-scroll max-h-40 overflow-y-auto whitespace-pre-wrap border border-edge bg-surface/30 p-2 text-ink-soft">
            {summary}
          </pre>
        ) : (
          <p className="text-ink-dim">summarize what the agent knows about this user</p>
        )}
      </div>
    </SidebarSection>
  );
}

type LogEntry =
  | { kind: "separator"; turnIdx: number; ts: number; key: string }
  | { kind: "event"; event: SseEvent; key: string };

function TurnSeparator({ idx, ts }: { idx: number; ts: number }) {
  return (
    <div className="flex items-center gap-2 pt-3 font-mono text-[10px] uppercase tracking-[0.14em] text-ink-dim first:pt-0">
      <span className="text-accent/80">▸ turn {String(idx).padStart(2, "0")}</span>
      <span className="h-px flex-1 bg-edge" />
      <span>{fmtTime(ts)}</span>
    </div>
  );
}

function SidebarSection({
  title,
  badge,
  action,
  children,
}: {
  title: string;
  badge?: string;
  action?: React.ReactNode;
  children: React.ReactNode;
}) {
  return (
    <section>
      <div className="flex items-center gap-2 border-b border-edge pb-2">
        <span className="font-mono text-[10px] uppercase tracking-[0.18em] text-ink-dim">
          {title}
        </span>
        {badge ? (
          <span className="font-mono text-[10px] uppercase tracking-[0.16em] text-accent">
            ▸ {badge}
          </span>
        ) : null}
        {action ? <span className="ml-auto">{action}</span> : null}
      </div>
      {children}
    </section>
  );
}

function EventRow({ event }: { event: SseEvent }) {
  const isHeartbeat = event.name === "heartbeat";

  const summary = useMemo(() => {
    if (isHeartbeat) return "—";
    const keys = Object.keys(event.data);
    if (keys.length === 0) return "{}";
    return keys.map((k) => `${k}=${formatVal(event.data[k])}`).join(" ");
  }, [event.data, isHeartbeat]);

  return (
    <div
      className={cn(
        "group flex gap-2 border-l pl-2 font-mono text-[11px] leading-relaxed",
        isHeartbeat ? "border-edge/50 opacity-50" : "border-edge",
      )}
    >
      <span
        className={cn(
          "shrink-0 inline-flex items-center gap-1",
          isHeartbeat ? "text-ink-dim" : "text-accent",
        )}
      >
        {isHeartbeat ? <span aria-hidden>♥</span> : null}
        {event.name}
      </span>
      <span className="min-w-0 flex-1 truncate text-ink-dim group-hover:text-ink-soft">
        {summary}
      </span>
    </div>
  );
}

interface ApprovalEvent {
  approvalId: string;
  action: string;
  expiresAt?: string;
  book: {
    title: string;
    author: string;
    amount: number;
    currency: string;
    prices?: Record<string, number>;
  };
}

function ApprovalCard({
  turnId,
  approval,
  result,
  onDecision,
}: {
  turnId: string;
  approval: ApprovalEvent;
  result: SseEvent | null;
  onDecision: (turnId: string, approvalId: string, decision: "approve" | "reject") => void;
}) {
  const [now, setNow] = useState(() => Date.now());
  const expiresAtMs = approval.expiresAt ? Date.parse(approval.expiresAt) : null;
  const secondsRemaining =
    typeof expiresAtMs === "number" && Number.isFinite(expiresAtMs)
      ? Math.max(0, Math.ceil((expiresAtMs - now) / 1000))
      : null;
  const expired = secondsRemaining === 0;
  const resultStatus = typeof result?.data.status === "string" ? result.data.status : null;
  const checkoutUrl = typeof result?.data.checkoutUrl === "string" ? result.data.checkoutUrl : null;
  const message = typeof result?.data.message === "string" ? result.data.message : null;
  const disabled = Boolean(result) || expired;

  useEffect(() => {
    if (!expiresAtMs || result || expired) return;
    const interval = window.setInterval(() => setNow(Date.now()), 1_000);
    return () => window.clearInterval(interval);
  }, [expired, expiresAtMs, result]);

  return (
    <div className="mt-4 border border-edge bg-surface/40 p-3">
      <div className="flex flex-wrap items-start justify-between gap-3">
        <div>
          <div className="font-mono text-[10px] uppercase tracking-[0.16em] text-accent">
            approval required
          </div>
          <div className="mt-1 text-sm font-medium text-ink">{approval.book.title}</div>
          <div className="font-mono text-[11px] text-ink-dim">
            {approval.book.author} · {formatMoney(approval.book.amount, approval.book.currency)}
          </div>
          {approval.book.prices ? (
            <div className="mt-1 font-mono text-[10px] uppercase tracking-[0.12em] text-ink-dim">
              {formatPriceList(approval.book.prices)}
            </div>
          ) : null}
        </div>
        <Badge
          tone={resultStatus === "rejected" || expired ? "warn" : checkoutUrl ? "accent" : "warn"}
          bracket
        >
          {resultStatus ?? (expired ? "expired" : "pending")}
        </Badge>
      </div>
      {secondsRemaining !== null ? (
        <div className="mt-2 font-mono text-[10px] uppercase tracking-[0.14em] text-ink-dim">
          {expired ? "approval expired" : `expires in ${formatCountdown(secondsRemaining)}`}
        </div>
      ) : null}
      {checkoutUrl ? (
        <a
          href={checkoutUrl}
          target="_blank"
          rel="noreferrer"
          className="mt-3 block truncate font-mono text-[11px] text-accent underline decoration-accent/40 underline-offset-2"
        >
          {checkoutUrl}
        </a>
      ) : message ? (
        <p className="mt-3 font-mono text-[11px] text-ink-soft">{message}</p>
      ) : null}
      <div className="mt-3 flex gap-2">
        <Button
          type="button"
          size="sm"
          disabled={disabled}
          onClick={() => onDecision(turnId, approval.approvalId, "approve")}
        >
          approve
        </Button>
        <Button
          type="button"
          size="sm"
          variant="secondary"
          disabled={disabled}
          onClick={() => onDecision(turnId, approval.approvalId, "reject")}
        >
          reject
        </Button>
      </div>
    </div>
  );
}

/* ── helpers ─────────────────────────────────────────────────────────────── */

function formatVal(v: unknown): string {
  if (typeof v === "string") return v.length > 24 ? `"${v.slice(0, 24)}…"` : `"${v}"`;
  if (typeof v === "number" || typeof v === "boolean") return String(v);
  if (Array.isArray(v)) return `[${v.length}]`;
  if (v && typeof v === "object") return `{${Object.keys(v).length}}`;
  return "null";
}

function formatMoney(amount: number, currency: string): string {
  return new Intl.NumberFormat("en-US", {
    style: "currency",
    currency: currency.toUpperCase(),
  }).format(amount / 100);
}

function formatPriceList(prices: Record<string, number>): string {
  return Object.entries(prices)
    .map(([currency, amount]) => formatMoney(amount, currency))
    .join(" · ");
}

function formatCountdown(totalSeconds: number): string {
  const minutes = Math.floor(totalSeconds / 60);
  const seconds = totalSeconds % 60;
  return `${minutes}:${String(seconds).padStart(2, "0")}`;
}

function latestApproval(events: SseEvent[]): ApprovalEvent | null {
  for (let i = events.length - 1; i >= 0; i--) {
    const ev = events[i];
    if (ev?.name !== "approval_required") continue;
    const approvalId = stringValue(ev.data.approvalId);
    const action = stringValue(ev.data.action);
    const book = ev.data.book;
    if (!approvalId || !action || !book || typeof book !== "object" || Array.isArray(book)) {
      continue;
    }
    const data = book as Record<string, unknown>;
    const title = stringValue(data.title);
    const author = stringValue(data.author);
    const amount = numberValue(data.amount);
    const currency = stringValue(data.currency);
    const prices = pricesValue(data.prices);
    if (!title || !author || typeof amount !== "number" || !currency) continue;
    return {
      approvalId,
      action,
      expiresAt: stringValue(ev.data.expiresAt),
      book: { title, author, amount, currency, prices },
    };
  }
  return null;
}

function pricesValue(value: unknown): Record<string, number> | undefined {
  if (!value || typeof value !== "object" || Array.isArray(value)) return undefined;
  const out: Record<string, number> = {};
  for (const [currency, amount] of Object.entries(value)) {
    if (typeof amount === "number" && Number.isFinite(amount)) out[currency] = amount;
  }
  return Object.keys(out).length > 0 ? out : undefined;
}

function latestApprovalResult(events: SseEvent[], approvalId: string): SseEvent | null {
  for (let i = events.length - 1; i >= 0; i--) {
    const ev = events[i];
    if (ev?.name === "approval_result" && ev.data.approvalId === approvalId) return ev;
  }
  return null;
}

function latestRunStats(turns: ChatTurn[]): RunStats | null {
  for (let i = turns.length - 1; i >= 0; i--) {
    const assistant = turns[i];
    if (!assistant || assistant.role !== "assistant") continue;

    const user = turns
      .slice(0, i)
      .reverse()
      .find((turn) => turn.role === "user");
    const done = [...assistant.events].reverse().find((event) => event.name === "done");
    const doneUsage = done ? usageFromEvent(done) : null;
    const status = [...assistant.events]
      .reverse()
      .find((event) => event.name === "status" && (event.data.route || event.data.contextNeed));
    const statusUsage = status ? usageFromNestedStatus(status) : null;
    const usage = doneUsage ?? statusUsage;
    const rendered = splitMetricsFooter(assistant.text);

    const inputTokens =
      usage?.inputTokens && usage.inputTokens > 0
        ? usage.inputTokens
        : estimateTokens(user?.text ?? "");
    const outputTokens =
      usage?.outputTokens && usage.outputTokens > 0
        ? usage.outputTokens
        : estimateTokens(rendered.body);

    return {
      route: stringValue(status?.data.route),
      contextNeed: stringValue(status?.data.contextNeed),
      elapsedSeconds:
        usage?.elapsedSeconds ??
        numberValue(status?.data.elapsedSeconds) ??
        msToSeconds(numberValue(status?.data.elapsedMs)),
      inputTokens,
      outputTokens,
      costUsd: usage?.costUsd,
      estimated: !usage || usage.inputTokens === 0 || usage.outputTokens === 0,
    };
  }

  return null;
}

function usageFromEvent(event: SseEvent): Pick<RunStats, "inputTokens" | "outputTokens" | "costUsd" | "elapsedSeconds"> {
  return {
    inputTokens: numberValue(event.data.inputTokens) ?? 0,
    outputTokens: numberValue(event.data.outputTokens) ?? 0,
    costUsd: numberValue(event.data.costUsd),
    elapsedSeconds: numberValue(event.data.elapsedSeconds),
  };
}

function usageFromNestedStatus(
  event: SseEvent,
): Pick<RunStats, "inputTokens" | "outputTokens" | "costUsd" | "elapsedSeconds"> | null {
  const usage = event.data.usage;
  if (!usage || typeof usage !== "object" || Array.isArray(usage)) return null;
  const data = usage as Record<string, unknown>;
  return {
    inputTokens: numberValue(data.inputTokens) ?? 0,
    outputTokens: numberValue(data.outputTokens) ?? 0,
    costUsd: numberValue(data.costUsd),
    elapsedSeconds: numberValue(data.elapsedSeconds),
  };
}

function estimateTokens(text: string): number {
  const trimmed = text.trim();
  if (!trimmed) return 0;
  return Math.max(1, Math.ceil(trimmed.length / 4));
}

function numberValue(value: unknown): number | undefined {
  return typeof value === "number" && Number.isFinite(value) ? value : undefined;
}

function stringValue(value: unknown): string | undefined {
  return typeof value === "string" && value.trim() ? value : undefined;
}

function msToSeconds(ms: number | undefined): number | undefined {
  return typeof ms === "number" ? ms / 1000 : undefined;
}

function latestStatusPhase(events: SseEvent[]): string | undefined {
  for (let i = events.length - 1; i >= 0; i--) {
    const ev = events[i];
    if (ev?.name === "status" && typeof ev.data.phase === "string") return ev.data.phase;
  }
  return undefined;
}

interface Source {
  index: number;
  title: string;
  url: string;
}

function extractSources(events: SseEvent[]): Source[] {
  for (let i = events.length - 1; i >= 0; i--) {
    const ev = events[i];
    if (ev?.name !== "sources") continue;
    const items = ev.data.items;
    if (!Array.isArray(items)) continue;
    return items.map((it, idx) => {
      const o = it as Record<string, unknown>;
      return {
        index: typeof o.citation === "number" ? o.citation : idx + 1,
        title: typeof o.title === "string" ? o.title : "",
        url: typeof o.url === "string" ? o.url : "",
      };
    });
  }
  return [];
}
