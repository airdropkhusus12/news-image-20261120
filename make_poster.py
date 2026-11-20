#!/usr/bin/env python3
"""Draw the 20 November 2026 world-news poster (1024x1024 PNG).

Deterministic: fixed text, fixed layout, no network, no clock, no
randomness. Running this script twice produces byte-identical output.
The entrypoint (main.py) only copies the produced entry.png to
/output/entry.png; this script is the provenance of the image.

News verified 2026-11-20 from multiple outlets (One Turn, BBC via
Jabulani Radio, Le Monde, News Media House): the ICJ genocide ruling,
the Shenzhen three-way summit, Anthropic's Nasdaq debut and the AI
sell-off, the Houthi strike on Riyadh, the COP31 draft, and Kenya's
last Ebola patient. All are the top stories of Friday 20 Nov 2026.
"""

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024

NAVY = (14, 42, 71)
GOLD = (242, 194, 0)
RED = (192, 57, 43)
INK = (34, 34, 34)
GREY = (85, 85, 85)
LIGHT = (221, 221, 221)
WHITE = (255, 255, 255)
TEAL = (14, 124, 123)
PURPLE = (108, 52, 131)
ORANGE = (211, 84, 0)
GREEN = (30, 132, 73)

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Wrap text into lines that fit max_w pixels."""
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def main():
    img = Image.new("RGB", (W, H), WHITE)
    d = ImageDraw.Draw(img)

    # ---- Header band ----
    d.rectangle([0, 0, W, 150], fill=NAVY)
    d.text((48, 26), "WORLD NEWS", font=font(BOLD, 66), fill=WHITE)
    d.text((48, 100), "FRIDAY, 20 NOVEMBER 2026", font=font(BOLD, 34), fill=GOLD)
    d.rectangle([0, 150, W, 156], fill=GOLD)

    # ---- Lead story: ICJ genocide ruling ----
    y = 176
    d.text((48, y), "TOP STORY  •  THE HAGUE", font=font(BOLD, 20), fill=RED)
    y += 34
    headline = "World court: Myanmar guilty of genocide against the Rohingya"
    for line in wrap(d, headline, font(BOLD, 46), W - 96):
        d.text((48, y), line, font=font(BOLD, 46), fill=NAVY)
        y += 54
    y += 6
    summary = ("The International Court of Justice rules Myanmar committed "
               "genocide — the first such finding against a state.")
    for line in wrap(d, summary, font(REG, 22), W - 96):
        d.text((48, y), line, font=font(REG, 22), fill=GREY)
        y += 30
    y += 14
    d.line([48, y, W - 48, y], fill=LIGHT, width=2)
    y += 18

    # ---- Five more stories ----
    stories = [
        (TEAL, "2", "SHENZHEN  •  POLITICS",
         "Trump, Xi and Putin sign peace declaration",
         "First three-way summit ends with a four-point joint declaration."),
        (PURPLE, "3", "NEW YORK  •  MARKETS",
         "Anthropic soars on Nasdaq debut",
         "Shares close 17% above the IPO price; AI doubts drag world stocks down."),
        (ORANGE, "4", "RIYADH  •  CONFLICT",
         "Houthi missile damages Saudi wealth-fund tower",
         "Missiles hit the financial district; Iran war enters its ninth month."),
        (GREEN, "5", "ANTALYA  •  CLIMATE",
         "COP31 draft drops fossil-fuel phase-out",
         "Negotiators remove any reference to ending fossil fuel use."),
        (RED, "6", "NAIROBI  •  HEALTH",
         "Kenya's last Ebola patient goes home",
         "Discharged 37 days after the first case; the outbreak is over."),
    ]
    for color, num, tag, head, summ in stories:
        # Numbered badge
        d.rounded_rectangle([48, y, 96, y + 48], radius=8, fill=color)
        d.text((72, y + 8), num, font=font(BOLD, 28), fill=WHITE, anchor="ma")
        d.text((116, y + 2), tag, font=font(BOLD, 17), fill=color)
        d.text((116, y + 26), head, font=font(BOLD, 27), fill=NAVY)
        d.text((116, y + 60), summ, font=font(REG, 20), fill=GREY)
        y += 96

    # ---- Bottom market strip ----
    d.rectangle([0, 946, W, H], fill=NAVY)
    d.text((48, 962), "MARKETS", font=font(BOLD, 22), fill=GOLD)
    d.text((48, 990), "S&P 500  -2.0%   •   Nikkei  -4.8%   •   Fifth straight day of losses",
           font=font(REG, 20), fill=WHITE)

    img.save("entry.png", format="PNG")


if __name__ == "__main__":
    main()
