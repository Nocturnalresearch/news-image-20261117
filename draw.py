#!/usr/bin/env python3
"""Draw the 17 November 2026 world-news front page (1024x1024 PNG).

A newspaper-style summary of the day's news, drawn with PIL vector shapes
and crisp text (no AI image generation, so no garbled text). Stories are the
real events of Tuesday 17 November 2026, researched from live news sources:
  1. U.S. strikes Iran (Qeshm Island) after tanker attacks in the Strait of Hormuz.
  2. Trump, Xi and Putin to meet Thursday at the APEC summit in Shenzhen.
  3. Ukraine strikes the Crimean Bridge; Russia hits Kyiv bridges and power.
  4. GTA VI launches tomorrow; leads The Game Awards with 8 nominations.
"""
import math
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
OUT = "entry.png"

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

NAVY = (22, 35, 63)
GOLD = (242, 193, 78)
RED = (178, 34, 34)
INK = (24, 24, 24)
GREY = (90, 90, 90)
PAPER = (250, 248, 242)
LINE = (200, 196, 186)


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap; returns list of lines that fit max_w."""
    lines, cur = [], ""
    for word in text.split(" "):
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def text_block(draw, x, y, text, fnt, fill, max_w, leading=1.25):
    """Draw wrapped text; returns y after the last line."""
    lines = wrap(draw, text, fnt, max_w)
    lh = int(fnt.size * leading)
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += lh
    return y


def burst(draw, cx, cy, r_out, r_in, n=12, fill=(255, 140, 0)):
    """Starburst (explosion) polygon."""
    pts = []
    for i in range(n * 2):
        r = r_out if i % 2 == 0 else r_in
        a = math.pi * i / n - math.pi / 2
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    draw.polygon(pts, fill=fill)


def draw_ship_scene(d, x0, y0, x1, y1):
    """Strait of Hormuz: night sea, tanker, explosion burst, jet."""
    d.rectangle([x0, y0, x1, y1], fill=(16, 42, 74))
    # sky stars
    for sx, sy in [(0.12, 0.12), (0.3, 0.07), (0.55, 0.15), (0.78, 0.08), (0.9, 0.18), (0.42, 0.2)]:
        d.ellipse([x0 + sx * (x1 - x0) - 2, y0 + sy * (y1 - y0) - 2,
                   x0 + sx * (x1 - x0) + 2, y0 + sy * (y1 - y0) + 2], fill=(220, 225, 235))
    # sea
    sea_y = y0 + int((y1 - y0) * 0.62)
    d.rectangle([x0, sea_y, x1, y1], fill=(10, 60, 96))
    for wy in (sea_y + 18, sea_y + 46, sea_y + 74):
        d.line([(x0 + 14, wy), (x1 - 14, wy)], fill=(90, 150, 200), width=3)
    # tanker: hull + deck + containers
    hx0, hx1 = x0 + 30, x1 - 90
    hy = sea_y - 26
    d.rectangle([hx0, hy, hx1, sea_y + 6], fill=(30, 30, 34))
    d.rectangle([hx0 + 18, hy - 34, hx0 + 120, hy], fill=(200, 60, 40))
    d.rectangle([hx0 + 130, hy - 34, hx0 + 210, hy], fill=(220, 180, 60))
    d.rectangle([hx0 + 220, hy - 34, hx0 + 280, hy], fill=(60, 140, 80))
    d.rectangle([hx1 - 46, hy - 58, hx1 - 10, hy], fill=(235, 235, 235))
    # explosion burst above the tanker
    burst(d, x1 - 120, y0 + 70, 52, 24, fill=(255, 140, 0))
    burst(d, x1 - 120, y0 + 70, 30, 14, fill=(255, 210, 60))
    # jet silhouette
    jx, jy = x0 + 70, y0 + 46
    d.polygon([(jx, jy), (jx + 46, jy + 8), (jx + 10, jy + 12), (jx + 4, jy + 22),
               (jx - 2, jy + 10), (jx - 34, jy + 16), (jx - 8, jy + 4)], fill=(225, 228, 235))


def draw_summit(d, x0, y0, x1, y1):
    """Three flags side by side: USA, China, Russia."""
    d.rectangle([x0, y0, x1, y1], fill=(240, 238, 230))
    w = (x1 - x0) // 3
    # USA
    ux = x0
    for i in range(7):
        d.rectangle([ux, y0 + i * (y1 - y0) // 7, ux + w, y0 + (i + 1) * (y1 - y0) // 7],
                    fill=(178, 34, 52) if i % 2 == 0 else (245, 245, 245))
    d.rectangle([ux, y0, ux + int(w * 0.55), y0 + int((y1 - y0) * 0.55)], fill=(30, 50, 110))
    # China
    cx = x0 + w
    d.rectangle([cx, y0, cx + w, y1], fill=(222, 41, 16))
    burst(d, cx + 26, y0 + 26, 12, 6, n=5, fill=(255, 222, 0))
    # Russia
    rx = x0 + 2 * w
    third = (y1 - y0) // 3
    d.rectangle([rx, y0, x1, y0 + third], fill=(245, 245, 245))
    d.rectangle([rx, y0 + third, x1, y0 + 2 * third], fill=(0, 57, 166))
    d.rectangle([rx, y0 + 2 * third, x1, y1], fill=(213, 0, 50))
    d.rectangle([x0, y0, x1, y1], outline=(120, 116, 108), width=2)


def draw_bridge(d, x0, y0, x1, y1):
    """Crimean Bridge over water with a blast on the deck."""
    d.rectangle([x0, y0, x1, y1], fill=(214, 228, 240))
    water_y = y0 + int((y1 - y0) * 0.68)
    d.rectangle([x0, water_y, x1, y1], fill=(70, 120, 170))
    for wy in (water_y + 14, water_y + 34):
        d.line([(x0 + 10, wy), (x1 - 10, wy)], fill=(150, 190, 220), width=3)
    # bridge deck + towers + cables
    deck_y = y0 + int((y1 - y0) * 0.52)
    d.rectangle([x0, deck_y, x1, deck_y + 12], fill=(60, 60, 66))
    for tx in (0.28, 0.72):
        cx = x0 + int(tx * (x1 - x0))
        d.rectangle([cx - 5, y0 + 12, cx + 5, deck_y], fill=(60, 60, 66))
        d.line([(cx, y0 + 14), (x0 + 8, deck_y)], fill=(120, 120, 126), width=2)
        d.line([(cx, y0 + 14), (x1 - 8, deck_y)], fill=(120, 120, 126), width=2)
    # blast on the deck
    burst(d, x0 + int(0.55 * (x1 - x0)), deck_y - 6, 40, 18, fill=(255, 140, 0))
    burst(d, x0 + int(0.55 * (x1 - x0)), deck_y - 6, 22, 10, fill=(255, 210, 60))
    # smoke
    for sx, sy, sr in [(0.5, 0.28, 14), (0.6, 0.2, 18), (0.68, 0.3, 12)]:
        d.ellipse([x0 + sx * (x1 - x0) - sr, y0 + sy * (y1 - y0) - sr,
                   x0 + sx * (x1 - x0) + sr, y0 + sy * (y1 - y0) + sr], fill=(120, 120, 124))


def draw_game(d, x0, y0, x1, y1):
    """GTA VI: neon VI on a dark Miami-night background."""
    d.rectangle([x0, y0, x1, y1], fill=(24, 10, 40))
    # sunset gradient bands
    bands = [(255, 94, 120), (255, 140, 90), (255, 190, 80), (180, 80, 200)]
    bh = (y1 - y0) // 4
    for i, col in enumerate(bands):
        d.rectangle([x0, y0 + i * bh, x1, y0 + (i + 1) * bh], fill=col)
    # sun
    cx = (x0 + x1) // 2
    d.ellipse([cx - 42, y0 + 26, cx + 42, y0 + 110], fill=(255, 240, 180))
    # skyline
    base = y1 - 34
    for bx, bw, bhgt in [(0.05, 0.12, 60), (0.2, 0.1, 86), (0.34, 0.14, 70), (0.52, 0.1, 96), (0.66, 0.12, 64), (0.82, 0.13, 80)]:
        d.rectangle([x0 + int(bx * (x1 - x0)), base - bhgt,
                     x0 + int((bx + bw) * (x1 - x0)), base], fill=(20, 8, 34))
    # big VI (kept inside the panel)
    f = font(SANS_B, 58)
    d.text((cx, y0 + 96), "VI", font=f, fill=(255, 255, 255),
           anchor="ma", stroke_width=3, stroke_fill=(140, 20, 90))


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    M = 24  # margin
    CW = W - 2 * M  # 976

    # ---- masthead ----
    d.rectangle([M, M, W - M, 140], fill=NAVY)
    d.text((W // 2, 34), "THE WORLD TODAY", font=font(SERIF_B, 50),
           fill=(255, 255, 255), anchor="ma")
    d.text((W // 2, 96), "TUESDAY, 17 NOVEMBER 2026", font=font(SANS_B, 34),
           fill=GOLD, anchor="ma")

    # ---- main story: U.S. strikes Iran ----
    y = 160
    d.rectangle([M, y, W - M, y + 8], fill=RED)  # red rule
    draw_ship_scene(d, M, y + 16, M + 436, y + 336)
    tx = M + 460
    tw = W - M - tx
    d.text((tx, y + 18), "MIDDLE EAST", font=font(SANS_B, 22), fill=RED)
    y2 = text_block(d, tx, y + 48, "U.S. STRIKES IRAN",
                    font(SANS_B, 56), NAVY, tw, leading=1.05)
    y2 = text_block(d, tx, y2 + 12,
                    "Warplanes hit a missile site on Qeshm Island after "
                    "attacks on tankers in the Strait of Hormuz. Trump says "
                    "reports of a possible \u2018dirty bomb\u2019 plot are "
                    "being taken seriously.",
                    font(SANS, 26), INK, tw, leading=1.3)

    # ---- divider ----
    dy = 516
    d.line([(M, dy), (W - M, dy)], fill=LINE, width=3)

    # ---- three panels ----
    gap = 16
    pw = (CW - 2 * gap) // 3  # 314
    panels = [
        ("SUMMIT IN CHINA",
         "Trump, Xi and Putin to meet Thursday at the APEC summit in Shenzhen \u2014 a first.",
         draw_summit),
        ("CRIMEAN BRIDGE HIT",
         "Ukraine strikes the bridge; Russia hits Kyiv bridges and power.",
         draw_bridge),
        ("GTA VI EVE",
         "Launches tomorrow; leads The Game Awards with 8 nominations.",
         draw_game),
    ]
    px = M
    for kicker, summary, scene in panels:
        scene(d, px, dy + 18, px + pw, dy + 188)
        yy = text_block(d, px, dy + 200, kicker, font(SANS_B, 24), RED, pw, leading=1.1)
        yy = text_block(d, px, yy + 8, summary, font(SANS, 23), INK, pw, leading=1.25)
        px += pw + gap

    # ---- footer ----
    d.line([(M, 992), (W - M, 992)], fill=LINE, width=2)
    d.text((W // 2, 998), "The day in one page  \u00b7  17 November 2026",
           font=font(SANS, 18), fill=GREY, anchor="ma")

    img.save(OUT, "PNG", optimize=True)
    print("saved", OUT)


if __name__ == "__main__":
    main()
