#!/usr/bin/env python3
"""
TikTok Developers Documentation Downloader
===========================================
Sumber  : https://developers.tiktok.com/doc/overview
Output  : docs/developers_tiktok_com/  (relatif terhadap root project)
Format  : Markdown (.md) per halaman, mengikuti hierarki navigasi situs

Cara pakai (dari root project):
    python scripts/developers_tiktok_com.py

Fitur:
  - Parsing navigasi dari HTML halaman overview
  - Konversi HTML → Markdown (heading, tabel, kode, link, list)
  - Resume otomatis — file yang sudah ada dilewati
  - Retry dengan exponential backoff pada error 429/5xx
  - Tidak memerlukan dependency eksternal (Python 3.8+ stdlib saja)
"""

import json
import re
import sys
import time
import urllib.request
import urllib.error
from html.parser import HTMLParser
from pathlib import Path

# ─── Konfigurasi ──────────────────────────────────────────────────────────────

BASE_URL   = "https://developers.tiktok.com"
START_URL  = f"{BASE_URL}/doc/overview"
OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "developers_tiktok_com"

DELAY_SECONDS   = 0.5
TIMEOUT_SECONDS = 30
MAX_RETRIES     = 3

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept":          "text/html,application/xhtml+xml,*/*",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer":         "https://developers.tiktok.com/",
}

stats = {"total": 0, "success": 0, "failed": 0, "skipped": 0}

# ─── Nav Parser ───────────────────────────────────────────────────────────────

class NavParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.items:     list[dict] = []
        self._depth_ul: int        = 0
        self._cur:      dict|None  = None
        self._capture:  bool       = False
        self._in_style: bool       = False

    def handle_starttag(self, tag, attrs):
        attr = dict(attrs)
        if tag == "style":
            self._in_style = True
            return
        if tag == "ul":
            self._depth_ul += 1
        elif tag == "a":
            href = attr.get("href", "").split("?")[0]
            if href.startswith("/doc/"):
                self._cur     = {"href": href, "label": "", "depth": self._depth_ul}
                self._capture = True

    def handle_endtag(self, tag):
        if tag == "style":
            self._in_style = False
            return
        if tag == "ul":
            self._depth_ul = max(0, self._depth_ul - 1)
        if tag == "a":
            if self._cur and self._cur["label"].strip():
                self.items.append(self._cur)
            self._cur     = None
            self._capture = False

    def handle_data(self, data):
        if self._in_style:
            return
        if self._capture and self._cur is not None:
            self._cur["label"] += data


# ─── HTML → Markdown ──────────────────────────────────────────────────────────

class HtmlToMarkdown(HTMLParser):
    SKIP_TAGS   = {"script", "style", "noscript", "svg", "path",
                   "nav", "header", "footer", "button", "form", "input"}
    HEADING_MAP = {"h1": "#", "h2": "##", "h3": "###",
                   "h4": "####", "h5": "#####", "h6": "######"}

    def __init__(self):
        super().__init__()
        self.lines:        list[str]  = []
        self.title:        str        = ""
        self._buf:         str        = ""
        self._skip:        int        = 0
        self._in_content:  bool       = False
        self._in_title:    bool       = False
        self._in_pre:      bool       = False
        self._heading:     str | None = None
        self._in_li:       bool       = False
        self._href:        str | None = None
        self._in_table:    bool       = False
        self._in_thead:    bool       = False
        self._in_th:       bool       = False
        self._in_td:       bool       = False
        self._row_cells:   list[str]  = []
        self._cell_buf:    str        = ""
        self._cell_href:   str | None = None
        self._header_done: bool       = False
        self._row_count:   int        = 0

    def _flush(self):
        t = self._buf.strip()
        if t:
            if self._heading:
                self.lines.append(f"{self._heading} {t}")
                self._heading = None
            elif self._in_li:
                self.lines.append(f"- {t}")
            else:
                self.lines.append(t)
        self._buf = ""

    def _flush_row(self):
        if not self._row_cells:
            return
        cells    = [re.sub(r' {2,}', ' ', c.strip()) for c in self._row_cells]
        row_line = "| " + " | ".join(cells) + " |"
        self.lines.append(row_line)
        is_header = self._in_thead or self._in_th or (
            not self._header_done and self._row_count == 1
        )
        if is_header and not self._header_done:
            self.lines.append("| " + " | ".join("---" for _ in cells) + " |")
            self._header_done = True
        self._row_cells = []
        self._cell_buf  = ""

    def handle_starttag(self, tag, attrs):
        attr = dict(attrs)
        cls  = attr.get("class", "")
        id_  = attr.get("id",    "")

        if tag == "title":
            self._in_title = True
            return

        if not self._in_content:
            if tag in ("main", "article"):
                self._in_content = True
            elif tag == "div" and any(
                kw in (cls + " " + id_).lower()
                for kw in ("doc-content", "article-content", "markdown-body",
                           "content-body", "doc-body", "main-content")
            ):
                self._in_content = True
            return

        if tag in self.SKIP_TAGS:
            self._skip += 1
            return
        if self._skip:
            return

        if tag == "table":
            self._flush()
            self._in_table    = True
            self._header_done = False
            self._row_count   = 0
            self.lines.append("")
            return

        if self._in_table:
            if tag == "thead":
                self._in_thead = True
            elif tag == "tbody":
                self._in_thead = False
            elif tag == "tr":
                self._row_cells = []
                self._cell_buf  = ""
                self._row_count += 1
            elif tag in ("th", "td"):
                self._cell_buf = ""
                self._in_th    = (tag == "th")
                self._in_td    = True
            elif self._in_td:
                if tag in ("b", "strong"):   self._cell_buf += "**"
                elif tag in ("i", "em"):     self._cell_buf += "_"
                elif tag == "code":          self._cell_buf += "`"
                elif tag == "br":            self._cell_buf += " "
                elif tag == "a":             self._cell_href = attr.get("href", "")
                elif tag in ("p", "div", "li", "dd", "dt"):
                    if self._cell_buf and not self._cell_buf.endswith(" "):
                        self._cell_buf += " "
            return

        if tag == "pre":
            self._flush()
            self._in_pre = True
            self._buf    = "\n```\n"
            return
        if tag == "code" and not self._in_pre:
            self._buf += "`"
            return

        if tag in self.HEADING_MAP:
            self._flush()
            self._heading = self.HEADING_MAP[tag]
            return

        if tag in ("p", "div", "section", "article", "main", "blockquote"):
            self._flush()
        elif tag == "li":
            self._flush()
            self._in_li = True
        elif tag == "br":
            self._buf += " "
        elif tag == "a":
            self._href = attr.get("href", "")
        elif tag in ("b", "strong"):
            self._buf += "**"
        elif tag in ("i", "em"):
            self._buf += "_"

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False
            return
        if tag in self.SKIP_TAGS:
            self._skip = max(0, self._skip - 1)
            return
        if self._skip:
            return

        if tag == "table":
            self._in_table = False
            self.lines.append("")
            return

        if self._in_table:
            if tag in ("thead", "tbody"):
                self._in_thead = False
            elif tag == "tr":
                self._flush_row()
            elif tag in ("th", "td"):
                self._row_cells.append(self._cell_buf)
                self._in_td = False
                self._in_th = False
            elif self._in_td:
                if tag in ("b", "strong"):   self._cell_buf += "**"
                elif tag in ("i", "em"):     self._cell_buf += "_"
                elif tag == "code":          self._cell_buf += "`"
                elif tag == "a":
                    if self._cell_href:
                        txt  = self._cell_buf.strip()
                        full = (BASE_URL + self._cell_href
                                if self._cell_href.startswith("/") else self._cell_href)
                        self._cell_buf = f"[{txt}]({full})" if txt else self._cell_buf
                    self._cell_href = None
                elif tag in ("p", "div"):
                    if self._cell_buf and not self._cell_buf.endswith(" "):
                        self._cell_buf += " "
            return

        if tag == "pre":
            self._buf += "\n```\n"
            self._flush()
            self._in_pre = False
            return
        if tag == "code" and not self._in_pre:
            self._buf += "`"
            return

        if tag in self.HEADING_MAP or tag in (
            "p", "div", "section", "article", "main", "li", "dt", "dd", "blockquote"
        ):
            self._flush()
            if tag == "li":
                self._in_li = False
            return

        if tag == "a":
            if self._href:
                t = self._buf.strip()
                if t:
                    full = (BASE_URL + self._href
                            if self._href.startswith("/") else self._href)
                    self._buf = f"[{t}]({full})"
            self._href = None
        elif tag in ("b", "strong"):
            self._buf += "**"
        elif tag in ("i", "em"):
            self._buf += "_"

    def handle_data(self, data):
        if self._in_title:
            self.title += data
            return
        if not self._in_content or self._skip:
            return
        if self._in_table and self._in_td:
            chunk = data.replace("\n", " ").replace("\t", " ")
            if chunk.strip():
                if self._cell_buf and not self._cell_buf.endswith((" ", "`", "_", "**")):
                    self._cell_buf += chunk
                else:
                    self._cell_buf += chunk.lstrip()
            return
        if self._in_pre:
            self._buf += data
        else:
            self._buf += data.replace("\n", " ")

    def get_markdown(self) -> str:
        self._flush()
        out, blank = [], 0
        for line in self.lines:
            if line.strip() == "":
                blank += 1
                if blank <= 1:
                    out.append("")
            else:
                blank = 0
                out.append(line)
        return "\n".join(out).strip()


# ─── Helper ───────────────────────────────────────────────────────────────────

def safe_name(name: str, max_len: int = 100) -> str:
    s = re.sub(r'[\\/:*?"<>|【】]', "_", name.strip())
    return (s.strip(". ") or "untitled")[:max_len]


def fetch_html(url: str, retries: int = MAX_RETRIES) -> str | None:
    for attempt in range(1, retries + 1):
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=TIMEOUT_SECONDS) as resp:
                charset = resp.headers.get_content_charset() or "utf-8"
                return resp.read().decode(charset, errors="replace")
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503, 504) and attempt < retries:
                wait = 2 ** attempt
                print(f"\n  [retry {attempt}] HTTP {e.code} → tunggu {wait}s...",
                      end="", flush=True)
                time.sleep(wait)
            else:
                return None
        except Exception:
            return None
    return None


def save_json(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


# ─── Dedup + build tree ───────────────────────────────────────────────────────

def dedup(items: list) -> list:
    seen, out = set(), []
    for it in items:
        if it["href"] in seen:
            continue
        label = it["label"].strip()
        if "{" in label or "}" in label:
            continue
        seen.add(it["href"])
        out.append(it)
    return out


def build_tree(flat: list) -> list:
    root:  list = []
    stack: list = []
    for item in flat:
        node = {**item, "children": []}
        while stack and stack[-1][0] >= item["depth"]:
            stack.pop()
        (stack[-1][1]["children"] if stack else root).append(node)
        stack.append((item["depth"], node))
    return root


# ─── Download satu halaman → .md ─────────────────────────────────────────────

def download(href: str, label: str, folder: Path, indent: str) -> None:
    md_path = folder / (safe_name(label) + ".md")
    stats["total"] += 1

    if md_path.exists():
        print(f"{indent}✔  {label}  (resume)")
        stats["skipped"] += 1
        return

    print(f"{indent}↓  {label} ...", end="", flush=True)
    time.sleep(DELAY_SECONDS)

    raw = fetch_html(BASE_URL + href)
    if not raw:
        print("  ✗")
        stats["failed"] += 1
        return

    conv = HtmlToMarkdown()
    conv.feed(raw)

    md_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.write_text(conv.get_markdown(), encoding="utf-8")
    print("  ✓")
    stats["success"] += 1


# ─── Rekursif proses tree ─────────────────────────────────────────────────────

def process(nodes: list, parent: Path, depth: int = 0) -> None:
    indent = "  " * depth
    for node in nodes:
        label    = node["label"].strip()
        children = node["children"]
        if children:
            folder = parent / safe_name(label)
            folder.mkdir(parents=True, exist_ok=True)
            print(f"{indent}[DIR]  {label}/")
            download(node["href"], label, folder, indent + "  ")
            process(children, folder, depth + 1)
        else:
            download(node["href"], label, parent, indent)


# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    print("=" * 65)
    print("  TikTok Developers Docs Downloader")
    print(f"  Output → {OUTPUT_DIR.resolve()}/")
    print("=" * 65 + "\n")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print("Mengambil navigasi...")
    overview = fetch_html(START_URL)
    if not overview:
        raise RuntimeError("Gagal fetch halaman overview.")

    np = NavParser()
    np.feed(overview)
    flat = dedup(np.items)

    if not flat:
        print("  ⚠  Fallback: ambil semua link /doc/* dari halaman")
        seen = set()
        for href in re.findall(r'href=["\'](/doc/[^"\'?#]+)["\']', overview):
            if href not in seen:
                seen.add(href)
                flat.append({
                    "href":  href,
                    "label": href.split("/")[-1].replace("-", " ").title(),
                    "depth": 1,
                })

    print(f"  ✓  {len(flat)} halaman ditemukan\n")

    tree = build_tree(flat)
    save_json(OUTPUT_DIR / "_nav_tree.json", {"tree": tree, "flat": flat})

    process(tree, OUTPUT_DIR)

    print("\n" + "=" * 65)
    print("  SELESAI")
    print(f"  Total   : {stats['total']}")
    print(f"  ✓ OK    : {stats['success']}")
    print(f"  ✔ Skip  : {stats['skipped']}")
    print(f"  ✗ Gagal : {stats['failed']}")
    if stats["failed"]:
        print("  Tip: Jalankan ulang untuk retry (resume otomatis).")
    print("=" * 65)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n  Dibatalkan. Output tersimpan.")
        sys.exit(0)
    except Exception as e:
        print(f"\n  ERROR: {e}")
        import traceback; traceback.print_exc()
        sys.exit(1)