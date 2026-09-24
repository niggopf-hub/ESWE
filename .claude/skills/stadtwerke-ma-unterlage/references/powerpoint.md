# PowerPoint: wie in der grünen Vorlage gearbeitet wird

## Die Grundregel

**Die grüne Referenzunterlage `20260907_Metzler DVV_vf.pptx` wird kopiert, und der neue
Text wird in die vorhandenen Boxen geschrieben. Es werden keine neuen Textfelder gezogen.**

Eine Folie dieser Vorlage besteht aus Platzhaltern und Shapes, die Schrift, Größe, Farbe,
Position und Zeilenabstand vom Master erben. Ein frei eingefügtes Textfeld erbt nichts davon:
andere Schrift, verschobene Position, und beim nächsten Bearbeiten fällt genau das auf.
Dazu kommt, dass die Diagramme think-cell-Objekte sind; wer eine Folie neu aufbaut statt sie
zu befüllen, verliert sie.

Zwei Ausnahmen, beide mit eigenem Skript:
- **Gelbe TBD-Kästen** (`tbd_box.py`): bewusst neue Shapes, heißen `TBD-‹Nr›`, werden vom
  Vergleich als solche erkannt und am Ende entfernt.
- **Spalten der Investitionstabelle** (`dup_shapes.py`): Kopien vorhandener Shapes, weil die
  Spaltenzahl vom Fall abhängt.

| Statt … | … so |
|---|---|
| neues Textfeld für den Titel | Text in `rolle:titel` |
| Quellenangabe unten hinschreiben | Text in `rolle:quelle` |
| Folie löschen und neu bauen | vorhandene Folie duplizieren und umschreiben |
| Kachel neu zeichnen | vorhandene Kachel per `id:` befüllen |
| vierte Spalte zeichnen | dritte Spalte mit `dup_shapes.py --dup` kopieren, dann `--columns` |

---

## Die Vorlage

Seit September 2026 gilt das grüne Haus-Design. Woran man es erkennt und was sich gegenüber
dem blauen Altbestand geändert hat:

| | Grün (Standard) | Blau (bis 08/2026) |
|---|---|---|
| Theme | `Metzler` | `Vorlage_BMSSC` |
| Primärfarbe | `#44501A` Olivgrün | `#003D7C` Dunkelblau |
| Akzente | `#8FB1A4` Salbei, `#A6ABCF` Flieder, `#B2B1A7` Taupe, `#DFB36C` Ocker, `#B0BE94` Hellgrün | Blautöne, Signal `#FF9900` |
| Schriften | Ninna Book (Titel), Cadiz (Text) | Univers for Metzler |
| Logo | Handschrift-Signatur „Metzler" als SVG | Wortmarke „METZLER Corporate Finance" |
| Inhaltslayout | `Nur Titel` | `Inhalt_0` |
| Agenda | `Agenda 2`, Tabelle mit Nummer, Kapitel, Seite | `2_Agenda` |
| Trenner | `Kapitel 2` | `Section` |
| Schluss | `Rechtliche Hinweise` | `Disclaimer_deutsch` |
| Datum, Foliennummer | Platzhalter auf jeder Inhaltsfolie | keine |

`inspect_deck.py` zeigt in der ersten Zeile `Template: gruen` oder `blau`. Blaue Folien
werden nicht in eine grüne Datei kopiert (zwei Master, hart gesetzte Blautöne); Inhalte aus
blauen Unterlagen werden im grünen Template neu aufgebaut. Für Kapitel 3 gibt es dafür
`assets/kapitel3_gruen.pptx` (siehe unten).

Foliengröße A4 quer, 29,7 × 21 cm. Schriften nicht ersetzen.

---

## Rollen und Adressen

Über Rollen adressieren, nicht über Indizes, weil `ph:14` im blauen Template die
Quellenzeile war und im grünen die Subline ist. `fill_deck.py` löst `rolle:` über den
Mustertext des Layouts auf.

| Rolle | Inhalt | Grün |
|---|---|---|
| `rolle:kolumne` | „2. ‹X› – Übersicht und Herausforderungen", wortgleich zu Agenda und Trenner | ph:13, über dem Titel |
| `rolle:titel` | Aussagesatz | ph:0 |
| `rolle:subline` | optional | ph:14 |
| `rolle:fussnote` | „1) …; 2) …" | ph:11, in der DVV-vf als freies Textfeld „Fußzeilenplatzhalter 10" |
| `rolle:quelle` | „Quellen: …" | ph:20, in der DVV-vf als freies Textfeld „Content Placeholder 16" |

Die Skripte erkennen die freien Kopien am Textanfang („Quelle", „1)"). Fehlt beides auf
einer Folie, wird die Box von einer Nachbarfolie kopiert, nicht neu gezogen.

**Shape-Namen sind in der grünen Vorlage nicht eindeutig.** Alle zehn Kacheln heißen
„Text Box 29", alle Kästchen der Beteiligungsstruktur „Shape 13", die Faktoren „Rechteck
55". Deshalb zeigt `inspect_deck.py --slide N` vor jedem Shape die Shape-ID, und
`fill_deck.py` nimmt `id:‹Nr›` als Adresse. Ein mehrdeutiger `name:` bricht ab.

### Landkarte der DVV-vf, Kapitel 2

Was auf welcher Folie wo steht, mit den Adressen aus der Vorlage. Nach dem Kopieren mit
`inspect_deck.py --slide` prüfen, die IDs bleiben beim Kopieren erhalten.

| Folie | Element | Adresse | Wer füllt |
|---|---|---|---|
| 12 Ausgangslage | Titel, Kolumne | `rolle:titel`, `rolle:kolumne` | Skript |
| | Kasten „Ausgangslage" | `name:Rectangle 8` | bleibt |
| | Kernsatz | `name:Rectangle 26` | Skript |
| | Bullets | `name:Textfeld 37` (Liste von Zeilen) | Skript |
| | Quellen | `rolle:quelle` | Skript |
| 13 Beteiligungsstruktur | Gesellschafter, Quoten, Kästchen | `id:` je Shape 13 | Skript, Struktur von Hand angepasst |
| | Logos | Picture-Shapes | gelb `LOGO` |
| | Fußnote, Quellen | `rolle:fussnote`, `rolle:quelle` | Skript |
| 14 Kunden und Netz | zehn Kacheln | `id:` je Text Box 29, drei Zeilen: Bezeichnung, Wert, Vorjahr | Skript aus Block `Kacheln` |
| | Erlösquellen-Kästen | `id:` je Rechteck 20 | Skript |
| | Legende Geschäftsfelder | `id:` je Text Box 29 | Skript |
| | „100 % ≙ ‹Summe›" | `name:Rectangle 41` | Skript |
| | Umsatzring | `name:Chart 57` | gelb `TC`, Block `Umsatzring` |
| | Icons | Graphic 36 bis 52 | gelb `LOGO`, wenn unpassend |
| 15 Financials | Blocküberschriften | `name:Rectangle 9`, `10`, `11` | bleibt |
| | Kommentar | `name:Rectangle 12` (Liste, erste Zeile „Kommentar:") | Skript |
| | Rohertrag-Marge, EBITDA-Marge | `id:` je Oval in `Group 96` | Skript aus Block `GuV-Chart` |
| | EK-Quote | `id:` je Oval 13 bis 16 und 85 | Skript aus Block `Bilanz-Chart` |
| | Kernsatz-Kasten | **fehlt in der DVV-vf**; Kasten und Pfeil von Folie 16 (`TextBox 87`, `Arrow: Right 86`) mit `dup_shapes.py` kopieren, unter den Kommentar setzen | Skript |
| | drei Charts | `Chart 120`, `Chart 121`, `Chart 75` | gelb `TC` |
| | Beschriftungen „Textplatzhalter 2" | think-cell-Labels | **nicht anfassen** |
| 16 Verschuldung und Invest | Segmentnamen | `id:` je Text Box 29 in der Zeile Investitionsschwerpunkt | Skript |
| | CapEx je Segment | `id:` je Rectangle 125 bis 127 | Skript |
| | Projekte | `id:` je Textfeld 55 | Skript |
| | Gesamtsumme, Horizont | `name:TextBox 132`, Text Box 29 in `Group 130` | Skript |
| | Faktoren | `id:` je Rechteck 55 | Skript aus Block `Verschuldung` |
| | Kernsatz | `name:TextBox 87` | Skript |
| | Net-Debt-Chart | `Chart 148` | gelb `TC` |
| | Icons je Segment | `Group 110`, `115`, `120` | gelb `LOGO`, wenn unpassend |
| | Fußnote, Quellen | `rolle:fussnote`, `rolle:quelle` | Skript |
| 17 Diskussionspunkte | fünf Thesen | `id:` je Rechteck 81 in Group 9 bis 21 | Skript (kurze Ausbaustufe) |
| 18 Mehrwert | sechs Punkte | Textfeld 30 | bleibt |

Die Beschriftungen an den Charts („2,619", „(24)", die Jahreszahlen) sind Shapes mit dem
Namen „Textplatzhalter 2". Sie gehören think-cell und werden beim Aktualisieren neu
gesetzt. Nicht per Skript beschreiben.

---

## Diagramme: think-cell

Die Säulen-, Ring- und Wasserfalldiagramme sind think-cell-Objekte. Erkennbar am
OLE-Objekt `think-cell data - do not delete` auf jeder Folie mit Diagrammen. Das Objekt nie
löschen, Diagramme nie programmatisch ersetzen, Folien mit Diagrammen duplizieren statt neu
bauen.

Die Arbeitsteilung: Das Excel liefert je Diagramm einen Block auf `Overview FS` ab Spalte J,
markierfertig mit Kopfzeile. Der Kollege öffnet think-cell, markiert den Block, fügt ihn
ein. Bis dahin liegt auf jedem Diagramm ein gelber Kasten `TC` mit dem Blocknamen. Ein
unversehrtes Diagramm mit alten Daten ist der gefährlichste Zustand einer Unterlage, weil
jede Skriptprüfung grün meldet; der Kasten verhindert, dass er unbemerkt bleibt.

Was nicht think-cell ist und deshalb fertig gebaut wird: die Kreise mit Margen und EK-Quote,
die Faktoren über dem Net-Debt-Chart, die Kacheln, die Segmenttabelle, alle Kästen.

---

## Gelbe TBD-Kästen

```bash
python3 scripts/tbd_box.py deck.pptx --add tbd.json --out deck_v2.pptx
python3 scripts/tbd_box.py deck_v2.pptx --list
python3 scripts/tbd_box.py deck_final.pptx --remove --out deck_clean.pptx
```

Befehlsdatei: je Kasten Folie, Sorte (`TC`, `LOGO`, `PRUEFEN`), Text, und entweder
`"ueber": "name:Chart 120"` (der Kasten legt sich auf das Objekt) oder eine Position in cm.
Die Nummern laufen fortlaufend und stehen wortgleich in der TBD-Liste des Reports. Standard
für eine Unterlage:

| Nr | Folie | Sorte | Text |
|---|---|---|---|
| 1 | 4 | PRUEFEN | Aktualität der Referenzprojekte |
| 2 | 8 | PRUEFEN | Aktualität der Mandate |
| 3 | 13 | LOGO | Logos je Gesellschaft ersetzen |
| 4 | 14 | TC | Excel-Block Umsatzring |
| 5 | 14 | LOGO | Icon ‹Geschäftsfeld› passt nicht (nur wenn nötig) |
| 6 | 15 | TC | Excel-Block GuV-Chart |
| 7 | 15 | TC | Excel-Block Cashflow-Chart |
| 8 | 15 | TC | Excel-Block Bilanz-Chart |
| 9 | 16 | TC | Excel-Block Verschuldung |
| 10 | 16 | LOGO | Icon Segment ‹X› fehlt in der Vorlage (nur wenn nötig) |
| 11 | 18 | PRUEFEN | zwei fallspezifische Ziele bestätigen |
| 12 | 19 | PRUEFEN | Assetauswahl und Beispielstruktur |

`inspect_deck.py --vergleich` zählt die Kästen getrennt und meldet sie nicht als fremde
Textfelder; `--check` überspringt sie. `stil_check.py` liest sie nicht.

---

## Die Investitionstabelle

Die Spaltenzahl hängt vom Fall ab. Vorgehen für vier Spalten aus der Vorlage mit dreien:

```bash
# 1. dritte Spalte kopieren (Segmentname, Icon-Gruppe, CapEx-Kasten, Projekte, Trennpfeil)
python3 scripts/dup_shapes.py deck.pptx --slide 16 \
        --dup "id:100,id:121,id:128,id:138,id:102" --dx 8.4 --out deck_a.pptx
# 2. alle vier Spalten gleichmäßig auf den Bereich verteilen (linker Rand 3,6 cm, Breite 25,1 cm)
python3 scripts/dup_shapes.py deck_a.pptx --slide 16 \
        --columns "id:98,id:116,id:126,id:109;id:99,id:111,id:127,id:110;id:100,id:121,id:128,id:138;name:Text Box 29 Kopie,name:Group 120 Kopie,name:Rectangle 127 Kopie,name:Textfeld 55 Kopie" \
        --area 3.6,25.1 --out deck_b.pptx
```

Für weniger Spalten `--delete` und dann `--columns` mit den verbleibenden. Die IDs oben sind
die der DVV-vf; nach dem Kopieren mit `inspect_deck.py --slide 16` prüfen. Danach
Sichtprüfung: Icons sitzen in den Spalten, Pfeile zwischen den Spalten, kein Textüberlauf
bei schmaleren Spalten (bei vier Spalten kürzer formulieren, nicht die Schrift verkleinern).

---

## Kapitel 3 im grünen Template

Die DVV-vf hat kein Kapitel 3, nur die Diskussionsfolie. Die Folien „Mögliche strategische
Ziele" und „Beteiligungsmodell" liegen anonymisiert im grünen Design in
`assets/kapitel3_gruen.pptx`. Sie werden mit `import_slide.py` in die Arbeitsdatei geholt:

```bash
python3 scripts/import_slide.py deck.pptx --von assets/kapitel3_gruen.pptx --folien 1,2 --nach 17 --out deck_c.pptx
```

Das Skript kopiert die Shapes einer Folie auf eine neue Folie mit dem Layout `Nur Titel`
des Zieldecks. Bilder und Diagramme werden nicht mitkopiert und gemeldet. Danach Titel,
Kolumne, Quellen und Texte per `fill_deck.py` setzen; die Kacheln und Kästen haben in der
Asset-Datei eindeutige Namen (`Ziel 1` bis `Ziel 6`, `Aspekte`, `Assets`, `Vorteile`,
`Kernsatz`).

Bei der kurzen Ausbaustufe entfällt das; die Diskussionsfolie ist Folie 17 der Vorlage.

---

## Skripte

| Skript | Wofür |
|---|---|
| `inspect_deck.py` | Inventar (`--slide N` mit Shape-IDs), Inhaltsprüfung (`--check`), Vergleich mit der Vorlage (`--vergleich`), fremde Namen (`--fremdnamen`) |
| `fill_deck.py` | Text in vorhandene Boxen und Tabellenzellen, Adressen `rolle:`, `ph:`, `name:`, `id:`, `!rNcM` |
| `tbd_box.py` | gelbe Kästen anlegen, listen, entfernen |
| `dup_shapes.py` | Shapes kopieren, löschen, Spalten verteilen |
| `import_slide.py` | Folie aus einer anderen Datei desselben Templates übernehmen |
| `stil_check.py` | Schreibregeln in pptx und md |
| `model_tools.py` | Excel: umbenennen, Kontrollen rechnen, Blöcke ausgeben, Euro-Zeichen finden |

Alle brauchen Python 3 und `python-pptx` beziehungsweise `openpyxl`; `model_tools.py
check` zusätzlich LibreOffice. Ausgabe auf UTF-8, damit sie auch unter Windows läuft.

**`fill_deck.py`** schreibt in vorhandene Boxen, bricht bei fehlendem oder mehrdeutigem
Ziel ab, entfernt beim Ersetzen unsichtbare Altlasten (Hyperlinks auf den alten Mandanten,
Felder, weiche Umbrüche) und meldet sie. Quell- und Zieldatei dürfen nicht identisch sein.
Mehrzeilige Inhalte als Liste von Zeilen. Format der Zuordnung:

```json
{
  "12": {
    "rolle:titel":   "Die ‹X› verbindet eine starke Versorgungs- und Infrastrukturposition mit …",
    "rolle:kolumne": "2. ‹X› – Übersicht und Herausforderungen",
    "name:Rectangle 26": "Die Finanzierung des jährlich wachsenden Investitionsprogramms bei …",
    "name:Textfeld 37": ["Die ‹X› ist der kommunale …", "Das Geschäftsmodell verbindet …"],
    "rolle:quelle":  "Quellen: Geschäftsberichte ‹X›, Unternehmensinformationen"
  },
  "14": {
    "id:23": ["Umsatz 2025", "474 Mio. EUR", "535 Mio. EUR (2024)"]
  }
}
```

**`inspect_deck.py --check`** meldet leere Pflichtplatzhalter, Arbeitsnotizen (WIP, TODO,
URLs, „xxx"), unersetzte Platzhalter, Folien ohne Aussagentitel, Kolumnen, die nicht zur
Agenda passen, doppelte Quellenzeilen. `--fremdnamen` ist Pflicht, sobald aus einer fremden
Vorlage gebaut wird: für die DVV-vf also `"DVV,Duisburg,Duisburger,DVG,Netze Duisburg"`.
Der Vergleich meldet jede Zugabe, Entfernung und Ersetzung gegenüber der Vorlage; jede muss
erklärbar sein.

**Was die Skripte nicht prüfen:** ob die Zahlen auf den Folien die des Modells sind, ob
die Diagramme aktuelle Daten zeigen, wie die Folien aussehen. Das wird von Hand abgenommen,
Folie für Folie, und im Prüfprotokoll des Reports vermerkt.

---

## Ablauf beim Bauen

1. Grüne Referenz kopieren, benennen: `JJJJMMTT_Metzler_‹X›_v1.pptx`.
2. `inspect_deck.py` laufen lassen, Folienliste gegen die Landkarte in der SKILL.md halten.
   Kapitel-3-Folien aus `assets/kapitel3_gruen.pptx` importieren, wenn die volle
   Ausbaustufe gilt; Diskussionsfolie löschen oder umgekehrt.
3. Agenda, Trenner und Kolumnen auf die Kapitelnamen setzen, Einheitsname Mergers &
   Acquisitions an allen sieben Stellen. Zuerst, weil sie überall gleich lauten müssen.
4. Kapitel 2 befüllen, Folie für Folie, mit Zwischenstopp. Investitionstabelle auf die
   Spaltenzahl des Falls bringen. Kernsatz-Kasten auf die Financials-Folie kopieren.
5. Kapitel 3 befüllen, dann Kapitel 1 (Kopie, Name, Aktualität).
6. Gelbe Kästen anlegen, `--list` in den Report.
7. `inspect_deck.py --check --vergleich vorlage.pptx --fremdnamen "…"`, `stil_check.py`,
   jede Abweichung erklären.
8. Jede Folie ansehen: fremde Namen, WIP-Reste, leere Platzhalter, Umbrüche, Überlauf,
   Icons, Pfeile. Datum auf Titelfolie und in den Platzhaltern gleich.
