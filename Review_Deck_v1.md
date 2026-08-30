# Review Deck v1 (2026_08_30_ESWE_AG_v1.pptx) — Stand 30.08.2026

Vollprüfung: Alle 22 Slides (Text via markitdown, alle 5 Chart-XMLs bis auf Rohdaten), abgeglichen gegen GB 2025, Financials-Excel und die vier HRB-Abschlüsse. LibreOffice-Rendering nicht möglich (think-cell-Objekte) — Layout-/Farbprüfung muss in PowerPoint erfolgen.

## A. BLOCKER — Copy-Paste-Reste und falsche Zahlen (vor jedem Versand fixen)

1. **Titelseite:** „Koblenz / Frankfurt am Main, 28. August 2026" → „Wiesbaden / Frankfurt am Main, [Datum]".
2. **Agenda, Punkt 2:** „evm AG – Übersicht und Herausforderungen" → „ESWE Versorgungs AG – …".
3. **Kapiteltrenner S. 11:** „DVV Duisburger Versorgungs- und Verkehrsgesellschaft mbh – …" → „ESWE Versorgungs AG – Übersicht und Herausforderungen".
4. **Kopfzeile S. 12:** „2. Duisburger Versorgungs- und Verkehrsgesellschaft– …" → ESWE. (Exakt der „Stadtwerke-Krefeld"-Fehler des evm-Decks, vor dem das Briefing warnt.)
5. **Kopfzeilen S. 16, S. 17:** „2. evm AG – …" → ESWE.
6. **Headline S. 19:** „…Positionierung der evm" → „…der ESWE".
7. **Quellenzeilen S. 13, 15, 16, 19:** überall „Jahresabschluss/Jahresabschlüsse evm AG …" bzw. „Jahresabschluss enm 2024" → „Geschäftsbericht ESWE Versorgungs AG 2025" bzw. „Jahresabschlüsse ESWE Versorgungs AG 2021–2025". S. 19 zudem „2024-2025" → „2024–2025" (Halbgeviertstrich).
8. **S. 13, Netz-Kacheln VERTAUSCHT:** Deck zeigt „Gasnetz 2025: 2.820 km / Stromnetz 2025: 823 km" — richtig ist **Stromnetz ~2.820 km (sw netz), Gasnetz ~823 km (ESWE direkt)**.
9. **S. 16, Chart Kapitalflussrechnung, Jahr 2023 VERTAUSCHT:** Serie Operating CF trägt 8,9 und Investing CF +47,3 — richtig: **OCF 47,3 / ICF +8,9**. Die ∑ (14) bleibt gleich, darum fällt es optisch kaum auf, die Stapel-Farben sind aber falsch.
10. **S. 16, Headline grammatisch defekt:** „Die Ertragskraft bleibt nach zwei Sonderjahren robust, Ausschüttungen und Investitionshochlauf die Liquidität weitgehend absorbieren" — es fehlt „während": „…robust, **während** Ausschüttungen und Investitionshochlauf die Liquidität weitgehend absorbieren".

## B. Zahlen- und Chartprüfung (verifiziert bzw. inkonsistent)

**Verifiziert korrekt:**
- Donut S. 13: 40,1/32,9/10,4/9,2/7,4 % — exakt, summiert auf 100 ✓
- Net-Debt-Reihe S. 15/16: 75,4/68,0/65,8/98,4/121,7 Mio. EUR — gegen die HRB-Anhänge geprüft (Bankverbindlichkeiten 79,0/98,7/110,8/119,9/124,2 abzgl. Kasse) ✓; Multiples 2,2x/1,3x/1,1x/1,1x/2,7x ✓
- GuV-Chart Umsätze, CF-Reihen (außer 2023-Tausch), Kasse-Reihe, EK-Quoten-Ovale ✓
- Beteiligungsslide S. 14: alle EK-/Ergebniswerte ✓, WRT-Fußnote (JA 2024) ✓, KMW-Ausschüttungs-Fußnote ✓

**Inkonsistent / zu fixen:**
11. **S. 16, Rohertrag-Definition vs. Margen-Ovale:** Die Säulen zeigen 118/124/153/150/134 (= Gesamtleistung ./. Materialaufwand, also inkl. aktivierter Eigenleistungen), die Ovale aber 27,0/25,1/23,7/27,6/27,9 % (= berechnet auf Umsatz ./. Materialaufwand: 115/119/150/147/132). Entweder Säulen auf 115/119/150/147/132 ändern (Empfehlung, dann stimmen die Ovale) oder Ovale auf 27,7/26,0/24,1/28,1/28,4 % anheben — und in jedem Fall Fußnote „Rohertrag = Umsatzerlöse ./. Materialaufwand" ergänzen.
12. **S. 15/16, Net-Debt-Fußnote falsch:** Fußnote 2 definiert die volle evm-Formel (inkl. Pensionsrückstellungen und verbundener Unternehmen), berechnet ist aber die vereinfachte Variante. → „Net Debt = Verbindlichkeiten gegenüber Kreditinstituten ./. liquide Mittel".
13. **S. 15, Fußnote 1 falsch:** „Keine öffentliche quantitative Aufteilung nach Investitionsschwerpunkten verfügbar" — stimmt für evm, nicht für ESWE: Die Abschlüsse weisen die Investitionen je Unternehmensbereich aus (2025: Wärme 6,5 / Wasser 14,0 / Strom+Gas 4,0 / Beteiligungen 5,2 / Summe 37,0). Empfehlung: echte Beträge in die CapEx-Zeile je Spalte, Fußnote streichen.
14. **S. 15, Takeaway passt nicht zum Chart:** Text argumentiert mit CapEx/Abschreibungen (1,8–3,7x), das Chart zeigt Net Debt. Entweder Takeaway wechseln („Die Nettoverschuldung ist 2025 auf das 2,7-fache des EBITDA gestiegen, obwohl der Investitionshochlauf erst bevorsteht" — 123 Z.) oder Chart auf die CapEx-Variante des Drehbuchs umstellen.
15. **S. 13, EBIT-Kachel:** „73.3 Mio. EUR (2024)" — englischer Dezimalpunkt und einzige Kachel mit Nachkommastelle → „73 Mio. EUR"; zudem fehlt eine Fußnote zur EBIT-Definition (= Betriebliches Ergebnis, ohne Beteiligungsergebnis von 25 Mio. EUR — sonst wirkt EBIT 29 gegen EAT 49 unplausibel). Alternativ wie im Briefing empfohlen EBT (53) zeigen.
16. **S. 13, Mitarbeiter-Kachel „ca. 644":** Basis fehlt → Fußnote „Jahresdurchschnitt 2025 inkl. Auszubildende" (+ Vorjahr kursiv 608 ergänzen, alle anderen Kacheln haben Vorjahreswerte).
17. **S. 13, Gasverkauf-Callout:** „Rückverkauf beschaffter Gasmengen zur Portfoliooptimierung" ist im GB 2025 nicht belegt — ersetzen durch das Belegte: „Wiederaufnahme des überregionalen Vertriebs (+11,3 % außerhalb Wiesbadens)".
18. **80-Mio.-Leitmotiv (S. 12 Bullet + Banner, S. 15 Klammer):** Quelle ist ein nicht datierbares zfk-Interview des Ex-CEO; Ist-Werte 43/54/27/27/37 haben die 80 nie erreicht. Wenn behalten: zwingend Quellenfußnote („gemäß Interview des früheren Vorstandsvorsitzenden, zfk"); Empfehlung laut Drehbuch: auf das belegbare Leitmotiv wechseln (Lagebericht-Zitat + CapEx/AfA 2,3x + Kapitaleinlagen + Kasse 2,5).

## C. Storyline und aktuelle Themen

19. **S. 12: Aktionärsstruktur-Bullet fehlt** (evm-Vorlage hat 7 Bullets, hier 6). Gerade weil Kapitel 3 auf der 50,62/49,38-Leitplanke aufbaut, sollte die duale Struktur in der Ausgangslage stehen: „Duale Aktionärsstruktur seit 2001: 50,62 % Landeshauptstadt Wiesbaden (über die WVV), 49,38 % Thüga AG als strategischer Partner; Gewinnabführung an die WVV, Ausgleichszahlung an die Thüga".
20. **S. 16, Kommentar-Bullet 2** endet nach „…20,6 Mio. EUR im Jahr 2024" — der zweite Halbsatz („mit einem EBT von 53 Mio. EUR deutlich über Plan markiert 2025 die Normalisierung") fehlt; ohne ihn fehlt die Normalisierungs-Botschaft, die die Headline trägt.
21. **Regulierungsrisiko RAMEN/NEST** kommt im Deck nirgends vor (GB 2025: „erhebliche Einbußen im Netzergebnis" befürchtet). Laut Drehbuch bewusst Moderation — vertretbar, aber vor allem falls sw netz auf S. 20 zum Vorschlag wird, gehört der Caveat mindestens in die Sprechnotiz.
22. **S. 20 ist noch die unveränderte evm-Slide** (Wärme/Netze SPV, evm-Assets, „Vorteile für die evm AG") — bekannt, hier kommt der gedraftete Inhalt rein (zwei Vorschläge: sw-netz-Minderheit + Kapitalpakt). Die auf S. 14 gesetzte Verweis-Marke „Mögliche Beteiligungsobjekte (Kapitel 3)" passt gut dazu.
23. **Eigene Notizen im Deck (S. 16):** „JÜ vor Gewinnabführung zeigen anstatt Jahresüberschuss / Net Debt / EBITDA" — vor Versand löschen. Inhaltlich: EAT 49 ist bereits der JÜ vor Abführung (Bilanzgewinn nach Abführung = 0), die Notiz ist also erledigt.

## D. Schreibweise (Satz-Regel) und Kleinigkeiten

24. **S. 12, Bullet 6 und Banner:** nutzen noch die Gedankenstrich-Konstruktion („…steigern' — von Ø ~22 auf …"); ausformulierte Fassungen stehen im Drehbuch.
25. **S. 14, Headline:** „…gebündelt − die Ergebnisbeiträge kommen aus…" → „…gebündelt, deren Ergebnisbeiträge vor allem aus sw netz, WiTCOM und KMW stammen".
26. **S. 15/16/17-Headlines:** S. 15 und die Takeaways tragen noch „−"-Konstruktionen; Drehbuch-Fassungen mit „während/obwohl" verwenden.
27. **S. 13, Icon-Leiste:** „Energie" → „Energieerzeugung"; Tippfehler „Energiedienstleistugen" → „Energiedienstleistungen".
28. **S. 13, Fußnote 2 abgeschnitten:** „…Gasnetz der ESWE Versorgungs" → „…der ESWE Versorgungs AG (Wiesbaden, Taunusstein, Schlangenbad, Walluf); Jahresstand der Netzlängen verifizieren".
29. **S. 14:** „Betrieb des Stromnetzes in Wiesbaden" → „…in Wiesbaden und Taunusstein"; Einheiten mischen sich („0,1 Mio. EUR" neben „25 T EUR") — einheitlich T EUR oder Mio. mit einer Nachkommastelle.
30. **S. 16, Fußnote 1 Leftover:** „nEHS: nationales Emissionshandelssystem" — nEHS kommt auf der Slide nicht vor; ersetzen durch Rohertrag-Definition + Rundungsfußnote.
31. **S. 21:** Tippfehler „Projektenund Investoren" (Leerzeichen fehlt); prüfen, ob der Pfeil „➔ keine Interessenkonflikte" im Original-Glyph erhalten ist.
32. **S. 16, CAGR-Badge:** Wert im Text nicht auslesbar — prüfen, dass dort „+2,7% p.a." steht (nicht evm-„+4%").
33. **S. 22:** leer — sicherstellen, dass der Disclaimer über das Layout kommt (wie im DVV-Deck) und im Export sichtbar ist.
