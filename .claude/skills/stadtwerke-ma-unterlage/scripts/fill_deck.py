#!/usr/bin/env python3
"""Schreibt Text in VORHANDENE Boxen und Tabellenzellen - und legt niemals neue an.

Der Sinn: Platzhalter erben Schrift, Groesse, Farbe und Position vom Master. Ein neu
eingefuegtes Textfeld erbt nichts davon. Deshalb bricht dieses Skript ab, wenn ein Ziel
nicht existiert, statt es anzulegen.

Ebenso wichtig und weniger offensichtlich: Beim Ersetzen von Text koennen Reste des alten
Inhalts stehenbleiben, die im Textfeld unsichtbar sind - Hyperlinks auf den alten Mandanten,
Felder (Foliennummer, Datum, eingefuegte Werte), weiche Zeilenumbrueche. Dieses Skript
entfernt sie ausdruecklich und meldet, was es dabei weggeworfen hat.

    python3 fill_deck.py deck.pptx --map befuellung.json --out deck_v2.pptx
    python3 fill_deck.py deck.pptx --map befuellung.json --dry-run

Zieladressen:
    "rolle:quelle"         Rolle der Folie - empfohlen, weil template-unabhaengig.
                           Rollen: titel, kolumne, subline, quelle, fussnote, bereich
    "ph:13"                Platzhalter mit diesem Index
    "name:Text Box 29"     Shape mit exakt diesem Namen (muss eindeutig sein)
    "name:Tab1!r2c1"       Zelle Zeile 2, Spalte 1 der Tabelle 'Tab1' (1-basiert)
    "ph:5!r3c2"            dasselbe fuer eine Tabelle in einem Platzhalter

Beispiel:

    {
      "12": {
        "ph:0":  "Starke Marktposition mit umfangreichem Investitionsprogramm ...",
        "ph:13": "2. Musterversorger AG - Uebersicht und Herausforderungen",
        "ph:15": ["1) Net Debt = ...", "2) Stichtag 31.12.2025"]
      },
      "13": { "name:One Pager!r4c2": "Musterstadt Holding GmbH 50,6 % - Partner AG 49,4 %" }
    }

Eine Liste wird zu mehreren Absaetzen; die Absatzformatierung des Originals bleibt erhalten.

Benoetigt: pip install python-pptx
"""
import argparse
import copy
import json
import os
import re
import sys

try:
    from pptx import Presentation
    from pptx.oxml.ns import qn
except ImportError:
    sys.exit("Fehlt: pip install python-pptx")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vorlage  # noqa: E402  gemeinsame Template-Logik

ZELLE = re.compile(r"^(?P<ziel>.+?)!r(?P<r>\d+)c(?P<c>\d+)$")
# Elemente, die beim Ersetzen sichtbaren oder unsichtbaren Altbestand tragen
ALTLAST = {
    qn("a:fld"): "Feld (Foliennummer, Datum o. ae.)",
    qn("a:br"): "weicher Zeilenumbruch",
}


def alle_shapes(shapes):
    for sh in shapes:
        yield sh
        if sh.shape_type == 6:  # GROUP
            yield from alle_shapes(sh.shapes)


def finde_shapes(slide, art, wert):
    """Alle passenden Shapes - Mehrdeutigkeit wird vom Aufrufer gemeldet, nicht verschluckt."""
    treffer = []
    for sh in alle_shapes(slide.shapes):
        if art == "ph" and sh.is_placeholder:
            try:
                if sh.placeholder_format.idx == int(wert):
                    treffer.append(sh)
            except ValueError:
                return []
        elif art == "name" and sh.name == wert:
            treffer.append(sh)
    return treffer


def rpr_vorlage(paragraph):
    """rPr des ersten Runs als Vorlage - ohne Hyperlinks, die zum alten Inhalt gehoeren."""
    for r in paragraph._p.findall(qn("a:r")):
        rpr = r.find(qn("a:rPr"))
        if rpr is not None:
            v = copy.deepcopy(rpr)
            for tag in ("a:hlinkClick", "a:hlinkMouseOver"):
                for h in v.findall(qn(tag)):
                    v.remove(h)
            return v
    return None


def gemischt(paragraph):
    """True, wenn die Runs des Absatzes unterschiedlich formatiert sind."""
    formate = set()
    for r in paragraph._p.findall(qn("a:r")):
        rpr = r.find(qn("a:rPr"))
        formate.add(str(rpr.xml) if rpr is not None else "")
        if len(formate) > 1:
            return True
    return False


def absatz_neu(paragraph, text, vorlage):
    """Leert den Absatz vollstaendig und setzt genau einen Run - meldet Verworfenes."""
    p = paragraph._p
    verworfen = []
    for kind in list(p):
        if kind.tag == qn("a:pPr"):
            continue
        if kind.tag in ALTLAST:
            verworfen.append(ALTLAST[kind.tag])
        elif kind.tag == qn("a:r"):
            rpr = kind.find(qn("a:rPr"))
            if rpr is not None and rpr.find(qn("a:hlinkClick")) is not None:
                verworfen.append("Hyperlink auf den alten Inhalt")
        p.remove(kind)
    r = p.makeelement(qn("a:r"), {})
    if vorlage is not None:
        r.append(copy.deepcopy(vorlage))
    t = p.makeelement(qn("a:t"), {})
    t.text = text
    r.append(t)
    p.append(r)
    return verworfen


def schreibe(textframe, inhalt):
    """Ersetzt den Text vollstaendig. Gibt (Warnungen, Verworfenes) zurueck."""
    zeilen = [str(z) for z in (inhalt if isinstance(inhalt, list) else [inhalt])]
    warn, verworfen = [], []
    erster = textframe.paragraphs[0]
    if gemischt(erster):
        warn.append(
            "Absatz war gemischt formatiert; der neue Text uebernimmt die Formatierung "
            "des ersten Runs. Wenn Teile anders aussehen sollen, von Hand nacharbeiten."
        )
    vorlage_rpr = rpr_vorlage(erster)
    vorlage_p = copy.deepcopy(erster._p)

    for p in list(textframe.paragraphs)[1:]:
        p._p.getparent().remove(p._p)
    verworfen += absatz_neu(textframe.paragraphs[0], zeilen[0], vorlage_rpr)

    for zeile in zeilen[1:]:
        neu = copy.deepcopy(vorlage_p)
        textframe._txBody.append(neu)
        verworfen += absatz_neu(textframe.paragraphs[-1], zeile, vorlage_rpr)
    return warn, sorted(set(verworfen))


def platzschaetzung(shape, text):
    r = vorlage.ueberlauf(shape, text)
    return f"Text {r}. Sichtpruefung noetig." if r else None


def loese_ziel(slide, adresse):
    """Gibt (textframe, shape, fehler) zurueck. Tabellenzellen werden mit aufgeloest."""
    m = ZELLE.match(adresse)
    zelle = None
    if m:
        adresse, zelle = m.group("ziel"), (int(m.group("r")), int(m.group("c")))
    art, _, wert = adresse.partition(":")
    if art not in ("ph", "name", "rolle"):
        return None, None, f"'{adresse}': unbekannte Adressart (erlaubt: rolle:, ph:, name:)"
    if art == "rolle":
        if wert not in vorlage.ROLLEN_MUSTER and wert != "titel":
            return None, None, (f"'{adresse}': unbekannte Rolle "
                                f"(erlaubt: titel, {', '.join(vorlage.ROLLEN_MUSTER)})")
        treffer = vorlage.finde_rolle(slide, wert)
        if not treffer:
            return None, None, (
                f"'{adresse}': Folie hat keine Box fuer diese Rolle - keine neue angelegt. "
                "Die Box von einer Nachbarfolie desselben Layouts kopieren (gleiche "
                "Position, gleiches Format) und dann befuellen.")
    else:
        treffer = finde_shapes(slide, art, wert)
    if not treffer:
        return None, None, (f"'{adresse}' nicht gefunden - keine neue Box angelegt. "
                            "Ziel mit inspect_deck.py pruefen.")
    if len(treffer) > 1:
        return None, None, (f"'{adresse}' ist mehrdeutig: {len(treffer)} Shapes tragen "
                            "diesen Namen. Eindeutig benennen oder ueber ph: adressieren.")
    sh = treffer[0]
    if zelle:
        if not sh.has_table:
            return None, None, f"'{adresse}': Shape ist keine Tabelle"
        r, c = zelle
        tb = sh.table
        if not (1 <= r <= len(tb.rows) and 1 <= c <= len(tb.columns)):
            return None, None, (f"'{adresse}': Zelle ausserhalb der Tabelle "
                                f"({len(tb.rows)}x{len(tb.columns)})")
        return tb.cell(r - 1, c - 1).text_frame, sh, None
    if sh.has_table:
        return None, None, (f"'{adresse}' ist eine Tabelle - Zelle angeben, "
                            f"z. B. '{adresse}!r2c1'")
    if not sh.has_text_frame:
        return None, None, f"'{adresse}' nimmt keinen Text auf"
    return sh.text_frame, sh, None


def main():
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("pptx")
    ap.add_argument("--map", required=True, help="JSON mit der Zuordnung")
    ap.add_argument("--out", help="Zieldatei (ohne --out nur Probelauf)")
    ap.add_argument("--dry-run", action="store_true", help="nur pruefen, nichts schreiben")
    a = ap.parse_args()

    if a.out and os.path.abspath(a.out) == os.path.abspath(a.pptx):
        sys.exit("Ziel- und Quelldatei sind identisch. Die Vorlage wird nicht ueberschrieben "
                 "- anderen Namen fuer --out waehlen.")

    prs = Presentation(a.pptx)
    with open(a.map, encoding="utf-8") as f:
        zuordnung = json.load(f)

    schreiben = bool(a.out) and not a.dry_run
    fehler, protokoll, hinweise = [], [], []

    for folie_nr, felder in zuordnung.items():
        try:
            nr = int(folie_nr)
        except ValueError:
            fehler.append(f"Folienummer '{folie_nr}' ist keine Zahl")
            continue
        if not 1 <= nr <= len(prs.slides):
            fehler.append(f"Folie {nr} gibt es nicht (1..{len(prs.slides)})")
            continue
        slide = prs.slides[nr - 1]
        for adresse, inhalt in felder.items():
            if isinstance(inhalt, list) and not inhalt:
                fehler.append(f"F{nr}: '{adresse}' hat eine leere Inhaltsliste. "
                              "Leeren Text als \"\" angeben, wenn das gewollt ist.")
                continue
            tf, sh, err = loese_ziel(slide, adresse)
            if err:
                fehler.append(f"F{nr}: {err}")
                continue
            text = inhalt if isinstance(inhalt, str) else "\n".join(map(str, inhalt))
            if schreiben:
                warn, verworfen = schreibe(tf, inhalt)
                for w in warn:
                    hinweise.append(f"F{nr} {adresse}: {w}")
                for v in verworfen:
                    hinweise.append(f"F{nr} {adresse}: {v} wurde entfernt.")
            if sh is not None and not sh.has_table:
                eng = platzschaetzung(sh, text)
                if eng:
                    hinweise.append(f"F{nr} {adresse}: {eng}")
            protokoll.append(f"F{nr:>2}  {adresse:<26} <- {text[:52]}")

    for z in protokoll:
        print(z)
    if hinweise:
        print("\nHinweise:")
        for h in hinweise:
            print(f"  {h}")
    if fehler:
        print(f"\n{len(fehler)} Problem(e):", file=sys.stderr)
        for f in fehler:
            print(f"  {f}", file=sys.stderr)
        sys.exit(1)

    if schreiben:
        prs.save(a.out)
        print(f"\nGespeichert: {a.out}  ({len(protokoll)} Felder)")
        print("Naechster Schritt: inspect_deck.py --check --vergleich <vorlage.pptx>")
    else:
        print(f"\nProbelauf ohne Befund ({len(protokoll)} Felder wuerden geschrieben).")


if __name__ == "__main__":
    main()
