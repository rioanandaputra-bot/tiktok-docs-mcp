#!/usr/bin/env python3
"""
TikTok Shop Partner Documentation Downloader
=============================================
Sumber  : https://partner.tiktokshop.com/docv2/
Output  : docs/partner_tiktokshop_com/  (relatif terhadap root project)
Format  : JSON per dokumen, mengikuti hierarki tree dari API

Cara pakai (dari root project):
    python scripts/partner_tiktokshop_com.py

Endpoint yang digunakan:
  - /api_meta  → API Reference docs  (is_api_doc=True)
  - /detail    → Guide / panduan     (is_api_doc=False)

Fitur:
  - Unduh JSON lengkap untuk semua API Reference via /api_meta
  - Unduh JSON lengkap untuk semua Guide via /detail
  - Fallback ke metadata jika endpoint gagal (Shape C)
  - Penamaan file & folder menggunakan field "name" dari tree
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
from pathlib import Path

# ─── Konfigurasi ──────────────────────────────────────────────────────────────

AID    = "359713"
LOCALE = "en-US"

BASE         = "https://partner.tiktokshop.com/api/v1/document"
TREE_URL     = f"{BASE}/tree?workspace_id=3&aid={AID}&locale={LOCALE}"
API_META_URL = f"{BASE}/api_meta?src_document_id={{doc_path}}&aid={AID}&locale={LOCALE}"
API_DOC_URL  = f"{BASE}/detail?document_id={{doc_path}}&workspace_id=3&aid={AID}&locale={LOCALE}"

OUTPUT_DIR      = Path(__file__).parent.parent / "docs" / "partner_tiktokshop_com"
DELAY_SECONDS   = 0.35
TIMEOUT_SECONDS = 30
MAX_RETRIES     = 3

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept":          "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer":         "https://partner.tiktokshop.com/docv2/",
    "Origin":          "https://partner.tiktokshop.com",
}

# ─── Statistik ────────────────────────────────────────────────────────────────

stats = {
    "api_total":   0,
    "api_success": 0,
    "api_failed":  0,
    "api_skipped": 0,
    "doc_total":   0,
    "doc_success": 0,
    "doc_failed":  0,
    "doc_skipped": 0,
}

# ─── Helper ───────────────────────────────────────────────────────────────────

def safe_name(name: str, max_len: int = 100) -> str:
    s = re.sub(r'[\\/:*?"<>|【】]', "_", name)
    s = s.strip(". ")
    return s[:max_len] or "untitled"


def fetch_json(url: str, retries: int = MAX_RETRIES):
    for attempt in range(1, retries + 1):
        req = urllib.request.Request(url, headers=HEADERS)
        try:
            with urllib.request.urlopen(req, timeout=TIMEOUT_SECONDS) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                if data.get("code") == 0:
                    return data
                return None
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
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


# ─── Fetch tree ───────────────────────────────────────────────────────────────

def fetch_tree():
    print("Mengambil document tree dari API...")
    data = fetch_json(TREE_URL)
    if not data:
        raise RuntimeError("Gagal mengambil tree. Periksa koneksi internet.")
    nodes = data["data"]["document_tree"]
    print(f"  ✓  {len(nodes)} node ditemukan.\n")
    return nodes


# ─── Bangun hierarki ──────────────────────────────────────────────────────────

def build_hierarchy(flat_nodes):
    indexed = {n["document_id"]: {**n, "children": []} for n in flat_nodes}
    roots = []
    for node in indexed.values():
        pid = node.get("parent_id", "")
        if pid and pid in indexed:
            indexed[pid]["children"].append(node)
        else:
            roots.append(node)
    return roots


# ─── Fetch functions ──────────────────────────────────────────────────────────

def fetch_api_meta(doc_path: str):
    """Unduh API Reference doc via /api_meta (is_api_doc=True)."""
    url  = API_META_URL.format(doc_path=doc_path)
    data = fetch_json(url)
    return data.get("data") if data else None


def fetch_api_doc(doc_path: str):
    """Unduh Guide doc via /detail (is_api_doc=False)."""
    url  = API_DOC_URL.format(doc_path=doc_path)
    data = fetch_json(url)
    return data.get("data") if data else None


# ─── Proses node secara rekursif ──────────────────────────────────────────────

def process_node(node, parent_dir: Path, depth: int = 0):
    indent   = "  " * depth
    name     = node["name"]
    is_dir   = node.get("is_dir", 0)
    is_api   = node.get("is_api_doc", False)
    doc_path = node.get("document_path", "")
    children = node.get("children", [])

    summary = {
        "document_id":   node["document_id"],
        "name":          name,
        "is_dir":        is_dir,
        "is_api_doc":    is_api,
        "document_path": doc_path,
        "children":      [],
    }

    if is_dir:
        folder = parent_dir / safe_name(name)
        print(f"{indent}[DIR]  {name}/")
        for child in children:
            child_sum = process_node(child, folder, depth + 1)
            summary["children"].append(child_sum)
        return summary

    meta = {
        "document_id":   node["document_id"],
        "parent_id":     node.get("parent_id", ""),
        "name":          name,
        "document_path": doc_path,
        "is_api_doc":    is_api,
        "doc_type":      node.get("doc_type"),
        "update_time":   node.get("update_time"),
        "keywords":      [k["keyword"] for k in node.get("keywords", []) if k.get("keyword")],
    }

    filename  = safe_name(name) + ".json"
    file_path = parent_dir / filename

    if is_api:
        stats["api_total"] += 1

        if not doc_path:
            print(f"{indent}[API]  {name}  ⏩ skip (no document_path)")
            stats["api_skipped"] += 1
            return summary

        if file_path.exists():
            print(f"{indent}[API]  {name}  ✔ (resume)")
            stats["api_skipped"] += 1
            summary["local_file"] = str(file_path)
            return summary

        print(f"{indent}[API]  {name} ...", end="", flush=True)
        time.sleep(DELAY_SECONDS)

        detail = fetch_api_meta(doc_path)
        if detail:
            save_json(file_path, {"meta": meta, "detail": detail})
            print("  ✓")
            stats["api_success"] += 1
        else:
            print("  ✗ (gagal diunduh)")
            stats["api_failed"] += 1

        summary["local_file"] = str(file_path)

    else:
        stats["doc_total"] += 1

        if not doc_path:
            print(f"{indent}[DOC]  {name}  ⏩ skip (no document_path)")
            stats["doc_skipped"] += 1
            return summary

        if file_path.exists():
            print(f"{indent}[DOC]  {name}  ✔ (resume)")
            stats["doc_skipped"] += 1
            summary["local_file"] = str(file_path)
            return summary

        print(f"{indent}[DOC]  {name} ...", end="", flush=True)
        time.sleep(DELAY_SECONDS)

        detail = fetch_api_doc(doc_path)
        if detail:
            save_json(file_path, {"meta": meta, "detail": detail})
            print("  ✓")
            stats["doc_success"] += 1
        else:
            # Fallback Shape C: simpan metadata + URL untuk akses manual
            save_json(file_path, {
                "note": "Konten tidak tersedia via API publik. Metadata dari tree.",
                "url":  f"https://partner.tiktokshop.com/docv2/page/{doc_path}",
                "meta": meta,
            })
            print("  ✗ (gagal, metadata saja)")
            stats["doc_failed"] += 1

        summary["local_file"] = str(file_path)

    return summary


# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    print("=" * 65)
    print("  TikTok Shop Partner Docs Downloader")
    print(f"  Output  → {OUTPUT_DIR.resolve()}/")
    print("=" * 65 + "\n")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    nodes = fetch_tree()

    raw_path = OUTPUT_DIR / "_tree_raw.json"
    save_json(raw_path, {"document_tree": nodes})
    print(f"  Saved: {raw_path}\n")

    roots = build_hierarchy(nodes)

    structured = []
    for root in roots:
        summary = process_node(root, OUTPUT_DIR, depth=0)
        structured.append(summary)
        print()

    struct_path = OUTPUT_DIR / "_tree_structured.json"
    save_json(struct_path, {"tree": structured})
    print(f"\n  Saved: {struct_path}")

    print("\n" + "=" * 65)
    print("  SELESAI")
    print(f"  API Reference docs  : {stats['api_total']} total")
    print(f"    ✓ Berhasil        : {stats['api_success']}")
    print(f"    ✔ Resume (skip)   : {stats['api_skipped']}")
    print(f"    ✗ Gagal           : {stats['api_failed']}")
    print(f"  Guide docs          : {stats['doc_total']} total")
    print(f"    ✓ Berhasil        : {stats['doc_success']}")
    print(f"    ✔ Resume (skip)   : {stats['doc_skipped']}")
    print(f"    ✗ Gagal (metadata): {stats['doc_failed']}")
    if stats["api_failed"] or stats["doc_failed"]:
        print("  Tip: Jalankan ulang untuk retry yang gagal (resume otomatis).")
    print("=" * 65)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n  Dibatalkan. Output yang sudah ada tetap tersimpan.")
        sys.exit(0)
    except Exception as e:
        print(f"\n  ERROR: {e}")
        import traceback; traceback.print_exc()
        sys.exit(1)