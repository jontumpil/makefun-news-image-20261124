# THE WORLD IN ONE DAY — Tuesday 24 November 2026

**Tuesday 24 November 2026 — The World in One Day: 40 dated stories, 7 regions: Riyadh tower hit again, BepiColombo reaches Mercury, Zaporizhzhia struck**

[![news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/jontumpil/makefun-news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/jontumpil/makefun-news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124)

A one-day newspaper for the make.fun `news-image-20261124` bounty, revised
with the full day of Tuesday 24 November 2026: **40 dated stories across
7 regions** (North America, Latin America, Europe, Middle East, Africa,
Asia-Pacific, Science & Culture), with **four illustrated lead cards**.

## Date discipline

Every story in this edition is dated Tuesday 24 November 2026. Each item
carries a tag on the page itself:

- **CONFIRMED** — the source confirms the event happened on 24 Nov 2026.
- **REPORTED** — the story was first reported on 24 Nov 2026.

The front page carries a **DATE CHECK** box stating this rule, and every
story names its source. Nothing here is borrowed from an older date.

## How to run

Standard library only — no third-party packages, no Pillow.

```sh
python3 main.py            # writes entry.png (1024x1024) to $MAKEFUN_OUTPUT_DIR
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

The renderer is deterministic: two runs to different directories produce
byte-identical `entry.png` files (verified by sha256).

## Files

- `main.py` — entry point; reads `$MAKEFUN_OUTPUT_DIR`, writes `entry.png`.
- `draw_frontpage.py` — stdlib PNG reader/writer, 5x7 bitmap font, canvas,
  and the full front-page layout (masthead, lead cards, DATE CHECK box,
  three story columns).
- `stories.py` — the 40 dated stories with region, source, and tag, plus
  the four illustrated leads.
- `thumb_gen.py` — build-time helper that crops the lead art to thumbnails.
- `assets/lead-*.png` — four editorial illustrations (no text in the art).
- `assets/thumb-*.png` — 232x142 thumbnails composited onto the page.
- `entry.png` — locally rendered output (1024x1024, under 1 MiB).


## Sources (all items verified 25 Nov 2026 against the original reports)

- Just Security — Early Edition: November 24, 2026
- Reuters — Zaporizhzhia strike; Gaza strikes; MSCI Indonesia; Hasina return;
  Japan ICC contribution; Tigray/Amnesty; Lula fiscal package; Iraq oilfields
- BBC — Nvidia/Huang reinstatement; NATO space defence
- AP — Pentagon on Canada; South Korea ADIZ; Commanders–Bengals; Indonesia
  factory-fire toll update
- NPR / WEKU — Oregon and Virginia sue SpaceX over Grok deepfakes
- New York Times — Rep. Jimmy Gomez resignation
- Politico — ex-Hegseth aide Kaspar; Megaspeed blacklist (background)
- The Hindu BusinessLine — Trump to meet NATO chief Rutte
- ENNW (News from Non Aligned World) — Mexico captures "El Chapo Isidro";
  Mexico Textile Art Atlas
- The Rio Times — Ecuador floods; Peru dengue; Chile Delfina Guzman;
  Nigeria boycott; Ghana patrol (background); Senegal CAS ruling; WHO Cuba aid
- Kyiv Independent — Germany access to Ukraine Delta system
- h.ua — Russian drone over Poland; Zelensky US support; DESNA air defence
- AFP via Pakistan TV — Houthi strike on Riyadh PIF Tower; Hormuz tankers
- Geopolitiki — US Treasury Iran sanctions; Middle East live blog 24 Nov
- UN News — DR Congo Ituri Ebola responders
- IQMIA — Somalia/Uganda vs al-Shabaab; SpaceX lawsuits (summary)
- IDNFinancials / AmCham — Jakarta Composite Index +0.49% on 24 Nov
- Wall Street Journal via Just Security — South Korea AI exam-cheat rewards
- The Register / Physics World / ESA — BepiColombo safe in Mercury orbit
- Ungated — FIFA 2031 Women's World Cup hosts
- La Mediterranee — London exhibition; Indonesia factory fire (live feed)
