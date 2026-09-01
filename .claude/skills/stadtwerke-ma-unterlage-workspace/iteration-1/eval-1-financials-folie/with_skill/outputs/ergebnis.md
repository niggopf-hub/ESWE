# Financial-Folie ESWE Versorgungs AG

Folie 2.5 („Financials", Deck-Position 16) plus den Verschuldungs-Baustein für Folie 2.4.
Alle Zahlen stammen aus dem Financial Model, nicht aus dem Fließtext.

---

## 0 · Materialstand und Lücken

| Material | Im Projekt | Bemerkung |
|---|---|---|
| Jahres-/Tätigkeitsabschlüsse 2021–2024 | ja | `Wiesbaden_HRB_2105_27.08.2026*.pdf` — vier Auszüge aus dem Unternehmensregister (Erstellung 13.02.2023 / 29.02.2024 / 03.02.2025 / 16.01.2026); liefern zusammen GJ 2020–2024 |
| Geschäftsbericht 2025 | ja | `Geschaeftsbericht-25.pdf` — enthält den **vollständigen geprüften Jahresabschluss 2025** (Bilanz S. 73, GuV S. 74, Anhang S. 75–86, Bestätigungsvermerk KPMG S. 87), nicht nur den Lagebericht |
| Financial Model | ja | `ESWE_Versorgungs_AG_Jahresabschluss_2020-2024.xlsx` — Bilanz, GuV, KFR, Overview FS, Quellen & Hinweise; **ohne** Rohertrag, EBITDA-Marge, Capex, Net Debt und ohne GJ 2025 |
| Referenzunterlage | teilweise | `20240305_Stadtwerke Duisburg_v4 1 (1).pptx` (Metzler, mit Financial-Folie 14) — verwendbar als Template. `20260813_Metzler_evm AG_vF.pdf` liegt **nur als PDF** vor; für Schritt 5 wird die .pptx gebraucht |
| Handelsregister | ja | HRB 2105, AG Wiesbaden — Gesellschafter und Grundkapital im Anhang bestätigt |

**Lücke, die den Bogen betrifft:** Es gibt **keine bezifferte Investitionssumme mit Horizont.**
Der Lagebericht 2025 sagt wörtlich nur: „Das Investitionsvolumen wird sich in den nächsten
Jahren nochmals erheblich steigern." Siehe Rückfrage 2.

**Quelldateien:** unverändert. Die Modellerweiterung liegt als neue Version daneben:
**`ESWE_Versorgungs_AG_Financial_Model_2020-2025_v2.xlsx`** (im selben Ordner wie diese Datei) —
das ist der maßgebliche Stand. Die ebenfalls dort liegende `modell_erweitert_2020-2025.xlsx` ist
ein früherer Zwischenstand desselben Modells; ihr fehlt die aktualisierte Fassung des Blattes
`Quellen & Hinweise` mit den acht dokumentierten Abweichungen. Sie kann gelöscht werden.

---

## 1 · Was am Modell ergänzt wurde (Schritt 3)

Neues Input-Blatt **`Anhang & Capex`** (Net-Debt-Komponenten und Investitionen nach Bereichen,
zeilengetreu aus den Anhangangaben (3), (5), (6) und der Investitionsübersicht der Lageberichte),
Spalte **2025** in Bilanz, GuV und Kapitalflussrechnung, `Overview FS` um Gesamtleistung,
Rohertrag, Margen, EBITDA, Capex, Free Cash Flow und den kompletten Net-Debt-Block erweitert.
Farbkonvention (blau = Eingabe, schwarz = Formel, grün = Verweis) durchgehalten, keine
hartcodierte Summe.

### Kontrollzeilen — Zwischenstopp vor der Folie

| Kontrolle | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|
| Bilanz: Aktiva ./. Passiva | 0 | 0 | 0 | 0 | 0 |
| GuV: Bilanzgewinn | 0 | 0 | 0 | 0 | 0 |
| KFR: berechneter ./. veröffentlichter Fonds | 0,0 | 0,0 | 0,0 | 0,0 | 0,0 |
| Finanzmittelfonds ./. Kassenbestand lt. Bilanz | 0,0 | 0,0 | 0,0 | 0,0 | 0,0 |
| EK-Quote: berechnet ./. Lagebericht (%-Punkte) | 0,0 | 0,0 | 0,0 | 0,0 | 0,0 |
| Gesamtinvestitionen: Bereiche ./. ausgewiesene Summe | 0 | 0 | 0 | 0 | 0 |
| Net Debt: Herleitung ./. Komponenten | 0 | 0 | 0 | 0 | 0 |
| Verbindlichkeiten: Anhang ./. Bilanz (T€) | 0 | 0 | 0 | **1** | 0 |

Die eine Einheit in 2024 ist echt und bewusst nicht geglättet: die Einzelposten des Anhangs (6)
im JA 2024 summieren sich auf 212.875 T€, ausgewiesen und bilanziert sind 212.874 T€.
Dokumentiert als Abweichung 5 im Blatt `Quellen & Hinweise`; angesetzt ist der Bilanzwert.

### Kennzahlenübersicht zum Plausibilisieren (Mio. EUR)

| | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|
| Umsatz | 426,5 | 475,7 | 634,1 | 534,7 | 473,8 |
| Rohertrag | 118,2 | 123,6 | 152,8 | 150,2 | 134,4 |
| EBITDA | 34,6 | 50,8 | 57,5 | 88,9 | 45,2 |
| Capex (inkl. Finanzanlagen) | 43,2 | 53,7 | 27,3 | 27,5 | 37,0 |
| Net Debt | 98,1 | 104,0 | 99,1 | 156,2 | 163,7 |
| Net Debt / EBITDA | 2,8x | 2,0x | 1,7x | 1,8x | 3,6x |
| EK-Quote | 30,3 % | 27,8 % | 26,3 % | 27,6 % | 28,5 % |
| Operating / Investing / Financing CF | 49,0 / (19,5) / (28,9) | 78,0 / (34,0) / (17,0) | 47,3 / 8,9 / (41,8) | 68,2 / (5,0) / (86,7) | 42,7 / (8,3) / (53,4) |

**Zeitraum 2021–2025** statt 2020–2024, aus zwei Gründen: für 2020 ist der operative Cashflow
nicht veröffentlicht (der JA 2021 beziffert ihn nicht), und 2025 ist das Normalisierungsjahr,
das die Argumentation trägt. 2020 bleibt im Modell vollständig erhalten. Siehe Rückfrage 4.

---

## 2 · Die Folie

Aufbau folgt Folie 14 der Duisburg-Unterlage (Layout `1_Inhalt_0`): Tabelle links,
nummerierte Kommentar-Marker, Kommentarspalte rechts, Kernaussagenkasten darunter.
Platzhalter-Indizes in Klammern.

### Aussagentitel (ph:0)

> **Nach dem sondereffektgeprägten Rekordjahr 2024 normalisiert sich die Ertragslage 2025 auf
> robustem Niveau − die Nettoverschuldung erreicht mit 163,7 Mio. EUR jedoch das 3,6-fache EBITDA**

### Kapitelnummer (ph:10) · Kapitelkolumne (ph:13) · Bereichsüberschrift (ph:12)

- ph:10 — `2`
- ph:13 — `2. Übersicht und Herausforderungen ESWE Versorgungs AG`
- ph:12 — `ESWE Versorgungs AG (HGB-Einzelabschluss)`

### Tabelle (Table, 7 Spalten × 35 Zeilen)

```
(in Mio. EUR)                         │    │   2021   │   2022   │   2023   │   2024   │   2025
──────────────────────────────────────┼────┼──────────┼──────────┼──────────┼──────────┼──────────
GuV                                   │    │          │          │          │          │
Umsatz                                │ ①  │    426,5 │    475,7 │    634,1 │    534,7 │    473,8
%-Wachstum                            │    │    9,2 % │   11,5 % │   33,3 % │ (15,7 %) │ (11,4 %)
                                      │    │          │          │          │          │
Gesamtleistung                        │    │    429,6 │    479,9 │    636,7 │    537,4 │    476,2
                                      │    │          │          │          │          │
Rohertrag                             │    │    118,2 │    123,6 │    152,8 │    150,2 │    134,4
Rohertrag-Marge                       │    │   27,7 % │   26,0 % │   24,1 % │   28,1 % │   28,4 %
                                      │    │          │          │          │          │
EBITDA ³⁾                             │ ②  │     34,6 │     50,8 │     57,5 │     88,9 │     45,2
EBITDA-Marge                          │    │    8,1 % │   10,7 % │    9,1 % │   16,6 % │    9,5 %
                                      │    │          │          │          │          │
EBIT                                  │    │     20,4 │     36,3 │     42,9 │     73,3 │     28,7
EBIT-Marge                            │    │    4,8 % │    7,6 % │    6,8 % │   13,7 % │    6,1 %
                                      │    │          │          │          │          │
Beteiligungsergebnis                  │    │     24,5 │     17,6 │     30,5 │     17,8 │     25,1
EBT ²⁾                                │    │     44,1 │     51,8 │     74,7 │     84,3 │     52,7
                                      │    │          │          │          │          │
EAT ¹⁾                                │    │     40,7 │     48,2 │     70,6 │     78,3 │     48,9
EAT-Marge                             │    │    9,6 % │   10,1 % │   11,1 % │   14,6 % │   10,3 %
                                      │    │          │          │          │          │
Einstellung in Gewinnrücklagen        │    │        – │        – │   (10,0) │        – │        –
Ausgleichszahlung Thüga AG            │ ③  │   (16,3) │   (17,3) │   (21,1) │   (29,8) │   (18,8)
Gewinnabführung WVV Holding           │    │   (24,4) │   (30,9) │   (39,5) │   (48,5) │   (30,1)
Bilanzgewinn                          │    │      0,0 │      0,0 │      0,0 │      0,0 │      0,0
                                      │    │          │          │          │          │
Kapitalflussrechnung ⁶⁾               │    │          │          │          │          │
Operating Cash Flow                   │ ④  │     49,0 │     78,0 │     47,3 │     68,2 │     42,7
Investing Cash Flow                   │ ⑤  │   (19,5) │   (34,0) │      8,9 │    (5,0) │    (8,3)
Financing Cash Flow                   │    │   (28,9) │   (17,0) │   (41,8) │   (86,7) │   (53,4)
Free Cash Flow                        │    │     29,5 │     44,0 │     56,2 │     63,2 │     34,4
Total Cash Flow                       │    │      0,6 │     27,0 │     14,4 │   (23,5) │   (19,0)
                                      │    │          │          │          │          │
Investitionen (inkl. Finanzanlagen)⁵⁾ │    │     43,2 │     53,7 │     27,3 │     27,5 │     37,0
   davon Finanzanlagen                │    │     14,2 │     24,0 │      1,9 │      2,2 │      5,2
                                      │    │          │          │          │          │
Bilanzpositionen                      │    │          │          │          │          │
Kassenbestand                         │    │      3,6 │     30,6 │     45,0 │     21,5 │      2,5
Net Debt ⁴⁾                           │ ⑥  │     98,1 │    104,0 │     99,1 │    156,2 │    163,7
Net Debt / EBITDA                     │    │     2,8x │     2,0x │     1,7x │     1,8x │     3,6x
Eigenkapital-Quote                    │    │   30,3 % │   27,8 % │   26,3 % │   27,6 % │   28,5 %
```

Zwei bewusste Abweichungen vom Duisburg-Layout, beide sachlich begründet:

- **`Investing / Gesamtleistung` ersetzt durch die Investitionszeilen.** Der Investing Cash
  Flow der ESWE ist keine Investitionsgröße — er saldiert die im Investitionsbereich
  ausgewiesenen Beteiligungserträge und wird 2023 dadurch positiv. Eine Quote daraus wäre
  irreführend.
- **`EBT` ergänzt.** ESWE steuert laut Lagebericht mit EBT, Betriebsergebnis und
  Beteiligungsergebnis, nicht mit EBITDA. Wer nur EBITDA zeigt, spricht nicht die Sprache des
  Adressaten; die Verschuldungsrelation braucht EBITDA trotzdem.

### Kommentarspalte — Überschrift (ph:19) `Kommentare`, Text (Content Placeholder)

> **①** Der Umsatz geht 2025 preis- und mengenbedingt um 11,4 % auf 473,8 Mio. EUR zurück; die
> Rohertrag-Marge verbessert sich zugleich auf 28,4 % (2023: 24,1 %), weil der Materialaufwand
> mit 45,4 Mio. EUR stärker sinkt als die Erlöse.

> **②** Das Ergebnis 2024 ist maßgeblich durch Sondereffekte getragen: periodenfremde Erträge
> von 25,6 Mio. EUR, davon 20,6 Mio. EUR aus der Auflösung von Rückstellungen (Wasserkartell­
> verfahren, Drohverlustrückstellungen), gegenläufig 9,0 Mio. EUR Abschreibungen auf
> Finanzanlagen (MHKW-Ausleihung 6,5; BioEnergie 2,1). 2025 betragen die periodenfremden
> Erträge 5,3 Mio. EUR — das EBITDA von 45,2 Mio. EUR liegt wieder auf dem Niveau von 2022.

> **③** Das Ergebnis fließt vertraglich vollständig ab: Ausgleichszahlung an die Thüga AG und
> Gewinnabführung an die WVV summieren sich 2025 auf 48,9 Mio. EUR (2024: 78,3 Mio. EUR); der
> Bilanzgewinn ist definitionsgemäß null. Thesaurierung findet nur über Beschluss statt
> (2023: 10,0 Mio. EUR Rücklageneinstellung, 2025: 10,0 Mio. EUR Einzahlung in die Kapital­
> rücklage durch beide Gesellschafter).

> **④** Die Schwankungen des operativen Cash Flows sind überwiegend Working-Capital- und
> Timing-Effekte: die 78,0 Mio. EUR in 2022 gehen laut Lagebericht auf die Erstattung der
> Dezember-Soforthilfe durch die KfW und den Abbau der Verbrauchsabgrenzung zurück, der
> Rückgang auf 42,7 Mio. EUR in 2025 auf das niedrigere Jahresergebnis.

> **⑤** Der positive Investing Cash Flow 2023 (+8,9 Mio. EUR) ist kein Investitionsstopp: er
> enthält laut Lagebericht vor allem höhere Beteiligungserträge — u. a. die KMW-Ausschüttung
> von 24,0 Mio. EUR — bei zugleich geringeren Anlagenzugängen. Die tatsächlichen Investitionen
> liegen 2023 bei 27,3 Mio. EUR und steigen 2025 auf 37,0 Mio. EUR, davon 31,8 Mio. EUR in
> Sachanlagen (Fernwärme- und Wassernetz).

> **⑥** Net Debt steigt seit 2023 um 64,6 Mio. EUR auf 163,7 Mio. EUR; der Verschuldungsfaktor
> springt von 1,7x auf 3,6x, weil zugleich das EBITDA auf Normalniveau zurückkehrt. Der
> Finanzmittelfonds sinkt von 45,0 Mio. EUR (2023) auf 2,5 Mio. EUR, die freien Kreditlinien
> von 37,1 Mio. EUR sind unverändert nicht gezogen. Die Eigenkapitalquote hält sich nur durch
> die Kapitalerhöhung von 10 Mio. EUR bei 28,5 % (Zielwert des Unternehmens: dauerhaft > 25 %).

### Kernaussagenkasten (TextBox unterhalb der Kommentare)

> **2025 stehen einem operativen Cash Flow von 42,7 Mio. EUR Investitionen von 37,0 Mio. EUR und
> vertragliche Abführungen an die Gesellschafter von 48,9 Mio. EUR gegenüber — das laut
> Lagebericht „nochmals erheblich" steigende Investitionsvolumen scheint auf dieser Basis nicht
> aus dem operativen Cash Flow finanzierbar zu sein**

Sobald die Investitionssumme mit Horizont vorliegt (Rückfrage 2), tritt an die Stelle von
„das laut Lagebericht ‚nochmals erheblich' steigende Investitionsvolumen" die Formulierung des
Hauses: *„Das Investitionsvolumen von ‹Summe› bis ‹Jahr› scheint nicht aus dem operativen Cash
Flow finanzierbar zu sein."*

### Quellenzeile (ph:14)

> Quellen: eigene Recherche, Jahres- und Tätigkeitsabschlüsse nach EnWG der ESWE Versorgungs AG
> 2021–2024 (Unternehmensregister, AG Wiesbaden HRB 2105), Geschäftsbericht 2025 mit
> Jahresabschluss zum 31. Dezember 2025, Unternehmenswebsite

### Fußnotenzeile (ph:15)

> 1) EAT = Unternehmensergebnis nach Steuern, vor Ausgleichszahlung und Gewinnabführung
> 2) EBT laut Gewinn- und Verlustrechnung; der Lagebericht nennt als „Unternehmensergebnis vor
>    Ertragsteuern" das Ergebnis nach sonstigen Steuern (2024: 83,8; 2025: 52,4 Mio. EUR)
> 3) EBITDA = Betriebliches Ergebnis + Abschreibungen auf immaterielle Vermögensgegenstände und
>    Sachanlagen, ohne Beteiligungsergebnis; inklusive Beteiligungsergebnis beträgt
>    Net Debt / EBITDA 2025 2,3x (2023: 1,1x)
> 4) Net Debt = Verbindlichkeiten gegenüber Kreditinstituten + Pensionsrückstellungen +
>    Verbindlichkeiten gegenüber verbundenen Unternehmen und Unternehmen mit
>    Beteiligungsverhältnis ./. liquide Mittel ./. Forderungen gegen dieselben; enthält damit die
>    zum Stichtag noch nicht ausgezahlte Ausgleichszahlung (31.12.2024: 29,8; 31.12.2025:
>    18,8 Mio. EUR); empfangene Ertragszuschüsse sind nicht enthalten
> 5) Investitionen = Gesamtinvestitionen laut Lagebericht inklusive Finanzanlagen; mit dem
>    Investing Cash Flow nicht vergleichbar, da dieser vereinnahmte Beteiligungserträge enthält
> 6) Cash Flow 2022 in der Fassung des Jahresabschlusses 2023 (Umgliederung gegenüber dem
>    Jahresabschluss 2022 bei identischer Summe von 27,0 Mio. EUR)

---

## 3 · Verschuldungs-Baustein für Folie 2.4 (linke Hälfte)

```
Kategorien:            2021     2022     2023     2024     2025
Säulen "Net Debt"      98,1    104,0     99,1    156,2    163,7      (Mio. EUR)
Über den Säulen:       2,8x     2,0x     1,7x     1,8x     3,6x      ← Net Debt / EBITDA
Legende:               ■ Net Debt ⁴⁾     ─ Net Debt / EBITDA ³⁾
```

Als think-cell-Objekt aus der Duisburg-Folie 13 übernehmen und nur die Datenwerte im
think-cell-Datenblatt aktualisieren — nicht programmatisch neu bauen.

**Kernsatz im Kasten (Folie 2.4):**

> **Die Verschuldung ist mit 2,3x EBITDA inklusive Beteiligungsergebnis weiterhin tragfähig, hat
> sich seit 2023 jedoch um 64,6 Mio. EUR auf 163,7 Mio. EUR erhöht und reduziert den finanziellen
> Spielraum für das Investitionsprogramm von ‹Summe bis Jahr›**

Der Faktor von 3,6x auf Basis des reinen EBITDA liegt über der 3x-Marke und gehört
kommentiert, nicht nur gezeigt — deshalb steht die Einordnung in Kommentar ⑥ und in Fußnote 3.
Zwei Drittel des Anstiegs 2023 → 2024 sind Stichtagseffekte, keine neue Kreditaufnahme:
Verbindlichkeiten aus Gewinnabführung und Ausgleichszahlung +23,6 Mio. EUR, Kassenabbau
+23,4 Mio. EUR, neue Bankdarlehen nur +9,2 Mio. EUR. Das gehört ins Gespräch, nicht auf die
Folie — es entwertet die Aussage nicht, aber der Vorstand wird darauf zeigen.

---

## 4 · Rückfragen — hier entscheidest du, nicht ich

Der Skill trennt Mechanik von Urteil. Sieben Punkte, die ich nicht selbst setzen kann:

1. **Adressat und Anlass.** Vorstand, Aufsichtsrat, die Stadt/WVV — oder die Thüga? Erstkontakt
   oder Fortsetzung? Besonderheit ESWE: mit der Thüga AG (49,38 %) sitzt bereits ein privater
   strategischer Partner am Tisch. Die Einbindung privaten Kapitals ist damit kein Tabubruch,
   sondern eine Fortsetzung — das ändert die Tonlage von Kapitel 3 erheblich und wirkt auf den
   Titel dieser Folie zurück.

2. **Investitionssumme mit Horizont — die Achse des ganzen Bogens.** Der Lagebericht beziffert
   das Programm nicht. Ohne Zahl in Kapitel 2.1 trägt der Bogen laut `storyline.md` nicht
   vollständig; der Kernsatz dieser Folie bleibt bis dahin qualitativ. Drei Wege: (a) aus dem
   Ratsinformationssystem und der 2026 beschlossenen Kommunalen Wärmeplanung eine
   Größenordnung ableiten, (b) über die Anschlussleistung des MHKW und die Fernwärme-Ausbaupläne
   rechnen, (c) den Bogen auf das offenkundige Muster umstellen: Investitionen +35 % in einem
   Jahr, Liquidität von 45,0 auf 2,5 Mio. EUR, Verschuldungsfaktor 1,7x → 3,6x. Option (c)
   trägt auch ohne Planzahl, ist aber eine andere Folie.

3. **Bewertungsnarrativ.** Meine Einordnung — 2023/2024 sondereffektgetragen, 2025 normalisiert
   auf robustem Niveau, Mittelfristplanung laut Lagebericht bis 2030 „stabil", aber unter den
   Sonderjahren — ist eine Wertung, keine Ableitung. Bitte bestätigen oder korrigieren.

4. **Zeitraum 2021–2025 statt 2020–2024.** Begründung oben; die Alternative ist im Modell
   vollständig vorhanden, es ist nur die Spaltenauswahl im Output-Blatt.

5. **EBITDA-Definition.** Ohne Beteiligungsergebnis (Skill-Definition) springt der Faktor 2025
   auf 3,6x; mit Beteiligungsergebnis — bei einem Querverbund mit Ergebnisabführungsverträgen
   der sw netz und WiTCOM und der KMW-Ausschüttung durchaus vertretbar — auf 2,3x. Beide
   stehen im Modell. Welche Fassung soll auf die Folie, welche in die Fußnote?

6. **Steuerungskennzahlen.** ESWE steuert mit EBT, Betriebsergebnis, Beteiligungsergebnis,
   Ergebnis vor Ausgleichszahlung und Abführung sowie EK-Quote. Soll die Tabelle stärker darauf
   umgestellt werden — etwa „Ergebnis vor Ausgleichszahlung und Abführung" statt EAT?

7. **Template für Schritt 5.** Die evm-Unterlage liegt nur als PDF vor. Soll die Folie auf Basis
   der Duisburg-.pptx (Layout `1_Inhalt_0`, Folie 14) gebaut werden, oder lieferst du die
   evm-.pptx nach?

---

## 5 · Prüfstand

**Zahlen** — jede Zahl auf einen offengelegten Abschluss oder den Geschäftsbericht rückführbar
und im Modell hinterlegt; alle Kontrollzeilen null (Ausnahme: dokumentierte 1 T€ Rundungs­
differenz 2024); Stichtage und Geschäftsjahre einheitlich; Modell in T€ und Mio. EUR getrennt,
Folie durchgehend Mio. EUR; acht Abweichungen zwischen Quellen im Blatt `Quellen & Hinweise`
dokumentiert, davon vier neu erhoben:

- **Investitionen 2023 nach Bereichen** — JA 2023 und JA 2024 teilen dieselben 27.342 T€
  unterschiedlich auf (Telekommunikation erst ab JA 2024 eigene Zeile). Angesetzt: JA 2024.
- **Bankverbindlichkeiten 31.12.2025** — der GB 2025 nennt drei Werte: 123,9 Mio. EUR (S. 18),
  123,7 Mio. EUR (S. 20) und 124.179 T€ im geprüften Anhang (S. 82). Angesetzt: Anhang.
- **Personalaufwand 2024** — Anhang des GB 2025 nennt als Vorjahr 53.317 T€, die GuV desselben
  Berichts und der JA 2024 nennen 55.317 T€. Angesetzt: JA 2024; ohne Folienwirkung.
- **Ergebnisdefinition** — der Lagebericht bezeichnet als „Ergebnis vor Ertragsteuern" das
  Ergebnis nach sonstigen Steuern (2025: 52,4 statt 52,7 Mio. EUR). Auf der Folie steht die
  GuV-Größe; die Differenz ist in Fußnote 2 erklärt, damit der Vorstand seine eigene Zahl
  wiederfindet.

**Aussage** — Titel ist ein vollständiger Aussagesatz mit Zahl; die Folie zieht die Konsequenz
vorsichtig („scheint nicht") und lässt die Mittelfristplanung ausdrücklich offen; Sondereffekte
sind benannt und beziffert; jeder Cashflow-Ausreißer ist erklärt.

**Offen bis zur Klärung von Rückfrage 2** — der Kernaussagenkasten trägt noch keine
Investitionssumme, und der Kernsatz auf Folie 2.4 hat an dieser Stelle einen Platzhalter.

**Noch nicht erledigt (Schritt 5)** — Text ist noch nicht in die .pptx geschrieben. Beim Befüllen
gilt: nur vorhandene Platzhalter beschreiben, keine neuen Textfelder; das Verschuldungsdiagramm
bleibt think-cell-Objekt; Kolumnentitel und Fußzeilen auf Reste von „Stadtwerke Duisburg" /
„DVV" prüfen; Dateiname nach Schema `20260901_Metzler_ESWE Versorgungs AG_v1`.
