# -*- coding: utf-8 -*-
"""Baut das ESWE-Deck in der Struktur des evm-Decks vom 13.08.2026."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from deck import new_deck, blank
from replay import replay, page_image
import front, s12, s13, s14, s15, s16, s17, s19, s20

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..',
                   '20260828_Metzler_ESWE Versorgungs AG_vF.pptx')


def build():
    prs = new_deck()
    front.title_page(prs)                                                    # 1
    front.agenda(prs)                                                        # 2
    front.divider(prs, 1, 'Metzler Corporate Finance – Übersicht und Referenzen', 3)
    for p in (4, 5, 6):                                                      # 4-6
        replay(blank(prs), p)
    for p in (7, 8, 9, 10):                                                  # 7-10
        page_image(blank(prs), p)
    front.divider(prs, 2, 'ESWE Versorgungs AG – Übersicht und Herausforderungen', 11)
    s12.build(prs)
    s13.build(prs)
    s14.build(prs)
    s15.build(prs)
    s16.build(prs)
    s17.build(prs)
    front.divider(prs, 3, 'Diskussion möglicher Handlungsoptionen', 18)
    s19.build(prs)
    s20.build(prs)
    replay(blank(prs), 21)                                                   # 21
    replay(blank(prs), 22)                                                   # 22
    prs.save(OUT)
    return OUT


if __name__ == '__main__':
    print(build())
