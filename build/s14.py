# -*- coding: utf-8 -*-
"""Slide 14 — Aktionärs- und Beteiligungsstruktur (Pendant evm S. 14)."""
from deck import *

HEADER = '2. ESWE Versorgungs AG – Übersicht und Herausforderungen'
SOURCES = ('Quellen: Metzler-Recherche, Geschäftsbericht ESWE Versorgungs AG 2025, '
           'Unternehmenswebsite')
FN = ('1) Unmittelbare Beteiligungsquoten der ESWE Versorgungs AG zum 31. Dezember 2025, '
      'weitere geringfügige Beteiligungen existieren; Zuordnung der Geschäftsfelder auf Basis '
      'der Tätigkeit der jeweiligen Gesellschaft durch Metzler; 2) Mitgesellschafter je 5 %: '
      'MBA Wiesbaden GmbH und Knettenbrech + Gurdulic; 3) Übrige 50 %: Mainzer Stadtwerke AG; '
      '4) Mitgesellschafter: Knettenbrech + Gurdulic 51 %, ENTEGA 24,5 %')

FN = ('1) Unmittelbare Beteiligungsquoten der ESWE Versorgungs AG zum 31. Dezember 2025; Zuordnung der '
      'Geschäftsfelder durch Metzler; 2) Mitgesellschafter je 5 %: MBA Wiesbaden GmbH und Knettenbrech + '
      'Gurdulic; 3) Übrige 50 %: Mainzer Stadtwerke AG; 4) Mitgesellschafter: Knettenbrech + Gurdulic 51 %, '
      'ENTEGA 24,5 %')

BAND_LABEL = rgb(0xADBCF4)
BAND_BG = rgb(0xD6DDF9)
PART_LABEL = rgb(0xC2DBFC)
PART_BG = rgb(0xE1EDFE)

SHAREHOLDERS = [('WVV Wiesbaden Holding GmbH', '50,62 %'), ('Thüga AG', '49,38 %')]

SIDE = ['WVV: 100 % Landeshauptstadt Wiesbaden',
        'Ergebnisabführungsvertrag mit der WVV (2025: 30,1 Mio. EUR)',
        'Vertragliche Ausgleichszahlung an die Thüga (2025: 18,8 Mio. EUR)',
        'ESWE Verkehr als Schwestergesellschaft unter der WVV (steuerlicher Querverbund)']

# (Name, Quote, Icons)
ROWS = [
    [('Stadtwerke Wiesbaden|Netz GmbH (sw netz)', '100 %', [2]),
     ('WiTCOM GmbH', '100 %', [5]),
     ('ESWE Taunuswind GmbH', '100 %', [3]),
     ('ESWE Windpark GmbH', '100 %', [3]),
     ('ESWE Windpark Uettingen|GmbH & Co. KG', '100 %', [3])],
    [('ESWE BioEnergie GmbH^2', '90 %', [3]),
     ('Kraftwerke Mainz-|Wiesbaden AG (KMW)^3', '50 %', [3]),
     ('Windkraft Kahlenberg|GmbH & Co. KG', '50 %', [3]),
     ('WRT Infrastrukturbau GmbH', '49 %', [2])],
    [('Windpark Bad Camberg|GmbH & Co. KG', '33,33 %', [3]),
     ('THEE ESWE Windpark-|beteiligungs GmbH & Co. KG', '33,33 %', [3]),
     ('MHKW Wiesbaden GmbH^4', '24,5 %', [3])],
]

LEGEND = ['Energievertrieb & -beschaffung', 'Netzgeschäft', 'Energieerzeugung',
          'Energiedienstleistungen, Wärme & E-Mobilität', 'Telekommunikation', 'Wasser']

COLX = [91.6, 240.7, 389.8, 539.0, 688.1]
CW = 117.6


def _tile(s, x, y, w, h, name, quote, icons):
    rect(s, x, y, w, h, fill=WHITE, linecolor=rgb(0xBFD3EC), linew=0.6)
    for k, ic in enumerate(icons):
        picture(s, 'gf%d.png' % ic, x + w - 6 - 13 * (len(icons) - k), y + 3.5, 11, 11)
    sup = ''
    if '^' in name:
        name, sup = name.split('^')
        sup = sup + ')'
    lines = []
    for chunk in name.split('|'):
        lines.extend(wrap(chunk, w - 12, 8.0, bold=True))

    n = len(lines) + 1
    y0 = y + (h - (len(lines) * 9.6 + 11.5)) / 2.0
    for j, l in enumerate(lines):
        runs = [Run(l, F_TWO, 8.0, DARK, True)]
        if sup and j == len(lines) - 1:
            runs.append(Run(sup, F_TWO, 8.0, DARK, True, baseline=30))
        textbox(s, x, y0 + j * 9.6, w, 9.6, [runs], anchor='m',
                align=PP_ALIGN.CENTER, wrap=False)
    textbox(s, x, y0 + len(lines) * 9.6 + 0.5, w, 11,
            [[Run(quote, F_TWO, 9.0, DARK, True)]], anchor='m',
            align=PP_ALIGN.CENTER, wrap=False)


def build(prs):
    s = blank(prs)
    chrome(s, 14, HEADER, SOURCES)
    title_2lines(s, 'Die ESWE ist kommunal und strategisch verankert und deckt mit ihrem',
                 'Beteiligungsportfolio die gesamte Wertschöpfungskette ab')
    textbox(s, 29.8, 535.6, 665, 20, [[Run(l, F_LIGHT, 8.0, BLACK)]
            for l in para_lines(FN, 660, 8.0)], line=9.6)

    # ---------------- Aktionärsband ----------------
    rect(s, 29.8, 118.8, 45.3, 63.8, fill=BAND_LABEL)
    rect(s, 80.2, 118.8, 579.7, 63.8, fill=BAND_BG)
    vlabel(s, 29.8, 118.8, 45.3, 63.8, ['Aktionäre', 'der ESWE'], size=8.5, line=10.5)
    for i, (name, q) in enumerate(SHAREHOLDERS):
        x = 114.0 + i * 272.0
        rect(s, x, 129.2, 240.0, 44.3, fill=WHITE, linecolor=rgb(0xBFD3EC), linew=0.6)
        textbox(s, x, 134.0, 240.0, 12,
                [[Run(name, F_TWO, 9.5, DARK, True)]], anchor='m',
                align=PP_ALIGN.CENTER, wrap=False)
        textbox(s, x, 150.0, 240.0, 14,
                [[Run(q, F_TWO, 11.0, DARK, True)]], anchor='m',
                align=PP_ALIGN.CENTER, wrap=False)

    # ---------------- Seitenkasten ----------------
    rect(s, 681.1, 129.2, 131.7, 121.6, fill=rgb(0xF2F2F2))
    vline(s, 677.1, 129.5, 249.8, DARK, 1.5)
    textbox(s, 686.0, 133.5, 122, 21,
            [[Run(l, F_TWO, 8.0, GREY, True)] for l in
             wrap('Konzernverbund und Gewinnverwendung', 122, 8.0, bold=True)], line=9.5)
    yy = 156.0
    for t in SIDE:
        ls = wrap(t, 108, 7.0)
        textbox(s, 686.0, yy, 8, 8.6, [[wing(6.0, DARK)]], anchor='m', wrap=False)
        textbox(s, 695.5, yy - 0.5, 112, len(ls) * 8.4 + 3,
                [[Run(l, F_LIGHT, 7.0, BLACK)] for l in ls], line=8.4)
        yy += len(ls) * 8.4 + 2.5

    # ---------------- Mitte: Logo + Icons ----------------
    vline(s, 370.0, 182.6, 198.8, DARK, 0.75)
    vline(s, 370.0, 243.1, 255.9, DARK, 0.75)
    rect(s, 311.3, 198.8, 117.6, 44.3, fill=rgb(0xF2F2F2))
    picture(s, 'eswe_logo.png', 327.0, 207.0, 86.0, 86.0 * 517 / 1233.0)
    for i in range(6):
        picture(s, 'gf%d.png' % (i + 1), 311.3 + 8.5 + i * 17, 185.0, 12, 12)

    # ---------------- Beteiligungsband ----------------
    rect(s, 30.2, 255.9, 44.9, 279.2, fill=PART_LABEL)
    rect(s, 80.2, 255.9, 732.0, 276.8, fill=PART_BG)
    vlabel(s, 30.2, 255.9, 44.9, 279.2,
           [[Run('Beteiligungsstruktur', F_TWO, 10.0, DARK, True),
             Run('1)', F_TWO, 10.0, DARK, True, baseline=30)]])
    RY = [280.3, 365.3, 450.3]
    RH = 58.0
    for ri, row in enumerate(ROWS):
        for ci, (name, q, icons) in enumerate(row):
            _tile(s, COLX[ci], RY[ri], CW, RH, name, q, icons)
    # Icon-Legende auf den freien Positionen 4-5 der letzten Reihe
    lx = [516.0, 668.0]
    for i, txt in enumerate(LEGEND):
        col, row = i % 2, i // 2
        x = lx[col]
        y = RY[2] + 1 + row * 22.0
        picture(s, 'gf%d.png' % (i + 1), x, y, 12, 12)
        ls = wrap(txt, 128, 7.0, bold=True)
        textbox(s, x + 16, y - 1, 132, len(ls) * 8.4 + 3,
                [[Run(l, F_TWO, 7.0, DARK, True)] for l in ls], line=8.4)
    return s
