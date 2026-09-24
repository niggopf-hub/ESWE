#!/usr/bin/env python3
"""Prueft PowerPoint und Report gegen die Schreibregeln des Hauses.

    python3 stil_check.py deck.pptx report.md [weitere Dateien]

Geprueft werden die mechanischen Regeln aus references/schreibregeln.md:
  - Euro-Zeichen statt "Mio. EUR"
  - "Prozent" ausgeschrieben statt Prozentzeichen; Prozentzeichen ohne Leerzeichen
  - "Cash Flow" im Text (Diagrammlegenden "Operating Cash Flow" usw. sind erlaubt)
  - Semikolon im Fliesstext, ausser in Fussnotenzeilen "1) ...; 2) ..."
  - "Corporate Finance" statt "Mergers & Acquisitions"
  - "~" und "Ø" statt "rund" und "durchschnittlich" (ausserhalb von Kacheln und Tabellen)
  - Kausalketten: waehrend, sodass, denn, obwohl, um ... zu (nur als Hinweis)
  - Adjektive, die in den vf-Fassungen gestrichen wurden (nur als Hinweis)

Befunde brechen mit Status 1 ab, Hinweise nicht. Was das Skript nicht prueft: ob ein Titel
ein Aussagesatz ist, ob ein Bullet zu lang ist, ob eine Zahl stimmt.

Benoetigt: pip install python-pptx (nur fuer .pptx)
"""
import re
import sys

for strom in (sys.stdout, sys.stderr):
    try:
        strom.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass

LEGENDE = re.compile(r"^(Operating|Investing|Financing|Total|Free)\s+Cash\s?Flow", re.I)
FUSSNOTE = re.compile(r"^\s*1\)")
KACHEL = re.compile(r"^\s*(ca\.|~)\s*[\d.,]+")

BEFUND = [
    (re.compile(r"€"), "Euro-Zeichen: 'Mio. EUR' schreiben"),
    (re.compile(r"\bProzent\b"), "'Prozent' ausgeschrieben: Prozentzeichen mit Leerzeichen"),
    (re.compile(r"\bCorporate Finance\b"), "Einheitsname ist 'Mergers & Acquisitions'"),
    (re.compile(r"\bCash[ -]Flow\b"), "'Cashflow' im Text (Legenden ausgenommen)"),
    (re.compile(r"\bT€|\bTEUR\b|\bT EUR\b"), "T EUR: auf der Folie nur Mio. EUR"),
]
HINWEIS = [
    (re.compile(r"\d%"), "Prozentzeichen ohne Leerzeichen (Regel: '25 %')"),
    (re.compile(r";\s*[A-ZÄÖÜ]"), "Semikolon mit Grossschreibung dahinter: neuer Bullet"),
    (re.compile(r"(^|\s)~\s?\d"), "'~' im Text: 'rund' (in Kacheln und Tabellen erlaubt)"),
    (re.compile(r"Ø"), "'Ø': 'durchschnittlich'"),
    (re.compile(r"\b(während|sodass|so dass|denn|obwohl)\b", re.I), "Kausalkette: zwei Aussagen sind zwei Bullets"),
    (re.compile(r"\b(kerngesund|massiv|erheblich|konsequent|robust|komfortabel|wirtschaftlichkeitsgeprüft)\w*", re.I),
     "wertendes Adjektiv, in den vf-Fassungen gestrichen"),
    (re.compile(r"[„\"‚'][^\"“‘']{25,}[“\"‘']"), "wörtliches Zitat: gehoert in den Report, nicht auf die Folie"),
    (re.compile(r"\bscheint\b"), "Hedging: nur ohne Beleg stehen lassen"),
    (re.compile(r"\bxxx\b|\bTODO\b|\bWIP\b", re.I), "Platzhalter"),
]


def stellen_pptx(pfad):
    from pptx import Presentation
    prs = Presentation(pfad)

    def walk(shapes):
        for sh in shapes:
            if sh.shape_type == 6:
                yield from walk(sh.shapes)
                continue
            if (sh.name or "").startswith("TBD-"):
                continue
            if sh.has_text_frame:
                for p in sh.text_frame.paragraphs:
                    t = p.text.strip()
                    if t:
                        yield sh.name, t
            if getattr(sh, "has_table", False) and sh.has_table:
                for ri, row in enumerate(sh.table.rows, 1):
                    for ci, c in enumerate(row.cells, 1):
                        t = c.text.strip()
                        if t:
                            yield f"{sh.name}!r{ri}c{ci}", t

    for i, s in enumerate(prs.slides, 1):
        for wo, t in walk(s.shapes):
            yield f"F{i:>2} {wo}", t


def stellen_text(pfad):
    with open(pfad, encoding="utf-8") as f:
        for n, zeile in enumerate(f, 1):
            t = zeile.strip()
            if t:
                yield f"{pfad}:{n}", t


def pruefe(quelle, text, befunde, hinweise, ist_folie):
    if LEGENDE.match(text):
        return
    if ist_folie and FUSSNOTE.match(text):
        # Fussnoten duerfen Semikolons tragen; die anderen Regeln gelten trotzdem
        regeln_b = [r for r in BEFUND]
        regeln_h = [r for r in HINWEIS if "Semikolon" not in r[1]]
    else:
        regeln_b, regeln_h = BEFUND, HINWEIS
    if ist_folie and KACHEL.match(text):
        regeln_h = [r for r in regeln_h if "'~'" not in r[1]]
    for muster, was in regeln_b:
        m = muster.search(text)
        if m:
            befunde.append((quelle, was, auszug(text, m)))
    for muster, was in regeln_h:
        m = muster.search(text)
        if m:
            hinweise.append((quelle, was, auszug(text, m)))


def auszug(text, m):
    a = max(0, m.start() - 35)
    return text[a:a + 80].replace("\n", " ")


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    befunde, hinweise = [], []
    for pfad in sys.argv[1:]:
        if pfad.lower().endswith(".pptx"):
            for q, t in stellen_pptx(pfad):
                pruefe(q, t, befunde, hinweise, True)
        else:
            for q, t in stellen_text(pfad):
                pruefe(q, t, befunde, hinweise, False)
    if befunde:
        print(f"{len(befunde)} Befund(e):")
        for q, was, t in befunde:
            print(f"  {q:<40} {was}\n      -> {t!r}")
    else:
        print("Keine Befunde gegen die harten Regeln.")
    if hinweise:
        print(f"\n{len(hinweise)} Hinweis(e) (von Hand beurteilen):")
        for q, was, t in hinweise:
            print(f"  {q:<40} {was}\n      -> {t!r}")
    sys.exit(1 if befunde else 0)


if __name__ == "__main__":
    main()
