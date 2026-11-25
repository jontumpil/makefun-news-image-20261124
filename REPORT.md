# REPORT — news-image-20261124-r3 (revisi full-day 24 Nov 2026)

**Folder:** `~/workspace/makefun/bots/news-image-20261124-r3/`
**Repo tujuan (push oleh koordinator):** `jontumpil/makefun-news-image-20261124`
**Judul:** Tuesday 24 November 2026 — The World in One Day: 40 dated stories,
7 regions: Riyadh tower hit again, BepiColombo reaches Mercury, Zaporizhzhia struck
**Status:** Folder lengkap, render lokal terverifikasi. TIDAK di-push / bundle / submit
oleh builder (tugas koordinator).

## Isi edisi

- **40 cerita**, 7 region: Amerika Utara 8, Amerika Latin 5, Eropa 6,
  Timur Tengah 5, Afrika 5, Asia-Pasifik 6, Sains & Budaya 5.
- **4 kartu bergambar** (ilustrasi editorial tanpa teks, dibuat + di-commit
  sebagai aset): serangan Houthi ke menara PIF Riyadh; BepiColombo di orbit
  Merkurius; serangan ke Zaporizhzhia; kemenangan walk-off Commanders 22-20.
- **Kotak DATE CHECK** di halaman: semua cerita bertanggal 24 Nov 2026,
  tag CONFIRMED (peristiwa 24 Nov) / REPORTED (pertama diberitakan 24 Nov)
  per cerita, sumber disebut di tiap cerita.
- Disiplin tanggal: tidak ada cerita yang tanggal aslinya lebih tua dari
  edisi. Dua pembaruan yang rawan tanggal ditangani dengan benar: korban
  kebakaran pabrik Serang naik ke 26 (kebakaran 21 Nov, *update* 24 Nov —
  REPORTED) dan gugatan Grok (diajukan 23 Nov, diliput luas 24 Nov — REPORTED).

## 40 cerita + sumber + verifikasi tanggal

| # | Cerita | Sumber | Tag |
|---|--------|--------|-----|
| 1 | Trump orders DOJ to speed up federal death sentences | Just Security | REPORTED |
| 2 | Jensen Huang reinstated as Nvidia CEO after Trump lobbying | BBC | REPORTED |
| 3 | Oregon and Virginia sue SpaceX over Grok sex deepfakes | NPR | REPORTED |
| 4 | Pentagon: Canada falling short as North America defence partner | AP | REPORTED |
| 5 | Commanders stun Bengals 22-20 on walk-off field goal | AP | REPORTED |
| 6 | Rep. Jimmy Gomez to quit Congress after ethics findings | NYT | REPORTED |
| 7 | Ex-Hegseth aide Kaspar: defence chief should resign | Politico | REPORTED |
| 8 | Trump to meet NATO chief Rutte in Florida on Wednesday | Hindu BusinessLine | REPORTED |
| 9 | Mexico captures 'El Chapo Isidro' in deadly Sinaloa raid | ENNW | CONFIRMED |
| 10 | Lula backs second fiscal package to curb spending | Reuters | CONFIRMED |
| 11 | Ecuador town declares flood emergency as El Nino rains hit | Rio Times | CONFIRMED |
| 12 | Dengue deaths reach 45 in Peru's Lambayeque region | Rio Times | CONFIRMED |
| 13 | Chile mourns actress Delfina Guzman, dead at 98 | Rio Times | CONFIRMED |
| 14 | Russian strike on Zaporizhzhia kills 2, wounds 40 | Reuters | CONFIRMED |
| 15 | Germany first to access Ukraine's Delta battle system | Kyiv Independent | CONFIRMED |
| 16 | NATO vows to defend space after Russian nuclear satellite reports | BBC | REPORTED |
| 17 | Russian drone briefly enters Polish airspace | h.ua | CONFIRMED |
| 18 | Zelensky: seek more US help if peace deal fails | h.ua | CONFIRMED |
| 19 | Ukraine and Norway expand joint DESNA air defence | h.ua | CONFIRMED |
| 20 | Houthi strike hits Riyadh's tallest tower again, 11 hurt | AFP | CONFIRMED |

| 21 | Three tankers catch fire after hitting mines in Hormuz | Pakistan TV | CONFIRMED |
| 22 | Israeli strike kills Hamas security chief in Gaza | Reuters | CONFIRMED |
| 23 | US Treasury sanctions Iran shadow banking network | Geopolitiki | CONFIRMED |
| 24 | Iran vows 'all means' against US naval blockade | Reuters | CONFIRMED |
| 25 | Fighting traps Ebola responders in DR Congo's Ituri | UN News | CONFIRMED |
| 26 | Amnesty: Tigray strikes may be war crimes | Reuters | CONFIRMED |
| 27 | Nigeria opposition boycotts police security meeting | Rio Times | CONFIRMED |
| 28 | Somalia and Uganda step up fight against al-Shabaab | IQMIA | CONFIRMED |
| 29 | CAS hands Senegal back Africa Cup title | Rio Times | CONFIRMED |
| 30 | Russian jets enter South Korea air defence zone | AP | CONFIRMED |
| 31 | MSCI: no decision yet on Indonesia market downgrade | Reuters | CONFIRMED |
| 32 | Indonesia factory fire toll rises to 26 | AP | REPORTED |
| 33 | Japan to pay full 2027 ICC bill early | Reuters | CONFIRMED |
| 34 | Seoul offers $375,000 to catch AI exam cheats | WSJ | CONFIRMED |
| 35 | Hasina plans return to Bangladesh on Dec 16 | Reuters | CONFIRMED |
| 36 | BepiColombo safe in Mercury orbit after glitch | The Register | REPORTED |
| 37 | FIFA: four nations to host 2031 Women's World Cup | Ungated | REPORTED |
| 38 | Mexico launches Atlas of Textile Art | ENNW | CONFIRMED |
| 39 | London show tells capital's story from Romans to street art | La Mediterranee | CONFIRMED |
| 40 | WHO offers Cuba $2m in vaccines as health crisis bites | Rio Times | CONFIRMED |

Riset dilakukan 25 Nov 2026 pagi (WIB) dari Just Security Early Edition
24 Nov, The Global Eye, Reuters/AP/BBC/NPR, The Rio Times, h.ua, dan
Geopolitiki live blog — semuanya bertanggal 24 Nov 2026. Cerita sore/malam
24 Nov tercakup (serangan Riyadh 13:21–22:23 GMT, sanksi Treasury 17:02,
Katz soal senjata kimia 22:10, gugatan Grok dilaporkan 24 Nov pagi).

## Verifikasi teknis (lokal)

- `python3 -P -s main.py` (flag grader) — **berhasil**, guard `sys.path`
  di main.py bekerja.
- `entry.png`: **1024x1024, 363.376 byte (< 1 MiB)**.
- **Deterministik:** 2 run ke direktori berbeda menghasilkan sha256 identik:
  `48d14d5a7d69baf313722110713a91578240581a756e86088d1afe1a44fdaab4`.
- Stdlib only: `main.py` (os, sys), `draw_frontpage.py` (os, struct, zlib),
  `stories.py` (tanpa import), `thumb_gen.py` (os + modul sendiri).
  Tidak ada Pillow/pihak ketiga di kode yang dinilai.
- Render diperiksa visual: masthead, 4 kartu bergambar + judul 2 baris,
  kotak DATE CHECK, 3 kolom berisi 40 cerita + sumber + tag, footer.
  Satu cacat ditemukan dan diperbaiki: judul kartu skala 2 meluber —
  wrap diubah dari 38 ke 19 karakter per baris.
- Badge live (cek 25 Nov 2026 ~08:10 WIB, semua HTTP 200):
  `make.fun/badge/news-image-20261124.svg` (5.131 B),
  `.../jontumpil/makefun-news-image-20261124/rank.svg` (1.410 B),
  `.../jontumpil/makefun-news-image-20261124/reward.svg` (1.293 B).
- `.makefun/owner.json` valid: wallet
  `2NwLtDyTtBRV7QiMQMgeS8aWTJDFsMZyqNNMUigQ5Eip`.
- `LICENSE`: MIT + baris `SPDX-License-Identifier: MIT`, Copyright (c) 2026 jontumpil.

## File di folder

`main.py`, `draw_frontpage.py`, `stories.py`, `thumb_gen.py`, `README.md`,
`LICENSE`, `REPORT.md`, `entry.png`, `.makefun/owner.json`,
`assets/lead-{riyadh,mercury,zaporizhzhia,mnf}.png` (1920x1280),
`assets/thumb-{riyadh,mercury,zaporizhzhia,mnf}.png` (232x142).

## Aturan transkrip

Semua file ditulis fresh dengan tool tulis/edit di sesi ini; tidak ada file
entri lama yang dibaca. Setiap file disentuh ≥2 operasi tulis/edit di ≥2
pesan berbeda. Sesi ini berisi ≥5 giliran teks. Tidak ada push, bundle,
atau submit dari builder.
