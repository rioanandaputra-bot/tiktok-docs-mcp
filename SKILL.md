# SKILL: TikTok Documentation Reference
> **Untuk AI Agent** — Claude Code, OpenClaw, Hermes Agent, dan sistem agentic kompatibel MCP.

## Overview

Skill ini memberikan akses ke dua korpus dokumentasi TikTok yang tersimpan secara lokal:

| Sumber | Direktori | Format | Cakupan |
|---|---|---|---|
| `developers.tiktok.com` | `docs/developers_tiktok_com/` | `.md` | Platform API: Login, Video, Content, Live, Research |
| `partner.tiktokshop.com` | `docs/partner_tiktokshop_com/` | `.json` | Shop API: Order, Product, Auth, Webhook, Logistics |

**Selalu baca file docs yang relevan sebelum menulis kode integrasi TikTok.**

---

## 1. Layout File

### `docs/developers_tiktok_com/`
```
├── _nav_tree.json              ← Indeks navigasi lengkap
├── Overview.md
├── Login Kit/
│   └── *.md
├── Content Posting API/
│   └── *.md
├── Video API/
│   └── *.md
└── ...
```

### `docs/partner_tiktokshop_com/`
```
├── _tree_raw.json              ← Flat node list dari API
├── _tree_structured.json       ← Hierarki dengan field local_file
├── Partner Guide/
│   └── *.json
├── Developer Guide/
│   └── *.json
└── API Reference/
    ├── Authorization/
    ├── Product/
    ├── Order/
    └── ...
```

---

## 2. Skema JSON — Partner Docs

Setiap file `.json` di `partner_tiktokshop_com/` memiliki salah satu dari tiga bentuk:

**Shape A — API Reference** (`is_api_doc: true`)
```json
{
  "meta": { "name": "...", "is_api_doc": true, ... },
  "detail": {
    "api_info": { "method": "GET", "path": "/...", "version": "202309" },
    "request":  { "header": [...], "query": [...], "body": [...] },
    "response": { "fields": [...] },
    "error_codes": [...],
    "examples":  { "request": {}, "response": {} }
  }
}
```

**Shape B — Guide / Panduan** (`is_api_doc: false`)
```json
{
  "meta": { ... },
  "detail": { "content": "<HTML/Markdown>", "title": "..." }
}
```

**Shape C — Metadata Fallback** (fetch gagal)
```json
{
  "note": "Konten tidak tersedia via API publik.",
  "url":  "https://partner.tiktokshop.com/docv2/page/...",
  "meta": { ... }
}
```
> Jika menemukan Shape C, buka `url`-nya via fetch tool untuk konten live.

---

## 3. Prosedur Lookup

**Cari endpoint:**
```bash
grep -r "keyword" docs/partner_tiktokshop_com/API\ Reference/ --include="*.json" -l
# Buka file → ambil detail.api_info.method + path, detail.request, detail.error_codes
```

**Pahami alur autentikasi:**
```
1. docs/partner_tiktokshop_com/Developer Guide/Overview.json
2. docs/partner_tiktokshop_com/API Reference/Authorization/ (semua file)
3. docs/developers_tiktok_com/Login Kit/ (semua .md)
```

**Implementasi webhook:**
```
1. docs/partner_tiktokshop_com/Developer Guide/Webhook Guide.json
2. grep -r "webhook" docs/partner_tiktokshop_com/ --include="*.json" -il
```

**Video / Content API:**
```
1. docs/developers_tiktok_com/Content Posting API/*.md
2. docs/developers_tiktok_com/Video API/*.md
```

---

## 4. Konvensi Penting

### TikTok Platform API (`developers.tiktok.com`)
- **Base URL:** `https://open.tiktokapis.com/v2/`
- **Auth:** OAuth 2.0 — Authorization Code → Access Token → Refresh Token
- **Header:** `Authorization: Bearer <access_token>`
- **Scope** harus didaftarkan di app portal dan diminta saat auth

### TikTok Shop Partner API (`partner.tiktokshop.com`)
- **Base URL:** `https://open-api.tiktokglobalshop.com`
- **Auth:** Setiap request wajib memiliki `app_key`, `timestamp`, `access_token`, dan `sign`
- **Sign:** HMAC-SHA256 dari parameter yang diurutkan (baca Developer Guide untuk spec lengkap)
- **Versi API:** Ada di path, contoh `/product/202309/products`
- **Pagination:** Cursor-based via `page_token`
- **Response envelope:**
  ```json
  { "code": 0, "message": "Success", "request_id": "...", "data": {} }
  ```
  `code: 0` = sukses. Non-zero = error.

---

## 5. Pitfall Umum

| Masalah | Yang Harus Dicek |
|---|---|
| `sign` mismatch | Urutan sort param, exclude `access_token` dari sign, versi API |
| `access_token` expired | Implementasi refresh flow; token Platform API ~24 jam |
| Error permission / scope | Pastikan scope aktif di app + re-authorize user |
| Webhook signature invalid | Verifikasi header `x-tts-signature` — baca Webhook Guide |
| Data terpotong di list | Loop via `page_token` sampai kosong |

---

## 6. Checklist Sebelum Menulis Kode

- [ ] Sudah baca file doc endpoint yang relevan
- [ ] Catat HTTP method dan path lengkap termasuk versi
- [ ] List semua parameter **required** (header + query + body)
- [ ] Pahami response envelope dan error codes
- [ ] Verifikasi kebutuhan OAuth scope (Platform API)
- [ ] Verifikasi kebutuhan HMAC sign (Shop API)
- [ ] Handle pagination jika endpoint mengembalikan list
- [ ] Tambahkan retry logic untuk 429 / 5xx

---

## 7. Refresh Dokumentasi

```bash
python scripts/developers_tiktok_com.py
python scripts/partner_tiktokshop_com.py
```

Resume otomatis — file yang sudah ada dilewati. Naikkan `DELAY_SECONDS` jika terkena rate limit.

---

## 8. Trigger — Kapan Menggunakan Skill Ini

Aktifkan skill ini untuk task yang menyebut: TikTok API · TikTok Shop · Login Kit · Content Posting · Video API · `open.tiktokapis.com` · `tiktokglobalshop` · HMAC sign TikTok · TikTok webhook · TikTok OAuth