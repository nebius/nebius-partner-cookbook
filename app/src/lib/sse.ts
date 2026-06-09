/**
 * Minimal SSE client for our cookbook agent endpoints.
 *
 * Native EventSource only supports GET, but our cookbooks use POST. So we use
 * fetch() + ReadableStream and parse SSE event blocks ourselves.
 *
 * Each emitted event has a `name` (the `event:` line) and a parsed JSON `data`.
 * Unknown payloads are surfaced as a string in `data._raw`.
 */

export interface SseEvent {
  name: string;
  data: Record<string, unknown>;
}

export interface StreamOptions {
  url: string;
  body: unknown;
  signal?: AbortSignal;
  headers?: Record<string, string>;
}

export async function* streamAgent({
  url,
  body,
  signal,
  headers,
}: StreamOptions): AsyncGenerator<SseEvent, void, void> {
  const response = await fetch(url, {
    method: "POST",
    headers: {
      "content-type": "application/json",
      accept: "text/event-stream",
      ...headers,
    },
    body: JSON.stringify(body),
    signal,
  });

  if (!response.ok) {
    const detail = await response.text().catch(() => response.statusText);
    throw new Error(`Agent returned ${response.status}: ${detail.slice(0, 200)}`);
  }

  if (!response.body) {
    throw new Error("Agent response has no body");
  }

  const reader = response.body.getReader();
  const decoder = new TextDecoder("utf-8");
  let buffer = "";

  try {
    while (true) {
      const { value, done } = await reader.read();
      if (done) break;
      buffer += decoder.decode(value, { stream: true });

      // SSE event blocks are separated by a blank line ("\n\n").
      let idx: number;
      while ((idx = buffer.indexOf("\n\n")) !== -1) {
        const block = buffer.slice(0, idx);
        buffer = buffer.slice(idx + 2);
        const event = parseBlock(block);
        if (event) yield event;
      }
    }

    // Flush any trailing block (in case server didn't end with \n\n).
    const trailing = buffer.trim();
    if (trailing) {
      const event = parseBlock(trailing);
      if (event) yield event;
    }
  } finally {
    reader.releaseLock();
  }
}

function parseBlock(block: string): SseEvent | null {
  let name = "message";
  const dataLines: string[] = [];

  for (const line of block.split("\n")) {
    if (!line || line.startsWith(":")) continue; // comments/heartbeats
    const colon = line.indexOf(":");
    if (colon === -1) continue;
    const field = line.slice(0, colon).trim();
    const value = line.slice(colon + 1).trimStart();
    if (field === "event") name = value;
    else if (field === "data") dataLines.push(value);
  }

  if (dataLines.length === 0) return { name, data: {} };

  const raw = dataLines.join("\n");
  try {
    const parsed = JSON.parse(raw);
    if (parsed && typeof parsed === "object" && !Array.isArray(parsed)) {
      return { name, data: parsed as Record<string, unknown> };
    }
    return { name, data: { _raw: parsed } };
  } catch {
    return { name, data: { _raw: raw } };
  }
}
