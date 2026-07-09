---
name: tiktok-docs
description: Use this skill whenever a task involves the TikTok Platform API (developers.tiktok.com - Login Kit, Content Posting, Video/Display API, Research Tools, Mini Games/Dramas, Scopes) or the TikTok Shop Partner API (partner.tiktokshop.com - Orders, Products, Authorization, Webhooks, Logistics, Finance, Affiliate, Return/Refund, and the Node.js SDK). Provides consolidated local reference docs and TypeScript SDK models so integration code (auth, signing, endpoints, webhooks) can be written correctly without guessing field names or request shapes. Trigger on mentions of TikTok API, TikTok Shop, open.tiktokapis.com, tiktokglobalshop, HMAC sign TikTok, TikTok webhook, or TikTok OAuth.
---

# TikTok Documentation Reference
> **Untuk AI Agent** - Claude Code, OpenClaw, Hermes Agent, dan agent lain yang bisa membaca skill file.

## Overview

Skill ini memberikan akses ke dua korpus dokumentasi TikTok, dikonsolidasikan menjadi file-file gabungan (bukan lagi ribuan file kecil) agar ringkas dan mudah di-grep.

| Sumber | Direktori | Format | Cakupan |
|---|---|---|---|
| `developers.tiktok.com` | `docs/developers_tiktok_com/` | `.md` per kategori | Platform API: Login, Video, Content, Live, Research, dll |
| `partner.tiktokshop.com` (docs) | `docs/partner_tiktokshop_com/` | `.json` per kategori (array record) | Shop API: Order, Product, Auth, Webhook, Logistics, dll |
| `partner.tiktokshop.com` (SDK) | `docs/partner_tiktokshop_com_sdk_models/` | `.ts` per modul | Model TypeScript Node.js SDK, digabung per modul |

**Selalu baca file docs yang relevan sebelum menulis kode integrasi TikTok.**

> Semua path `docs/...` di bawah relatif terhadap direktori skill ini (base directory yang ditampilkan saat skill di-load), bukan working directory project.

---

## 1. Layout File

### `docs/developers_tiktok_com/`
Satu file `.md` per kategori top-level (contoh: `Login_Kit.md`, `Content_Posting_API.md`, `Display_API.md`, `Research_Tools.md`, dst). Tiap file berisi gabungan semua dokumen asli di kategori itu, dipisahkan dengan penanda:
```
---
## SOURCE: <path relatif file asli>
```

### `docs/partner_tiktokshop_com/`
Satu file `.json` per kategori (`API_Reference.json`, `Partner_Guide.json`, `Developer_Guide.json`, `Changelog.json`, `Webhooks.json`, `Terms_and_Policies.json`). Tiap file adalah **array of records**:
```json
[
  { "path": "Products/Create Product.json", "data": { "meta": {...}, "detail": {...} } },
  ...
]
```
Skema `data` per shape ada di Bagian 2.

### `docs/partner_tiktokshop_com_sdk_models/`
Satu file `.ts` per modul SDK (`product.ts`, `order.ts`, `returnRefund.ts`, `finance.ts`, `affiliate.ts`, `affiliateCreator.ts`, `affiliatePartner.ts`, `affiliateSeller.ts`, `analytics.ts`, `authorization.ts`, `customerService.ts`, `dataReconciliation.ts`, `event.ts`, `fulfillment.ts`, `logistics.ts`, `open.ts`, `promotion.ts`, `seller.ts`, `supplyChain.ts`), plus `_utils.ts` dan `_sdk_README.md`. Model didefinisikan sebagai **`export class`** (bukan `interface`) hasil OpenAPI Generator, lengkap dengan `attributeTypeMap` (mapping properti camelCase <-> field API snake_case). Tiap definisi diberi penanda:
```
// ==== SOURCE: <path relatif file asli> ====
```

---

## 2. Skema JSON - Partner Docs (di dalam field `data` tiap record)

**Shape A - API Reference** (`API_Reference.json`, `meta.is_api_doc: true`)
```json
{
  "meta": { "document_id": "...", "name": "Create Product", "document_path": "...", "is_api_doc": true, "keywords": [...], ... },
  "detail": {
    "document_id": "...",
    "document_api_meta": {
      "title": "...",
      "interface_path": "/product/202309/products",
      "method": 1,
      "query": "https://open-api.tiktokglobalshop.com/...?app_key=...&sign=...&timestamp=...",
      "request_header_param": [...],
      "request_query_param": [...],
      "request_body_param": [...],
      "response_param": [...],
      "request_body": "...", "response_body": "...",
      "error_code_list": [...]
    }
  }
}
```
`method` numerik: **1=POST, 2=GET, 3=PUT, 4=DELETE**. Versi API ada di `interface_path` (segmen `202309` dll). `query` adalah contoh URL lengkap.

**Shape B - Guide / Panduan** (file selain API_Reference, `meta.is_api_doc: false`)
```json
{ "meta": { ... }, "detail": { "title": "...", "content": "<HTML>", "doc_type": ..., "keywords": [...], "update_time": ..., "next_document_path": "...", "prev_document_path": "..." } }
```

**Shape C - Metadata Fallback** (fetch gagal; hanya segelintir record, mis. di `Developer_Guide.json`)
```json
{ "note": "Konten tidak tersedia via API publik.", "url": "https://partner.tiktokshop.com/docv2/page/...", "meta": { ... } }
```
> Jika menemukan Shape C, buka `url`-nya via fetch tool untuk konten live.

---

## 3. Prosedur Lookup

**Cari endpoint tertentu (mis. "Create Product"):** file JSON besar (satu baris), jangan di-Read langsung - parse per record:
```bash
python3 -c "
import json
data = json.load(open('docs/partner_tiktokshop_com/API_Reference.json'))
for r in data:
    if 'create product' in r['path'].lower():
        m = r['data']['detail']['document_api_meta']
        print(r['path'], {1:'POST',2:'GET',3:'PUT',4:'DELETE'}[m['method']], m['interface_path'])
        print(json.dumps(m['request_body_param'], indent=1)[:3000])
"
```
Daftar semua endpoint: loop record, print `r['path']` + `interface_path`.

**Cari model TypeScript (mis. product SKU):**
```bash
grep -n "class.*Sku" docs/partner_tiktokshop_com_sdk_models/product.ts
# Lalu Read file di sekitar line number match untuk lihat properti + attributeTypeMap
```

**Pahami alur autentikasi (Shop API):**
```
docs/partner_tiktokshop_com/Developer_Guide.json - record dengan path:
  "Get started/Authorization/..."                          -> alur OAuth shop
  "TikTok Shop API concepts/Sign your API request.json"    -> spec HMAC sign
  "Get started/Make your first API call/..."               -> contoh end-to-end
docs/partner_tiktokshop_com/API_Reference.json - filter path mengandung "Authorization"
```
Untuk Platform API: `docs/developers_tiktok_com/Login_Kit.md`.

**Implementasi webhook:**
```
1. docs/partner_tiktokshop_com/Webhooks.json (semua record)
2. grep -i "webhook" docs/partner_tiktokshop_com/Developer_Guide.json
```

**Video / Content API:**
```
1. docs/developers_tiktok_com/Content_Posting_API.md
2. docs/developers_tiktok_com/Display_API.md
```

---

## 4. Konvensi Penting

### TikTok Platform API (`developers.tiktok.com`)
- **Base URL:** `https://open.tiktokapis.com/v2/`
- **Auth:** OAuth 2.0 - Authorization Code -> Access Token -> Refresh Token
- **Header:** `Authorization: Bearer <access_token>`
- **Scope** harus didaftarkan di app portal dan diminta saat auth

### TikTok Shop Partner API (`partner.tiktokshop.com`)
- **Base URL:** `https://open-api.tiktokglobalshop.com`
- **Auth:** Setiap request wajib memiliki `app_key`, `timestamp`, `access_token`, dan `sign`
- **Sign:** HMAC-SHA256 dari parameter yang diurutkan (baca Developer_Guide.json untuk spec lengkap)
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
| Webhook signature invalid | Verifikasi header `x-tts-signature` - baca Webhooks.json |
| Data terpotong di list | Loop via `page_token` sampai kosong |

---

## 6. Checklist Sebelum Menulis Kode

- [ ] Sudah baca record/section doc endpoint yang relevan
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
Resume otomatis - file yang sudah ada dilewati. Naikkan `DELAY_SECONDS` jika terkena rate limit.

> Script menghasilkan struktur mentah per-file (ribuan file kecil). Jalankan langkah konsolidasi (merge per kategori sesuai layout Bagian 1) sebelum mengganti isi `docs/`, agar tetap ringkas dan mudah di-grep.

---

## 8. Trigger - Kapan Menggunakan Skill Ini

Aktifkan skill ini untuk task yang menyebut: TikTok API, TikTok Shop, Login Kit, Content Posting, Video API, `open.tiktokapis.com`, `tiktokglobalshop`, HMAC sign TikTok, TikTok webhook, TikTok OAuth
