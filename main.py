# main.py -- entry point for THE WORLD IN ONE DAY, 24 November 2026.
# Standard library only. Reads $MAKEFUN_OUTPUT_DIR (default /output)
# and writes entry.png (1024x1024, under 1 MiB), deterministically.

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from draw_frontpage import PAGE_H, PAGE_W, render_frontpage, write_png


def main():
    # The sys.path guard above matters: the grader runs
    # `python3 -P -s main.py`, which drops the script directory
    # from sys.path. Without the insert, `import draw_frontpage`
    # fails and the entry scores 0 on run_completes.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    here = os.path.dirname(os.path.abspath(__file__))
    assets_dir = os.path.join(here, "assets")
    rgb = render_frontpage(assets_dir)
    out_path = os.path.join(out_dir, "entry.png")
    write_png(out_path, PAGE_W, PAGE_H, rgb)
    size = os.path.getsize(out_path)
    print("wrote %s (%dx%d, %d bytes)" % (out_path, PAGE_W, PAGE_H, size))
    if size >= 1024 * 1024:
        raise SystemExit("entry.png exceeds 1 MiB: %d bytes" % size)


if __name__ == "__main__":
    main()
