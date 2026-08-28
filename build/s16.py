# -*- coding: utf-8 -*-
"""Slide 16 — Financials-Tripel: GuV / Cashflow / Bilanz (Pendant evm S. 16)."""
from deck import *

HEADER = '2. ESWE Versorgungs AG – Übersicht und Herausforderungen'
SOURCES = ('Quellen: Metzler-Recherche, Jahresabschlüsse ESWE Versorgungs AG 2021–2025, '
           'Unternehmenswebsite')
FN = ('1) Rohertrag = Umsatzerlöse ./. Materialaufwand; 2) Abweichungen der Säulensummen '
      'von den ∑-Werten rundungsbedingt')

C_DARK = rgb(0x003D7C)
C_MID = rgb(0x3157E3)
C_LILA = rgb(0x718BEB)
C_LIGHT = rgb(0xA5CAFB)
C_ORANGE = rgb(0xFF9900)
BANDBG = rgb(0xF2F2F2)

YEARS = ['2021', '2022', '2023', '2024', '2025']
UMSATZ = [427, 476, 634, 535, 474]
ROHERTRAG = [115, 119, 150, 147, 132]
MARGE = ['27,0 %', '25,1 %', '23,7 %', '27,6 %', '27,9 %']
MARGE_V = [27.0, 25.1, 23.7, 27.6, 27.9]

CF_OP = [49, 78, 47, 68, 43]
CF_INV = [-20, -34, 9, -5, -8]
CF_FIN = [-29, -17, -42, -87, -53]
CF_TOT = [1, 27, 14, -24, -19]

KASSE = [4, 31, 45, 22, 3]
EKQ = ['30,3 %', '27,8 %', '26,3 %', '27,6 %', '28,5 %']
EKQ_V = [30.3, 27.8, 26.3, 27.6, 28.5]

KOMMENTAR = [
    'Umsatz 2025 preisbedingt rückläufig (−11 %), Rohertragsmarge auf 27,9 % gestiegen',
    'Rekordergebnisse 2023/2024 sondereffektgetrieben (2024: Rückstellungsauflösungen von '
    '20,6 Mio. EUR) − 2025 markiert die Normalisierung auf robustem Niveau (EBT 53 Mio. EUR, '
    'deutlich über Plan)',
    'Der operative Cashflow (Ø ~57 Mio. EUR p. a.) wird nahezu vollständig durch die '
    'Ergebnisabführung an die Gesellschafter und den Investitionshochlauf absorbiert − die '
    'liquiden Mittel sanken Ende 2025 auf 2,5 Mio. EUR',
    'Der geplante Investitionsanstieg auf bis zu 80 Mio. EUR p. a. scheint bei unveränderter '
    'Ausschüttungspolitik nicht aus dem operativen Cash Flow finanzierbar zu sein − bereits '
    '2025 waren Kapitaleinlagen der Aktionäre (10 Mio. EUR) zur Sicherung der Ziel-EK-Quote '
    'von über 25 % erforderlich',
]

PITCH = 49.2


def _num(v):
    return '(%d)' % abs(v) if v < 0 else '%d' % v


def _legend(s, x, y, color, label, shape='rect'):
    if shape == 'rect':
        rect(s, x, y + 1.0, 13, 9, fill=color)
    else:
        oval(s, x + 6.5, y + 5.5, 15, 9, fill=color)
    line_text(s, x + 17, y, y + 10, label, F_LIGHT, 9.0, BLACK, w=140)


def build(prs):
    s = blank(prs)
    chrome(s, 16, HEADER, SOURCES)
    title_2lines(s, 'Robuste Ertragskraft nach zwei Sonderjahren − jedoch absorbieren',
                 'Ausschüttungen und Investitionshochlauf die Liquidität weitgehend')
    textbox(s, 29.8, 535.6, 665, 20, [[Run(l, F_LIGHT, 8.0, BLACK)]
            for l in para_lines(FN, 660, 8.0)], line=9.6)

    # ================= Panel 1: GuV =================
    line_text(s, 40.8, 133.9, 145.0, 'Gewinn- und Verlustrechnung (Mio. EUR)',
              F_TWO, 10.0, C_MID, True, w=250)
    _legend(s, 40.8, 150.4, C_DARK, 'Umsatz')
    rect(s, 95.9, 151.4, 13, 9, fill=C_MID)
    textbox(s, 112.9, 150.4, 90, 11,
            [[Run('Rohertrag', F_LIGHT, 9.0, BLACK),
              Run('1)', F_LIGHT, 9.0, BLACK, baseline=30)]], anchor='m', wrap=False)
    oval(s, 178.0, 155.9, 22, 11, fill=None, linecolor=C_ORANGE, linew=1.0)
    line_text(s, 189.5, 151.2, 161.2, 'CAGR', F_LIGHT, 9.0, BLACK, w=60)
    _legend(s, 40.8, 164.6, C_LILA, 'Rohertrag-Marge', shape='oval')

    BASE1, SC1 = 374.8, 97.6 / 634.0
    hline(s, 30.0, 276.1, BASE1, BLACK, 0.75)
    for i in range(5):
        x = 37.1 + i * PITCH
        h1, h2 = UMSATZ[i] * SC1, ROHERTRAG[i] * SC1
        rect(s, x, BASE1 - h1, 17.5, h1, fill=C_DARK)
        rect(s, x + 17.5, BASE1 - h2, 17.5, h2, fill=C_MID)
        textbox(s, x - 9, BASE1 - h1 - 12, 35, 11,
                [[Run('%d' % UMSATZ[i], F_LIGHT, 9.0, BLACK)]], anchor='m',
                align=PP_ALIGN.CENTER, wrap=False)
        textbox(s, x + 9, BASE1 - h2 - 12, 35, 11,
                [[Run('%d' % ROHERTRAG[i], F_LIGHT, 9.0, BLACK)]], anchor='m',
                align=PP_ALIGN.CENTER, wrap=False)
        textbox(s, x, BASE1 + 3, 35, 12, [[Run(YEARS[i], F_LIGHT, 9.0, BLACK)]],
                anchor='m', align=PP_ALIGN.CENTER, wrap=False)
        my = 232.0 - (MARGE_V[i] - 23.5) / 5.0 * 48.0
        oval(s, x + 17.5, my, 48.5, 18.4, fill=C_LILA)
        textbox(s, x - 7, my - 6, 49, 12, [[Run(MARGE[i], F_TWO, 9.0, WHITE, True)]],
                anchor='m', align=PP_ALIGN.CENTER, wrap=False)
    ar = rect(s, 45.7, 240.4, 196.9, 15.1, fill=C_ORANGE, shape=MSO_SHAPE.RIGHT_ARROW)
    oval(s, 144.1, 248.9, 55.8, 15.3, fill=WHITE, linecolor=C_ORANGE, linew=1.0)
    textbox(s, 116.2, 242.9, 56, 12, [[Run('+2,7% p.a.', F_TWO, 9.0, BLACK, True)]],
            anchor='m', align=PP_ALIGN.CENTER, wrap=False)

    # ================= Panel 2: Kapitalflussrechnung =================
    line_text(s, 307.1, 133.9, 145.0, 'Kapitalflussrechnung (Mio. EUR)',
              F_TWO, 10.0, C_LILA, True, w=250)
    _legend(s, 307.1, 150.4, C_DARK, 'Operating Cash Flow')
    _legend(s, 416.2, 150.4, C_LILA, 'Financing Cash Flow')
    _legend(s, 307.1, 165.1, C_MID, 'Investing Cash Flow')
    line_text(s, 418.2, 164.6, 175.0, '∑   Total Cash Flow', F_TWO, 9.0, BLACK, w=140)

    ZERO, SC2 = 312.0, 0.50
    w = 27.6
    labels = []
    for i in range(5):
        x = 307.2 + i * PITCH
        up = dn = ZERO
        for val, c in ((CF_OP[i], C_DARK), (CF_INV[i], C_MID), (CF_FIN[i], C_LILA)):
            h = abs(val) * SC2
            if val >= 0:
                up -= h
                rect(s, x, up, w, h, fill=c)
                cy = up + h / 2.0
            else:
                rect(s, x, dn, w, h, fill=c)
                cy = dn + h / 2.0
                dn += h
            inside = h > 10
            labels.append((x + (0 if inside else w + 2), cy - 6,
                           _num(val), WHITE if inside else BLACK, False))
        ty = (up - 13) if CF_TOT[i] >= 0 else (dn + 2)
        labels.append((x, ty, _num(CF_TOT[i]), BLACK, True))
        labels.append((x, 380.0, YEARS[i], BLACK, False))
    hline(s, 296.2, 542.5, ZERO, BLACK, 0.75)
    for lx, ly, txt, col, bold in labels:
        textbox(s, lx, ly, w, 12,
                [[Run(txt, F_TWO if bold else F_LIGHT, 9.0, col, bold)]],
                anchor='m', align=PP_ALIGN.CENTER, wrap=False)

    # ================= Panel 3: Bilanzpositionen =================
    line_text(s, 573.6, 133.9, 145.0, 'Bilanzpositionen (Mio. EUR)',
              F_TWO, 10.0, rgb(0x67A6F9), True, w=250)
    _legend(s, 573.6, 150.4, C_DARK, 'Kassenbestand')
    _legend(s, 573.6, 164.6, C_LIGHT, 'Eigenkapital-Quote', shape='oval')

    BASE3, SC3 = 374.0, 90.0 / 45.0
    hline(s, 562.8, 809.1, BASE3, BLACK, 0.75)
    for i in range(5):
        x = 573.0 + i * PITCH
        h = KASSE[i] * SC3
        rect(s, x, BASE3 - h, 26.0, h, fill=C_DARK)
        textbox(s, x - 5, BASE3 - h - 12, 36, 11,
                [[Run('%d' % KASSE[i], F_LIGHT, 9.0, BLACK)]], anchor='m',
                align=PP_ALIGN.CENTER, wrap=False)
        textbox(s, x - 5, BASE3 + 3, 36, 12, [[Run(YEARS[i], F_LIGHT, 9.0, BLACK)]],
                anchor='m', align=PP_ALIGN.CENTER, wrap=False)
        ey = 245.0 - (EKQ_V[i] - 25.8) / 5.0 * 48.0
        oval(s, x + 13, ey, 48.5, 18.4, fill=C_LIGHT)
        textbox(s, x - 11, ey - 6, 48.5, 12, [[Run(EKQ[i], F_TWO, 9.0, WHITE, True)]],
                anchor='m', align=PP_ALIGN.CENTER, wrap=False)

    # ================= Kommentarband =================
    rect(s, 29.8, 423.1, 782.4, 112.0, fill=BANDBG)
    line_text(s, 44.0, 430.5, 441.0, 'Kommentar:', F_TWO, 9.0, DARK, True, w=120)
    yy = 447.0
    for b in KOMMENTAR:
        ls = para_lines(nb(b), 748, 9.0)
        textbox(s, 44.0, yy, 8, 10.8, [[wing(7.7, DARK)]], anchor='m', wrap=False)
        textbox(s, 57.0, yy - 0.5, 752, len(ls) * 10.8 + 3,
                [[Run(l, F_LIGHT, 9.0, BLACK)] for l in ls], line=10.8)
        yy += len(ls) * 10.8 + 3.5
    return s
