"""Gemeinsame Template-Logik fuer inspect_deck.py und fill_deck.py.

Das Haus-Template hat gewechselt (September 2026: blau -> gruen, neue Layouts, neue
Platzhalter-Indizes). Die Rollen einer Folie - Titel, Kapitelkolumne, Subline, Quelle,
Fussnote - werden deshalb NICHT ueber feste Indizes bestimmt, sondern ueber den
Mustertext, den das Layout fuer den Platzhalter vorgibt. Der ist in beiden Templates
eindeutig ("Quelle:", "1)", "Overline" bzw. "Agenda", "Subline").

Warum das wichtig ist: ph:14 war im alten Template die Quellenzeile, im neuen ist es die
Subline direkt unter dem Titel. Wer mit festen Indizes arbeitet, schreibt die Quellen
unter die Ueberschrift.
"""
import re

# Rolle -> Erkennungsmuster fuer den Mustertext des Layout-Platzhalters
ROLLEN_MUSTER = {
    "quelle": re.compile(r"^\s*Quelle", re.I),
    "fussnote": re.compile(r"^\s*1\)"),
    "kolumne": re.compile(r"^\s*(Overline|Agenda)\b", re.I),
    "subline": re.compile(r"Subline", re.I),
    "bereich": re.compile(r"^\s*Untertitel\s*$", re.I),
}
# Rolle -> Textanfang, an dem eine frei platzierte Kopie erkannt wird (die vf von
# DVV fuehrt Quelle und Fussnote als freie Textfelder statt als Platzhalter)
FREI_MUSTER = {
    "quelle": re.compile(r"^\s*Quelle", re.I),
    "fussnote": re.compile(r"^\s*1\)"),
}
KEIN_INHALT = re.compile(
    r"^(\d_)?titel|agenda|section|kapitel|disclaimer|rechtliche|vielen dank", re.I)
TRENNER = re.compile(r"^(section|kapitel)", re.I)
TECHNISCH = ("DATE", "SLIDE_NUMBER", "FOOTER")


def template(prs):
    """'gruen' fuer das Template ab 09/2026, 'blau' fuer das alte, sonst 'unbekannt'."""
    namen = {l.name for m in prs.slide_masters for l in m.slide_layouts}
    if "Nur Titel" in namen:
        return "gruen"
    if any(n.endswith("Inhalt_0") for n in namen):
        return "blau"
    return "unbekannt"


def mustertext(ph):
    try:
        return ph.text_frame.text.strip() if ph.has_text_frame else ""
    except Exception:
        return ""


def ph_typ(ph):
    return str(ph.placeholder_format.type).split()[0]


def rollen_im_layout(layout):
    """{rolle: platzhalter-index} aus den Mustertexten des Layouts."""
    rollen = {}
    for ph in layout.placeholders:
        idx = ph.placeholder_format.idx
        if idx == 0:
            rollen.setdefault("titel", 0)
            continue
        if ph_typ(ph) in ("DATE", "SLIDE_NUMBER"):
            continue
        t = mustertext(ph)
        for rolle, muster in ROLLEN_MUSTER.items():
            if muster.search(t) and rolle not in rollen:
                rollen[rolle] = idx
                break
    return rollen


def ist_inhaltsfolie(slide):
    """Inhaltsfolie = hat einen Titelplatzhalter und ist kein Rahmen-Layout."""
    l = slide.slide_layout
    if KEIN_INHALT.search(l.name):
        return False
    return any(ph.placeholder_format.idx == 0 for ph in l.placeholders)


def ist_trenner(slide):
    return bool(TRENNER.search(slide.slide_layout.name))


def alle_shapes(shapes):
    for sh in shapes:
        yield sh
        if sh.shape_type == 6:  # GROUP
            yield from alle_shapes(sh.shapes)


def finde_rolle(slide, rolle):
    """Alle Shapes, die auf dieser Folie die Rolle ausfuellen.

    Erst der Platzhalter mit dem passenden Index; fehlt er, eine frei platzierte Kopie,
    erkannt am Textanfang. Mehrere Treffer werden zurueckgegeben, nicht verschluckt.
    """
    idx = rollen_im_layout(slide.slide_layout).get(rolle)
    if idx is not None:
        treffer = [sh for sh in alle_shapes(slide.shapes)
                   if sh.is_placeholder and sh.placeholder_format.idx == idx]
        if treffer:
            return treffer
    muster = FREI_MUSTER.get(rolle)
    if muster:
        return [sh for sh in alle_shapes(slide.shapes)
                if not sh.is_placeholder and sh.has_text_frame
                and muster.search(sh.text_frame.text)]
    return []


def rollentext(slide, rolle):
    return " ".join(sh.text_frame.text.strip() for sh in finde_rolle(slide, rolle)
                    if sh.has_text_frame).strip()


def trenner_titel(slide):
    """Kapiteltitel eines Trenners - alt ph:11, neu ph:0."""
    for sh in slide.shapes:
        if not sh.is_placeholder or not sh.has_text_frame:
            continue
        idx = sh.placeholder_format.idx
        t = sh.text_frame.text.strip()
        if t and (idx == 11 or (idx == 0 and slide.slide_layout.name.lower().startswith("kapitel"))):
            return t
    return ""


def ueberlauf(shape, text=None):
    """Grobe, zeilenbewusste Schaetzung, ob Text die Box sprengt. Ersetzt keine Sichtpruefung.

    Beruecksichtigt harte Zeilenumbrueche: drei kurze Zeilen in einer KPI-Kachel sind
    etwas anderes als ein langer Fliesstext mit gleicher Zeichenzahl.
    """
    import math
    if not getattr(shape, "has_text_frame", False) or shape.width is None or shape.height is None:
        return None
    t = (text if text is not None else shape.text_frame.text).strip()
    if not t:
        return None
    b, h = shape.width / 360000, shape.height / 360000
    if b <= 0 or h <= 0:
        return None
    pt = 9.0
    for para in shape.text_frame.paragraphs:
        for r in para.runs:
            if r.font.size:
                pt = r.font.size.pt
            break
        break
    pro_zeile = max(1, int(b / (pt * 0.0352778 * 0.5)))
    verfuegbar = max(1, int(h / (pt * 0.0352778 * 1.2)))
    noetig = sum(max(1, math.ceil(len(z) / pro_zeile))
                 for z in t.replace("\x0b", "\n").split("\n"))
    if noetig > verfuegbar + 1 and noetig > verfuegbar * 1.3:
        return (f"braucht ~{noetig} Zeilen, Box fasst ~{verfuegbar} "
                f"({len(t)} Zeichen bei {pt:.0f} pt)")
    return None


ZAHL = re.compile(r"\d")


def zeigt_zahlen(slide):
    """True, wenn die Folie ausserhalb von Kolumne und Technik Zahlen traegt."""
    # Ueber die Shape-ID vergleichen: python-pptx erzeugt bei jedem Durchlauf neue
    # Proxy-Objekte, id() waere also nie gleich.
    kolumne = {sh.shape_id for sh in finde_rolle(slide, "kolumne")}
    for sh in alle_shapes(slide.shapes):
        if sh.shape_id in kolumne:
            continue
        if sh.is_placeholder and ph_typ(sh) in TECHNISCH:
            continue
        if getattr(sh, "has_table", False) and sh.has_table:
            return True
        if getattr(sh, "has_chart", False) and sh.has_chart:
            return True
        if sh.has_text_frame and ZAHL.search(sh.text_frame.text):
            if any(m.search(sh.text_frame.text) for m in FREI_MUSTER.values()):
                continue  # Quellen- und Fussnotenzeilen selbst zaehlen nicht
            return True
    return False
