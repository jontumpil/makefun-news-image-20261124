# draw_frontpage.py -- stdlib-only newspaper renderer.
# Reads the four thumbnail illustrations, draws the masthead,
# the four illustrated lead cards, the DATE CHECK box and the
# 40 dated stories in three columns, and writes a 1024x1024
# RGB PNG. No third-party code is used anywhere in this file.

import os
import struct
import zlib

from stories import LEADS, REGIONS, STORIES, TITLE

PAGE_W = 1024
PAGE_H = 1024

PAPER = (250, 248, 240)
INK = (22, 22, 22)
RED = (178, 34, 34)
GREY = (105, 105, 105)
LIGHT = (228, 224, 214)
NAVY = (24, 42, 78)


# ---------------------------------------------------------------- PNG reading
def _paeth(a, b, c):
    p = a + b - c
    pa = abs(p - a)
    pb = abs(p - b)
    pc = abs(p - c)
    if pa <= pb and pa <= pc:
        return a
    if pb <= pc:
        return b
    return c


def read_png(path):
    """Decode an 8-bit non-interlaced PNG into (w, h, rgb bytearray)."""
    raw = open(path, "rb").read()
    if raw[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("not a PNG file: " + path)
    pos = 8
    width = height = bitdepth = ctype = None
    palette = None
    trns = None
    idat = bytearray()
    while pos < len(raw):
        size, kind = struct.unpack(">I4s", raw[pos:pos + 8])
        data = raw[pos + 8:pos + 8 + size]
        pos += 12 + size
        if kind == b"IHDR":
            width, height, bitdepth, ctype, _cm, _fm, interlace = struct.unpack(
                ">IIBBBBB", data)
            if bitdepth != 8:
                raise ValueError("only 8-bit PNG supported: " + path)
            if interlace != 0:
                raise ValueError("interlaced PNG not supported: " + path)
        elif kind == b"PLTE":
            palette = data
        elif kind == b"tRNS":
            trns = data
        elif kind == b"IDAT":
            idat += data
        elif kind == b"IEND":
            break
    if ctype is None:
        raise ValueError("missing IHDR: " + path)
    channels = {0: 1, 2: 3, 3: 1, 4: 2, 6: 4}[ctype]
    stride = width * channels
    scan = zlib.decompress(bytes(idat))
    out = bytearray(width * height * 3)
    prev = bytearray(stride)
    p = 0
    for y in range(height):
        ftype = scan[p]
        p += 1
        line = bytearray(scan[p:p + stride])
        p += stride
        if ftype == 1:
            for i in range(channels, stride):
                line[i] = (line[i] + line[i - channels]) & 255
        elif ftype == 2:
            for i in range(stride):
                line[i] = (line[i] + prev[i]) & 255
        elif ftype == 3:
            for i in range(stride):
                a = line[i - channels] if i >= channels else 0
                line[i] = (line[i] + ((a + prev[i]) >> 1)) & 255
        elif ftype == 4:
            for i in range(stride):
                a = line[i - channels] if i >= channels else 0
                b = prev[i]
                c = prev[i - channels] if i >= channels else 0
                line[i] = (line[i] + _paeth(a, b, c)) & 255
        elif ftype != 0:
            raise ValueError("bad PNG filter %d in %s" % (ftype, path))
        for x in range(width):
            base = (y * width + x) * 3
            src = x * channels
            if ctype == 2:
                out[base:base + 3] = line[src:src + 3]
            elif ctype == 6:
                out[base:base + 3] = line[src:src + 3]
            elif ctype == 0:
                g = line[src]
                out[base] = g
                out[base + 1] = g
                out[base + 2] = g
            elif ctype == 3:
                pi = line[src] * 3
                out[base:base + 3] = palette[pi:pi + 3]
            elif ctype == 4:
                g = line[src]
                out[base] = g
                out[base + 1] = g
                out[base + 2] = g
        prev = line
    return width, height, out


# ---------------------------------------------------------------- PNG writing
def write_png(path, width, height, rgb):
    """Write an RGB bytearray as a deterministic PNG (filter 0)."""
    raw = bytearray()
    stride = width * 3
    for y in range(height):
        raw.append(0)
        raw += rgb[y * stride:(y + 1) * stride]
    comp = zlib.compress(bytes(raw), 9)

    def chunk(kind, data):
        out = struct.pack(">I", len(data)) + kind + data
        out += struct.pack(">I", zlib.crc32(kind + data) & 0xFFFFFFFF)
        return out

    ihdr = struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0)
    blob = b"\x89PNG\r\n\x1a\n"
    blob += chunk(b"IHDR", ihdr)
    blob += chunk(b"IDAT", comp)
    blob += chunk(b"IEND", b"")
    with open(path, "wb") as fh:
        fh.write(blob)


# ---------------------------------------------------------------- 5x7 font
# Each glyph is 7 rows of 5 pixels; '#' is ink, '.' is blank.
FONT = {
    "A": (".###.", "#...#", "#...#", "#####", "#...#", "#...#", "#...#"),
    "B": ("####.", "#...#", "#...#", "####.", "#...#", "#...#", "####."),
    "C": (".####", "#....", "#....", "#....", "#....", "#....", ".####"),
    "D": ("###..", "#..#.", "#...#", "#...#", "#...#", "#..#.", "###.."),
    "E": ("#####", "#....", "#....", "####.", "#....", "#....", "#####"),
    "F": ("#####", "#....", "#....", "####.", "#....", "#....", "#...."),
    "G": (".####", "#....", "#....", "#.###", "#...#", "#...#", ".###."),
    "H": ("#...#", "#...#", "#...#", "#####", "#...#", "#...#", "#...#"),
    "I": (".###.", "..#..", "..#..", "..#..", "..#..", "..#..", ".###."),
    "J": ("..###", "...#.", "...#.", "...#.", "...#.", "#..#.", ".##.."),
    "K": ("#...#", "#..#.", "#.#..", "##...", "#.#..", "#..#.", "#...#"),
    "L": ("#....", "#....", "#....", "#....", "#....", "#....", "#####"),
    "M": ("#...#", "##.##", "#.#.#", "#.#.#", "#...#", "#...#", "#...#"),
    "N": ("#...#", "##..#", "##..#", "#.#.#", "#..##", "#..##", "#...#"),
    "O": (".###.", "#...#", "#...#", "#...#", "#...#", "#...#", ".###."),
    "P": ("####.", "#...#", "#...#", "####.", "#....", "#....", "#...."),
    "Q": (".###.", "#...#", "#...#", "#...#", "#.#.#", "#..#.", ".##.#"),
    "R": ("####.", "#...#", "#...#", "####.", "#.#..", "#..#.", "#...#"),
    "S": (".####", "#....", "#....", ".###.", "....#", "....#", "####."),
    "T": ("#####", "..#..", "..#..", "..#..", "..#..", "..#..", "..#.."),
    "U": ("#...#", "#...#", "#...#", "#...#", "#...#", "#...#", ".###."),
    "V": ("#...#", "#...#", "#...#", "#...#", "#...#", ".#.#.", "..#.."),
    "W": ("#...#", "#...#", "#...#", "#.#.#", "#.#.#", "##.##", "#...#"),
    "X": ("#...#", "#...#", ".#.#.", "..#..", ".#.#.", "#...#", "#...#"),
    "Y": ("#...#", "#...#", ".#.#.", "..#..", "..#..", "..#..", "..#.."),
    "Z": ("#####", "....#", "...#.", "..#..", ".#...", "#....", "#####"),
    "0": (".###.", "#..##", "#.#.#", "##..#", "#...#", "#...#", ".###."),
    "1": ("..#..", ".##..", "..#..", "..#..", "..#..", "..#..", ".###."),
    "2": (".###.", "#...#", "....#", "...#.", "..#..", ".#...", "#####"),
    "3": ("####.", "....#", "....#", ".###.", "....#", "....#", "####."),
    "4": ("...#.", "..##.", ".#.#.", "#..#.", "#####", "...#.", "...#."),
    "5": ("#####", "#....", "####.", "....#", "....#", "#...#", ".###."),
    "6": (".###.", "#....", "#....", "####.", "#...#", "#...#", ".###."),
    "7": ("#####", "....#", "...#.", "...#.", "..#..", "..#..", "..#.."),
    "8": (".###.", "#...#", "#...#", ".###.", "#...#", "#...#", ".###."),
    "9": (".###.", "#...#", "#...#", ".####", "....#", "....#", ".###."),
    " ": (".....", ".....", ".....", ".....", ".....", ".....", "....."),
    ".": (".....", ".....", ".....", ".....", ".....", ".##..", ".##.."),
    ",": (".....", ".....", ".....", ".....", ".##..", ".##..", ".#..."),
    ":": (".....", ".##..", ".....", ".....", ".....", ".##..", ".##.."),
    ";": (".....", ".##..", ".....", ".....", ".##..", ".##..", ".#..."),
    "-": (".....", ".....", ".....", "#####", ".....", ".....", "....."),
    "(": ("...#.", "..#..", ".#...", ".#...", ".#...", "..#..", "...#."),
    ")": (".#...", "..#..", "...#.", "...#.", "...#.", "..#..", ".#..."),
    "'": ("..#..", "..#..", ".#...", ".....", ".....", ".....", "....."),
    "/": ("....#", "...#.", "...#.", "..#..", ".#...", ".#...", "#...."),
    "&": (".##..", "#..#.", "#.#..", ".#...", "#.#.#", "#..#.", ".##.#"),
    "%": ("#...#", "#..#.", "...#.", "..#..", ".#...", "#..#.", "#...#"),
    "+": (".....", "..#..", "..#..", "#####", "..#..", "..#..", "....."),
    "=": (".....", ".....", "#####", ".....", "#####", ".....", "....."),
    "!": ("..#..", "..#..", "..#..", "..#..", "..#..", ".....", "..#.."),
    "?": (".###.", "#...#", "....#", "...#.", "..#..", ".....", "..#.."),
    '"': (".#.#.", ".#.#.", ".#.#.", ".....", ".....", ".....", "....."),
    "$": ("..#..", ".####", "#.#.#", ".###.", "..#.#", "####.", "..#.."),
    "*": (".....", ".#.#.", "..#..", "#####", "..#..", ".#.#.", "....."),
    "#": (".#.#.", ".#.#.", "#####", ".#.#.", "#####", ".#.#.", ".#.#."),
    "@": (".###.", "#...#", "#.###", "#.#.#", "#.###", "#....", ".###."),
    "_": (".....", ".....", ".....", ".....", ".....", ".....", "#####"),
    "[": (".###.", ".#...", ".#...", ".#...", ".#...", ".#...", ".###."),
    "]": (".###.", "...#.", "...#.", "...#.", "...#.", "...#.", ".###."),
    "<": ("...#.", "..#..", ".#...", "#....", ".#...", "..#..", "...#."),
    ">": (".#...", "..#..", "...#.", "....#", "...#.", "..#..", ".#..."),
    "^": ("..#..", ".#.#.", ".....", ".....", ".....", ".....", "....."),
    "~": (".....", ".....", ".##.#", "#.#.#", ".....", ".....", "....."),
    "|": ("..#..", "..#..", "..#..", "..#..", "..#..", "..#..", "..#.."),
    "\\": ("#....", "#....", ".#...", "..#..", "...#.", "....#", "....#"),
    "`": (".#...", "..#..", "...#.", ".....", ".....", ".....", "....."),
    "{": ("...##", "..#..", "..#..", ".##..", "..#..", "..#..", "...##"),
    "}": ("##...", "..#..", "..#..", "..##.", "..#..", "..#..", "##..."),
}


def text_width(text, scale):
    return len(text) * 6 * scale


def wrap_text(text, max_chars):
    """Greedy word wrap; returns a list of lines, each <= max_chars."""
    words = text.split(" ")
    lines = []
    cur = ""
    for word in words:
        if not cur:
            cur = word
        elif len(cur) + 1 + len(word) <= max_chars:
            cur += " " + word
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


# ---------------------------------------------------------------- canvas
class Canvas:
    def __init__(self, width, height, bg):
        self.w = width
        self.h = height
        self.px = bytearray(width * height * 3)
        self.fill(bg)

    def fill(self, color):
        r, g, b = color
        for i in range(0, len(self.px), 3):
            self.px[i] = r
            self.px[i + 1] = g
            self.px[i + 2] = b

    def set_px(self, x, y, color):
        if 0 <= x < self.w and 0 <= y < self.h:
            i = (y * self.w + x) * 3
            self.px[i] = color[0]
            self.px[i + 1] = color[1]
            self.px[i + 2] = color[2]

    def rect(self, x, y, w, h, color):
        for yy in range(y, y + h):
            base = (yy * self.w + x) * 3
            for xx in range(w):
                i = base + xx * 3
                self.px[i] = color[0]
                self.px[i + 1] = color[1]
                self.px[i + 2] = color[2]

    def hline(self, x, y, w, color, thick=1):
        self.rect(x, y, w, thick, color)

    def frame(self, x, y, w, h, color, thick=1):
        self.hline(x, y, w, color, thick)
        self.hline(x, y + h - thick, w, color, thick)
        self.rect(x, y, thick, h, color)
        self.rect(x + w - thick, y, thick, h, color)

    def draw_text(self, x, y, text, scale, color):
        """Draw upper-cased ASCII text; unknown glyphs become spaces."""
        cx = x
        for ch in text.upper():
            glyph = FONT.get(ch, FONT[" "])
            for row in range(7):
                bits = glyph[row]
                for col in range(5):
                    if bits[col] == "#":
                        self.rect(cx + col * scale, y + row * scale,
                                  scale, scale, color)
            cx += 6 * scale
        return cx

    def draw_text_centered(self, y, text, scale, color):
        w = text_width(text, scale)
        self.draw_text((self.w - w) // 2, y, text, scale, color)

    def draw_wrapped(self, x, y, text, max_chars, scale, color, leading=9):
        lines = wrap_text(text, max_chars)
        for line in lines:
            self.draw_text(x, y, line, scale, color)
            y += leading
        return y

    def blit(self, img_w, img_h, img_rgb, dx, dy, dw, dh):
        """Nearest-neighbour scale of an RGB image onto the canvas."""
        for yy in range(dh):
            sy = min(img_h - 1, yy * img_h // dh)
            for xx in range(dw):
                sx = min(img_w - 1, xx * img_w // dw)
                si = (sy * img_w + sx) * 3
                self.set_px(dx + xx, dy + yy,
                            (img_rgb[si], img_rgb[si + 1], img_rgb[si + 2]))


# ---------------------------------------------------------------- layout
DATE_CHECK_TEXT = (
    "DATE CHECK: EVERY STORY IN THIS EDITION IS DATED TUESDAY 24 NOVEMBER "
    "2026. EACH ITEM IS TAGGED CONFIRMED WHEN THE EVENT HAPPENED ON 24 NOV, "
    "OR REPORTED WHEN IT WAS FIRST REPORTED ON 24 NOV. SOURCES ARE NAMED "
    "WITH EVERY STORY; NOTHING HERE IS BORROWED FROM AN OLDER DATE."
)

COLUMN_REGIONS = ((0, 1), (2, 3), (4, 5, 6))


def draw_masthead(cv):
    cv.draw_text_centered(16, "THE WORLD IN ONE DAY", 4, INK)
    cv.hline(28, 52, PAGE_W - 56, RED, 3)
    cv.draw_text_centered(62, "TUESDAY 24 NOVEMBER 2026  -  40 DATED STORIES  -  7 REGIONS",
                          2, NAVY)
    cv.draw_text_centered(88, "REVISED FULL-DAY EDITION  -  RIYADH TOWER HIT AGAIN  -  "
                          "BEPICOLOMBO REACHES MERCURY  -  ZAPORIZHZHIA STRUCK",
                          1, GREY)
    cv.hline(28, 108, PAGE_W - 56, INK, 2)


def draw_lead_cards(cv, assets_dir):
    card_w = 232
    gap = 12
    x0 = 30
    y = 124
    img_h = 142
    for i, (img, kicker, headline, caption) in enumerate(LEADS):
        cx = x0 + i * (card_w + gap)
        iw, ih, rgb = read_png(os.path.join(assets_dir, img))
        cv.blit(iw, ih, rgb, cx, y, card_w, img_h)
        cv.frame(cx, y, card_w, img_h, INK, 1)
        ty = y + img_h + 8
        cv.draw_text(cx, ty, kicker, 1, RED)
        ty += 11
        # Scale-2 glyphs are 12 px wide: a 232 px card fits 19 chars/line.
        ty = cv.draw_wrapped(cx, ty, headline, 19, 2, INK, leading=16)
        ty += 2
        cv.draw_wrapped(cx, ty, caption, 38, 1, GREY, leading=9)


def draw_date_check(cv):
    x, y, w, h = 28, 366, PAGE_W - 56, 44
    cv.frame(x, y, w, h, RED, 2)
    cv.rect(x + 2, y + 2, w - 4, h - 4, LIGHT)
    cv.draw_text(x + 10, y + 7, "DATE CHECK", 1, RED)
    cv.draw_wrapped(x + 92, y + 7, DATE_CHECK_TEXT, 138, 1, INK, leading=9)


def draw_story_columns(cv):
    col_w = 312
    gap = 18
    x0 = 26
    y_top = 426
    y_bottom = 1000
    for ci, region_ids in enumerate(COLUMN_REGIONS):
        cx = x0 + ci * (col_w + gap)
        y = y_top
        for rid in region_ids:
            cv.draw_text(cx, y, REGIONS[rid], 1, RED)
            cv.hline(cx, y + 10, col_w, RED, 1)
            y += 16
            for (r, headline, source, tag) in STORIES:
                if r != rid:
                    continue
                y = cv.draw_wrapped(cx + 10, y, headline, 50, 1, INK,
                                    leading=9)
                cv.draw_text(cx + 10, y, "-- " + source + " [" + tag + "]",
                             1, GREY)
                y += 12
            y += 6
        if y > y_bottom:
            raise ValueError("column %d overflowed: y=%d" % (ci, y))


def draw_footer(cv):
    cv.hline(28, 1006, PAGE_W - 56, INK, 2)
    cv.draw_text_centered(
        1012,
        "THE WORLD IN ONE DAY  -  TUESDAY 24 NOVEMBER 2026  -  "
        "40 STORIES  -  ALL DATED 24 NOV 2026",
        1, GREY)


def render_frontpage(assets_dir):
    cv = Canvas(PAGE_W, PAGE_H, PAPER)
    draw_masthead(cv)
    draw_lead_cards(cv, assets_dir)
    draw_date_check(cv)
    draw_story_columns(cv)
    draw_footer(cv)
    return cv.px
