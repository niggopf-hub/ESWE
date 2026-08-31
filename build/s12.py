# -*- coding: utf-8 -*-
"""Slide 12 — Ausgangslage (Pendant evm S. 12)."""
from deck import *

HEADER = '2. ESWE Versorgungs AG – Übersicht und Herausforderungen'
SOURCES = ('Quellen: Metzler-Recherche, Geschäftsbericht ESWE Versorgungs AG 2025, '
           'Unternehmenswebsite')

BULLETS_RAW = [
    'ESWE ist der zentrale Energieversorger und Energiedienstleister der hessischen '
    'Landeshauptstadt Wiesbaden und versorgt rund 200.000 Kunden mit Strom, Erdgas, Wärme '
    'sowie energienahen Dienstleistungen',

    'Das Geschäftsmodell verbindet Vertrieb, Netzinfrastruktur, Erzeugung und '
    'Dienstleistungen: Das Stromnetz ist in der 100%igen Tochter Stadtwerke Wiesbaden Netz '
    'GmbH (sw netz) gebündelt, Gas-, Wasser- und Wärmenetz betreibt die AG selbst; hinzu '
    'kommen Telekommunikation (WiTCOM) und ein regionales Erzeugungsportfolio (Biomasse, '
    'Wind, 50 % KMW)',

    'Mit einem Umsatz von 474 Mio. EUR und einem Jahresüberschuss von 49 Mio. EUR übertraf '
    'die ESWE 2025 ihr Planergebnis (33 Mio. EUR) deutlich – nach zwei sondereffekt'
    'getriebenen Rekordjahren 2023/2024',

    'Duale Aktionärsstruktur seit 2001: 50,62 % Landeshauptstadt Wiesbaden (über die WVV '
    'Wiesbaden Holding), 49,38 % Thüga AG als strategischer Partner; Gewinnabführung an die '
    'WVV, vertragliche Ausgleichszahlung an die Thüga',

    'ESWE ist zentraler Umsetzungspartner der im Juni 2026 beschlossenen Kommunalen '
    'Wärmeplanung mit dem Ziel der Klimaneutralität Wiesbadens bis 2045; für das '
    'Fernwärmenetz läuft ein Transformationsplan zur Klimaneutralität',

    'Das Investitionsvolumen wird sich laut Lagebericht „in den nächsten Jahren nochmals '
    'erheblich steigern" – von Ø ~22 Mio. EUR p. a. in den letzten 20 Jahren auf bis zu '
    '80 Mio. EUR p. a. für Strom- und Wärmenetze, MHKW-Anbindung, Windpark Hohe Wurzel und '
    'Ladeinfrastruktur',

    'Zur Sicherung der Ziel-Eigenkapitalquote von dauerhaft über 25 % sind bereits heute '
    'Kapitaleinlagen der Aktionäre erforderlich (2025: 10 Mio. EUR in die Kapitalrücklage; '
    'weitere Zuführung für 2026 beschlossen)',
]

BULLETS = [nb(b) for b in BULLETS_RAW]

TAKEAWAY = nb('Die Finanzierung des von Ø ~22 auf bis zu 80 Mio. EUR p. a. wachsenden '
            'Investitionsprogramms bei zeitgleicher Wahrung finanzieller und strategischer '
            'Flexibilität ist die zentrale Herausforderung der ESWE Versorgungs AG')


def build(prs):
    s = blank(prs)
    chrome(s, 12, HEADER, SOURCES)
    title_2lines(s,
                 'Kerngesunder kommunaler Versorger mit starker Ergebnishistorie −',
                 'am Beginn der investitionsintensivsten Phase seiner Geschichte')
    line_text(s, 29.8, 101.5, 115.5, 'Unser Verständnis der Ausgangslage',
              F_REG, 14, GREY, True, w=400)

    kachel = soft_shadow(rect(s, 30, 128, 98, 350, fill=DARK))
    kasten = soft_shadow(rect(s, 139, 128, 673, 350, fill=LIGHTBOX,
                              linecolor=rgb(0xD9D9D9), linew=0.75))

    # Label und Bullets stehen im Textrahmen der jeweiligen Form
    shape_text(kachel, [Run('Ausgangslage', F_TWO, 10.6, WHITE, True)],
               align=PP_ALIGN.CENTER, anchor='t', inset=(2.0, 145.6, 2.0, 2.0))
    picture(s, 'doc_icon.png', 56.5, 296, 45, 60)

    shape_text(kasten, BULLETS, size=10.6, line=12.7, before=13.5, anchor='m',
               bullets=True, indent=28.4, inset=(11.5, 12.0, 15.0, 12.0))

    # Takeaway-Banner
    banner = soft_shadow(rect(s, 30, 495, 782, 41, fill=WHITE, linecolor=DARK,
                              linew=1.0))
    chev = rect(s, 30, 497, 14.5, 37, fill=DARK, shape=MSO_SHAPE.PENTAGON)
    try:
        chev.adjustments[0] = 0.62
    except Exception:
        pass
    shape_text(banner, [Run(TAKEAWAY, F_TWO, 10.6, DARK, True)],
               line=12.6, anchor='m', inset=(33.8, 3.0, 12.0, 3.0))
    return s
