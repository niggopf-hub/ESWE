# Tabellen- und Bauteillayouts

Exakte Layouts der wiederkehrenden Elemente. Zahlen sind Platzhalter.

---

## 1. Financial-Tabelle (ausführliche Variante)

Sieben Spalten: Bezeichnung, schmale Marker-Spalte für die Kommentarnummern, fünf Jahre.
Leerzeilen trennen die Blöcke — sie sind Teil des Layouts, nicht Zufall.

```
(in Mio. EUR)              │    │  ‹J1›  │  ‹J2›  │  ‹J3›  │  ‹J4›  │  ‹J5›
───────────────────────────┼────┼────────┼────────┼────────┼────────┼────────
GuV                        │    │        │        │        │        │
Umsatz                     │ ①  │        │        │        │        │
%-Wachstum                 │    │   %    │   %    │   %    │   %    │   %
                           │    │        │        │        │        │
Gesamtleistung             │    │        │        │        │        │
                           │    │        │        │        │        │
Rohertrag                  │ ②  │        │        │        │        │
Rohertrag-Marge            │    │   %    │   %    │   %    │   %    │   %
                           │    │        │        │        │        │
EBITDA                     │ ③  │        │        │        │        │
EBITDA-Marge               │    │   %    │   %    │   %    │   %    │   %
                           │    │        │        │        │        │
EBIT                       │    │        │        │        │        │
EBIT-Marge                 │    │   %    │   %    │   %    │   %    │   %
                           │    │        │        │        │        │
EAT                        │    │        │        │        │        │
EAT-Marge                  │    │   %    │   %    │   %    │   %    │   %
                           │    │        │        │        │        │
Gewinnabführung            │    │  ( )   │  ( )   │  ( )   │  ( )   │  ( )
Jahresüberschuss           │    │        │        │        │        │
                           │    │        │        │        │        │
Kapitalflussrechnung       │    │        │        │        │        │
Operating Cash Flow        │ ④  │        │        │        │        │
Investing Cash Flow        │    │  ( )   │  ( )   │  ( )   │  ( )   │  ( )
Investing / Gesamtleistung │    │   %    │   %    │   %    │   %    │   %
                           │    │        │        │        │        │
Free Cash Flow             │ ⑤  │        │        │        │        │
                           │    │        │        │        │        │
Bilanzpositionen           │    │        │        │        │        │
Kassenbestand              │    │        │        │        │        │
Net Debt / (Net Cash) ¹⁾   │ ⑥  │        │        │        │        │
Net Debt / EBITDA          │    │   x    │   x    │   x    │   x    │   x
Eigenkapital-Quote         │    │   %    │   %    │   %    │   %    │   %
```

**Konventionen:**
- Negative Werte in **runden Klammern**, nicht mit Minuszeichen.
- Vielfache mit nachgestelltem `x` (`2,6x`), Prozente mit `%`.
- Deutsche Zahlformatierung: Punkt als Tausender-, Komma als Dezimaltrennzeichen.
- Eine Nachkommastelle bei Mio.-Beträgen, eine bei Prozenten und Faktoren.
- Blockzeilen (`GuV`, `Kapitalflussrechnung`, `Bilanzpositionen`) fett, ohne Werte.
- Die Marker-Spalte trägt nummerierte Kreise, die auf den Kommentarblock rechts verweisen.
  Nach jeder Zeilenänderung prüfen, ob Nummern und Kommentare noch zusammenpassen.

---

## 2. Financial-Blöcke (kompakte Variante)

Drei nebeneinanderliegende Diagrammblöcke statt einer Tabelle. Datenformat je Block:

```
Block 1 — Gewinn- und Verlustrechnung (Mio. EUR)
  Kategorien:      ‹J1›  ‹J2›  ‹J3›  ‹J4›  ‹J5›
  Reihe "Umsatz"
  Reihe "Rohertrag"
  Anmerkung:       CAGR  +X% p.a.
  Über den Säulen: Rohertrag-Marge in %

Block 2 — Kapitalflussrechnung (Mio. EUR)
  Reihen: Operating / Investing / Financing Cash Flow
  Summenzeile: ∑ Total Cash Flow

Block 3 — Bilanzpositionen (Mio. EUR)
  Reihen: Kassenbestand · Net Debt
  Über den Säulen: Eigenkapital-Quote in %
```

Diese Blöcke sind think-cell-Diagramme — Werte im think-cell-Datenblatt eintragen, nicht
programmatisch erzeugen.

---

## 3. Verschuldungsentwicklung

```
Kategorien:        ‹J1›   ‹J2›   ‹J3›   ‹J4›   ‹J5›
Säulen "Net Debt"    ▮      ▮      ▮      ▮      ▮
Über den Säulen:   ‹a›x   ‹b›x   ‹c›x   ‹d›x   ‹e›x     ← Net Debt / EBITDA
Legende:           ■ Net Debt ²⁾    ─ Net Debt / EBITDA
Fußnote:           2) Net Debt = ‹Definition›
```

---

## 4. Investitionsprogramm

Drei Spalten, drei Zeilen — als Raster, nicht als Fließtext:

```
                    │ ‹Schwerpunkt A›   │ ‹Schwerpunkt B›   │ ‹Schwerpunkt C›
────────────────────┼───────────────────┼───────────────────┼──────────────────
Investitions-       │ Stromnetze &      │ Wind- & Solar-    │ Wärmenetze
schwerpunkt         │ Digitalisierung   │ parks             │
────────────────────┼───────────────────┼───────────────────┼──────────────────
Geplante Projekte   │ ▪ ‹Projekt mit    │ ▪ ‹Projekt mit    │ ▪ ‹Projekt mit
                    │   Leistung/Ort›   │   Leistung/Ort›   │   Leistung/Ort›
                    │ ▪ ‹…›             │ ▪ ‹…›             │ ▪ ‹…›
                    │ ▪ ‹…›             │ ▪ ‹…›             │ ▪ ‹…›
────────────────────┴───────────────────┴───────────────────┴──────────────────
CapEx                            ‹Gesamtsumme›
```

Jedes Projekt trägt ein konkretes Merkmal — Anlagenzahl, Leistung, Länge, Ort oder
Zeitpunkt. Ohne Merkmal liest es sich wie eine Absichtserklärung.

---

## 5. KPI-Kachelblock

```
┌──────────────────┐   Wert:        9 pt, Primärfarbe #003D7C
│  ‹X› Mio. EUR    │   Bezeichnung: 9 pt, schwarz, mit Jahr
│  Umsatz ‹J›      │   Vorjahr:     kleinere Zeile darunter
│  ‹Y› Mio. EUR    │
│  (‹J-1›)         │
└──────────────────┘
```

Standardsatz: Umsatz · EBITDA · EBIT · EAT · CapEx · Mitarbeiter · Kunden je Sparte ·
Netzlänge je Sparte. Auswahl an den Fall anpassen.

---

## 6. Umsatzring

```
Ring mit ‹n› Segmenten, Prozentwerte außen
Mittelbeschriftung:  100% ≙ ‹Summe› Mio. EUR
Legende außen als eigene Textelemente, nicht als Diagrammlegende
Daneben je Erlösquelle:  ‹Überschrift›
                         ▪ ‹Erläuterung 1›
                         ▪ ‹Erläuterung 2›
```

---

## 7. Beteiligungsstruktur

```
Ebene 1   ‹Gesellschafter A›  ‹X %›   │   ‹Gesellschafter B›  ‹Y %›
                            ╲         │        ╱
                             ▼        ▼       ▼
Ebene 2                    ‹G E S E L L S C H A F T›
                    ┌──────────┼──────────┬──────────┐
                  ‹100 %›   ‹50 %›     ‹33,3 %›   ‹24,5 %›
                    ▼          ▼           ▼          ▼
                 ‹Tochter›  ‹Tochter›  ‹Beteil.›  ‹Beteil.›

Kasten bei wesentlichen Beteiligungen (drei Zeilen):
   ‹Tätigkeit in einem Halbsatz›
   Umsatz ‹J›: ‹X› Mio. EUR
   ‹Gewinnabführung / Jahresergebnis› ‹J›: ‹X› Mio. EUR

Farbkodierung nach Geschäftsbereich, Legende darunter.
Fußnote mit Stichtag und Hinweis auf die eigene Zuordnung.
```

---

## 8. Optionenvergleich

```
                    │ Verkauf Minderheit │ Verkauf Minderheit │ Verkauf Mehrheit │ Komplett-
                    │ am Geschäftsbereich│ am Unternehmen     │ am Geschäftsber. │ verkauf
────────────────────┼────────────────────┼────────────────────┼──────────────────┼──────────
Beschreibung        │ ▪ ‹2 Bullets›      │ ▪ ‹2 Bullets›      │ ▪ ‹2 Bullets›    │ ▪ ‹…›
────────────────────┼────────────────────┼────────────────────┼──────────────────┼──────────
Einschätzung        │ ▪ ‹Vorteil›        │ ▪ ‹Vorteil›        │ ▪ ‹Vorteil›      │ ▪ ‹…›
                    │ ▪ ‹Vorteil›        │ ▪ ‹Vorteil›        │ ▪ ‹Vorteil›      │ ▪ ‹…›
                    │ ▪ ‹Nachteil›       │ ▪ ‹Nachteil›       │ ▪ ‹Nachteil›     │ ▪ ‹…›
                    │ ▪ ‹Nachteil›       │ ▪ ‹Nachteil›       │ ▪ ‹Nachteil›     │ ▪ ‹…›
```

Jede Spalte nennt mindestens einen Nachteil. Eine Option ohne Nachteil liest sich wie ein
Verkaufsargument.
