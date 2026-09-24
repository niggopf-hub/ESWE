# Tabellen- und Bauteillayouts

Exakte Layouts der wiederkehrenden Elemente der grünen Vorlage. Zahlen sind Platzhalter.
Konventionen überall: Mio. EUR, negative Werte in runden Klammern, Vielfache mit `x`,
Prozente mit Leerzeichen, deutsche Zahlformatierung, eine Nachkommastelle bei Beträgen
unter 100 Mio. EUR.

---

## 1. Kacheln (Kunden und Netzinfrastruktur)

Zehn Kacheln in zwei Reihen, je drei Zeilen. Der Vorjahreswert in Klammern.

```
┌──────────────────────┐ ┌──────────────────────┐ ┌──────────────────────┐ ┌──────────────────────┐ ┌──────────────────────┐
│ Stromkunden ‹J›      │ │ Gaskunden ‹J›        │ │ Stromnetz ‹J›³⁾      │ │ Gasnetz ‹J›⁴⁾        │ │ Mitarbeiter          │
│ 207.431              │ │ 53.323               │ │ 2.820 km             │ │ 823 km               │ │ ca. 644              │
└──────────────────────┘ └──────────────────────┘ └──────────────────────┘ └──────────────────────┘ └──────────────────────┘
┌──────────────────────┐ ┌──────────────────────┐ ┌──────────────────────┐ ┌──────────────────────┐ ┌──────────────────────┐
│ Umsatz ‹J›           │ │ EBITDA ‹J›           │ │ EBIT¹⁾ ‹J›           │ │ EAT ‹J›²⁾            │ │ CapEx ‹J›            │
│ 474 Mio. EUR         │ │ 70 Mio. EUR          │ │ 53 Mio. EUR          │ │ 49 Mio. EUR          │ │ 37 Mio. EUR          │
│ 535 Mio. EUR (‹J-1›) │ │ 107 Mio. EUR (‹J-1›) │ │ 82 Mio. EUR (‹J-1›)  │ │ 78 Mio. EUR (‹J-1›)  │ │ 27 Mio. EUR (‹J-1›)  │
└──────────────────────┘ └──────────────────────┘ └──────────────────────┘ └──────────────────────┘ └──────────────────────┘
```

Bei Konzernen statt Kunden der Absatz („Stromabsatz ‹J›, 1,9 Mrd. kWh"). Quelle der Werte:
Excel-Block `Kacheln`. Fußnoten: EBIT-Definition, EAT-Definition, Bezugsgesellschaft der
Netzlängen, Mitarbeiterzahl bei Abweichung.

Daneben der Umsatzring (think-cell, Block `Umsatzring`), in der Mitte „100 % ≙ ‹Summe› Mio.
EUR", außen die Prozentwerte, und je Erlösquelle ein Erklärkasten mit Überschrift und zwei
Bullets:

```
Stromverkauf                 Gasverkauf                    Wärme
▪ Vertrieb an Privat-,       ▪ Erdgasvertrieb an Privat-,  ▪ Fernwärme-Verbundnetz mit
  Gewerbe- und Geschäfts-      Gewerbe- und Geschäfts-       ‹X› km und ‹n› Anschlüssen
  kunden                       kunden
▪ Beschaffung und            ▪ Rückverkauf beschaffter     Wasser
  Vermarktung                  Gasmengen zur Portfolio-    ▪ Betriebsführung des Wasser-
                               optimierung                   netzes für ‹Eigenbetrieb›
Dienstleistungen & Übrige                                  ▪ Wasserverkauf an ‹…›
▪ Leistungen für verbundene Unternehmen (u. a. ‹Netz›, ‹Telko›)
▪ E-Mobilität und weitere Erlösquellen
```

Legende der Geschäftsfelder unter den Kacheln: Energievertrieb & -beschaffung, Netzgeschäft,
Energieerzeugung, Energiedienstleistungen (Wärme & E-Mobilität), Telekommunikation, Wasser.
Konzern: Mobilität & ÖPNV, Services & Gebäudemanagement.

---

## 2. Financials: drei Blöcke

```
Gewinn- und Verlustrechnung (Mio. EUR)   Kapitalflussrechnung (Mio. EUR)     Bilanzpositionen (Mio. EUR)
■ Umsatz ■ Rohertrag ■ EBITDA            ■ Operating ■ Investing ■ Financing  ■ Liquide Mittel ■ Net Debt
● Rohertrag-Marge ● EBITDA-Marge         ∑ Total Cashflow                     ● Eigenkapital-Quote

  (37,3 %) (35,3 %) (36,8 %) (37,5 %) (…)                                       (30,3 %) (27,8 %) (26,3 %) (27,6 %) (28,5 %)
  (13,8 %) (14,4 %) (13,9 %) (20,0 %) (14,8 %)
       +3 % p.a. ─────────────►
  ▮▮▮   ▮▮▮   ▮▮▮   ▮▮▮   ▮▮▮            ▮   ▮   ▮   ▮   ▮                     ▮▮  ▮▮  ▮▮  ▮▮  ▮▮
  ‹J1›  ‹J2›  ‹J3›  ‹J4›  ‹J5›           ‹J1› … ‹J5›  Summe je Jahr als Zahl   ‹J1› … ‹J5›

Kommentar:
▪ Umsatz ‹J-1› und ‹J› nach dem energiepreis- und handelsbedingten Höchststand ‹Jahr› (‹Wert›) auf ‹Wert› und ‹Wert› normalisiert
▪ Materialaufwand mit den Beschaffungspreisen auf ‹Wert› gesunken
▪ Ergebnis nach Steuern ‹Jahre› sondereffektgetrieben, vor allem ‹Effekt› von ‹X› Mio. EUR im Jahr ‹J›, ‹J+1› mit ‹Wert› dennoch deutlich über Plan
▪ Operativer Cashflow von durchschnittlich rund ‹Wert› nahezu vollständig durch ‹Ergebnisabführung und Investitionshochlauf› gebunden

┌───────────────────────────────────────────────────────────────────────────────────────────────┐
│ ▶ Investitionsanstieg bei unveränderter Ausschüttungspolitik nicht aus dem operativen Cashflow │
│   finanzierbar, bereits ‹Jahr› Kapitaleinlage der Aktionäre von ‹X› Mio. EUR … erforderlich   │
└───────────────────────────────────────────────────────────────────────────────────────────────┘
```

Die Säulen sind think-cell (Blöcke `GuV-Chart`, `Cashflow-Chart`, `Bilanz-Chart`), die Kreise
und Kästen native Shapes. Der Kernsatz-Kasten fehlt in der DVV-vf und wird von der
Investitionsfolie kopiert. Bei Konzernen mit sehr großem Umsatz gegen kleines EBITDA (DVV:
6.898 gegen 110) das EBITDA als Kreis statt Säule; Entscheidung des Kollegen in think-cell,
Hinweis im Report.

---

## 3. Verschuldung und Investitionsbedarf

```
Investitionsbedarf
┌──────────────────┬──────────────────────┬──────────────────────┬──────────────────────┬──────────────────────┐
│ Investitions-    │      [Icon]          │      [Icon]          │      [Icon]          │      [Icon]          │
│ schwerpunkt      │  Wasser              │  Wärme               │  Strom & Gas         │  Beteiligungen &     │
│                  │                      │                      │                      │  Erzeugung           │
├──────────────────┼──────────────────────┼──────────────────────┼──────────────────────┼──────────────────────┤
│ CapEx ‹J›¹⁾      │  ~14,0 Mio. EUR      │  ~6,5 Mio. EUR       │  ~5,2 Mio. EUR       │  ~4,0 Mio. EUR       │
├──────────────────┼──────────────────────┴──────────────────────┴──────────────────────┴──────────────────────┤
│ CapEx bis ‹Jahr› │        ◄──────────── Fast 600 Mio. EUR, Geplante Investitionen ‹J1›-‹J5›²⁾ ────────────► │
├──────────────────┼──────────────────────┬──────────────────────┬──────────────────────┬──────────────────────┤
│ Geplante         │ ▪ ‹Projekt, Zahl›    │ ▪ ‹Projekt, Zahl›    │ ▪ ‹Projekt, Zahl›    │ ▪ ‹Projekt, Zahl›    │
│ Projekte         │ ▪ ‹Projekt, Zahl›    │ ▪ ‹Projekt, Zahl›    │ ▪ ‹Projekt, Zahl›    │ ▪ ‹Projekt, Zahl›    │
│                  │ ▪ ‹Projekt, Zahl›    │ ▪ ‹Projekt, Zahl›    │ ▪ ‹Projekt, Zahl›    │ ▪ ‹Projekt, Zahl›    │
└──────────────────┴──────────────────────┴──────────────────────┴──────────────────────┴──────────────────────┘

Entwicklung der Verschuldung (Mio. EUR)
■ Net Debt²⁾  ● Net Debt / EBITDA
   (1,0x)   (0,7x)   (0,9x)   (1,7x)   (1,3x)
     75       68       66       98      122          ▶ Die Nettoverschuldung ist ‹J› auf das ‹Faktor›-fache
     ▮        ▮        ▮        ▮        ▮             des EBITDA gestiegen – moderat, doch Investitions-
   ‹J1›     ‹J2›     ‹J3›     ‹J4›     ‹J5›            hochlauf steht noch bevor

1) Ohne ‹nicht gezeigte Bereiche› von zusammen ‹X› Mio. EUR; Gesamtinvestitionen ‹J› inklusive Finanzanlagen ‹Y› Mio. EUR;
2) Net Debt = ‹Definition der gewählten Stufe›
```

Spalten nach CapEx absteigend. Drei bis sechs Spalten je Fall (`dup_shapes.py`). Zeile
„CapEx bis ‹Jahr›" trägt die Gesamtsumme mit Horizont als Pfeil über alle Spalten; beim
Einzelabschluss ohne Gesamtsumme steht dort „Anstieg auf bis zu ‹X› Mio. EUR p. a. von Ø
‹Y› Mio. EUR p. a. in den letzten ‹n› Jahren". Säulen think-cell (Block `Verschuldung`),
Faktoren native.

---

## 4. Beteiligungsstruktur

```
      ‹Gesellschafter A›  ‹Quote›              ‹Gesellschafter B›  ‹Quote›
                    ╲                                 ╱
                     ▼                               ▼
                           ‹G E S E L L S C H A F T›
                     ▪ Gewinnabführung an ‹A›: ‹X› Mio. EUR
                     ▪ Ausgleichszahlung ‹B›: ‹Y› Mio. EUR
      ┌────────────┬────────────┬────────────┬────────────┬────────────┐
    100 %        100 %         90 %         50 %        24,5 %       33,33 %
      ▼            ▼            ▼            ▼            ▼            ▼
  [Netz GmbH]  [Telko GmbH] [BioEnergie]   [KMW AG]     [MHKW]     [Windpark KG]
  ▪ Betrieb    ▪ Glasfaser  ▪ Biomasse-   ▪ Erzeugung  ▪ Neues     ▪ Windportfolio
    des Strom-   und Rechen-  Heizkraft-    und Energie-  Müllheiz-    gemeinsam mit
    netzes       zentren      werk          hub           kraftwerk    ‹Partner›
  ▪ EK ‹J›:    ▪ Umsatz ‹J›: ▪ EK ‹J›:     ▪ EK ‹J›:    ▪ EK ‹J›:   ▪ EK ‹J›:
    ‹X› Mio.     ‹X› Mio.      ‹X› Mio.      ‹X› Mio.     ‹X› Mio.    ‹X› Mio.
  ▪ Gewinn-    ▪ Gewinn-     ▪ Jahres-     ▪ Ausschüt-  ▪ Jahres-   ▪ Jahres-
    abführung    abführung     ergebnis      tung          ergebnis    ergebnis

Farbcodierung nach Geschäftsbereich, Legende unten.
Logos: Platzhalter-Rechteck mit Gesellschaftsname, gelber Kasten LOGO.
Fußnote: Anteilsbesitz nach § 285 Nr. 11 HGB zum ‹Stichtag›; EAV mit ‹…›; nicht dargestellt ‹…› sowie Beteiligungen unter 20 % (‹…›)
```

Bei mehr als zwölf Gesellschaften die Quoten-Variante ohne Kästchen (DVV), gruppiert nach
Geschäftsbereichen mit „at equity"-Vermerk bei assoziierten Unternehmen.

---

## 5. Kapitel 3: Ziele und Beteiligungsmodell

```
Mögliche strategische Ziele
┌────────────────────────────┐ ┌────────────────────────────┐ ┌────────────────────────────┐
│ Erweiterung des Fremd-     │ │ Stärkung der Eigenkapital- │ │ ‹fallspezifisch 1›         │
│ finanzierungsspielraums    │ │ basis zur Sicherung lang-  │ │                            │
│ zur Umsetzung geplanter    │ │ fristiger finanzieller     │ │                            │
│ Investitionen              │ │ Flexibilität               │ │                            │
└────────────────────────────┘ └────────────────────────────┘ └────────────────────────────┘
┌────────────────────────────┐ ┌────────────────────────────┐ ┌────────────────────────────┐
│ ‹fallspezifisch 2›         │ │ Ausbau der regionalen      │ │ Erweiterung der ‹…›platt-  │
│                            │ │ Marktposition durch ge-    │ │ formen um zusätzliche      │
│                            │ │ zielte Akquisitionen und   │ │ Kompetenzen und Kunden     │
│                            │ │ Beteiligungen              │ │                            │
└────────────────────────────┘ └────────────────────────────┘ └────────────────────────────┘

Beispielstruktur: Minderheitsbeteiligung an der ‹Netz GmbH›¹⁾        Wesentliche Aspekte bei der Gestaltung
                                                                      einer Partnerschaft
        ‹X›                              Kapitalpartner               ▪ Ausgewogene Governance mit definierten
   Mehrheit / Kontrolle              Minderheitsbeteiligung             Reserved Matters, Dividendenpolitik und
          ╲                               ╱                              Exit-Mechanismen
           ▼                             ▼                            ▪ Investorengerechte Schaffung einer
        ┌──────────────────────────────────┐  Kapitalerhöhung             Plattform / eines abgegrenzten Vehikels
        │ ‹Netz GmbH›                      │  finanziert den            ▪ Rendite- und Rückzahlungsmechanismen
        │ bestehende Gesellschaft,         │  Stromnetzausbau           ▪ Festlegung Budget und Investitionsplan
        │ kein Carve-out erforderlich      │                            ▪ Gemeinsames Rollenverständnis
        └──────────────────────────────────┘
                     ▼
              Stromnetz ‹Stadt›                                       Vorteile für die ‹X›
                                                                      ▪ Teilung von Risiken und Investitionen
(private) Beteiligung an Unternehmen / Assets                         ▪ Zufluss eines Kaufpreises
▪ ‹Netz GmbH› (Minderheitsbeteiligung)                                ▪ Schnellere Umsetzung von Investitionen möglich
▪ ‹Telko GmbH› (Minderheit oder Wachstumspartnerschaft)               ▪ Zusätzlicher strategischer Input durch Partner
▪ Wärme-Neubaugeschäft (Projektgesellschaft)                          ▪ Governance flexibel strukturierbar zum Erhalt
▪ Fernwärmenetz                                                         des kommunalen Einflusses

┌───────────────────────────────────────────────────────────────────────────────────────────────┐
│ Beteiligungen unterhalb der AG-Ebene erschließen Kapital für Netzausbau und Wärmewende,         │
│ während Aktionärsstruktur und kommunale Steuerung der ‹X› unverändert bleiben                   │
└───────────────────────────────────────────────────────────────────────────────────────────────┘
1) Beteiligungshöhen illustrativ; Mitspracherechte des Investors über die Gesellschaftervereinbarung; Struktur übertragbar auf die weiteren Assets
```

Beide Folien liegen im grünen Design in `assets/kapitel3_gruen.pptx`.

---

## 6. Diskussionspunkte (kurze Ausbaustufe)

Fünf Thesen untereinander, je eine Zeile in einem Parallelogramm-Kasten der Vorlage
(Folie 17 der DVV-vf). Text in `references/kapitel-3-handlungsoptionen.md`.

---

## 7. Agenda

Tabelle mit drei Zeilen: Nummer, Kapitelname, Seite des Trenners.

```
01 │ Metzler Mergers & Acquisitions – Vorstellung und Referenzen │ 3
02 │ ‹X› – Übersicht und Herausforderungen                        │ 11
03 │ Diskussion möglicher Handlungsoptionen                       │ 17
```

Die Kapitelnamen stehen wortgleich auf den Trennern und in jeder Kolumne. Seitenzahlen nach
jedem Einfügen oder Löschen nachziehen.
