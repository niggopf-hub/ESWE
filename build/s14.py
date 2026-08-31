# -*- coding: utf-8 -*-
"""Slide 14 — Beteiligungsstruktur im Duisburg-Format (Organigramm mit Ergebnisbeiträgen).

Layout und Formatsprache nach '20240305_Stadtwerke Duisburg_v4', Folie 11.
Alle Aeste sind geklebte Verbindungslinien (Konnektoren an den Verbindungspunkten
der Kacheln) — beim Verschieben einer Kachel laeuft die Linie mit. Die Knicke einer
Reihe liegen ueber eine gemeinsame Adjustierung exakt auf einer Hoehe.
Jeder Infokasten ist genau ein Textfeld mit echten Aufzaehlungszeichen.
"""
import os
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

BOX = rgb(0xE1EDFE)
TILE_LINE = rgb(0x1F4E79)
GREEN = rgb(0x00B050)
RED = rgb(0xFF0000)
ORANGE = rgb(0xEF664B)
GREY2 = rgb(0xA6A6A6)

# ---- Geometrie ----------------------------------------------------------
COLX = [29.8, 162.1, 294.5, 426.8, 559.1, 691.5]
CW = 120.8
TILE_H = 24.0

STADT_X, STADT_W = 87.5, 667.0            # Mitte 421.0
WVV_X, WVV_W = 133.05, 575.9              # Mitte 421.0
THUEGA_X, THUEGA_W = 732.8, 79.4
STADT_Y, WVV_Y, ESWE_Y = 118.0, 152.0, 190.0
BAND_Y, BAND_H = 214.0, 18.0              # Kennzahlenband, Unterkante 232.0
BAND_BOT = BAND_Y + BAND_H

R1_TILE_Y, R1_BOX_Y, R1_BOX_H = 254.0, 280.0, 92.0
R2_TILE_Y, R2_BOX_Y, R2_BOX_H = 396.0, 422.0, 86.0
BUS2_Y = 380.0                            # Verteilerlinie der zweiten Reihe

# (Name, Quote, Tätigkeit, Kennzahl, Ergebniszeile, Ergebnisfarbe, Logo-Datei)
ROW1 = [
    ('Stadtwerke Wiesbaden Netz GmbH', '100 %',
     'Betrieb des Stromnetzes in Wiesbaden',
     'Eigenkapital 2025: 69,6 Mio. EUR', 'Gewinnabführung 2025: 5,4 Mio. EUR', GREEN,
     'logo_swnetz.png'),
    ('WiTCOM GmbH', '100 %',
     'Glasfaser und Rechenzentren (B2B und Carrier)',
     'Umsatz 2025: 17,7 Mio. EUR', 'Gewinnabführung 2025: 3,4 Mio. EUR', GREEN,
     'logo_witcom.png'),
    ('ESWE BioEnergie GmbH', '90 %',
     'Biomasse-Heizkraftwerk, Strom und Fernwärme',
     'Eigenkapital 2025: 18,8 Mio. EUR', 'Jahresergebnis 2025: 1,3 Mio. EUR', GREEN,
     'logo_bioenergie.png'),
    ('Kraftwerke Mainz-Wiesbaden AG (KMW)', '50 %',
     'Erzeugung und Energiehub der Region',
     'Eigenkapital 2025: 396,0 Mio. EUR', 'Ausschüttung: 14,0 Mio. EUR^2', GREEN,
     'logo_kmw.png'),
    ('MHKW Wiesbaden GmbH', '24,5 %',
     'Neues Müllheizkraftwerk (Inbetriebnahme läuft)',
     'Eigenkapital 2025: 27,4 Mio. EUR', 'Jahresergebnis 2025: −3,5 Mio. EUR', RED,
     'logo_mhkw.png'),
    ('WRT Infrastrukturbau GmbH', '49 %',
     'Tief- und Rohrleitungsbau (Baukapazitäten)',
     'Eigenkapital 2024: 25 T EUR^3', 'Jahresergebnis 2024: −4 T EUR^3', RED,
     'logo_wrt.png'),
]

ROW2 = [
    ('ESWE Taunuswind GmbH', '100 %',
     'Projektgesellschaft Windpark Hohe Wurzel',
     'Eigenkapital 2025: 0,1 Mio. EUR', 'Verlustübernahme durch die ESWE', RED,
     'logo_taunuswind.png'),
    ('ESWE Windpark GmbH', '100 %',
     'Projektgesellschaft für Windenergievorhaben',
     'Eigenkapital 2025: 25 T EUR', 'Verlustübernahme durch die ESWE', RED,
     'logo_eswewindpark.png'),
    ('ESWE Windpark Uettingen GmbH & Co. KG', '100 %',
     'Windpark Uettingen in Unterfranken',
     'Eigenkapital 2025: 3,6 Mio. EUR', 'Jahresergebnis 2025: −0,1 Mio. EUR', RED,
     'logo_uettingen.png'),
    ('Windkraft Kahlenberg GmbH & Co. KG', '50 %',
     'Windpark Kahlenberg',
     'Eigenkapital 2025: 2,6 Mio. EUR', 'Jahresergebnis 2025: −0,2 Mio. EUR', RED,
     'logo_kahlenberg.png'),
    ('Windpark Bad Camberg GmbH & Co. KG', '33,33 %',
     'Windpark Bad Camberg',
     'Eigenkapital 2025: 3,1 Mio. EUR', 'Jahresergebnis 2025: −0,3 Mio. EUR', RED,
     'logo_badcamberg.png'),
    ('THEE ESWE Windparkbeteiligungs KG', '33,33 %',
     'Windportfolio gemeinsam mit Thüga Erneuerbare Energien',
     'Eigenkapital 2025: 11,3 Mio. EUR', 'Jahresergebnis 2025: −1,1 Mio. EUR', RED,
     'logo_thee.png'),
]

# (Label, Wert, Farbe, x, Breite) – jedes Feld ein eigenes Rechteck, die vier
# ergeben zusammen das durchgehende Kennzahlenband
KENNZAHLEN = [('Umsatz 2025: ', '473,8 Mio. EUR', BLACK, 29.8, 164.2),
              ('Jahresüberschuss 2025: ', '48,9 Mio. EUR', GREEN, 194.0, 192.0),
              ('Gewinnabführung an die WVV: ', '30,1 Mio. EUR', GREEN, 386.0, 218.0),
              ('Ausgleichszahlung Thüga: ', '18,8 Mio. EUR', GREEN, 604.0, 208.2)]


def _sup_runs(text, font, size, color, bold=False):
    """'…^2' als hochgestellte Fußnotenziffer."""
    if '^' not in text:
        return [Run(text, font, size, color, bold)]
    base, sup = text.split('^')
    return [Run(base, font, size, color, bold),
            Run(sup + ')', font, size, color, bold, baseline=30)]


def _tile(s, x, y, w, name, size=7.5, logo=None):
    """Namenskachel – der Name steht im Textrahmen des Rechtecks selbst.
    Liegt eine Logo-Datei in assets/, wird sie statt des Namens gesetzt."""
    box = rect(s, x, y, w, TILE_H, fill=WHITE, linecolor=TILE_LINE, linew=0.9)
    if logo and os.path.exists(os.path.join(ASSETS, logo)):
        from PIL import Image
        iw, ih = Image.open(os.path.join(ASSETS, logo)).size
        h = min(TILE_H - 7.0, (w - 16.0) * ih / float(iw))
        picture(s, logo, x + (w - h * iw / float(ih)) / 2.0, y + (TILE_H - h) / 2.0,
                h * iw / float(ih), h)
        return box
    shape_text(box, [Run(name, F_TWO, size, DARK, True)], align=PP_ALIGN.CENTER,
               anchor='m', line=9.0, inset=(4.0, 1.0, 4.0, 1.0))
    return box


def _quote(s, cx, y, txt):
    """Beteiligungsquote rechts neben der Verbindungslinie."""
    textbox(s, cx + 3.0, y, 58, 12.0, [_sup_runs(txt, F_LIGHT, 9.0, BLACK)],
            anchor='m', wrap=False)


def build(prs):
    s = blank(prs)
    chrome(s, 14, HEADER, SOURCES)
    title_2lines(s, 'Netz, Telekommunikation und Erzeugung sind in zwölf Beteiligungen',
                 'gebündelt − die Ergebnisbeiträge kommen aus sw netz, WiTCOM und der KMW')
    textbox(s, 29.8, 516.0, 782, 34, [[Run(l, F_LIGHT, 8.0, BLACK)]
            for l in para_lines(FN, 780, 8.0)], line=9.6)

    textbox(s, 29.8, 97.9, 500, 21.3,
            [[Run('Beteiligungsstruktur', F_REG, 14.0, GREY, True),
              Run(' (vereinfacht)', F_REG, 14.0, GREY2, False)]], anchor='m', wrap=False)

    # ---------------- Konzernspitze ----------------
    stadt = _tile(s, STADT_X, STADT_Y, STADT_W, 'Landeshauptstadt Wiesbaden', size=9.0)
    wvv = _tile(s, WVV_X, WVV_Y, WVV_W, 'WVV Wiesbaden Holding GmbH', size=9.0,
                logo='logo_wvv.png')
    thuega = _tile(s, THUEGA_X, WVV_Y, THUEGA_W, 'Thüga AG', size=9.0,
                   logo='logo_thuega.png')
    eswe = _tile(s, 29.8, ESWE_Y, 782.4, 'ESWE Versorgungs AG', size=10.0)

    connect(s, 421.0, STADT_Y + TILE_H, 421.0, WVV_Y,
            begin=(stadt, 2), end=(wvv, 0))
    _quote(s, 421.0, STADT_Y + TILE_H + 1.0, '100 %')
    connect(s, 421.0, WVV_Y + TILE_H, 421.0, ESWE_Y,
            begin=(wvv, 2), end=(eswe, 0))
    _quote(s, 421.0, WVV_Y + TILE_H + 3.0, '50,62 %')
    # Thuega haengt wie die RheinEnergie in der Vorlage senkrecht an der
    # durchgehenden ESWE-Kachel
    connect(s, 772.5, WVV_Y + TILE_H, 772.5, ESWE_Y, begin=(thuega, 2))
    textbox(s, 700.0, WVV_Y + TILE_H + 3.0, 68, 12.0,
            [[Run('49,38 %', F_LIGHT, 9.0, BLACK)]], anchor='m',
            align=PP_ALIGN.RIGHT, wrap=False)

    # ---------------- Kennzahlenband ----------------
    band = None
    for label, val, col, x, w in KENNZAHLEN:
        seg = rect(s, x, BAND_Y, w, BAND_H, fill=BOX)
        shape_text(seg, [[Run(label, F_LIGHT, 9.0, BLACK), Run(val, F_LIGHT, 9.0, col)]],
                   size=9.0, line=11.0, anchor='m', bullets=True, indent=10.0,
                   inset=(6.0, 0.0, 2.0, 0.0), wrap=False)
        if band is None:
            band = seg

    # ---------------- Reihe 1 und 2 ----------------
    # Reihe 2 wird ueber eine Klammer versorgt: senkrecht in der Gasse zwischen
    # Spalte 3 und 4 (genau unter der Mitte der ESWE-Kachel), dann waagerecht
    connect(s, 421.0, BAND_BOT, 421.0, BUS2_Y, begin=(band, 2))
    connect(s, COLX[0] + CW / 2.0, BUS2_Y, COLX[5] + CW / 2.0, BUS2_Y)

    for row, tile_y, box_y, box_h, drop_y in (
            (ROW1, R1_TILE_Y, R1_BOX_Y, R1_BOX_H, BAND_BOT),
            (ROW2, R2_TILE_Y, R2_BOX_Y, R2_BOX_H, BUS2_Y)):
        for i, (name, q, akt, kpi, erg, col, logo) in enumerate(row):
            x = COLX[i]
            cx = x + CW / 2.0
            tile = _tile(s, x, tile_y, CW, name, logo=logo)
            # senkrechter Abgang, oben mittig an die Kachel geklebt
            connect(s, cx, drop_y, cx, tile_y, end=(tile, 0))
            _quote(s, cx, drop_y + 3.0, q)
            info = rect(s, x, box_y, CW, box_h, fill=BOX)
            shape_text(info, [_sup_runs(akt, F_LIGHT, 9.0, BLACK),
                              _sup_runs(kpi, F_LIGHT, 9.0, BLACK),
                              _sup_runs(erg, F_LIGHT, 9.0, col)],
                       size=9.0, line=10.4, before=3.0, anchor='t', bullets=True,
                       indent=10.0, inset=(5.0, 5.0, 4.0, 3.0))

    # ---------------- Beteiligungsobjekte hervorheben ----------------
    dashed_rect(s, 26.0, 250.0, 261.0, 126.0, ORANGE, linew=1.25)
    dashed_rect(s, 26.0, 392.0, 790.0, 120.0, ORANGE, linew=1.25)
    dashed_rect(s, 505.0, 561.0, 22.9, 11.8, ORANGE, linew=1.25)
    line_text(s, 534.0, 559.6, 571.0, 'Mögliche Beteiligungsobjekte (Kapitel 3)',
              F_LIGHT, 8.1, BLACK, w=220)
    return s
