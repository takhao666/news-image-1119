#!/usr/bin/env python3
"""Draw the 19 November 2026 front page for news-image-1119.

One 1024x1024 PNG newspaper front page: a masthead naming the day,
a lead story, four illustrated panels, one wide panel and an
"Also today" strip. Every story was reported on 19 November 2026.
Run:  python3 render.py   (writes entry.png next to this file)
"""

from PIL import Image, ImageDraw, ImageFont

W = H = 1024
PAPER = (246, 241, 223)
INK = (22, 22, 22)
RED = (158, 27, 27)
BLUE = (31, 78, 121)
GOLD = (176, 138, 52)
TEAL = (38, 122, 106)
SKY = (178, 214, 235)
SEA = (46, 110, 158)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Greedy word wrap; returns a list of lines that fit `width`."""
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def block(draw, x, y, text, fnt, width, leading, fill=INK):
    """Draw wrapped text; returns the y just below the last line."""
    for line in wrap(draw, text, fnt, width):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def kicker(draw, x, y, text, color=RED):
    draw.text((x, y), text, font=font(SANS_B, 18), fill=color)
    return y + 24


def rule(draw, x0, y, x1, width=2, fill=INK):
    draw.line([(x0, y), (x1, y)], fill=fill, width=width)


def rich_item(draw, x, y, width, lead, rest, size=16, leading=20):
    """One 'Also today' item: bold lead-in, regular rest, wrapped to 2 lines."""
    fb, fr = font(SANS_B, size), font(SANS, size)
    tokens = [(w, fb) for w in lead.split()] + [(w, fr) for w in rest.split()]
    lines, cur, cur_w = [], [], 0.0
    for word, fnt in tokens:
        ww = draw.textlength(word + " ", font=fnt)
        if cur and cur_w + ww > width:
            lines.append(cur)
            cur, cur_w = [(word, fnt)], ww
        else:
            cur.append((word, fnt))
            cur_w += ww
    if cur:
        lines.append(cur)
    for line in lines:
        cx = x
        for word, fnt in line:
            draw.text((cx, y), word, font=fnt, fill=INK)
            cx += draw.textlength(word + " ", font=fnt)
        y += leading
    return y


# ---------------------------------------------------------------- icons
def icon_flags(draw, x, y, w, h):
    """Three flags (US, China, Russia) on poles above a skyline."""
    draw.rectangle([x, y, x + w, y + h], fill=(233, 226, 205),
                   outline=INK, width=2)
    base = y + h - 34
    draw.rectangle([x, base, x + w, y + h], fill=(214, 203, 175))
    for bx, bw, bh in [(8, 34, 26), (52, 26, 38), (92, 30, 20),
                       (136, 26, 34), (172, 30, 24)]:
        draw.rectangle([x + bx, base - bh, x + bx + bw, base],
                       fill=(120, 110, 88))
    fw, fh, gap = 52, 34, 14
    total = 3 * fw + 2 * gap
    fx = x + (w - total) // 2
    fy = y + 16
    for i in range(3):
        px = fx + i * (fw + gap)
        draw.line([(px + fw // 2, fy + fh), (px + fw // 2, base - 6)],
                  fill=INK, width=3)
    ux = fx
    for s in range(5):
        draw.rectangle([ux, fy + s * 7, ux + fw, fy + s * 7 + 4],
                       fill=RED if s % 2 == 0 else (245, 245, 245))
    draw.rectangle([ux, fy, ux + 22, fy + 16], fill=BLUE)
    for dx in (4, 11, 18):
        for dy in (4, 11):
            draw.ellipse([ux + dx, fy + dy, ux + dx + 3, fy + dy + 3],
                         fill=(255, 255, 255))
    cx = fx + fw + gap
    draw.rectangle([cx, fy, cx + fw, fy + fh], fill=(222, 41, 16))
    draw.ellipse([cx + 8, fy + 8, cx + 18, fy + 18], fill=(255, 222, 0))
    rx = fx + 2 * (fw + gap)
    for s, c in enumerate([(245, 245, 245), (0, 57, 166), (213, 0, 50)]):
        draw.rectangle([rx, fy + s * 12, rx + fw, fy + s * 12 + 11], fill=c)


def icon_bridge(draw, x, y, w, h):
    """An arched bridge over water, hit by a burst at mid-span."""
    import math
    draw.rectangle([x, y, x + w, y + h], fill=SKY, outline=INK, width=2)
    draw.rectangle([x, y + h - 26, x + w, y + h], fill=SEA)
    for wx in range(x + 8, x + w - 8, 22):
        draw.arc([wx, y + h - 20, wx + 16, y + h - 8], 0, 180,
                 fill=(255, 255, 255), width=2)
    draw.rectangle([x + 14, y + 30, x + 22, y + h - 26], fill=INK)
    draw.rectangle([x + w - 22, y + 30, x + w - 14, y + h - 26], fill=INK)
    draw.line([(x + 18, y + 30), (x + w // 2, y + 52)], fill=INK, width=3)
    draw.line([(x + w - 18, y + 30), (x + w // 2, y + 52)], fill=INK, width=3)
    draw.rectangle([x + 6, y + 56, x + w // 2 - 16, y + 64], fill=INK)
    draw.rectangle([x + w // 2 + 16, y + 56, x + w - 6, y + 64], fill=INK)
    cx, cy = x + w // 2, y + 46
    for ang in range(0, 360, 30):
        r1, r2 = 8, 26
        x1 = cx + r1 * math.cos(math.radians(ang))
        y1 = cy + r1 * math.sin(math.radians(ang))
        x2 = cx + r2 * math.cos(math.radians(ang))
        y2 = cy + r2 * math.sin(math.radians(ang))
        draw.line([(x1, y1), (x2, y2)], fill=(230, 120, 20), width=5)
    draw.ellipse([cx - 12, cy - 12, cx + 12, cy + 12], fill=(240, 170, 30),
                 outline=(200, 80, 10), width=2)


def icon_scales(draw, x, y, w, h):
    """Scales of justice."""
    draw.rectangle([x, y, x + w, y + h], fill=(233, 226, 205),
                   outline=INK, width=2)
    cx = x + w // 2
    draw.rectangle([cx - 3, y + 18, cx + 3, y + h - 30], fill=INK)
    draw.line([(x + 18, y + 30), (x + w - 18, y + 30)], fill=INK, width=4)
    draw.ellipse([cx - 7, y + 12, cx + 7, y + 26], fill=GOLD)
    for sx in (x + 24, x + w - 24):
        draw.line([(sx, y + 30), (sx - 16, y + 62)], fill=INK, width=2)
        draw.line([(sx, y + 30), (sx + 16, y + 62)], fill=INK, width=2)
        draw.arc([sx - 18, y + 56, sx + 18, y + 80], 0, 180, fill=GOLD, width=4)
    draw.rectangle([cx - 22, y + h - 30, cx + 22, y + h - 22], fill=INK)
    draw.rectangle([x + 16, y + h - 20, x + w - 16, y + h - 14], fill=INK)


def icon_chart(draw, x, y, w, h):
    """Rising market chart with an ANT ticker tag."""
    draw.rectangle([x, y, x + w, y + h], fill=(233, 226, 205),
                   outline=INK, width=2)
    draw.line([(x + 14, y + 14), (x + 14, y + h - 14)], fill=INK, width=2)
    draw.line([(x + 14, y + h - 14), (x + w - 10, y + h - 14)], fill=INK, width=2)
    pts = [(x + 18, y + h - 34), (x + 42, y + h - 52), (x + 60, y + h - 44),
           (x + 82, y + h - 66), (x + 104, y + h - 40), (x + w - 16, y + 26)]
    draw.line(pts, fill=TEAL, width=5, joint="curve")
    draw.polygon([(x + w - 16, y + 26), (x + w - 30, y + 28), (x + w - 18, y + 40)],
                 fill=TEAL)
    draw.text((x + 20, y + 12), "ANT", font=font(SANS_B, 26), fill=RED)


def icon_palms(draw, x, y, w, h):
    """Vice City: sunset, palms and a skyline."""
    import math
    draw.rectangle([x, y, x + w, y + h], fill=(255, 196, 120),
                   outline=INK, width=2)
    draw.ellipse([x + w // 2 - 26, y + 12, x + w // 2 + 26, y + 64],
                 fill=(240, 110, 60))
    base = y + h - 26
    for bx, bw, bh in [(6, 26, 30), (38, 20, 44), (64, 30, 24), (100, 22, 36)]:
        draw.rectangle([x + bx, base - bh, x + bx + bw, base], fill=(90, 60, 90))
    draw.rectangle([x, base, x + w, y + h], fill=(70, 45, 80))
    px, py = x + w - 34, y + h - 26
    draw.line([(px, py), (px + 6, py - 44)], fill=(60, 40, 20), width=5)
    for ang in (200, 240, 280, 320, 350):
        ex = px + 6 + 22 * math.cos(math.radians(ang))
        ey = py - 44 + 12 * math.sin(math.radians(ang))
        draw.line([(px + 6, py - 44), (ex, ey)], fill=(30, 120, 60), width=4)
    draw.text((x + 10, y + h - 30), "VI", font=font(SERIF_B, 26),
              fill=(255, 255, 255))


# ---------------------------------------------------------------- page
def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    M = 28  # margin
    d.rectangle([8, 8, W - 9, H - 9], outline=INK, width=3)
    d.rectangle([14, 14, W - 15, H - 15], outline=INK, width=1)

    # ---- masthead
    title = "THE WORLD TODAY"
    tf = font(SERIF_B, 62)
    tw = d.textlength(title, font=tf)
    d.text(((W - tw) / 2, 22), title, font=tf, fill=INK)
    rule(d, M, 100, W - M, 3)
    rule(d, M, 105, W - M, 1)
    date = "THURSDAY  ·  19 NOVEMBER 2026"
    df = font(SANS_B, 28)
    dw = d.textlength(date, font=df)
    d.text(((W - dw) / 2, 112), date, font=df, fill=RED)
    tag = "ONE DAY  ·  SIX STORIES  ·  THE WORLD IN A PAGE"
    tagf = font(SANS, 16)
    tagw = d.textlength(tag, font=tagf)
    d.text(((W - tagw) / 2, 144), tag, font=tagf, fill=INK)
    rule(d, M, 164, W - M, 3)

    # ---- lead story (174-374)
    lx, ly, lw, lh = M, 174, W - 2 * M, 200
    d.rectangle([lx, ly, lx + lw, ly + lh], outline=INK, width=2)
    d.rectangle([lx, ly, lx + lw, ly + lh], fill=(250, 246, 232))
    icon_flags(d, lx + lw - 252, ly + 12, 240, lh - 24)
    tx = lx + 16
    y = kicker(d, tx, ly + 10, "LEAD  —  SHENZHEN, CHINA")
    y = block(d, tx, y, "Trump, Xi and Putin meet today in first-ever trilateral",
              font(SERIF_B, 32), lw - 292, 40)
    block(d, tx, y + 4,
          "Xi Jinping hosts Donald Trump and Vladimir Putin at APEC for the "
          "first three-way meeting of the leaders of the three nuclear powers. "
          "Nuclear arms and Iran top the agenda; no deal is expected.",
          font(SANS, 20), lw - 292, 26)

    # ---- four illustrated panels, 2 x 2 (386-566, 578-758)
    gy, gh, gutter = 386, 180, 12
    pw = (W - 2 * M - gutter) // 2
    panels = [
        ("UKRAINE", "Crimean Bridge hit again",
         "Third attack this week halts traffic on the 19 km link to Crimea, "
         "days after a strike brought down a road span.", icon_bridge),
        ("THE HAGUE", "World Court rules on Rohingya genocide",
         "The ICJ delivers its verdict today in The Gambia's case against "
         "Myanmar. A first if it finds a state guilty of genocide.", icon_scales),
        ("MARKETS", "Anthropic debuts on Nasdaq",
         "Claude-maker Anthropic starts trading today as ANT, valued at about "
         "$1.4 trillion — set to be the biggest listing ever.", icon_chart),
        ("CULTURE", "GTA VI rolls out worldwide",
         "Rockstar's epic unlocks at midnight in each market, New Zealand "
         "first — 13 years after GTA V, and already a 99 on Metacritic.",
         icon_palms),
    ]
    for i, (kick, head, body, icon) in enumerate(panels):
        px = M + (i % 2) * (pw + gutter)
        py = gy + (i // 2) * (gh + gutter)
        d.rectangle([px, py, px + pw, py + gh], outline=INK, width=2)
        d.rectangle([px, py, px + pw, py + gh], fill=(250, 246, 232))
        icon(d, px + 12, py + 12, 110, gh - 24)
        tx = px + 134
        tw_ = pw - 146
        y = kicker(d, tx, py + 10, kick)
        y = block(d, tx, y, head, font(SERIF_B, 23), tw_, 28)
        block(d, tx, y + 2, body, font(SANS, 17), tw_, 21)

    # ---- wide panel: children in war (770-862)
    wy, wh = 770, 92
    d.rectangle([M, wy, W - M, wy + wh], outline=INK, width=2)
    d.rectangle([M, wy, W - M, wy + wh], fill=(250, 246, 232))
    d.text((M + 16, wy + 22), "589M", font=font(SERIF_B, 40), fill=RED)
    d.text((M + 195, wy + 10), "CHILDREN IN WAR", font=font(SANS_B, 18), fill=RED)
    block(d, M + 195, wy + 36,
          "A record 589 million children — nearly one in four worldwide — now live "
          "in conflict zones, the most since records began in 1990. (Save the Children)",
          font(SANS, 18), W - M - (M + 195) - 14, 23)

    # ---- also today strip (874-980)
    ay = 874
    d.text((M, ay), "ALSO TODAY", font=font(SANS_B, 18), fill=RED)
    rule(d, M + 118, ay + 10, W - M, 1)
    items = [
        ("Van Gogh sells for a record $190.4m", "at Sotheby's in New York."),
        ("Israeli tanks cross Gaza's Yellow Line,", "first ground raid since the 2025 ceasefire."),
        ("NASA confirms Voyager 1", "is now one light-day from Earth."),
        ("Iran says three tankers hit mines", "east of the Strait of Hormuz."),
    ]
    colw = (W - 2 * M) // 2
    for i, (lead, rest) in enumerate(items):
        ix = M + (i % 2) * colw
        iy = ay + 26 + (i // 2) * 44
        d.text((ix, iy), "•  ", font=font(SANS_B, 16), fill=RED)
        rich_item(d, ix + 16, iy, colw - 32, lead, rest)

    # ---- footer
    rule(d, M, 988, W - M, 1)
    foot = "All stories reported on 19 November 2026  ·  Sources: NYT · Reuters · CNA · Al Jazeera · BBC · ReliefWeb"
    ff = font(SANS, 13)
    fw = d.textlength(foot, font=ff)
    d.text(((W - fw) / 2, 994), foot, font=ff, fill=(90, 90, 90))

    img.save("entry.png", optimize=True)
    print("saved entry.png")


if __name__ == "__main__":
    main()
