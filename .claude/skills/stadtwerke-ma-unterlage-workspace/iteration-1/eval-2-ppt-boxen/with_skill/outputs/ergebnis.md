# Kapitel 2 auf die ESWE Versorgungs AG umgeschrieben

**Datei:** `20260901_Metzler_ESWE Versorgungs AG_v1.pptx` (aus `20240305_Stadtwerke Duisburg_v4 1 (1).pptx` abgeleitet, 21 Folien, Dateiname nach Schema `JJJJMMTT_<Haus>_<Unternehmen>_<Version>`)
**Bearbeitet:** Folien 9–14 (Kapitel 2) plus die Agendazeile zu Kapitel 2 auf Folie 3. Kapitel 1 und 3 sind unberührt.
**Nicht angefasst:** alle think-cell-Objekte — Ringdiagramm (F12), Säulendiagramm Net Debt (F13), deren Datenobjekte und die von think-cell verwalteten Beschriftungen (Jahresachse 2018–2022 auf F13). Die Datenreihen dafür stehen unten.

---

## 1. Vorgehen

**Reihenfolge nach Skill:** Material sichten → Storyline prüfen → Financial Model prüfen → Kapitel 2 schreiben → in die vorhandenen Boxen füllen → prüfen.

**Material, das vorlag und ausgewertet wurde**

| Quelle | Woher | Wofür |
|---|---|---|
| `20240305_Stadtwerke Duisburg_v4 1 (1).pptx` | Projekt | Bogen, Template, alle Boxen |
| `Wiesbaden_HRB_2105_*.pdf` (4 Dateien) | Unternehmensregister | Jahres-/Tätigkeitsabschlüsse **2021–2024** (mit Vorjahr 2020): Anteilsbesitzliste, Verbindlichkeitenspiegel, Rückstellungen, GuV-Anhang |
| `ESWE_Versorgungs_AG_Jahresabschluss_2020-2024.xlsx` | Projekt | Financial Model, Blatt `Overview FS` — **alle Kontrollzeilen stehen auf null** |
| `Geschaeftsbericht-25.pdf` | Projekt | Geschäftsjahr 2025: Kennwerte, Erlös-, Investitions-, Cashflow- und Bilanzkurzfassung, Prognosebericht, Projekte |
| `Briefing_ESWE_Versorgungs_AG.md` | Projekt | Einstieg; jede übernommene Zahl gegen Primärquelle geprüft |
| `20260813_Metzler_evm AG_vF.pdf` | Projekt | jüngste vergleichbare Unterlage — als Stil- und Formulierungsreferenz für Kapitel 2 herangezogen |

Nicht vorhanden und deshalb nicht verwendet: Handelsregisterauszug zur WVV-Beteiligungskette, Wirtschaftsplan/Mittelfristplanung, Beschlussfassung zur Kommunalen Wärmeplanung.

**Grundregel eingehalten:** Es wurden keine neuen Textfelder angelegt. Der gesamte Text steht in den vorhandenen Platzhaltern und Boxen. Einzige Ausnahme, vom Skill ausdrücklich gedeckt: In der Capex-Zeile auf Folie 13 hatten zwei der sieben Spalten kein Wertfeld — dort wurde ein **vorhandenes Wertfeld derselben Art dupliziert** (nicht neu gezogen), damit es Format und Größe erbt.

---

## 2. Was inhaltlich auf den Folien steht

**F9 Kapiteltrenner / F3 Agenda / Kolumnentitel F10–F14** — durchgängig „ESWE Versorgungs AG – Übersicht und Herausforderungen“, wortgleich in Agenda, Trenner und allen fünf Kapitelkolumnen.

**F10 Unser Verständnis der Ausgangslage** — Kernsatz im Kasten („Umsetzung eines deutlich steigenden Investitionsprogramms bei zeitgleicher Wahrung finanzieller und strategischer Flexibilität“) und sieben Bullets in der Dramaturgie des Skills: Markt → Geschäftsmodell → Ergebnisbeleg → Klimaziel → kommunale Rolle → Investitionsprogramm → vertragliche Verpflichtungen. Jeder Bullet trägt mindestens eine Zahl oder einen Eigennamen.

**F11 Beteiligungsstruktur** — Gesellschafterebene (WVV Wiesbaden Holding 50,62 % / Thüga AG 49,38 %), darunter vier verbundene Unternehmen und ein Sammelknoten „Beteiligungen“, darunter die sechs nicht beherrschenden Beteiligungen. Alle Quoten, Eigenkapital- und Jahresergebniswerte aus der Anteilsbesitzliste nach § 285 Nr. 11 HGB **zum 31.12.2024**. EAV-bedingte Nullergebnisse sind per Fußnote als solche gekennzeichnet.

**F12 Kunden und Infrastruktur** — sechs Kennzahlkacheln jeweils mit Vorjahreswert (Umsatz, EBT, Unternehmensergebnis, Investitionen, Beschäftigte, EK-Quote), vier Netzkacheln (Strom-, Gas-, Wasser-, Fernwärmenetz), Geschäftsmodellblöcke Strom/Gas/Wärme/Wasser/Sonstiges mit Absatzmengen und Verbrauchsstellen 2025, Summenbezug `100 % ≙ 473,8 Mio. EUR`.

**F13 Investitionsbedarf** — links Verschuldungsentwicklung mit Net-Debt/EBITDA-Faktoren 2,0x → 2,4x → 1,5x → 1,3x → 1,2x, rechts sieben Investitionsschwerpunkte in der Gliederung des Geschäftsberichts 2025 mit Capex 2025 je Schwerpunkt und je zwei bis drei konkreten Projekten.

**F14 Financials** — vollständige Tabelle 2020–2024 (GuV, Kapitalflussrechnung, Bilanzpositionen), sechs nummerierte Kommentare, die den Nummernkreisen in der Tabelle folgen, und der vorsichtig formulierte Schlusssatz.

---

## 3. Die wichtigste fachliche Rückfrage: Der Bogen trägt — aber anders als in Duisburg

`storyline.md` verlangt vor dem Schreiben die Prüfung, ob es wirklich eine Schere zwischen Investitionsprogramm und Innenfinanzierungskraft gibt. Für ESWE lautet die Antwort **ja, aber nicht über die Verschuldung**:

- **Die Verschuldung ist gerade kein Engpass.** Net Debt / EBITDA fällt über fünf Jahre von 2,0x auf 1,2x, die EK-Quote liegt mit 27,6 % (2024) bzw. 28,5 % (2025) über dem eigenen Zielwert von 25 %. Ein Deck, das hier Anspannung behauptet, wäre im Termin sofort widerlegt.
- **Der Engpass ist die Ergebnisverwendung.** Über EAV und Ausgleichszahlung fließt das Jahresergebnis **vollständig** ab — 2024 78,3 Mio. EUR. Einzige Thesaurierung in fünf Jahren: 10,0 Mio. EUR in 2023. Innenfinanzierung besteht damit praktisch nur aus Abschreibungen.
- **Und die Liquidität ist bereits aufgezehrt.** Der Finanzmittelfonds fällt von 45,0 (2023) über 21,5 (2024) auf **2,5 Mio. EUR** (31.12.2025), während die Investitionen von 27,5 auf 37,0 Mio. EUR steigen und die Gesellschafter 10 Mio. EUR Eigenkapital nachschießen mussten.

Kapitel 2 ist entsprechend gebaut: Titel und Kernsätze argumentieren über die **gebundene Innenfinanzierung**, nicht über eine hohe Verschuldung. Der Kernsatz auf F13 erkennt die Verschuldung ausdrücklich als tragfähig an.

> **Bitte bestätigen:** Ist dieser Dreh (gebundene Innenfinanzierung statt Verschuldungsdruck) so gewollt? Er ist aus den Zahlen belegbar, verschiebt aber die Stoßrichtung gegenüber der Duisburg-Vorlage und damit auch die Anknüpfung von Kapitel 3.

---

## 4. Offene Punkte

**Fachlich — hier ist eine Entscheidung nötig, kein Formulierungsvorschlag**

1. **Das Investitionsprogramm ist öffentlich nicht beziffert.** Der Lagebericht 2025 sagt nur, das Investitionsvolumen werde „sich in den nächsten Jahren nochmals erheblich steigern“. Damit fehlt genau die Zahl, die nach `storyline.md` die Achse der Unterlage ist. Auf den Folien steht deshalb an drei Stellen ausdrücklich, dass keine Bezifferung vorliegt (Fußnoten F10, F13 und die Zeile „Ausblick“). **Wenn eine Größenordnung aus der Kommunalen Wärmeplanung, dem Wirtschaftsplan 2026 oder einem Gespräch vorliegt, sollte sie eingesetzt werden** — sie macht den Unterschied zwischen einem starken und einem nur soliden Kapitel 2.
2. **Adressat und Anlass sind nicht bekannt.** Vorstand, Aufsichtsrat oder Gesellschafter (Stadt / Thüga)? Erstkontakt oder Fortsetzung? Beides bestimmt Tonlage und Gewicht der Kapitel; Kapitel 2 ist derzeit für einen Vorstandsadressaten beim Erstkontakt geschrieben.
3. **Bewertung der Ergebnislage.** 2024 ist als sondereffektgetrieben benannt und quantifiziert (20,6 Mio. EUR Rückstellungsauflösungen). Ob 2025 (EBT 52,4 Mio. EUR) als „normalisiert, aber robust“ oder als „weiterhin über Plan“ eingeordnet werden soll, ist eine Wertung — derzeit steht die vorsichtigere Variante.
4. **Zeitraum der Financial-Tabelle.** Sie zeigt 2020–2024, weil nur diese Jahre im Modell stehen und alle Kontrollzeilen tragen. Der Jahresabschluss 2025 ist noch nicht im Unternehmensregister offengelegt; die 2025er Werte aus dem Geschäftsbericht sind in den Kommentaren verarbeitet. **Soll auf 2021–2025 umgestellt werden?** Dann müssten die Kurzfassungen des Geschäftsberichts 2025 ins Modell übernommen werden — Gesamtleistung und Rohertrag 2025 sind daraus allerdings nicht exakt ableitbar (sonstige betriebliche Erträge werden nicht einzeln ausgewiesen).
5. **WRT Infrastruktur GmbH** (Gemeinschaftsunternehmen Tief-/Rohrleitungsbau, gegründet 2024) taucht weder im Jahresabschluss 2024 noch im Geschäftsbericht 2025 auf, nur im Briefing. Sie steht deshalb **nicht** im Strukturschaubild, sondern nur in der Fußnote von F11. Wenn Quote und Kennzahlen vorliegen, gehört sie ins Schaubild.

**In PowerPoint nachzuziehen — bewusst nicht programmatisch gemacht**

6. **Diagrammdaten in think-cell** (Datenreihen siehe Abschnitt 5): Ringdiagramm F12, Säulendiagramm Net Debt F13 samt Jahresachse (steht noch auf 2018–2022).
7. **Bildmaterial.** Alle Duisburger Logos wurden entfernt (Aufstellung unten). Auf F11 tragen die Gesellschaftskästen jetzt **Text statt Logo** — falls ESWE-Logos gewünscht sind, gehören sie in dieselben Kästen. Auf F13 fehlt in der Spalte „Wasser“ ein Motiv (das Zoo-Foto wurde entfernt); die Spalte „Gas“ hat das Rohrleitungsmotiv aus dem Deck erhalten.
8. **Textlängen visuell prüfen.** Die Datei ließ sich hier nicht rendern (LibreOffice kann sie wegen der OLE-Objekte nicht öffnen), die Passung wurde rechnerisch über Boxmaße abgeschätzt. Genauer anzusehen: die Projektspalten „Gas“ und „Gemeinsame Bereiche“ auf F13 (niedrige Kästen) und der Bullet 2 auf F10 (längster Bullet).
9. **Folie „Strategische Stoßrichtungen“ fehlt.** Die Duisburg-Vorlage hat sie nicht; die Landkarte des Skills und die evm-Unterlage sehen sie als Brücke zu Kapitel 3 vor. Vorschlag: F10 duplizieren und mit folgenden fünf Stoßrichtungen füllen (aus Lagebericht und Geschäftsbericht 2025, in der Sprache des Unternehmens):
   - *Wärme:* Fortsetzung des Fernwärmeausbaus in der Innenstadt, Anbindung des Müllheizkraftwerks und Entwicklung der Erzeugungsbasis in Richtung Klimaneutralität bis 2045 im Teilprojekt Transformation Fernwärmenetz
   - *Strom:* konsequente Fortführung der Investitionen in Modernisierung und Digitalisierung der Netzinfrastruktur für Wärmepumpen, Ladeinfrastruktur und neue Erzeugungsanlagen
   - *Gas:* Prüfung der Wasserstofftauglichkeit und der Rückbauperspektiven des Gasnetzes, erstmals unterlegt mit einer Ansammlungsrückstellung für Stilllegung und Rückbau
   - *Kunde und Vertrieb:* Weiterentwicklung kundenorientierter Produkte in Photovoltaik, Elektromobilität und Wärmelösungen sowie Fortführung des wieder aufgenommenen überregionalen Vertriebs
   - *Wasser und Telekommunikation:* Zielnetzplanung mit Hessenwasser einschließlich Neubau der Riedleitung sowie zielgerichteter Infrastruktur- und Rechenzentrumsausbau gemeinsam mit WiTCOM
10. **Außerhalb Kapitel 2** stehen weiterhin Duisburg-Bezüge: Titelfolie (Adressaten Brauers/Schulte), Folie 20 („…die Stadtwerke Duisburg bei strategischen Überlegungen zu beraten“) sowie die Handlungsoptionen in Kapitel 3. Auftragsgemäß nicht angefasst.

---

## 5. Datenreihen für think-cell

**F13 — Net Debt (Mio. EUR) und Net Debt / EBITDA**

| | 2020 | 2021 | 2022 | 2023 | 2024 |
|---|---|---|---|---|---|
| Net Debt | 71,9 | 84,4 | 77,3 | 75,0 | 106,9 |
| Net Debt / EBITDA | 2,0x | 2,4x | 1,5x | 1,3x | 1,2x |

Net Debt = Verbindlichkeiten gegenüber Kreditinstituten (66,1 / 79,0 / 98,7 / 110,7 / 119,9) + Rückstellungen für Pensionen (8,9 / 9,0 / 9,2 / 9,2 / 8,5) − Kassenbestand (3,0 / 3,6 / 30,6 / 45,0 / 21,5). Die Faktorenkästchen über den Säulen sind bereits gefüllt; die Jahresbeschriftung gehört ins think-cell-Datenblatt.

**F12 — Ring Umsatzerlöse 2025 (100 % ≙ 473,8 Mio. EUR)**

| Segment | Mio. EUR | Anteil |
|---|---|---|
| Stromversorgung (inkl. Handelsgeschäfte) | 190,0 | 40,1 % |
| Gasversorgung (inkl. Handelsgeschäfte) | 155,7 | 32,9 % |
| Wärmeversorgung | 43,7 | 9,2 % |
| Betriebsführung Wasserversorgung | 32,6 | 6,9 % |
| Konzerninterne Dienstleistungen | 20,2 | 4,3 % |
| Wasserverkauf an WLW | 16,9 | 3,6 % |
| Übrige Umsatzerlöse | 14,7 | 3,1 % |

Das manuelle Ringlabel „1 %“ aus der Duisburg-Fassung wurde geleert; die Segmentbeschriftung kommt mit dem think-cell-Diagramm.

---

## 6. Prüfergebnis

`python3 scripts/inspect_deck.py … --check` — Vorher 9 Befunde, jetzt 7. **Alle Befunde in Kapitel 2 sind beseitigt:**

| Befund in der Vorlage | Status |
|---|---|
| F12 Arbeitsnotiz „WIP: Wind ~14,2 MW …“ (außerhalb des sichtbaren Bereichs) | entfernt |
| F13 Quell-URL „https://bericht.dvv.de/#swdu-erzeugung / Seite 40 DVV“ | entfernt |

Die verbleibenden 7 Befunde betreffen ausschließlich Kapitel 1 und 3 (leere Quellenzeilen F16–F19, leere Kapitelkolumnen F2 und F20) und einen Template-Effekt auf F13, der auch in der Vorlage besteht: Die sichtbare Quellenzeile liegt dort in einer kopierten Textbox statt im Platzhalter ph:14 — sie ist gefüllt, der Prüfer sieht nur den leeren Layout-Platzhalter.

**Prüfliste des Skills, Kapitel 2**

- **Aussage** — Jeder der fünf Folientitel ist ein vollständiger Aussagesatz. Der Bogen läuft: solide aufgestellt → kommunal und strategisch verankert → Substanz und Ertragsstruktur → Investitionsbedarf steigt bei gebundener Innenfinanzierung → das ist aus dem operativen Cashflow nicht darstellbar.
- **Zahlen** — Jede Zahl der Financial-Tabelle wurde gegen `Overview FS` nachgerechnet (Umsatz, Wachstum, Gesamtleistung, Rohertrag, sämtliche Margen, EBITDA, EBIT, EAT, Ergebnisverwendung, Cashflows, Kassenbestand, Net Debt, EK-Quote — alle Werte stimmen). Alle Kontrollzeilen des Modells stehen auf null. Einheiten: T€ im Modell, Mio. EUR auf den Folien, nirgends vermischt. Stichtage überall genannt.
- **Quellendifferenzen dokumentiert** — drei Stück, jeweils per Fußnote auf der Folie erklärt:
  (a) EBT 2024: 84,3 Mio. EUR laut Jahresabschluss (vor sonstigen Steuern) gegen 83,8 Mio. EUR laut Geschäftsbericht 2025 (nach sonstigen Steuern);
  (b) Beschäftigte: 663 zum 31.12.2025 laut Geschäftsbericht gegen Ø 608 laut Jahresabschluss 2024;
  (c) Cashflow 2022: Der Jahresabschluss 2023 gliedert die Vorjahreswerte um (78,0 / −34,0 / −17,0 statt 95,4 / −44,9 / −23,5) — angesetzt ist die Fassung des Jahresabschlusses 2023, so wie im Modell dokumentiert.
  Zusätzlich vermerkt: Der Geschäftsbericht 2025 weist die Investitionen 2024 anders gegliedert aus als der Jahresabschluss 2024 (Wegfall der Zeile „Telekommunikation“); die Summe 27,5 Mio. EUR ist identisch. Auf der Folie stehen deshalb ausschließlich die 2025er Werte.
- **Mechanik** — Keine fremden Mandantennamen mehr in Kapitel 2 (Volltextsuche über Titel, Boxen, Tabellen und Fußnoten auf 14 Duisburg-Begriffe: null Treffer). Keine WIP-Notizen, keine Quell-URLs, auch nicht außerhalb des sichtbaren Bereichs. Keine neu gezogenen Textfelder. Diagramme unverändert think-cell. Agenda, Kapiteltrenner und alle fünf Kolumnentitel nennen denselben Kapitelnamen. Datei öffnet fehlerfrei, keine doppelten Shape-IDs.

**Entfernte Elemente (alle Duisburg-spezifisch, jedes einzeln geprüft)**

| Folie | Entfernt |
|---|---|
| F11 | 14 Logos (Stadt Duisburg, DVV, RheinEnergie, Stadtwerke Duisburg, DVG, Netze Duisburg, DuisburgCity, octeo, energieGUT, SWDU Energiehandel, Thermoplus, Wasserbeschaffung Niederrhein, Zoo Duisburg, Fernwärme Duisburg); Kasten des zweiten SWDU-Gesellschafters samt Verbindungslinie und Quoten 80,0 % / 20,0 %; Direktlinie Stadt → Tochter samt Quote 25,8 %; Legende „Gesprächsfokus 5.3.2024“ |
| F12 | WIP-Notizkasten und ein Screenshot einer Duisburg-Recherche (beide außerhalb des sichtbaren Folienbereichs); 12 Duisburger Logos |
| F13 | WIP-Kasten mit Quell-URLs und fünf Ablagebilder (alle außerhalb der Folie); Zoo-Foto; 9 Duisburger Logos |

Alle sieben verbliebenen Bildmotive auf F13 sind generische Stockfotos (Strommast, Fernwärmeleitung, Rohrleitungsbau, Photovoltaik/Wind, Glasfaser, Gebäude) und passen zu den neuen Spaltenüberschriften.
