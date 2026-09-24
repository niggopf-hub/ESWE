# Financial Model

Die Zahlen der Unterlage kommen aus einer Excel-Mappe, nicht aus dem Fließtext. Die
Financial- und die Verschuldungsfolie sind die Stellen, an denen der Adressat dich im
Termin sofort widerlegen kann. Wackelt dort eine Zahl, wackelt der Rest.

Die Mappe wird bei jedem Fall gebaut, aus den Jahresabschlüssen, im Hausformat. Die Vorlage
ist `assets/financial_model_vorlage.xlsx`; sie hat den Aufbau des ESWE-Modells 2021–2025
(das seinerseits das evm/enm-Format übernommen hat) und ist anonymisiert.

## Inhalt

1. Aufbau der Mappe
2. Vom Abschluss ins Modell
3. Definitionen nach Einheit und Datenlage
4. Kontrollen
5. Abweichungen und Lücken
6. Die think-cell-Blöcke
7. Skript `model_tools.py`
8. Mehrere Gesellschaften

---

## 1. Aufbau der Mappe

```
Cover                 Inhalt, Farbkonvention, Einheit
Output>>              Trenner
  Overview FS         verdichtete Ertrags-, Finanz- und Vermögenslage, Kennzahlen,
                      rechts daneben die think-cell-Blöcke
Input>>               Trenner
  GES Bilanz          zeilengetreu nach § 266 HGB, ein Jahr je Spalte
  GES GuV             zeilengetreu nach § 275 Abs. 2 HGB, Gesamtkostenverfahren
  GES Cashflow        die drei Salden nach DRS 21 plus Fonds
  GES KPIs            Rohertrag, EBITDA, EBIT, EAT, Cashflows, Net Debt, Faktoren, CapEx, Absatz
  GES Capex Revenue   Investitionen und Umsatz nach Bereichen, Absatzmengen, Umsatzring
  Quellen & Hinweise  Gesellschaft, Quellen je Jahr, Einheit, Definitionen, Abweichungen
```

„GES" wird durch das Kürzel der Gesellschaft ersetzt (`ESWE Bilanz`, `DVV GuV`). Die
Formeln der Vorlage verweisen auf die Blattnamen; `model_tools.py rename` benennt Blätter
und Formeln in einem Schritt um.

**Input-Blätter transkribieren, Output-Blätter rechnen.** Wer auf einem Input-Blatt rechnet
oder auf einem Output-Blatt tippt, verliert die Nachvollziehbarkeit, und die ist der einzige
Zweck der Mappe.

**Format:** Alles in **Mio. EUR**, nie T€, nie ein Euro-Zeichen. Die Abschlüsse
veröffentlichen in T€; die Werte werden exakt hinterlegt (T€ geteilt durch 1.000) und auf
eine Nachkommastelle angezeigt. Summen und Kontrollen rechnen mit den vollen Werten.
Zahlenformat `#.##0,0` mit Klammern für negative Werte und Strich für null, Prozente `0,0 %`,
Vielfache `0,0x`. Titelbanner und Kopfzeile in den Farben der Vorlage, Spalte A als
Randspalte, Gitternetz aus.

**Farbkonvention** (steht auf dem Cover, sonst versteht sie beim nächsten Mal niemand):

| Farbe | Bedeutung |
|---|---|
| Blau | Eingabewert direkt aus dem Abschluss oder Geschäftsbericht |
| Schwarz | Formel innerhalb des Blattes |
| Grün | Verweis auf ein anderes Blatt |
| Grau kursiv | im betreffenden Jahr nicht separat ausgewiesen (n.a.) |

Sämtliche Zwischen- und Endsummen sind Formeln, nirgends hartcodiert. Eine hartcodierte
Summe stimmt beim Anlegen und ist nach der ersten Korrektur falsch.

---

## 2. Vom Abschluss ins Modell

**Fünf Jahre aus vier Abschlüssen.** Jeder Abschluss trägt das Geschäftsjahr und das
Vorjahr. Der Geschäftsbericht des jüngsten Jahres enthält oft den vollständigen Abschluss
(Bilanz, GuV, Anhang, Kapitalflussrechnung); dann reicht die Reihe ein Jahr weiter.

**Die Gliederung folgt dem jüngsten Abschluss.** Bezeichnungen und Positionsnummern ändern
sich über die Jahre; ältere Jahre werden darauf harmonisiert. Positionen, die es in einem
Jahr nicht gab, werden mit null angesetzt, damit die Gliederung über fünf Jahre gleich
bleibt, und das steht in `Quellen & Hinweise`.

**Vorjahreswerte, die sich ändern.** Derselbe Cashflow steht im Folgeabschluss oft anders,
weil zwischen den Bereichen umgegliedert wurde. Erkennungsmerkmal: die Summe stimmt, die
Aufteilung nicht. Regel: der jüngere Abschluss gilt, die Abweichung wird notiert.

**Lagebericht gegen Anhang.** Der Lagebericht rundet und rechnet betriebswirtschaftlich
(EBT 52,4 statt 52,7 in der GuV, Bankverbindlichkeiten 123,7 statt 124,2 im
Verbindlichkeitenspiegel). Regel: die GuV und der Anhang gelten, weil sie zur Bilanzsumme
passen. Die Lagebericht-Werte kommen als „nachrichtlich" daneben, wo sie eine Kontrolle
ermöglichen (EK-Quote laut Lagebericht).

**Segmentzeilen, die auftauchen und verschwinden.** Ein Abschluss weist eine eigene Zeile
„Telekommunikation" aus, der nächste nicht. Regel: die Darstellung des Berichtsjahres,
Gesamtsumme prüfen, in `Quellen & Hinweise` festhalten.

**Bild-PDFs.** Registerauszüge von Konzernen sind oft Bild-Container mit OCR-Textlayer
(DVV). Text extrahieren, jede Zahl gegen das gerenderte Bild lesen, bevor sie ins Modell
geht. Das ist der Schritt, der die meiste Zeit kostet, und der einzige, den der Nutzer
danach stichprobenweise sehen will.

---

## 3. Definitionen nach Einheit und Datenlage

Die Kennzahlen sind nicht standardisiert. Sie werden einmal festgelegt, stehen im Blatt
`Quellen & Hinweise` und auf der Folie in der Fußnote, an beiden Stellen gleich. Das
ESWE-Modell rechnete EBITDA anders als die ESWE-Folie; das darf nicht wieder passieren.

### EBIT und EBITDA nach Einheit

| Einheit | EBIT | EBITDA |
|---|---|---|
| **Einzelabschluss** (Vertriebs-AG mit Töchtern, ESWE, evm) | Betriebliches Ergebnis + Beteiligungsergebnis − Abschreibungen auf Finanzanlagen, also EBT − Zinsergebnis | EBIT + Abschreibungen auf Sachanlagen und immaterielle Vermögensgegenstände + Abschreibungen auf Finanzanlagen |
| **Konzernabschluss** (Holding, DVV, Krefeld) | Konzern-Betriebsergebnis | EBIT + Abschreibungen |

Beim Einzelabschluss gehört das Beteiligungsergebnis dazu, weil es das operative Ergebnis
der nicht konsolidierten Töchter ist. Bei ESWE sind das sw netz, WiTCOM und KMW: ein
Drittel des Geschäfts. Es wegzulassen hieße, die halbe Ertragskraft zu ignorieren, und der
Faktor Net Debt zu EBITDA wäre um die Hälfte zu hoch (2,7x statt 1,7x). Beim Konzern ist es
konsolidiert; was als Beteiligungsergebnis bleibt, sind at-equity-Anteile und Minderheiten,
und die bleiben unterhalb.

Das KPI-Blatt führt beide Wege als Zeilen. Die Einheit aus Schritt 0 entscheidet, welche
Zeile in den Chart-Block geht. Fußnote auf der Kachelfolie: „1) Betriebliches Ergebnis
inklusive Beteiligungsergebnis".

### Net Debt nach Datenlage

Drei Stufen, die Stufe wird im Blatt `Quellen & Hinweise` und in der Fußnote genannt:

| Stufe | Definition | Wann |
|---|---|---|
| 1 voll | Finanzverbindlichkeiten + Pensionsrückstellungen + Verbindlichkeiten gegen verbundene / assoziierte Unternehmen − liquide Mittel − Forderungen gegen verbundene / assoziierte Unternehmen | Konzern mit Cash-Pool, Pensionen und Verbundsalden im Anhang ausgewiesen (evm, Krefeld, Duisburg 2024) |
| 2 mittel | Verbindlichkeiten gegenüber Kreditinstituten + Pensionsrückstellungen − liquide Mittel | Pensionen ausgewiesen, keine relevanten Verbundsalden (DVV) |
| 3 kurz | Verbindlichkeiten gegenüber Kreditinstituten − liquide Mittel | Einzelabschluss ohne Pensionsrückstellungen im Anhang oder ohne Aufgliederung (ESWE) |

Vorsicht bei Ergebnisabführungsvertrag: Die noch nicht gezahlte Gewinnabführung und die
Ausgleichszahlung stecken in den Verbindlichkeiten gegen verbundene Unternehmen und wandern
nach Stufe 1 in die Nettoverschuldung, obwohl sie Ergebnisverwendung sind. Dann Stufe 2
oder 3 nehmen und in `Quellen & Hinweise` sagen, warum.

Über alle Jahre dieselbe Stufe. Bei Definitionsänderung gegenüber einer älteren Unterlage
eine Überleitung im Modell: alter Wert, jede Änderung mit Betrag, neuer Wert.

### Weitere Größen

| Kennzahl | Definition |
|---|---|
| Gesamtleistung | Umsatz + Bestandsveränderung + aktivierte Eigenleistungen |
| Rohertrag | Gesamtleistung − Materialaufwand |
| Rohertrag-Marge | Rohertrag / Gesamtleistung (evm/ESWE-Konvention; DVV rechnet auf Umsatz, das steht dann in der Fußnote) |
| EBITDA-Marge | EBITDA / Umsatz |
| EAT | Ergebnis nach Steuern, **vor** Ausgleichszahlung und Gewinnabführung, also der Jahresüberschuss vor Ergebnisverwendung |
| Free Cashflow | Operating + Investing Cashflow |
| Total Cashflow | Summe der drei Cashflows = Veränderung des Finanzmittelfonds |
| Net Debt / EBITDA | Verschuldungsfaktor, `n. m.` bei EBITDA ≤ 0 |
| EK-Quote | Eigenkapital / Bilanzsumme; beim Konzern inklusive nicht beherrschender Anteile; nachrichtlich die Quote laut Lagebericht daneben |
| CapEx | Gesamtinvestitionen inklusive Finanzanlagen (Kachel); in der Segmenttabelle ohne Finanzanlagen mit Fußnote |
| Umsatz | netto Strom- und Gassteuer, wie in der GuV; ein Brutto-Ausweis aus einer älteren Unterlage wird in `Quellen & Hinweise` erklärt (DVV: 31 Mio. EUR Differenz) |

### Wo Kennzahlen ihre Aussage verlieren

- **Net Debt / EBITDA bei EBITDA nahe null oder negativ.** Faktor nicht ausweisen (`n. m.`),
  Kommentar sagt in einem Satz, warum.
- **CAGR bei ungeeignetem Ausgangsjahr.** Nur über Zeiträume, deren Randjahre beide normal
  sind; sonst die Reihe zeigen und die Bewegung im Kommentar beschreiben.
- **Ein Sonderjahr.** Ein Beteiligungsverkauf drückt den Faktor auf 0,1x; zwölf Monate
  später sind es 1,2x. Nie auf ein Jahr stützen.

---

## 4. Kontrollen

Vier Kontrollzeilen, jede muss null ergeben. Solange eine ungeklärt ist, geht keine Zahl
auf eine Folie. Geklärt heißt: null, oder eine benannte und begründete Differenz.

| Kontrolle | Blatt | Prüft |
|---|---|---|
| Aktiva ./. Passiva | Bilanz | Bilanz vollständig übertragen |
| Bilanzgewinn GuV ./. Bilanz | GuV | Ergebnisverwendung abgebildet (bei EAV null) |
| Finanzmittelfonds berechnet ./. veröffentlicht, und ./. Kassenbestand | Cashflow | Kapitalflussrechnung schlüssig |
| Umsatzaufteilung ./. GuV | Capex Revenue | Erlösquellen vollständig |

Dazu nachrichtlich: EK-Quote berechnet gegen Lagebericht.

**Der Finanzmittelfonds ist keine Bilanzposition.** Die Kontrolle gegen den Kassenbestand
gilt nur, wenn das Unternehmen den Fonds als reine Bankguthaben definiert. Konzerne rechnen
oft Kassenkredite ab; dann ist der Fonds negativ bei positivem Kassenbestand. Dann die
veröffentlichte Fondsdefinition nachbauen (Kasse + kurzfristige Anlagen − Kassenkredite) und
nur berechnet gegen veröffentlicht auf null prüfen. Die Kontrolle prüft die Übertragung,
nicht die Definition. Nie die Quelle anpassen, damit ein Test besteht.

`model_tools.py check` rechnet die Mappe mit LibreOffice durch und liest die Kontrollzeilen.

---

## 5. Abweichungen und Lücken

**Vier Fälle, vier Kennzeichnungen**, nie zusammenwerfen:

| Fall | Kennzeichen |
|---|---|
| Tatsächlich null | `0` |
| Nicht gesondert ausgewiesen | `n.a.`, grau kursiv |
| In anderer Position enthalten | `→ Pos. X` |
| Nicht verfügbar | `n. v.` |

Nur der erste Fall geht in Summen ein. Eine leere Zelle mit null zu füllen, macht aus einer
Unbekannten eine Aussage.

**Rundung.** Drei Positionen zu je 33,3 ergeben 99,9, die ausgewiesene Summe lautet 100,0.
Das ist kein Fehler. Toleranz: die halbe Anzeigeeinheit mal Anzahl der Summanden. Auf der
Folie steht der Quellwert; Einzelposten werden nie angepasst, damit eine Summe aufgeht.

**Das Blatt `Quellen & Hinweise`** ist der Prüfpfad und der Teil, der sich im Termin
auszahlt. Es enthält: Gesellschaft mit Registergericht und Nummer; je Jahr die Quelle mit
Erstellungsdatum und welche Jahre sie liefert; Berichtsumfang und Abgrenzung
(Tätigkeitsabschlüsse nach § 6b EnWG nicht enthalten, kein Konzernabschluss wegen
Einbeziehung in die Holding); Einheit; Farbkonvention; die gewählten Definitionen (EBIT,
EBITDA, Net-Debt-Stufe, EK-Quote, CapEx) mit Begründung; die Abweichungen durchnummeriert
mit Fundstelle, beiden Werten und der Entscheidung; die Gliederungsharmonisierung.

Die Abweichungen wandern wortgleich in den Report.

---

## 6. Die think-cell-Blöcke

Rechts auf `Overview FS`, ab Spalte J. Jeder Block entspricht genau einem think-cell-Objekt
der Folien, in der Reihenfolge der Datenreihen, die das Objekt braucht, mit Kopfzeile und
Jahren. Jede Zelle ist ein grüner Verweis, nichts wird doppelt erfasst. Der Kollege
markiert den Block inklusive Kopfzeile und fügt ihn in think-cell ein. Das ist die
Vorarbeit, die think-cell im Haus hält und trotzdem Handarbeit spart.

| Block | Reihen | Folie, Objekt |
|---|---|---|
| `GuV-Chart` | Umsatz, Rohertrag, EBITDA, Rohertrag-Marge, EBITDA-Marge, CAGR Umsatz | Financials, Block 1 |
| `Cashflow-Chart` | Operating Cashflow, Investing Cashflow, Financing Cashflow, Total Cashflow | Financials, Block 2 |
| `Bilanz-Chart` | Liquide Mittel, Net Debt, Eigenkapitalquote | Financials, Block 3 |
| `Verschuldung` | Net Debt, Net Debt / EBITDA | Investitionsbedarf, links |
| `Kacheln` | zehn Werte mit Vorjahr: Kunden oder Absatz Strom, Kunden oder Absatz Gas, Stromnetz km, Gasnetz km, Umsatz, EBITDA, EBIT, EAT, CapEx, Mitarbeiter | Kunden und Netz, Kacheln (native Textfelder, per Skript befüllt) |
| `Umsatzring` | Erlösquellen in Mio. EUR und Prozent, Summe | Kunden und Netz, Ring |
| `Investitionstabelle` | CapEx je Segment für ‹J› und ‹J-1›, Summe, nicht enthaltene Bereiche | Investitionsbedarf, Tabelle |

Der Blockname steht im gelben Kasten auf der Folie („think-cell aktualisieren, Excel-Block
GuV-Chart"). `model_tools.py blocks` gibt alle Blöcke als Markdown für den Report aus.

Die Kreise (Margen, EK-Quote, Faktoren) sind auf den Folien native Shapes und werden per
`fill_deck.py` aus dem Block befüllt; nur die Säulen sind think-cell.

---

## 7. Skript `model_tools.py`

```bash
python3 scripts/model_tools.py rename vorlage.xlsx --kuerzel ESWE --name "ESWE Versorgungs AG" --out modell.xlsx
python3 scripts/model_tools.py check modell.xlsx           # Kontrollen über LibreOffice durchrechnen
python3 scripts/model_tools.py blocks modell.xlsx          # think-cell-Blöcke als Markdown
python3 scripts/model_tools.py euro modell.xlsx            # Euro-Zeichen und T€ finden
```

`rename` ersetzt „GES" in Blattnamen, Formeln und Titeln. `check` schreibt eine
durchgerechnete Kopie (LibreOffice headless) und meldet jede Kontrollzeile, die nicht null
ist. `blocks` liest die Blöcke ab Spalte J und gibt sie als Tabellen aus. `euro` findet
Verstöße gegen die Einheitenregel.

---

## 8. Mehrere Gesellschaften

Bei Versorgern liegt das Netzgeschäft oft in einer eigenen Gesellschaft mit eigenem
Abschluss (evm mit enm). Dann bekommt jede Gesellschaft ihren Satz Input-Blätter mit
eigenem Kürzel, und `Overview FS` zeigt beide Blöcke untereinander.

**Nicht addieren.** Ohne Konsolidierung führt eine Summe zu Doppelzählungen bei
Innenumsätzen, Pacht und Ergebnisabführung. Die Blöcke stehen nebeneinander, die Folie sagt,
welche Gesellschaft gezeigt wird.

**Der Blindfleck.** Wo eine Tochter einen eigenen Abschluss hat, dessen Zahlen nicht
vorliegen, fehlt ihr Investitionsbedarf in der Darstellung. Bei Versorgern trifft das das
Stromnetz. Der Kapitalbedarf der Gruppe ist dann höher als gezeigt, und das gehört auf die
Investitionsfolie als Bullet und in den Report als Lücke.
