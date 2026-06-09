// Forge-style topbar: lime-pill NEBIUS mark, product wordmark, nav links, account pill

const NAV = [
  { id: "audit",   label: "Audit"      },
  { id: "compare", label: "Compare"    },
  { id: "eval",    label: "Evaluation" },
];

// Nebius logo — inlined SVG, lime pill background + ink wordmark
const NebiusLogo = ({ height = 44 }) => (
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1133.9 311.8"
       style={{ height, width: "auto", display: "block" }} role="img" aria-label="Nebius">
    <path fill="var(--forge-lime)" d="M1055.8,0H78C34.9,0,0,35.2,0,78.6v154.6c0,43.4,34.9,78.6,78,78.6h977.8c43.1,0,78-35.2,78-78.6V78.6c0-43.4-34.9-78.6-78-78.6Z"/>
    <g fill="var(--forge-ink)">
      <path d="M203.9,187.7h0l-36.6-84.5c-6-13.7-15.8-21.4-29.7-21.4s-23.4,11.3-23.4,23.3c0,0,17.5-2.4,26.8,18.9l36.6,84.5c6,13.7,15.8,21.4,29.7,21.4s23.4-11.3,23.4-23.3c0,0-17.5,2.4-26.8-18.9Z"/>
      <path d="M85.2,140.3v87.5h29.1v-122.7s-29.1,1.8-29.1,35.2Z"/>
      <path d="M230.7,206.7s29.1-1.8,29.1-35.2v-87.5h-29.1v122.7Z"/>
      <polygon points="289.7 83.9 289.7 83.9 289.7 227.9 289.7 227.9 439.2 227.9 439.2 200.6 319 200.6 319 169.3 426.2 169.3 426.2 142.1 319 142.1 319 111.1 439.2 111.1 439.2 83.9 319 83.9 289.7 83.9"/>
      <path d="M596.8,152.9h0c7.8-5.2,14.4-15.1,14.4-29.8,0-33.5-32.1-39.1-57.1-39.3h-84.9v144h93.7c43.2,0,57.3-16.5,57.3-40.7s-15.5-31.8-23.4-34.2ZM498.5,111.1h60.8c13.5,0,23.8,4.7,23.8,16.9s-11.8,14.7-19.8,14.8h-64.8v-31.7ZM563.2,200.6h0s-64.8,0-64.8,0v-32.3h64.4c12.6,0,27,2.7,27,16.4s-13.1,15.9-26.6,15.9Z"/>
      <rect x="646.6" y="83.9" width="29.3" height="144"/>
      <path d="M1038,158.7h0s0,0,0,0c-14.3-11.5-26.6-12.8-50-15.2l-2.1-.2c-2.9-.2-43.2-3.6-46.3-3.9-27.6-2.6-25.6-15.1-25.6-15.1,0-13.8,27.9-14.9,27.9-14.9,23.1-2.3,68.4-1.6,71.2,18.8h32c-2.9-40.3-52.8-46.1-84.8-46.5-21.2.5-44.4,1.8-62.7,13.8-20.6,13.6-18.6,40.6-5.7,52.8,5,4.4,12.7,10.4,28.3,13.3,7.2,1.3,19,3.1,35.1,4.2,0,0,25.8,1.6,31.3,2,.3,0,.5,0,.8,0h0c8.6.7,26.9,2.1,28.4,15.8,1.7,15.1-24.4,19.5-51.1,19.5-11.7,0-23.6-.5-36-4-10.4-3-16.4-9.1-17.4-19.3h-31.7c0,43.4,49.3,50.1,83.7,50.1,23.5-.6,48.9-2.2,69.2-15.2,22.4-14.7,20.1-43.2,5.3-56Z"/>
      <path d="M826.3,160.5c0,26.7-17,42.5-45.8,42.5s-45.6-15.8-45.6-42.5v-76.6h-29.1v76.1c0,42.1,29.5,70,74.6,70s74.9-27.7,74.9-70v-76.1h-29.1v76.6Z"/>
    </g>
  </svg>
);

const Topbar = ({ scene, nav }) => (
  <header style={{
    height: 76, padding: "0 32px",
    display: "flex", alignItems: "center", gap: 28,
    borderBottom: "1px solid rgba(7,26,48,0.08)",
    background: "rgba(232, 244, 252, 0.7)",
    backdropFilter: "blur(10px)",
    position: "sticky", top: 0, zIndex: 30,
  }}>
    {/* Nebius logo */}
    <NebiusLogo height={40}/>

    {/* Divider + product wordmark */}
    <div style={{ width: 1, height: 28, background: "rgba(7,26,48,0.2)" }}/>
    <div style={{
      font: "700 22px/1 var(--forge-font)",
      letterSpacing: "-0.01em",
      color: "var(--forge-ink)",
    }}>Sentinel</div>

    <div style={{ flex: 1 }}/>

    {/* Nav */}
    <nav style={{ display: "flex", alignItems: "center", gap: 26 }}>
      {NAV.map(n => {
        const active = scene === n.id;
        return (
          <button key={n.id} onClick={() => nav && nav(n.id)} style={{
            background: "transparent", border: 0,
            font: `${active ? 700 : 500} 15px/1 var(--forge-font)`,
            color: active ? "var(--forge-ink)" : "var(--forge-on-light-mute)",
            cursor: "pointer",
            position: "relative", padding: "4px 0",
            letterSpacing: "-0.005em", whiteSpace: "nowrap",
          }}>
            {n.label}
            {active && <span style={{
              position: "absolute", left: 0, right: 0, bottom: -6, height: 2,
              background: "var(--forge-ink)", borderRadius: 999,
            }}/>}
          </button>
        );
      })}
    </nav>
  </header>
);

Object.assign(window, { Topbar });
