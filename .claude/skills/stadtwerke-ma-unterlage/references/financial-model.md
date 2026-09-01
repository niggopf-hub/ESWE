# Financial Model

Die Zahlen der Unterlage kommen aus einer Excel-Mappe, nicht aus dem Fließtext. Der Grund
ist praktisch: die Financial- und die Verschuldungsfolie sind die einzigen Stellen, an
denen der Adressat dich im Termin sofort widerlegen kann. Wenn dort eine Zahl wackelt,
wackelt der Rest der Unterlage mit.

## Inhalt

1. Architektur der Mappe
2. Farbkonvention
3. Kontrollzeilen
4. Blatt "Quellen & Hinweise"
5. Kennzahlendefinitionen
6. Was auf welche Folie geht
7. Wenn mehrere Gesellschaften abzubilden sind

---

## 1. Architektur

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

## 2. Farbkonvention

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

## 3. Kontrollzeilen

Am Ende von `Overview FS` ein Block `Kontrollen`. Jede Zeile muss null ergeben (oder
"n. v.", wo die Quelle nichts hergibt). **Solange eine Kontrolle nicht null ist, darf keine
Zahl auf eine Folie.**

| Kontrolle | Prüft |
|---|---|
| Aktiva ./. Passiva | Bilanz vollständig übertragen |
| Bilanzgewinn = 0 | Ergebnisverwendung korrekt abgebildet (bei EAV) |
| Berechneter ./. veröffentlichter Finanzmittelfonds | Kapitalflussrechnung schlüssig |
| EK-Quote berechnet ./. Lagebericht | eigene Definition trifft die des Unternehmens |
| Finanzmittelfonds ./. Kassenbestand laut Bilanz | Cashflow und Bilanz konsistent |

Die vierte ist die lehrreichste: Wenn die selbst berechnete EK-Quote von der im Lagebericht
genannten abweicht, rechnet das Unternehmen anders — etwa mit Ertragszuschüssen im
wirtschaftlichen Eigenkapital. Dann ist **die Definition des Unternehmens** zu übernehmen
und die Abweichung zu dokumentieren. Auf der Folie steht sonst eine Zahl, die der Vorstand
nicht wiedererkennt.

Kontrollen, die auf fehlende Daten treffen, mit `IF(ISNUMBER(...); ...; "n. v.")` abfangen,
statt sie leer zu lassen — eine leere Kontrollzelle sieht aus wie eine bestandene.

---

## 4. Blatt "Quellen & Hinweise"

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

## 5. Kennzahlendefinitionen

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
Cash-Pooling-Salden innerhalb des Stadtkonzerns sonst die Verschuldung verzerren. Wenn du
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

Zwei Fallstricke, die bei kommunalen Versorgern regelmäßig auftreten:

- **EAT vor Ergebnisabführung.** Wo ein Ergebnisabführungsvertrag besteht, ist der
  Jahresüberschuss nach Abführung nahe null und als Ertragsmaß wertlos. Die Ertragskraft
  steht im Ergebnis *vor* Abführung. Beide Größen zeigen und den Unterschied benennen.
- **Capex mit und ohne Finanzanlagen.** Der Erwerb einer Beteiligung ist keine
  Sachinvestition. Getrennt ausweisen, sonst entsteht ein Investitionspeak, der keiner ist.

---

## 6. Was auf welche Folie geht

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

## 7. Wenn mehrere Gesellschaften abzubilden sind

Bei Versorgern liegt das Netzgeschäft oft in einer eigenen Gesellschaft, die einen eigenen
Abschluss offenlegt. Dann bekommt jede Gesellschaft ihren eigenen Satz Input-Blätter mit
Präfix (`EVU Bilanz`, `Netz Bilanz`), und `Overview` zeigt beide Blöcke untereinander.

**Nicht addieren.** Ohne Konsolidierung führt eine Summe zu Doppelzählungen bei
Innenumsätzen, Pacht und Ergebnisabführung. Die Blöcke stehen nebeneinander, und die Folie
sagt, welche Gesellschaft gezeigt wird. Wo die Gruppengröße relevant ist, gehört ein
qualitativer Hinweis in eine Fußnote — keine addierte Zahl.
