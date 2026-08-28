# -*- coding: utf-8 -*-
"""Titelseite, Agenda und Kapiteltrenner (Pendants evm S. 1, 2, 3, 11, 18)."""
from deck import *

TITLE_L1 = 'Überlegungen zur Kapitalflexibilisierung durch Einbindung privater'
TITLE_L2 = 'Investoren'
DATELINE = 'Wiesbaden / Frankfurt am Main, 28. August 2026'

AGENDA = ['Metzler Corporate Finance – Übersicht und Referenzen',
          'ESWE Versorgungs AG – Übersicht und Herausforderungen',
          'Diskussion möglicher Handlungsoptionen']


def title_page(prs):
    s = blank(prs)
    picture(s, 'title_bg.jpg', 0, 0, PW, PH)
    set_alpha(rect(s, 22, 61, 805, 516, fill=WHITE), 72)
    hline(s, 30, 812, 92)
    line_text(s, 640, 78.7, 90.7, 'Streng vertraulich', F_REG, 12.0, DARK, True, True,
              align=PP_ALIGN.RIGHT, w=172)
    line_text(s, 59.6, 152.1, 172.1, TITLE_L1, F_TWO, 20.0, BLACK, True, w=740)
    line_text(s, 59.6, 176.1, 196.1, TITLE_L2, F_TWO, 20.0, BLACK, True, w=740)
    picture(s, 'eswe_logo.png', 60, 314, 187.0, 187.0 * 517 / 1233.0)
    line_text(s, 53.9, 508.1, 524.1, DATELINE, F_TWO, 16.0, BLACK, True, w=500)
    hline(s, 30, 689, 557)
    hline(s, 699, 786, 557)
    hline(s, 796, 812, 557)
    picture(s, LOGO, 699, 543, 111, 28)
    line_text(s, 30.0, 563.5, 571.6, '1', F_LIGHT, 8.0, BLACK, w=30)
    return s


def agenda(prs):
    s = blank(prs)
    chrome(s, 2)
    line_text(s, 29.8, 40.4, 60.5, 'Agenda', F_REG, 20.0, BLACK, True, w=300)
    for i, txt in enumerate(AGENDA):
        y = 173.0 + i * 47.8
        rect(s, 71, y, 37, 30, fill=DARK)
        textbox(s, 71, y, 37, 30, [[Run(str(i + 1), F_TWO, 20.0, WHITE, True)]],
                anchor='m', align=PP_ALIGN.CENTER, wrap=False)
        line_text(s, 131.9, y + 9.8, y + 23.9, txt, F_TWO, 14.0, DARK, True, w=600)
    return s


def divider(prs, number, title, page):
    s = blank(prs)
    chrome(s, page, rule_y=None)
    hline(s, 30, 812, 255)
    rect(s, 30, 282, 38, 33, fill=DARK)
    textbox(s, 30, 282, 38, 33, [[Run(str(number), F_TWO, 22.0, WHITE, True)]],
            anchor='m', align=PP_ALIGN.CENTER, wrap=False)
    line_text(s, 87.1, 289.8, 309.8, title, F_TWO, 20.0, DARK, True, w=700)
    return s
