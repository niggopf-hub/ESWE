# Kapitel 2 auf ESWE Versorgungs AG umgeschrieben

**Ergebnisdatei:** `20260901_ESWE Versorgungs AG_Kapitel2_v1.pptx`
**Vorlage:** `20240305_Stadtwerke Duisburg_v4 1 (1).pptx` (21 Folien, unverändert übernommen)
**Bearbeitet:** Folien 3 (Agenda), 9–14 (Kapitel 2)
**Stand:** 01.09.2026

---

## 1. Vorgehen

1. **Vorlage analysiert.** Alle 21 Folien mit `python-pptx` ausgelesen (Shape-IDs, Positionen,
   Textinhalte, Tabellenzellen, Bilder, OLE-Objekte). Kapitel 2 der Duisburg-Unterlage besteht aus:

   | Folie | Inhalt Duisburg | Abschnitt Briefing |
   |---|---|---|
   | 9 | Kapiteltrenner | – |
   | 10 | „Unser Verständnis der Ausgangslage" | i – Ausgangslage |
   | 11 | Beteiligungsstruktur (vereinfacht) | iii – Beteiligungsstruktur |
   | 12 | Überblick / Geschäftsmodell / KPI-Kacheln | ii – One Pager / Steckbrief |
   | 13 | Investitionsbedarf + Verschuldung | iv – Investitionshorizont |
   | 14 | Financials-Tabelle + Kommentare | v – Financials, vi – Überleitung Kap. 3 |

   Die Folienlogik der Vorlage wurde 1:1 beibehalten; jede Folie hat dieselbe Rolle behalten.

2. **Datengrundlage aufgebaut.**
   - `ESWE_Versorgungs_AG_Jahresabschluss_2020-2024.xlsx` (Bilanz, GuV, Kapitalflussrechnung 2020–2024)
   - `Geschaeftsbericht-25.pdf` (92 Seiten, vollständig ausgewertet – inkl. der als Bild
     eingebetteten Tabellen auf S. 15, 18, 19, 80, 81, die per Seitenrendering gelesen wurden)
   - `Briefing_ESWE_Versorgungs_AG.md` (Struktur- und Inhaltsvorgabe)
   - Ergänzend die vier Unternehmensregister-Auszüge `Wiesbaden_HRB_2105_*.pdf` für
     Bankverbindlichkeiten und Pensionsrückstellungen 2021–2024 (im Briefing nicht enthalten)

3. **Text ersetzt, Layout nicht angefasst.** Die Bearbeitung erfolgt shape-genau über die
   Shape-IDs; je Absatz wird der erste Run behalten (damit Schrift, Größe, Farbe, Bullet-Ebene
   erhalten bleiben) und nur der Text getauscht. Hoch­gestellte Fußnotenziffern werden erkannt und
   wieder hochgestellt geschrieben, Zeilenumbrüche (`<a:br/>`) gezielt gesetzt.

4. **Charts unberührt gelassen** (wie gewünscht): `Chart 241` (Umsatzverteilung, Folie 12) und
   `Chart 49` (Net Debt, Folie 13) sowie alle think-cell-OLE-Objekte sind unverändert im File.
   Geprüft: identische Part-Liste (225 Teile), alle Medien und Embeddings bitgleich.

---

## 2. Was auf welcher Folie steht

### Folie 3 – Agenda
Punkt 2 lautet jetzt „Übersicht und Herausforderungen ESWE Versorgungs AG". Punkte 1 und 3 unverändert.

### Folie 9 – Kapiteltrenner
„Übersicht und Herausforderungen ESWE Versorgungs AG".

### Folie 10 – Ausgangslage
Titel: *Die Umsetzung der Kommunalen Wärmeplanung und der Klimaneutralität Wiesbadens bis 2045
erfordert von ESWE erheblich steigende Investitionsmittel.*
Sechs Bullets: Klimaneutralität 2045 / KWP-Umsetzungspartner · Geschäft und Netze · duale
Aktionärsstruktur (WVV 50,62 % / Thüga 49,38 %, EAV seit 2010) · Ergebnisverlauf 2023–2025 und
Mittelfristplanung bis 2030 · Projekt „Wärmewende" · Aussage des Lageberichts, dass klassische
Bankdarlehen künftig nicht mehr ausreichen.
Kernaussage-Balken: Finanzierung übersteigt Innenfinanzierungskraft und klassischen
Fremdkapitalrahmen → Kapitalflexibilisierung als Option.

### Folie 11 – Beteiligungsstruktur
Gesellschafterebene: Landeshauptstadt Wiesbaden (100 %) → WVV, 50,62 % → **ESWE Versorgungs AG**
(Umsatz 2025 473,8 Mio. EUR; Ergebnis vor Ausgleichszahlung/Gewinnabführung 48,9 Mio. EUR),
Thüga AG 49,38 %.
**Obere Boxenreihe – verbundene Unternehmen:** sw netz (100 %), WiTCOM (100 %), ESWE BioEnergie
(90 %), ESWE Taunuswind/Windpark (100 %), THEE ESWE Windparkbeteiligung (33,33 %).
**Untere Boxenreihe – Beteiligungen:** KMW (50 %), MHKW Wiesbaden (24,5 %), WRT Infrastrukturbau
(49 %), Windkraft Kahlenberg (50 %), Windpark Bad Camberg (33,33 %), ESWE Windpark Uettingen (100 %).
Alle Eigenkapital-/Ergebniswerte aus den Angaben zum Anteilsbesitz (§ 285 Nr. 11 HGB), GB 2025 S. 80.

### Folie 12 – Überblick und Geschäftsmodell
KPI-Kacheln 2025: Umsatz 473,8 · EBITDA 70,2 · EBT 52,7 · Investitionen 37,0 · Operating Cash Flow
42,7 Mio. EUR · EK-Quote 28,5 %.
Zweite Kachelreihe (vorher „Produktion und Netze"): Absatzmengen 2025 – Strom 605 Mio. kWh,
Gas 1.445 Mio. kWh, Wärme 275 Mio. kWh, Wasser 14,7 Mio. m³.
Geschäftsfelder Strom / Gas / Wärme / Wasser / Sonstiges neu getextet; Donut-Mitte auf
„100 % ≙ 473,8 Mio. EUR" gesetzt.

### Folie 13 – Investitionsbedarf
Titel: *Das Investitionsvolumen wird sich laut Lagebericht in den nächsten Jahren nochmals erheblich
steigern – Wärme- und Stromnetz sind die zentralen Treiber.*
Die sieben Segmentspalten entsprechen jetzt exakt der Investitionsgliederung des GB 2025:
Strom- (~1,0) · Gas- (~3,0) · Wasser- (~14,0) · Wärmeversorgung (~6,5) · Sonstige Bereiche (~3,4) ·
Gemeinsame Bereiche (~4,0) · Beteiligungen (~5,2 Mio. EUR) = 37,0 Mio. EUR.
Je Segment „Geplante Projekte" getextet. Net-Debt/EBITDA-Marker: 1,4x / 1,1x / 0,9x / 1,0x / 1,8x
(2021–2025).

### Folie 14 – Financials
Tabelle vollständig auf ESWE 2021–2025 umgestellt (siehe Abschnitt 3), sechs Kommentare neu,
Überleitungs-Textbox auf die Kernaussage „klassische Bankdarlehen reichen nicht mehr aus" gesetzt.

---

## 3. Financials-Tabelle (Folie 14) – Werte und Herleitung

Alle Werte in Mio. EUR, HGB-Einzelabschluss.

| | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|
| Umsatzerlöse | 426,5 | 475,7 | 634,1 | 534,7 | 473,8 |
| %-Wachstum | 9,2 % | 11,5 % | 33,3 % | (15,7 %) | (11,4 %) |
| Rohertrag¹ | 115,1 | 119,4 | 150,1 | 147,5 | 132,0 |
| EBITDA² | 59,0 | 68,4 | 88,0 | 106,7 | 70,2 |
| EBITDA-Marge | 13,8 % | 14,4 % | 13,9 % | 20,0 % | 14,8 % |
| EBIT | 44,8 | 51,8 | 73,5 | 82,1 | 53,4 |
| EBIT-Marge | 10,5 % | 10,9 % | 11,6 % | 15,3 % | 11,3 % |
| EBT | 44,1 | 51,8 | 74,7 | 84,3 | 52,7 |
| EBT-Marge | 10,3 % | 10,9 % | 11,8 % | 15,8 % | 11,1 % |
| Ergebnis vor Ausgleich/Abführung | 40,7 | 48,2 | 70,6 | 78,3 | 48,9 |
| in % der Umsatzerlöse | 9,6 % | 10,1 % | 11,1 % | 14,6 % | 10,3 % |
| Ausgleichszahlung Thüga | (16,3) | (17,3) | (21,1) | (29,8) | (18,8) |
| Gewinnabführung WVV | (24,4) | (30,9) | (39,5) | (48,5) | (30,1) |
| Operating Cash Flow | 49,0 | 78,0 | 47,3 | 68,2 | 42,7 |
| Investing Cash Flow | (19,5) | (34,0) | 8,9 | (5,0) | (8,3) |
| Investitionen / Umsatzerlöse | 10,1 % | 11,3 % | 4,3 % | 5,1 % | 7,8 % |
| Free Cash Flow | 29,5 | 44,0 | 56,2 | 63,2 | 34,4 |
| Liquide Mittel | 3,6 | 30,6 | 45,0 | 21,5 | 2,5 |
| Net Debt³ | 84,4 | 77,3 | 75,0 | 106,9 | 129,7 |
| Net Debt / EBITDA | 1,4x | 1,1x | 0,9x | 1,0x | 1,8x |
| Eigenkapital-Quote | 30,3 % | 27,8 % | 26,3 % | 27,6 % | 28,5 % |

**Definitionen (so auch als Fußnoten auf der Folie):**
1. Rohertrag = Umsatzerlöse ./. Materialaufwand
2. EBITDA in der Definition der Gesellschaft, **inkl. Beteiligungsergebnis** (Ertragslage-Kurzfassung
   GB 2025, S. 15). 2024/2025 direkt aus dem GB, 2021–2023 nach identischer Formel aus der GuV
   berechnet – Gegenprobe: EBITDA ohne Beteiligungsergebnis ergibt exakt die Werte des
   Overview-Blatts der Excel-Mappe (34,6 / 50,8 / 57,5).
3. Net Debt = Verbindlichkeiten gegenüber Kreditinstituten + Pensionsrückstellungen ./. liquide
   Mittel. Bankverbindlichkeiten: 79,0 / 98,7 / 110,7 / 119,9 / 124,2; Pensionsrückstellungen:
   9,0 / 9,2 / 9,2 / 8,5 / 8,1. (Abweichend von Duisburg ohne Verrechnung finanzieller Forderungen
   gegen verbundene Unternehmen – bei ESWE nicht sauber aus den veröffentlichten Zahlen ableitbar.)

**Konsistenzprüfungen bestanden:** EBIT + Zinsergebnis = EBT (alle Jahre gegen die GuV geprüft);
Ausgleichszahlung + Gewinnabführung (+ Rücklageneinstellung 2023 von 10,0) = Ergebnis vor
Ausgleich/Abführung; EK-Quote deckt sich mit den Angaben der Lageberichte.

**Anmerkung zu 2025:** Der GB nennt im Fließtext „EBT 52,4 Mio. EUR" (= Ergebnis vor Ertragsteuern
nach Abzug der sonstigen Steuern). In der Tabelle ist die Position aus der Ertragslage-Kurzfassung
verwendet: **Ergebnis vor Steuern 52,7 Mio. EUR** (52.650 T€). Beide Größen sind korrekt, die
Tabellenlogik ist jahresübergreifend konsistent.

---

## 4. Offene Punkte

**Hoch – vor Versand zu erledigen:**

1. **Charts (bewusst nicht angefasst, wie abgestimmt):**
   - Folie 12, `Chart 241` „Umsatzverteilung" – enthält noch Duisburger Daten. Erlösstruktur 2025
     steht im GB 2025, S. 16 (Strom, Gas, Wärme, Wasserverpachtung 32,6, Wasserverkauf 16,9,
     konzerninterne DL, sonstige 11,4 + 0,9 + 2,5).
   - Folie 13, `Chart 49` „Entwicklung der Verschuldung" – Net-Debt-Reihe 2021–2025:
     **84,4 / 77,3 / 75,0 / 106,9 / 129,7 Mio. EUR**. Die Multiples (1,4x … 1,8x) und die
     Jahresbeschriftungen darüber sind bereits gesetzt und passen zu dieser Reihe.

2. **Logos und Icons auf Folie 11.** Die Boxen tragen weiterhin die Bildmarken der DVV-Gruppe
   (Stadt Duisburg, DVV, RheinEnergie, DVG, octeo, energieGUT, duisburgcity.com, Zoo Duisburg).
   Diese müssen durch ESWE-, sw-netz-, WiTCOM-, KMW-, MHKW- usw. Logos ersetzt werden
   (`ppt/media/image47.png` … `image59.png`).

3. **Verbinderlinien auf Folie 11.** Die Duisburger Struktur ist zweistufig (Holding → Stadtwerke →
   Operativgesellschaften); ESWE ist flach – alle elf Gesellschaften hängen direkt an der ESWE
   Versorgungs AG. Die sechs Winkelverbinder der unteren Reihe starten derzeit noch an der rechten
   Box der oberen Reihe und müssen an die ESWE-Box umgehängt werden. Reine Grafikarbeit, ca. 5 Min.
   Ebenfalls auf Folie 11: die Legende „Gesprächsfokus" (Datum entfernt) markierte in der Vorlage
   per Farbfläche die Stadtwerke Duisburg AG – bitte entscheiden, welche ESWE-Gesellschaft(en) so
   hervorgehoben werden sollen, oder Legende und Marker entfernen.

4. **Kapitel 1 und 3 sowie Titelfolie sind unverändert** (Auftrag war ausdrücklich Kapitel 2).
   Dort steht noch Duisburg:
   - Folie 1: Titel „Überlegungen zur Kapitalflexibilisierung / Unterlage für Herrn Thomas Brauers,
     Herrn Dennis Schulte im Walde" sowie „Duisburg / Frankfurt am Main, 5. März 2024" und die
     Duisburger Logos
   - Folie 19: „Plattform für die Mitgestaltung der Energiewende in **Duisburg**"
   - Folie 20: „Metzler ist ideal positioniert, die **Stadtwerke Duisburg** bei strategischen
     Überlegungen zu beraten"

**Mittel:**

5. **Segment-Icons Folie 13.** Über den sieben Segmentspalten sitzen noch die Duisburger Piktogramme
   (u. a. Bus/Zoo). Für „Sonstige Bereiche", „Gemeinsame Bereiche" und „Beteiligungen" passen sie
   inhaltlich nicht mehr.

6. **Nummerierte Marker auf Folie 14.** Die Ziffern 1–6 in der Tabelle (Balken links) markierten die
   Duisburger Zeilen. Die Kommentare 1–6 sind neu, die Balken sitzen aber noch auf den alten
   Zeilenhöhen und sollten auf die jetzt kommentierten Zeilen (Umsatz, EBITDA, EBT,
   Ausgleichszahlung/Gewinnabführung, Cash Flow, Net Debt/EK-Quote) verschoben werden.

7. **Zwei ergänzte Textfelder auf Folie 13.** Für „Stromversorgung" und „Wasserversorgung" gab es in
   der Vorlage keine Capex-Textfelder; sie wurden durch Duplizieren des vorhandenen Feldes ergänzt
   (Shape-IDs 3075/3076, gleiche Formatierung). Bitte optisch gegenprüfen, ob sie exakt im Raster sitzen.

8. **Zeilenlängen prüfen.** Einige Boxen sind eng (Folie 11: Boxen 4,3 cm breit; Folie 13:
   Projektspalten 3,5 cm). Ich habe wie in der Vorlage weiche Trennstriche gesetzt
   („Telekommunikations-infrastruktur", „Erweiterungs-investitionen", „Groß-wärmepumpen"). Nach dem
   ersten Öffnen in PowerPoint bitte auf Überläufe schauen.

**Niedrig / inhaltlich zu entscheiden:**

9. **Abschnitt vi des Briefings** (Summary Kapitel 2 / Überleitung zu Kapitel 3) hat in der
   Duisburg-Vorlage keine eigene Folie. Ich habe die Kernbotschaft in die Kernaussage-Balken der
   Folien 10 und 14 gelegt, statt eine neue Folie einzufügen. Falls eine eigene Summary-Folie
   gewünscht ist, bitte kurz Bescheid geben.

10. **KMW-Ausschüttung.** Die 14,0 Mio. EUR auf Folie 11 sind die Gewinnausschüttung der KMW für das
    Geschäftsjahr 2024, die 2025 vereinnahmt wurde (GB 2025, S. 85). Auf der Folie steht
    „Ausschüttung 2025" – falls die Unterscheidung wichtig ist, präzisieren.

11. **WRT Infrastrukturbau.** Das Briefing nennt „WRT Infrastruktur GmbH"; laut Anteilsbesitzliste
    im GB 2025 lautet die Firma „WRT Infrastrukturbau GmbH" mit 49,0 % (nicht 50 %). Ich bin der
    Registerangabe im Geschäftsbericht gefolgt; Werte sind der Jahresabschluss 2024, da 2025 noch
    nicht vorliegt.

12. **Arbeitsnotizen außerhalb der Folienfläche.** Auf den Folien 12 und 13 lagen neben der Folie
    Arbeitsnotizen der Duisburg-Bearbeitung (u. a. eine dvv.de-URL). Diese habe ich durch
    ESWE-Quellenverweise ersetzt, damit im File keine falschen Hinweise mehr stehen.

---

## 5. Technische Anmerkung

Die Datei wurde mit `python-pptx` geschrieben. Sie enthält weiterhin alle 225 Package-Teile des
Originals; Medien und OLE-Embeddings sind unverändert, beide Diagramme und alle
„think-cell data – do not delete"-Objekte sind erhalten. Der Größenunterschied zur Vorlage
(10,7 statt 11,8 MB) resultiert ausschließlich aus der ZIP-Kompression, nicht aus fehlendem Inhalt.
