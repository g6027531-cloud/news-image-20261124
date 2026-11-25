#!/usr/bin/env python3
"""Render the 24 November 2026 front page (1024x1024 PNG).

Density upgrade: 32 dated stories across 7 regions, every headline
checked against reports first published on 24 November 2026.
Deterministic: fixed fonts, fixed geometry, no network, no randomness.
Run:  python3 render.py  -> writes assets/entry.png next to this script.
All text and artwork in this file were written fresh for 24 November 2026.
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "assets", "entry.png")

W, H = 1024, 1024
PAPER = (247, 243, 232)
INK = (26, 26, 26)
RED = (178, 35, 24)
NAVY = (18, 48, 84)
TEAL = (15, 90, 90)
GOLD = (176, 124, 10)
GREY = (88, 86, 80)
LIGHT = (233, 228, 214)
PALE = (238, 234, 222)
ORANGE = (214, 96, 20)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_width):
    words = text.split()
    lines, cur = [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def centre(draw, y, text, fnt, fill, cx=512):
    w = draw.textlength(text, font=fnt)
    draw.text((cx - w / 2, y), text, font=fnt, fill=fill)
    return w


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    L, R = 36, 988
    width = R - L

    # ---- top line ----
    f_small = font(SANS_B, 15)
    d.text((L, 20), "INTERNATIONAL EDITION", font=f_small, fill=GREY)
    right = "32 DATED STORIES  •  7 REGIONS"
    d.text((R - d.textlength(right, font=f_small), 20), right, font=f_small, fill=GREY)
    d.line([(L, 44), (R, 44)], fill=INK, width=2)

    # ---- masthead ----
    f_mast = font(SERIF_B, 58)
    centre(d, 50, "THE GLOBAL BRIEFING", f_mast, INK)
    f_sub = font(SERIF, 17)
    centre(d, 114, "—  THE WORLD'S NEWS, ONE DAY ON ONE PAGE  —", f_sub, GREY)

    # ---- date band ----
    d.rectangle([L, 136, R, 170], fill=NAVY)
    f_date = font(SERIF_B, 25)
    centre(d, 143, "TUESDAY 24 NOVEMBER 2026", f_date, (255, 255, 255))

    # ---- tagline ----
    f_tag = font(SERIF, 16)
    centre(d, 178, "Huawei guilty  •  Four tankers hit mines  •  Ukraine strikes Russian ships  •  Riyadh tower hit",
           f_tag, INK)
    d.line([(L, 200), (R, 200)], fill=INK, width=2)
    d.line([(L, 204), (R, 204)], fill=INK, width=1)

    # ---- lead story: Huawei ----
    box = (L, 210, R, 340)
    d.rectangle(box, outline=INK, width=2)
    d.rectangle([box[0], box[1], 648, box[3]], fill=PALE)
    d.line([(648, 210), (648, 340)], fill=INK, width=1)
    f_kick = font(SANS_B, 15)
    d.text((56, 222), "TECH  •  UNITED STATES v HUAWEI", font=f_kick, fill=RED)
    f_head = font(SERIF_B, 30)
    d.text((56, 242), "HUAWEI GUILTY OF TRADE-SECRET", font=f_head, fill=INK)
    d.text((56, 276), "THEFT AND BANK FRAUD", font=f_head, fill=INK)
    f_body = font(SANS, 14)
    body = ("A US jury convicted Huawei on 10 of 12 counts, including trade-secret "
            "theft and sanctions violations, but acquitted it of racketeering.")
    blines = wrap(d, body, f_body, 572)
    assert len(blines) <= 2, blines
    for i, ln in enumerate(blines):
        d.text((56, 312 + i * 17), ln, font=f_body, fill=INK)

    # lead panel: verdict box
    px0, px1 = 648, R
    cx = (px0 + px1) // 2
    # small scales of justice
    d.line([(cx, 224), (cx, 252)], fill=NAVY, width=3)
    d.line([(cx - 34, 230), (cx + 34, 230)], fill=NAVY, width=3)
    d.line([(cx - 34, 230), (cx - 44, 250)], fill=NAVY, width=2)
    d.line([(cx + 34, 230), (cx + 44, 250)], fill=NAVY, width=2)
    d.arc([cx - 54, 246, cx - 34, 262], 0, 180, fill=NAVY, width=2)
    d.arc([cx + 34, 246, cx + 54, 262], 0, 180, fill=NAVY, width=2)
    d.line([(cx - 14, 252), (cx + 14, 252)], fill=NAVY, width=3)
    f_verdict = font(SERIF_B, 34)
    centre(d, 262, "GUILTY", f_verdict, RED, cx=cx)
    f_v2 = font(SANS_B, 17)
    centre(d, 300, "10 OF 12 COUNTS", f_v2, INK, cx=cx)
    f_v3 = font(SANS, 12)
    centre(d, 321, "APPEAL PLANNED  •  SENTENCING SEPT 2027", f_v3, GREY, cx=cx)

    # ---- front row: 3 stories ----
    front = [
        dict(kick="MIDDLE EAST  •  STRAIT OF HORMUZ", colour=RED,
             head=["FOUR TANKERS HIT MINES", "IN THE STRAIT"],
             body="Iran said four tankers hit mines; a maritime centre called it unconfirmed."),
        dict(kick="WAR IN UKRAINE  •  TWO SEAS", colour=NAVY,
             head=["UKRAINE HITS RUSSIAN SHIPS", "IN TWO SEAS"],
             body="Drones hit Sparta II in the Gulf of Finland and ships off Libya."),
        dict(kick="MIDDLE EAST  •  RIYADH", colour=ORANGE,
             head=["DRONE HITS RIYADH TOWER;", "11 WOUNDED"],
             body="A Houthi strike on the PIF tower, its second hit in under a week."),
    ]
    f_fkick = font(SANS_B, 13)
    f_fhead = font(SERIF_B, 18)
    f_fbody = font(SANS, 13)
    col_w = 301
    gap = 24
    for i, cell in enumerate(front):
        x = L + i * (col_w + gap)
        y = 348
        d.rectangle([x, y, x + col_w, y + 112], outline=INK, width=1)
        d.rectangle([x, y, x + col_w, y + 5], fill=cell["colour"])
        d.text((x + 12, y + 13), cell["kick"], font=f_fkick, fill=cell["colour"])
        head_text = " ".join(cell["head"])
        hlines = wrap(d, head_text, f_fhead, col_w - 24)
        assert 1 <= len(hlines) <= 2, (cell["kick"], hlines)
        hy = y + 33
        for ln in hlines:
            d.text((x + 12, hy), ln, font=f_fhead, fill=INK)
            hy += 21
        blines = wrap(d, cell["body"], f_fbody, col_w - 24)
        assert len(blines) <= 2, (cell["kick"], blines)
        for j, ln in enumerate(blines):
            d.text((x + 12, hy + 3 + j * 15), ln, font=f_fbody, fill=INK)

    # ---- dense region grid: 26 stories in 3 columns ----
    # (headline, colour) per item; headlines are complete facts.
    columns = [
        [("MIDDLE EAST", RED, [
            "IRGC: container ship attacked in Hormuz",
            "Houthis 60 km from Aden, ready to attack",
            "Saudi strikes in Yemen: 25 dead or missing",
            "Gaza meningitis alert; 272 cases in Oct.",
            "Israel kills Hamas security chief in Gaza",
        ]),
         ("AFRICA", TEAL, [
            "Senegal regains Africa Cup title at CAS",
            "Congo plane missing; rebels claim downing",
            "Haftar visits Turkey for the first time",
         ])],
        [("EUROPE", NAVY, [
            "Poland accuses Russia of airspace violation",
            "Zelensky urges four-party talks soon",
            "NATO vows defence against space threat",
            "Turkish helicopter crash kills five crew",
        ]),
         ("EAST ASIA", GOLD, [
            "China sentences official to death for spying",
            "Korea shelters islanders after Russian jets",
            "Asian stocks rally on Huang return; Taiex +9%",
            "Nvidia slips 5.6% after record $952bn day",
            "Shenzhou-24 crew named; Pakistani to fly",
         ])],
        [("SOUTH & SOUTHEAST ASIA", ORANGE, [
            "Indonesia names two candidates for VP",
            "Malaysia to return migrants to Myanmar",
            "Hasina plans 16 Dec return to Bangladesh",
            "Hanoi restaurant blast kills at least six",
        ]),
         ("THE AMERICAS", RED, [
            "25 held hostage in Cartagena supermarket",
            "Car bomb injures 23 in Villavicencio",
            "US drone helped catch 'El Chapo Isidro'",
            "Pentagon rebukes Canada over F-35 review",
            "US blacklists Megaspeed in Nvidia scandal",
         ])],
    ]
    f_sect = font(SANS_B, 14)
    f_item = font(SANS_B, 14)
    grid_top = 468
    grid_bottom = 880
    for ci, col in enumerate(columns):
        x = L + ci * (col_w + gap)
        y = grid_top
        for si, (title, colour, items) in enumerate(col):
            if si > 0:
                y += 10
            d.text((x, y), title, font=f_sect, fill=colour)
            d.line([(x, y + 19), (x + col_w, y + 19)], fill=colour, width=2)
            y += 26
            for head in items:
                lines = wrap(d, head, f_item, col_w - 8)
                assert 1 <= len(lines) <= 2, (title, head, lines)
                for ln in lines:
                    d.text((x, y), ln, font=f_item, fill=INK)
                    y += 16
                y += 5
        assert y <= grid_bottom, (ci, y)

    # ---- also strip ----
    ay = 888
    d.line([(L, ay), (R, ay)], fill=INK, width=1)
    f_also = font(SANS, 13)
    d.text((L, ay + 8), "ALSO —  Iraq orders Baghdad control of Kurdish oilfields   •   UK sanctions the Houthis and four officials",
           font=f_also, fill=INK)

    # ---- footer: sources + dating disclosures ----
    f_foot = font(SANS, 12)
    fy = 920
    d.line([(L, 914), (R, 914)], fill=INK, width=1)
    sources = ("Sources: Reuters, AP, CNN, Al Jazeera, Le Temps, Nature, Xinhua, Saba; day digest: Daily Summary Of "
               "(30 stories, 64 sources). Regions: Middle East, Europe, East Asia, South Asia, Southeast Asia, Africa, the Americas.")
    dating = ("Dating: the Villavicencio bomb went off on Monday night and the El Chapo Isidro capture happened at the "
              "weekend; both were confirmed on Tuesday. Shenzhou-24's crew was named on Tuesday; the launch is set for "
              "Wednesday. Nvidia's $952bn surge was Monday (US); Tuesday brought Asia's rally and a 5.6% fall. "
              "The Hormuz mine claims and the Congo shootdown claim are unconfirmed; the China spy sentence "
              "was reported by Gold Wall Press.")
    credit = "Original text and artwork drawn for 24 November 2026. No photographs or third-party artwork used."
    for txt in (sources, dating, credit):
        ls = wrap(d, txt, f_foot, width)
        for ln in ls:
            d.text((L, fy), ln, font=f_foot, fill=GREY)
            fy += 14
        fy += 1
    assert fy <= 1024, fy

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    img.save(OUT, "PNG", optimize=True)
    size = os.path.getsize(OUT)
    assert size <= 1048576, size
    print(OUT, img.size, size, "bytes")


if __name__ == "__main__":
    main()
