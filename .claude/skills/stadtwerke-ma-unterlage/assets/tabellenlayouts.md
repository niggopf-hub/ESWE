# Tabellen- und Bauteillayouts

Exakte Layouts der wiederkehrenden Elemente. Zahlen sind Platzhalter.

---

## 1. One Pager / Steckbrief

Zweispaltig, Merkmal links, Angabe rechts. Feste Zeilenfolge — von der Rechtsform über
Eigentümer und Organe zu den Zahlen und zuletzt der Steuerungslogik.

```
Merkmal                    │ Angabe
───────────────────────────┼──────────────────────────────────────────────────────
Firma / Sitz               │ ‹Firma›, ‹Straße›, ‹PLZ Ort›
Rechtsform / Register      │ ‹Rechtsform›, ‹HRB-Nummer› (‹Amtsgericht›)
Aktionäre / Gesellschafter │ ‹Gesellschafter A› ‹X› % · ‹Gesellschafter B› ‹Y› %
Grundkapital               │ ‹X› Mio. € (‹Anzahl/Art der Anteile›)
Vorstand                   │ ‹Name› (Vors.), ‹Name›
AR-Vorsitz                 │ ‹Name, Funktion›
Mitarbeiter                │ Ø ‹X› (‹Jahr›)
Kunden                     │ ~‹X› (‹Sparten›, ‹Jahr›)
Umsatz ‹J-1› / ‹J›         │ ‹X› Mio. € / ‹Y› Mio. €
EBT ‹J-1› / ‹J›            │ ‹X› Mio. € / ‹Y› Mio. €
Jahresüberschuss ‹J-1›/‹J› │ ‹X› Mio. € / ‹Y› Mio. €
Eigenkapital / EK-Quote    │ ‹X› Mio. € / ‹Y› % (‹Stichtag›)
Absatz ‹J›                 │ Strom ‹X› GWh · Gas ‹Y› GWh · Wärme ‹Z› GWh · Wasser ‹W› Mio. m³
Netz                       │ ‹Sparte› > ‹X› km; ‹weitere Sparten›; ‹Sparte› via ‹Tochter›
Ergebnisverwendung         │ ‹EAV mit …, seit …› · ‹Ausgleichszahlung an …›
Steuerungskennzahlen       │ ‹Finanzielle›; nicht-finanziell: ‹operative›
```

**Konventionen:**
- Mehrteilige Angaben mit Mittelpunkt `·` in derselben Zelle, statt zusätzliche Zeilen.
- Zahlen immer mit Jahr, Bestandsgrößen mit Stichtag.
- Zwei Jahre nebeneinander bei Umsatz, EBT und Jahresüberschuss — der Leser sieht die
  Richtung, ohne dass die Folie sie behaupten muss.
- Die letzte Zeile ist keine Deko: Sie nennt die Kennzahlen, mit denen das Unternehmen sich
  selbst steuert, und legt damit fest, welche Größen in der übrigen Unterlage zu verwenden
  sind.

---

## 2. Financials — drei Blöcke (Regelfall)

Drei nebeneinanderliegende Diagrammblöcke, alle über denselben Fünfjahreszeitraum, darunter
der Kommentarblock. Es sind think-cell-Diagramme: Werte im Datenblatt eintragen, nicht
programmatisch erzeugen.

```
Block 1 — Ertragslage (Mio. EUR)
  Kategorien:        ‹J1›  ‹J2›  ‹J3›  ‹J4›  ‹J5›
  Reihe "Umsatz"       ▮     ▮     ▮     ▮     ▮
  Reihe "Rohertrag"    ▮     ▮     ▮     ▮     ▮
  Über den Säulen:   Rohertragsmarge in %
  Anmerkung:         CAGR +‹X› % p.a.

Block 2 — Finanzlage (Mio. EUR)
  Reihen: Cashflow aus laufender Geschäftstätigkeit
          Cashflow aus Investitionstätigkeit
          Cashflow aus Finanzierungstätigkeit
  Summenzeile: ∑ Veränderung des Finanzmittelfonds

Block 3 — Vermögenslage (Mio. EUR)
  Reihen: Finanzmittelfonds · Net Debt
  Über den Säulen: Eigenkapitalquote in %
```

**Block 1 ist der wichtigste und wird am häufigsten falsch gebaut: Es sind Umsatz und
Rohertrag, nicht Umsatz und Ergebnis.** Der Umsatz eines Versorgers schwankt mit den
Beschaffungspreisen, ohne dass sich am Geschäft etwas ändert; der Rohertrag zeigt, was davon
bleibt. Die beiden Reihen nebeneinander machen genau das sichtbar — Umsatz halbiert sich,
Rohertrag bleibt. Das ist die Entwarnung, die vor der schlechten Nachricht kommen muss.

---

## 3. Financials — Zeilengerüst (HGB-Einzelabschluss)

Die Zeilenlogik folgt dem HGB-Einzelabschluss, nicht der angelsächsischen Kennzahlenkaskade.
Dieses Gerüst liegt sowohl den drei Blöcken als auch der ausführlichen Tabelle zugrunde und
entspricht dem Output-Blatt des Modells.

```
Position                                  ‹J1›  ‹J2›  ‹J3›  ‹J4›  ‹J5›
─────────────────────────────────────────────────────────────────────────
Ertragslage
  Umsatzerlöse
  Materialaufwand
  Personalaufwand
  Abschreibungen
  Sonstige betriebliche Aufwendungen
  Betriebliches Ergebnis
  Beteiligungsergebnis
  Zinsergebnis
  Ergebnis vor Steuern
  Unternehmensergebnis / Jahresüberschuss

Vermögenslage
  Anlagevermögen
  Umlaufvermögen
    davon Kassenbestand und Guthaben bei Kreditinstituten
  Rechnungsabgrenzungsposten
  Bilanzsumme
  Eigenkapital
  Empfangene Ertragszuschüsse
  Rückstellungen
  Verbindlichkeiten

Finanzlage (Mio. €)
  Cashflow aus laufender Geschäftstätigkeit
  Cashflow aus Investitionstätigkeit
  Cashflow aus Finanzierungstätigkeit
  Veränderung des Finanzmittelfonds
  Finanzmittelfonds am Ende der Periode

Kennzahlen
  Eigenkapitalquote
  Anlagenintensität
  Umsatzrendite (Unternehmensergebnis / Umsatz)
  EBITDA (Betriebliches Ergebnis + Abschreibungen)
  nachrichtlich: Eigenkapitalquote lt. Lagebericht
```

**Warum diese Gliederung und nicht EBITDA-Marge / EBIT-Marge / EAT-Marge:** Kommunale
Versorger steuern mit Betriebsergebnis, Beteiligungsergebnis und EBT. Das
Beteiligungsergebnis ist bei einem Querverbund keine Nebenposition, sondern häufig die
Hälfte des Ergebnisses — wer es in einem EBITDA verschwinden lässt, verliert die halbe
Ertragskraft aus dem Blick. Die Zeile *nachrichtlich: Eigenkapitalquote lt. Lagebericht*
gehört dazu, weil die eigene Berechnung von der des Unternehmens abweichen kann; die
Differenz ist eine Kontrolle, keine Nachlässigkeit.

**Konventionen:**
- Negative Werte in **runden Klammern**, nicht mit Minuszeichen.
- Vielfache mit nachgestelltem `x` (`2,6x`), Prozente mit `%`.
- Deutsche Zahlformatierung: Punkt als Tausender-, Komma als Dezimaltrennzeichen.
- Eine Nachkommastelle bei Mio.-Beträgen, eine bei Prozenten und Faktoren.
- Blockzeilen (`Ertragslage`, `Vermögenslage`, `Finanzlage`, `Kennzahlen`) fett, ohne Werte.

---

## 4. Financials — ausführliche Tabelle (Variante)

Wo mehr Detailtiefe gewünscht ist, tritt an die Stelle der drei Blöcke eine durchgehende
Tabelle. Sie nutzt dasselbe Zeilengerüst aus Abschnitt 3, ergänzt um eine schmale
Marker-Spalte, deren nummerierte Kreise auf den Kommentarblock rechts verweisen.

```
Position                                  │    │  ‹J1›  │  ‹J2›  │  ‹J3›  │  ‹J4›  │  ‹J5›
──────────────────────────────────────────┼────┼────────┼────────┼────────┼────────┼────────
Ertragslage                               │    │        │        │        │        │
  Umsatzerlöse                            │ ①  │        │        │        │        │
  …                                       │    │        │        │        │        │
  Betriebliches Ergebnis                  │ ②  │        │        │        │        │
  Beteiligungsergebnis                    │ ③  │        │        │        │        │
                                          │    │        │        │        │        │
Finanzlage                                │    │        │        │        │        │
  Cashflow aus laufender Geschäftstät.    │ ④  │        │        │        │        │
  …                                       │    │  ( )   │  ( )   │  ( )   │  ( )   │  ( )
                                          │    │        │        │        │        │
Kennzahlen                                │    │        │        │        │        │
  Eigenkapitalquote                       │ ⑤  │   %    │   %    │   %    │   %    │   %
  Net Debt / EBITDA ¹⁾                    │ ⑥  │   x    │   x    │   x    │   x    │   x
```

Leerzeilen zwischen den Blöcken sind Teil des Layouts. Nach jeder Zeilenänderung prüfen, ob
Nummern und Kommentare noch zusammenpassen — sie verrutschen, wenn Zeilen wegfallen.

---

## 5. Verschuldungsentwicklung

```
Kategorien:        ‹J1›   ‹J2›   ‹J3›   ‹J4›   ‹J5›
Säulen "Net Debt"    ▮      ▮      ▮      ▮      ▮
Über den Säulen:   ‹a›x   ‹b›x   ‹c›x   ‹d›x   ‹e›x     ← Net Debt / EBITDA
Legende:           ■ Net Debt ²⁾    ─ Net Debt / EBITDA
Fußnote:           2) Net Debt = ‹Definition›
```

---

## 6. Investitionshorizont

Drei Teile: Historie links, Verschuldung darunter oder daneben, Ausblick rechts als Raster.

```
Historie (Mio. EUR)     ‹J1›   ‹J2›   ‹J3›   ‹J4›   ‹J5›
Gesamtinvestitionen       ▮      ▮      ▮      ▮      ▮
Schwerpunkte ‹J5›:      ‹Sparte› ‹X› · ‹Sparte› ‹Y› · ‹Sparte› ‹Z›

                    │ ‹Schwerpunkt A›   │ ‹Schwerpunkt B›   │ ‹Schwerpunkt C›
────────────────────┼───────────────────┼───────────────────┼──────────────────
Investitions-       │ ‹z. B. Netze &    │ ‹z. B. Wind- &    │ ‹z. B. Wärme-
schwerpunkt         │  Digitalisierung› │  Solarparks›      │  netze›
────────────────────┼───────────────────┼───────────────────┼──────────────────
Geplante Projekte   │ ▪ ‹Projekt mit    │ ▪ ‹Projekt mit    │ ▪ ‹Projekt mit
                    │   Leistung/Ort›   │   Leistung/Ort›   │   Leistung/Ort›
                    │ ▪ ‹…›             │ ▪ ‹…›             │ ▪ ‹…›
────────────────────┴───────────────────┴───────────────────┴──────────────────
CapEx                            ‹Gesamtsumme›
```

Jedes Projekt trägt ein konkretes Merkmal — Anlagenzahl, Leistung, Länge, Ort oder
Zeitpunkt. Ohne Merkmal liest es sich wie eine Absichtserklärung. Die Historie links trägt
das Argument: Eine Investitionssumme wirkt erst dann groß, wenn danebensteht, was das Haus
bisher jährlich gestemmt hat.

---

## 7. Summary / Überleitung

```
[Bereich]  Summary ‹Kapitelname› / Überleitung zu Kapitel 3

Kernbotschaft (Absatz, kein Bullet):
  ‹Gesellschaft› ist ein ‹Charakterisierung: wirtschaftlich gesunder, kommunal
  verankerter …› mit ‹Stärke 1›, ‹Stärke 2› und ‹Stärke 3› — steht aber am Beginn
  ‹der investitionsintensivsten Phase›. ‹Auslöser: Wärmeplanung, Klimaziel› machen
  ‹Gesellschaft› zum ‹Rolle›, während gleichzeitig ‹Gegenkräfte: Normalisierung,
  Wettbewerb, Zinsen, Regulierung› die Innenfinanzierungskraft begrenzen.

Leitfrage (hervorgehobener Kasten, ein Satz):
  Wie finanziert und organisiert ‹Gesellschaft› ‹das Vorhaben› bei gleichzeitig
  ‹bestehender Verpflichtung› und ‹bestehender Nebenbedingung›?
```

Die Leitfrage hat drei Bestandteile — Vorhaben, Verpflichtung, Nebenbedingung. Wer nur das
Vorhaben nennt, bekommt die Antwort „dann nehmen wir eben mehr Kredit auf". Erst die beiden
anderen machen sichtbar, dass es diesen Weg nicht gibt.

---

## 8. KPI-Kachelblock (Variante zum One Pager)

```
┌──────────────────┐   Wert:        9 pt, Primärfarbe #003D7C
│  ‹X› Mio. EUR    │   Bezeichnung: 9 pt, schwarz, mit Jahr
│  Umsatz ‹J›      │   Vorjahr:     kleinere Zeile darunter
│  ‹Y› Mio. EUR    │
│  (‹J-1›)         │
└──────────────────┘
```

Dazu der Umsatzring:

```
Ring mit ‹n› Segmenten, Prozentwerte außen
Mittelbeschriftung:  100% ≙ ‹Summe› Mio. EUR
Legende außen als eigene Textelemente, nicht als Diagrammlegende
```

---

## 9. Beteiligungsstruktur

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
   ‹Eigenkapital / Umsatz› ‹J›: ‹X› Mio. EUR
   ‹Jahresergebnis / Gewinnabführung› ‹J›: ‹X› Mio. EUR

Farbkodierung nach Geschäftsbereich, Legende darunter.
Fußnote mit Stichtag und Hinweis auf die eigene Zuordnung.
```

---

## 10. Ziele und Ansatzpunkte (Kapitel 3)

```
Folie 19 — Mögliche Ziele des Unternehmens
  1. ‹Ziel›  — ‹Anker: Jahreszahl, Projekt, Quote, Beschluss›
  2. ‹Ziel›  — ‹Anker›
  …  bis 6–7 Ziele

Folie 20 — Ansatzpunkte für direkte Vorschläge
  ┌ Finanzierungsseite ─────┬ Eigenkapitalseite ──────┐
  │ ▪ ‹Ansatz›              │ ▪ ‹Ansatz›              │
  │ ▪ ‹Ansatz›              │ ▪ ‹Ansatz›              │
  ├ Portfolio und Struktur ─┼ Operativ ───────────────┤
  │ ▪ ‹Ansatz›              │ ▪ ‹Ansatz›              │
  │ ▪ ‹Ansatz›              │ ▪ ‹Ansatz›              │
  └─────────────────────────┴─────────────────────────┘
```

Jeder Ansatz muss auf ein Ziel aus Folie 19 und eine Zahl aus Kapitel 2 zurückführbar sein.
Wer das nicht kann, streicht ihn.
