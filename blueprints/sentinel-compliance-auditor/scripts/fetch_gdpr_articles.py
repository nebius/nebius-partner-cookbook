#!/usr/bin/env python3
"""Fetch GDPR article texts from gdpr-info.eu and write to a markdown file."""
import re
import time
import urllib.request
from html.parser import HTMLParser
from pathlib import Path


ARTICLES = {
    "Chapter I: General Provisions": [1, 2, 3, 4],
    "Chapter II: Principles": [5, 6, 7, 8, 9, 10, 11],
    "Chapter III: Rights of the Data Subject": [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
    "Chapter IV: Controller and Processor": [24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43],
    "Chapter V: Transfers to Third Countries": [44, 45, 46, 47, 48, 49, 50],
    "Chapter VIII: Remedies, Liability and Penalties": [77, 78, 79, 80, 81, 82, 83, 84],
}

OUTPUT = Path(__file__).resolve().parent.parent / "data" / "regulations" / "gdpr_full_text.md"


class ArticleParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_entry = False
        self.in_h1 = False
        self.title = ""
        self.paragraphs = []
        self.current_text = []
        self.in_p = False
        self.depth = 0
        self.entry_depth = 0

    def handle_starttag(self, tag, attrs):
        classes = dict(attrs).get("class", "")
        if tag == "div" and "entry-content" in classes:
            self.in_entry = True
            self.entry_depth = self.depth
        if self.in_entry:
            if tag in ("p", "li"):
                self.in_p = True
                self.current_text = []
        if tag == "h1":
            self.in_h1 = True
            self.current_text = []
        if tag in ("div", "section", "article", "main", "header", "footer", "nav", "aside"):
            self.depth += 1

    def handle_endtag(self, tag):
        if tag in ("div", "section", "article", "main", "header", "footer", "nav", "aside"):
            self.depth -= 1
            if self.in_entry and self.depth < self.entry_depth:
                self.in_entry = False
        if tag == "h1" and self.in_h1:
            self.in_h1 = False
            self.title = "".join(self.current_text).strip()
        if self.in_entry and tag in ("p", "li") and self.in_p:
            self.in_p = False
            text = "".join(self.current_text).strip()
            if text:
                self.paragraphs.append(text)

    def handle_data(self, data):
        if self.in_h1 or self.in_p:
            self.current_text.append(data)


def fetch_article(n: int) -> tuple[str, str]:
    url = f"https://gdpr-info.eu/art-{n}-gdpr/"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            html = resp.read().decode("utf-8", errors="replace")
    except Exception as e:
        return f"Article {n}", f"[Fetch failed: {e}]"

    parser = ArticleParser()
    parser.feed(html)

    title = parser.title or f"Article {n}"
    title = re.sub(r"^Art\.\s*\d+\s*GDPR\s*[–—-]\s*", "", title).strip()
    body = "\n\n".join(parser.paragraphs) if parser.paragraphs else "[No text extracted]"
    return title, body


def main():
    lines = ["# GDPR — Regulation (EU) 2016/679\n"]
    lines.append("Full text of key articles. Source: gdpr-info.eu\n")
    lines.append("For the complete regulation including recitals, see gdpr_regulation_eu_2016_679.pdf\n")

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
