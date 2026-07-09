# tiktok-docs-mcp

> Mirror lokal dokumentasi TikTok API + skill siap pakai untuk AI agent (Claude Code, OpenClaw, Hermes, dan agent lain).

Dokumentasi resmi TikTok di-render via JavaScript — tidak bisa di-fetch langsung oleh agent, dan model AI sering menjawab dengan API usang. Repo ini berisi **snapshot statis yang sudah di-commit**, dikonsolidasikan menjadi file gabungan per kategori agar mudah di-`grep` dan hemat jumlah file, plus [`SKILL.md`](SKILL.md) berisi prosedur lookup untuk agent.

| Sumber | Direktori | Format |
|---|---|---|
| [developers.tiktok.com](https://developers.tiktok.com/doc/overview) — Platform API | `docs/developers_tiktok_com/` | `.md` per kategori |
| [partner.tiktokshop.com](https://partner.tiktokshop.com/docv2/) — Shop Partner API | `docs/partner_tiktokshop_com/` | `.json` per kategori (array record) |
| Node.js SDK TikTok Shop | `docs/partner_tiktokshop_com_sdk_models/` | `.ts` model per modul |

---

## Struktur

```
tiktok-docs-mcp/
├── SKILL.md                                  # Instruksi + prosedur lookup untuk AI agent
├── docs/
│   ├── developers_tiktok_com/                # Login_Kit.md, Content_Posting_API.md, Display_API.md, ...
│   ├── partner_tiktokshop_com/               # API_Reference.json, Developer_Guide.json, Webhooks.json, ...
│   └── partner_tiktokshop_com_sdk_models/    # product.ts, order.ts, finance.ts, ...
└── scripts/
    ├── developers_tiktok_com.py              # Downloader: Platform API → Markdown
    └── partner_tiktokshop_com.py             # Downloader: Shop Partner API → JSON
```

Skema tiap format dan cara lookup ada di [`SKILL.md`](SKILL.md).

---

## Instalasi — Claude Code

Skill di Claude Code = folder berisi `SKILL.md` di `~/.claude/skills/`:

```bash
git clone https://github.com/rioanandaputra-bot/tiktok-docs-mcp ~/.claude/skills/tiktok-docs
```

Restart session Claude Code — skill `tiktok-docs` otomatis terdeteksi dan aktif saat task menyentuh TikTok API / TikTok Shop.

Update:

```bash
git -C ~/.claude/skills/tiktok-docs pull
```

### Agent Lain (OpenClaw / Hermes / dsb.)

Arahkan agent ke `SKILL.md` sebagai context file, contoh konfigurasi:

```yaml
skills:
  - path: ./SKILL.md
    name: tiktok-docs
    trigger_keywords: [tiktok, tiktok shop, open.tiktokapis.com, tiktokglobalshop]
```

---

## Cakupan

**TikTok Platform API** — Login Kit · Content Posting · Display · Data Portability · Research Tools · Commercial Content · Share Kit · Embed · Mini Games/Dramas · Scopes · Account/App Management

**TikTok Shop Partner API** — Authorization · Product · Order · Fulfillment · Logistics · Finance · Promotion · Affiliate · Return/Refund · Customer Service · Webhooks (39 event) · Node.js SDK models

---

## Refresh Dokumentasi

Script mengunduh ulang dari sumber (Python 3.8+, tanpa dependency eksternal):

```bash
python scripts/developers_tiktok_com.py
python scripts/partner_tiktokshop_com.py
```

- **Resume otomatis** — file yang sudah ada dilewati, aman diinterupsi.
- Rate limiting built-in: `DELAY_SECONDS` + exponential backoff pada 429/5xx. Naikkan `DELAY_SECONDS` jika kena rate limit.
- Output script adalah struktur mentah per-file; jalankan langkah konsolidasi (merge per kategori) sebelum mengganti isi `docs/`, sesuai catatan di `SKILL.md` §7.

---

## Catatan

- Hanya mengunduh dokumentasi yang **dapat diakses publik** — tanpa kredensial, token, atau data pribadi.
- Snapshot bisa tertinggal dari docs live; cek `Changelog` di kedua korpus untuk perubahan terbaru.

## License

MIT
