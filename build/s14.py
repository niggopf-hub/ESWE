# -*- coding: utf-8 -*-
"""Slide 14 — Beteiligungsstruktur im Duisburg-Format (Organigramm mit Ergebnisbeiträgen).

Layout und Formatsprache nach '20240305_Stadtwerke Duisburg_v4', Folie 11:
Konzernbaum mit Quoten an den Verbindungslinien, je Gesellschaft eine Kachel
und darunter ein hellblauer Kasten mit Tätigkeit, Kapital-/Umsatzgröße und
Ergebnisbeitrag (grün = Zufluss, rot = Verlust).
"""
from deck import *

HEADER = '2. ESWE Versorgungs AG – Übersicht und Herausforderungen'
SOURCES = ('Quellen: Metzler-Recherche, Geschäftsbericht ESWE Versorgungs AG 2025, '
           'Unternehmenswebsite')
FN = ('1) Angaben zum Anteilsbesitz nach § 285 Nr. 11 HGB zum 31. Dezember 2025; mit der '
      'Stadtwerke Wiesbaden Netz GmbH und der WiTCOM GmbH besteht ein Ergebnisabführungs'
      'vertrag, bei der ESWE Taunuswind GmbH und der ESWE Windpark GmbH erfolgt eine '
      'freiwillige Ergebnisübernahme durch die ESWE; 2) Ausschüttung der KMW für das '
      'Geschäftsjahr 2024; 3) Jahresabschluss 2024, Werte für 2025 lagen nicht vor; '
      'die THEE ESWE Windparkbeteiligungs Verwaltungs GmbH (33,33 %) ist nicht dargestellt')

BOX = rgb(0xE1EDFE)          # hellblauer Infokasten
TILE_LINE = rgb(0x1F4E79)    # Rahmen der Namenskachel
GREEN = rgb(0x00B050)
RED = rgb(0xFF0000)
ORANGE = rgb(0xEF664B)
GREY2 = rgb(0xA6A6A6)

# Geometrie (aus der Duisburg-Vorlage übernommen)
COLX = [29.8, 162.1, 294.5, 426.8, 559.1, 691.5]
CW = 120.8
TILE_H = 24.0
R1_TILE_Y, R1_BOX_Y, R1_BOX_H = 248.0, 274.0, 92.0
R2_BUS_Y = 374.0
R2_TILE_Y, R2_BOX_Y, R2_BOX_H = 390.0, 416.0, 90.0
ESWE_BOT = 232.0

# (Name, Quote, Tätigkeit, Kennzahl, Ergebniszeile, Ergebnisfarbe)
ROW1 = [
    ('Stadtwerke Wiesbaden Netz GmbH', '100 %',
     'Betrieb des Stromnetzes in Wiesbaden',
     'Eigenkapital 2025: 69,6 Mio. EUR', 'Gewinnabführung 2025: 5,4 Mio. EUR', GREEN),
    ('WiTCOM GmbH', '100 %',
     'Glasfaser- und Rechenzentrumsgeschäft (B2B und Carrier)',
     'Umsatz 2025: 17,7 Mio. EUR', 'Gewinnabführung 2025: 3,4 Mio. EUR', GREEN),
    ('ESWE BioEnergie GmbH', '90 %',
     'Biomasse-Heizkraftwerk, Strom und Fernwärme',
     'Eigenkapital 2025: 18,8 Mio. EUR', 'Jahresergebnis 2025: 1,3 Mio. EUR', GREEN),
    ('Kraftwerke Mainz-Wiesbaden AG (KMW)', '50 %',
     'Erzeugung und Energiehub der Region',
     'Eigenkapital 2025: 396,0 Mio. EUR', 'Ausschüttung: 14,0 Mio. EUR^2', GREEN),
    ('MHKW Wiesbaden GmbH', '24,5 %',
     'Neues Müllheizkraftwerk, Inbetriebnahmephase läuft',
     'Eigenkapital 2025: 27,4 Mio. EUR', 'Jahresergebnis 2025: −3,5 Mio. EUR', RED),
    ('WRT Infrastrukturbau GmbH', '49 %',
     'Tief- und Rohrleitungsbau (Baukapazitäten)',
     'Eigenkapital 2024: 25 T EUR^3', 'Jahresergebnis 2024: −4 T EUR^3', RED),
]

ROW2 = [
    ('ESWE Taunuswind GmbH', '100 %',
     'Projektgesellschaft Windpark Hohe Wurzel',
     'Eigenkapital 2025: 0,1 Mio. EUR', 'Verlustübernahme durch die ESWE', RED),
    ('ESWE Windpark GmbH', '100 %',
     'Projektgesellschaft für Windenergievorhaben',
     'Eigenkapital 2025: 25 T EUR', 'Verlustübernahme durch die ESWE', RED),
    ('ESWE Windpark Uettingen GmbH & Co. KG', '100 %',
     'Windpark Uettingen in Unterfranken',
     'Eigenkapital 2025: 3,6 Mio. EUR', 'Jahresergebnis 2025: −0,1 Mio. EUR', RED),
    ('Windkraft Kahlenberg GmbH & Co. KG', '50 %',
     'Windpark Kahlenberg',
     'Eigenkapital 2025: 2,6 Mio. EUR', 'Jahresergebnis 2025: −0,2 Mio. EUR', RED),
    ('Windpark Bad Camberg GmbH & Co. KG', '33,33 %',
     'Windpark Bad Camberg',
     'Eigenkapital 2025: 3,1 Mio. EUR', 'Jahresergebnis 2025: −0,3 Mio. EUR', RED),
    ('THEE ESWE Windparkbeteiligungs KG', '33,33 %',
     'Windportfolio gemeinsam mit Thüga Erneuerbare Energien',
     'Eigenkapital 2025: 11,3 Mio. EUR', 'Jahresergebnis 2025: −1,1 Mio. EUR', RED),
]

KENNZAHLEN = [('Umsatz 2025: ', '473,8 Mio. EUR', BLACK),
              ('Jahresüberschuss 2025: ', '48,9 Mio. EUR', GREEN),
              ('Gewinnabführung an die WVV: ', '30,1 Mio. EUR', GREEN),
              ('Ausgleichszahlung Thüga: ', '18,8 Mio. EUR', GREEN)]
KZ_X = [36.0, 200.0, 392.0, 610.0]
KZ_W = [156.0, 184.0, 210.0, 196.0]


def _sup(text, font, size, color, bold=False):
    """'…^2' als hochgestellte Fußnotenziffer setzen."""
    if '^' not in text:
        return [Run(text, font, size, color, bold)]
    base, sup = text.split('^')
    return [Run(base, font, size, color, bold),
            Run(sup + ')', font, size, color, bold, baseline=30)]


def _tile(s, x, y, w, name, size=7.5):
    rect(s, x, y, w, TILE_H, fill=WHITE, linecolor=TILE_LINE, linew=0.9)
    lines = wrap(name, w - 8, size, bold=True)
    y0 = y + (TILE_H - len(lines) * 9.0) / 2.0
    for j, l in enumerate(lines):
        textbox(s, x, y0 + j * 9.0, w, 9.0, [[Run(l, F_TWO, size, DARK, True)]],
                anchor='m', align=PP_ALIGN.CENTER, wrap=False)


def _infobox(s, x, y, w, h, rows):
    rect(s, x, y, w, h, fill=BOX)
    yy = y + 5.0
    for text, color in rows:
        runs_lines = []
        for l in para_lines(text, w - 20, 9.0):
            runs_lines.append(l)
        textbox(s, x + 5.5, yy + 0.5, 7, 10.4, [[wing(6.5, DARK)]], anchor='m', wrap=False)
        paras = []
        for i, l in enumerate(runs_lines):
            paras.append(_sup(l, F_LIGHT, 9.0, color))
        textbox(s, x + 15.0, yy, w - 18, len(runs_lines) * 10.4 + 3, paras, line=10.4)
        yy += len(runs_lines) * 10.4 + 3.0


def _quote(s, cx, y, txt):
    """Beteiligungsquote neben der Verbindungslinie."""
    runs = _sup(txt, F_LIGHT, 9.0, BLACK)
    textbox(s, cx + 2.5, y, 55, 12.1, [runs], anchor='m', wrap=False)


def build(prs):
    s = blank(prs)
    chrome(s, 14, HEADER, SOURCES)
    title_2lines(s, 'Netz, Telekommunikation und Erzeugung sind in zwölf Beteiligungen',
                 'gebündelt − die Ergebnisbeiträge kommen aus sw netz, WiTCOM und der KMW')
    textbox(s, 29.8, 514.0, 782, 34, [[Run(l, F_LIGHT, 8.0, BLACK)]
            for l in para_lines(FN, 780, 8.0)], line=9.6)

    textbox(s, 29.8, 97.9, 500, 21.3,
            [[Run('Beteiligungsstruktur', F_REG, 14.0, GREY, True),
              Run(' (vereinfacht)', F_REG, 14.0, GREY2, False)]], anchor='m', wrap=False)

    # ---------------- Konzernspitze ----------------
    _tile(s, 29.8, 118.0, 626.5, 'Landeshauptstadt Wiesbaden', size=9.0)
    vline(s, 342.0, 138.1, 152.0, DARK, 0.9)
    _quote(s, 342.0, 139.5, '100 %')
    _tile(s, 145.6, 152.0, 575.9, 'WVV Wiesbaden Holding GmbH', size=9.0)
    _tile(s, 732.8, 152.0, 79.4, 'Thüga AG', size=9.0)

    vline(s, 433.5, 174.1, 190.0, DARK, 0.9)
    _quote(s, 433.5, 176.0, '50,62 %')
    vline(s, 772.5, 174.1, 190.0, DARK, 0.9)
    _quote(s, 715.0, 176.0, '49,38 %')

    _tile(s, 29.8, 190.0, 782.4, 'ESWE Versorgungs AG', size=10.0)
    rect(s, 29.8, 214.0, 782.4, 18.0, fill=BOX)
    for i, (label, val, col) in enumerate(KENNZAHLEN):
        x = KZ_X[i]
        textbox(s, x, 215.5, 7, 14.7, [[wing(6.5, DARK)]], anchor='m', wrap=False)
        textbox(s, x + 10.0, 215.0, KZ_W[i], 15.7,
                [[Run(label, F_LIGHT, 9.0, BLACK), Run(val, F_LIGHT, 9.0, col)]],
                anchor='m', wrap=False)

    # ---------------- Reihe 1 ----------------
    for i, (name, q, akt, kpi, erg, col) in enumerate(ROW1):
        x = COLX[i]
        cx = x + CW / 2.0
        vline(s, cx, ESWE_BOT, R1_TILE_Y, DARK, 0.9)
        _quote(s, cx, 234.5, q)
        _tile(s, x, R1_TILE_Y, CW, name)
        _infobox(s, x, R1_BOX_Y, CW, R1_BOX_H,
                 [(akt, BLACK), (kpi, BLACK), (erg, col)])

    # ---------------- Reihe 2 ----------------
    gap_x = (COLX[0] + CW + COLX[1]) / 2.0
    vline(s, gap_x, ESWE_BOT, R2_BUS_Y, DARK, 0.9)
    hline(s, COLX[0] + CW / 2.0, COLX[5] + CW / 2.0, R2_BUS_Y, DARK, 0.9)
    for i, (name, q, akt, kpi, erg, col) in enumerate(ROW2):
        x = COLX[i]
        cx = x + CW / 2.0
        vline(s, cx, R2_BUS_Y, R2_TILE_Y, DARK, 0.9)
        _quote(s, cx, 375.5, q)
        _tile(s, x, R2_TILE_Y, CW, name)
        _infobox(s, x, R2_BOX_Y, CW, R2_BOX_H,
                 [(akt, BLACK), (kpi, BLACK), (erg, col)])

    # ---------------- Beteiligungsobjekte hervorheben ----------------
    dashed_rect(s, 26.0, 244.0, 261.0, 126.0, ORANGE, linew=1.25)
    dashed_rect(s, 26.0, 384.0, 790.0, 126.0, ORANGE, linew=1.25)
    dashed_rect(s, 505.0, 561.0, 22.9, 11.8, ORANGE, linew=1.25)
    line_text(s, 534.0, 559.6, 571.0, 'Mögliche Beteiligungsobjekte (Kapitel 3)',
              F_LIGHT, 8.1, BLACK, w=220)
    return s
