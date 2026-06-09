#!/usr/bin/env python3
"""Fetch EU AI Act article texts from artificialintelligenceact.eu and write to markdown."""
import re
import time
import urllib.request
from html.parser import HTMLParser
from pathlib import Path


ARTICLES = {
    "Chapter I: General Provisions": [1, 2, 3, 4],
    "Chapter II: Prohibited AI Practices": [5],
    "Chapter III, Section 1: Classification of High-Risk AI Systems": [6, 7],
    "Chapter III, Section 2: Requirements for High-Risk AI Systems": [8, 9, 10, 11, 12, 13, 14, 15],
    "Chapter III, Section 3: Obligations of Providers and Deployers": [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27],
    "Chapter IV: Transparency Obligations": [50],
    "Chapter V: General-Purpose AI Models": [51, 52, 53, 54, 55, 56],
    "Chapter VI: Measures in Support of Innovation": [57, 60, 62],
    "Chapter IX, Section 1: Post-Market Monitoring": [72],
    "Chapter IX, Section 2: Serious Incidents": [73],
    "Chapter XII: Penalties": [99, 100, 101],
    "Chapter XIII: Final Provisions": [111, 113],
}

OUTPUT = Path(__file__).resolve().parent.parent / "data" / "regulations" / "eu_ai_act_full_text.md"


class ArticleParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_content = False
        self.in_h1 = False
        self.title = ""
        self.paragraphs = []
        self.current_text = []
        self.in_p = False
        self.skip_tags = {"script", "style", "nav", "footer", "header"}
        self.in_skip = 0

    def handle_starttag(self, tag, attrs):
        classes = dict(attrs).get("class", "")

        if tag in self.skip_tags:
            self.in_skip += 1
            return

        if tag == "div" and ("et_pb_post_content" in classes or "entry-content" in classes):
            self.in_content = True

        if not self.in_skip and self.in_content:
            if tag in ("p", "li"):
                self.in_p = True
                self.current_text = []

        if tag == "h1":
            self.in_h1 = True
            self.current_text = []

    def handle_endtag(self, tag):
        if tag in self.skip_tags:
            self.in_skip = max(0, self.in_skip - 1)
            return

        if tag == "h1" and self.in_h1:
            self.in_h1 = False
            self.title = "".join(self.current_text).strip()

        if self.in_content and tag in ("p", "li") and self.in_p:
            self.in_p = False
            text = "".join(self.current_text).strip()
            if text and len(text) > 5:
                self.paragraphs.append(text)

    def handle_data(self, data):
        if self.in_skip:
            return
        if self.in_h1 or self.in_p:
            self.current_text.append(data)


def fetch_article(n: int) -> tuple[str, str]:
    url = f"https://artificialintelligenceact.eu/article/{n}/"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            html = resp.read().decode("utf-8", errors="replace")
    except Exception as e:
        return f"Article {n}", f"[Fetch failed: {e}]"

    parser = ArticleParser()
    parser.feed(html)

    title = parser.title or f"Article {n}"
    title = re.sub(r"^Article\s*\d+\s*[–—-]\s*", "", title).strip()
    body = "\n\n".join(parser.paragraphs) if parser.paragraphs else "[No text extracted]"
    return title, body


def main():
    lines = ["# EU AI Act — Regulation (EU) 2024/1689\n"]
    lines.append("Full text of key articles for compliance auditing.")
    lines.append("Source: artificialintelligenceact.eu\n")
    lines.append("Entered into force: 1 August 2024. Fully applicable: 2 August 2026.")
    lines.append("For the complete regulation, see eu_ai_act_regulation_eu_2024_1689.pdf\n")

    total = sum(len(arts) for arts in ARTICLES.values())
    done = 0

    for chapter, article_nums in ARTICLES.items():
        lines.append(f"\n## {chapter}\n")
        for n in article_nums:
            done += 1
            print(f"[{done}/{total}] Fetching Article {n}...")
            title, body = fetch_article(n)
            lines.append(f"### Article {n} — {title}\n")
            lines.append(body)
            lines.append("")
            time.sleep(0.5)

    OUTPUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"\nDone. Wrote {OUTPUT} ({OUTPUT.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
