// Thin client for the UI's FastAPI backend.
// Exposes window.ForgeAPI with fetch helpers + an SSE consumer.
//
// Auth: the backend gates /api/* behind a shared X-API-Key (when UI_API_KEY is
// set server-side). The key is never shipped in this bundle — the user is
// prompted for it at runtime and it is kept in sessionStorage (not localStorage,
// to limit exposure if any XSS slips through). Every request carries the key in
// the X-API-Key header; a 401 clears it and re-prompts.

(function () {
  const API_BASE = window.FORGE_API_BASE || "";
  const KEY_STORAGE = "sentinel_api_key";
  // Cheap, gated endpoint used to verify a key before accepting it.
  const VALIDATE_PATH = "/api/auth-check";

  function getKey() {
    try {
      return window.sessionStorage.getItem(KEY_STORAGE) || "";
    } catch (_e) {
      return window.__forgeKey || "";
    }
  }
  function setKey(k) {
    try {
      window.sessionStorage.setItem(KEY_STORAGE, k);
    } catch (_e) {
      window.__forgeKey = k;
    }
  }
  function clearKey() {
    try {
      window.sessionStorage.removeItem(KEY_STORAGE);
    } catch (_e) {
      /* ignore */
    }
    window.__forgeKey = "";
  }

  // Single shared prompt so concurrent callers don't stack overlays.
  let _pending = null;
  function promptForKey(message) {
    if (_pending) return _pending;
    _pending = new Promise((resolve) => {
      const overlay = document.createElement("div");
      overlay.style.cssText =
        "position:fixed;inset:0;z-index:9999;display:flex;align-items:center;" +
        "justify-content:center;background:rgba(8,8,10,0.82);" +
        "font:500 13px/1.5 ui-monospace,SFMono-Regular,Menlo,monospace;color:#e7e7ea;";
      const card = document.createElement("div");
      card.style.cssText =
        "min-width:320px;max-width:90vw;padding:24px;background:#141417;" +
        "border:1px solid #2a2a30;border-radius:10px;box-shadow:0 20px 60px rgba(0,0,0,0.5);";
      const title = document.createElement("div");
      title.textContent = "Sentinel — API key required";
      title.style.cssText = "font-size:14px;font-weight:700;margin-bottom:6px;";
      const hint = document.createElement("div");
      hint.textContent = message || "Enter the API key to access this demo.";
      hint.style.cssText = "color:#9a9aa2;margin-bottom:14px;";
      const input = document.createElement("input");
      input.type = "password";
      input.autocomplete = "off";
      input.placeholder = "X-API-Key";
      input.style.cssText =
        "width:100%;box-sizing:border-box;padding:9px 11px;background:#0d0d10;" +
        "border:1px solid #2a2a30;border-radius:6px;color:#e7e7ea;outline:none;";
      const err = document.createElement("div");
      err.style.cssText = "min-height:16px;margin-top:8px;color:#ff6b6b;font-size:12px;";
      const btn = document.createElement("button");
      btn.textContent = "Continue";
      btn.style.cssText =
        "margin-top:10px;width:100%;padding:9px;background:#d4fa50;color:#0d0d10;" +
        "border:0;border-radius:6px;font-weight:700;cursor:pointer;";
      // Validate the key against a gated endpoint; only close on success so a
      // wrong key keeps the modal open with an error instead of falling through
      // to a broken UI.
      const submit = async () => {
        const v = input.value.trim();
        if (!v) return;
        btn.disabled = true;
        btn.textContent = "Checking…";
        err.textContent = "";
        let ok = false;
        try {
          const resp = await fetch(API_BASE + VALIDATE_PATH, {
            headers: { Accept: "application/json", "X-API-Key": v },
          });
          ok = resp.ok;
        } catch (_e) {
          ok = false;
        }
        if (!ok) {
          err.textContent = "Invalid key — please try again.";
          btn.disabled = false;
          btn.textContent = "Continue";
          input.focus();
          input.select();
          return;
        }
        setKey(v);
        if (overlay.parentNode) overlay.parentNode.removeChild(overlay);
        _pending = null;
        resolve(v);
      };
      btn.addEventListener("click", submit);
      input.addEventListener("keydown", (e) => {
        if (e.key === "Enter") submit();
      });
      card.appendChild(title);
      card.appendChild(hint);
      card.appendChild(input);
      card.appendChild(err);
      card.appendChild(btn);
      overlay.appendChild(card);
      document.body.appendChild(overlay);
      input.focus();
    });
    return _pending;
  }

  async function ensureKey() {
    return getKey() || (await promptForKey());
  }

  async function getJSON(path, _retried) {
    const key = await ensureKey();
    const resp = await fetch(API_BASE + path, {
      headers: { Accept: "application/json", "X-API-Key": key },
    });
    if (resp.status === 401 && !_retried) {
      clearKey();
      await promptForKey("Invalid key — please try again.");
      return getJSON(path, true);
    }
    if (!resp.ok) throw new Error(`${path}: ${resp.status} ${resp.statusText}`);
    return resp.json();
  }

  // POST a JSON body, consume the SSE stream, call onEvent(obj) for each `data:` chunk.
  async function streamSSE(path, body, handlers, _retried) {
    const { onEvent, onDone, onError, signal } = handlers;
    const key = await ensureKey();
    let resp;
    try {
      resp = await fetch(API_BASE + path, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Accept: "text/event-stream",
          "X-API-Key": key,
        },
        body: JSON.stringify(body),
        signal,
      });
    } catch (err) {
      onError?.(err);
      return;
    }
    if (resp.status === 401 && !_retried) {
      clearKey();
      await promptForKey("Invalid key — please try again.");
      return streamSSE(path, body, handlers, true);
    }
    if (!resp.ok || !resp.body) {
      onError?.(new Error(`${path}: ${resp.status} ${resp.statusText}`));
      return;
    }
    const reader = resp.body.getReader();
    const decoder = new TextDecoder();
    let buffer = "";
    try {
      while (true) {
        const { done, value } = await reader.read();
        if (done) break;
        buffer += decoder.decode(value, { stream: true });
        let idx;
        while ((idx = buffer.indexOf("\n\n")) >= 0) {
          const chunk = buffer.slice(0, idx);
          buffer = buffer.slice(idx + 2);
          if (!chunk.startsWith("data: ")) continue;
          const payload = chunk.slice(6).trim();
          if (!payload) continue;
          try {
            const obj = JSON.parse(payload);
            if (obj.type === "all_done") {
              onDone?.();
              return;
            }
            onEvent?.(obj);
          } catch (err) {
            // ignore malformed lines
          }
        }
      }
      onDone?.();
    } catch (err) {
      onError?.(err);
    }
  }

  window.ForgeAPI = {
    getKbStats:     () => getJSON("/api/kb-stats"),
    getEvalResults: () => getJSON("/api/eval-results"),
    getDataset:     () => getJSON("/api/dataset"),
    getFindings:    () => getJSON("/api/findings"),
    streamAudit:    (message, graph_id, handlers) =>
      streamSSE("/api/audit/stream", { message, graph_id }, handlers),
    streamRace:     (message, question_id, handlers) =>
      streamSSE("/api/race/stream", { message, question_id }, handlers),
  };
})();
