export function normalizeBaseUrl(value?: string): string {
  const url = new URL(value?.trim() || "https://api.tokenfactory.nebius.com/v1/");
  const path = url.pathname.replace(/\/+$/, "");
  url.pathname = path || "/v1";
  return url.toString().replace(/\/+$/, "");
}
