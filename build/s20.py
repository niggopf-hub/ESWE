# -*- coding: utf-8 -*-
"""Slide 20 — Beteiligungsmodelle, ausgewählte Impulse (Pendant evm S. 20)."""
from deck import *

HEADER = '3. Diskussion möglicher Handlungsoptionen'
FN = ('1) Ähnlich übertragbar auf weitere Geschäftsfelder, z. B. Wind-/Solarbeteiligungen '
      'oder Ladeinfrastruktur')

TITLE_BAR = rgb(0x67A6F9)
BODY = rgb(0xF3F8FF)
BLUE = rgb(0x3157E3)
ORANGE = rgb(0xFF9900)
GREYF = rgb(0xF2F2F2)

ASSETS_LIST = ['ESWE Versorgungs AG', 'Stadtwerke Wiesbaden Netz GmbH', 'WiTCOM GmbH',
               'Fernwärme-Geschäft (post Carve-out)',
               'Windportfolio inkl. Projekt Hohe Wurzel']

ASPEKTE = ['Ausgewogene Governance mit definierten Reserved Matters, Dividendenpolitik '
           'und Exit-Mechanismen',
           'Investorengerechte Schaffung einer Plattform/eines abgegrenzten Vehikels',
           'Rendite- und Rückzahlungsmechanismen',
           'Festlegung Budget und Investitionsplan',
           'Frühzeitige Einbindung beider Ankergesellschafter (Stadt und Thüga)']

VORTEILE = ['Teilung von Risiken und Investitionsbedarf',
            'Zufluss des Kaufpreises',
            'Schnellere Umsetzung von Investitionen möglich',
            'Zusätzlicher strategischer Input',
            'Governance flexibel strukturierbar']


def _quadrant_title(s, x, w, text, sup=None):
    rect(s, x, 127.6, w, 19.8, fill=TITLE_BAR)
    runs = [Run(text, F_TWO, 10.0, WHITE, True)]
    if sup:
        runs.append(Run(sup, F_TWO, 10.0, WHITE, True, baseline=30))
    textbox(s, x, 128.5, w, 18, [runs], anchor='m', align=PP_ALIGN.CENTER, wrap=False)


def _bullets(s, x, y0, w, items, pitch=18.0, size=10.0, line=12.0):
    yy = y0
    for it in items:
        ls = para_lines(it, w - 14, size)
        textbox(s, x, yy, 9, line, [[wing(size * 0.73, DARK)]], anchor='m', wrap=False)
        textbox(s, x + 13.8, yy - 0.5, w - 13, len(ls) * line + 3,
                [[Run(l, F_LIGHT, size, DARK)] for l in ls], line=line)
        yy += max(pitch, len(ls) * line + 5.5)
    return yy


def build(prs):
    s = blank(prs)
    chrome(s, 20, HEADER, None)
    title_2lines(s, 'Bei Bedarf können private Investoren in unterschiedlichen Modellen und',
                 'bei unterschiedlichen Assets beteiligt werden − ausgewählte Impulse')
    textbox(s, 29.8, 545.2, 665, 12, [[Run(l, F_LIGHT, 8.0, BLACK)]
            for l in para_lines(FN, 660, 8.0)], line=9.6)

    # ---------------- Q1: Joint Venture ----------------
    _quadrant_title(s, 29.8, 385.5, 'Joint Venture Wärme/Erneuerbare Energien', '1)')
    rect(s, 29.8, 147.4, 385.5, 228.3, fill=BODY)
    # SPV
    rect(s, 154.1, 204.3, 137.0, 133.1, fill=WHITE, linecolor=TITLE_BAR, linew=0.75)
    rect(s, 154.1, 204.3, 137.0, 28.4, fill=DARK, linecolor=TITLE_BAR, linew=0.75)
    textbox(s, 154.1, 206.5, 137, 12, [[Run('Wärme/EE SPV', F_TWO, 9.0, WHITE, True)]],
            anchor='m', align=PP_ALIGN.CENTER, wrap=False)
    textbox(s, 154.1, 217.5, 137, 12,
            [[Run('post Carve-Out', F_TWO, 9.0, WHITE, True, italic=True)]],
            anchor='m', align=PP_ALIGN.CENTER, wrap=False)
    picture(s, 'gf4.png', 166.0, 250.0, 26, 26)
    line_text(s, 200.0, 258.0, 269.0, 'Fernwärme', F_LIGHT, 9.0, BLACK, w=90)
    picture(s, 'gf3.png', 166.0, 293.0, 26, 26)
    line_text(s, 200.0, 301.0, 312.0, 'EE-Erzeugung', F_LIGHT, 9.0, BLACK, w=90)
    # ESWE / Investor
    picture(s, 'eswe_logo.png', 46.0, 166.0, 76.0, 76.0 * 517 / 1233.0)
    rect(s, 316.1, 167.8, 72.8, 19.4, fill=ORANGE, linecolor=WHITE, linew=0.75)
    textbox(s, 316.1, 168.8, 72.8, 17, [[Run('Investor', F_TWO, 9.0, WHITE, True)]],
            anchor='m', align=PP_ALIGN.CENTER, wrap=False)
    # Pfeile
    elbow(s, [(84.0, 200.0), (84.0, 218.4), (152.0, 218.4)], BLUE, 1.5)
    elbow(s, [(352.5, 187.2), (352.5, 218.4), (293.0, 218.4)], ORANGE, 1.5)
    line_text(s, 160.0, 185.7, 196.0, 'X%', F_LIGHT, 10.0, BLACK, w=40)
    line_text(s, 252.0, 185.7, 196.0, 'X%', F_LIGHT, 10.0, BLACK, w=40)
    line_text(s, 296.0, 190.0, 201.0, 'Minderheit', F_TWO, 9.0, ORANGE, True,
              align=PP_ALIGN.CENTER, w=52)
    # gestrichelte Kommentarkästen
    dashed_rect(s, 41.9, 263.9, 101.4, 67.8, BLUE, fill=GREYF)
    textbox(s, 46.9, 280.0, 92, 40,
            [[Run(l, F_LIGHT, 9.0, DARK, italic=True)] for l in
             ['Einbringung', 'Fernwärmenetz/', 'EE-Projekte']],
            anchor='m', align=PP_ALIGN.CENTER, line=10.8)
    dashed_rect(s, 301.8, 263.9, 101.4, 67.8, ORANGE, fill=GREYF)
    textbox(s, 306.8, 285.0, 92, 30,
            [[Run(l, F_LIGHT, 9.0, DARK, italic=True)] for l in
             ['Einbringung EK für', 'Capex und Kaufpreis']],
            anchor='m', align=PP_ALIGN.CENTER, line=10.8)

    # ---------------- Q2: Beteiligung an Unternehmen/Assets ----------------
    _quadrant_title(s, 426.7, 385.5, '(private) Beteiligung an Unternehmen/Assets')
    rect(s, 426.7, 147.4, 385.5, 228.3, fill=BODY)
    _bullets(s, 433.9, 162.4, 360, ASSETS_LIST, pitch=24.0)

    # ---------------- Q3 / Q4 ----------------
    line_text(s, 37.0, 397.5, 408.0, 'Wesentliche Aspekte bei der Gestaltung einer '
              'Partnerschaft', F_TWO, 10.0, DARK, True, w=380)
    rect(s, 29.8, 410.8, 385.5, 108.4, fill=WHITE, linecolor=GREYF, linew=0.75)
    _bullets(s, 37.0, 417.3, 372, ASPEKTE, pitch=17.0, line=13.7)

    line_text(s, 433.9, 397.5, 408.0, 'Vorteile für die ESWE Versorgungs AG',
              F_TWO, 10.0, DARK, True, w=380)
    rect(s, 426.7, 410.8, 385.5, 108.4, fill=WHITE, linecolor=GREYF, linew=0.75)
    _bullets(s, 433.9, 417.3, 372, VORTEILE, pitch=18.0, line=13.7)
    return s
