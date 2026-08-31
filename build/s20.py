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
    bar = rect(s, x, 127.6, w, 19.8, fill=TITLE_BAR)
    runs = [Run(text, F_TWO, 10.0, WHITE, True)]
    if sup:
        runs.append(Run(sup, F_TWO, 10.0, WHITE, True, baseline=30))
    shape_text(bar, [runs], anchor='m', align=PP_ALIGN.CENTER, wrap=False)


def _bullets(shape, items, size=10.0, line=12.0, before=6.0, inset=None):
    """Aufzaehlung direkt in den Textrahmen der uebergebenen Form."""
    shape_text(shape, [[Run(t, F_LIGHT, size, DARK)] for t in items],
               size=size, line=line, before=before, anchor='t', bullets=True,
               indent=13.8, inset=inset or (7.2, 8.0, 8.0, 4.0))
    return shape


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
    kopf = rect(s, 154.1, 204.3, 137.0, 28.4, fill=DARK, linecolor=TITLE_BAR,
                linew=0.75)
    shape_text(kopf, [[Run('Wärme/EE SPV', F_TWO, 9.0, WHITE, True)],
                      [Run('post Carve-Out', F_TWO, 9.0, WHITE, True, italic=True)]],
               line=11.0, anchor='m', align=PP_ALIGN.CENTER, wrap=False)
    picture(s, 'gf4.png', 166.0, 250.0, 26, 26)
    line_text(s, 200.0, 258.0, 269.0, 'Fernwärme', F_LIGHT, 9.0, BLACK, w=90)
    picture(s, 'gf3.png', 166.0, 293.0, 26, 26)
    line_text(s, 200.0, 301.0, 312.0, 'EE-Erzeugung', F_LIGHT, 9.0, BLACK, w=90)
    # ESWE / Investor
    picture(s, 'eswe_logo.png', 46.0, 166.0, 76.0, 76.0 * 517 / 1233.0)
    shape_text(rect(s, 316.1, 167.8, 72.8, 19.4, fill=ORANGE, linecolor=WHITE,
                    linew=0.75),
               [Run('Investor', F_TWO, 9.0, WHITE, True)],
               anchor='m', align=PP_ALIGN.CENTER, wrap=False)
    # Pfeile
    elbow(s, [(84.0, 200.0), (84.0, 218.4), (152.0, 218.4)], BLUE, 1.5)
    elbow(s, [(352.5, 187.2), (352.5, 218.4), (293.0, 218.4)], ORANGE, 1.5)
    line_text(s, 160.0, 185.7, 196.0, 'X%', F_LIGHT, 10.0, BLACK, w=40)
    line_text(s, 252.0, 185.7, 196.0, 'X%', F_LIGHT, 10.0, BLACK, w=40)
    line_text(s, 296.0, 190.0, 201.0, 'Minderheit', F_TWO, 9.0, ORANGE, True,
              align=PP_ALIGN.CENTER, w=52)
    # gestrichelte Kommentarkästen
    shape_text(dashed_rect(s, 41.9, 263.9, 101.4, 67.8, BLUE, fill=GREYF),
               [[Run(l, F_LIGHT, 9.0, DARK, italic=True)] for l in
                ['Einbringung', 'Fernwärmenetz/', 'EE-Projekte']],
               line=10.8, anchor='m', align=PP_ALIGN.CENTER, wrap=False)
    shape_text(dashed_rect(s, 301.8, 263.9, 101.4, 67.8, ORANGE, fill=GREYF),
               [[Run(l, F_LIGHT, 9.0, DARK, italic=True)] for l in
                ['Einbringung EK für', 'Capex und Kaufpreis']],
               line=10.8, anchor='m', align=PP_ALIGN.CENTER, wrap=False)

    # ---------------- Q2: Beteiligung an Unternehmen/Assets ----------------
    _quadrant_title(s, 426.7, 385.5, '(private) Beteiligung an Unternehmen/Assets')
    _bullets(rect(s, 426.7, 147.4, 385.5, 228.3, fill=BODY), ASSETS_LIST,
             line=12.0, before=12.0, inset=(7.2, 13.0, 12.0, 4.0))

    # ---------------- Q3 / Q4 ----------------
    line_text(s, 37.0, 397.5, 408.0, 'Wesentliche Aspekte bei der Gestaltung einer '
              'Partnerschaft', F_TWO, 10.0, DARK, True, w=380)
    _bullets(rect(s, 29.8, 410.8, 385.5, 108.4, fill=WHITE, linecolor=GREYF,
                  linew=0.75),
             ASPEKTE, line=13.7, before=4.3, inset=(7.2, 5.0, 10.0, 3.0))

    line_text(s, 433.9, 397.5, 408.0, 'Vorteile für die ESWE Versorgungs AG',
              F_TWO, 10.0, DARK, True, w=380)
    _bullets(rect(s, 426.7, 410.8, 385.5, 108.4, fill=WHITE, linecolor=GREYF,
                  linew=0.75),
             VORTEILE, line=13.7, before=4.3, inset=(7.2, 5.0, 10.0, 3.0))
    return s
