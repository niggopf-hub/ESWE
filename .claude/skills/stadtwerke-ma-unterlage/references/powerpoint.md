# PowerPoint — wie in dieser Vorlage gearbeitet wird

## Die Grundregel

**Die letzte vergleichbare Unterlage wird kopiert, und der neue Text wird in die vorhandenen
Boxen geschrieben. Es werden keine neuen Textfelder eingefügt.**

Der Grund ist nicht Ästhetik. Eine Folie dieser Vorlage besteht aus Platzhaltern, die ihre
Schrift, Größe, Farbe, Position, Aufzählungszeichen und Zeilenabstände vom Layout und vom
Master erben. Ein frei eingefügtes Textfeld erbt nichts davon: Es steht in der
Standardschrift statt in der Hausschrift, an einer um Millimeter abweichenden Position, mit
anderem Zeilenabstand — und beim nächsten Bearbeiten fällt genau das auf. Eine Folie aus
lauter frei platzierten Kästchen lässt sich außerdem nicht mehr sauber weiterverwenden: der
nächste Bearbeiter muss raten, was Inhalt und was Dekoration ist.

Es kommt hinzu, dass die Diagramme keine PowerPoint-Diagramme sind (siehe unten). Wer eine
Folie neu aufbaut, statt sie zu befüllen, verliert sie.

**Konkret heißt das:**

| Statt … | … so |
|---|---|
| neues Textfeld für den Titel einfügen | Text in den Titel-Platzhalter schreiben |
| Quellenangabe unten hinschreiben | in den Quellen-Platzhalter schreiben |
| Fußnote als kleines Textfeld ergänzen | in den Fußnoten-Platzhalter schreiben |
| Folie löschen und neu bauen | vorhandene Folie duplizieren und umschreiben |
| Kachel neu zeichnen | vorhandene Kachelgruppe kopieren und Werte ersetzen |

Neue Shapes sind genau dann gerechtfertigt, wenn ein Schaubild tatsächlich mehr Elemente
braucht als das Vorbild — etwa eine Beteiligungsstruktur mit mehr Gesellschaften. Dann wird
ein **vorhandenes Element derselben Art dupliziert**, nicht ein leeres Textfeld gezogen.
Das Duplikat erbt Formatierung, Größe und Ausrichtung.

---

## Aufbau der Vorlage

**Seit September 2026 gilt das neue Haus-Design.** Referenzdatei ist
`20260907_Metzler_DVV_vf.pptx` — neue Unterlagen werden aus ihr abgeleitet, nicht mehr aus
dem blauen Altbestand. Woran man die beiden Templates auseinanderhält und was sich geändert
hat:

| | **Neu (Standard ab 09/2026)** | Alt (bis 08/2026) |
|---|---|---|
| Theme-Name | `Metzler` | `Vorlage_BMSSC` |
| Primärfarbe | **`#44501A`** (Olivgrün) | `#003D7C` (Dunkelblau) |
| Akzente | `#8FB1A4` Salbei · `#A6ABCF` Flieder · `#B2B1A7` Taupe · `#DFB36C` Ocker · `#B0BE94` Hellgrün | Blautöne `#3157E3` … `#A5CAFB`, Signal `#FF9900` |
| Helle Flächen | `#D1E0D7`, `#BEDFB6` | `#D1E4FD` |
| Schrift Überschriften | **Ninna Book** | Univers for Metzler Light |
| Schrift Fließtext | **Cadiz** | Univers for Metzler Light |
| Logo | grüne Handschrift-Signatur „Metzler" mit Kreismarke, als **SVG** in den Layouts (PNG-Fallback) | blaue Serifen-Wortmarke „METZLER Corporate Finance", PNG im Master |
| Inhaltslayout | **`Nur Titel`** (plus `Zwei Inhalte`, `Drei Inhalte`, `Infografik`, `Inhalt mit Bild` …) | `Inhalt_0` und Varianten |
| Titelfolie | `Titel 1` (auch `Titel 2`, `Titel 3` mit Bild) | `Titel` |
| Agenda | `Agenda 2` — Agenda als **Tabelle** mit Nummer, Kapitel, Seitenzahl | `2_Agenda` |
| Kapiteltrenner | `Kapitel 2` (auch `Kapitel 1`, `Kapitel 3` mit Bild) | `Section` |
| Schlussfolie | `Rechtliche Hinweise`, optional `Vielen Dank` | `Disclaimer_deutsch` |
| Datum / Foliennummer | als Platzhalter unten rechts auf jeder Inhaltsfolie | nicht vorhanden |

Welches Template eine Datei hat, zeigt `inspect_deck.py` in der ersten Zeile an
(`Template: gruen` / `blau`).

**Foliengröße** unverändert: A4 quer, 29,7 × 21 cm.

**Schriften nicht ersetzen.** Ninna Book und Cadiz sind Hausschriften und auf fremden
Rechnern oft nicht installiert. Solange Text in den Platzhaltern steht, sieht die Datei beim
Empfänger trotzdem richtig aus; ein frei eingefügtes Textfeld mit Ersatzschrift fällt sofort
auf — ein Grund mehr für die Grundregel.

**Farben.** Kennzahlwerte, Kernaussagen-Kästen und Akzentlinien stehen in der Primärfarbe
`#44501A`. Diagrammreihen folgen der Akzentreihenfolge des Themes. Wer eine Folie aus einer
blauen Altunterlage übernimmt, muss alle **hart gesetzten** Blautöne (`#003D7C` und die
hellen Blauflächen) von Hand auf das neue Theme umstellen — Theme-Farben stellen sich beim
Einfügen in das neue Template selbst um, fest eingetragene RGB-Werte nicht.

**Altbestand.** Unterlagen im blauen Template werden nicht nachträglich umgestellt, sondern
beim nächsten Fall neu aus der grünen Referenz aufgebaut. Blaue Folien in eine grüne Datei zu
kopieren, erzeugt Mischlayouts mit zwei Mastern — das ist der schnellste Weg zu einer
uneinheitlichen Unterlage.

---

## Die Platzhalter einer Inhaltsfolie

Das ist die Landkarte, nach der befüllt wird. **Die Indizes unterscheiden sich zwischen den
Templates — deshalb über Rollen adressieren, nicht über Indizes.**

| Rolle | Inhalt | Neu (`Nur Titel`) | Alt (`Inhalt_0`) |
|---|---|---|---|
| `rolle:kolumne` | „2. ‹Kapitelname›" — wortgleich zu Agenda und Trenner | ph:13, **über** dem Titel („Overline") | ph:13 |
| `rolle:titel` | Aussagesatz, ein bis zwei Zeilen | ph:0 | ph:0 |
| `rolle:subline` | optionale Unterzeile direkt unter dem Titel | **ph:14** | — |
| `rolle:bereich` | Bereichsüberschrift | — (im Inhalt selbst) | ph:12 |
| `rolle:fussnote` | „1) …; 2) …" | **ph:11** (y ≈ 19,4 cm) | ph:15 |
| `rolle:quelle` | „Quellen: …" | **ph:20** (y ≈ 20,0 cm, links) | **ph:14** |

**Die Falle: `ph:14`.** Im alten Template ist es die Quellenzeile, im neuen die Subline direkt
unter dem Titel. Wer mit einer alten Zuordnung befüllt, schreibt die Quellen unter die
Überschrift — und weil die Subline ein gültiger Platzhalter ist, meldet kein Werkzeug einen
Fehler. `fill_deck.py` löst `rolle:` deshalb über den **Mustertext** des Layouts auf
(„Quelle:", „1)", „Overline", „Subline") statt über den Index; das funktioniert in beiden
Templates.

**Quelle und Fußnote als freie Textfelder.** In der DVV-vf stehen Quelle und Fußnoten nicht
im Platzhalter, sondern in frei platzierten Textfeldern an derselben Position (Namen wie
„Content Placeholder 16" oder „Fußzeilenplatzhalter 10", obwohl es keine Platzhalter mehr
sind). Die Skripte erkennen diese Kopien am Textanfang („Quelle", „1)") und behandeln sie
als die Rolle. Fehlt beides auf einer Folie, wird die Box von einer Nachbarfolie desselben
Layouts kopiert — nicht neu gezogen.

**Datum und Foliennummer** (ph:2, ph:18) füllt PowerPoint selbst; nicht überschreiben. Das
Datum muss zum Datum auf der Titelfolie passen.

Auf dem **Kapiteltrenner** trägt im neuen Template ph:0 den Kapiteltitel und ph:10 die
Nummer; im alten ph:11 den Titel und ph:10 die Nummer.

**Die Rollen, die regelmäßig vergessen werden, sind Kolumne, Quelle und Fußnote.** Sie sind
klein, fallen beim Arbeiten nicht auf — und sind genau die Stellen, an denen der Name des
vorherigen Mandanten stehen bleibt. In einer ausgelieferten Unterlage stand auf einer Folie
des Kapitels 2 noch die Kapitelkolumne eines völlig anderen Stadtwerks. Deshalb: **nach dem
Befüllen jede Folie einzeln prüfen** und `inspect_deck.py --check --fremdnamen` laufen lassen.

---

## Diagramme: think-cell

Die Säulen-, Ring- und Wasserfalldiagramme sind **think-cell-Objekte**, keine
PowerPoint-Diagramme. Erkennbar an einem eingebetteten OLE-Objekt namens
`think-cell data - do not delete`, das auf jeder Folie mit Diagrammen liegt.

**Konsequenzen für die Arbeit:**

- Diagramme **nicht** programmatisch ersetzen oder neu erzeugen. Ein mit python-pptx
  eingefügtes Diagramm hat weder die Formatierung noch die Beschriftungslogik, und das
  think-cell-Datenobjekt wird inkonsistent.
- Zahlen werden **in think-cell in PowerPoint** aktualisiert: Diagramm anklicken, Datenblatt
  öffnen, Werte ersetzen. Beschriftungen, Differenzpfeile und die Faktoren über den Säulen
  ziehen automatisch nach.
- Das OLE-Objekt niemals löschen, auch nicht wenn es unbenutzt aussieht.
- Wenn eine Folie mit Diagramm für einen neuen Fall gebraucht wird: **Folie duplizieren**,
  nicht neu aufbauen.

Der praktikable Weg, der die Trennung sauber hält: Der Skill liefert die **Datenreihen** aus
dem Modell (Jahre, Werte, Faktoren) in einer klar beschrifteten Tabelle, und diese Werte
werden in think-cell eingetragen. Textteile der Folie werden programmatisch befüllt,
Diagrammdaten von Hand.

### Übergabeliste für die Diagramme

Der gefährlichste Zustand einer Unterlage ist ein **unversehrtes Diagramm mit alten Daten**.
Es sieht richtig aus, jede Skriptprüfung meldet grün, und es zeigt die Zahlen des
Vorgängerfalls. Weder `--check` noch `--vergleich` können das finden: Sie sehen, dass das
think-cell-Objekt da ist, nicht was drinsteht.

Deshalb bekommt jedes Diagramm eine Zeile in einer Übergabeliste, die mit der Datei
weitergereicht wird:

| Folie | Diagramm | Datenreihe aus dem Modell | Werte eingetragen | Gegengelesen |
|---|---|---|---|---|
| 15 | Net Debt + Faktoren | `Overview FS`, Verschuldungsblock | ☐ | ☐ |
| 16 | Umsatz / Rohertrag | `Overview FS`, Ertragslage | ☐ | ☐ |
| 16 | Cashflows | `Overview FS`, Finanzlage | ☐ | ☐ |
| 16 | Kassenbestand / Net Debt | `Overview FS`, Vermögenslage | ☐ | ☐ |
| 13 | Umsatzring | `Overview FS`, Umsatzaufteilung | ☐ | ☐ |

„Gegengelesen" heißt: Jemand hat den Wert im Diagramm mit dem Wert im Modell verglichen —
nicht, dass das Diagramm existiert. Solange eine Zeile offen ist, ist die Unterlage nicht
fertig. Das gilt auch für Diagramme auf Folien, die inhaltlich unverändert übernommen
wurden: Wenn sich der Fall geändert hat, haben sich ihre Daten geändert.

---

## Wiederkehrende Bauteile

**KPI-Kachel.** Eine Gruppe aus zwei Textfeldern: oben der Wert (9 pt, Primärfarbe `#44501A`), darunter
die Bezeichnung mit Jahr (9 pt, schwarz). Der Vorjahreswert steht als eigene kleine Zeile
darunter. Für eine neue Kachel eine bestehende Gruppe kopieren.

**Ring mit Summenbezug.** think-cell-Ring plus ein Textelement `100% ≙ ‹Summe› Mio. EUR`.
Die Legende steht als eigene Textelemente außen, nicht als Diagrammlegende.

**Strukturschaubild.** Rechteck je Gesellschaft, Verbindungslinien, Prozentwerte als eigene
kleine Textfelder an den Kanten, Farbkodierung nach Geschäftsbereich. Für eine zusätzliche
Gesellschaft ein vorhandenes Rechteck samt Linie duplizieren und die Kante neu verbinden.
Bei Beteiligungen mit Kennzahlen: dreizeiliger Kasten (Tätigkeit / Umsatz Jahr /
Ergebnis Jahr).

**Kommentarkasten mit Nummernbezug.** Auf der Financial-Folie verweisen nummerierte Kreise
in der Tabelle auf die Kommentare daneben. Beim Befüllen prüfen, ob Nummern und Kommentare
noch zusammenpassen — sie verrutschen, wenn Zeilen wegfallen.

**Kernaussagen-Kasten.** Ein farbig hinterlegtes Rechteck mit einem Dreieck als Anker, das
den Kernsatz der Folie trägt. Steht auf den Argumentationsfolien (2.1, 2.4, 3.x) und ist
inhaltlich die wichtigste Box der Folie — nicht als Dekoration behandeln.

---

## Skripte

Zwei kleine Werkzeuge im Ordner `scripts/`. Sie ersetzen kein PowerPoint, sondern nehmen
die stumpfe Arbeit ab und verhindern, dass beim Befüllen neue Boxen entstehen.

**`inspect_deck.py`** — listet Folien, Layouts, Platzhalter mit Index, Textboxen mit Namen,
Tabellen und Diagramme. Damit findest du die Box, in die geschrieben werden soll, und siehst
sofort, welche Platzhalter noch leer sind.

```bash
python3 scripts/inspect_deck.py unterlage.pptx                 # Übersicht
python3 scripts/inspect_deck.py unterlage.pptx --slide 12      # eine Folie im Detail
python3 scripts/inspect_deck.py unterlage.pptx --check         # Prüfmodus
python3 scripts/inspect_deck.py neu.pptx --vergleich alt.pptx  # gegen die Vorlage
python3 scripts/inspect_deck.py neu.pptx --check --fremdnamen "evm,Koblenz,DVV"
```

**Fremdnamen sind Pflicht, sobald aus einer Unterlage eines anderen Mandanten gebaut wird.**
Die Agendaprüfung allein reicht nicht: In der DVV-v1 stand sogar in der Agenda noch
„evm AG – Übersicht und Herausforderungen", sodass die Kolumne „2. evm AG" formal
agendakonform war. Mit `--fremdnamen "evm,Koblenz,Mittelrhein,enm"` fand der Prüfer dort 37
Stellen auf neun Folien. Die Liste enthält den Vorgängermandanten, seine Stadt, seine
Tochtergesellschaften und seine auffälligsten Zahlen (etwa „600 Mio.").

Der **Vergleichsmodus** ist der Wächter über die Grundregel: Er stellt die Shapes der
bearbeiteten Datei denen der Vorlage gegenüber und meldet jede Zugabe, Entfernung und
Ersetzung einzeln. Er verlässt sich dabei nicht auf die Shape-ID allein — PowerPoint vergibt
die ID eines gelöschten Shapes neu, sodass ein eingeschmuggeltes Textfeld unter recycelter ID
sonst unsichtbar bliebe. Zusätzliche und fehlende Folien werden ebenfalls gemeldet, und der
Inhalt zusätzlicher Folien wird ausgegeben.

**Beide Prüfungen zusammen laufen lassen.** `--check` und `--vergleich` prüfen Verschiedenes
und verdrängen einander nicht:

```bash
python3 scripts/inspect_deck.py neu.pptx --check --vergleich vorlage.pptx
```

Rückgabestatus 0 heißt: keine Abweichung und kein Inhaltsbefund. Jede gemeldete Abweichung
muss erklärbar sein — auch Entfernungen, denn ein versehentlich gelöschtes Element fällt
sonst niemandem auf.

**Was der Prüfer nicht kann.** Er prüft Text, Tabellenzellen, Platzhalter, Kapitelkolumnen
gegen die Agenda und eine grobe Überlaufschätzung. Er prüft **nicht**, ob die Zahlen stimmen,
ob die Diagramme aktuelle Daten zeigen und wie die Folien aussehen. Ein grüner Status
bescheinigt ausschließlich das Geprüfte — die drei genannten Punkte werden von Hand
abgenommen (siehe Übergabeliste oben und Schritt 7 der SKILL.md).

Der Prüfmodus meldet genau die Fehler aus der Prüfliste: leere Pflicht-Platzhalter
(Quellenzeile, Kapitelkolumne), Textreste mit verdächtigen Mustern (`WIP`, `TODO`, `http`,
`n.a.` in Titeln) und Folien ohne Aussagentitel.

**`fill_deck.py`** — schreibt Text in **vorhandene** Boxen, adressiert über Folie plus
Platzhalter-Index oder Shape-Name. Legt bewusst keine neuen Shapes an und bricht mit einer
Fehlermeldung ab, wenn das Ziel nicht existiert — damit ein Tippfehler nicht stillschweigend
eine neue Box erzeugt.

```bash
python3 scripts/fill_deck.py unterlage.pptx --map befuellung.json --out unterlage_v2.pptx
```

Format der Zuordnungsdatei:

```json
{
  "12": {
    "ph:0":  "Starke Marktposition mit umfangreichem Investitionsprogramm …",
    "ph:13": "2. ‹Gesellschaft› – Übersicht und Herausforderungen",
    "ph:14": "Quellen: eigene Recherche, Jahresabschluss ‹Gesellschaft› ‹Jahr›",
    "ph:15": "1) Net Debt = …"
  },
  "13": {
    "name:Text Box 29": "999 Mio. EUR"
  }
}
```

Adressierung:

| Form | Ziel |
|---|---|
| `rolle:quelle` | **empfohlen** — die Box dieser Rolle, in beiden Templates richtig (Rollen: `titel`, `kolumne`, `subline`, `quelle`, `fussnote`, `bereich`) |
| `ph:13` | Platzhalter mit diesem Index — nur wenn das Template feststeht |
| `name:Text Box 29` | Shape mit exakt diesem Namen — **muss eindeutig sein** |
| `name:One Pager!r4c2` | Zelle Zeile 4, Spalte 2 der Tabelle „One Pager" (1-basiert) |
| `ph:5!r3c2` | dieselbe Zellenadressierung für eine Tabelle in einem Platzhalter |

Die Zellenadressierung ist nicht optional: One Pager und Financial-Tabelle stehen in
Tabellen, nicht in Textrahmen. Die vollständigen Shape-Namen liefert
`inspect_deck.py --slide N` — ungekürzt, denn sie sind die Zieladresse.

Mehrzeilige Inhalte als Liste von Zeilen übergeben; die Absatzformatierung bleibt erhalten.

**Was das Skript beim Ersetzen wegwirft — und meldet.** Beim Überschreiben eines Absatzes
bleiben sonst Reste des alten Inhalts stehen, die im Textfeld unsichtbar sind: Hyperlinks auf
den alten Mandanten, Felder (Foliennummer, Datum, eingefügte Werte), weiche Zeilenumbrüche.
Das Skript entfernt sie ausdrücklich und schreibt in die Hinweise, was es entfernt hat. Bei
gemischt formatierten Absätzen übernimmt der neue Text die Formatierung des ersten Runs und
meldet das — wenn Teile anders aussehen sollen, ist das von Hand nachzuarbeiten.

Zwei Sicherungen, die das Skript fail-closed machen: Ein **mehrdeutiger Shape-Name** bricht
mit Fehler ab, statt das erste Vorkommen zu treffen; und **Quell- und Zieldatei dürfen nicht
identisch sein**, damit die Vorlage nicht überschrieben wird.

---

## Ablauf beim Bauen

1. **Die grüne Referenz** (`20260907_Metzler_DVV_vf.pptx`) kopieren und nach Schema
   umbenennen: `JJJJMMTT_<Haus>_<Unternehmen>_<Version>.pptx`. Nicht aus einer blauen
   Altunterlage bauen.
2. `inspect_deck.py` laufen lassen und die Folienliste gegen die Landkarte in der SKILL.md
   halten. Folien, die dieser Fall nicht braucht, löschen; fehlende durch **Duplizieren**
   einer verwandten Folie ergänzen.
3. Kapitelkolumnen (Index 13), Agenda und Trennerfolien auf die neuen Kapitelnamen setzen —
   zuerst, weil sie überall gleich lauten müssen.
4. Kapitel 2 befüllen, dann 3, dann 1 (Kapitel 1 ist meist reine Übernahme).
5. Diagrammdaten in think-cell eintragen.
6. `inspect_deck.py --check --vergleich <vorlage.pptx> --fremdnamen "<alter Mandant>,…"`
   laufen lassen und jede Abweichung erklären.
7. Übergabeliste der Diagramme abarbeiten: jede Datenreihe eingetragen und gegengelesen.
8. Jede Folie einmal ansehen: fremde Namen, WIP-Reste, leere Platzhalter, Umbrüche,
   Überlauf, Nummernbezüge in Kommentaren.

**Voraussetzungen.** Beide Skripte brauchen Python 3 und `python-pptx`
(`pip install python-pptx`); weitere Abhängigkeiten gibt es nicht. Die Ausgabe ist auf
ASCII beschränkt und stellt die Konsole auf UTF-8 um, damit sie auch unter Windows ohne
Zeichenkodierungsfehler läuft.
