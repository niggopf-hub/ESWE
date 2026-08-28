# -*- coding: utf-8 -*-
"""Slide 15 — Investitionsmatrix + CapEx-Chart (Pendant evm S. 15)."""
from deck import *

HEADER = '2. ESWE Versorgungs AG – Übersicht und Herausforderungen'
SOURCES = ('Quellen: Metzler-Recherche, Jahresabschlüsse ESWE Versorgungs AG 2021–2025, '
           'Unternehmenswebsite')
FN = ('1) Anstieg von Ø ~22 Mio. EUR p. a. (letzte 20 Jahre) auf bis zu 80 Mio. EUR p. a. gemäß '
      'Interview des früheren Vorstandsvorsitzenden (zfk); keine öffentliche quantitative '
      'Aufteilung nach Investitionsschwerpunkten verfügbar')

TITLEBAR = rgb(0xF2F2F2)
R1_LAB, R1_BG = rgb(0xADBCF4), rgb(0xD6DDF9)
R2_LAB, R2_BG = rgb(0xC6D1F7), rgb(0xE3E8FB)
R3_LAB, R3_BG = rgb(0xC2DBFC), rgb(0xE1EDFE)
BAR = rgb(0x3157E3)

COLS = [
    (219.4, 'gf4.png', 'Wärmenetze & Wärmewende', [
        'Konsequenter Fernwärmeausbau mit Schwerpunkt Innenstadt (BEW-gefördert); neue '
        'Pumpstation Deponiestraße (~8 Mio. EUR, seit 04/2024) als realisierter Anker des '
        'Verbundnetzes',
        'Anbindung des neuen Müllheizkraftwerks (~40 MW thermisch, ~100 GWh Wärme p. a.; '
        'Inbetriebnahmephase läuft) und sukzessive Ablösung der erdgasbefeuerten Heizwerke',
        'Transformationsplan für ein klimaneutrales Fernwärmenetz sowie Prüfung von '
        'Großwärmepumpen, Flusswärme und Geothermie']),
    (456.3, 'gf2.png', 'Strom- & Gasnetze & Digitalisierung', [
        'Massiver Stromnetzausbau durch die sw netz – der Energieentwicklungsplan erwartet '
        'die künftige Wärmeversorgung großteils über Wärmepumpen',
        'Smart-Meter-Rollout und IT-Transformation (Thüga-Abrechnungsplattform TAP als '
        'SAP-Ablösung)',
        'Zurückhaltende Gasnetz-Investitionen: Erneuerung nur bei technischer Notwendigkeit, '
        'Prüfung der H2-Tauglichkeit („Rh2ein-Main Connect" ab 2028)']),
    (693.7, 'gf3.png', 'Erneuerbare Erzeugung & E-Mobilität', [
        'Windpark Hohe Wurzel (10 Anlagen, ~30 MW, ~85 GWh p. a.) nach erneut positivem '
        'VGH-Entscheid (02/2026) juristisch weit fortgeschritten – Berufung noch anhängig',
        'Ausbau des regionalen Wind-/PV-Portfolios gemeinsam mit Thüga Erneuerbare Energien '
        'und der KMW',
        'Ladeinfrastruktur-Konzession: 800 öffentliche Ladepunkte bis 2030, davon bereits '
        '446 errichtet']),
]

CAPEX = [('2021', 43), ('2022', 54), ('2023', 27), ('2024', 27), ('2025', 37)]
TARGET = 80

TAKEAWAY = ('Bankdarlehen allein werden künftig nicht ausreichen − schon heute sichern '
            'Bürgschaften der Stadt und Kapitaleinlagen die Finanzierung')


def build(prs):
    s = blank(prs)
    chrome(s, 15, HEADER, SOURCES)
    title_2lines(s, 'Die ESWE ist finanziell solide aufgestellt − der Investitionshochlauf',
                 'auf bis zu 80 Mio. EUR p. a. übersteigt die bisherige Größenordnung')
    textbox(s, 29.8, 535.6, 665, 20, [[Run(l, F_LIGHT, 8.0, BLACK)]
            for l in para_lines(FN, 660, 8.0)], line=9.6)

    # ---------------- Matrix ----------------
    rect(s, 29.8, 118.8, 782.4, 19.9, fill=TITLEBAR)
    line_text(s, 40.0, 122.5, 134.5, 'Investitionsbedarf', F_TWO, 10.0, DARK, True, w=200)
    rect(s, 29.8, 141.0, 70.0, 73.3, fill=R1_LAB)
    rect(s, 101.0, 141.0, 710.7, 73.3, fill=R1_BG)
    rect(s, 29.8, 218.2, 70.0, 36.4, fill=R2_LAB)
    rect(s, 101.0, 218.2, 711.2, 36.4, fill=R2_BG)
    rect(s, 29.8, 258.5, 70.0, 145.0, fill=R3_LAB)
    rect(s, 101.1, 258.5, 711.7, 145.0, fill=R3_BG)
    textbox(s, 34.0, 141.0, 62, 73.3,
            [[Run('Investitions-', F_TWO, 9.0, DARK, True)],
             [Run('schwerpunkt', F_TWO, 9.0, DARK, True)]], anchor='m', line=11.0)
    textbox(s, 34.0, 218.2, 62, 36.4, [[Run('CapEx', F_TWO, 9.0, DARK, True)]], anchor='m')
    textbox(s, 34.0, 258.5, 62, 145.0,
            [[Run('Geplante', F_TWO, 9.0, DARK, True)],
             [Run('Projekte', F_TWO, 9.0, DARK, True)]], anchor='m', line=11.0)
    for x in (337.9, 574.7):
        vline(s, x, 152.5, 202.9, rgb(0xCCCCCC), 1.5, dash=True)
        vline(s, x, 277.0, 385.0, rgb(0xCCCCCC), 1.5, dash=True)

    for i, (cx, icon, title, bullets) in enumerate(COLS):
        oval(s, cx, 170.2, 43.2, 43.2, fill=None, linecolor=DARK, linew=2.0)
        picture(s, icon, cx - 13, 157.5, 26, 26)
        for j, l in enumerate(wrap(title, 215, 10.0, bold=True)):
            textbox(s, cx - 115, 198.0 + j * 12.0, 230, 12,
                    [[Run(l, F_TWO, 10.0, DARK, True)]], anchor='m',
                    align=PP_ALIGN.CENTER, wrap=False)
        x0 = [101.1, 337.9, 574.7][i]
        yy = 265.0
        for b in bullets:
            ls = para_lines(b, 200, 9.0)
            textbox(s, x0 + 12, yy, 8, 10.8, [[wing(7.7, DARK)]], anchor='m', wrap=False)
            textbox(s, x0 + 24, yy - 0.5, 206, len(ls) * 10.8 + 3,
                    [[Run(l, F_LIGHT, 9.0, BLACK)] for l in ls], line=10.8)
            yy += len(ls) * 10.8 + 4.5

    # CapEx-Klammer
    hline(s, 187.0, 727.0, 233.2, DARK, 1.5)
    vline(s, 187.0, 226.9, 239.5, DARK, 1.5)
    vline(s, 727.0, 226.9, 239.5, DARK, 1.5)
    rect(s, 366.0, 220.5, 182.0, 25.0, fill=R2_BG)
    textbox(s, 366.0, 221.5, 182, 12,
            [[Run(nb('Anstieg auf bis zu 80 Mio. EUR p. a.'), F_TWO, 10.0, DARK, True)]],
            anchor='m', align=PP_ALIGN.CENTER, wrap=False)
    textbox(s, 360.0, 233.5, 194, 12,
            [[Run(nb('von Ø ~22 Mio. EUR p. a. in den letzten 20 Jahren'), F_TWO, 9.0,
                  BAR, True),
              Run('1)', F_TWO, 9.0, BAR, True, baseline=30)]],
            anchor='m', align=PP_ALIGN.CENTER, wrap=False)

    # ---------------- CapEx-Chart ----------------
    line_text(s, 51.0, 425.0, 437.0, 'Entwicklung der Investitionen (Mio. EUR)',
              F_TWO, 10.0, DARK, True, w=300)
    BASE_Y, SCALE = 519.6, 60.0 / 90.0
    X0, BW, PITCH = 51.0, 54.0, 96.4
    hline(s, 29.9, 510.0, BASE_Y, GREY, 0.75)
    for i, (yr, val) in enumerate(CAPEX):
        x = X0 + i * PITCH
        h = val * SCALE
        rect(s, x, BASE_Y - h, BW, h, fill=BAR)
        textbox(s, x, BASE_Y - h - 13, BW, 12, [[Run(str(val), F_LIGHT, 10.0, BLACK)]],
                anchor='m', align=PP_ALIGN.CENTER, wrap=False)
        textbox(s, x, BASE_Y + 3, BW, 12, [[Run(yr, F_LIGHT, 10.0, BLACK)]],
                anchor='m', align=PP_ALIGN.CENTER, wrap=False)
    ty = BASE_Y - TARGET * SCALE
    hline(s, 45.0, 500.0, ty, DARK, 1.25, dash=True)
    textbox(s, 295.0, ty - 15, 205, 12,
            [[Run('Zielniveau: bis zu 80 Mio. EUR p. a.', F_TWO, 9.0, DARK, True),
              Run('1)', F_TWO, 9.0, DARK, True, baseline=30)]],
            anchor='m', align=PP_ALIGN.RIGHT, wrap=False)
    rect(s, 51.0, 440.5, 12, 9, fill=BAR)
    line_text(s, 67.0, 440.0, 450.0, 'CapEx inkl. Finanzanlagen', F_LIGHT, 9.0, BLACK, w=160)

    # ---------------- Takeaway ----------------
    ar = rect(s, 520.0, 452.0, 34, 16, fill=BAR, shape=MSO_SHAPE.RIGHT_ARROW)
    tl = para_lines(TAKEAWAY, 245, 10.0, bold=True)
    textbox(s, 562.0, 447.0, 250, len(tl) * 12.6 + 4,
            [[Run(l, F_TWO, 10.0, DARK, True)] for l in tl], line=12.6)
    return s
