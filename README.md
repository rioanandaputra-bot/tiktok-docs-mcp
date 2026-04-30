# tiktok-docs-mcp

> Mirror dokumentasi TikTok API ke lokal + SKILL.md untuk AI agent (Claude Code, MCP, Hermes, OpenClaw).

Dua script Python yang mengunduh seluruh dokumentasi TikTok ke disk lokal dalam format yang bisa dibaca agent. Tanpa browser, tanpa login, tanpa dependency eksternal.

| Script | Sumber | Output | Format |
|---|---|---|---|
| `scripts/developers_tiktok_com.py` | [developers.tiktok.com](https://developers.tiktok.com/doc/overview) | `docs/developers_tiktok_com/` | Markdown |
| `scripts/partner_tiktokshop_com.py` | [partner.tiktokshop.com](https://partner.tiktokshop.com/docv2/) | `docs/partner_tiktokshop_com/` | JSON |

---

## Mengapa Ini Dibutuhkan

Dokumentasi resmi TikTok di-render via JavaScript — tidak bisa diakses langsung oleh agent. Model AI juga sering memberikan jawaban usang karena API TikTok sering berubah. Project ini menyediakan snapshot statis yang bisa di-`cat`, `grep`, atau di-parse oleh tools apapun.

---

## Struktur

```
tiktok-docs-mcp/
├── README.md
├── SKILL.md                        # Instruksi untuk AI agent
├── LICENSE
├── .gitignore
├── scripts/
│   ├── developers_tiktok_com.py    # Downloader: Platform API → Markdown
│   └── partner_tiktokshop_com.py   # Downloader: Shop Partner API → JSON
└── docs/                           # Di-generate lokal, tidak di-commit
    ├── developers_tiktok_com/
    │   ├── _nav_tree.json
    │   └── ...
    └── partner_tiktokshop_com/
        ├── _tree_raw.json
        ├── _tree_structured.json
        └── ...
```

> `docs/` ada di `.gitignore`. Generate sendiri dengan menjalankan script.

---

## Quick Start

**Requirement:** Python 3.8+ — tidak ada dependency eksternal.

```bash
git clone https://github.com/your-username/tiktok-docs-mcp
cd tiktok-docs-mcp

# TikTok Platform API (developers.tiktok.com)
python scripts/developers_tiktok_com.py

# TikTok Shop Partner API (partner.tiktokshop.com)
python scripts/partner_tiktokshop_com.py
```

Kedua script mendukung **resume otomatis** — file yang sudah ada dilewati, aman untuk diinterupsi dan dijalankan ulang.

---

## Integrasi dengan AI Agent

### Claude Code

Tambahkan ke `CLAUDE.md` di root project:

```markdown
Dokumentasi TikTok API tersedia di `docs/`.
Baca `SKILL.md` sebelum menulis kode integrasi TikTok apapun.
```

Atau taruh `SKILL.md` di `.claude/skills/SKILL_tiktok.md` untuk dimuat otomatis.

### OpenClaw / Hermes Agent

```yaml
skills:
  - path: ./SKILL.md
    name: tiktok-docs
    trigger_keywords:
      - tiktok
      - tiktok shop
      - open.tiktokapis.com
      - tiktokglobalshop
```

### Agent MCP Lainnya

Arahkan agent ke `SKILL.md` sebagai context file. Skill ini berisi prosedur lookup endpoint, skema JSON, pola auth, dan daftar pitfall umum.

---

## Cakupan Dokumentasi

**TikTok Platform API** — Login Kit · Content Posting · Video · Live · Research · Account Management · Webhooks · Sandbox

**TikTok Shop Partner API** — Authorization · Product · Order · Logistics · Promotion · Fulfillment · Seller · Finance · Webhook

---

## Memperbarui Docs

```bash
python scripts/developers_tiktok_com.py
python scripts/partner_tiktokshop_com.py
```

Naikkan `DELAY_SECONDS` di dalam script jika terkena rate limit 429.

---

## Catatan

- Hanya mengunduh dokumentasi yang **dapat diakses publik**.
- Tidak memerlukan kredensial, token, atau data pribadi apapun.
- Rate limiting sudah built-in: `DELAY_SECONDS` + exponential backoff pada 429/5xx.

---

## License

MIT