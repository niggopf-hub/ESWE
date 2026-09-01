---
name: stadtwerke-ma-unterlage
description: >-
  Erstellt M&A-Unterlagen zu kommunalen Versorgern, Stadtwerken, Energieversorgern und
  Netzgesellschaften nach dem Bogen "Kapitalflexibilisierung durch Einbindung privater
  Investoren" — von der Recherche in Unternehmensregister und Geschäftsbericht über das
  Financial Model bis zur PowerPoint, die aus der letzten Unterlage abgeleitet und in deren
  vorhandene Boxen geschrieben wird. Unbedingt verwenden, sobald ein Stadtwerk, kommunaler
  Versorger oder Netzbetreiber genannt wird und es um Unterlage, Präsentation, Pitch, Deck,
  Foliensatz, Steckbrief, One Pager, Beteiligungsstruktur, Investitionsbedarf, Verschuldung,
  Kapitalflexibilisierung, Investorenansprache, Handlungsoptionen oder Storyline geht. Auch bei
  beiläufigen Formulierungen auslösen ("mach mal was zu den Stadtwerken X", "schau dir die
  Zahlen von Y an", "Unterlage wie beim letzten Mal", "bau mir Kapitel 2") und wenn
  Jahresabschlüsse eines Versorgers im Projekt liegen. Auch für Teilaufgaben: nur Storyline, nur
  Financials, nur eine Folie.
---

# Unterlage kommunaler Versorger — Kapitalflexibilisierung

## Wofür das hier gut ist

Das Zieldokument ist eine rund 20-seitige Unterlage an den Vorstand eines kommunalen
Versorgers. Sie ist kein Informationsdokument, sondern ein Argument in drei Akten: *wer
spricht* (Credentials), *was wir an eurem Haus sehen* (Ausgangslage und Engpass, belegt aus
den offengelegten Zahlen), *worüber man deshalb reden sollte* (Handlungsoptionen). Sie wird
gelesen von Leuten, die ihre eigenen Zahlen besser kennen als du — jede Zahl muss deshalb
sitzen, und jede Aussage muss aus einer Quelle stammen, die auf dem Tisch liegt.

Der Adressat entscheidet nicht in der Unterlage. Er entscheidet, ob er das Gespräch führt.
Das ist der Maßstab für alles, was folgt.

## Ablauf

Sechs Schritte, jeder mit einem Zwischenstopp. Nicht in einem Durchlauf produzieren — die
Unterlage lebt davon, dass der Nutzer die Zwischenstände korrigiert, und ein falsch
gesetzter Bogen macht 15 Folien wertlos.

### Schritt 0 — Auftrag klären

Vor allem anderen zwei Dinge feststellen, weil sie den gesamten Bogen bestimmen:

- **Wer ist der Adressat?** Vorstand, Aufsichtsrat, Gesellschafter (Stadt/Kämmerei), oder
  ein strategischer Partner? Ein Kämmerer liest Kapitel 3 anders als ein technischer Vorstand.
- **Ist das ein Erstkontakt oder eine Fortsetzung?** Beim Erstkontakt trägt Kapitel 1 viel
  Gewicht. Bei einer Fortsetzung schrumpft es auf zwei Folien, und Kapitel 3 wird konkreter.

Wenn beides nicht aus dem Auftrag hervorgeht: fragen. Es sind zwei Sätze, und sie sparen
einen kompletten Umbau.

### Schritt 1 — Material sichten und Lücken benennen

Prüfen, was im Projekt liegt, und **explizit sagen, was fehlt**. Ohne die letzte Unterlage
gibt es keinen Bogen und kein Template; ohne die Abschlüsse gibt es keine Financials.

Details, Quellen und was aus jedem Dokument zu holen ist: `references/recherche.md`.

Kurzfassung der Pflichtmaterialien:

| Material | Wozu | Wo |
|---|---|---|
| Letzte vergleichbare Unterlage (.pptx) | Bogen, Template, Kapitel 1, Schaubilder | Projektordner |
| Jahresabschlüsse 4–5 Jahre | Financials, Beteiligungen, Lagebericht | Unternehmensregister |
| Geschäftsbericht (aktuellstes Jahr) | Aktuelles Jahr, Strategie, O-Töne | Website des Unternehmens |
| Handelsregisterauszug | Gesellschafter, Organe, Kapital | Registerportal |
| Website / Presse | Projekte, Personalien, Wärmeplanung | Recherche |

**Zwischenstopp:** Materialstand und Lücken melden, bevor du anfängst.

### Schritt 2 — Storyline für diesen Deal ableiten und bestätigen lassen

**Das ist immer der erste inhaltliche Arbeitsschritt — vor jeder Folie, vor jeder Zahl.**

`references/storyline.md` lesen. Dort steht der Bogen als Argumentationskette: was jedes
Kapitel behauptet, womit es das belegt, welche Frage es offen lässt. Der Bogen ist das
übertragbare Gerüst; die Belege sind pro Transaktion neu.

Dann prüfen, ob das Gerüst zur vorliegenden Transaktion trägt. Die entscheidende Frage:

> **Gibt es hier wirklich eine Schere zwischen Investitionsprogramm und
> Innenfinanzierungskraft — und lässt sie sich aus offengelegten Zahlen belegen?**

Wenn ja, trägt der Bogen. Wenn nein — etwa weil das Unternehmen kaum verschuldet ist, weil
das Investitionsprogramm nicht beziffert ist, oder weil der eigentliche Anlass ein ganz
anderer ist (Gesellschafterwechsel, Portfoliobereinigung, Nachfolge) — dann trägt er nicht,
und du musst das sagen, statt ihn zu erzwingen. Eine Unterlage, die eine Not konstruiert,
die der Vorstand nicht empfindet, verliert ihn auf Folie 12.

Ergebnis dieses Schritts ist ein kurzer Text, kein Foliensatz: Gesamtbogen in drei bis fünf
Sätzen, dann pro Kapitel Aussage / Beleg / offene Frage. Belege konkret benennen — mit Zahl
und Quelle, nicht als Platzhalter.

**Zwischenstopp:** Storyline vorlegen und bestätigen lassen. Erst danach schreiben.

### Schritt 3 — Financial Model bauen

Die Zahlen kommen aus einer Excel-Mappe, nicht aus dem Fließtext. Das ist keine Formalie:
die Financial-Folie und die Verschuldungsfolie sind die einzigen Stellen, an denen der
Adressat dich sofort widerlegen kann.

Architektur, Farbkonvention, Kontrollzeilen und Kennzahlendefinitionen:
`references/financial-model.md`. Wichtigste Punkte:

- Input-Blätter transkribieren den HGB-Abschluss zeilengetreu, ein Blatt je Rechenwerk.
- Ein Output-Blatt (`Overview FS`) enthält genau die Blöcke, die auf die Folien gehen.
- Farbkonvention: **blau = Eingabewert aus dem Abschluss, schwarz = Formel im Blatt,
  grün = Verweis auf ein anderes Blatt.** Summen sind nie hartcodiert.
- Kontrollzeilen (Aktiva ./. Passiva, Bilanzgewinn = 0, Cashflow-Abstimmung, EK-Quote
  berechnet gegen Lagebericht) müssen null ergeben, bevor eine Zahl auf eine Folie darf.
- Ein Blatt `Quellen & Hinweise` dokumentiert Abgrenzung, Gliederungsharmonisierung und
  **jede Abweichung zwischen zwei Abschlüssen**. Vorjahreswerte werden regelmäßig
  umgegliedert; wer das nicht dokumentiert, wird im Termin darauf angesprochen.

**Quelldateien bleiben unverändert.** Ein vorhandenes Modell wird nie an Ort und Stelle
erweitert, sondern als neue Version kopiert (`…_v2.xlsx`) — ebenso Abschlüsse, Berichte und
die Referenzunterlage. Wer eine Quelldatei überschreibt, nimmt dem Nutzer den Stand, gegen
den er prüfen wollte, und macht die Änderung unsichtbar. Wenn eine Quelldatei doch angefasst
werden muss, vorher sagen.

**Zwischenstopp:** Kennzahlenübersicht (Umsatz, Rohertrag, EBITDA, Capex, Net Debt,
Net Debt/EBITDA, EK-Quote, Cashflows) zeigen und plausibilisieren lassen.

### Schritt 4 — Kapitelweise schreiben

Nicht das ganze Deck am Stück. Reihenfolge: **Kapitel 2 → Kapitel 3 → Kapitel 1.**

Kapitel 2 zuerst, weil es die Fakten setzt, aus denen Kapitel 3 folgen muss. Kapitel 1
zuletzt, weil es das Standardteil ist und aus der letzten Unterlage übernommen wird —
inhaltliche Energie gehört nach hinten, nicht nach vorn.

Nach jedem Kapitel anhalten und vorlegen. Die Details je Kapitel:

- `references/kapitel-2-unternehmen.md` — Ausgangslage, Steckbrief, Beteiligungsstruktur,
  Investitionsbedarf, Financials, strategische Stoßrichtungen
- `references/kapitel-3-handlungsoptionen.md` — Ziele, Optionenraum, Beteiligungsmodelle,
  Investorenlandschaft, Mehrwert des Hauses
- `references/kapitel-1-credentials.md` — Ansprechpartner, Haus, Sektorfokus, Track Record,
  Case Studies

### Schritt 5 — In PowerPoint bauen

**Grundregel: Die letzte Unterlage wird kopiert, und der Text wird in die vorhandenen
Boxen geschrieben. Es werden keine neuen Textfelder eingefügt.**

Das ist die wichtigste operative Regel des Skills. Das Template trägt Master, Schriften,
Farben, Fußzeilen und die think-cell-Objekte der Diagramme. Ein neu eingefügtes Textfeld
erbt nichts davon: es steht in einer anderen Schrift, an einer minimal anderen Position,
und beim nächsten Bearbeiten fällt es auf. Eine Folie, die aus lauter frei platzierten
Kästchen besteht, ist nicht mehr pflegbar.

Vollständige Mechanik — Platzhalter-Indizes, Layoutfamilien, think-cell, Schaubilder,
Skripte: `references/powerpoint.md`. Das Wichtigste in Kürze:

- Jede Inhaltsfolie hat feste Platzhalter, die alle befüllt gehören: Aussagentitel,
  Kapitelkolumne, Bereichsüberschriften, **Quellenzeile**, **Fußnotenzeile**.
- Diagramme sind think-cell-Objekte mit einem eingebetteten Datenobjekt. Nicht
  programmatisch neu bauen — Datenwerte in think-cell aktualisieren, sonst geht das Diagramm
  kaputt.
- `scripts/inspect_deck.py` listet alle Folien, Layouts, Platzhalter und Textboxen einer
  .pptx — damit findest du die Box, in die geschrieben werden soll.
- `scripts/fill_deck.py` schreibt Text in vorhandene Boxen (nach Folie + Platzhalter-Index
  oder Shape-Name) und legt bewusst keine neuen an.
- `scripts/inspect_deck.py --vergleich <vorlage.pptx>` meldet vor der Übergabe jede Zugabe
  gegenüber der Vorlage. Eine hinzugefügte Box fällt sonst niemandem auf.

### Schritt 6 — Prüfen

Die Prüfliste am Ende dieser Datei abarbeiten. Danach die Unterlage übergeben, mit einer
kurzen Notiz, welche Zahlen aus welchem Jahr stammen und was noch offen ist.

## Landkarte des Dokuments

Rund 20 Folien, drei Kapitel. Zweck je Folie in einer Zeile — die inhaltliche Tiefe steht
in den references-Dateien.

| # | Folie | Zweck |
|---|---|---|
| 1 | Titel | Thema, Ort/Datum, Vertraulichkeitsvermerk |
| 2 | Agenda | Die drei Kapitel als Versprechen |
| 3 | Kapiteltrenner 1 | — |
| 4 | Ihre Ansprechpartner | Personen, die haften; Profil plus Referenzprojekte |
| 5 | Das Haus | Warum unabhängig, warum langfristig |
| 6 | Geschäftsfelder | Breite als Beleg für Substanz |
| 7 | Sektorfokus | Energie & Infrastruktur ist kein Nebengeschäft |
| 8 | Track Record | Aktuelle Mandate als Tombstones |
| 9–10 | Case Studies | Zwei Transaktionen im Detail: was wir konkret gemacht haben |
| 11 | Kapiteltrenner 2 | — |
| 12 | Unser Verständnis der Ausgangslage | Die These des Kapitels, sieben Bullets, Kernsatz im Kasten |
| 13 | Kunden und Infrastruktur | Steckbrief: KPI-Kacheln, Umsatzsplit, Erlösquellen |
| 14 | Beteiligungsstruktur | Wer hält was — kommunale und strategische Verankerung |
| 15 | Investitionsbedarf | Verschuldungsentwicklung gegen Investitionsprogramm |
| 16 | Financials | GuV, Cashflow, Bilanz über 5 Jahre plus Kommentar |
| 17 | Strategische Stoßrichtungen | Wohin das Unternehmen selbst will |
| 18 | Kapiteltrenner 3 | — |
| 19 | Mögliche strategische Ziele | Der Zielraum, aus dem Optionen folgen |
| 20 | Beteiligungsmodelle | Wie eine Partnerschaft konkret aussähe |
| 21 | Mehrwert des Hauses | Warum wir, in sechs Punkten |
| 22 | Disclaimer | Standardtext aus dem Master |

## Mechanik und Urteil trennen

Ein Teil dieser Arbeit ist reproduzierbar, ein Teil nicht. Die Trennung sauber zu halten,
ist der Unterschied zwischen einer brauchbaren und einer peinlichen Unterlage.

**Mechanisch — eigenständig erledigen:**
Gliederung und Folienreihenfolge; Steckbrief und KPI-Kacheln; Beteiligungsstruktur aus
Register und Anteilsbesitzliste; Financial Model inklusive Kontrollen; die Financial-Tabelle
und ihre Kommentierung *der Zahlenbewegung*; Kapitel 1 aus der letzten Unterlage;
Quellenzeilen, Fußnoten, Kapitelkolumnen; Vollständigkeitsprüfung.

**Urteil — nicht vorformulieren, sondern fragen:**
- **Die strategische Begründung.** Warum ist gerade jetzt der Moment, warum diese Option?
  Das hängt an Gesprächen, Politik und Gesellschafterlage, die in keinem Abschluss stehen.
- **Das Bewertungsnarrativ.** Wie die Ergebnislage einzuordnen ist — normalisiert, durch
  Sondereffekte getragen, nachhaltig oder nicht — ist eine Wertung, keine Ableitung.
- **Die Auswahl der Handlungsoptionen.** Welche Assets überhaupt in Frage kommen, ist eine
  Einschätzung über politische Durchsetzbarkeit.
- **Die Schärfe von Kapitel 3.** Konkreter Vorschlag oder Gesprächsangebot? Das entscheidet
  der Nutzer, nicht du.

An diesen Stellen gehören gezielte Rückfragen und eine Checkliste "was darf hier nicht
fehlen" in die Arbeit — kein vorgeschriebener Text. Die Checklisten stehen jeweils am Ende
von `references/kapitel-2-unternehmen.md` und `references/kapitel-3-handlungsoptionen.md`.

## Wo nachschlagen

| Datei | Wann |
|---|---|
| `references/storyline.md` | **Immer zuerst**, in Schritt 2 |
| `references/recherche.md` | Schritt 1: welche Quelle liefert was, und wie zitiert man sie |
| `references/financial-model.md` | Schritt 3: Excel-Architektur, Kennzahlen, Kontrollen |
| `references/kapitel-2-unternehmen.md` | Schritt 4: Folien 12–17 im Detail |
| `references/kapitel-3-handlungsoptionen.md` | Schritt 4: Folien 19–21 im Detail |
| `references/kapitel-1-credentials.md` | Schritt 4: Folien 4–10, meist Übernahme |
| `references/powerpoint.md` | Schritt 5: Template-Mechanik, think-cell, Skripte |
| `assets/musterdokument.md` | Folie-für-Folie-Vorlage mit Platzhaltern |
| `assets/textbausteine.md` | Standardformulierungen und Titelmuster |
| `assets/tabellenlayouts.md` | Exakte Layouts für Financial-Tabelle, KPI-Kacheln, Struktur |

## Typische Fehler

Diese Liste stammt aus echten Unterlagen, nicht aus der Theorie.

**Reste aus der Vorlage.** In einer ausgelieferten Unterlage stand auf einer Folie des
Kapitels 2 noch die Kapitelkolumne des *vorherigen* Mandanten. Die Kolumnentitel,
Fußzeilen und Kapitelnamen werden beim Kopieren übersehen, weil sie klein und grau sind.
Nach dem Befüllen jede Folie einzeln auf fremde Namen prüfen — auch in Fußnoten und
Quellenzeilen.

**Arbeitsnotizen auf der Folie.** In einer anderen Unterlage lagen noch WIP-Kästchen mit
Quell-URLs und Zwischenständen auf der Folie, in 8 pt. Vor Übergabe alle Notizkästchen,
Links und Klebezettel entfernen — auch die, die hinter einem Bild oder außerhalb des
sichtbaren Bereichs liegen.

**Quelldatei still überschrieben.** Modelle, Abschlüsse und die Referenzunterlage sind
Belege, keine Arbeitsdateien. Änderungen gehören in eine neue Version mit eigenem Namen.

**Neue Textboxen statt Platzhalter.** Führt zu falscher Schrift, verrutschten Rändern und
einer Datei, die niemand mehr sauber weiterbearbeiten kann. Siehe Schritt 5.

**Diagramme programmatisch angefasst.** Die Diagramme sind think-cell-Objekte. Wer sie mit
einem Skript ersetzt, verliert die Verknüpfung und die Formatierung.

**Zwei Quellen, eine Zahl.** Mitarbeiterzahl laut Abschluss und laut Website weichen fast
immer ab, ebenso Netzlängen und Kundenzahlen. Nicht stillschweigend eine wählen — beide
nennen und die Differenz in einer Fußnote erklären.

**Vorjahreswerte, die sich ändern.** Derselbe Cashflow steht im Abschluss des Folgejahres
oft anders. Das ist meist eine Umgliederung, keine Korrektur. Im Modell dokumentieren,
welche Fassung angesetzt wurde.

**Beteiligungsstruktur aus dem Gedächtnis.** Quoten, Eigenkapital und Jahresergebnis je
Beteiligung gehören aus der Anteilsbesitzliste des Abschlusses, mit Stichtag. Zwischen
mittelbaren und unmittelbaren Beteiligungen unterscheiden.

**Generisches Kapitel 3.** Handlungsoptionen, die für jedes Stadtwerk gelten, sind
wertlos. Jede Option muss an den in Kapitel 2 belegten Engpass anknüpfen.

**Titel ohne Aussage.** "Financials" ist kein Titel. Siehe Prüfliste.

## Prüfliste vor Übergabe

**Aussage**
- [ ] Jeder Folientitel ist ein vollständiger Aussagesatz, der allein gelesen die Botschaft
      trägt. Wer nur die Titel liest, kennt die Argumentation.
- [ ] Kapitel 3 knüpft erkennbar an den in Kapitel 2 belegten Engpass an; keine Option
      steht ohne Bezug zu einer Zahl aus Kapitel 2.
- [ ] Der Bogen stimmt: Legitimation → Engpass → Lösungsraum, ohne Sprung.

**Zahlen**
- [ ] Jede Zahl ist auf einen offengelegten Abschluss oder Geschäftsbericht rückführbar und
      steht so auch im Modell.
- [ ] Alle Kontrollzeilen im Modell stehen auf null.
- [ ] Abweichungen zwischen Quellen sind dokumentiert und, wo sie auf der Folie sichtbar
      werden, in einer Fußnote erklärt.
- [ ] Stichtage und Geschäftsjahre sind überall genannt und einheitlich.
- [ ] Einheiten stimmen (T€ im Modell, Mio. € auf den Folien — nicht vermischen).

**Mechanik**
- [ ] Keine fremden Mandanten- oder Projektnamen mehr im Dokument — auch nicht in
      Kolumnentiteln, Fußnoten und Dateinamen.
- [ ] Keine WIP-Notizen, Klebezettel oder Quell-URLs auf den Folien.
- [ ] Keine neu eingefügten Textfelder neben den Template-Platzhaltern — mit
      `--vergleich` gegen die Vorlage geprüft, jede Zugabe ist ein erklärtes Duplikat.
- [ ] Jede Inhaltsfolie hat Quellenzeile und, wo nötig, Fußnoten.
- [ ] Diagramme sind unverändert think-cell-Objekte.
- [ ] Agenda, Kapiteltrenner und Kolumnentitel nennen dieselben Kapitelnamen.
- [ ] Dateiname nach Schema `JJJJMMTT_<Haus>_<Unternehmen>_<Version>`.
