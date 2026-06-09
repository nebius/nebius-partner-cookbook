// Forge primitives — building blocks of the dark-slab + light-page layout.

const Icons = {
  bolt:    <><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></>,
  shield:  <><path d="M12 2l8 4v6c0 5-3.5 9-8 10-4.5-1-8-5-8-10V6l8-4z"/></>,
  check:   <polyline points="20 6 9 17 4 12"/>,
  x:       <><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></>,
  arrow:   <><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></>,
  arrowUR: <><line x1="7" y1="17" x2="17" y2="7"/><polyline points="7 7 17 7 17 17"/></>,
  chevron: <polyline points="6 9 12 15 18 9"/>,
  search:  <><circle cx="11" cy="11" r="7"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></>,
  play:    <polygon points="5 3 19 12 5 21 5 3"/>,
  pause:   <><rect x="6" y="4" width="4" height="16"/><rect x="14" y="4" width="4" height="16"/></>,
  download:<><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></>,
  link:    <><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></>,
  send:    <><line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/></>,
  spark:   <><path d="M12 3v4M12 17v4M3 12h4M17 12h4M5.5 5.5l2.5 2.5M16 16l2.5 2.5M5.5 18.5L8 16M16 8l2.5-2.5"/></>,
  ticket:  <><path d="M3 9a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2v3a2 2 0 0 0 0 4v3a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-3a2 2 0 0 0 0-4z"/><line x1="13" y1="5" x2="13" y2="19" strokeDasharray="2 3"/></>,
  flag:    <><path d="M4 22V4a1 1 0 0 1 1-1h14a1 1 0 0 1 .8 1.6L16 9l3.8 4.4A1 1 0 0 1 19 15H5"/></>,
  copy:    <><rect x="9" y="9" width="13" height="13" rx="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></>,
  globe:   <><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></>,
  book:    <><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></>,
  doc:     <><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></>,
};

const Icon = ({ name, size = 16, color = "currentColor", stroke = 1.75 }) => (
  <svg width={size} height={size} viewBox="0 0 24 24" fill="none"
       stroke={color} strokeWidth={stroke}
       strokeLinecap="round" strokeLinejoin="round">
    {Icons[name]}
  </svg>
);

// ── SLAB — the deep navy hero panel; the signature Forge surface
const Slab = ({ children, style, padding = 36 }) => (
  <section style={{
    background: "var(--forge-ink)",
    borderRadius: "var(--forge-r-xl)",
    padding,
    color: "var(--forge-on-dark)",
    boxShadow: "0 1px 2px rgba(0,0,0,0.06)",
    ...style,
  }}>{children}</section>
);

// ── PANEL — a nested darker card *inside* a slab (used for stats, tool calls, etc)
const Panel = ({ children, style, padding = 22 }) => (
  <div style={{
    background: "var(--forge-ink-2)",
    border: "1px solid var(--forge-border-dark)",
    borderRadius: "var(--forge-r-lg)",
    padding,
    color: "var(--forge-on-dark)",
    ...style,
  }}>{children}</div>
);

// ── WHITE CARD — used in lighter sections under slabs
const PaperCard = ({ children, style, padding }) => (
  <div style={{
    background: "#fff",
    border: "1px solid var(--forge-border-light)",
    borderRadius: "var(--forge-r-lg)",
    padding: padding || 0,
    color: "var(--forge-on-light)",
    boxShadow: "0 1px 2px rgba(0,0,0,0.03)",
    ...style,
  }}>{children}</div>
);

// ── STAT CARD — Forge signature: kicker (caps) + huge number + body
const StatCard = ({ kicker, value, valueColor, body, size = "m", style }) => (
  <Panel padding={size === "l" ? 28 : 22} style={style}>
    <div className="f-kicker" style={{ color: "var(--forge-on-dark-mute)", marginBottom: size === "l" ? 16 : 14 }}>{kicker}</div>
    <div style={{
      font: `800 ${size === "l" ? "64px" : "44px"}/1 var(--forge-font)`,
      letterSpacing: "-0.03em",
      color: valueColor || "var(--forge-on-dark-strong)",
      marginBottom: size === "l" ? 18 : 14,
    }}>{value}</div>
    {body && (
      <div style={{
        font: "400 13px/19px var(--forge-font)",
        color: "var(--forge-on-dark-mute)",
        maxWidth: size === "l" ? "100%" : 200,
      }}>{body}</div>
    )}
  </Panel>
);

// ── OUTLINE PILL — Forge's cyan-ringed tag (DIFFUSION, SDXL, AUTH)
const OutlinePill = ({ children, size = "m", tone = "cyan", style }) => {
  const tones = {
    cyan: { color: "var(--forge-cyan)", border: "var(--forge-cyan-deep)" },
    lime: { color: "var(--forge-ink)",  border: "var(--forge-lime)", bg: "var(--forge-lime)" },
    limeRing: { color: "var(--forge-lime)", border: "var(--forge-lime)" },
    muteLight: { color: "var(--forge-on-light-mute)", border: "rgba(7,26,48,0.20)" },
    muteDark:  { color: "var(--forge-on-dark-mute)",  border: "rgba(255,255,255,0.18)" },
  };
  const t = tones[tone];
  const px = size === "s" ? 10 : 14;
  const py = size === "s" ? 4  : 6;
  const fs = size === "s" ? 10 : 11;
  return (
    <span style={{
      display: "inline-flex", alignItems: "center", gap: 6,
      padding: `${py}px ${px}px`,
      border: `1px solid ${t.border}`,
      borderRadius: "var(--forge-r-pill)",
      background: t.bg || "transparent",
      color: t.color,
      font: `600 ${fs}px/1 var(--forge-font)`,
      letterSpacing: "0.10em",
      textTransform: "uppercase",
      whiteSpace: "nowrap",
      ...style,
    }}>{children}</span>
  );
};

// ── FILLED LIME PILL — Forge's selected/primary tag (ALL, DF 1.3B 540P DIFFUSERS · DEFAULT)
const LimePill = ({ children, style, size = "m" }) => (
  <span style={{
    display: "inline-flex", alignItems: "center", gap: 6,
    padding: size === "s" ? "5px 10px" : "8px 14px",
    border: "1px solid var(--forge-lime)",
    borderRadius: "var(--forge-r-pill)",
    background: "transparent",
    color: "var(--forge-lime)",
    font: `700 ${size === "s" ? 10 : 11}px/1 var(--forge-font)`,
    letterSpacing: "0.10em",
    textTransform: "uppercase",
    whiteSpace: "nowrap",
    ...style,
  }}>{children}</span>
);

// ── STATUS CHIP — small live status like "COLD", "WARM", "running"
const StatusChip = ({ tone = "cold", children, style }) => {
  const tones = {
    cold:    { color: "var(--forge-on-dark-mute)", border: "rgba(255,255,255,0.18)", bg: "transparent" },
    warm:    { color: "var(--forge-mint-warm)",    border: "var(--forge-mint-warm)", bg: "transparent" },
    live:    { color: "var(--forge-ink)",          border: "var(--forge-lime)",      bg: "var(--forge-lime)" },
    running: { color: "var(--forge-lime)",         border: "var(--forge-lime)",      bg: "transparent" },
    danger:  { color: "var(--forge-red)",          border: "var(--forge-red)",       bg: "transparent" },
    partial: { color: "var(--forge-amber)",        border: "var(--forge-amber)",     bg: "transparent" },
  };
  const t = tones[tone];
  return (
    <span style={{
      display: "inline-flex", alignItems: "center", gap: 6,
      padding: "4px 10px",
      border: `1px solid ${t.border}`,
      borderRadius: "var(--forge-r-pill)",
      background: t.bg,
      color: t.color,
      font: "600 10px/1 var(--forge-font)",
      letterSpacing: "0.12em",
      textTransform: "uppercase",
      whiteSpace: "nowrap",
      ...style,
    }}>{children}</span>
  );
};

// ── BUTTON
const Btn = ({ variant = "ink", icon, iconRight, size = "m", children, style, disabled, ...p }) => {
  const h = { s: 28, m: 38, l: 44 }[size];
  const px = { s: 12, m: 18, l: 22 }[size];
  const fs = { s: 12, m: 13, l: 14 }[size];
  const variants = {
    ink:   { bg: "var(--forge-ink)",  fg: "#fff", border: "none" },
    lime:  { bg: "var(--forge-lime)", fg: "var(--forge-ink)", border: "none" },
    ghost: { bg: "transparent", fg: "var(--forge-on-light)", border: "1px solid var(--forge-border-light)" },
    ghostDark: { bg: "transparent", fg: "var(--forge-on-dark)", border: "1px solid var(--forge-border-dark-strong)" },
  };
  const v = variants[variant];
  return (
    <button {...p} disabled={disabled} style={{
      display: "inline-flex", alignItems: "center", gap: 8,
      height: h, padding: `0 ${px}px`,
      borderRadius: variant === "lime" || variant === "ink" ? 12 : "var(--forge-r-pill)",
      background: v.bg, color: v.fg, border: v.border,
      font: `700 ${fs}px/1 var(--forge-font)`,
      cursor: disabled ? "default" : "pointer", letterSpacing: "0.005em",
      whiteSpace: "nowrap",
      opacity: disabled ? 0.45 : 1,
      transition: "filter .15s, opacity .15s",
      ...style,
    }}>{icon}{children}{iconRight}</button>
  );
};

// ── LINK ARROW (Forge's "OPEN MODEL DETAILS →" pattern)
const LinkArrow = ({ children, color = "var(--forge-cyan)", style }) => (
  <span style={{
    display: "inline-flex", alignItems: "center", gap: 8,
    color, font: "600 11px/1 var(--forge-font)",
    letterSpacing: "0.16em", textTransform: "uppercase",
    cursor: "pointer", ...style,
  }}>
    {children} <span style={{ font: "600 14px/1 var(--forge-mono)" }}>→</span>
  </span>
);

// ── SECTION TITLE (light-bg sections)
const SectionTitle = ({ children, kicker, action }) => (
  <div style={{ display: "flex", alignItems: "flex-end", justifyContent: "space-between", gap: 24, marginBottom: 20 }}>
    <div>
      {kicker && <div className="f-kicker-light" style={{ marginBottom: 10 }}>{kicker}</div>}
      <div style={{ font: "700 32px/1.05 var(--forge-font)", letterSpacing: "-0.02em", color: "var(--forge-on-light)" }}>
        {children}
      </div>
    </div>
    {action}
  </div>
);

// ── Mono inline-code chip
const M = ({ children, on = "light" }) => (
  <span style={{
    font: "500 12px/1 var(--forge-mono)",
    padding: "2px 6px",
    background: on === "dark" ? "rgba(255,255,255,0.07)" : "rgba(7,26,48,0.06)",
    color: on === "dark" ? "var(--forge-on-dark)" : "var(--forge-on-light)",
    borderRadius: 4,
  }}>{children}</span>
);

// ── SPINNER for in-flight tool calls
const Spinner = ({ color = "var(--forge-lime)", size = 14 }) => (
  <div style={{
    width: size, height: size, borderRadius: "50%",
    border: `2px solid rgba(255,255,255,0.10)`,
    borderTopColor: color,
    animation: "f-spin 0.9s linear infinite",
  }}/>
);
const SpinnerStyle = () => (
  <style>{"@keyframes f-spin { to { transform: rotate(360deg); } }"}</style>
);

// ── STREAM PANE — fixed-height scroll area for live SSE output.
// Sticks to bottom while `status === "running"` unless the user scrolled up.
const StreamPane = ({ children, status, maxHeight = 480, padding = "20px 24px" }) => {
  const ref = React.useRef(null);
  const stickyRef = React.useRef(true);

  const onScroll = () => {
    const el = ref.current;
    if (!el) return;
    stickyRef.current = el.scrollHeight - el.scrollTop - el.clientHeight < 24;
  };

  React.useEffect(() => {
    const el = ref.current;
    if (!el) return;
    if (status === "running" && stickyRef.current) {
      el.scrollTop = el.scrollHeight;
    }
  });

  return (
    <div
      ref={ref}
      onScroll={onScroll}
      style={{
        padding,
        display: "flex", flexDirection: "column", gap: 12,
        maxHeight,
        overflowY: "auto",
        scrollbarGutter: "stable",
        flex: "0 0 auto",
      }}>
      {children}
    </div>
  );
};

// ── MARKDOWN — renders a markdown string to HTML via `marked`, then sanitises
// it with DOMPurify before injection. `marked` does NOT sanitise on its own, so
// the DOMPurify pass is what neutralises any script/event-handler markup that
// could ride in via agent output (SOPs, web-search results, etc.).
const _markedOpts = (() => {
  if (typeof marked === "undefined") return null;
  marked.setOptions({ breaks: true, gfm: true });
  return true;
})();

const Markdown = ({ text, style }) => {
  const html = React.useMemo(() => {
    if (!text) return "";
    if (typeof marked === "undefined") return text.replace(/</g, "&lt;");
    const raw = marked.parse(text);
    // If DOMPurify failed to load, fall back to escaping rather than inject raw HTML.
    return typeof DOMPurify !== "undefined" ? DOMPurify.sanitize(raw) : raw.replace(/</g, "&lt;");
  }, [text]);
  return <div className="forge-md" style={style} dangerouslySetInnerHTML={{ __html: html }} />;
};

// ── METER — label + large mono value, used in metrics rows
const Meter = ({ label, value, accent, live }) => (
  <div style={{ display: "flex", flexDirection: "column", gap: 4 }}>
    <span style={{ font: "600 10px/1 var(--forge-font)", letterSpacing: "0.10em", textTransform: "uppercase", color: "var(--forge-on-dark-mute)" }}>{label}</span>
    <span style={{
      font: "700 16px/1 var(--forge-mono)",
      color: accent ? "var(--forge-lime)" : "var(--forge-on-dark-strong)",
      display: "flex", alignItems: "center", gap: 6,
    }}>
      {live && <span style={{ width: 6, height: 6, borderRadius: 999, background: "var(--forge-lime)", boxShadow: "0 0 0 3px rgba(212,250,80,0.25)" }}/>}
      {value}
    </span>
  </div>
);

Object.assign(window, {
  Icons, Icon, Slab, Panel, PaperCard,
  StatCard, OutlinePill, LimePill, StatusChip,
  Btn, LinkArrow, SectionTitle, M, Spinner, SpinnerStyle, StreamPane,
  Markdown, Meter,
});
