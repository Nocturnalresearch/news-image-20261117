#!/usr/bin/env python3
"""Entry program for news-image-20261117.

Copies the pre-drawn front-page image (entry.png, drawn by draw.py from
researched real news of Tuesday 17 November 2026) to /output/entry.png.
Deterministic: the same bytes on every run. Standard library only, no network.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dst)
    size = os.path.getsize(dst)
    if size > 1048576:
        print(f"entry.png too large: {size} bytes", file=sys.stderr)
        return 1
    # Validate: PNG magic bytes + 1024x1024 dimensions (read from the IHDR).
    with open(dst, "rb") as f:
        head = f.read(33)
    if head[:8] != b"\x89PNG\r\n\x1a\n":
        print("entry.png is not a PNG", file=sys.stderr)
        return 1
    width = int.from_bytes(head[16:20], "big")
    height = int.from_bytes(head[20:24], "big")
    if (width, height) != (1024, 1024):
        print(f"entry.png is {width}x{height}, expected 1024x1024", file=sys.stderr)
        return 1
    print(f"wrote {dst} ({size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
