# Handoff ESWE-Unterlage — Stand 30.08.2026 abends

**Deck:** `2026_08_30_ESWE_AG_v1.pptx` (23 Slides, Stand nach zweitem Review) · **Referenzen im Repo:** `ESWE_Slide_Drehbuch.md` (finale Texte je Slide), `Briefing_ESWE_Kapitel_2_3_v2.md` (Zahlen), `Review_Deck_v1.md` (Erst-Review), `research/` (Quellanalysen).

## Status

Kapitel 1, Trenner, Titelseite, Agenda: fertig. Kapitel 2 inhaltlich fertig bis auf Chart-Fixes und Kleinkram. Kapitel 3 komplett gebaut (Ziele-Slide + sw-netz-Beispielstruktur mit Asset-Liste). Alle DVV-/Duisburg-/Koblenz-Reste sind raus. Die Net-Debt-Reihe (75/68/66/98/122) und alle übrigen Chartdaten sind gegen HRB-Abschlüsse und GB 2025 verifiziert.

## Restliste (geschätzt ~1,5 h)

**A. Suchen & Ersetzen (~20 Min.)**
1. Vier Quellenzeilen mit „evm"/„enm" (S. 13, 16, 17, 20) → „Quellen: Metzler-Recherche, Geschäftsbericht ESWE Versorgungs AG 2025, Unternehmenswebsite" (S. 13) bzw. „…, Jahresabschlüsse ESWE Versorgungs AG 2021–2025, Unternehmenswebsite" (S. 16, 17); S. 20: „…2024–2025" (Halbgeviertstrich). Kontrolle: Suchlauf „evm" und „enm" über die Datei muss null Treffer liefern.
2. S. 17: Platzhalter „xxx" ersetzen durch „1) Rohertrag = Umsatzerlöse ./. Materialaufwand; 2) Abweichungen der Säulensummen rundungsbedingt"; eigene Notizen im Notizenfeld löschen.
3. S. 21: „75.1%"/„24.9%" → „75,1 %"/„24,9 %"; Fußnote ersetzen durch „1) Beteiligungshöhen illustrativ; Mitspracherechte des Investors werden vertraglich über die Gesellschaftervereinbarung abgebildet; Struktur ähnlich übertragbar auf die weiteren aufgeführten Assets"; Chart-Label „Stromnetz Wiesbaden" → „Stromnetz Wiesbaden und Taunusstein".
4. S. 16 Fußnote: „gegen Kreditinstituten" → „gegenüber Kreditinstituten".
5. S. 13: Fußnoten neu nummerieren (aktuell zweimal „2)"): 1) EBIT-Definition, 2) EAT, 3) Netzlängen; Fußnote 3 vervollständigen („…Gasnetz der ESWE Versorgungs AG"); Icon-Leiste: „Energie" → „Energieerzeugung", Tippfehler „Energiedienstleistugen" → „Energiedienstleistungen".

**B. Storyline-Fixes (~25 Min.)**
6. **S. 21 Banner ergänzen (wichtigster Punkt):** „Flankierend stärkt ein Kapitalpakt der Aktionäre aus planbaren Einlagen, Thesaurierungspfad und Nachrangkapital die Eigenkapitalbasis ohne jede Strukturveränderung" — erst damit haben die Ziele 3, 4 und 6 von S. 20 eine Antwort.
7. **S. 12 siebter Bullet ergänzen** (bereitet Ziel 2 vor, evm-Vorlage hat sieben): „Duale Aktionärsstruktur seit 2001: 50,62 % Landeshauptstadt Wiesbaden (über die WVV Wiesbaden Holding), 49,38 % Thüga AG als strategischer Partner; Gewinnabführung an die WVV, vertragliche Ausgleichszahlung an die Thüga"
8. **S. 12/16, 80-Mio.-Zahl:** bleibt laut Entscheidung — dann Quellenfußnote setzen: „Anstieg gemäß Interview des früheren Vorstandsvorsitzenden (zfk); Ist-Investitionen 2021–2025: 43 / 54 / 27 / 27 / 37 Mio. EUR". Ohne Fußnote ist die prominenteste Zahl des Decks die am schwächsten belegte.
9. **Leere S. 15 löschen** (bricht den Fluss zwischen Beteiligungen und Investitionen) — oder bewusst befüllen.

**C. think-cell (~30 Min.)**
10. S. 17 Kapitalflussrechnung, Jahr 2023: Operating (47,3) und Investing (+8,9) sind vertauscht — im Datenblatt drehen. Summe 14 bleibt gleich, nur die Stapel stimmen dann.
11. S. 17 GuV: Rohertrag-Säulen auf 115 / 119 / 150 / 147 / 132 stellen (aktuell 118/124/153/150/134 = inkl. aktivierter Eigenleistungen) — dann passen die vorhandenen Margen-Ovale 27,0/25,1/23,7/27,6/27,9 %. CAGR-Badge prüfen: „+2,7% p.a.".

**D. Schlussrunde**
12. PDF-Export: Disclaimer auf letzter Seite sichtbar? Kopfzeilen-Klick durch alle Kap.-2/3-Slides; Suchläufe „evm", „enm", „xxx", „TODO"; Seitenzahlen.

## Offene Verifikationspunkte (nicht deckkritisch, vor dem Termin)
- Stand Stromkonzession Wiesbaden (Sonderkündigungsrecht der Stadt ab 2025) — bewertungsrelevant für die sw-netz-Struktur
- EnWG-Entflechtungsprüfung für einen Netz-Minderheitsgesellschafter (lenkt Auswahl auf Finanzinvestoren)
- Konditionen Hessischer EnergieFonds (WIBank) für die ESWE
- Gasverkauf-Callout S. 13 „Rückverkauf zur Portfoliooptimierung" ist im GB nicht belegt — ersetzen durch „Wiederaufnahme des überregionalen Vertriebs" oder intern bestätigen

## Kernbotschaften für den Termin (Spickzettel)
- Leitfrage: Wie finanziert die ESWE ein sich vervielfachendes Investitionsprogramm, ohne Flexibilität zu verlieren? (Kasse 2,5 Mio., Net Debt/EBITDA 2,7x, Kapitaleinlagen bereits nötig)
- Leitplanke: 50,62/49,38 schließt Eigenkapital Dritter auf AG-Ebene aus → Kapital kommt unterhalb der AG (sw netz) oder verwässerungsfrei (Kapitalpakt/Nachrangkapital)
- 75,1/24,9 statt 74,9/25,1: ESWE behält die Dreiviertelmehrheit (§ 53 GmbHG); Sperrminorität ist Verhandlungsmasse, Schutzrechte laufen über Reserved Matters; Sub-25-Modelle sind im Haus gelebt (MHKW 24,5 %); 24,9 % kann zudem unter der 25-%-Schwelle der Fusionskontrolle (§ 37 GWB) bleiben
