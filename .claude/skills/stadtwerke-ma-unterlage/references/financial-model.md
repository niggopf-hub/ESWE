# Financial Model

Die Zahlen der Unterlage kommen aus einer Excel-Mappe, nicht aus dem Fließtext. Der Grund
ist praktisch: die Financial- und die Verschuldungsfolie sind die einzigen Stellen, an
denen der Adressat dich im Termin sofort widerlegen kann. Wenn dort eine Zahl wackelt,
wackelt der Rest der Unterlage mit.

## Inhalt

1. Analyseprofil — vor der ersten Zahl
2. Architektur der Mappe
3. Farbkonvention
4. Kontrollzeilen
5. Fehlende und gerundete Werte
6. Blatt "Quellen & Hinweise"
7. Kennzahlendefinitionen
8. Was auf welche Folie geht
9. Wenn mehrere Gesellschaften abzubilden sind

---

## 1. Analyseprofil — vor der ersten Zahl

Bevor eine Zahl abgeschrieben wird, wird schriftlich festgehalten, **was genau** dargestellt
wird. Ohne das entstehen Reihen, die in sich stimmen, aber nicht dasselbe messen — und der
Fehler fällt erst im Termin auf, wenn jemand eine Zahl aus einem älteren Stand danebenhält.

| Festlegung | Warum sie nicht offenbleiben darf |
|---|---|
| **Einzelabschluss oder Konzern** | Eine Stadtwerke-Holding wird sinnvoll als Konzern dargestellt, eine Vertriebs-AG mit Netztochter als Einzelabschluss. Die falsche Wahl zeigt die falsche wirtschaftliche Einheit — nicht bloß andere Zahlen. |
| **Zeitraum je Rechenwerk** | Bilanz, GuV und Kapitalflussrechnung reichen oft unterschiedlich weit zurück. Der Zeitraum wird erst festgelegt, wenn **alle** Quellen gesichtet sind, nicht vorher. |
| **Modellversion und Stand** | Welche Mappe gilt, mit Datum. Ältere Arbeitsstände kursieren weiter. |
| **Einheiten** | T€ im Modell, Mio. € auf den Folien. Die Umrechnung passiert an genau einer Stelle. |
| **Definition von Net Debt, EBITDA, Free Cashflow** | Alle drei sind nicht standardisiert (siehe Abschnitt 7). |
| **Verhältnis zu älteren Ständen** | Wenn eine Zahl von einem früheren Arbeitsstand abweicht, ist das erklärungsbedürftig. |

**Definitionsänderungen brauchen eine Überleitung, keine Fußnote.** Wenn eine Kennzahl
anders gerechnet wird als zuvor, gehört die Brücke ins Modell: alter Wert, jede einzelne
Änderung mit Betrag, neuer Wert. Zwei Beispiele, an denen das regelmäßig hängt:

- **Net Debt** einmal als Banken + Pensionen ./. Cash, einmal zusätzlich abzüglich
  Forderungen gegen verbundene Unternehmen. Beide Zahlen sind vertretbar; nebeneinander
  ohne Brücke sehen sie nach einem Fehler aus.
- **Free Cashflow** einmal als operativer plus Investitions-Cashflow, einmal als operativer
  Cashflow abzüglich operativem Capex. In derselben Periode kann die erste Größe positiv und
  die zweite negativ sein — mit gegensätzlicher Aussage für die Storyline. Welche gemeint
  ist, muss auf der Folie stehen, nicht nur im Modell.

Und: Ein Urteil nie auf ein einzelnes Jahr stützen. Ein Sonderjahr mit einem
Beteiligungsverkauf drückt den Verschuldungsfaktor auf einen Wert, der zwölf Monate später
nicht mehr gilt.

## 2. Architektur

Zwei Zonen, durch Trennerblätter sichtbar getrennt:

```
Cover
Output>>            ← Trenner
  Overview          Kennzahlenübersicht über alle Jahre
  Overview FS       genau die Blöcke, die auf die Folien gehen
Input>>             ← Trenner
  Bilanz            zeilengetreu aus dem Abschluss
  GuV               zeilengetreu aus dem Abschluss
  Kapitalflussrechnung
  KPIs              Absatzmengen, Kunden, Mitarbeiter, Netzlängen
  Capex             Investitionen nach Sparten
  Quellen & Hinweise
```

Die Trennung ist der Kern. **Input-Blätter transkribieren, Output-Blätter rechnen.** Wer
auf einem Input-Blatt rechnet oder auf einem Output-Blatt tippt, verliert die
Nachvollziehbarkeit — und damit den einzigen Zweck der Mappe.

**Input-Blätter** bilden die Gliederung des Abschlusses zeilengetreu ab, inklusive
Positionsnummern. Ein Jahr je Spalte. Die Gliederung folgt dem **jüngsten** Abschluss, weil
sich Bezeichnungen über die Jahre ändern; ältere Jahre werden darauf harmonisiert.
Positionen, die es in früheren Jahren nicht gab, mit 0 ansetzen — nicht die Zeile weglassen,
sonst verrutscht die Reihe.

**Output-Blätter** enthalten ausschließlich Verweise auf Input-Blätter plus daraus
berechnete Kennzahlen. `Overview FS` ist so aufgebaut, dass jeder Block einem Element auf
den Folien entspricht.

---

## 3. Farbkonvention

Bewährte Konvention aus dem Financial Modelling, hier durchgehend angewandt:

| Farbe | Bedeutung |
|---|---|
| **Blau** | Eingabewert, direkt aus dem Abschluss abgeschrieben |
| **Schwarz** | Formel innerhalb desselben Blattes |
| **Grün** | Verweis auf ein anderes Blatt |

Damit sieht jeder Leser in Sekunden, welche Zellen Handarbeit sind — und nur die müssen
gegen das PDF geprüft werden. **Sämtliche Zwischen- und Endsummen sind Formeln und nirgends
hartcodiert.** Eine hartcodierte Summe ist der häufigste stille Fehler in solchen Mappen:
sie stimmt beim Anlegen und ist nach der ersten Korrektur falsch.

Die Konvention gehört ins Blatt `Quellen & Hinweise`, sonst versteht sie beim nächsten Mal
niemand mehr.

---

## 4. Kontrollzeilen

Am Ende von `Overview FS` ein Block `Kontrollen`. **Solange eine Kontrolle ungeklärt ist,
darf keine Zahl auf eine Folie.** Geklärt heißt: null, oder eine benannte und begründete
Differenz — nicht jede Abweichung ist ein Fehler.

| Kontrolle | Prüft |
|---|---|
| Aktiva ./. Passiva | Bilanz vollständig übertragen |
| Bilanzgewinn = 0 | Ergebnisverwendung korrekt abgebildet (bei EAV) |
| Berechneter ./. veröffentlichter Finanzmittelfonds | Kapitalflussrechnung schlüssig |
| EK-Quote berechnet ./. Lagebericht | eigene Definition trifft die des Unternehmens |
| Summe der Einzelposten ./. ausgewiesene Summe | Übertragungsfehler gegen Rundung abgegrenzt |

### Der Finanzmittelfonds ist keine Bilanzposition

Die naheliegende Kontrolle — Finanzmittelfonds gegen Kassenbestand laut Bilanz — **gilt
nicht allgemein.** Sie geht nur auf, wenn das Unternehmen den Fonds ausdrücklich als reine
Bankguthaben definiert. Viele Versorger und praktisch alle Stadtkonzerne rechnen anders,
insbesondere mit kurzfristigen Kassenkrediten als **Abzugsposten**:

```
  Kassenbestand und Guthaben bei Kreditinstituten
+ kurzfristige Liquiditätsanlagen
− kurzfristig fällige Kassenkredite
= Finanzmittelfonds
```

Bei einem Konzern mit ausgenutzten Kontokorrentlinien wird der Fonds so **negativ**, während
die Bilanz einen positiven Kassenbestand zeigt. Wer hier eine Nullkontrolle erzwingt,
erzeugt eine Differenz in zweistelliger Millionenhöhe und hält eine erklärte
Definitionsdifferenz für einen Übertragungsfehler.

**Richtig ist deshalb:** Die veröffentlichte Fondsdefinition im Modell **nachbauen** und die
Überleitung als eigene Zeilen führen — Bilanzliquidität, kurzfristige Anlagen, einbezogene
Kassenkredite, Ergebnis. Erst die Differenz zwischen **selbst gerechnetem** und
**veröffentlichtem** Fonds muss null ergeben. Die Definition steht in den Erläuterungen zur
Kapitalflussrechnung; sie ist bei jedem Fall neu zu lesen und kann sich zwischen Jahren
ändern.

Dieselbe Vorsicht gilt für jede Kontrolle: Sie prüft die **Übertragung**, nicht die
Definition. Wo eine Kontrolle eine Definitionsdifferenz aufdeckt, wird die Definition
übernommen und die Differenz dokumentiert — nicht die Quelle stillschweigend angepasst,
damit ein Test besteht.

## 5. Fehlende und gerundete Werte

Die häufigste stille Verfälschung entsteht nicht beim Rechnen, sondern beim Umgang mit
Lücken. Eine leere Zelle mit null zu füllen, macht aus einer Unbekannten eine Aussage.

**Vier Fälle, vier Kennzeichnungen — nie zusammenwerfen:**

| Fall | Kennzeichen | Bedeutung |
|---|---|---|
| Tatsächlich null | `0` | Die Position existiert und beträgt null |
| Nicht gesondert ausgewiesen | `n. a.` | Existiert, steckt aber in einer Sammelposition |
| In anderer Position enthalten | `→ Pos. X` | Mit Verweis, wo sie steckt |
| Nicht verfügbar | `n. v.` | Die Quelle beziffert es nicht |

Für die Zeitreihe heißt das: Eine Position, die es in früheren Jahren nicht gab, wird **nicht
pauschal auf null gesetzt**. Erst prüfen, ob sie fehlt, null ist oder woanders steckt — und
das im Blatt `Quellen & Hinweise` festhalten. Nur der erste Fall geht in Summen ein.

**Rundung.** Veröffentlichte Zahlen sind gerundet. Drei Positionen zu je 33,3 ergeben
rechnerisch 99,9, während die ausgewiesene Summe 100,0 lautet. Das ist kein Fehler.
Deshalb drei getrennte Felder je Summenzeile:

- der **Quellwert** (so, wie er im Abschluss steht),
- die **errechnete Summe** aus den Einzelposten,
- die **Differenz**, mit Toleranz.

Als Toleranz gilt: die halbe Anzeigeeinheit mal Anzahl der Summanden — bei fünf Positionen
in T€ also 2,5 T€. Innerhalb der Toleranz ist die Differenz Rundung und wird nur vermerkt.
Darüber ist sie aufzuklären. **Auf der Folie steht der Quellwert.** Einzelposten werden
niemals angepasst, damit eine Summe aufgeht.

Die Regel „Summen sind Formeln, nie hartcodiert" bleibt bestehen — sie betrifft die
errechnete Summe. Der Quellwert ist ein Eingabewert und als solcher blau. Beide stehen
nebeneinander; das ist der Unterschied zwischen Transkribieren und Rechnen.

## 6. Blatt "Quellen & Hinweise"

Der Prüfpfad der Mappe. Ohne dieses Blatt ist die Arbeit nach zwei Wochen nicht mehr
reproduzierbar. Es enthält:

- **Gesellschaft** mit Registergericht und Nummer
- **Quelle** der Abschlüsse
- **Je Abschluss:** Geschäftsjahr, Tag der Erstellung/Offenlegung, und **welche Jahre er
  liefert** (jeder Abschluss liefert GJ und Vorjahr)
- **Abgrenzung:** welcher Abschluss dargestellt ist, was ausdrücklich nicht enthalten ist
  (Tätigkeitsabschlüsse nach § 6b EnWG, Konzernabschluss), und warum
- **Farbkonvention**
- **Abweichungen**, durchnummeriert, je mit Fundstelle (Abschluss, Seite, Position), beiden
  Werten und der Entscheidung, welcher angesetzt wurde und warum
- **Gliederungsharmonisierung:** welche Positionen in früheren Jahren fehlten und wie sie
  behandelt wurden

Die Abweichungen sind der eigentliche Wert. Beispiele für den Typ von Eintrag, der sich im
Termin auszahlt: eine Position, deren ausgewiesene Summe um eine Einheit von der Rechnung
abweicht und die im Folgejahresabschluss anders beziffert ist; eine Kapitalflussrechnung,
die zwei Abschlüsse unterschiedlich aufteilen bei identischer Gesamtsumme; ein Jahr, für
das der Cashflow nur qualitativ beschrieben und nicht beziffert wurde.

---

## 7. Kennzahlendefinitionen

Nicht standardisiert, deshalb einmal festlegen, im Modell dokumentieren und auf der Folie
in einer Fußnote nennen.

**Net Debt** — die wichtigste und am wenigsten standardisierte Größe:

```
  Finanzverbindlichkeiten
+ Pensionsrückstellungen
+ Verbindlichkeiten gegenüber verbundenen/assoziierten Unternehmen
− liquide Mittel
− Forderungen gegen verbundene/assoziierte Unternehmen
```

Pensionsrückstellungen gehören hinein, weil sie bei kommunalen Versorgern erheblich sind
und wie Fremdkapital wirken. Verbundene Unternehmen werden **saldiert**, weil
Cash-Pooling-Salden innerhalb des Stadtkonzerns sonst die Verschuldung verzerren.

**Vorsicht bei Ergebnisabführungsvertrag.** Wo ein EAV besteht, stecken die noch nicht
gezahlte Gewinnabführung und die Ausgleichszahlung an den Minderheitsgesellschafter in den
Verbindlichkeiten gegenüber verbundenen und Beteiligungsunternehmen. Nach der Formel oben
wandern sie damit in die Nettoverschuldung — obwohl sie Ergebnisverwendung sind und kein
Fremdkapital. Der Faktor wird dadurch systematisch zu hoch. Praktikabel ist, eine engere
Definition auf die Folie zu nehmen (Bankverbindlichkeiten + Pensionsrückstellungen ./.
liquide Mittel) und die weitere Definition in der Fußnote mitzugeben. Wichtig ist nur, dass
die gewählte Definition über alle Jahre gleich gerechnet und offen genannt ist. Wenn du
von dieser Definition abweichst, muss die Fußnote das sagen — und die Reihe muss über alle
Jahre konsistent gerechnet sein.

**Weitere Größen:**

| Kennzahl | Definition |
|---|---|
| Rohertrag | Gesamtleistung ./. Materialaufwand |
| Rohertragsmarge | Rohertrag / Umsatz |
| EBITDA | Betriebsergebnis + Abschreibungen |
| EBIT | Betriebsergebnis |
| EAT | Ergebnis nach Steuern, **vor** Ergebnisabführung |
| Net Debt / EBITDA | Verschuldungsfaktor |
| EK-Quote | Eigenkapital / Bilanzsumme — Definition des Unternehmens prüfen |
| Capex | Investitionen in Sach- und immaterielles Anlagevermögen; Finanzanlagen getrennt |

Drei Fallstricke, die bei kommunalen Versorgern regelmäßig auftreten:

- **EBITDA mit oder ohne Beteiligungsergebnis.** Wo ein erheblicher Teil des Ergebnisses aus
  Beteiligungen stammt — bei Querverbund-Versorgern oft die Hälfte des Vorsteuerergebnisses —
  klaffen die Definitionen weit auseinander: das Unternehmen rechnet das Beteiligungsergebnis
  häufig ein, die Deck-Konvention (Betriebsergebnis + Abschreibungen) lässt es draußen. Der
  Unterschied schlägt voll auf den Verschuldungsfaktor durch und kann ihn glatt halbieren.
  Beide Reihen rechnen, auf der Folie eine zeigen, die andere in die Fußnote — und die
  Entscheidung, welche nach vorn gehört, mit dem Nutzer abstimmen. Nur eine Reihe zu zeigen
  macht die Folie angreifbar, sobald der Adressat mit seiner eigenen Definition gegenrechnet.

- **EAT vor Ergebnisabführung.** Wo ein Ergebnisabführungsvertrag besteht, ist der
  Jahresüberschuss nach Abführung nahe null und als Ertragsmaß wertlos. Die Ertragskraft
  steht im Ergebnis *vor* Abführung. Beide Größen zeigen und den Unterschied benennen.
- **Capex mit und ohne Finanzanlagen.** Der Erwerb einer Beteiligung ist keine
  Sachinvestition. Getrennt ausweisen, sonst entsteht ein Investitionspeak, der keiner ist.

### Wo die Kennzahlen ihre Aussage verlieren

Zwei Fälle, in denen eine formal korrekt gerechnete Zahl auf der Folie irreführt:

- **Net Debt / EBITDA bei EBITDA nahe null oder negativ.** Der Quotient explodiert oder
  wechselt das Vorzeichen und suggeriert eine Aussage, die er nicht trägt. Regel: Bei
  EBITDA ≤ 0 wird der Faktor **nicht ausgewiesen** (`n. m.` für nicht aussagekräftig), und
  der Kommentar sagt in einem Satz, warum. Auch bei sehr kleinem positivem EBITDA — Faustwert
  unter einem Zehntel des Net Debt — gehört der Wert eingeordnet statt bloß gezeigt.
- **CAGR bei ungeeignetem Ausgangswert.** Eine Wachstumsrate über einen Zeitraum, dessen
  erstes Jahr ein Ausreißer war, misst den Ausreißer, nicht das Wachstum. Bei negativem oder
  nahe null liegendem Ausgangswert ist sie mathematisch nicht definiert beziehungsweise
  sinnlos. Regel: CAGR nur über Zeiträume, deren Randjahre beide normal sind; sonst die
  Reihe zeigen und die Bewegung im Kommentar beschreiben.

In beiden Fällen ist das Weglassen die stärkere Wahl. Eine fehlende Kennzahl fällt auf und
lässt sich erklären; eine irreführende wird geglaubt.

---

## 8. Was auf welche Folie geht

`Overview FS` ist so gegliedert, dass jeder Block einem Folienelement entspricht:

| Block in `Overview FS` | Folie |
|---|---|
| Ertragslage (Umsatz, Rohertrag, Margen, EBITDA, Capex) | 2.5, GuV-Teil |
| Cashflows (operativ, Investitions-, Finanzierungs-, Total) | 2.5, Cashflow-Teil |
| Bilanzpositionen (Kassenbestand, Net Debt, EK-Quote) | 2.5, Bilanz-Teil |
| Umsatzaufteilung | 2.2, Ring |
| Entwicklung der Verschuldung (Net Debt, Net Debt/EBITDA) | 2.4, links |
| KPIs (Kunden, Netzlängen, Mitarbeiter) | 2.2, Kacheln |

**Einheiten:** im Modell durchgehend T€ (so stehen sie im Abschluss), auf den Folien Mio. €.
Die Umrechnung passiert an genau einer Stelle im Output-Blatt, nie auf der Folie. Gemischte
Einheiten innerhalb einer Mappe sind die häufigste Ursache für Zahlendreher um Faktor 1000.

---

## 9. Wenn mehrere Gesellschaften abzubilden sind

Bei Versorgern liegt das Netzgeschäft oft in einer eigenen Gesellschaft, die einen eigenen
Abschluss offenlegt. Dann bekommt jede Gesellschaft ihren eigenen Satz Input-Blätter mit
Präfix (`EVU Bilanz`, `Netz Bilanz`), und `Overview` zeigt beide Blöcke untereinander.

**Der Blindfleck, den das erzeugt.** Wo eine Tochter einen eigenen Abschluss hat, dessen
Zahlen aber nicht vorliegen, fehlt ihr Investitionsbedarf vollständig in der Darstellung.
Bei Versorgern trifft das typischerweise das Stromnetz: die Netzgesellschaft trägt die
größten Investitionen der nächsten Jahre, und der Einzelabschluss der Mutter zeigt davon
nichts. Der tatsächliche Kapitalbedarf der Gruppe ist dann höher als das, was auf der Folie
steht — und das gehört ausdrücklich gesagt, in einer Fußnote oder einem Kommentarsatz.
Sonst argumentiert die Unterlage gegen sich selbst: der Adressat weiß, was in seiner
Netztochter liegt.

**Nicht addieren.** Ohne Konsolidierung führt eine Summe zu Doppelzählungen bei
Innenumsätzen, Pacht und Ergebnisabführung. Die Blöcke stehen nebeneinander, und die Folie
sagt, welche Gesellschaft gezeigt wird. Wo die Gruppengröße relevant ist, gehört ein
qualitativer Hinweis in eine Fußnote — keine addierte Zahl.
