#!/usr/bin/env python3
"""Inventar und Pruefung einer Unterlage.

    python3 inspect_deck.py deck.pptx                      Uebersicht
    python3 inspect_deck.py deck.pptx --slide 12           eine Folie im Detail
    python3 inspect_deck.py deck.pptx --check              Inhaltspruefung
    python3 inspect_deck.py neu.pptx --vergleich alt.pptx  Shapes gegen die Vorlage
    python3 inspect_deck.py neu.pptx --check --vergleich alt.pptx    beides
    python3 inspect_deck.py neu.pptx --check --fremdnamen "evm,Koblenz"  alte Mandanten suchen

Was dieses Skript NICHT leistet, und was deshalb trotz gruener Meldung von Hand zu pruefen
bleibt: ob die Zahlen stimmen, ob die Diagramme aktuelle Daten zeigen (ein erhaltenes
think-cell-Objekt kann alte Werte enthalten), und wie die Folie tatsaechlich aussieht. Ein
Rueckgabestatus 0 bescheinigt ausschliesslich die hier geprueften Eigenschaften.

Benoetigt: pip install python-pptx
"""
import argparse
import re
import sys

try:
    from pptx import Presentation
    from pptx.util import Emu
except ImportError:
    sys.exit("Fehlt: pip install python-pptx")

import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vorlage  # noqa: E402  gemeinsame Template-Logik

# Ausgabe auch unter Windows-Konsolen ohne UTF-8 lesbar halten
for strom in (sys.stdout, sys.stderr):
    try:
        strom.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass

ROLLEN_TEXT = {
    "titel": "Titel (Aussagesatz)",
    "kolumne": "Kapitelkolumne",
    "subline": "Subline",
    "quelle": "Quellenzeile",
    "fussnote": "Fussnotenzeile",
    "bereich": "Bereichsueberschrift",
}
VERDACHT = [
    (re.compile(r"\bWIP\b|\bTODO\b|\bTBD\b|\bDRAFT\b|\bPLATZHALTER\b", re.I), "Arbeitsnotiz"),
    (re.compile(r"https?://"), "Quell-URL im Dokument"),
    (re.compile(r"‹[^›]*›|\bX{3,6}\b|\bN\.?N\.?\b"), "unersetzter Platzhalter"),
    (re.compile(r"^\s*(Lorem|Text hier|Beispieltext)", re.I), "Blindtext"),
]


def cm(v):
    return round(Emu(v).cm, 1) if v is not None else None


def alle_shapes(shapes, tiefe=0):
    for sh in shapes:
        yield sh, tiefe
        if sh.shape_type == 6:  # GROUP
            yield from alle_shapes(sh.shapes, tiefe + 1)


def flach(slide):
    for sh, _ in alle_shapes(slide.shapes):
        yield sh


def texte(sh):
    """Alle Textstellen eines Shapes - Textrahmen UND Tabellenzellen.

    Tabellen sind die haeufigste blinde Stelle: der One Pager und die Financial-Tabelle
    stehen in Tabellen, und wer nur Textrahmen liest, prueft genau die Folien nicht, auf
    denen die Zahlen stehen.
    """
    if sh.has_text_frame:
        t = sh.text_frame.text.strip()
        if t:
            yield ("Textrahmen", t)
    if sh.has_table:
        tb = sh.table
        for ri, row in enumerate(tb.rows, 1):
            for ci, zelle in enumerate(row.cells, 1):
                t = zelle.text.strip()
                if t:
                    yield (f"Zelle r{ri}c{ci}", t)


def haupttext(sh):
    return sh.text_frame.text.strip() if sh.has_text_frame else ""


def ueberlauf(sh):
    r = vorlage.ueberlauf(sh)
    return f"Text {r}" if r else None


def signatur(sh):
    return (sh.name, str(sh.shape_type))


# ---------------------------------------------------------------- Uebersicht

def uebersicht(prs):
    print(f"Folien: {len(prs.slides)}   Groesse: {cm(prs.slide_width)} x {cm(prs.slide_height)} cm"
          f"   Template: {vorlage.template(prs)}\n")
    for i, s in enumerate(prs.slides, 1):
        titel = kolumne = ""
        n_ph = n_leer = n_box = n_tab = n_chart = 0
        thinkcell = False
        for sh in flach(s):
            if sh.is_placeholder:
                n_ph += 1
                idx = sh.placeholder_format.idx
                t = haupttext(sh)
                if not t:
                    n_leer += 1
                if idx == 0:
                    titel = t
            elif sh.has_text_frame and haupttext(sh):
                n_box += 1
            if sh.has_table:
                n_tab += 1
            if sh.has_chart:
                n_chart += 1
            if "think-cell" in (sh.name or ""):
                thinkcell = True
        kolumne = vorlage.rollentext(s, "kolumne") if vorlage.ist_inhaltsfolie(s) else ""
        extra = (f" Tab={n_tab}" if n_tab else "") + (f" Chart={n_chart}" if n_chart else "")
        marker = " [think-cell]" if thinkcell else ""
        print(f"F{i:>2} | {s.slide_layout.name:<18} | PH {n_ph} (leer {n_leer}) "
              f"Boxen {n_box}{extra}{marker}")
        print(f"     Titel:   {titel.replace(chr(10), ' . ')[:96] or '- kein Titel -'}")
        if kolumne:
            print(f"     Kolumne: {kolumne[:96]}")


def detail(prs, nr):
    if not 1 <= nr <= len(prs.slides):
        sys.exit(f"Folie {nr} gibt es nicht (1..{len(prs.slides)})")
    s = prs.slides[nr - 1]
    print(f"### Folie {nr} - Layout {s.slide_layout.name}\n")
    rollen = vorlage.rollen_im_layout(s.slide_layout)
    je_idx = {v: k for k, v in rollen.items()}
    print(f"Template: {vorlage.template(prs)}")
    print("Platzhalter des Layouts (Rolle aus dem Mustertext):")
    for ph in s.slide_layout.placeholders:
        idx = ph.placeholder_format.idx
        rolle = je_idx.get(idx)
        name = ROLLEN_TEXT.get(rolle, "") if rolle else vorlage.ph_typ(ph).lower()
        adr = f"rolle:{rolle}" if rolle else ""
        print(f"  ph:{idx:<3} {name:<22} {adr:<16} Mustertext: {vorlage.mustertext(ph)[:40]!r}")
    print("\nShapes der Folie (vollstaendige Namen - sie sind die Zieladresse):")
    for sh, tiefe in alle_shapes(s.shapes):
        ind = "    " * tiefe
        adr = (f"ph:{sh.placeholder_format.idx}" if sh.is_placeholder else f"name:{sh.name}")
        rolle = (ROLLEN_TEXT.get(je_idx.get(sh.placeholder_format.idx), "")
                 if sh.is_placeholder else "")
        kopf = f"{ind}  {adr}" + (f"  [{rolle}]" if rolle else "")
        stellen = list(texte(sh))
        if stellen:
            for wo, t in stellen:
                zusatz = f"!r{wo[6]}c{wo[8]}" if wo.startswith("Zelle") else ""
                print(f'{kopf}{zusatz}  "{t.replace(chr(10), " | ")[:96]}"')
        elif sh.has_chart:
            print(f"{kopf}  [Diagramm {sh.chart.chart_type}]")
        elif "think-cell" in (sh.name or ""):
            print(f"{kopf}  [think-cell-Datenobjekt - nicht loeschen]")
        else:
            print(f"{kopf}  [{sh.shape_type}]")
    leer = [f"ph:{sh.placeholder_format.idx}" for sh in flach(s)
            if sh.is_placeholder and not haupttext(sh)]
    print("\nLeere Platzhalter: " + (", ".join(leer) if leer else "keine"))


# ---------------------------------------------------------------- Inhaltspruefung

def agenda_kapitel(prs):
    """Kapitelnamen aus der Agendafolie - der Massstab fuer Kolumnen und Trenner.

    Datum, Foliennummer und Fusszeile werden ignoriert; in Agenda-Tabellen zaehlt je
    Zeile nur die laengste Zelle (die Nummer und die Seitenzahl daneben nicht).
    """
    datum = re.compile(r"^\d{1,2}[./]\d{1,2}[./]\d{2,4}$")
    for s in prs.slides:
        if "agenda" not in s.slide_layout.name.lower():
            continue
        namen = []
        for sh in flach(s):
            if sh.is_placeholder and vorlage.ph_typ(sh) in vorlage.TECHNISCH:
                continue
            if sh.has_table:
                for row in sh.table.rows:
                    zellen = [c.text.strip() for c in row.cells if c.text.strip()]
                    if zellen:
                        namen.append(max(zellen, key=len))
                continue
            if sh.has_text_frame:
                for zeile in sh.text_frame.text.split("\n"):
                    z = zeile.strip()
                    if len(z) > 8 and z.lower() != "agenda" and not datum.match(z):
                        namen.append(z)
        namen = [n for n in namen if len(n) > 8 and not n.isdigit()]
        if namen:
            return namen
    return []


def check(prs, fremdnamen=()):
    befunde = []
    kapitel = agenda_kapitel(prs)
    fremd = [re.compile(r"(?<!\w)" + re.escape(n.strip()) + r"(?!\w)", re.I)
             for n in fremdnamen if n.strip()]

    for i, s in enumerate(prs.slides, 1):
        for sh in flach(s):
            if sh.is_placeholder and vorlage.ph_typ(sh) in vorlage.TECHNISCH:
                continue
            for wo, t in texte(sh):
                for muster, was in VERDACHT:
                    if muster.search(t):
                        befunde.append((i, f"{was} ({wo})", t.replace("\n", " ")[:70]))
                        break
                for m in fremd:
                    treffer = m.search(t)
                    if treffer:
                        a = max(0, treffer.start() - 30)
                        befunde.append((i, f"fremder Name '{treffer.group(0)}' ({wo})",
                                        t.replace("\n", " ")[a:a + 70]))
            eng = ueberlauf(sh)
            if eng:
                befunde.append((i, f"Textueberlauf in '{sh.name}'", eng))

        if not vorlage.ist_inhaltsfolie(s):
            continue
        titel = vorlage.rollentext(s, "titel")
        kolumne = vorlage.rollentext(s, "kolumne")
        if not titel:
            befunde.append((i, "Titel leer", ""))
        if not kolumne:
            befunde.append((i, "Kapitelkolumne leer", ""))
        # Zahlen brauchen eine Quelle - Standardtexte wie die Mehrwert-Folie und die
        # Credentials in Kapitel 1 ("seit 1674", Referenzmandate) nicht
        if not kolumne.startswith("1.") and vorlage.zeigt_zahlen(s) \
                and not vorlage.rollentext(s, "quelle"):
            befunde.append((i, "Quellenzeile fehlt, obwohl die Folie Zahlen zeigt", ""))
        # Mehrere Quellen-/Fussnotenzeilen sind fast immer ein Rest aus der Vorlage
        for rolle in ("quelle", "fussnote"):
            treffer = vorlage.finde_rolle(s, rolle)
            if len(treffer) > 1:
                befunde.append((i, f"{ROLLEN_TEXT[rolle]} doppelt ({len(treffer)}x)", ""))
        # Etikett-Regel nur fuer die Inhaltskapitel: in Kapitel 1 sind kurze
        # Standardtitel wie "Ihre Ansprechpartner" richtig und kein Befund.
        if titel and len(titel.split()) <= 3 and kolumne and not kolumne.startswith("1."):
            befunde.append((i, "Titel ist ein Etikett, kein Aussagesatz", titel))

    # Kapitelkolumnen gegen die Agenda und gegeneinander pruefen
    kolumnen = {}
    for i, s in enumerate(prs.slides, 1):
        if vorlage.ist_inhaltsfolie(s):
            t = vorlage.rollentext(s, "kolumne")
            if t:
                kolumnen.setdefault(t, []).append(i)
    je_nummer = {}
    for t, folien in kolumnen.items():
        m = re.match(r"\s*(\d+)\s*\.", t)
        if m:
            je_nummer.setdefault(m.group(1), []).append((t, folien))
    for nummer, varianten in sorted(je_nummer.items()):
        if len(varianten) > 1:
            haupt = max(varianten, key=lambda v: len(v[1]))
            for t, folien in varianten:
                if t == haupt[0]:
                    continue
                for f in folien:
                    befunde.append((f, f"Kapitelkolumne weicht ab (Kapitel {nummer})",
                                    f'"{t}" statt "{haupt[0]}"'))

    def in_agenda(text):
        rumpf = re.sub(r"^\s*\d+\s*\.\s*", "", text).strip().lower()
        return any(rumpf and (rumpf in k.lower() or k.lower() in rumpf) for k in kapitel)

    if kapitel:
        for t, folien in kolumnen.items():
            if not in_agenda(t):
                for f in folien:
                    befunde.append((f, "Kapitelkolumne steht nicht so in der Agenda", t[:70]))
        for i, s in enumerate(prs.slides, 1):
            if vorlage.ist_trenner(s):
                t = vorlage.trenner_titel(s)
                if t and not in_agenda(t):
                    befunde.append((i, "Kapiteltrenner steht nicht so in der Agenda", t[:70]))

    print(f"Template: {vorlage.template(prs)}\n")
    if kolumnen:
        print("Kapitelkolumnen:")
        for t, folien in sorted(kolumnen.items(), key=lambda x: x[1][0]):
            print(f"  F{','.join(map(str, folien)):<16} {t}")
        print()
    if kapitel:
        print("Kapitel laut Agenda:")
        for k in kapitel:
            print(f"  {k}")
        print()

    if not befunde:
        print("Inhaltspruefung ohne Befund.")
        print("Ungeprueft bleiben: Richtigkeit der Zahlen, Aktualitaet der Diagrammdaten,")
        print("Satz und Aussehen der Folien. Diese drei von Hand abnehmen.")
        return 0
    print(f"{len(befunde)} Befund(e):")
    for nr, was, auszug in sorted(befunde):
        print(f"  F{nr:>2}  {was}" + (f'  ->  "{auszug}"' if auszug else ""))
    return 1


# ---------------------------------------------------------------- Vergleich

def vergleich(prs, vorlage_pfad):
    """Stellt die Shapes der bearbeiteten Datei denen der Vorlage gegenueber.

    Shape-IDs allein reichen nicht: PowerPoint vergibt die ID eines geloeschten Shapes neu,
    sodass ein eingeschmuggeltes Textfeld unter einer recycelten ID unsichtbar bliebe.
    Deshalb wird zusaetzlich Name und Typ verglichen - stimmt die ID, aber nicht die
    Signatur, gilt das Shape als ersetzt.
    """
    alt = Presentation(vorlage_pfad)
    zu = weg = ersetzt = 0
    n_alt, n_neu = len(alt.slides), len(prs.slides)

    for i in range(min(n_alt, n_neu)):
        a = {sh.shape_id: signatur(sh) for sh in flach(alt.slides[i])}
        b = {sh.shape_id: signatur(sh) for sh in flach(prs.slides[i])}
        for sid in sorted(set(b) - set(a)):
            name, typ = b[sid]
            marker = "  <- neues Textfeld" if "TEXT_BOX" in typ else ""
            print(f"  F{i+1:>2}  NEU       <{sid}> {name!r}{marker}")
            zu += 1
        for sid in sorted(set(a) - set(b)):
            print(f"  F{i+1:>2}  ENTFERNT  <{sid}> {a[sid][0]!r}")
            weg += 1
        for sid in sorted(set(a) & set(b)):
            if a[sid] != b[sid]:
                print(f"  F{i+1:>2}  ERSETZT   <{sid}> {a[sid][0]!r} -> {b[sid][0]!r} "
                      "(gleiche ID, anderes Shape)")
                ersetzt += 1

    for i in range(n_alt, n_neu):
        shapes = list(flach(prs.slides[i]))
        print(f"  F{i+1:>2}  NEUE FOLIE mit {len(shapes)} Shape(s) - in der Vorlage nicht vorhanden")
        for sh in shapes:
            t = haupttext(sh)
            print(f"        <{sh.shape_id}> {sh.name!r}" + (f'  "{t[:60]}"' if t else ""))
        zu += len(shapes)
    for i in range(n_neu, n_alt):
        print(f"  F{i+1:>2}  FOLIE FEHLT - in der Vorlage vorhanden, in der Datei nicht")
        weg += len(list(flach(alt.slides[i])))

    print(f"\n{zu} Shape(s) hinzugefuegt, {weg} entfernt, {ersetzt} ersetzt.")
    if zu or weg or ersetzt:
        print("Jede Abweichung muss erklaerbar sein. Hinzugefuegte Shapes sollten Duplikate")
        print("eines gleichartigen vorhandenen Elements sein - ein frei gezogenes Textfeld")
        print("erbt weder Schrift noch Position. Entfernte Shapes bewusst entfernt haben.")
        return 1
    print("Keine Abweichung gegenueber der Vorlage.")
    return 0


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("pptx")
    p.add_argument("--slide", type=int, help="eine Folie im Detail")
    p.add_argument("--check", action="store_true", help="Inhaltspruefung")
    p.add_argument("--vergleich", metavar="VORLAGE.pptx", help="Shapes gegen die Vorlage")
    p.add_argument("--fremdnamen", metavar="NAME,NAME",
                   help="Namen frueherer Mandanten, die nicht mehr vorkommen duerfen, z. B. "
                        "'evm,Koblenz,Krefeld' - Pflicht, wenn aus einer fremden Vorlage gebaut wird")
    a = p.parse_args()
    prs = Presentation(a.pptx)

    if a.slide:
        detail(prs, a.slide)
        return
    if not (a.check or a.vergleich):
        uebersicht(prs)
        return

    status = 0
    # Beide Pruefungen laufen, wenn beide angefordert sind - eine darf die andere
    # nicht verdraengen, sonst entsteht genau das falsche Sicherheitsgefuehl.
    if a.check:
        status |= check(prs, (a.fremdnamen or "").split(","))
    if a.vergleich:
        if a.check:
            print("\n--- Vergleich mit der Vorlage ---")
        status |= vergleich(prs, a.vergleich)
    sys.exit(status)


if __name__ == "__main__":
    main()
