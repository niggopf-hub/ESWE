# -*- coding: utf-8 -*-
"""Slide 20 — Beteiligungsmodelle: Beispielstruktur sw netz + sortierte Asset-Liste.

evm-Quadranten-Layout (Pendant evm S. 20): links das konkrete „Wie" als
Beispielstruktur, rechts das „Wo" als nach Eignung sortierte Asset-Liste, unten
Aspekte und Vorteile. Der Kapitalpakt laeuft in der Banner-Zeile mit.
"""
from deck import *

HEADER = '3. Diskussion möglicher Handlungsoptionen'
FN = ('1) Beteiligungshöhen illustrativ; Struktur ähnlich übertragbar auf die weiteren '
      'aufgeführten Assets')

TITLE_BAR = rgb(0x67A6F9)
BODY = rgb(0xF3F8FF)
BLUE = rgb(0x3157E3)
ORANGE = rgb(0xFF9900)
GREYF = rgb(0xF2F2F2)

# ---- Geometrie ----------------------------------------------------------
QL_X, QR_X, QW = 29.8, 426.7, 385.5
BAR_Y, BAR_H = 127.6, 19.8
BODY_Y, BODY_H = 147.4, 185.0
SUB_Y = 344.0
BOX_Y, BOX_H = 358.0, 136.0
BANNER_Y, BANNER_H = 500.0, 30.0

ASSETS_LIST = ['Stadtwerke Wiesbaden Netz GmbH (Minderheitsbeteiligung)',
               'WiTCOM GmbH (Minderheit oder Wachstumspartnerschaft)',
               'Windportfolio inklusive Projekt Hohe Wurzel',
               'Wärme-Neubaugeschäft (Projektgesellschaft)']

ASPEKTE = ['Ausgewogene Governance mit definierten Reserved Matters, Dividendenpolitik '
           'und Exit-Mechanismen',
           'Vereinbarkeit mit dem Ergebnisabführungsvertrag und der Ausgleichszahlung '
           'an die Thüga',
           'Auswirkungen der RAMEN- und NEST-Festlegungen auf das Netzergebnis sind in '
           'der Bewertung zu berücksichtigen',
           'Rendite- und Rückzahlungsmechanismen sowie Festlegung von Budget und '
           'Investitionsplan',
           'Frühzeitige Einbindung beider Ankergesellschafter']

VORTEILE = ['Teilung von Kapitalbedarf und Projektrisiken',
            'Entlastung der Gesellschafter von weiteren Eigenkapitalzuführungen',
            'Zufluss von Kaufpreis und frischem Eigenkapital in den Netzausbau',
            'Schnellere Umsetzung der Netz- und Wärmewende-Investitionen',
            'Governance flexibel strukturierbar bei Erhalt der kommunalen Steuerung']

BANNER = ('Flankierend stärkt ein Kapitalpakt der Aktionäre aus planbaren Einlagen, '
          'Thesaurierungspfad und Nachrangkapital die Eigenkapitalbasis ohne jede '
          'Strukturveränderung')


def _quadrant_title(s, x, w, text, sup=None):
    bar = rect(s, x, BAR_Y, w, BAR_H, fill=TITLE_BAR)
    runs = [Run(text, F_TWO, 10.0, WHITE, True)]
    if sup:
        runs.append(Run(sup, F_TWO, 10.0, WHITE, True, baseline=30))
    shape_text(bar, [runs], anchor='m', align=PP_ALIGN.CENTER, wrap=False)
    return bar


def _bullets(shape, items, size=10.0, line=12.0, before=6.0, inset=None):
    """Aufzaehlung direkt in den Textrahmen der uebergebenen Form."""
    shape_text(shape, [[Run(t, F_LIGHT, size, DARK)] for t in items],
               size=size, line=line, before=before, anchor='t', bullets=True,
               indent=13.8, inset=inset or (7.2, 8.0, 8.0, 4.0))
    return shape


def _strukturchart(s):
    """Beispielstruktur: Minderheitsbeteiligung an der sw netz."""
    # Gesellschafter
    picture(s, 'eswe_logo.png', 46.0, 160.0, 76.0, 76.0 * 517 / 1233.0)
    shape_text(rect(s, 316.1, 161.0, 72.8, 19.4, fill=ORANGE, linecolor=WHITE,
                    linew=0.75),
               [Run('Investor', F_TWO, 9.0, WHITE, True)],
               anchor='m', align=PP_ALIGN.CENTER, wrap=False)

    # Quoten und Minderheitsvermerk
    line_text(s, 150.0, 186.0, 196.5, '74,9 %', F_LIGHT, 10.0, BLACK, w=48)
    line_text(s, 246.0, 186.0, 196.5, '25,1 %', F_LIGHT, 10.0, BLACK, w=48)
    line_text(s, 300.0, 183.0, 193.5, 'Minderheit', F_TWO, 9.0, ORANGE, True,
              True, align=PP_ALIGN.CENTER, w=52)

    # Zielgesellschaft
    kopf = rect(s, 154.1, 202.0, 137.0, 54.0, fill=DARK, linecolor=TITLE_BAR,
                linew=0.75)
    shape_text(kopf, [[Run('Stadtwerke Wiesbaden', F_TWO, 9.0, WHITE, True)],
                      [Run('Netz GmbH', F_TWO, 9.0, WHITE, True)],
                      [Run('bestehende Gesellschaft,', F_TWO, 8.0, WHITE, True,
                           italic=True)],
                      [Run('kein Carve-out erforderlich', F_TWO, 8.0, WHITE, True,
                           italic=True)]],
               line=10.4, anchor='m', align=PP_ALIGN.CENTER, wrap=False)
    koerper = rect(s, 154.1, 256.0, 137.0, 46.0, fill=WHITE, linecolor=TITLE_BAR,
                   linew=0.75)
    picture(s, 'gf2.png', 168.0, 264.0, 26, 26)
    shape_text(koerper, [Run('Stromnetz Wiesbaden', F_LIGHT, 8.5, BLACK)],
               anchor='m', inset=(46.0, 2.0, 3.0, 2.0), wrap=False)

    # Beteiligungspfeile
    connect(s, 84.0, 194.0, 84.0, 216.0, color=BLUE, width=1.5)
    connect(s, 84.0, 216.0, 152.0, 216.0, color=BLUE, width=1.5)
    connect(s, 352.5, 180.4, 352.5, 216.0, color=ORANGE, width=1.5)
    connect(s, 352.5, 216.0, 293.0, 216.0, color=ORANGE, width=1.5)

    # Mittelverwendung
    shape_text(dashed_rect(s, 41.9, 252.0, 101.4, 62.0, BLUE, fill=GREYF),
               [[Run(l, F_LIGHT, 9.0, DARK, italic=True)] for l in
                ['Kapitalerhöhung', 'finanziert den', 'Stromnetzausbau']],
               line=10.8, anchor='m', align=PP_ALIGN.CENTER, wrap=False)
    shape_text(dashed_rect(s, 301.8, 252.0, 101.4, 62.0, ORANGE, fill=GREYF),
               [[Run(l, F_LIGHT, 9.0, DARK, italic=True)] for l in
                ['Anteilskaufpreis', 'fließt der ESWE zu']],
               line=10.8, anchor='m', align=PP_ALIGN.CENTER, wrap=False)


def build(prs):
    s = blank(prs)
    chrome(s, 20, HEADER, None)
    title_2lines(s, 'Bei Bedarf können private Investoren in unterschiedlichen Modellen',
                 'und bei unterschiedlichen Assets beteiligt werden')
    line_text(s, 29.8, 101.5, 115.5, 'Ausgewählte Impulse', F_REG, 14, GREY, True,
              w=400)
    textbox(s, 29.8, 545.2, 665, 12, [[Run(l, F_LIGHT, 8.0, BLACK)]
            for l in para_lines(FN, 660, 8.0)], line=9.6)

    # ---------------- Oben links: Beispielstruktur ----------------
    _quadrant_title(s, QL_X, QW, 'Beispielstruktur: Minderheitsbeteiligung an der '
                    'sw netz', '1)')
    rect(s, QL_X, BODY_Y, QW, BODY_H, fill=BODY)
    _strukturchart(s)

    # ---------------- Oben rechts: Asset-Liste ----------------
    _quadrant_title(s, QR_X, QW, '(private) Beteiligung an Unternehmen/Assets')
    _bullets(rect(s, QR_X, BODY_Y, QW, BODY_H, fill=BODY), ASSETS_LIST,
             line=12.0, before=14.0, inset=(7.2, 16.0, 12.0, 4.0))

    # ---------------- Unten: Aspekte und Vorteile ----------------
    line_text(s, 37.0, SUB_Y, SUB_Y + 10.5, 'Wesentliche Aspekte bei der Gestaltung '
              'einer Partnerschaft', F_TWO, 10.0, DARK, True, w=380)
    _bullets(rect(s, QL_X, BOX_Y, QW, BOX_H, fill=WHITE, linecolor=GREYF, linew=0.75),
             ASPEKTE, size=9.0, line=12.0, before=3.5, inset=(7.2, 5.0, 10.0, 3.0))

    line_text(s, 433.9, SUB_Y, SUB_Y + 10.5, 'Vorteile für die ESWE Versorgungs AG',
              F_TWO, 10.0, DARK, True, w=380)
    _bullets(rect(s, QR_X, BOX_Y, QW, BOX_H, fill=WHITE, linecolor=GREYF, linew=0.75),
             VORTEILE, size=9.0, line=12.0, before=3.5, inset=(7.2, 5.0, 10.0, 3.0))

    # ---------------- Banner: Kapitalpakt ----------------
    banner = soft_shadow(rect(s, 29.8, BANNER_Y, 782.4, BANNER_H, fill=WHITE,
                              linecolor=DARK, linew=1.0))
    chev = rect(s, 29.8, BANNER_Y + 2.0, 14.5, BANNER_H - 4.0, fill=DARK,
                shape=MSO_SHAPE.PENTAGON)
    try:
        chev.adjustments[0] = 0.62
    except Exception:
        pass
    shape_text(banner, [Run(BANNER, F_TWO, 10.0, DARK, True)],
               line=12.0, anchor='m', inset=(33.8, 3.0, 12.0, 3.0))
    return s
