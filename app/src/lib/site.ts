/**
 * Site-wide constants resolved from env vars at build time.
 *
 * The defaults match the current canonical hosts but can be overridden per
 * environment via Clever Cloud env config or a local `.env` file.
 */

export const GITHUB_REPO_URL =
  process.env.NEXT_PUBLIC_GITHUB_REPO ?? "https://github.com/nebius/nebius-partner-cookbook";

function envOrDefault(value: string | undefined, fallback: string): string {
  const trimmed = value?.trim();
  return trimmed ? trimmed : fallback;
}

export const SITE_URL = envOrDefault(
  process.env.NEXT_PUBLIC_SITE_URL,
  "https://cookbook.nebius.com",
);

/** Build a deep link into the canonical GitHub repo. */
export function ghPath(...segments: string[]): string {
  return `${GITHUB_REPO_URL}/${segments.map((s) => s.replace(/^\/+|\/+$/g, "")).join("/")}`;
}
