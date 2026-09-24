# Der Report

Der Report ist das Beleg- und Übergabedokument. Er beantwortet die Frage „woher kommt das,
und was ist noch offen". Die PowerPoint ist das Arbeitsprodukt, das Excel die Zahlenquelle;
der Report verbindet beide und macht sie prüfbar. Ohne ihn kann ein Kollege eine Zahl auf
der Folie nicht nachvollziehen, und ohne die TBD-Liste weiß er nicht, was noch zu tun ist.

Kein Fließtext-Roman. Folie für Folie, tabellarisch, wo es geht.

## Format

Word-Datei `JJJJMMTT_‹Gesellschaft›_Report.docx`, erzeugt aus einem Markdown-Entwurf nach
`assets/report_vorlage.md` über die docx-Fähigkeit. Die Schreibregeln gelten (Mio. EUR,
Prozentzeichen, Cashflow, Einheitsname); der Report darf Sätze haben und Zitate mit Seite.

## Aufbau

```
1  Auftrag und Rahmen
   Gesellschaft, Einheit (Einzel / Konzern), Anlass, Adressat, Zeitraum je Rechenwerk,
   Stand der Quellen, die drei Ergebnisdateien mit Dateinamen

2  Storyline
   Tonlage mit Begründung: die vier Größen und ihre Werte
   Gegenhypothese und warum sie nicht trägt (oder: was offen ist)
   Die drei Kernsätze (Ausgangslage, Verschuldung, Financials) wie auf den Folien
   Einordnung der Ergebnislage (normalisiert, sondereffektgetrieben, nachhaltig)

3  Kapitel 2 Folie für Folie
   Je Folie:
     Was auf der Folie steht (Titel, Kernsatz, Zahlen in einer Tabelle)
     Belege in der Langfassung: jede Zahl und jede Aussage mit Dokument, Jahr, Seite
     Definitionen, die auf dieser Folie in Fußnoten stehen
     Was gelb ist, mit TBD-Nummer

4  Financial Model
   Definitionen (EBIT, EBITDA nach Einheit, Net-Debt-Stufe, EAT, CapEx, EK-Quote, Umsatz
   netto) mit Begründung
   Abweichungen, durchnummeriert, wortgleich aus dem Blatt Quellen & Hinweise
   Kontrollen: Ergebnis von model_tools.py check
   Die think-cell-Blöcke als Tabellen (model_tools.py blocks)

5  Research-Dossier
   Lückenliste: was nicht öffentlich ist und wie die Folie damit umgeht
   Widerspruchsliste: zwei Quellen, eine Zahl, Entscheidung
   Zitate aus dem Lagebericht, die die Storyline tragen, mit Seite

6  Kapitel 3 Ideen
   Die sechs Kacheln, die zwei fallspezifischen mit Beleg aus Kapitel 2
   Beteiligungsfähige Einheiten aus der Beteiligungsstruktur, je ein Satz
   Vorgeschlagene Beispielstruktur mit Begründung
   Empfohlene Ausbaustufe

7  Kapitel 1 und Rahmen
   Titel nach Anlass, Kapitelnamen, was aus der Vorlage kopiert wurde,
   was auf Aktualität zu prüfen ist

8  TBD-Liste
   Nummer, Folie, Sorte (TC / LOGO / PRUEFEN), was zu tun ist, welcher Excel-Block
   Wortgleich die Ausgabe von tbd_box.py --list

9  Prüfprotokoll
   Ausgabe von inspect_deck.py --check --vergleich --fremdnamen,
   stil_check.py, model_tools.py check; jede gemeldete Abweichung mit Erklärung
   Was von Hand abgenommen wurde: Zahlen gegen Modell je Folie, Sichtprüfung
```

## Was den Report gut macht

**Jede Zahl hat eine Seite.** „Geschäftsbericht 2025" reicht nicht; „Geschäftsbericht 2025,
GuV, S. 74" ist nachprüfbar. Bei Websites URL und Abrufdatum, bei Ratsvorlagen die
Vorlagennummer.

**Die Zitate stehen hier, nicht auf der Folie.** Der Satz aus dem Lagebericht, dass die
Investitionen nicht durch Abschreibungen gedeckt werden, ist der stärkste Beleg für die
Tonlage. Auf der Folie steht er in eigenen Worten; im Report wörtlich mit Seite.

**Die TBD-Liste ist die Arbeitsliste des Kollegen.** Er öffnet die PowerPoint, sieht Kasten
Nr. 4, schlägt Nr. 4 im Report nach, findet den Excel-Block und den Hinweis. Deshalb sind
die Nummern in Kasten und Liste dieselben, und deshalb steht bei jedem `TC` der Blockname
und bei jedem `LOGO` die Gesellschaft oder das Segment.

**Das Prüfprotokoll steht drin, auch wenn es grün ist.** Ein Kollege soll sehen, was geprüft
wurde und was nicht. Die Skripte prüfen Text, Boxen, Stil und Kontrollen; sie prüfen nicht,
ob die Zahl auf der Folie die des Modells ist. Das steht als Handabnahme drin, je Folie.

**Offene Fragen an den Nutzer** gehören an das Ende von Abschnitt 2 und 6, als Liste. Der
Report ist auch das Protokoll der Zwischenstopps.

## Was nicht hinein gehört

Persönliche Kontaktdaten aus Kapitel 1. Kaufpreise, Multiplikatoren, Bewertungen. Wertungen
über Personen oder Politik. Der Report wird weitergereicht, und er soll dieselbe Nüchternheit
haben wie die Unterlage.
