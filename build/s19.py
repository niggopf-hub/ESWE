# -*- coding: utf-8 -*-
"""Slide 19 — Mögliche strategische Ziele (Pendant evm S. 19)."""
from deck import *

HEADER = '3. Diskussion möglicher Handlungsoptionen'
SOURCES = ('Quellen: Metzler-Recherche, Jahresabschlüsse ESWE Versorgungs AG 2024–2025, '
           'Unternehmenswebsite')

ZIELE = [
    # (Seite, Bandmitte, Text, Farbe, Icon, Icon-Rect)
    ('l', 184.8, 'Erweiterung des Fremdfinanzierungsspielraums zur Umsetzung des '
     'Investitionsprogramms', rgb(0x003D7C), 'ziel1.png', (56.1, 166.4, 41.2, 38.0)),
    ('r', 184.8, 'Stärkung der Eigenkapitalbasis zur dauerhaften Sicherung der '
     'Ziel-EK-Quote von über 25 %', rgb(0x3157E3), 'ziel2.png', (756.6, 165.1, 32.4, 40.5)),
    ('l', 327.0, 'Teilung von Kapitalbedarf und Projektrisiken bei größeren '
     'Investitionsvorhaben', rgb(0x808080), 'ziel3.png', (55.0, 312.3, 43.4, 29.3)),
    ('r', 327.0, 'Freisetzung gebundenen Kapitals aus ausgewählten Assets und '
     'Beteiligungen', rgb(0x718BEB), 'ziel4.png', (761.9, 311.4, 22.4, 31.1)),
    ('l', 470.0, 'Ausbau der regionalen Marktposition durch gezielte Akquisitionen und '
     'Beteiligungen', rgb(0xA5CAFB), 'ziel5.png', (59.5, 453.5, 34.5, 32.8)),
    ('r', 470.0, 'Erweiterung bestehender Energie- und Wärmeplattformen um zusätzliche '
     'Kompetenzen und Kunden', rgb(0x67A6F9), 'ziel6.png', (748.5, 451.8, 36.7, 36.2)),
]


def build(prs):
    s = blank(prs)
    chrome(s, 19, HEADER, SOURCES)
    title_2lines(s, 'Verschiedene Handlungsoptionen für die zukünftige Positionierung der ESWE')

    oval(s, 421.0, 334.45, 206.2, 206.1, fill=rgb(0xE3E8FB))
    for y in (255.5, 398.4):
        hline(s, 72.3, 769.7, y, DARK, 1.0, dash=True)
    textbox(s, 321.0, 279.0, 200, 34,
            [[Run('Mögliche strategische', F_TWO, 14.0, DARK, True)],
             [Run('Ziele', F_TWO, 14.0, DARK, True)]],
            anchor='m', align=PP_ALIGN.CENTER, line=15.8)
    picture(s, 'eswe_logo.png', 371.0, 341.0, 100.0, 100.0 * 517 / 1233.0)

    for side, cy, txt, col, icon, (ix, iy, iw, ih) in ZIELE:
        x = 120.5 if side == 'l' else 534.5
        ls = wrap(txt, 172, 12.0, bold=True)
        y0 = cy - len(ls) * 14.4 / 2.0
        textbox(s, x, y0, 178, len(ls) * 14.4 + 4,
                [[Run(l, F_TWO, 12.0, col, True)] for l in ls], line=14.4)
        picture(s, icon, ix, iy, iw, ih)
    return s
