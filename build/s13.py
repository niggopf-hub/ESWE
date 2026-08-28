# -*- coding: utf-8 -*-
"""Slide 13 — One Pager: KPI-Grid + Umsatzsplit-Donut (Pendant evm S. 13)."""
from deck import *

HEADER = '2. ESWE Versorgungs AG – Übersicht und Herausforderungen'
SOURCES = ('Quellen: Metzler-Recherche, Geschäftsbericht ESWE Versorgungs AG 2025, '
           'Unternehmenswebsite')
FN = ('1) EBITDA = Betriebliches Ergebnis zzgl. Abschreibungen, ohne Beteiligungsergebnis (2025: 25 Mio. EUR); '
      '2) EBT = zentrale Steuerungskennzahl inkl. Beteiligungs- und Zinsergebnis; 3) Ø 2025 inkl. 47 '
      'Auszubildende; 4) Stromnetz der sw netz, Gasnetz der ESWE Versorgungs AG; 5) Summenabweichung '
      'rundungsbedingt')

PANEL = rgb(0xF9F9F9)
DONUTBG = rgb(0xF4F4F4)
ICONBLUE = rgb(0x1789FF)

SEG = [
    ('Stromverkauf (inkl. Handel)', 40.1, rgb(0x003D7C), '40 %'),
    ('Gasverkauf (inkl. Handel)',   32.9, rgb(0x3157E3), '33 %'),
    ('Wasser',                      10.4, rgb(0x67A6F9), '10 %'),
    ('Wärme',                        9.2, rgb(0x718BEB), '9 %'),
    ('Dienstleistungen & Übrige',    7.4, rgb(0xA5CAFB), '7 %'),
]

# Kacheln: (Label, Wert, Vorjahr)
TILES = [
    ('Umsatz 2025',      '474 Mio. EUR', '535 Mio. EUR (2024)'),
    ('EBITDA 2025^1',    '45 Mio. EUR',  '89 Mio. EUR (2024)'),
    ('EBT 2025^2',       '53 Mio. EUR',  '84 Mio. EUR (2024)'),
    ('EAT 2025',         '49 Mio. EUR',  '78 Mio. EUR (2024)'),
    ('CapEx 2025',       '37 Mio. EUR',  '27 Mio. EUR (2024)'),
    ('Mitarbeiter^3',    '644',          None),
    ('Stromkunden 2025', '207.431',      None),
    ('Gaskunden 2025',   '53.323',       None),
    ('Stromnetz^4',      '~2.820 km',    None),
    ('Gasnetz^4',        '~823 km',      None),
]

CALLOUTS = [
    # (x, y, Titel, Farbe, [Bullets])
    (321.1, 165.2, 'Stromverkauf', 0,
     ['Vertrieb an Privat- und Geschäftskunden in Wiesbaden und überregional',
      'Beschaffung und Vermarktung']),
    (662.8, 165.2, 'Gasverkauf', 1,
     ['Vertrieb und Handel',
      'Wiederaufnahme des überregionalen Vertriebs (+11,3 %)']),
    (321.1, 282.6, 'Dienstleistungen & Übrige', 4,
     ['Leistungen für verbundene Unternehmen (u. a. sw netz, WiTCOM)',
      'E-Mobilität und kleinere Erlösquellen']),
    (491.2, 282.6, 'Wärme', 3,
     ['Fernwärme-Verbundnetz mit 132,9 km und 1.979 Anschlüssen',
      'Absatz +1,0 % durch Netzausbau']),
    (661.4, 282.6, 'Wasser', 2,
     ['Betriebsführung des Wassernetzes für den Eigenbetrieb WLW',
      'Wasserverkauf an die WLW']),
]

FIELDS = ['Energievertrieb &|-beschaffung', 'Netzgeschäft', 'Energieerzeugung',
          'Energiedienstleistungen,|Wärme & E-Mobilität', 'Telekommunikation', 'Wasser']
GF_CX = [95.25, 225.4, 355.85, 486.2, 616.45, 747.0]


def build(prs):
    s = blank(prs)
    chrome(s, 13, HEADER, SOURCES)
    title_2lines(s, 'Die ESWE erwirtschaftet ~ 73 % des Umsatzes mit Strom- und Gasverkäufen',
                 'und betreibt Wiesbadens zentrale Energie- und Wasserinfrastruktur')
    textbox(s, 29.8, 535.6, 665, 20, [[Run(l, F_LIGHT, 8.0, BLACK)]
            for l in para_lines(FN, 660, 8.0)], line=9.6)

    # ---------------- KPI-Grid ----------------
    rect(s, 29.8, 128.1, 251.0, 325.3, fill=PANEL)
    XS = [29.8, 163.7]
    YS = [137.4, 196.1, 254.8, 336.7, 395.1]
    for i, (label, val, prev) in enumerate(TILES):
        x = XS[i % 2]
        y = YS[i // 2]
        rect(s, x, y, 117.7, 44.3, fill=WHITE, linecolor=DARK, linew=0.75)
        rows = [(label, F_LIGHT, False, False), (val, F_TWO, True, False)]
        if prev:
            rows.append((prev, F_LIGHT, False, True))
        y0 = y + (44.3 - len(rows) * 12.0) / 2.0 + 1.0
        for j, (t, f, b, it) in enumerate(rows):
            runs = []
            if '^' in t:
                base, sup = t.split('^')
                runs = [Run(base, f, 10.0, DARK, b, it),
                        Run(sup + ')', f, 10.0, DARK, b, it, baseline=30)]
            else:
                runs = [Run(t, f, 10.0, DARK, b, it)]
            textbox(s, x, y0 + j * 12.0, 117.7, 12.5, [runs], anchor='m',
                    align=PP_ALIGN.CENTER, wrap=False)
    line_text(s, 29.8, 318.4, 328.3, 'Kunden und Netzinfrastruktur', F_TWO, 10.0, DARK,
              True, w=250)

    # ---------------- Donut ----------------
    rect(s, 313.3, 128.5, 499.0, 310.9, fill=DONUTBG)
    CX, CY, RO, RI = 561.9, 196.4, 66.4, 33.0
    ang = 270.0 - SEG[0][1] / 100.0 * 360.0      # Start links oben wie in der Vorlage
    mids = []
    for name, pct, color, lab in SEG:
        sweep = pct / 100.0 * 360.0
        block_arc(s, CX, CY, RO, RI, ang, ang + sweep, color)
        mids.append(ang + sweep / 2.0)
        ang += sweep
    import math
    oval(s, CX, CY, 2 * RI, 2 * RI, fill=WHITE)
    for (name, pct, color, lab), m in zip(SEG, mids):
        inside = pct > 12
        rr = (RO + RI) / 2.0 if inside else RO + 12.0
        lx = CX + rr * math.cos(math.radians(m))
        ly = CY + rr * math.sin(math.radians(m))
        col = WHITE if inside else BLACK
        textbox(s, lx - 22, ly - 6, 44, 12, [[Run(lab, F_TWO, 10.0, col, True)]],
                anchor='m', align=PP_ALIGN.CENTER, wrap=False)
    textbox(s, CX - 45, CY - 11, 90, 22,
            [[Run('100 % ≙', F_TWO, 9.0, DARK, True)],
             [Run('474 Mio. EUR', F_TWO, 9.0, DARK, True)]],
            anchor='m', align=PP_ALIGN.CENTER, line=11.3, wrap=False)

    # ---------------- Callouts ----------------
    for x, y, title, si, bullets in CALLOUTS:
        col = SEG[si][2]
        dashed_rect(s, x, y, 141.7, 99.2, col, fill=WHITE)
        line_text(s, x + 7.2, y + 9.7, y + 19.7, title, F_TWO, 10.0, col, True, w=134)
        yy = y + 21.4
        for b in bullets:
            lines = para_lines(b, 108, 9.0)
            textbox(s, x + 7.2, yy, 8, 10.8, [[wing(7.7, col)]], anchor='m', wrap=False)
            textbox(s, x + 21.4, yy - 0.5, 116, len(lines) * 10.8 + 3,
                    [[Run(l, F_LIGHT, 9.0, BLACK)] for l in lines], line=10.8)
            yy += len(lines) * 10.8
    # Verbindungslinien Callout -> Donut
    elbow(s, [(462.8, 217.8), (501.9, 217.8)], SEG[0][2])
    elbow(s, [(620.6, 218.6), (662.8, 218.6)], SEG[1][2])
    elbow(s, [(391.9, 282.6), (391.9, 261.8), (528.0, 261.8)], SEG[4][2])
    elbow(s, [(562.0, 282.6), (562.0, 264.0)], SEG[3][2])
    elbow(s, [(732.3, 282.6), (732.3, 254.0), (600.0, 254.0)], SEG[2][2])

    # ---------------- Icon-Leiste ----------------
    rect(s, 29.8, 451.7, 782.4, 83.4, fill=PANEL)
    for x in (160.2, 290.6, 421.0, 551.4, 681.8):
        vline(s, x, 468.2, 518.6, ICONBLUE, 1.5, dash=True)
    for i, (cx, label) in enumerate(zip(GF_CX, FIELDS)):
        pic_h = 38.0
        picture(s, 'gf%d.png' % (i + 1), cx - 19, 461.5, 38, pic_h)
        lines = label.split('|')
        y0 = 512.8 if len(lines) == 1 else 506.8
        for j, l in enumerate(lines):
            textbox(s, cx - 65, y0 + j * 12.0, 130, 11,
                    [[Run(l, F_TWO, 10.0, ICONBLUE, True)]], anchor='m',
                    align=PP_ALIGN.CENTER, wrap=False)
    return s
