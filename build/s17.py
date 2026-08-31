# -*- coding: utf-8 -*-
"""Slide 17 — Strategie je Geschäftsfeld (Pendant evm S. 17)."""
from deck import *

HEADER = '2. ESWE Versorgungs AG – Übersicht und Herausforderungen'
SOURCES = ('Quellen: Metzler-Recherche, Geschäftsbericht ESWE Versorgungs AG 2025, '
           'Unternehmenswebsite')

BARS = [
    ('gf1.png', 'Stabilisierung der Kundenbasis im intensiven Wettbewerb durch '
     'geschäftsfeldübergreifende Angebote, dynamische Tarife sowie Ausbau von Photovoltaik-, '
     'Wärmepumpen- und Energiemanagementlösungen'),
    ('gf2.png', 'Massiver Ausbau und Digitalisierung des Stromnetzes zur Integration von '
     'Wärmepumpen, Photovoltaik und Ladeinfrastruktur sowie zurückhaltende '
     'Gasnetz-Investitionen mit Prüfung einer künftigen Wasserstoffversorgung'),
    ('gf3.png', 'Dekarbonisierung der Erzeugung über Biomasse und MHKW-Abwärme sowie '
     'Realisierung des Windparks Hohe Wurzel und Ausbau des regionalen EE-Portfolios '
     'gemeinsam mit Thüga und KMW'),
    ('gf4.png', 'Umsetzung der Kommunalen Wärmeplanung als zentraler Partner der Stadt durch '
     'Fernwärmeausbau, Quartierslösungen und Contracting sowie zügiger Ausbau der '
     'Ladeinfrastruktur auf 800 öffentliche Ladepunkte bis 2030'),
    ('gf5.png', 'Ausbau des Glasfaser- und Rechenzentrumsgeschäfts über die WiTCOM als stabil '
     'profitables Wachstumsfeld mit einer Ergebnisabführung von 3,4 Mio. EUR im Jahr 2025'),
    ('gf6.png', 'Langfristige Sicherung der Trinkwasser-Betriebsführung für den städtischen '
     'Eigenbetrieb WLW und Modernisierung der Wasserinfrastruktur als '
     'Investitionsschwerpunkt 2025 (14,0 Mio. EUR)'),
]

BAR_Y = [118.8, 189.5, 260.1, 330.8, 401.4, 472.1]
BAR_H = 63.0
BARBG = rgb(0xEBF4FF)


def build(prs):
    s = blank(prs)
    chrome(s, 17, HEADER, SOURCES)
    title_2lines(s, 'Die ESWE fokussiert sich auf die Wärmewende, resiliente Netze,',
                 'regionale Erzeugung und profitable Wachstumsfelder')
    for (icon, txt), y in zip(BARS, BAR_Y):
        bar = rect(s, 29.8, y, 779.8, BAR_H, fill=BARBG)
        picture(s, icon, 62.0, y + 15.5, 32, 32)
        # Der Satz steht im Textrahmen des Balkens selbst
        shape_text(bar, [Run(nb(txt), F_LIGHT, 10.6, DARK)],
                   line=12.6, anchor='m', inset=(98.2, 4.0, 12.0, 4.0))
    return s
