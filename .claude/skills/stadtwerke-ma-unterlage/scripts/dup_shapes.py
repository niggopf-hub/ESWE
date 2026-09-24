#!/usr/bin/env python3
"""Spalten der Investitionstabelle duplizieren, loeschen und neu verteilen.

Die Investitionstabelle ist die einzige Folie, auf der die Zahl der Boxen vom Fall abhaengt:
drei Segmente bei evm und DVV, vier bei ESWE, sechs bei Krefeld. Neue Boxen werden nie
frei gezogen, sondern als Kopie vorhandener Shapes erzeugt, damit Schrift, Farbe und
Abstaende stimmen. Danach werden alle Spalten gleichmaessig ueber die Tabellenbreite
verteilt.

    python3 dup_shapes.py deck.pptx --slide 16 --dup "id:98,id:111,id:126,id:109" --dx 8.4 --out deck_v2.pptx
    python3 dup_shapes.py deck.pptx --slide 16 --delete "id:100,id:121,id:128,id:138" --out deck_v2.pptx
    python3 dup_shapes.py deck.pptx --slide 16 --columns "id:98,id:111,id:126,id:109;id:99,id:116,id:127,id:110;id:100,id:121,id:128,id:138" \\
            --area 3.6,25.1 --out deck_v2.pptx

--dup      kopiert die genannten Shapes und verschiebt die Kopien um dx/dy (cm). Die Kopien
           bekommen den Namen "<alt> Kopie". Gruppen werden mitsamt Inhalt kopiert.
--delete   entfernt die genannten Shapes.
--columns  Spalten als Listen von Shapes, durch ';' getrennt; --area = linker Rand und Breite
           des Spaltenbereichs in cm. Jede Spalte wird auf 1/n der Breite gesetzt und ihre
           Shapes proportional in die neue Breite eingepasst.

Shape-IDs zeigt inspect_deck.py --slide N. Reihenfolge fuer vier Spalten aus drei: erst --dup
der dritten Spalte mit dx = Spaltenbreite, dann --columns mit allen vier.

Benoetigt: pip install python-pptx
"""
import argparse
import copy
import os
import sys

try:
    from pptx import Presentation
    from pptx.util import Cm
except ImportError:
    sys.exit("Fehlt: pip install python-pptx")


def alle_shapes(shapes):
    for sh in shapes:
        yield sh
        if sh.shape_type == 6:
            yield from alle_shapes(sh.shapes)


def finde(slide, adresse):
    art, _, wert = adresse.strip().partition(":")
    treffer = []
    for sh in slide.shapes:  # nur oberste Ebene: Gruppen werden als Ganzes behandelt
        if art == "id" and str(sh.shape_id) == wert:
            treffer.append(sh)
        elif art == "name" and sh.name == wert:
            treffer.append(sh)
    if not treffer:
        sys.exit(f"'{adresse}' nicht auf der obersten Ebene der Folie gefunden (inspect_deck.py --slide N)")
    if len(treffer) > 1:
        sys.exit(f"'{adresse}' ist mehrdeutig ({len(treffer)} Shapes) - ueber id: adressieren")
    return treffer[0]


def naechste_id(prs):
    return max(sh.shape_id for s in prs.slides for sh in alle_shapes(s.shapes)) + 1


def dupliziere(prs, slide, shapes, dx, dy):
    neu = []
    nid = naechste_id(prs)
    for sh in shapes:
        el = copy.deepcopy(sh._element)
        slide.shapes._spTree.append(el)
        kopie = slide.shapes[-1]
        # IDs eindeutig halten, auch in Gruppen
        for k in alle_shapes([kopie]):
            k._element.xpath("./*[local-name()='nvSpPr' or local-name()='nvGrpSpPr' or "
                             "local-name()='nvPicPr' or local-name()='nvCxnSpPr']/*[local-name()='cNvPr']")[0].set("id", str(nid))
            nid += 1
        kopie.name = f"{sh.name} Kopie"
        if kopie.left is not None:
            kopie.left = kopie.left + Cm(dx)
            kopie.top = kopie.top + Cm(dy)
        neu.append(kopie)
    return neu


def verteile(spalten, x0, breite):
    n = len(spalten)
    sb = breite / n
    for i, shapes in enumerate(spalten):
        if not shapes:
            continue
        links = min(sh.left for sh in shapes if sh.left is not None)
        rechts = max(sh.left + sh.width for sh in shapes if sh.left is not None)
        alt_breite = max(rechts - links, 1)
        neu_links = Cm(x0 + i * sb)
        faktor = Cm(sb) / alt_breite
        for sh in shapes:
            if sh.left is None:
                continue
            rel = sh.left - links
            sh.left = int(neu_links + rel * faktor)
            if sh.width and sh.width > Cm(0.2):    # Linien mit Breite 0 nicht skalieren
                sh.width = int(sh.width * faktor)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pptx")
    ap.add_argument("--slide", type=int, required=True)
    ap.add_argument("--dup", help="Shapes, die kopiert werden (id:.. oder name:.., kommagetrennt)")
    ap.add_argument("--dx", type=float, default=0.0)
    ap.add_argument("--dy", type=float, default=0.0)
    ap.add_argument("--delete", help="Shapes, die entfernt werden")
    ap.add_argument("--columns", help="Spalten, durch ';' getrennt, je Spalte Shapes kommagetrennt")
    ap.add_argument("--area", help="linker Rand,Breite in cm des Spaltenbereichs, z. B. 3.6,25.1")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    if os.path.abspath(a.out) == os.path.abspath(a.pptx):
        sys.exit("Ziel- und Quelldatei sind identisch - anderen Namen fuer --out waehlen.")

    prs = Presentation(a.pptx)
    if not 1 <= a.slide <= len(prs.slides):
        sys.exit(f"Folie {a.slide} gibt es nicht")
    slide = prs.slides[a.slide - 1]

    if a.dup:
        shapes = [finde(slide, s) for s in a.dup.split(",")]
        neu = dupliziere(prs, slide, shapes, a.dx, a.dy)
        for k in neu:
            print(f"kopiert: <{k.shape_id}> {k.name!r}")
    if a.delete:
        for s in a.delete.split(","):
            sh = finde(slide, s)
            sh._element.getparent().remove(sh._element)
            print(f"entfernt: {s}")
    if a.columns:
        if not a.area:
            sys.exit("--columns braucht --area")
        x0, breite = (float(v) for v in a.area.split(","))
        spalten = [[finde(slide, s) for s in sp.split(",") if s.strip()] for sp in a.columns.split(";")]
        verteile(spalten, x0, breite)
        print(f"{len(spalten)} Spalten auf {breite:.1f} cm ab x={x0:.1f} cm verteilt "
              f"(je {breite / len(spalten):.2f} cm).")
    prs.save(a.out)
    print(f"Gespeichert: {a.out}. Sichtpruefung der Folie {a.slide} ist Pflicht: Icons, Pfeile, Umbrueche.")


if __name__ == "__main__":
    main()
