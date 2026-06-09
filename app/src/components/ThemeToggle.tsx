"use client";

import { useEffect, useState } from "react";
import { Monitor, Moon, Sun } from "lucide-react";
import { cn } from "@/components/cn";

type ThemeChoice = "system" | "light" | "dark";

const STORAGE_KEY = "nebius-cookbook:theme";

const OPTIONS: { value: ThemeChoice; label: string; Icon: typeof Sun }[] = [
  { value: "system", label: "System", Icon: Monitor },
  { value: "light", label: "Light", Icon: Sun },
  { value: "dark", label: "Dark", Icon: Moon },
];

function systemTheme(): "light" | "dark" {
  return window.matchMedia("(prefers-color-scheme: light)").matches ? "light" : "dark";
}

/** Resolve a choice to a concrete theme and write it to <html data-theme>. */
function apply(choice: ThemeChoice): void {
  document.documentElement.dataset.theme =
    choice === "system" ? systemTheme() : choice;
}

export function ThemeToggle() {
  const [choice, setChoice] = useState<ThemeChoice>("system");
  // The server can't know the stored choice; defer active styling until mount
  // so the first client render matches the server and React stays quiet.
  const [mounted, setMounted] = useState(false);

  useEffect(() => {
    const stored = window.localStorage.getItem(STORAGE_KEY);
    setChoice(stored === "light" || stored === "dark" ? stored : "system");
    setMounted(true);
  }, []);

  // While on "system", track the OS preference live.
  useEffect(() => {
    if (choice !== "system") return;
    const mq = window.matchMedia("(prefers-color-scheme: light)");
    const onChange = () => apply("system");
    mq.addEventListener("change", onChange);
    return () => mq.removeEventListener("change", onChange);
  }, [choice]);

  const pick = (next: ThemeChoice) => {
    setChoice(next);
    apply(next);
    try {
      // "system" is the default — store nothing so it follows the OS forever.
      if (next === "system") window.localStorage.removeItem(STORAGE_KEY);
      else window.localStorage.setItem(STORAGE_KEY, next);
    } catch {
      /* storage blocked (private mode) — the theme is still applied at runtime */
    }
  };

  return (
    <div
      role="group"
      aria-label="Color theme"
      className="fixed bottom-4 right-4 z-50 inline-flex border border-edge-strong bg-surface/80 shadow-[0_8px_24px_-12px_rgba(0,0,0,0.5)] backdrop-blur-md"
    >
      {OPTIONS.map(({ value, label, Icon }) => {
        const active = mounted && choice === value;
        return (
          <button
            key={value}
            type="button"
            onClick={() => pick(value)}
            aria-label={`${label} theme`}
            aria-pressed={active}
            title={`${label} theme`}
            className={cn(
              "inline-flex size-9 items-center justify-center transition",
              active ? "bg-accent-soft text-accent" : "text-ink-dim hover:text-ink",
            )}
          >
            <Icon className="size-4" />
          </button>
        );
      })}
    </div>
  );
}
