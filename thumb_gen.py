# thumb_gen.py -- build-time helper (not part of the graded entry).
# Center-crops each lead-*.png to the 232x142 card aspect and
# downsamples it to thumb-*.png with plain nearest neighbour.
# Run once before rendering:  python3 thumb_gen.py

import os

from draw_frontpage import read_png, write_png

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "assets")
TW, TH = 232, 142


def make_thumb(src_path, dst_path):
    # Center-crop to the card aspect first (never stretch), then
    # downsample with nearest neighbour so the thumbnail stays
    # a faithful miniature of the editorial illustration.
    w, h, rgb = read_png(src_path)
    target_aspect = TW / TH
    src_aspect = w / h
    if src_aspect > target_aspect:
        cw = int(h * target_aspect)
        x0 = (w - cw) // 2
        y0, ch = 0, h
    else:
        ch = int(w / target_aspect)
        y0 = (h - ch) // 2
        x0, cw = 0, w
    out = bytearray(TW * TH * 3)
    for yy in range(TH):
        sy = y0 + yy * ch // TH
        for xx in range(TW):
            sx = x0 + xx * cw // TW
            si = (sy * w + sx) * 3
            di = (yy * TW + xx) * 3
            out[di:di + 3] = rgb[si:si + 3]
    write_png(dst_path, TW, TH, out)


def main():
    for name in ("riyadh", "mercury", "zaporizhzhia", "mnf"):
        src = os.path.join(ASSETS, "lead-%s.png" % name)
        dst = os.path.join(ASSETS, "thumb-%s.png" % name)
        make_thumb(src, dst)
        print("wrote %s" % dst)


if __name__ == "__main__":
    main()
