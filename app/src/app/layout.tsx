import type { Metadata } from "next";
import { IBM_Plex_Sans, IBM_Plex_Mono, Jersey_15 } from "next/font/google";
import { GitHubCorner, ThemeToggle } from "@/components";
import { SITE_URL } from "@/lib/site";
import "./globals.css";

// Runs before first paint: resolves the stored theme (or the OS preference)
// and sets <html data-theme> so there is no flash of the wrong palette.
const themeScript = `
(function(){
  try {
    var c = localStorage.getItem('nebius-cookbook:theme');
    var t = (c === 'light' || c === 'dark')
      ? c
      : (matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark');
    document.documentElement.dataset.theme = t;
  } catch (e) {
    document.documentElement.dataset.theme = 'dark';
  }
})();
`;

const plexSans = IBM_Plex_Sans({
  subsets: ["latin"],
  weight: ["400", "500", "600", "700"],
  variable: "--font-plex-sans",
  display: "swap",
});

const plexMono = IBM_Plex_Mono({
  subsets: ["latin"],
  weight: ["400", "500", "600"],
  variable: "--font-plex-mono",
  display: "swap",
});

const jersey = Jersey_15({
  subsets: ["latin"],
  weight: "400",
  variable: "--font-display-jersey",
  display: "swap",
});

export const metadata: Metadata = {
  title: {
    default: "Agent Blueprint Recipes",
    template: "%s — Agent Blueprint Recipes",
  },
  description: "Production-grade recipes for building AI agents on Nebius AgentKit.",
  metadataBase: new URL(SITE_URL),
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html
      lang="en"
      suppressHydrationWarning
      className={`${plexSans.variable} ${plexMono.variable} ${jersey.variable}`}
    >
      <body className="min-h-dvh antialiased">
        <script dangerouslySetInnerHTML={{ __html: themeScript }} />
        {children}
        <GitHubCorner />
        <ThemeToggle />
      </body>
    </html>
  );
}
