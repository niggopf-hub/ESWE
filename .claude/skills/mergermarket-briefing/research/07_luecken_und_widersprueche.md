# Lückenanalyse Transkript → SKILL.md

Geprüft gegen die SKILL.md-Fassung vom 17.09.26 (inkl. der neu ergänzten Abschnitte
„Drei Abgrenzungen" und „Nur aus der Meldung" in 6.2). Referenzdateien unter
`research/` wurden zur Abgrenzung mitgelesen; gemeldet wird nur, was in **SKILL.md
selbst** fehlt oder ihr widerspricht. Alle Zeilenangaben beziehen sich auf
`briefing_utf8.txt`.

---

## FEHLT IM SKILL

### 1. Der Mail-Rahmen fehlt komplett — und SKILL.md sagt sogar das Gegenteil
**Beleg:** Z. 2207–2209, 2237–2239, 2253–2254, 2260–2262, 2277–2278 (Nico → Robert);
Z. 1346–1348, 1461–1463 (Robert → Verteiler); Z. 1368 (Nutzer erklärt die Unterscheidung).

> „Guten Morgen Robert,\n\nanbei das Mergermarket Briefing der letzten Woche." … „Viele Grüße\nNico" (Z. 2207/2209/2253)
> „Liebe Kollegen,\n\nnachfolgend schicke ich euch die Zusammenfassung der Mergermarket Intelligence der letzten Woche." (Z. 1346/1348)
> Nutzer: „die finale abgeschickte, **die beginnt immer mit liebe kollegen** sodass du außeinanderhalten kannst" (Z. 1368)

Es gibt zwei feste Rahmen: (a) Entwurf an Robert, (b) Roberts Weiterleitung an den
Verteiler. SKILL.md Abschnitt 8 schreibt dagegen „kein Vorspann" — das gilt nur für
den Chat-Output, nicht für die Mail. Der Rahmen steht zwar in `research/03`, aber
nicht in SKILL.md.
**Wohin:** Neuer Unterabschnitt „8.1 Mailrahmen" vor Block 1.

### 2. Freistehende Mergermarket-Links = hochgeladene Artikel; nie ignorieren
**Beleg:** Z. 6876 (Nutzer), Z. 7223 (Nutzer), Z. 7233 (Zusage), Z. 6880–6894.

> „pls check die einzlenen links sind immer z udenartikeln die als datei quasi hochgeladen werden weil sie so lange sind check dass du die nie ausgelassen hattest" (Z. 6876)
> „wenn freie links dann siend das die angehangenen dokumente – die dann nicht ignorieren sondern dann ohne quelle markiert anzeigen wenn du die da noch nciht zuiordnne kannst" (Z. 7223)
> „Wenn ich einen Link nicht eindeutig zuordnen kann, hänge ich ihn trotzdem an den Eintrag und markiere ihn als ‚Quelle: unzugeordnet', statt ihn wegzulassen." (Z. 7233)

Das ist eine **explizite Nutzeranweisung** und betrifft den Input-Umgang: Der Batch
besteht aus Artikeltexten + separat gepasteten Links; die Links gehören zu
angehängten Dokumenten. Assistent hatte mehrfach „Link ohne Artikel" gemeldet
(Z. 6191, 6420, 6536, 6872, 7219) — das wurde als Fehler korrigiert.
**Wohin:** Abschnitt „Arbeitsweise" / Input-Beschreibung, plus Prüfliste.

### 3. Quellen-URL-Muster inkl. des angehängten `?` steht nirgends in SKILL.md
**Beleg:** Z. 504–517 und durchgängig bis Z. 7967.

> `[Quelle](https://mergermarket.ionanalytics.com/content/1004511570?)` (Z. 517)

Maschinell ausgezählt: 235 Quellen-Links, **alle** auf
`mergermarket.ionanalytics.com/content/<ID>`; 228 davon mit anhängendem `?`, 7 ohne.
Nie auf die im Artikel verlinkte Originalquelle (FAZ, Handelsblatt, PLUTA-PM etc.).
SKILL.md schreibt nur `[Quelle](URL)`.
**Wohin:** Abschnitt 6, direkt unter das Grundformat.

### 4. Financials-Zuordnung: nur Zahlen des Klammer-Trägers, nie Konzernzahlen
**Beleg:** Z. 1329 (SRK/Alexianer), Z. 1861 (Webasto Indien), Z. 4953 (Secop), Z. 5776 (Delivery Hero).

> „die genannten 2,5 Mrd. EUR Umsatz beziehen sich auf den gesamten Alexianer-Konzern, nicht auf das Zielobjekt SRK, daher hab ich die nicht mit reingenommen, um keine falsche Größenordnung für das eigentliche Target zu suggerieren" (Z. 1329)
> „Financials-Klammer bleibt hier bewusst schlank …, da die genannten Finanzkennzahlen sich auf die indische Einheit beziehen, nicht auf Webasto selbst" (Z. 1861)
> „Bei Secop bezieht sich das EBITDA von >40 Mio. EUR auf die zum Verkauf stehenden Assets …, nicht auf die Gruppe" (Z. 4953)
> „der Artikel nennt nur Bookings-Zahlen des kombinierten Unternehmens, keine Delivery-Hero-Einzelzahlen" (Z. 5776)

SKILL.md 6.2 sagt jetzt „nur aus der Meldung", aber nicht, **welche** Zahl aus der
Meldung. Das ist die häufigste inhaltliche Anmerkung im ganzen Transkript.
**Wohin:** Abschnitt 6.2, direkt hinter „Nur aus der Meldung".

### 5. Fallback-Hierarchie der Financials: Mitarbeiterzahl als Anker
**Beleg:** Z. 265 (Giotto.ai), Z. 496 (Squid), Z. 1329 (Klinikum Leverkusen).

> „Als Financials-Anker nutze ich Mitarbeiterzahl (25), da kein belastbarer aktueller Umsatz vorliegt (nur Run-Rate-Prognose für Ende 2026)" (Z. 265)
> „Als Financials-Anker nutze ich die Mitarbeiterzahl (18), da kein Umsatz offengelegt wurde" (Z. 496)

Reihenfolge in der Praxis: Umsatz/EBITDA → sonst Marktkapitalisierung → sonst
Mitarbeiter. Prognose-/Run-Rate-Zahlen gelten nicht als belastbar.
**Wohin:** Abschnitt 6.2, neben Punkt 4.

### 6. Unbelastbare Zahlen weglassen (bestritten, veraltet, unspezifisch)
**Beleg:** Z. 4953 (RTS Wind), Z. 5265 (Swissbit), Z. 2093 (Drooms), Z. 5289 (Bali Treatment), Z. 8003 (Quarkwerk).

> „die im Artikel genannten ~200 Mio. EUR Umsatz / ~15 Mio. EUR EBITDA stammen von Quellen, denen der Eigentümer explizit widerspricht (‚inaccurate'), und die 50 Mio. EUR von der Website sind von 2023" → gar keine Financials gesetzt (Z. 4953)
> „Die 250 Mio. USD sind laut Artikel ‚annual earnings' ohne nähere Spezifikation – ich habe das neutral als ‚Gewinn' übernommen statt EBITDA zu unterstellen" (Z. 5265)
> „Die ‚mid-double-digit million-euro'-Umsatzangabe ist unpräzise aus der Quelle – ich hab sie sinngemäß übernommen statt eine Zahl zu erfinden" → `Umsatz: mittlerer zweistelliger Mio.-EUR-Bereich` (Z. 2093, Zeile Z. 2240)
> „die 200 Mio. EUR sind die Zielgröße des gesuchten Partners, nicht Quarkwerks eigener Umsatz" (Z. 8003, auf Nutzerfrage Z. 8001)

Vier Teilregeln: bestrittene Zahl → weg; Website-Altzahl → weg; unspezifisches
Label → neutral („Gewinn") statt Interpretation; Zielgröße des Suchprofils ≠
eigener Umsatz.
**Wohin:** Abschnitt 6.2.

### 7. Financials-Labels, die tatsächlich benutzt werden, fehlen in der Liste
**Beleg:** maschinelle Auszählung aller `Label:` in Einträgen.

Benutzt, aber **nicht** in SKILL.md 6.2 gelistet:
`EBITDA-Marge:` (12×, z.B. Z. 5273 Webasto „EBITDA-Marge: 40%"), `Gewinn:` (11×, Z. 292
HolidayCheck), `EV-Erwartung:` (8×, Z. 293 GBA „EV-Erwartung: ~15x EBITDA"),
`Feuerkraft:` (6×, Z. 1239 ABB „Feuerkraft: über 13 Mrd. USD"), `Volumen:` (2×, Z. 7205
CSN „Volumen: 1,5 Mrd. BRL"), `Eigenkapitalwert:` (1×, Z. 7967 HCOB).
Umgekehrt: `ARR:` steht in SKILL.md als Klammer-Label, kommt im Transkript aber **nur
im Satz** vor („Zielgröße bis 5-7 Mio. EUR ARR", Z. 4135), nie als Klammer-Label.
**Wohin:** Abschnitt 6.2, Financials-Liste.

### 8. Berater-Labels: `Buy-side Berater:` und `Global-Coordinator-Kandidaten:` fehlen
**Beleg:** Z. 5955–5957, Z. 3011/3043, Z. 20.

> „Nomura ist hier Buy-side-Berater von CIP, kein Sell-side-Berater." → `…, Buy-side Berater: Nomura` (Z. 5955/5957)
> `…, Global-Coordinator-Kandidaten: Deutsche Bank und Goldman Sachs` — wenn Banken genannt, aber noch nicht fix mandatiert (Z. 3011/3043)
> `Sole Global Coordinator:` für den Einzelfall (Z. 20)

SKILL.md 6.3 kennt nur `Sell-side Berater:` und `Global Coordinators:`.
**Wohin:** Abschnitt 6.3.

### 9. „ohne externen Berater" wird explizit geschrieben, wenn der Artikel das sagt
**Beleg:** Z. 291/517 (HelloBetter), Z. 541, Z. 544.

> „HelloBetter – Artikel sagt explizit ‚ohne externen Berater' (das steht ja auch schon so im Eintrag)" (Z. 541)
> Zeile: `… prüft Verkauf ab Juli, ohne externen Berater [Quelle](…)` (Z. 517)
> „Kein Berater im Text = kein Berater im Eintrag." (Z. 544)

SKILL.md 6.3 deckt nur „nicht ergänzen". Der aktive Gegenfall — Artikel sagt
ausdrücklich, dass kein Berater mandatiert ist → das kommt in den Eintrag — fehlt.
**Wohin:** Abschnitt 6.3.

### 10. Konsortien: Partner mit Schrägstrich + „-Konsortium", komplett fett
**Beleg:** Z. 3013/3045/3085/3106/3128/3137, Frage des Nutzers Z. 3129/3133, Antwort Z. 3135.

> `… im Rennen u.a. Astatine/USS-Konsortium und Basalt Infrastructure Partners …` (Z. 3106)
> „In diesem Satz fett zu machen: DBAG, Cartonplast, Astatine/USS-Konsortium, Basalt Infrastructure Partners – also alle Akteure/Bieter." (Z. 3135)

SKILL.md 6.4 sagt nur „Konsortialpartner fett", nicht wie das Konstrukt geschrieben
wird. Der Nutzer hat hier explizit nachgefragt.
**Wohin:** Abschnitt 6.4 oder 6.5.

### 11. Staatliche / kommunale Akteure zählen als normale Akteure und werden fett
**Beleg:** Z. 5941, Z. 6008, Z. 5924, Z. 5652, Z. 1323, Z. 3876.

> „bei Niedersachsen (31.08.) ist das Bundesland als Käufer nicht fett … Da Niedersachsen hier der handelnde Akteur ist, sollte es konsistent auch fett sein." (Z. 5941, erneut Z. 6008)
> Zeile: `31.08.26: Niedersachsen erwägt Rückkauf der knapp 24%-Minderheitsbeteiligung von Sparkassen und Landesbanken an der NordLB (DE, Landesbank) für rund 760 Mio. EUR` (Z. 6024)
> `26.08.26: Saarland-Heilstätten startet Verkauf seiner 50,05%-Beteiligung an Klinikum Idar-Oberstein (DE, Krankenhausbetreiber), Sell-side Berater: Dornbach Health Care` (Z. 6033)
> Klinikum Leverkusen: „kommunaler Krankenhausbetreiber legt Übernahmeangebot … vor" → drin (Z. 1323)

Bundesland, kommunaler Träger, Stadtwerke, öffentliche Klinikholding sind
Akteure wie jeder andere — kein Sonderfall, kein Ausschluss.
**Wohin:** Abschnitt 6.4 (Fettung) und als Satz in Abschnitt 1.

### 12. Prozent- und Beteiligungsformulierungen — feste Muster, nirgends dokumentiert
**Beleg:** Z. 4672, Z. 5269, Z. 6033, Z. 6024, Z. 292, Z. 4137.

> `steht vor Erwerb einer 5%-Beteiligung an FC Bayern München AG (DE, Fußballclub) für 250 Mio. EUR, Bewertung: 5 Mrd. EUR` (Z. 4672)
> `meldet Erwerb von 65% an Quabus (AT, …) zur Kartellprüfung an` (Z. 5269)
> `startet Verkauf seiner 50,05%-Beteiligung an Klinikum Idar-Oberstein` (Z. 6033)
> `erwägt Rückkauf der knapp 24%-Minderheitsbeteiligung von Sparkassen und Landesbanken an der NordLB` (Z. 6024)
> in der Klammer: `…, Burda hält ~88%)` (Z. 292); im Satz: `hält nach Spin-off 51%` (Z. 4137)

Muster: attributiv `X%-Beteiligung an Y` mit Bindestrich; prädikativ `Erwerb von X% an Y`;
Kaufpreis mit `für`, Bewertung als `Bewertung: …`; Stake des Eigentümers in der
Klammer als `Eigentümer hält ~X%`. SKILL.md 6.6 sagt nur, wann Prozente
*gestrichen* werden, nie wie sie geschrieben werden.
**Wohin:** neuer Unterabschnitt 6.2 oder 6.7.

### 13. Mehrere Verkäufer / mehrere Akteure als gemeinsames Satzsubjekt
**Beleg:** Z. 864, Z. 4147, Z. 1243, Z. 6024.

> `14.07.26: CDPQ und Columna Capital beleben Exit-Pläne für Datamars (CH, Agrartechnologie, EBITDA: ~90 Mio. EUR) wieder, Sell-side Berater: Goldman Sachs` (Z. 864)
> `06.08.26: Commerzbank und UniCredit nehmen … Gespräche über gemeinsame Strategie auf …` (Z. 4147)
> `16.07.26: Armira, Flex Capital und Paragon Partners zählen zu den Bietern für Babtec (…)` (Z. 1243)
> Verkäufer-Mehrzahl in der Objektphrase: `… von Sparkassen und Landesbanken an der NordLB` (Z. 6024)

Regel aus der Praxis: mehrere gleichrangige Akteure werden mit Komma/„und" zum
gemeinsamen Subjekt, alle fett, **eine** Klammer beim Zielobjekt.
**Wohin:** Abschnitt 6.1.

### 14. Satzmuster „X und Y zählen zu den Bietern für Z" (Bieter als Subjekt)
**Beleg:** 14 Vorkommen, u.a. Z. 1243, Z. 2247, Z. 4433-Umfeld; Diskussion Z. 2227–2235.

> Nutzer: „ist das nicht irgendwiue ganz anderer satzbau als sosnt immer" (Z. 2227)
> „hier fehlt das Verb komplett … der Satz hat keine zusätzliche Handlung mehr wie sonst üblich" (Z. 2229)

Der Nutzer hat dieses Muster selbst als stilistischen Ausreißer erkannt, es aber
bewusst stehen gelassen (Z. 2256 „past so jettz", Z. 2258). Es ist damit ein
zulässiges, aber schwächeres Muster — SKILL.md 6.5 kennt nur die Anhänge-Variante
`Bieter u.a. …`.
**Wohin:** Abschnitt 6.5.

### 15. Fokus-/Zielregionsangaben werden mit „mit" angebunden, nicht per Komma
**Beleg:** Z. 672 (Robert-Feedback via Nutzer), Z. 673–677.

> Nutzer: „feedback bei dem war dass ein mit vor Fokus soll wie ist der satz dann rund" (Z. 672)
> → `… plant Zukauf von zehn bis zwölf Uhrenkomponenten-Herstellern **mit** Fokus Schweiz` (Z. 675)

Das ist ein direkter Robert-Korrekturbeleg. Bestätigt in Z. 2273 („Fokus zentrale/
östliche Schweiz"), Z. 2277 („mit Fokus auf Süd- und Osteuropa").
**Wohin:** Abschnitt 7 (Textnormen-Tabelle) — `, Fokus X` → `mit Fokus X`.

### 16. Keine Parenthese in der Parenthese
**Beleg:** Z. 1410.

> „‚(Mitarbeiter Zielobjekt: 550+)' ist ein Parenthese-in-Parenthese-Konstrukt, das nach der härteren Linie raus sollte" (Z. 1410)

Robert hat den ganzen Halbsatz danach sogar komplett gestrichen (Z. 1486).
**Wohin:** Abschnitt 6.6 (Kürzungsprinzip).

### 17. Kein Komma vor „mit u.a."
**Beleg:** Z. 2165.

> „Bei ConSense steht ‚erreicht zweite Bieterrunde, mit u.a.' – das Komma vor ‚mit u.a.' ist stilistisch uneinheitlich … würde ich das Komma rausnehmen" (Z. 2165); umgesetzt Z. 2205.

**Wohin:** Abschnitt 6.5.

### 18. Bieterlisten ohne „von"
**Beleg:** Z. 4601.

> „SK Pharma nutzt ‚u.a. von Chequers Capital…' während alle anderen Bieterlisten ohne ‚von' auskommen … Für Einheitlichkeit würde ich ‚von' streichen." (Z. 4601)

**Wohin:** Abschnitt 6.5.

### 19. Grammatik: „zwischen X und Y" oder „X bis Y" — nie mischen
**Beleg:** Z. 1456.

> „‚zwischen zehn bis fünfzig' ist falsch kombiniert (entweder ‚zwischen X und Y' oder ‚X bis Y', nicht gemischt)" (Z. 1456)

**Wohin:** Abschnitt 6.2 (Zahlen) oder 7.

### 20. „avisierte Bewertung" → „Bewertung"
**Beleg:** Z. 2280 (Nutzer-Änderung, vom Assistenten bestätigt), Zeile Z. 2272.

> „‚Bewertung' statt ‚avisierte Bewertung' bei SGB-SMIT" (Z. 2280)

Fehlt in der Textnormen-Tabelle. Gleiche Kategorie: „angepeiltes Volumen"
(Z. 2270) blieb dagegen stehen.
**Wohin:** Abschnitt 7.

### 21. Dementi / Klarstellung → kein eigener Eintrag
**Beleg:** Z. 4129 (Kammerer), Z. 851–853 (Burda), Z. 6411 (Delivery Hero).

> „Kammerer Medical Group – Unternehmen hat nach Veröffentlichung explizit dementiert, dass ein Verkaufsprozess läuft → raus" (Z. 4129)
> „Burda dementiert den Verkauf … Das ist kein neuer Deal, sondern eine Klarstellung zu deinem bereits gelisteten 09.07.-Eintrag." (Z. 853)
> „Delivery Hero – Vorstandsempfehlung zum bereits gelisteten Uber-Angebot; kein neuer Sachverhalt, nur Zustimmung → Grenzfall" (Z. 6411)

Eigene Ausschlusskategorie: Dementi und reine Zustimmungs-/Bestätigungsmeldungen
ohne neuen Sachverhalt. SKILL.md Abschnitt 2 hat das nicht.
**Wohin:** Abschnitt 2.

### 22. Reine Berater-/Mandatsmeldungen ohne Prozessfortschritt → raus
**Beleg:** Z. 5963 (Nutzerfrage), Z. 5967, Z. 5973 (Nutzerentscheidung).

> Nutzer: „das ist aber ja kein deal oder?" (Z. 5963)
> „Es passiert nichts am Prozess selbst, keine neue Runde, keine neuen Zahlen – nur ein Bieter mandatiert eine Bank … würde ich das eher weglassen" (Z. 5967)
> Nutzer: „ja habve jetzt herausgelöscht" (Z. 5973)

Das ist eine **entschiedene** Nutzerentscheidung, nicht nur ein Vorschlag.
**Wohin:** Abschnitt 2.

### 23. Nebenerwähnungen in ausgeschlossenen Artikeln können eigenständig aufnahmefähig sein
**Beleg:** Z. 7564 (Warburg Pincus/Oyora im RAD-x-Refi-Artikel), Z. 6338 (L Catterton/Hyrox im Wanda-Artikel).

> „Eine Sache aus dem RAD-x-Artikel wäre aber aufnahmefähig …: Warburg Pincus hat Goldman Sachs für den Verkauf von Oyora mandatiert … Das ist nur eine Nebenerwähnung hier, aber ein eigenständiger DACH-Verkaufsprozess." (Z. 7564)

Ein Artikel kann als Ganzes ausgeschlossen sein und trotzdem einen aufnahmefähigen
Sachverhalt enthalten. Gegenprobe: ib vogt Australien/Indien wurden *nicht*
aufgenommen, weil Randnotiz (Z. 668) — also: eigenständiger Prozess mit
Berater/Zahlen ja, bloße Erwähnung nein.
**Wohin:** Abschnitt 1 oder 5.

### 24. Format der Ausschlussliste: nach Kategorie gruppiert, mit Anzahl
**Beleg:** durchgängig, u.a. Z. 1214–1230, Z. 2073–2085, Z. 2992–3005, Z. 3864–3873.

> „Ausgeschlossen (Insolvenz/Administration, 7): …", „Ausgeschlossen (Refinanzierung/Debt-Finanzierung für bereits verkündete Deals, 3): …", „Ausgeschlossen (kein DACH-Bezug, 3): …", „Grenzfälle, nicht aufgenommen: …", „Aufnahmefähig (6), chronologisch sortiert:" (Z. 2992–3005)

SKILL.md 8 zeigt eine flache Liste „Ausgeschlossen:" plus „Zum Prüfen:". Die
Begriffe „--- nicht mitkopieren ---" und „Zum Prüfen" kommen im Transkript
**nirgends** vor; die belegten Begriffe sind „Ausgeschlossen (N)",
„Aufnahmefähig (N), chronologisch sortiert" und „Grenzfall, sag Bescheid".
**Wohin:** Abschnitt 8, Block 2.

### 25. Akteur und verkaufte Sparte bekommen je eine eigene Klammer
**Beleg:** Z. 7575–7576, Z. 5273 (Webasto als Vorbild), Endstand Z. 8063.

> „Bei Webasto hast du es korrekt gemacht (Akteur und verkaufte Sparte bekommen je eine Klammer). Konsistent wäre: ‚CSN (BR, Stahlindustrie) steht vor Entscheidung über Verkauf seiner deutschen Stahlaktivitäten (DE, Langstahl/Stahlprofile), Volumen: 1,5 Mrd. BRL'" (Z. 7575/7576)
> `19.08.26: Webasto (DE, Automobilzulieferer, Umsatz: 4 Mrd. EUR) treibt Verkauf seiner verteidigungsnahen HVAC-Sparte in Polen voran (Umsatz: 16,7 Mio. EUR, EBITDA-Marge: 40%), Sell-side Berater: Rothschild` (Z. 5273)

Einschränkung: Robert hat CSN ohne Akteurs-Klammer durchgehen lassen (Z. 8063) →
erwünscht, aber nicht zwingend. Die Sparten-Klammer sollte direkt am Objekt hängen,
nicht hinter „voran" (Z. 5291, Z. 5385).
**Wohin:** Abschnitt 6.1.

### 26. Beraternamen: operative Advisory-Einheit, aber ohne Dachgesellschaft
**Beleg:** Z. 4696 (Nutzerfrage), Z. 4698–4704.

> Nutzer: „bei dem macquarie ding ist das falsch es sollte macquarie group sien oder" (Z. 4696)
> „Macquarie Capital ist genau richtig. Das ist die Investment-Banking-/Advisory-Sparte … ‚Macquarie Group' wäre die Dachgesellschaft und für ein Berater-Feld zu unspezifisch, ähnlich wie du ja auch nicht ‚Goldman Sachs Group' schreibst" (Z. 4698/4702)

Steht in Spannung zur Kurzform-Regel „Lincoln International → Lincoln"
(SKILL.md 7): Kürzen ja, aber nicht bis zur Dachgesellschaft und nicht so weit,
dass die beratende Einheit unklar wird.
**Wohin:** Abschnitt 6.3 oder 7.

### 27. Exakter Akteursname aus der Mergermarket-Relationship-Angabe
**Beleg:** Z. 4567 (Nutzer), Z. 4569–4573.

> Nutzer: „warte mal hast du gechekt hier ist es viessmann generation group der bidder und nicht viessmann heizneck" (Z. 4567)
> „bei Holdinggesellschaften mit ähnlichem Markennamen wie ein bekanntes Tochter-/Schwesterunternehmen achte ich … genauer darauf, den exakten Bidder-Namen aus der Mergermarket-Relationship-Angabe zu übernehmen statt den naheliegenderen Markennamen" (Z. 4573)

**Wohin:** Abschnitt 6.4 oder Prüfliste.

### 28. Firmennamen-Schreibweise bei uneinheitlicher Quelle
**Beleg:** Z. 575.

> „im Originalartikel wechselt die Quelle selbst zwischen ‚Vam Investment' und ‚Vam Investments' … Ich würde mich an die häufigere Schreibweise im Artikel halten" (Z. 575)

Ergänzend: Eigenschreibweisen bleiben erhalten — `blau direkt`, `autmatec`, `init`,
`pit`, `dss+`, `ib vogt`, `iMPREG`, `dormakaba`, `Kuehne+Nagel`, `Waipu.TV` stehen
alle klein/als Eigenmarke in den freigegebenen Zeilen.
**Wohin:** Abschnitt 7.

### 29. Update-Meldung innerhalb desselben Batches → bestehenden Eintrag aktualisieren
**Beleg:** Z. 1236 (BASF), Z. 2405 (Babtec), Z. 4426 (Thyssenkrupp), Z. 5987–5999 (Siemens Energy).

> „BASF-Artikel vom 17.07. ist eine Fortschreibung deines bereits gelisteten 13.07.-Eintrags … Ich würde den bestehenden Eintrag aktualisieren statt duplizieren" (Z. 1236)
> „Thyssenkrupp TK Accelis (03.08.) – inhaltlich identisch mit dem bereits aufgenommenen 07.08.-Artikel zum selben Spin-off, daher nicht doppelt gelistet" (Z. 4426)
> Siemens Energy 24.08. (Bloomberg-Gerücht) vs. 25.08. (Pressemitteilung) → Nutzer streicht eine (Z. 5991 „soll ich nicht eher den zweiten rauslassen?", Auflösung Z. 5995–5999, umgesetzt Z. 6017)

Abzugrenzen von SKILL.md 5 („Wochen später → neuer Eintrag"): **innerhalb** eines
Batches wird konsolidiert, **wochenübergreifend** neu angelegt.
**Wohin:** Abschnitt 5, als zweiter Fall.

### 30. Mergermarket-Tags „(translated)" und „Proprietary" — ohne Relevanz für Aufnahme
**Beleg:** Z. 388 (Nutzerfrage), Z. 390–394.

> „Für deine Zwecke hat das keine inhaltliche Relevanz – ändert nichts an Aufnahme/Ausschluss, ist nur ein Hinweis auf die Sprache der Originalquelle." (Z. 394)

Kleine, aber explizit gestellte Nutzerfrage; verhindert, dass ein Nachfolger daraus
ein Kriterium macht.
**Wohin:** Fußnote in Abschnitt 1 oder Glossar.

### 31. Outlook-Übergabe: Markdown-Link und Fettung
**Beleg:** Z. 6052 (Nutzer), Z. 6056, Z. 5313, Z. 5396.

> Nutzer: „kann ich eig auch links hier reinkopieren und du machst so str k verlinkte quelle die ich sofort rauskpoieren kann?" (Z. 6052)
> „Markdown wird dort nicht automatisch in einen klickbaren Link umgewandelt … Falls nicht, müsstest du in Outlook manuell verlinken (Strg+K auf ‚Quelle')." (Z. 6056)
> „In der Textfassung ist nichts fett – falls du wie sonst vor dem Versenden in Outlook formatierst, denk an die Akteursnamen (…)" (Z. 5313)

Die Fettung entsteht erst in Outlook, nicht im gelieferten Text. Das erklärt, warum
`**…**` in den versendeten Fassungen nicht auftaucht.
**Wohin:** Abschnitt 8.

---

## WIDERSPRÜCHE ZUM SKILL

| Skill sagt | Transkript sagt | Beleg | Empfehlung |
|---|---|---|---|
| 6.2: `Bewertung:` und `Deal-Value:` sind Klammer-Financials | „Die Bewertung gehört **nicht** in die Klammer, sondern bleibt … im Satz. Die Klammer ist für Land/Branche/Financials des Unternehmens …, die Deal-Bewertung ist ein Transaktionsfakt und steht nach dem Kerninhalt." | Z. 4666, bestätigt Z. 5306 („Bewertung im Satz statt Klammer (APCOA) ✓ – konsistent mit FC Bayern/SGB-SMIT"); Gegenbeleg nur die Altzeile Mammut Z. 4674 | `Bewertung:` / `Deal-Value:` aus der Klammer-Liste nehmen und als Satz-Element nach dem Kerninhalt dokumentieren; Mammut als dokumentierte Altzeile markieren |
| 6.2: `Keine Geografie, wenn das Länderkürzel sie schon trägt` | Robert kürzte `(CH, Wohnimmobilien **Deutschland**, …)` → `(CH, Wohnimmobilien, …)` — hier trug das Kürzel die Geografie gerade **nicht** | Z. 8051 | Regel verallgemeinern: **gar keine** Geografie in der Branchenbezeichnung, unabhängig vom Länderkürzel |
| 6: „Aufzählungszeichen: `•`", Prüfliste Pkt. 14 | 43 Einträge mit `•`, **491 ohne**. Alle drei Bullet-Blöcke (Z. 286–297, 2240–2252, 5353–5369) sind Nicos eigene Fassungen; die Mehrzahl der versendeten Fassungen beginnt direkt mit `TT.MM.JJ:`. `research/02` sagt sogar ausdrücklich „Zeilenanfang kein Bullet, kein Spiegelstrich" | maschinelle Auszählung; Z. 2207–2223 vs. Z. 2237–2252 | Widerspruch auflösen: entweder Bullet als optional kennzeichnen oder auf die Mehrheitsform umstellen. So wie es dasteht, widerspricht SKILL.md der eigenen Referenzdatei |
| 6.2: `ARR:` als Klammer-Label | `ARR` kommt nur im Satz vor: „Zielgröße bis 5-7 Mio. EUR ARR" | Z. 4135; 0 Treffer für `ARR:` | Aus der Klammer-Liste entfernen oder als Satz-Element markieren |
| 8: „kein Vorspann" | Jede versendete Mail hat Anrede + genau einen Einleitungssatz + „Viele Grüße / Nico" | Z. 2207–2209/2253, Z. 1346–1348 | „kein Vorspann" auf den Chat-Output beschränken, Mailrahmen separat dokumentieren (siehe Fund 1) |
| 3: „Rein … CSN/Stahlwerk Thüringen, **Matthews/Olbrich**" | Matthews/Olbrich wurde im Transkript ausdrücklich **ausgeschlossen** („da der handelnde Akteur (Matthews) nicht DACH ist … → raus") | Z. 3870 | Sachlich richtig als Endstand (`research/01` Nachtrag), aber der Beispielname suggeriert, er sei aufgenommen worden. Als „Fehlausschluss, nach neuer Regel aufnahmefähig" kennzeichnen |
| 6.5: „Nicht ‚Interessenten'" (Abweichung nur in Abschnitt 10 vermerkt) | `Interessenten u.a.` 15×, `im Rennen u.a.` 14×, `Wettbewerber u.a.` 3× — gegenüber `Bieter u.a.` 21× und `mit u.a.` 25× | maschinelle Auszählung | Die Varianten sind zu häufig für „Abweichung". Besser als zulässige Alternativen mit Anwendungsfall dokumentieren (`im Rennen` bei laufendem Prozess ohne Rundenbezug) |
| 7: „`bereinigtes EBITDA` → `Adj. EBITDA`" als durchgesetzte Norm | 20× `bereinigtes EBITDA`, 2× `Adj. EBITDA` im gesamten Transkript. Die Anordnung kam erst ganz am Ende | Z. 8070 („immer adj. ebtida anstelle breinigtes"), Zählung | Korrekt als Endstand, aber in Abschnitt 10 ist die Größenordnung (20:2) untertrieben dargestellt |

---

## ECHTE UNKLARHEITEN (Nutzer muss entscheiden)

1. **Woher kommen die Artikel konkret?** Das Transkript zeigt nur: der Nutzer kippt
   Artikeltexte + separate Content-Links batchweise ein (Z. 59 „Schick mir die
   Rohartikel oder den Mergermarket-Export"). Ein Suchfilter, eine gespeicherte
   Suche, ein Alert oder ein Newsletter wird **nirgends** beschrieben. Der einzige
   Filter-artige Hinweis ist ein Artefakt einer kopierten Artikelseite:
   `Topic: [Family O](https://mergermarket.ionanalytics.com/?newsTopicId=226)` (Z. 6179/6180)
   — das ist ein Topic-Tag des Artikels, keine Suchdefinition. **Offen: welcher
   Mergermarket-Filter/Screen liefert den Wochenbatch?**

2. **Zeitraum.** Nur „oich mache montags immer merger market briefing über die letzte
   woiche" (Z. 37). Kein Mo–So, kein „seit dem letzten Briefing". In der Praxis
   ergibt sich der Zeitraum aus dem gelieferten Batch — und der ist nicht immer eine
   Woche: das letzte Briefing umfasst „38 Einträge vom 01.09. bis 14.09." (Z. 8030),
   also zwei Wochen. Feiertage/verlängerte Zeiträume kommen nie vor. Die neue
   SKILL.md-Regel „Keine Zeitraumabgrenzung" ist damit belegkonform — aber der
   Nutzer sollte bestätigen, dass es keine Nachzügler-Regel gibt.

3. **Bullet ja oder nein** (siehe Widerspruchstabelle). Belege für beides, SKILL.md
   und `research/02` sagen Gegenteiliges.

4. **Ausschlussquote mitliefern?** Angeboten in Z. 1684 („Willst du, dass ich
   zukünftig kurz die Ausschlussquote mit angebe…"), nie beantwortet. In der Praxis
   wird faktisch immer eine Zahl genannt („Ausgeschlossen (5)", „Aufnahmefähig (7)").

5. **`Global-Coordinator-Kandidaten:` gültig oder nicht?** Das Label wurde benutzt
   (Z. 3011/3043), aber in derselben Sachlage hat Robert den Nicht-fix-Hinweis
   gestrichen („Mandate an Deutsche Bank und Goldman Sachs noch nicht fix" raus,
   Z. 1380). Unklar, ob das Label überlebt oder ob noch nicht mandatierte Banken
   ganz wegfallen.

6. **`Buy-side Berater:`** — das Label existiert (Z. 5957), aber genau dieser Eintrag
   wurde vom Nutzer wieder gelöscht (Z. 5973). Es gibt also kein freigegebenes
   Beispiel. Soll das Label im Skill stehen?

7. **Asset-/Standortverkäufe und Reverse-Merger** — in `research/01` als
   „tendenziell rein, dann flaggen" aufgelöst, aber im Transkript selbst nie
   entschieden (Lenzing raus Z. 3004, Webasto-Werk Polen rein Z. 5079, Milton
   Capital/Apostrophy offen Z. 6854/6896). ARLANXEO zweimal vorgelegt (Z. 7509,
   7832), nie beantwortet. Quarkwerk dreimal vorgelegt (Z. 7511, 7962, 8035), nie
   beantwortet.

8. **Sekundärsortierung innerhalb eines Tages** — ausdrücklich offen (Z. 30, Z. 520).

---

## GEPRÜFT UND BEREITS ABGEDECKT

Diese Punkte habe ich im Transkript gefunden und gegen SKILL.md geprüft — sie sind
**drin**, ich melde sie nicht als Lücke:

- Insolvenz/Eigenverwaltung/Schutzschirm/Nachlassstundung als härtester Filter
  (~60 Einzelfälle im Transkript) — Abschnitt 2 ✓
- Startup-Runden, PE-Fundraising, Refinanzierungen, Buyout-Finanzierungen für
  bereits verkündete Deals, syndizierte Kredite, Debt-for-Equity (Z. 489) — Abschnitt 2 ✓
- Abgeschlossene Deals; Ausnahme Rückzug/Verschiebung (Naxicap Z. 54, Frostkrone Z. 872) — Abschnitt 1/2 ✓
- Aktien-Distribution an Altaktionäre (Siemens/Healthineers Z. 2681/2699) — Abschnitt 2 ✓
- Interne Restrukturierung ohne M&A-Bezug (Badischer Winzerkeller Z. 1320) — Abschnitt 2 ✓
- Marktkommentar/Podcast/Personalien/Fondsstrategie (Z. 849, 4424, 6858) — Abschnitt 2 ✓
- Nicht-DACH mit DACH-Präsenz rein; Nutzeranweisung Z. 4546 — Abschnitt 3 ✓
- „Europa ja, außereuropäisch nein" (Sonova Z. 6859 vs. Kuehne+Nagel Z. 5351) — Abschnitt 3 ✓
- Vagheits-Schwelle inkl. BASF-Korrektur (Z. 3152–3165) — Abschnitt 4 ✓
- Doppelmeldung Wochen später = neuer Eintrag, Nutzeranweisung Z. 3890 — Abschnitt 5 ✓
- Datum aus dem Artikel-Timestamp; vier Datumsfehler in einer Session (Z. 2095–2135) — Abschnitt 6 + Prüfliste ✓
- Klammer beim grammatischen Subjekt; Investor-als-Subjekt (Nutzerkorrektur Z. 4636) — Abschnitt 6.1 ✓
- „via/über Plattform" nur bei Zukäufen (Z. 4646/4650) — Abschnitt 6.1/7.1 ✓
- Originalwährung, keine Umrechnung (Nutzerfrage Z. 546, Antwort Z. 550) — Abschnitt 6.2 ✓
- Ziffern bei Finanzbeträgen, Zahlwörter bei kleinen Stückzahlen (Z. 1495–1497) — Abschnitt 6.2 ✓
- Branche großgeschrieben, knapp (Z. 8050–8055) — Abschnitt 6.2 ✓
- Berater nur wenn im Artikel, nie fett (Nutzerfrage Z. 535, Anweisung Z. 3117) — Abschnitt 6.3/6.4 ✓
- „immer Sell-side Berater" statt bloß „Berater" (Nutzeranweisung Z. 3019) — Abschnitt 6.3 ✓
- Alle Akteursnamen fett (Nutzeranweisung Z. 3117, Rückfrage Z. 3133) — Abschnitt 6.4 ✓
- `Bieter u.a.` / `mit u.a.` je nach Satz (Z. 1546) — Abschnitt 6.5 ✓
- Nicht stapeln: Bieternamen + Deal-Value (Babtec Z. 1489) — Abschnitt 6.5 ✓
- Timing-Nachsätze, Motivation, Historie, Börsensegmente streichen (Z. 87–93, 4623–4628) — Abschnitt 6.6 ✓
- Attribution streichen, außer die Aussage ist die Nachricht (Z. 4769) — Abschnitt 6.6 ✓
- Stake-Prozente als Nachsatz streichen (Moin Group Z. 1374) — Abschnitt 6.6 ✓
- „laufenden"/„im Bereich" als Füllwörter (Z. 1382, 1420) — Abschnitt 6.6 ✓
- IPO statt Börsengang, DE statt Deutschland, Adj. EBITDA, Lincoln, i.H.v., Aktiv
  statt Passiv, Rechtsform weg, `<20 Mio.` (Nutzeranweisung Z. 8070, Diff Z. 8041–8055) — Abschnitt 7 ✓
- Roberts härtere Kürzungslinie als Grundhaltung (Z. 1384, 1484) — Abschnitt 7.2 ✓
- Keine Untergrenze für die Dealgröße — Abschnitt 1 ✓
- Keine externe Recherche / keine Beschaffung / keine Zeitraumabgrenzung — neu
  ergänzter Kopfabschnitt ✓ (nur die Zahl-Auswahl-Nuancen fehlen, siehe Funde 4–6)
